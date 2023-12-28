import sys
from collections import defaultdict

# adds sg_utils functions to path, have to do this due to pytest path issues
sys.path.append("../")


from sg_utils import (
    get_expected_strokes,
    add_expected_strokes,
    get_sg_for_shot,
    convert_raw_input_to_shot,
)
from shot import Shot


# TODO potentially add more asserts for each function, although these may be obselete when moving to website
# TODO look into class based tests?
# TODO need more edge case testing around penalty strokes, de-greening, etc

##### Testing sg_utils functions #####


# --------------------------------------------------
def test_get_expected_strokes_tee():
    assert get_expected_strokes("T", 450) == 4.22


# --------------------------------------------------
def test_get_expected_strokes_fairway():
    assert get_expected_strokes("F", 116) == 2.86


# --------------------------------------------------
def test_get_expected_strokes_rough():
    assert get_expected_strokes("R", 166) == 3.28


# --------------------------------------------------
def test_get_expected_strokes_sand():
    assert get_expected_strokes("S", 305) == 4.12


# --------------------------------------------------
def test_get_expected_strokes_recovery():
    assert get_expected_strokes("X", 157) == 3.81


# --------------------------------------------------
def test_get_expected_strokes_putt():
    assert get_expected_strokes("P", 33) == 1.99


# --------------------------------------------------
# TODO fix this test/ reqrite class, can't create shot object and pass expected shots to hold out without calling the set_expected_shots_function
# def test_add_expected_strokes():
#     input_dict = {
#         "1": [Shot(1, "T", 400), Shot(2, "F", 100), Shot(3, "P", 10)],
#         "2": [Shot(1, "F", 150), Shot(2, "P", 25)],
#     }
#     output_dict = {
#         "1": [
#             Shot(1, "T", 400, False, expected_strokes_to_hole_out=4.01),
#             #Shot(2, "F", 100, False, 2.80),
#             #Shot(3, "P", 10, False, 1.5),
#         ]#,
#         #"2": [Shot(1, "F", 150, False, 2.98), Shot(2, "P", 25, False, 1.89)],
#     }

#     assert add_expected_strokes(input_dict) == output_dict


# --------------------------------------------------
def test_get_sg_for_shot_no_penalty():
    assert get_sg_for_shot(5.23, 4.20, False) == 0.03


# --------------------------------------------------
def test_get_sg_for_shot_with_penalty():
    assert get_sg_for_shot(3.00, 2.00, True) == -1.0


# --------------------------------------------------
# TODO once again want to test edge cases more rigourously
# TODO fix this
def test_convert_raw_input_to_shot():
    raw_input = "1:[1,'T',400],[2,'F',100],[3,'P',10];2:[1,'F',150],[2,'P',25]"
    output = {
        "1": [
            Shot(1, "T", 400),
            Shot(2, "F", 100),
            Shot(3, "P", 10),
        ],
        "2": [Shot(1, "F", 150), Shot(2, "P", 25)],
    }
    dd_output = defaultdict(list, output)

    assert convert_raw_input_to_shot(raw_input) == dd_output
