"""
Financial Modeling Calculation Engine
=====================================
Client-independent, industry-agnostic, decimal-safe financial calculation library
for franchise unit economics, revenue sharing, break-even, cash flow, and ROI.
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


def to_decimal(val: Any) -> Decimal:
    """Safely convert any numeric/string value to Decimal."""
    if isinstance(val, Decimal):
        return val
    return Decimal(str(val))


def quantize_money(val: Decimal, precision: str = "0.01") -> Decimal:
    """Quantize to currency precision using standard ROUND_HALF_UP."""
    return val.quantize(Decimal(precision), rounding=ROUND_HALF_UP)


@dataclass
class ProductPricing:
    product_id: str
    name: str
    price_net: Decimal
    implementation_fee_net: Decimal = Decimal("0.00")
    annual_renewal_net: Decimal = Decimal("0.00")
    currency: str = "INR"


@dataclass
class RevenueSharingRule:
    franchisee_share_percent: Decimal  # e.g., Decimal("40.0")
    franchisor_share_percent: Decimal  # e.g., Decimal("60.0")
    deduct_third_party_infra: bool = False


@dataclass
class FranchiseeCapEx:
    office_setup_deposit: Decimal
    interior_and_signage: Decimal
    hardware_and_networking: Decimal
    miscellaneous_setup: Decimal = Decimal("0.00")

    @property
    def total_capex(self) -> Decimal:
        return (
            self.office_setup_deposit
            + self.interior_and_signage
            + self.hardware_and_networking
            + self.miscellaneous_setup
        )


@dataclass
class FranchiseeMonthlyOpEx:
    office_rent: Decimal
    salesperson_salary: Decimal
    utilities_and_internet: Decimal
    local_travel_and_marketing: Decimal = Decimal("0.00")
    accounting_and_admin: Decimal = Decimal("0.00")

    @property
    def total_fixed_monthly_opex(self) -> Decimal:
        return (
            self.office_rent
            + self.salesperson_salary
            + self.utilities_and_internet
            + self.local_travel_and_marketing
            + self.accounting_and_admin
        )


@dataclass
class MonthlyProjection:
    month: int
    new_units_sold: int
    active_renewing_units: int
    gross_customer_billings: Decimal
    tax_collected: Decimal
    net_revenue: Decimal
    franchisee_gross_commission: Decimal
    franchisor_retained_revenue: Decimal
    franchisee_monthly_opex: Decimal
    franchisee_ebitda: Decimal
    franchisee_cumulative_cash_flow: Decimal
    franchisor_ebitda: Decimal


class FranchiseFinancialEngine:
    """
    Core calculation engine for franchise economics.
    Configurable for any client, currency, tax structure, and product portfolio.
    """

    def __init__(
        self,
        products: List[ProductPricing],
        joining_fee_per_product: Decimal,
        capex: FranchiseeCapEx,
        monthly_opex: FranchiseeMonthlyOpEx,
        revenue_share: RevenueSharingRule,
        renewal_share: Optional[RevenueSharingRule] = None,
        implementation_share: Optional[RevenueSharingRule] = None,
        tax_rate_percent: Decimal = Decimal("18.0"),
        working_capital_months: int = 4,
        currency: str = "INR"
    ):
        self.products = {p.product_id: p for p in products}
        self.joining_fee_per_product = to_decimal(joining_fee_per_product)
        self.capex = capex
        self.monthly_opex = monthly_opex
        self.revenue_share = revenue_share
        self.renewal_share = renewal_share or revenue_share
        self.implementation_share = implementation_share or RevenueSharingRule(
            franchisee_share_percent=Decimal("20.0"),
            franchisor_share_percent=Decimal("80.0")
        )
        self.tax_rate_percent = to_decimal(tax_rate_percent)
        self.working_capital_months = working_capital_months
        self.currency = currency

    def calculate_total_joining_fee(self, product_ids: Optional[List[str]] = None) -> Decimal:
        """Calculate upfront joining fee across selected products."""
        num_products = len(product_ids) if product_ids else len(self.products)
        return quantize_money(self.joining_fee_per_product * Decimal(num_products))

    def calculate_working_capital_reserve(self) -> Decimal:
        """Calculate mandatory working capital reserve for fixed runway."""
        return quantize_money(
            self.monthly_opex.total_fixed_monthly_opex * Decimal(self.working_capital_months)
        )

    def calculate_total_initial_investment(self, product_ids: Optional[List[str]] = None) -> Decimal:
        """Total capital outlay = Joining Fee + CapEx + Working Capital Reserve."""
        joining = self.calculate_total_joining_fee(product_ids)
        capex = self.capex.total_capex
        working_cap = self.calculate_working_capital_reserve()
        return quantize_money(joining + capex + working_cap)

    def calculate_split(
        self,
        net_amount: Decimal,
        rule: RevenueSharingRule
    ) -> Dict[str, Decimal]:
        """Split a net revenue amount into franchisee and franchisor portions."""
        net = to_decimal(net_amount)
        fee_portion = quantize_money(net * (rule.franchisee_share_percent / Decimal("100.0")))
        sor_portion = quantize_money(net - fee_portion)
        return {
            "franchisee": fee_portion,
            "franchisor": sor_portion
        }

    def calculate_break_even_units(
        self,
        average_product_price_net: Optional[Decimal] = None
    ) -> Decimal:
        """
        Calculate monthly product units required to break even against monthly fixed OpEx.
        Formula: Fixed OpEx / (Avg Price * Franchisee Share %)
        """
        if average_product_price_net is None:
            if not self.products:
                return Decimal("0.00")
            avg_price = sum(p.price_net for p in self.products.values()) / Decimal(len(self.products))
        else:
            avg_price = to_decimal(average_product_price_net)

        franchisee_commission_per_unit = avg_price * (self.revenue_share.franchisee_share_percent / Decimal("100.0"))
        if franchisee_commission_per_unit <= Decimal("0"):
            return Decimal("Infinity")

        be_units = self.monthly_opex.total_fixed_monthly_opex / franchisee_commission_per_unit
        return quantize_money(be_units, "0.01")

    def run_projection(
        self,
        monthly_sales_velocity: Decimal,
        annual_renewal_rate_percent: Decimal = Decimal("85.0"),
        months: int = 36,
        ramp_up_months: int = 3,
        product_mix_weights: Optional[Dict[str, Decimal]] = None,
        franchisor_monthly_central_cost_per_unit: Decimal = Decimal("5000.00")
    ) -> List[MonthlyProjection]:
        """
        Generate month-by-month multi-year financial projection.
        Includes sales ramp-up, renewals compounding, and cash flows.
        """
        projections: List[MonthlyProjection] = []
        cumulative_cash_flow = -self.calculate_total_initial_investment()
        active_customer_cohort: List[int] = []  # tracks new sales by month

        # Default equal weighting across products if not specified
        if not product_mix_weights:
            weight = Decimal("1.0") / Decimal(len(self.products)) if self.products else Decimal("1.0")
            weights = {p_id: weight for p_id in self.products}
        else:
            weights = product_mix_weights

        # Average blended product price
        blended_price = sum(
            self.products[p_id].price_net * weights.get(p_id, Decimal("0.0"))
            for p_id in self.products
        )
        blended_renewal = sum(
            self.products[p_id].annual_renewal_net * weights.get(p_id, Decimal("0.0"))
            for p_id in self.products
        )

        tax_mult = self.tax_rate_percent / Decimal("100.0")

        for m in range(1, months + 1):
            # Ramp-up factor: linear progression from 33% to 100% over ramp_up_months
            if m <= ramp_up_months:
                ramp_factor = Decimal(m) / Decimal(ramp_up_months)
            else:
                ramp_factor = Decimal("1.0")

            expected_sales = monthly_sales_velocity * ramp_factor
            units_sold = int(quantize_money(expected_sales, "1"))
            active_customer_cohort.append(units_sold)

            # Renewals trigger every 12 months for cohort that started 12, 24 months ago
            renewing_units = 0
            if m > 12:
                past_cohort = active_customer_cohort[m - 13]
                retention_rate = annual_renewal_rate_percent / Decimal("100.0")
                renewing_units = int(quantize_money(Decimal(past_cohort) * retention_rate, "1"))

            # Calculate revenues
            new_license_net = quantize_money(Decimal(units_sold) * blended_price)
            renewal_net = quantize_money(Decimal(renewing_units) * blended_renewal)
            total_net = new_license_net + renewal_net

            tax_collected = quantize_money(total_net * tax_mult)
            gross_billings = total_net + tax_collected

            # Split revenues
            new_split = self.calculate_split(new_license_net, self.revenue_share)
            renewal_split = self.calculate_split(renewal_net, self.renewal_share)

            franchisee_comm = new_split["franchisee"] + renewal_split["franchisee"]
            franchisor_rev = new_split["franchisor"] + renewal_split["franchisor"]

            # Monthly OpEx & EBITDA
            monthly_opex = self.monthly_opex.total_fixed_monthly_opex
            franchisee_ebitda = franchisee_comm - monthly_opex
            cumulative_cash_flow += franchisee_ebitda

            franchisor_ebitda = franchisor_rev - franchisor_monthly_central_cost_per_unit

            proj = MonthlyProjection(
                month=m,
                new_units_sold=units_sold,
                active_renewing_units=renewing_units,
                gross_customer_billings=gross_billings,
                tax_collected=tax_collected,
                net_revenue=total_net,
                franchisee_gross_commission=franchisee_comm,
                franchisor_retained_revenue=franchisor_rev,
                franchisee_monthly_opex=monthly_opex,
                franchisee_ebitda=franchisee_ebitda,
                franchisee_cumulative_cash_flow=cumulative_cash_flow,
                franchisor_ebitda=franchisor_ebitda
            )
            projections.append(proj)

        return projections

    def calculate_payback_and_roi(
        self,
        projections: List[MonthlyProjection]
    ) -> Dict[str, Any]:
        """Compute exact payback month and 36-month ROI."""
        initial_inv = self.calculate_total_initial_investment()
        payback_month: Optional[int] = None

        total_ebitda = sum(p.franchisee_ebitda for p in projections)

        for p in projections:
            if p.franchisee_cumulative_cash_flow >= Decimal("0.00"):
                payback_month = p.month
                break

        net_profit_36 = total_ebitda - initial_inv
        roi_percent = Decimal("0.00")
        if initial_inv > Decimal("0"):
            roi_percent = quantize_money((net_profit_36 / initial_inv) * Decimal("100.0"))

        return {
            "initial_investment": initial_inv,
            "payback_month": payback_month,
            "total_36m_ebitda": quantize_money(total_ebitda),
            "net_36m_profit": quantize_money(net_profit_36),
            "roi_percent": roi_percent
        }
