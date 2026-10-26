"""
Proxy module exposing financial modeling tools for Python package resolution.
"""
import sys
import os

pkg_dir = os.path.join(os.path.dirname(__file__), "..", "financial-modeling")
if pkg_dir not in sys.path:
    sys.path.insert(0, os.path.abspath(pkg_dir))

from calculator import (  # noqa: F401
    FranchiseFinancialEngine,
    ProductPricing,
    RevenueSharingRule,
    FranchiseeCapEx,
    FranchiseeMonthlyOpEx,
    MonthlyProjection,
    to_decimal,
    quantize_money
)
from excel_generator import FranchiseExcelGenerator  # noqa: F401
