from SGTotal import strokes_gained, get_expected_strokes, get_sg_nonputting, get_sg_putting
import datatest as dt

one_putt_hole = {
        '1': [[1, 'T', 452], [2, 'F', 164], [3, 'P', 24]]
}

zero_putt_hole = {
    '1': [[1, 'T', 452], [2, 'F', 164]]
}

two_putt_hole = {
    '1': [[1, 'T', 452], [2, 'F', 164], [3, 'P', 24], [4, 'P', 2]]
}

degreen_hole = {
    '1': [[1, 'T', 452], [2, 'F', 164], [3, 'P', 24] , [4, 'F', 7], [5, 'P', 1]]
}

penalty_shot_hole = {
    '1': [[1, 'T', 452], [2, 'NA'], [3, 'T', 452], [4, 'F', 150] , [5, 'P', 7],]
}


def test_get_expected_strokes_tee():
    assert get_expected_strokes('T', 452) == 4.23
    

def test_get_expected_strokes_rough():
    assert get_expected_strokes('R', 123) == 3.12


def test_get_expected_strokes_fairway():
    assert get_expected_strokes('F', 150) == 2.98


def test_get_expected_strokes_sand():
    assert get_expected_strokes('S', 85) == 3.12


def test_get_expected_strokes_recovery():
    assert get_expected_strokes('X', 200) == 3.87

def test_get_sg_putting():
    assert get_sg_putting(2.3, 2) == .3
    assert get_sg_putting(2.0, 2) == 0.0
    assert get_sg_putting(1.7, 2) == -.3

def test_get_sg_nonputting():
    assert get_sg_nonputting(4.5, 3.9) == -.4
    assert get_sg_nonputting(3.9, 2.3) == .6
    assert get_sg_nonputting(4.0, 3.0) == 0


# test for output of strokes_gained, ie correct SG in each list
# test all edge cases here