from strokes_gained_logic.strokes_gained import *

one_putt_hole = {"1": [[1, "T", 452], [2, "F", 164], [3, "P", 24]]}

zero_putt_hole = {"1": [[1, "T", 452], [2, "F", 164]]}

two_putt_hole = {"1": [[1, "T", 452], [2, "F", 164], [3, "P", 24], [4, "P", 2]]}

degreen_hole = {
    "1": [[1, "T", 452], [2, "F", 164], [3, "P", 24], [4, "F", 7], [5, "P", 1]]
}

penalty_shot_hole = {
    "1": [
        [1, "T", 452],
        [2, "NA"],
        [3, "T", 452],
        [4, "F", 150],
        [5, "P", 7],
    ]
}


# TODO test for hole outs, degreening, penalty shots, other edge cases, multiple hole variations of data
def test_get_expected_strokes_tee():
    assert get_expected_strokes("T", 452) == 4.23


def test_get_expected_strokes_rough():
    assert get_expected_strokes("R", 123) == 3.12


def test_get_expected_strokes_fairway():
    assert get_expected_strokes("F", 150) == 2.98


def test_get_expected_strokes_sand():
    assert get_expected_strokes("S", 85) == 3.12


def test_get_expected_strokes_recovery():
    assert get_expected_strokes("X", 200) == 3.87


def test_get_sg_putting():
    assert get_sg_putting(2.3, 2) == 0.3
    assert get_sg_putting(2.0, 2) == 0.0
    assert get_sg_putting(1.7, 2) == -0.3


def test_get_sg_nonputting():
    assert get_sg_nonputting(4.5, 3.9) == -0.4
    assert get_sg_nonputting(3.9, 2.3) == 0.6
    assert get_sg_nonputting(4.0, 3.0) == 0


def test_add_expected_strokes():
    assert add_expected_strokes(one_putt_hole) == {
        "1": [[1, "T", 452, 4.23], [2, "F", 164, 3.03], [3, "P", 24, 1.88]]
    }


def test_get_category_OTT():
    get_category(500, "T") == "OTT"

    # add mmore categories
