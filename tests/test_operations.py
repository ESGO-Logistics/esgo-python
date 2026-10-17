"""The hand-written layer must cover the spec exactly.

When the API gains an endpoint, regenerate.yml updates openapi.json and these
tests fail until the operation is added to esgo._resources.OPERATIONS.
"""

import json
from pathlib import Path

import pytest

import esgo
from esgo._resources import OPERATIONS

SPEC = json.loads((Path(__file__).resolve().parent.parent / "openapi.json").read_text("utf-8"))


def _spec_operations():
    for path, item in SPEC["paths"].items():
        for method, op in item.items():
            if isinstance(op, dict) and "operationId" in op:
                yield op["operationId"], method.upper(), path, op


def _ref_name(schema):
    ref = (schema or {}).get("$ref", "")
    return ref.rsplit("/", 1)[-1] or None


def test_every_spec_operation_has_an_sdk_method():
    assert {op_id for op_id, *_ in _spec_operations()} == set(OPERATIONS)


@pytest.mark.parametrize("op_id, method, path, op", list(_spec_operations()))
def test_operation_matches_spec(op_id, method, path, op):
    sdk = OPERATIONS[op_id]
    assert (sdk.method, sdk.path) == (method, path)

    body = op.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema")
    assert (sdk.request.__name__ if sdk.request else None) == _ref_name(body)

    success = next(code for code in op["responses"] if code.startswith("2"))
    response = op["responses"][success]["content"]["application/json"]["schema"]
    assert sdk.response.__name__ == _ref_name(response)


@pytest.mark.parametrize("op_id", list(OPERATIONS))
def test_sdk_method_exists_in_both_styles(op_id):
    resource, method = OPERATIONS[op_id].sdk_method.split(".")
    client = esgo.Client(api_key="esgo_live_test")
    assert callable(getattr(getattr(client, resource), method))
    assert getattr(esgo, resource)._name == resource
