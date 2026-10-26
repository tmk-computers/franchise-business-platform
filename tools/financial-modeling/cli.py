"""
Financial Modeling CLI Utility
==============================
Command line interface to calculate projections, evaluate scenarios,
and generate dynamic Excel workbooks for any client workspace.
"""

import argparse
import json
import os
import sys
from decimal import Decimal
from typing import Dict, Any

import argparse
import json
import os
import sys
from decimal import Decimal
from typing import Dict, Any

# Ensure stdout supports UTF-8 on Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# Ensure local directory is on sys.path for direct execution
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

repo_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

try:
    from tools.financial_modeling.calculator import (
        FranchiseFinancialEngine,
        ProductPricing,
        RevenueSharingRule,
        FranchiseeCapEx,
        FranchiseeMonthlyOpEx,
        quantize_money
    )
    from tools.financial_modeling.excel_generator import FranchiseExcelGenerator
except ImportError:
    from calculator import (
        FranchiseFinancialEngine,
        ProductPricing,
        RevenueSharingRule,
        FranchiseeCapEx,
        FranchiseeMonthlyOpEx,
        quantize_money
    )
    from excel_generator import FranchiseExcelGenerator



def load_client_data(client_slug: str, base_dir: str = ".") -> Dict[str, Any]:
    """Load client catalog and assumptions from client workspace."""
    client_dir = os.path.join(base_dir, "clients", client_slug)
    if not os.path.exists(client_dir):
        raise FileNotFoundError(f"Client directory not found: {client_dir}")

    # Load product catalog
    catalog_path = os.path.join(client_dir, "products", "products-catalog.json")
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    # Load assumptions
    assumptions_path = os.path.join(client_dir, "financial-models", "assumptions.json")
    with open(assumptions_path, "r", encoding="utf-8") as f:
        assumptions = json.load(f)

    # Load revenue sharing
    revenue_sharing_path = os.path.join(client_dir, "franchise-model", "revenue-sharing-config.json")
    with open(revenue_sharing_path, "r", encoding="utf-8") as f:
        rev_share = json.load(f)

    return {
        "catalog": catalog,
        "assumptions": assumptions,
        "revenue_sharing": rev_share
    }


def build_engine(data: Dict[str, Any], promo_fee: bool = True) -> FranchiseFinancialEngine:
    """Instantiate the financial calculation engine from client JSON data."""
    catalog = data["catalog"]
    assumptions = data["assumptions"]
    rev_share = data["revenue_sharing"]

    products = [
        ProductPricing(
            product_id=p["productId"],
            name=p["name"],
            price_net=Decimal(str(p["indicativePriceNet"])),
            implementation_fee_net=Decimal(str(p.get("implementationFeeNet", 0))),
            annual_renewal_net=Decimal(str(p.get("estimatedAnnualRenewalNet", 0))),
            currency=p.get("currency", "INR")
        )
        for p in catalog["products"]
    ]

    capex_data = assumptions["franchiseeCapEx"]
    capex = FranchiseeCapEx(
        office_setup_deposit=Decimal(str(capex_data["officeSetupDeposit"])),
        interior_and_signage=Decimal(str(capex_data["interiorAndSignage"])),
        hardware_and_networking=Decimal(str(capex_data["hardwareAndNetworking"])),
        miscellaneous_setup=Decimal(str(capex_data.get("miscellaneousSetup", 0)))
    )

    opex_data = assumptions["franchiseeMonthlyOpEx"]
    monthly_opex = FranchiseeMonthlyOpEx(
        office_rent=Decimal(str(opex_data["officeRent"])),
        salesperson_salary=Decimal(str(opex_data["salespersonSalary"])),
        utilities_and_internet=Decimal(str(opex_data["utilitiesAndInternet"])),
        local_travel_and_marketing=Decimal(str(opex_data.get("localTravelAndMarketing", 0))),
        accounting_and_admin=Decimal(str(opex_data.get("accountingAndAdmin", 0)))
    )

    fee_tier = 25000 if promo_fee else 50000

    def_rules = rev_share["defaultRules"]
    lic_split = RevenueSharingRule(
        franchisee_share_percent=Decimal(str(def_rules["newSoftwareLicense"]["franchiseeSharePercent"])),
        franchisor_share_percent=Decimal(str(def_rules["newSoftwareLicense"]["franchisorSharePercent"]))
    )
    ren_split = RevenueSharingRule(
        franchisee_share_percent=Decimal(str(def_rules["annualRenewal"]["franchiseeSharePercent"])),
        franchisor_share_percent=Decimal(str(def_rules["annualRenewal"]["franchisorSharePercent"]))
    )

    return FranchiseFinancialEngine(
        products=products,
        joining_fee_per_product=Decimal(str(fee_tier)),
        capex=capex,
        monthly_opex=monthly_opex,
        revenue_share=lic_split,
        renewal_share=ren_split,
        tax_rate_percent=Decimal(str(assumptions.get("taxRatePercent", 18))),
        currency=assumptions.get("currency", "INR")
    )


def main():
    parser = argparse.ArgumentParser(description="Franchise Financial Modeling CLI")
    parser.add_argument("--client", default="tmk-it-solutions", help="Client workspace slug")
    parser.add_argument("--scenario", default="base", choices=["conservative", "base", "optimistic"], help="Scenario to run")
    parser.add_argument("--generate-excel", action="store_true", help="Generate Excel workbook")
    parser.add_argument("--output-dir", default=None, help="Output directory")

    args = parser.parse_args()

    client_slug = args.client
    base_dir = "."
    output_dir = args.output_dir or os.path.join(base_dir, "clients", client_slug, "financial-models")

    print(f"Loading data for client '{client_slug}'...")
    data = load_client_data(client_slug, base_dir)
    engine = build_engine(data)

    scenario_config = data["assumptions"]["scenarios"][args.scenario]
    velocity = Decimal(str(scenario_config["monthlyUnitSalesVelocity"]))
    renewal_rate = Decimal(str(scenario_config["annualRenewalRatePercent"]))
    ramp_months = scenario_config["rampUpMonths"]

    print(f"\n--- Running Scenario: {args.scenario.upper()} ---")
    print(f"Sales Velocity: {velocity} units/month | Renewal Rate: {renewal_rate}% | Ramp: {ramp_months} months")

    projections = engine.run_projection(
        monthly_sales_velocity=velocity,
        annual_renewal_rate_percent=renewal_rate,
        months=36,
        ramp_up_months=ramp_months
    )

    metrics = engine.calculate_payback_and_roi(projections)
    be_units = engine.calculate_break_even_units()

    print(f"Total Initial Investment:  ₹{metrics['initial_investment']:,.2f}")
    print(f"Monthly Break-Even Units:  {be_units} units / month")
    print(f"Payback Period:            Month {metrics['payback_month'] if metrics['payback_month'] else 'N/A'}")
    print(f"36-Month Total EBITDA:     ₹{metrics['total_36m_ebitda']:,.2f}")
    print(f"36-Month Net Profit:       ₹{metrics['net_36m_profit']:,.2f}")
    print(f"36-Month ROI:              {metrics['roi_percent']}%")

    if args.generate_excel:
        excel_path = os.path.join(output_dir, f"{client_slug.replace('-', '_')}_franchise_financial_model.xlsx")
        print(f"\nGenerating Excel workbook: {excel_path}...")
        client_name = data.get("client", {}).get("legalName", "TMK IT Solutions LLP")
        generator = FranchiseExcelGenerator(client_name=client_name)
        generator.generate(excel_path)
        print("Excel workbook generated successfully with 10 formula-linked sheets!")


if __name__ == "__main__":
    main()
