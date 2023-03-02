from SGTotal import strokes_gained, get_expected_strokes

dummy_round = {
        '1': [(1, 'T', 452), (2, 'F', 164), (3, 'P', 24)]
    }


def test_get_expetced_strokes_tee():
    assert get_expected_strokes('T', 452) == 4.23
    
def test_get_expetced_strokes_rough():
    assert get_expected_strokes('R', 123) == 3.12