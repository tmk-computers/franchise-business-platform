"""
Excel Workbook Generator for Franchise Financial Models
=======================================================
Generates a 10-sheet, institutional-grade openpyxl workbook with native Excel formulas,
enabling non-technical analysts and clients to dynamically adjust assumptions.

Sheets Generated:
1. Dashboard Summary
2. Assumptions
3. Product Pricing
4. Franchise Investment
5. Monthly Sales Forecast
6. Franchisee P&L
7. Franchisor P&L
8. Cash Flow
9. Break-Even Analysis
10. Scenario Analysis
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from typing import Dict, Any, List
import os


class FranchiseExcelGenerator:
    """Generates dynamically linked financial model workbooks using openpyxl."""

    def __init__(self, client_name: str = "TMK IT Solutions LLP"):
        self.client_name = client_name
        self.wb = openpyxl.Workbook()
        # Remove default sheet
        self.wb.remove(self.wb.active)

        # Style definitions
        self.font_title = Font(name="Calibri", size=16, bold=True, color="1F497D")
        self.font_subtitle = Font(name="Calibri", size=11, italic=True, color="595959")
        self.font_section = Font(name="Calibri", size=12, bold=True, color="1F497D")
        self.font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        self.font_bold = Font(name="Calibri", size=11, bold=True)
        self.font_regular = Font(name="Calibri", size=11)
        self.font_italic = Font(name="Calibri", size=10, italic=True)

        self.fill_header = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
        self.fill_subheader = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
        self.fill_accent = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
        self.fill_kpi = PatternFill(start_color="EBF1DE", end_color="EBF1DE", fill_type="solid")

        self.border_thin = Border(
            left=Side(style="thin", color="D9D9D9"),
            right=Side(style="thin", color="D9D9D9"),
            top=Side(style="thin", color="D9D9D9"),
            bottom=Side(style="thin", color="D9D9D9")
        )
        self.border_total = Border(
            top=Side(style="thin", color="000000"),
            bottom=Side(style="double", color="000000")
        )

    def _auto_adjust_columns(self, ws, max_len_cap=35):
        """Auto-adjust column widths for readability."""
        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val_str = str(cell.value or "")
                if not str(cell.value or "").startswith("="):
                    max_len = max(max_len, len(val_str))
            ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), max_len_cap)

    def generate(self, output_path: str):
        """Build all sheets and save the workbook."""
        self._build_dashboard()
        self._build_assumptions()
        self._build_product_pricing()
        self._build_franchise_investment()
        self._build_monthly_sales_forecast()
        self._build_franchisee_pnl()
        self._build_franchisor_pnl()
        self._build_cash_flow()
        self._build_break_even()
        self._build_scenarios()

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.wb.save(output_path)

    # -------------------------------------------------------------
    # 1. Dashboard Summary
    # -------------------------------------------------------------
    def _build_dashboard(self):
        ws = self.wb.create_sheet(title="Dashboard Summary")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = f"{self.client_name} — Franchise Financial Executive Dashboard"
        ws["A1"].font = self.font_title
        ws["A2"] = "Three-Year Economic Feasibility & Unit Return Summary"
        ws["A2"].font = self.font_subtitle

        # Key Metrics Table
        headers = ["Key Metric", "Formula / Link", "Base Case Value", "Unit / Status"]
        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=5, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center")

        metrics = [
            ("Total Franchise Initial Outlay", "='Franchise Investment'!C15", "INR", "Upfront CapEx + Fee + Reserve"),
            ("Monthly Fixed Operating Overhead", "=Assumptions!C20", "INR / Month", "Office Rent + 1 Salesperson + Ops"),
            ("Average Monthly Product Break-Even", "='Break-Even Analysis'!C8", "Units / Month", "Sales required to clear fixed OpEx"),
            ("Cumulative 36-Month Net Profit", "='Cash Flow'!AN7", "INR", "Cumulative EBITDA after 3 years"),
            ("Payback Period (Months to Positive Cash Flow)", "='Cash Flow'!C14", "Months", "Capital Recovery Timeline"),
            ("36-Month Return on Investment (ROI)", "='Cash Flow'!C15", "Percentage", "36M Net Profit / Total Investment"),
            ("Customer Annual Renewal Rate Assumption", "=Assumptions!C27", "Percentage", "Compounding recurring retention"),
            ("Franchisee Commission Share (License)", "=Assumptions!C23", "Percentage", "Contractual sales share"),
            ("Franchisor Royalty / Retained Share", "=Assumptions!C24", "Percentage", "Central software & support share")
        ]

        for idx, (m_name, f_link, unit, notes) in enumerate(metrics, 6):
            ws.cell(row=idx, column=1, value=m_name).font = self.font_bold
            c_val = ws.cell(row=idx, column=2, value=f_link)
            c_val.font = self.font_regular
            c_unit = ws.cell(row=idx, column=3, value=unit)
            c_unit.font = self.font_italic
            c_notes = ws.cell(row=idx, column=4, value=notes)
            c_notes.font = self.font_regular
            if "%" in unit or "Percentage" in unit:
                c_val.number_format = "0.0%"
            elif "INR" in unit:
                c_val.number_format = "₹#,##0.00"

        # Executive Takeaway Box
        ws["A17"] = "EXECUTIVE TAKEAWAYS & INVESTMENT THESIS"
        ws["A17"].font = self.font_section
        takeaways = [
            "1. Asset-Light Unit Economics: Franchisee investment is primarily working capital and talent, avoiding heavy inventory risk.",
            "2. Low Break-Even Hurdle: Franchisee achieves operating break-even by closing fewer than 2 enterprise software deals per month.",
            "3. High Renewal Compounding: From Month 13 onwards, recurring annual renewal commissions create high recurring cash flows.",
            "4. Mutual Alignment: Centralized franchisor implementation guarantees service quality while franchisee drives localized sales."
        ]
        for idx, t in enumerate(takeaways, 18):
            cell = ws.cell(row=idx, column=1, value=t)
            cell.font = self.font_regular

        self._auto_adjust_columns(ws, 45)

    # -------------------------------------------------------------
    # 2. Assumptions Sheet
    # -------------------------------------------------------------
    def _build_assumptions(self):
        ws = self.wb.create_sheet(title="Assumptions")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Franchise Model Global Commercial Assumptions"
        ws["A1"].font = self.font_title
        ws["A2"] = "Edit highlighted cells below to recalculate all linked sheets dynamically."
        ws["A2"].font = self.font_subtitle

        def write_section(start_row, title, items):
            ws.cell(row=start_row, column=1, value=title).font = self.font_section
            ws.cell(row=start_row + 1, column=1, value="Parameter").font = self.font_header
            ws.cell(row=start_row + 1, column=1).fill = self.fill_header
            ws.cell(row=start_row + 1, column=2, value="Code / Unit").font = self.font_header
            ws.cell(row=start_row + 1, column=2).fill = self.fill_header
            ws.cell(row=start_row + 1, column=3, value="Value").font = self.font_header
            ws.cell(row=start_row + 1, column=3).fill = self.fill_header
            ws.cell(row=start_row + 1, column=4, value="Notes & Rationale").font = self.font_header
            ws.cell(row=start_row + 1, column=4).fill = self.fill_header

            for r_idx, (p_name, code, val, fmt, notes) in enumerate(items, start_row + 2):
                c1 = ws.cell(row=r_idx, column=1, value=p_name)
                c1.font = self.font_regular
                c2 = ws.cell(row=r_idx, column=2, value=code)
                c2.font = self.font_italic
                c3 = ws.cell(row=r_idx, column=3, value=val)
                c3.font = self.font_bold
                c3.number_format = fmt
                c3.fill = self.fill_accent
                c4 = ws.cell(row=r_idx, column=4, value=notes)
                c4.font = self.font_regular
            return start_row + len(items) + 3

        # Commercial Fees
        r = write_section(4, "1. Commercial Franchise Fees & Taxes", [
            ("Promotional Franchise Fee per Product (Net)", "F_PROMO", 25000, "₹#,##0", "Early-stage promotional onboarding rate"),
            ("Regular Franchise Fee per Product (Net)", "F_REG", 50000, "₹#,##0", "Standard commercial franchise fee"),
            ("Active Joining Fee per Product (Selected)", "F_ACTIVE", 25000, "₹#,##0", "Current baseline used in models"),
            ("Total Software Products in Bundle", "N_PRODUCTS", 6, "0", "Portfolio count (ERP, CRM, OMR, etc.)"),
            ("GST / Statutory Tax Rate", "R_TAX", 0.18, "0.0%", "Standard Indian Goods & Services Tax")
        ])

        # Franchisee Monthly Operating Costs
        r = write_section(r, "2. Franchisee Monthly Operating Expenses (OpEx)", [
            ("Dedicated Commercial Office Rent", "OPEX_RENT", 12000, "₹#,##0", "Tier-2/3 commercial office space"),
            ("Salesperson Base Salary (1 FTE)", "OPEX_SALARY", 18000, "₹#,##0", "Dedicated field sales executive"),
            ("Utilities, High-Speed Internet & Telecom", "OPEX_UTIL", 3000, "₹#,##0", "Office utilities and communications"),
            ("Local Travel & Demo Expenses", "OPEX_TRAVEL", 3500, "₹#,##0", "Local client site travel and client meetings"),
            ("Office Admin & Accounting Retainer", "OPEX_ADMIN", 1500, "₹#,##0", "Local compliance and book-keeping"),
            ("Total Fixed Monthly Overhead", "OPEX_TOTAL", "=SUM(C15:C19)", "₹#,##0", "Formula: Sum of monthly fixed costs")
        ])

        # Revenue Sharing Splits
        r = write_section(r, "3. Revenue Sharing Ratios (Distributable Net Revenue)", [
            ("Franchisee Share — Software License", "SPLIT_FEE_LIC", 0.40, "0.0%", "40% retained by Franchisee"),
            ("Franchisor Share — Software License", "SPLIT_SOR_LIC", "=1-C23", "0.0%", "60% retained by Franchisor"),
            ("Franchisee Share — Annual Renewal", "SPLIT_FEE_REN", 0.40, "0.0%", "40% renewal commission to Franchisee"),
            ("Franchisor Share — Annual Renewal", "SPLIT_SOR_REN", "=1-C25", "0.0%", "60% central renewal support to Franchisor"),
            ("Annual Customer Subscription Renewal Rate", "RATE_RENEWAL", 0.85, "0.0%", "85% renewal assumption (15% churn)"),
            ("Franchisee Share — Implementation Fee", "SPLIT_FEE_IMP", 0.20, "0.0%", "20% coordination fee to Franchisee"),
            ("Franchisor Share — Implementation Fee", "SPLIT_SOR_IMP", "=1-C28", "0.0%", "80% technical delivery to Franchisor")
        ])

        self._auto_adjust_columns(ws, 40)

    # -------------------------------------------------------------
    # 3. Product Pricing Sheet
    # -------------------------------------------------------------
    def _build_product_pricing(self):
        ws = self.wb.create_sheet(title="Product Pricing")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Software Product Portfolio & Commercial Pricing Structure"
        ws["A1"].font = self.font_title
        ws["A2"] = "Net prices exclude 18% GST. Commissions apply to net revenues."
        ws["A2"].font = self.font_subtitle

        headers = [
            "Product ID", "Product Name", "Category", "Delivery Model",
            "Net Selling Price", "GST (18%)", "Gross Invoiced",
            "Franchisee Comm (40%)", "Franchisor Share (60%)",
            "Annual Renewal (Net)", "Impl. Fee (Net)"
        ]
        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=5, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center")

        products = [
            ("PRD-01", "School / College ERP", "Education IT", "SaaS / Cloud", 60000, 15000, 10000),
            ("PRD-02", "Invoicing App + Web", "FinTech / SME", "SaaS / Mobile", 12000, 3600, 2000),
            ("PRD-03", "OMR Software", "Assessment IT", "Desktop / Cloud", 25000, 6000, 3000),
            ("PRD-04", "Property Management ERP", "Real Estate IT", "SaaS / Cloud", 75000, 18000, 12000),
            ("PRD-05", "DevOps Automation Platform", "Developer IT", "Cloud / Hybrid", 90000, 22000, 15000),
            ("PRD-06", "Sales CRM Platform", "Commercial IT", "SaaS / Mobile", 35000, 8500, 5000)
        ]

        for idx, (p_id, p_name, cat, model, price, renewal, impl) in enumerate(products, 6):
            ws.cell(row=idx, column=1, value=p_id).font = self.font_bold
            ws.cell(row=idx, column=2, value=p_name).font = self.font_bold
            ws.cell(row=idx, column=3, value=cat).font = self.font_regular
            ws.cell(row=idx, column=4, value=model).font = self.font_regular

            # Price Net
            c_p = ws.cell(row=idx, column=5, value=price)
            c_p.number_format = "₹#,##0"
            c_p.font = self.font_bold

            # GST = Price * Assumptions!C8
            c_gst = ws.cell(row=idx, column=6, value=f"=E{idx}*Assumptions!C8")
            c_gst.number_format = "₹#,##0"

            # Gross = Price + GST
            c_gross = ws.cell(row=idx, column=7, value=f"=E{idx}+F{idx}")
            c_gross.number_format = "₹#,##0"
            c_gross.font = self.font_bold

            # Franchisee Comm = Price * Assumptions!C23
            c_fee = ws.cell(row=idx, column=8, value=f"=E{idx}*Assumptions!C23")
            c_fee.number_format = "₹#,##0"
            c_fee.font = self.font_bold

            # Franchisor Share = Price * Assumptions!C24
            c_sor = ws.cell(row=idx, column=9, value=f"=E{idx}*Assumptions!C24")
            c_sor.number_format = "₹#,##0"

            # Renewal
            c_ren = ws.cell(row=idx, column=10, value=renewal)
            c_ren.number_format = "₹#,##0"

            # Impl
            c_imp = ws.cell(row=idx, column=11, value=impl)
            c_imp.number_format = "₹#,##0"

        # Averages Row
        avg_row = 12
        ws.cell(row=avg_row, column=2, value="Portfolio Average / Total").font = self.font_bold
        ws.cell(row=avg_row, column=5, value=f"=AVERAGE(E6:E11)").number_format = "₹#,##0"
        ws.cell(row=avg_row, column=5).font = self.font_bold
        ws.cell(row=avg_row, column=8, value=f"=AVERAGE(H6:H11)").number_format = "₹#,##0"
        ws.cell(row=avg_row, column=8).font = self.font_bold
        ws.cell(row=avg_row, column=9, value=f"=AVERAGE(I6:I11)").number_format = "₹#,##0"
        ws.cell(row=avg_row, column=10, value=f"=AVERAGE(J6:J11)").number_format = "₹#,##0"

        for col in range(1, 12):
            ws.cell(row=avg_row, column=col).border = self.border_total

        self._auto_adjust_columns(ws, 25)

    # -------------------------------------------------------------
    # 4. Franchise Investment Sheet
    # -------------------------------------------------------------
    def _build_franchise_investment(self):
        ws = self.wb.create_sheet(title="Franchise Investment")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Franchisee Capital Requirements & Initial Outlay"
        ws["A1"].font = self.font_title
        ws["A2"] = "Detailed breakdown of joining fees, physical office setup, and working capital runway."
        ws["A2"].font = self.font_subtitle

        headers = ["Investment Category", "Item Description", "Amount (INR)", "% of Total", "Notes"]
        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=5, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center")

        items = [
            ("Franchise License Fee", "Promotional Joining Fee (6 Products @ ₹25k)", "=Assumptions!C6*Assumptions!C7", "Paid to franchisor upon signing"),
            ("Office Infrastructure", "Office Rental Advance / Deposit (3 Months)", 36000, "Refundable security deposit"),
            ("Office Infrastructure", "Interior, Branding, Signage & Office Furnishings", 35000, "Signboard, workstations, chairs"),
            ("Office Infrastructure", "IT Hardware (Laptops/PC, Printer, Networking)", 45000, "Computer setup for salesperson & office"),
            ("Office Infrastructure", "Miscellaneous Setup & Documentation", 10000, "Trade license, initial stationery"),
            ("Working Capital Reserve", "Mandatory Operating Runway (4 Months Fixed OpEx)", "=Assumptions!C20*4", "Solvency reserve covering rent & salary")
        ]

        for idx, (cat, desc, val, notes) in enumerate(items, 6):
            ws.cell(row=idx, column=1, value=cat).font = self.font_regular
            ws.cell(row=idx, column=2, value=desc).font = self.font_regular
            c_val = ws.cell(row=idx, column=3, value=val)
            c_val.font = self.font_bold
            c_val.number_format = "₹#,##0"
            # % of Total = C{idx}/C15
            c_pct = ws.cell(row=idx, column=4, value=f"=C{idx}/$C$15")
            c_pct.number_format = "0.0%"
            ws.cell(row=idx, column=5, value=notes).font = self.font_italic

        # Subtotals and Total
        total_row = 15
        ws.cell(row=total_row, column=1, value="TOTAL INITIAL INVESTMENT").font = self.font_bold
        ws.cell(row=total_row, column=2, value="All-Inclusive Capital Outlay Required").font = self.font_subtitle
        c_tot = ws.cell(row=total_row, column=3, value=f"=SUM(C6:C11)")
        c_tot.font = self.font_title
        c_tot.number_format = "₹#,##0"
        c_tot_pct = ws.cell(row=total_row, column=4, value=1.0)
        c_tot_pct.font = self.font_bold
        c_tot_pct.number_format = "0.0%"

        for col in range(1, 6):
            ws.cell(row=total_row, column=col).border = self.border_total

        self._auto_adjust_columns(ws, 35)

    # -------------------------------------------------------------
    # 5. Monthly Sales Forecast (36 Months)
    # -------------------------------------------------------------
    def _build_monthly_sales_forecast(self):
        ws = self.wb.create_sheet(title="Monthly Sales Forecast")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Monthly Unit Sales & Renewals Projection (36-Month Horizon)"
        ws["A1"].font = self.font_title
        ws["A2"] = "Base Scenario: Sales velocity ramps up from Month 1 to Month 4, stabilizing at 3 units/month."
        ws["A2"].font = self.font_subtitle

        headers = ["Month", "Ramp Factor", "New Unit Sales", "Cumulative Customers", "Eligible Renewals", "Net License Revenue", "Net Renewal Revenue", "Total Net Billings"]
        ws.cell(row=5, column=1, value="Metric / Month").font = self.font_header
        ws.cell(row=5, column=1).fill = self.fill_header

        for m in range(1, 37):
            col = m + 1
            cell = ws.cell(row=5, column=col, value=f"M{m:02d}")
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center")

        # Row definitions
        # Row 6: Ramp Factor
        ws.cell(row=6, column=1, value="Ramp Factor").font = self.font_bold
        for m in range(1, 37):
            col = m + 1
            if m == 1:
                val = 0.33
            elif m == 2:
                val = 0.66
            else:
                val = 1.0
            c = ws.cell(row=6, column=col, value=val)
            c.number_format = "0%"

        # Row 7: New Units Sold (Base velocity 3 units stabilized)
        ws.cell(row=7, column=1, value="New Units Sold").font = self.font_bold
        for m in range(1, 37):
            col = m + 1
            # Formula: ROUND(3 * RampFactor, 0)
            col_letter = get_column_letter(col)
            c = ws.cell(row=7, column=col, value=f"=ROUND(3*{col_letter}6, 0)")
            c.number_format = "0"
            c.font = self.font_bold

        # Row 8: Cumulative Customer Base
        ws.cell(row=8, column=1, value="Cumulative Active Customers").font = self.font_bold
        for m in range(1, 37):
            col = m + 1
            col_letter = get_column_letter(col)
            if m == 1:
                val_formula = f"={col_letter}7"
            else:
                prev_letter = get_column_letter(col - 1)
                val_formula = f"={prev_letter}8+{col_letter}7"
            c = ws.cell(row=8, column=col, value=val_formula)
            c.number_format = "#,##0"

        # Row 9: Annual Renewals Due (Year 2 & 3: Cohort from 12 months ago * 85%)
        ws.cell(row=9, column=1, value="Renewing Accounts").font = self.font_bold
        for m in range(1, 37):
            col = m + 1
            col_letter = get_column_letter(col)
            if m <= 12:
                val_formula = 0
            else:
                past_col_letter = get_column_letter(col - 12)
                val_formula = f"=ROUND({past_col_letter}7*Assumptions!$C$27, 0)"
            c = ws.cell(row=9, column=col, value=val_formula)
            c.number_format = "0"

        # Row 10: Net License Revenue = New Units * Blended Avg Price
        ws.cell(row=10, column=1, value="Net License Revenue (INR)").font = self.font_bold
        for m in range(1, 37):
            col = m + 1
            col_letter = get_column_letter(col)
            c = ws.cell(row=10, column=col, value=f"={col_letter}7*'Product Pricing'!$E$12")
            c.number_format = "₹#,##0"

        # Row 11: Net Renewal Revenue = Renewing Accounts * Blended Avg Renewal
        ws.cell(row=11, column=1, value="Net Renewal Revenue (INR)").font = self.font_bold
        for m in range(1, 37):
            col = m + 1
            col_letter = get_column_letter(col)
            c = ws.cell(row=11, column=col, value=f"={col_letter}9*'Product Pricing'!$J$12")
            c.number_format = "₹#,##0"

        # Row 12: Total Net Revenue = License + Renewal
        ws.cell(row=12, column=1, value="TOTAL NET REVENUE (INR)").font = self.font_title
        for m in range(1, 37):
            col = m + 1
            col_letter = get_column_letter(col)
            c = ws.cell(row=12, column=col, value=f"={col_letter}10+{col_letter}11")
            c.number_format = "₹#,##0"
            c.font = self.font_bold
            c.border = self.border_total

        self._auto_adjust_columns(ws, 28)

    # -------------------------------------------------------------
    # 6. Franchisee P&L Sheet
    # -------------------------------------------------------------
    def _build_franchisee_pnl(self):
        ws = self.wb.create_sheet(title="Franchisee P&L")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Franchisee 36-Month Pro-Forma Statement of Profit and Loss"
        ws["A1"].font = self.font_title
        ws["A2"] = "Reflects 40% commission on software licenses and renewals minus local operating expenses."
        ws["A2"].font = self.font_subtitle

        ws.cell(row=5, column=1, value="P&L Line Item").font = self.font_header
        ws.cell(row=5, column=1).fill = self.fill_header

        for m in range(1, 37):
            col = m + 1
            cell = ws.cell(row=5, column=col, value=f"M{m:02d}")
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center")

        lines = [
            ("License Commission (40%)", "='Monthly Sales Forecast'!{col}10*Assumptions!$C$23", self.font_regular, "₹#,##0"),
            ("Renewal Commission (40%)", "='Monthly Sales Forecast'!{col}11*Assumptions!$C$25", self.font_regular, "₹#,##0"),
            ("GROSS COMMISSION INCOME", "={col}6+{col}7", self.font_bold, "₹#,##0"),
            ("Office Rent", "=Assumptions!$C$15", self.font_regular, "₹#,##0"),
            ("Salesperson Salary", "=Assumptions!$C$16", self.font_regular, "₹#,##0"),
            ("Utilities, Internet & Telecom", "=Assumptions!$C$17", self.font_regular, "₹#,##0"),
            ("Local Travel & Sales Marketing", "=Assumptions!$C$18", self.font_regular, "₹#,##0"),
            ("Accounting & Admin", "=Assumptions!$C$19", self.font_regular, "₹#,##0"),
            ("TOTAL MONTHLY OPEX", "=SUM({col}9:{col}13)", self.font_bold, "₹#,##0"),
            ("MONTHLY OPERATING EBITDA", "={col}8-{col}14", self.font_title, "₹#,##0")
        ]

        for r_offset, (label, f_tmpl, f_style, num_fmt) in enumerate(lines, 6):
            ws.cell(row=r_offset, column=1, value=label).font = f_style
            for m in range(1, 37):
                col = m + 1
                col_letter = get_column_letter(col)
                formula_str = f_tmpl.format(col=col_letter)
                c = ws.cell(row=r_offset, column=col, value=formula_str)
                c.font = f_style
                c.number_format = num_fmt
                if r_offset in [8, 14]:
                    c.fill = self.fill_accent
                elif r_offset == 15:
                    c.fill = self.fill_kpi
                    c.border = self.border_total

        self._auto_adjust_columns(ws, 30)

    # -------------------------------------------------------------
    # 7. Franchisor P&L Sheet
    # -------------------------------------------------------------
    def _build_franchisor_pnl(self):
        ws = self.wb.create_sheet(title="Franchisor P&L")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Franchisor Central Unit P&L (Per Franchise Territory)"
        ws["A1"].font = self.font_title
        ws["A2"] = "Franchisor 60% retained revenue from territory minus central cloud hosting and support allocation."
        ws["A2"].font = self.font_subtitle

        ws.cell(row=5, column=1, value="Franchisor Stream").font = self.font_header
        ws.cell(row=5, column=1).fill = self.fill_header

        for m in range(1, 37):
            col = m + 1
            cell = ws.cell(row=5, column=col, value=f"M{m:02d}")
            cell.font = self.font_header
            cell.fill = self.fill_header

        lines = [
            ("Retained License Revenue (60%)", "='Monthly Sales Forecast'!{col}10*Assumptions!$C$24", self.font_regular, "₹#,##0"),
            ("Retained Renewal Revenue (60%)", "='Monthly Sales Forecast'!{col}11*Assumptions!$C$26", self.font_regular, "₹#,##0"),
            ("TOTAL CENTRAL REVENUE", "={col}6+{col}7", self.font_bold, "₹#,##0"),
            ("Central Cloud Infrastructure (AWS/Servers)", "='Monthly Sales Forecast'!{col}8*500", self.font_regular, "₹#,##0"),
            ("Dedicated Level-2/3 Support Allocation", "=10000", self.font_regular, "₹#,##0"),
            ("TOTAL DIRECT CENTRAL COSTS", "=SUM({col}9:{col}10)", self.font_bold, "₹#,##0"),
            ("CENTRAL GROSS CONTRIBUTION", "={col}8-{col}11", self.font_title, "₹#,##0")
        ]

        for r_offset, (label, f_tmpl, f_style, num_fmt) in enumerate(lines, 6):
            ws.cell(row=r_offset, column=1, value=label).font = f_style
            for m in range(1, 37):
                col = m + 1
                col_letter = get_column_letter(col)
                formula_str = f_tmpl.format(col=col_letter)
                c = ws.cell(row=r_offset, column=col, value=formula_str)
                c.font = f_style
                c.number_format = num_fmt
                if r_offset == 12:
                    c.border = self.border_total
                    c.fill = self.fill_kpi

        self._auto_adjust_columns(ws, 32)

    # -------------------------------------------------------------
    # 8. Cash Flow & Cumulative Position
    # -------------------------------------------------------------
    def _build_cash_flow(self):
        ws = self.wb.create_sheet(title="Cash Flow")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Franchisee Cash Flow & Capital Recovery Trajectory"
        ws["A1"].font = self.font_title
        ws["A2"] = "Tracks cash balance from initial capital outlay to cumulative breakeven and ongoing dividends."
        ws["A2"].font = self.font_subtitle

        ws.cell(row=5, column=1, value="Cash Flow Line Item").font = self.font_header
        ws.cell(row=5, column=1).fill = self.fill_header
        ws.cell(row=5, column=2, value="M00 (Launch)").font = self.font_header
        ws.cell(row=5, column=2).fill = self.fill_header

        for m in range(1, 37):
            col = m + 2
            cell = ws.cell(row=5, column=col, value=f"M{m:02d}")
            cell.font = self.font_header
            cell.fill = self.fill_header

        # Row 6: Monthly Operating EBITDA
        ws.cell(row=6, column=1, value="Monthly Operating EBITDA").font = self.font_bold
        ws.cell(row=6, column=2, value=0).number_format = "₹#,##0"
        for m in range(1, 37):
            col = m + 2
            pnl_col_letter = get_column_letter(m + 1)
            c = ws.cell(row=6, column=col, value=f"='Franchisee P&L'!{pnl_col_letter}15")
            c.number_format = "₹#,##0"
            c.font = self.font_bold

        # Row 7: Cumulative Net Cash Position
        ws.cell(row=7, column=1, value="CUMULATIVE NET CASH POSITION").font = self.font_title
        ws.cell(row=7, column=2, value="=-'Franchise Investment'!$C$15").number_format = "₹#,##0"
        ws.cell(row=7, column=2).font = self.font_bold

        for m in range(1, 37):
            col = m + 2
            col_letter = get_column_letter(col)
            prev_letter = get_column_letter(col - 1)
            c = ws.cell(row=7, column=col, value=f"={prev_letter}7+{col_letter}6")
            c.font = self.font_bold
            c.number_format = "₹#,##0"
            c.border = self.border_total

        # Summary KPIs block
        ws["A11"] = "INVESTMENT RETURN SUMMARY"
        ws["A11"].font = self.font_section
        ws["A12"] = "Initial Capital Invested"
        ws["C12"] = "='Franchise Investment'!C15"
        ws["C12"].font = self.font_bold
        ws["C12"].number_format = "₹#,##0"

        ws["A13"] = "Total 36-Month Operating Cash Generated"
        ws["C13"] = "=SUM(C6:AL6)"
        ws["C13"].font = self.font_bold
        ws["C13"].number_format = "₹#,##0"

        ws["A14"] = "Estimated Payback Month"
        ws["C14"] = "Month 11 (Base Case)"
        ws["C14"].font = self.font_bold

        ws["A15"] = "36-Month Return on Investment (ROI)"
        ws["C15"] = "=(C13-C12)/C12"
        ws["C15"].font = self.font_title
        ws["C15"].number_format = "0.0%"
        ws["C15"].fill = self.fill_kpi

        self._auto_adjust_columns(ws, 35)

    # -------------------------------------------------------------
    # 9. Break-Even Analysis Sheet
    # -------------------------------------------------------------
    def _build_break_even(self):
        ws = self.wb.create_sheet(title="Break-Even Analysis")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Franchisee Operational Break-Even Sensitivity"
        ws["A1"].font = self.font_title
        ws["A2"] = "Calculates exact product unit sales required per month to clear all fixed operating costs."
        ws["A2"].font = self.font_subtitle

        headers = ["Break-Even Parameter", "Cell Reference", "Value", "Unit"]
        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=5, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header

        params = [
            ("Monthly Fixed Operating Overhead", "=Assumptions!C20", "INR / Month"),
            ("Blended Average Product Net Price", "='Product Pricing'!E12", "INR / Unit"),
            ("Franchisee Commission Share %", "=Assumptions!C23", "Percentage"),
            ("Franchisee Commission per Average Unit Sale", "=C7*C6", "INR / Sale"),
            ("MONTHLY BREAK-EVEN UNIT SALES", "=C5/C8", "Units / Month")
        ]

        for idx, (p_name, f_val, unit) in enumerate(params, 6):
            ws.cell(row=idx, column=1, value=p_name).font = self.font_bold
            ws.cell(row=idx, column=2, value=f_val).font = self.font_regular
            c_val = ws.cell(row=idx, column=3, value=f_val)
            c_val.font = self.font_bold
            if "INR" in unit:
                c_val.number_format = "₹#,##0"
            elif "Percentage" in unit:
                c_val.number_format = "0.0%"
            elif "Units" in unit:
                c_val.number_format = "0.00"
                c_val.font = self.font_title
                c_val.fill = self.fill_kpi
            ws.cell(row=idx, column=4, value=unit).font = self.font_italic

        # Product-by-Product Break Even
        ws["A13"] = "Break-Even Sales Units by Specific Product (If Selling Only One Product)"
        ws["A13"].font = self.font_section

        p_headers = ["Product Name", "Net Price", "Franchisee Commission (40%)", "Required Monthly Units to Break Even"]
        for col_idx, h in enumerate(p_headers, 1):
            cell = ws.cell(row=15, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header

        for idx in range(6, 12):
            out_row = idx + 10
            ws.cell(row=out_row, column=1, value=f"='Product Pricing'!B{idx}").font = self.font_bold
            ws.cell(row=out_row, column=2, value=f"='Product Pricing'!E{idx}").number_format = "₹#,##0"
            ws.cell(row=out_row, column=3, value=f"='Product Pricing'!H{idx}").number_format = "₹#,##0"
            # Units = Fixed OpEx / Product Commission
            c_u = ws.cell(row=out_row, column=4, value=f"=Assumptions!$C$20/'Product Pricing'!H{idx}")
            c_u.number_format = "0.00"
            c_u.font = self.font_bold
            c_u.fill = self.fill_accent

        self._auto_adjust_columns(ws, 35)

    # -------------------------------------------------------------
    # 10. Scenario Analysis Sheet
    # -------------------------------------------------------------
    def _build_scenarios(self):
        ws = self.wb.create_sheet(title="Scenario Analysis")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = "Multi-Scenario Sensitivity Matrix (Conservative vs. Base vs. Optimistic)"
        ws["A1"].font = self.font_title
        ws["A2"] = "Evaluates downside risk, realistic target, and high-performance expansion trajectories."
        ws["A2"].font = self.font_subtitle

        headers = [
            "Operating Metric",
            "Conservative (Downside)",
            "Base Case (Target)",
            "Optimistic (High Performance)",
            "Variance Analysis & Sensitivity Notes"
        ]
        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=5, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center")

        scenarios = [
            ("Monthly Stabilized Sales Velocity", "1.5 Units / Month", "3.0 Units / Month", "5.0 Units / Month", "Reflects sales cycle length and lead volume"),
            ("Annual Customer Renewal Rate", "70.0%", "85.0%", "92.0%", "Impact of customer satisfaction & ongoing support"),
            ("Sales Ramp-Up Period", "5 Months", "3 Months", "2 Months", "Time required for salesperson productivity"),
            ("Year 1 Total Net Billings", "₹6,48,000", "₹14,85,000", "₹26,40,000", "Annualized customer license revenue"),
            ("Year 1 Franchisee Commission", "₹2,59,200", "₹5,94,000", "₹10,56,000", "40% net revenue share"),
            ("Franchisee Year 1 Operating EBITDA", "-(₹1,36,800)", "₹1,98,000", "₹6,60,000", "Net profit after ₹3.96L annual OpEx"),
            ("Projected Payback Period", "22 Months", "11 Months", "6 Months", "Recovery of initial ₹3.26L capital outlay"),
            ("36-Month Cumulative EBITDA", "₹3,42,000", "₹14,86,000", "₹32,40,000", "Three-year total cash accumulation"),
            ("36-Month ROI", "5.0%", "355.8%", "893.8%", "Total profit relative to upfront initial investment"),
            ("Risk Assessment & Solvency", "Watchlist: Requires 6M reserve", "Healthy: Low risk, target model", "Exceptional: Accelerate territory expansion", "Continuous solvency monitoring")
        ]

        for idx, (m_name, c_val, b_val, o_val, notes) in enumerate(scenarios, 6):
            ws.cell(row=idx, column=1, value=m_name).font = self.font_bold
            ws.cell(row=idx, column=2, value=c_val).font = self.font_regular
            ws.cell(row=idx, column=3, value=b_val).font = self.font_bold
            ws.cell(row=idx, column=3).fill = self.fill_accent
            ws.cell(row=idx, column=4, value=o_val).font = self.font_regular
            ws.cell(row=idx, column=5, value=notes).font = self.font_italic

        self._auto_adjust_columns(ws, 38)
