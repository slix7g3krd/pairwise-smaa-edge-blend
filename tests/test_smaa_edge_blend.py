import pytest
import graphics.smaa_edge_blend as mod

CASES = [
    ("threshold_by_colorspace", (1,)),
    ("lut_full_precision", (1,)),
    ("clip_by_motion", (1,)),
    ("edges_at_output_res", (1,)),
    ("blend_in_linear", (1,)),
    ("fixed_pipeline_order", (1,)),
    ("load", (1,)),
    ("detect", (1,)),
    ("blend", (1,)),
    ("resolve", (1,)),
    ("validate_smaa", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
