"""
Unit Tests for Repository Structural Integrity
==============================================
Validates that mandatory directories, required files, and links exist.
"""

import pytest
import os
import sys

pkg_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tools", "validation"))
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

from validate_repo import RepoValidator


def test_repo_integrity_suite():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    validator = RepoValidator(repo_root)
    success = validator.run_all()
    assert success is True, f"Validation failed with errors: {validator.errors}"
    assert len(validator.errors) == 0
