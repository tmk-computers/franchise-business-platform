"""
Unit Tests for JSON Schemas
===========================
Validates JSON configuration files against schemas in schemas/.
"""

import pytest
import os
import json
from jsonschema import validate, ValidationError

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load_json(rel_path):
    fpath = os.path.join(REPO_ROOT, rel_path)
    with open(fpath, "r", encoding="utf-8") as f:
        return json.load(f)


def test_client_schema_validation():
    schema = load_json("schemas/client.schema.json")
    client_data = load_json("clients/tmk-it-solutions/profile/client.json")
    # Should validate without error
    validate(instance=client_data, schema=schema)


def test_product_catalog_schema_validation():
    schema = load_json("schemas/product.schema.json")
    catalog_data = load_json("clients/tmk-it-solutions/products/products-catalog.json")
    validate(instance=catalog_data, schema=schema)
    assert len(catalog_data["products"]) == 6


def test_financial_assumptions_schema_validation():
    schema = load_json("schemas/financial-assumptions.schema.json")
    assumptions_data = load_json("clients/tmk-it-solutions/financial-models/assumptions.json")
    validate(instance=assumptions_data, schema=schema)


def test_revenue_sharing_schema_validation():
    schema = load_json("schemas/revenue-sharing.schema.json")
    rev_data = load_json("clients/tmk-it-solutions/franchise-model/revenue-sharing-config.json")
    validate(instance=rev_data, schema=schema)


def test_invalid_client_schema_fails():
    schema = load_json("schemas/client.schema.json")
    invalid_data = {
        "clientId": "INVALID_UPPERCASE",
        "legalName": "Missing Required Fields"
    }
    with pytest.raises(ValidationError):
        validate(instance=invalid_data, schema=schema)
