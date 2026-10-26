"""
Repository Integrity, Schema, and Link Validation Suite
========================================================
Comprehensive automated validation script verifying:
1. JSON Schema validity for client configs and catalogs.
2. Structural existence of mandatory directories and key deliverables.
3. Integrity of relative markdown links across repository documentation.
4. Financial configuration rules (e.g., revenue sharing splits sum to 100%).

Exits with code 0 on complete pass, or code 1 on any failure.
"""

import os
import sys
import json
import re
from typing import List, Dict, Tuple
from jsonschema import validate, Draft7Validator, ValidationError

# Configure UTF-8 on Windows stdout
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass



class RepoValidator:
    def __init__(self, repo_root: str = "."):
        self.repo_root = os.path.abspath(repo_root)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.checked_files = 0
        self.schemas: Dict[str, dict] = {}
        self._load_schemas()

    def _load_schemas(self):
        """Preload all JSON schemas from schemas/."""
        schema_dir = os.path.join(self.repo_root, "schemas")
        if not os.path.exists(schema_dir):
            self.errors.append(f"Schemas directory not found: {schema_dir}")
            return

        for fname in os.listdir(schema_dir):
            if fname.endswith(".schema.json"):
                fpath = os.path.join(schema_dir, fname)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        self.schemas[fname] = json.load(f)
                except Exception as e:
                    self.errors.append(f"Failed to load schema {fname}: {e}")

    def log_error(self, msg: str):
        self.errors.append(msg)
        print(f"  [ERROR] {msg}")

    def log_warning(self, msg: str):
        self.warnings.append(msg)
        print(f"  [WARN]  {msg}")

    def validate_required_structure(self):
        """Verify existence of mandatory platform and client files."""
        print("\n--- 1. Validating Repository Directory & File Structure ---")
        required_paths = [
            "README.md",
            "AGENTS.md",
            "CONTRIBUTING.md",
            "CHANGELOG.md",
            "LICENSE-DECISION.md",
            ".gitignore",
            ".editorconfig",
            ".github/workflows/ci.yml",
            ".github/pull_request_template.md",
            "platform/vision/platform-vision.md",
            "platform/product-requirements/prd-v0.1.md",
            "platform/architecture/system-architecture.md",
            "platform/data-models/domain-model.md",
            "platform/security/security-policy.md",
            "platform/roadmap/roadmap-v1-to-v3.md",
            "frameworks/franchise-model-design/franchise-archetypes-comparison.md",
            "frameworks/feasibility-analysis/financial-feasibility-framework.md",
            "frameworks/revenue-sharing/configurable-revenue-sharing-framework.md",
            "frameworks/territory-intelligence/territory-intelligence-framework.md",
            "frameworks/investor-protection/investor-protection-framework.md",
            "frameworks/performance-analytics/kpi-analytics-framework.md",
            "tools/financial-modeling/calculator.py",
            "tools/financial-modeling/excel_generator.py",
            "clients/tmk-it-solutions/profile/client.json",
            "clients/tmk-it-solutions/products/products-catalog.json",
            "clients/tmk-it-solutions/franchise-model/revenue-sharing-config.json",
            "clients/tmk-it-solutions/financial-models/assumptions.json"
        ]

        for rel_path in required_paths:
            abs_path = os.path.join(self.repo_root, rel_path)
            if not os.path.exists(abs_path):
                self.log_error(f"Missing mandatory file: {rel_path}")
            else:
                self.checked_files += 1

        print(f"Structure check completed. Verified {self.checked_files} mandatory files.")

    def validate_json_schemas(self):
        """Validate client JSON configurations against their respective schemas."""
        print("\n--- 2. Validating JSON Configurations Against Schemas ---")
        validation_targets = [
            ("clients/tmk-it-solutions/profile/client.json", "client.schema.json"),
            ("clients/tmk-it-solutions/products/products-catalog.json", "product.schema.json"),
            ("clients/tmk-it-solutions/financial-models/assumptions.json", "financial-assumptions.schema.json"),
            ("clients/tmk-it-solutions/franchise-model/revenue-sharing-config.json", "revenue-sharing.schema.json")
        ]

        for rel_json, schema_name in validation_targets:
            json_path = os.path.join(self.repo_root, rel_json)
            if not os.path.exists(json_path):
                self.log_error(f"Target JSON not found: {rel_json}")
                continue

            schema = self.schemas.get(schema_name)
            if not schema:
                self.log_error(f"Schema not loaded: {schema_name}")
                continue

            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                validate(instance=data, schema=schema)
                print(f"  [PASS] {rel_json} conforms to {schema_name}")
            except ValidationError as ve:
                self.log_error(f"Schema validation failed for {rel_json} against {schema_name}: {ve.message}")
            except Exception as e:
                self.log_error(f"Error reading {rel_json}: {e}")

    def validate_financial_consistency(self):
        """Verify mathematical consistency of client commercial parameters."""
        print("\n--- 3. Validating Financial Configuration Consistency ---")
        assumptions_path = os.path.join(self.repo_root, "clients/tmk-it-solutions/financial-models/assumptions.json")
        rev_share_path = os.path.join(self.repo_root, "clients/tmk-it-solutions/franchise-model/revenue-sharing-config.json")

        if os.path.exists(rev_share_path):
            with open(rev_share_path, "r", encoding="utf-8") as f:
                rdata = json.load(f)
            # Check default rules sum to 100%
            def_rules = rdata.get("defaultRules", {})
            for rule_name, rule_split in def_rules.items():
                fee_pct = rule_split.get("franchiseeSharePercent", 0)
                sor_pct = rule_split.get("franchisorSharePercent", 0)
                total_pct = fee_pct + sor_pct
                if total_pct != 100:
                    self.log_error(f"Revenue split for '{rule_name}' does not sum to 100%: {fee_pct}% + {sor_pct}% = {total_pct}%")
                else:
                    print(f"  [PASS] Split '{rule_name}': {fee_pct}% Fee / {sor_pct}% Sor = 100%")

        if os.path.exists(assumptions_path):
            with open(assumptions_path, "r", encoding="utf-8") as f:
                adata = json.load(f)
            # Verify positive costs
            opex = adata.get("franchiseeMonthlyOpEx", {})
            total_fixed = sum(val for val in opex.values() if isinstance(val, (int, float)))
            if total_fixed <= 0:
                self.log_error(f"Monthly OpEx must be strictly positive, got {total_fixed}")
            else:
                print(f"  [PASS] Monthly Fixed OpEx is positive: ₹{total_fixed:,.2f}")

    def validate_markdown_links(self):
        """Check for broken relative file links in markdown files."""
        print("\n--- 4. Validating Markdown Relative Links ---")
        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        broken_links = 0
        total_links = 0

        for root, _, files in os.walk(self.repo_root):
            if any(p in root for p in [".git", "venv", ".venv", "__pycache__"]):
                continue
            for fname in files:
                if fname.endswith(".md"):
                    fpath = os.path.join(root, fname)
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    matches = link_pattern.findall(content)
                    for text, target in matches:
                        target = target.strip()
                        # Ignore external links, anchor links, and mailto
                        if target.startswith("http://") or target.startswith("https://") or target.startswith("#") or target.startswith("mailto:"):
                            continue
                        
                        # Strip anchor #...
                        clean_target = target.split("#")[0]
                        if not clean_target:
                            continue

                        # Resolve target path relative to current markdown file
                        if clean_target.startswith("file:///"):
                            # Local file uri
                            target_abs = clean_target.replace("file:///", "").replace("/", os.sep)
                        elif clean_target.startswith("/"):
                            target_abs = os.path.join(self.repo_root, clean_target.lstrip("/"))
                        else:
                            target_abs = os.path.normpath(os.path.join(root, clean_target))

                        total_links += 1
                        if not os.path.exists(target_abs):
                            self.log_warning(f"Broken relative link in {os.path.relpath(fpath, self.repo_root)}: '{target}'")
                            broken_links += 1

        print(f"Scanned {total_links} relative links. Found {broken_links} broken references.")

    def run_all(self) -> bool:
        self.validate_required_structure()
        self.validate_json_schemas()
        self.validate_financial_consistency()
        self.validate_markdown_links()

        print("\n================ VALIDATION SUMMARY ================")
        print(f"Total Errors:   {len(self.errors)}")
        print(f"Total Warnings: {len(self.warnings)}")

        if self.errors:
            print("\nValidation FAILED with errors:")
            for err in self.errors:
                print(f"  - {err}")
            return False
        else:
            print("\nValidation PASSED successfully with 0 errors!")
            return True


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    validator = RepoValidator(repo_root)
    success = validator.run_all()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
