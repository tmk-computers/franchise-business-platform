"""
Franchise Launch Readiness Excel Workbook Generator
===================================================
Automated openpyxl tool to generate an interactive, formula-driven
Franchise Launch Readiness Task Tracker for any client workspace.

Sheets Generated:
1. Readiness Dashboard (Executive KPIs, Gate status, overall readiness score)
2. Workstream Summary (Aggregated metrics across the 12 workstreams)
3. Owner Summary (Task distribution and completion across responsible roles)
4. Master Checklist (Granular 12-workstream itemized tracker with filters, validation, overdue formulas)
5. Launch Gates & Blockers (Detailed gate prerequisites, blocker conditions, and resolution rules)
"""

import os
import sys
import json
import argparse
from typing import Dict, Any, List
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

# Ensure stdout supports UTF-8 on Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class LaunchReadinessExcelGenerator:
    """Generates dynamically formula-linked Launch Readiness workbooks using openpyxl."""

    def __init__(self, checklist_data: Dict[str, Any], client_name: str = "TMK IT Solutions LLP"):
        self.data = checklist_data
        self.client_name = client_name
        self.wb = openpyxl.Workbook()
        self.wb.remove(self.wb.active)  # Remove initial sheet

        # Styles
        self.font_title = Font(name="Calibri", size=16, bold=True, color="1F497D")
        self.font_subtitle = Font(name="Calibri", size=11, italic=True, color="595959")
        self.font_section = Font(name="Calibri", size=12, bold=True, color="1F497D")
        self.font_header = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
        self.font_bold = Font(name="Calibri", size=10, bold=True)
        self.font_regular = Font(name="Calibri", size=10)
        self.font_italic = Font(name="Calibri", size=9, italic=True, color="595959")
        self.font_kpi_num = Font(name="Calibri", size=18, bold=True, color="1F497D")

        self.fill_header = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
        self.fill_subheader = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
        self.fill_accent = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
        self.fill_kpi = PatternFill(start_color="EBF1DE", end_color="EBF1DE", fill_type="solid")
        self.fill_alert = PatternFill(start_color="FDE9D9", end_color="FDE9D9", fill_type="solid")
        self.fill_gate_cleared = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")

        self.border_thin = Border(
            left=Side(style="thin", color="D9D9D9"),
            right=Side(style="thin", color="D9D9D9"),
            top=Side(style="thin", color="D9D9D9"),
            bottom=Side(style="thin", color="D9D9D9")
        )
        self.border_header = Border(
            left=Side(style="thin", color="FFFFFF"),
            right=Side(style="thin", color="FFFFFF"),
            top=Side(style="thin", color="1F497D"),
            bottom=Side(style="medium", color="1F497D")
        )
        self.border_total = Border(
            top=Side(style="thin", color="000000"),
            bottom=Side(style="double", color="000000")
        )

    def _auto_fit_columns(self, ws, max_width_dict: Dict[int, int] = None):
        """Auto-fit column widths with a sensible minimum and maximum."""
        for col in ws.columns:
            col_letter = get_column_letter(col[0].column)
            col_idx = col[0].column
            max_len = 0
            for cell in col:
                # Skip merged or very long title lines in column A
                if cell.row < 4 and col_letter == 'A':
                    continue
                if cell.value:
                    val_str = str(cell.value)
                    # Ignore formula text length
                    if val_str.startswith("="):
                        val_str = "12345678"
                    max_len = max(max_len, len(val_str))
            
            override_max = max_width_dict.get(col_idx) if max_width_dict else None
            if override_max:
                ws.column_dimensions[col_letter].width = override_max
            else:
                ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 45)

    def build_dashboard(self):
        """Sheet 1: Readiness Dashboard with Executive KPIs & Launch Gates."""
        ws = self.wb.create_sheet(title="Readiness Dashboard")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = f"{self.client_name} — Franchise Launch Readiness Dashboard"
        ws["A1"].font = self.font_title
        ws["A2"] = f"Master 12-Workstream Readiness Tracker | Version {self.data.get('version', '1.0.0')} | Updated {self.data.get('lastUpdated', '2026-10-26')}"
        ws["A2"].font = self.font_subtitle

        # KPI Block Table
        ws["A4"] = "EXECUTIVE READINESS KPIS"
        ws["A4"].font = self.font_section

        kpi_metrics = [
            ("Total Program Tasks", "=COUNTA('Master Checklist'!A5:A80)", "Total itemized deliverables across 12 workstreams"),
            ("Approved / Verified Tasks", "=COUNTIF('Master Checklist'!G5:G80, \"Document Approved\") + COUNTIF('Master Checklist'!G5:G80, \"Process Implemented\") + COUNTIF('Master Checklist'!G5:G80, \"Process Verified\")", "Formally verified deliverables meeting acceptance criteria"),
            ("In Progress / Draft Tasks", "=COUNTIF('Master Checklist'!G5:G80, \"In Progress\") + COUNTIF('Master Checklist'!G5:G80, \"Document Created\") + COUNTIF('Master Checklist'!G5:G80, \"Document Reviewed\")", "Active work underway across business and engineering units"),
            ("Not Started Tasks", "=COUNTIF('Master Checklist'!G5:G80, \"Not Started\")", "Post-launch or milestone deliverables scheduled for future waves"),
            ("Active Critical Blockers", "=COUNTIFS('Master Checklist'!O5:O80, TRUE, 'Master Checklist'!G5:G80, \"<>Document Approved\", 'Master Checklist'!G5:G80, \"<>Process Verified\")", "Systemic defects or unvetted contracts that veto gate passage"),
            ("Launch Readiness Completion %", "=ROUND((B6/B5)*100, 1)", "Weighted percentage of verified deliverables vs total scope")
        ]

        headers = ["Metric Description", "Value", "Notes & Status Interpretation"]
        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=5, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center" if col_idx == 2 else "left")

        for idx, (label, formula, note) in enumerate(kpi_metrics, 6):
            c_lbl = ws.cell(row=idx, column=1, value=label)
            c_lbl.font = self.font_bold
            c_lbl.border = self.border_thin

            c_val = ws.cell(row=idx, column=2, value=formula)
            c_val.font = self.font_bold
            c_val.alignment = Alignment(horizontal="center")
            c_val.border = self.border_thin
            if "Completion" in label:
                c_val.fill = self.fill_kpi
                c_val.number_format = "0.0\"%\""
            elif "Blockers" in label:
                c_val.fill = self.fill_alert
            else:
                c_val.fill = self.fill_accent

            c_not = ws.cell(row=idx, column=3, value=note)
            c_not.font = self.font_italic
            c_not.border = self.border_thin

        # Launch Gates Status Block
        ws["A13"] = "SIX SEQUENTIAL LAUNCH GATES"
        ws["A13"].font = self.font_section

        gate_headers = ["Gate ID", "Gate Name", "Target Date", "Current Status", "Workstreams Governed"]
        for col_idx, h in enumerate(gate_headers, 1):
            cell = ws.cell(row=14, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center" if col_idx in [1, 3, 4] else "left")

        gates = self.data.get("launchGates", [])
        for idx, g in enumerate(gates, 15):
            ws.cell(row=idx, column=1, value=g["gateId"]).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=2, value=g["name"]).font = self.font_bold
            ws.cell(row=idx, column=3, value=g["targetDate"]).alignment = Alignment(horizontal="center")
            
            c_stat = ws.cell(row=idx, column=4, value=g["status"])
            c_stat.alignment = Alignment(horizontal="center")
            c_stat.font = self.font_bold
            if g["status"] == "Gate Cleared":
                c_stat.fill = self.fill_gate_cleared
            elif g["status"] == "In Progress":
                c_stat.fill = self.fill_subheader
            else:
                c_stat.fill = self.fill_accent

            ws.cell(row=idx, column=5, value=", ".join(g.get("workstreamsCovered", []))).font = self.font_regular

            for c in range(1, 6):
                ws.cell(row=idx, column=c).border = self.border_thin

        self._auto_fit_columns(ws, {1: 32, 2: 24, 3: 20, 4: 18, 5: 42})

    def build_workstream_summary(self):
        """Sheet 2: Workstream Summary table."""
        ws = self.wb.create_sheet(title="Workstream Summary")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = f"{self.client_name} — 12-Workstream Readiness Summary"
        ws["A1"].font = self.font_title
        ws["A2"] = "Dynamic aggregation of deliverables, completion counts, and readiness percentage by domain"
        ws["A2"].font = self.font_subtitle

        headers = ["#", "Workstream Name", "Total Tasks", "Approved / Verified", "In Progress / Draft", "Not Started", "Completion %"]
        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=4, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center" if col_idx in [1, 3, 4, 5, 6, 7] else "left")

        workstreams = self.data.get("workstreams", [])
        for idx, ws_name in enumerate(workstreams, 5):
            ws.cell(row=idx, column=1, value=idx - 4).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=2, value=ws_name).font = self.font_bold

            # Excel formulas referencing Master Checklist
            total_formula = f'=COUNTIF(\'Master Checklist\'!$B$5:$B$80, "{ws_name}")'
            appr_formula = (
                f'=COUNTIFS(\'Master Checklist\'!$B$5:$B$80, "{ws_name}", \'Master Checklist\'!$G$5:$G$80, "Document Approved") + '
                f'COUNTIFS(\'Master Checklist\'!$B$5:$B$80, "{ws_name}", \'Master Checklist\'!$G$5:$G$80, "Process Implemented") + '
                f'COUNTIFS(\'Master Checklist\'!$B$5:$B$80, "{ws_name}", \'Master Checklist\'!$G$5:$G$80, "Process Verified")'
            )
            prog_formula = (
                f'=COUNTIFS(\'Master Checklist\'!$B$5:$B$80, "{ws_name}", \'Master Checklist\'!$G$5:$G$80, "In Progress") + '
                f'COUNTIFS(\'Master Checklist\'!$B$5:$B$80, "{ws_name}", \'Master Checklist\'!$G$5:$G$80, "Document Created") + '
                f'COUNTIFS(\'Master Checklist\'!$B$5:$B$80, "{ws_name}", \'Master Checklist\'!$G$5:$G$80, "Document Reviewed")'
            )
            ns_formula = f'=COUNTIFS(\'Master Checklist\'!$B$5:$B$80, "{ws_name}", \'Master Checklist\'!$G$5:$G$80, "Not Started")'
            pct_formula = f'=IF(C{idx}>0, ROUND((D{idx}/C{idx})*100, 1), 0)'

            ws.cell(row=idx, column=3, value=total_formula).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=4, value=appr_formula).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=5, value=prog_formula).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=6, value=ns_formula).alignment = Alignment(horizontal="center")
            
            c_pct = ws.cell(row=idx, column=7, value=pct_formula)
            c_pct.alignment = Alignment(horizontal="center")
            c_pct.number_format = "0.0\"%\""
            c_pct.font = self.font_bold

            for c in range(1, 8):
                ws.cell(row=idx, column=c).border = self.border_thin

        # Total Row
        tot_row = len(workstreams) + 5
        ws.cell(row=tot_row, column=1, value="")
        ws.cell(row=tot_row, column=2, value="TOTAL ALL WORKSTREAMS").font = self.font_bold
        ws.cell(row=tot_row, column=3, value=f"=SUM(C5:C{tot_row-1})").alignment = Alignment(horizontal="center")
        ws.cell(row=tot_row, column=4, value=f"=SUM(D5:D{tot_row-1})").alignment = Alignment(horizontal="center")
        ws.cell(row=tot_row, column=5, value=f"=SUM(E5:E{tot_row-1})").alignment = Alignment(horizontal="center")
        ws.cell(row=tot_row, column=6, value=f"=SUM(F5:F{tot_row-1})").alignment = Alignment(horizontal="center")
        
        c_tot_pct = ws.cell(row=tot_row, column=7, value=f"=IF(C{tot_row}>0, ROUND((D{tot_row}/C{tot_row})*100, 1), 0)")
        c_tot_pct.alignment = Alignment(horizontal="center")
        c_tot_pct.font = self.font_bold
        c_tot_pct.number_format = "0.0\"%\""

        for c in range(1, 8):
            cell = ws.cell(row=tot_row, column=c)
            cell.font = self.font_bold
            cell.border = self.border_total
            cell.fill = self.fill_subheader

        self._auto_fit_columns(ws, {2: 38, 7: 16})

    def build_owner_summary(self):
        """Sheet 3: Owner Summary table."""
        ws = self.wb.create_sheet(title="Owner Summary")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = f"{self.client_name} — Accountable Owner Task Summary"
        ws["A1"].font = self.font_title
        ws["A2"] = "Resource allocation and task completion by responsible role"
        ws["A2"].font = self.font_subtitle

        headers = ["Role / Responsible Owner", "Domain Focus", "Total Tasks Assigned", "Verified / Approved", "In Progress / Draft", "Overdue / Blocked"]
        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=4, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center" if col_idx in [3, 4, 5, 6] else "left")

        owners = [
            ("Analyst 1", "Business Strategy, Research, Documentation & Collateral"),
            ("Analyst 2", "Financial Modeling, Analytics, Schemas & Excel Math"),
            ("Legal Counsel", "Franchise Agreements, Trademark Licensing & Regulatory Review"),
            ("Lead Software Architect", "6 Software Demo Sandboxes, Cloud HA, RBAC & Provisioning"),
            ("Finance Director / CA", "Banking Escrow, GST Pass-Through Tax & Solvency Verification"),
            ("Franchise Operations Lead", "SOP Handbook, Training Curriculum, Recruitment & Support SLAs"),
            ("Managing Partner", "Executive Decisions, Pilot Agreements & Expansion Gate Approvals")
        ]

        for idx, (role, domain) in enumerate(owners, 5):
            ws.cell(row=idx, column=1, value=role).font = self.font_bold
            ws.cell(row=idx, column=2, value=domain).font = self.font_regular

            tot_f = f'=COUNTIF(\'Master Checklist\'!$F$5:$F$80, "{role}")'
            appr_f = (
                f'=COUNTIFS(\'Master Checklist\'!$F$5:$F$80, "{role}", \'Master Checklist\'!$G$5:$G$80, "Document Approved") + '
                f'COUNTIFS(\'Master Checklist\'!$F$5:$F$80, "{role}", \'Master Checklist\'!$G$5:$G$80, "Process Implemented") + '
                f'COUNTIFS(\'Master Checklist\'!$F$5:$F$80, "{role}", \'Master Checklist\'!$G$5:$G$80, "Process Verified")'
            )
            prog_f = (
                f'=COUNTIFS(\'Master Checklist\'!$F$5:$F$80, "{role}", \'Master Checklist\'!$G$5:$G$80, "In Progress") + '
                f'COUNTIFS(\'Master Checklist\'!$F$5:$F$80, "{role}", \'Master Checklist\'!$G$5:$G$80, "Document Created") + '
                f'COUNTIFS(\'Master Checklist\'!$F$5:$F$80, "{role}", \'Master Checklist\'!$G$5:$G$80, "Document Reviewed")'
            )
            over_f = f'=COUNTIFS(\'Master Checklist\'!$F$5:$F$80, "{role}", \'Master Checklist\'!$L$5:$L$80, "OVERDUE")'

            ws.cell(row=idx, column=3, value=tot_f).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=4, value=appr_f).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=5, value=prog_f).alignment = Alignment(horizontal="center")
            
            c_over = ws.cell(row=idx, column=6, value=over_f)
            c_over.alignment = Alignment(horizontal="center")
            c_over.font = self.font_bold

            for c in range(1, 7):
                ws.cell(row=idx, column=c).border = self.border_thin

        # Summary Row
        tot_row = len(owners) + 5
        ws.cell(row=tot_row, column=1, value="TOTAL ALL ROLES").font = self.font_bold
        ws.cell(row=tot_row, column=2, value="")
        ws.cell(row=tot_row, column=3, value=f"=SUM(C5:C{tot_row-1})").alignment = Alignment(horizontal="center")
        ws.cell(row=tot_row, column=4, value=f"=SUM(D5:D{tot_row-1})").alignment = Alignment(horizontal="center")
        ws.cell(row=tot_row, column=5, value=f"=SUM(E5:E{tot_row-1})").alignment = Alignment(horizontal="center")
        ws.cell(row=tot_row, column=6, value=f"=SUM(F5:F{tot_row-1})").alignment = Alignment(horizontal="center")

        for c in range(1, 7):
            cell = ws.cell(row=tot_row, column=c)
            cell.font = self.font_bold
            cell.border = self.border_total
            cell.fill = self.fill_subheader

        self._auto_fit_columns(ws, {1: 28, 2: 45, 6: 20})

    def build_master_checklist(self):
        """Sheet 4: Master Checklist with filters, data validation dropdowns, and overdue logic."""
        ws = self.wb.create_sheet(title="Master Checklist")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = f"{self.client_name} — Master 12-Workstream Launch Readiness Checklist"
        ws["A1"].font = self.font_title
        ws["A2"] = "Complete task inventory, ownership RACI, status tracking, launch gating, and blocker registry"
        ws["A2"].font = self.font_subtitle

        headers = [
            "Task ID", "Workstream", "Title", "Description", "Priority", 
            "Owner Role", "Status", "Classification", "Reviewer Role", 
            "Approval Authority", "Target Date", "Overdue Indicator", "Dependencies", 
            "Launch Gate", "Is Blocker?", "Related Document"
        ]

        for col_idx, h in enumerate(headers, 1):
            cell = ws.cell(row=4, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center" if col_idx in [1, 5, 7, 11, 12, 14, 15] else "left")

        items = self.data.get("items", [])
        start_row = 5
        end_row = start_row + len(items) - 1

        for idx, item in enumerate(items, start_row):
            ws.cell(row=idx, column=1, value=item["taskId"]).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=2, value=item["workstream"])
            ws.cell(row=idx, column=3, value=item["title"]).font = self.font_bold
            ws.cell(row=idx, column=4, value=item["description"])
            ws.cell(row=idx, column=5, value=item["priority"]).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=6, value=item["ownerRole"])
            
            c_stat = ws.cell(row=idx, column=7, value=item["status"])
            c_stat.alignment = Alignment(horizontal="center")
            c_stat.font = self.font_bold
            if item["status"] in ["Document Approved", "Process Implemented", "Process Verified"]:
                c_stat.fill = self.fill_kpi
            elif item["status"] in ["In Progress", "Document Created", "Document Reviewed"]:
                c_stat.fill = self.fill_subheader
            else:
                c_stat.fill = self.fill_accent

            ws.cell(row=idx, column=8, value=item["classification"])
            ws.cell(row=idx, column=9, value=item["reviewerRole"])
            ws.cell(row=idx, column=10, value=item["approvalAuthority"])
            
            c_date = ws.cell(row=idx, column=11, value=item["targetDate"])
            c_date.alignment = Alignment(horizontal="center")

            # Overdue formula: IF(AND(TargetDate < TODAY(), Status <> Approved, Status <> Verified), "OVERDUE", "On Track")
            overdue_formula = f'=IF(AND(K{idx}<TODAY(), G{idx}<>"Document Approved", G{idx}<>"Process Verified"), "OVERDUE", "On Track")'
            c_over = ws.cell(row=idx, column=12, value=overdue_formula)
            c_over.alignment = Alignment(horizontal="center")
            c_over.font = self.font_bold

            ws.cell(row=idx, column=13, value=", ".join(item.get("dependencies", []))).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=14, value=item["launchGate"])
            
            c_blk = ws.cell(row=idx, column=15, value=item["isBlocker"])
            c_blk.alignment = Alignment(horizontal="center")
            if item["isBlocker"]:
                c_blk.font = self.font_bold

            rel_docs = item.get("relatedDocuments", [])
            ws.cell(row=idx, column=16, value=", ".join(rel_docs) if rel_docs else "")

            for c in range(1, 17):
                ws.cell(row=idx, column=c).border = self.border_thin

        # Enable AutoFilter on master checklist
        ws.auto_filter.ref = f"A4:P{end_row}"

        # Data Validation: Status Dropdown
        dv_status = DataValidation(
            type="list",
            formula1='"Not Started,In Progress,Document Created,Document Reviewed,Document Approved,Process Implemented,Process Verified"',
            allow_blank=True
        )
        dv_status.error = 'Invalid status selected. Choose from official maturity stages.'
        dv_status.errorTitle = 'Invalid Status'
        ws.add_data_validation(dv_status)
        dv_status.add(f"G5:G{end_row}")

        # Data Validation: Priority Dropdown
        dv_priority = DataValidation(
            type="list",
            formula1='"Critical,High,Medium,Low"',
            allow_blank=True
        )
        ws.add_data_validation(dv_priority)
        dv_priority.add(f"E5:E{end_row}")

        self._auto_fit_columns(ws, {
            1: 14, 2: 32, 3: 35, 4: 45, 5: 12, 6: 22, 
            7: 22, 8: 26, 9: 22, 10: 22, 11: 14, 12: 18, 
            13: 16, 14: 30, 15: 14, 16: 40
        })

    def build_launch_gates_and_blockers(self):
        """Sheet 5: Launch Gates Reference & Blocker Catalog."""
        ws = self.wb.create_sheet(title="Gates & Blockers")
        ws.views.sheetView[0].showGridLines = True

        ws["A1"] = f"{self.client_name} — Launch Gates & Blocker Specifications"
        ws["A1"].font = self.font_title
        ws["A2"] = "Stage-gate entry/exit criteria, non-negotiable blocker definitions, and override policies"
        ws["A2"].font = self.font_subtitle

        # Gates Table
        ws["A4"] = "STAGE-GATE GOVERNANCE MATRIX"
        ws["A4"].font = self.font_section

        gate_cols = ["Gate ID", "Gate Name", "Target Date", "Governing Domains", "Mandatory Exit Criteria", "Approval Authority"]
        for col_idx, h in enumerate(gate_cols, 1):
            cell = ws.cell(row=5, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center" if col_idx in [1, 3] else "left")

        gates_meta = [
            ("Gate 1", "Gate 1: Business Model Approved", "2026-10-26", "Strategy, Pricing & Revenue Sharing", "Break-even units verified (2 contracts/mo); payback <= 12 months; formal sign-off.", "Managing Partner"),
            ("Gate 2", "Gate 2: Legal & Financial Readiness", "2026-12-01", "Legal Agreements, Statutory Taxes & Escrow", "Master agreement certified by corporate legal counsel; 18% GST pass-through isolated; bank escrow active.", "Corporate Legal Counsel & CA"),
            ("Gate 3", "Gate 3: Product & Delivery Readiness", "2026-12-15", "6 Software Products, Central SLAs & Cloud", "Live demonstration sandboxes active for all 6 products; support SLA matrix approved; 99.9% cloud HA.", "Lead Software Architect"),
            ("Gate 4", "Gate 4: Franchise Recruitment Readiness", "2027-01-05", "Pitch Collateral, Prospectus & Vetting", "Institutional prospectus and FAQ completed with disclaimers; partner application form active; proof-of-funds verified.", "Head of Recruitment & Counsel"),
            ("Gate 5", "Gate 5: Pilot Launch Readiness", "2027-01-20", "Operations SOPs, CRM Deal Lock & Training", "10-day training curriculum completed; 90-day CRM deal lock engine active; 3 pilot partner agreements signed.", "Director of Operations & CEO"),
            ("Gate 6", "Gate 6: National Expansion Approval", "2027-04-30", "Pilot Audits, CSAT & Network Gating", "90-day pilot sales velocity reconciled against model; end-customer CSAT >= 85%; board authorization.", "Board of Directors / Executive Lead")
        ]

        for idx, (gid, gname, gdate, gdom, gcrit, gauth) in enumerate(gates_meta, 6):
            ws.cell(row=idx, column=1, value=gid).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=2, value=gname).font = self.font_bold
            ws.cell(row=idx, column=3, value=gdate).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=4, value=gdom)
            ws.cell(row=idx, column=5, value=gcrit)
            ws.cell(row=idx, column=6, value=gauth).font = self.font_bold

            for c in range(1, 7):
                ws.cell(row=idx, column=c).border = self.border_thin

        # Blockers Table
        b_start = 14
        ws.cell(row=b_start, column=1, value="CRITICAL LAUNCH BLOCKER TAXONOMY (AUTOMATIC VETO CONDITIONS)").font = self.font_section

        blocker_cols = ["Blocker ID", "Affected Gates", "Defect Title & Root Cause", "Impact & Risk", "Mandatory Resolution Requirement", "Default Status"]
        for col_idx, h in enumerate(blocker_cols, 1):
            cell = ws.cell(row=b_start + 1, column=col_idx, value=h)
            cell.font = self.font_header
            cell.fill = self.fill_header
            cell.alignment = Alignment(horizontal="center" if col_idx in [1, 2, 6] else "left")

        blockers = [
            ("BLK-001", "Gate 2, Gate 4", "Unvetted Franchise Contract", "Regulatory fines, illegal contract claims, partner litigation", "Written certification and legal opinion signed by corporate counsel", "Active - In Progress"),
            ("BLK-002", "Gate 2", "Tax Pass-Through Non-Segregation", "Illegal GST tax non-compliance, distorted partner commission calculations", "Decimal calculator isolates 18% GST before computing 40:60 splits", "Resolved - Verified"),
            ("BLK-003", "Gate 3", "Unstable Software Demo Sandbox", "Failed sales presentations, damaged franchisor credibility, zero conversions", "Dedicated cloud demo instances deployed with synthetic test data and 99.9% uptime", "Active - Staging"),
            ("BLK-004", "Gate 3, Gate 5", "Undefined Central SLA Escalation", "Unresolved software defects, customer churn, partner dissatisfaction", "Published SLA matrix with signed engineering commitment for P1 (< 2h) issues", "Resolved - Approved"),
            ("BLK-005", "Gate 4, Gate 5", "Inadequate Partner Working Capital Reserve", "Partner insolvency during initial ramp-up, unit abandonment, brand failure", "Mandatory bank statement proof-of-funds verification (minimum ₹50k liquid cushion)", "Active - Draft Created"),
            ("BLK-006", "Gate 6", "Unvalidated Pilot Milestone Audit", "Premature national rollout of flawed economic or operational model", "Completed 90-day pilot revenue audit and CSAT survey (>= 85%)", "Pending - Scheduled"),
            ("BLK-007", "Gate 5", "Absence of CRM Deal Registration Lock", "Partner lead poaching, territory disputes, channel cannibalization", "Technical enforcement of 90-day prospect protection in central partner portal", "Active - Testing")
        ]

        for idx, (bid, bgates, bname, bimp, bres, bstat) in enumerate(blockers, b_start + 2):
            ws.cell(row=idx, column=1, value=bid).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=2, value=bgates).alignment = Alignment(horizontal="center")
            ws.cell(row=idx, column=3, value=bname).font = self.font_bold
            ws.cell(row=idx, column=4, value=bimp)
            ws.cell(row=idx, column=5, value=bres)
            
            c_stat = ws.cell(row=idx, column=6, value=bstat)
            c_stat.alignment = Alignment(horizontal="center")
            c_stat.font = self.font_bold
            if "Resolved" in bstat:
                c_stat.fill = self.fill_kpi
            else:
                c_stat.fill = self.fill_alert

            for c in range(1, 7):
                ws.cell(row=idx, column=c).border = self.border_thin

        self._auto_fit_columns(ws, {1: 14, 2: 18, 3: 35, 4: 35, 5: 45, 6: 22})

    def generate(self, output_filepath: str):
        """Assemble all sheets and save workbook."""
        os.makedirs(os.path.dirname(os.path.abspath(output_filepath)), exist_ok=True)
        self.build_dashboard()
        self.build_workstream_summary()
        self.build_owner_summary()
        self.build_master_checklist()
        self.build_launch_gates_and_blockers()

        self.wb.save(output_filepath)
        print(f"Excel workbook successfully generated: {output_filepath}")


def main():
    parser = argparse.ArgumentParser(description="Franchise Launch Readiness Tracker Generator")
    parser.add_argument("--client", default="tmk-it-solutions", help="Client workspace slug")
    parser.add_argument("--output", default=None, help="Output Excel workbook file path")

    args = parser.parse_args()
    client_slug = args.client
    base_dir = "."

    checklist_path = os.path.join(base_dir, "clients", client_slug, "launch-readiness", f"{client_slug.replace('-', '_')}_launch_readiness_checklist.json")
    if not os.path.exists(checklist_path):
        checklist_path = os.path.join(base_dir, "clients", client_slug, "launch-readiness", "tmk-launch-readiness-checklist.json")

    if not os.path.exists(checklist_path):
        print(f"Error: Checklist JSON not found: {checklist_path}")
        sys.exit(1)

    with open(checklist_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    client_name = "TMK IT Solutions LLP"
    output_path = args.output or os.path.join(base_dir, "clients", client_slug, "launch-readiness", "tmk_launch_readiness_tracker.xlsx")

    generator = LaunchReadinessExcelGenerator(checklist_data=data, client_name=client_name)
    generator.generate(output_path)


if __name__ == "__main__":
    main()
