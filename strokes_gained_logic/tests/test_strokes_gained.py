from strokes_gained_logic.sg_utils import get_expected_strokes


##### Testing sg_utils functions #####

# --------------------------------------------------
def test_get_expected_strokes_tee():
    assert get_expected_strokes('T', 450) == 4.22

# --------------------------------------------------
