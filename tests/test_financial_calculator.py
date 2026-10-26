"""
Unit Tests for Financial Modeling Engine
========================================
Validates Decimal precision, revenue sharing arithmetic, break-even formulas,
churn compounding, and edge-case boundary conditions.
"""

import pytest
from decimal import Decimal
import sys
import os

pkg_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tools", "financial-modeling"))
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

from calculator import (
    FranchiseFinancialEngine,
    ProductPricing,
    RevenueSharingRule,
    FranchiseeCapEx,
    FranchiseeMonthlyOpEx,
    to_decimal,
    quantize_money
)


@pytest.fixture
def sample_engine():
    products = [
        ProductPricing(
            product_id="prd-erp",
            name="School ERP",
            price_net=Decimal("60000.00"),
            annual_renewal_net=Decimal("15000.00")
        ),
        ProductPricing(
            product_id="prd-inv",
            name="Invoicing App",
            price_net=Decimal("12000.00"),
            annual_renewal_net=Decimal("3600.00")
        )
    ]
    capex = FranchiseeCapEx(
        office_setup_deposit=Decimal("36000.00"),
        interior_and_signage=Decimal("35000.00"),
        hardware_and_networking=Decimal("45000.00"),
        miscellaneous_setup=Decimal("10000.00")
    )
    monthly_opex = FranchiseeMonthlyOpEx(
        office_rent=Decimal("12000.00"),
        salesperson_salary=Decimal("18000.00"),
        utilities_and_internet=Decimal("3000.00"),
        local_travel_and_marketing=Decimal("3500.00"),
        accounting_and_admin=Decimal("1500.00")
    )
    rev_share = RevenueSharingRule(
        franchisee_share_percent=Decimal("40.0"),
        franchisor_share_percent=Decimal("60.0")
    )
    return FranchiseFinancialEngine(
        products=products,
        joining_fee_per_product=Decimal("25000.00"),
        capex=capex,
        monthly_opex=monthly_opex,
        revenue_share=rev_share,
        tax_rate_percent=Decimal("18.0"),
        working_capital_months=4
    )


def test_decimal_safety_and_quantization():
    val = Decimal("100.005")
    quantized = quantize_money(val)
    assert quantized == Decimal("100.01")
    assert isinstance(quantized, Decimal)


def test_initial_investment_calculation(sample_engine):
    # 2 products * 25k = 50k joining fee
    joining = sample_engine.calculate_total_joining_fee()
    assert joining == Decimal("50000.00")

    # CapEx = 36k + 35k + 45k + 10k = 126k
    capex = sample_engine.capex.total_capex
    assert capex == Decimal("126000.00")

    # Monthly fixed OpEx = 12k + 18k + 3k + 3.5k + 1.5k = 38k
    assert sample_engine.monthly_opex.total_fixed_monthly_opex == Decimal("38000.00")

    # Working capital 4 months = 38k * 4 = 152k
    wc = sample_engine.calculate_working_capital_reserve()
    assert wc == Decimal("152000.00")

    # Total = 50k + 126k + 152k = 328k
    total = sample_engine.calculate_total_initial_investment()
    assert total == Decimal("328000.00")


def test_revenue_split_exact_sum(sample_engine):
    net_amount = Decimal("60000.00")
    split = sample_engine.calculate_split(net_amount, sample_engine.revenue_share)
    assert split["franchisee"] == Decimal("24000.00")
    assert split["franchisor"] == Decimal("36000.00")
    assert split["franchisee"] + split["franchisor"] == net_amount


def test_break_even_units(sample_engine):
    # Blended price across 60k and 12k is 36k
    # 40% commission on 36k is 14.4k
    # Break-even = 38,000 / 14,400 = 2.64 units
    be_units = sample_engine.calculate_break_even_units()
    assert be_units == Decimal("2.64")


def test_36_month_projection_and_payback(sample_engine):
    projections = sample_engine.run_projection(
        monthly_sales_velocity=Decimal("4.0"),
        annual_renewal_rate_percent=Decimal("85.0"),
        months=36,
        ramp_up_months=3
    )
    assert len(projections) == 36
    # Month 1 ramp: 4.0 * (1/3) = 1.33 -> 1 unit
    assert projections[0].new_units_sold == 1
    # Month 12: Renewals should still be 0 (renewals start Month 13)
    assert projections[11].active_renewing_units == 0
    # Month 13: Renewals should reflect Month 1 cohort (1 unit * 85% = 1 unit)
    assert projections[12].active_renewing_units == 1

    metrics = sample_engine.calculate_payback_and_roi(projections)
    assert metrics["payback_month"] is not None
    assert metrics["payback_month"] <= 36
    assert metrics["roi_percent"] > Decimal("0")


def test_zero_sales_velocity_drawdown(sample_engine):
    """Stress test: under 0 sales, cumulative cash flow burns working capital."""
    projections = sample_engine.run_projection(
        monthly_sales_velocity=Decimal("0.0"),
        annual_renewal_rate_percent=Decimal("85.0"),
        months=6
    )
    assert all(p.new_units_sold == 0 for p in projections)
    assert all(p.franchisee_ebitda == -Decimal("38000.00") for p in projections)
