import pandas as pd
from shot import Shot

# TODO clean up this mess
nonputting_df = pd.read_csv("/Users/wil/Code/golf/touraverages/NonPutting.csv")
putting_df = pd.read_csv("/Users/wil/Code/golf/touraverages/Putting.csv")

rounded_nonputting_df = nonputting_df.round(2)
rounded_putting_df = putting_df.round(2)

lookup_tee = dict(zip(rounded_nonputting_df.Distance, rounded_nonputting_df.TeeExt))
lookup_fairway = dict(
    zip(rounded_nonputting_df.Distance, rounded_nonputting_df.FairwayExt)
)
lookup_rough = dict(zip(rounded_nonputting_df.Distance, rounded_nonputting_df.RoughExt))
lookup_sand = dict(zip(rounded_nonputting_df.Distance, rounded_nonputting_df.SandExt))
lookup_recovery = dict(
    zip(rounded_nonputting_df.Distance, rounded_nonputting_df.RecoveryExt)
)
# Uses a more recent graphic about putts by pros
lookup_pro1 = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsPro))
# Only found limited table, had to extrapolate to get all averages between 0 and 90
lookup_pro2 = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsProExt))
lookup_scratch = dict(
    zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsScratchExt)
)
lookup_90s = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPutts90Ext))


def get_expected_strokes(shot_lie: str, shot_distance: int) -> float:
    """Depending on the lie type, use the correct lookup dictionary to get the expected strokes to hole"""

    strokes_to_hole = 0.0
    match shot_lie:
        case "T":
            strokes_to_hole = lookup_tee[shot_distance]
        case "F":
            strokes_to_hole = lookup_fairway[shot_distance]
        case "R":
            strokes_to_hole = lookup_rough[shot_distance]
        case "S":
            strokes_to_hole = lookup_sand[shot_distance]
        case "X":
            strokes_to_hole = lookup_recovery[shot_distance]
        case "P":
            strokes_to_hole = lookup_pro2[shot_distance]

    return strokes_to_hole


def add_expected_strokes(round: dict) -> dict:
    """Appends expected number of strokes to hole out for PGA player to the round data dict"""
    for hole in round.values():
        [
            shot.set_expected_strokes_to_hole_out(
                get_expected_strokes(shot.lie, shot.distance_remaining)
            )
            for shot in hole
        ]

    return round


def get_sg_for_shot(
    current_expected_strokes: float, next_expected_strokes: float, penalty: bool
) -> float:
    """Returns your SG for an individual shot for off the tee or approach"""
    if penalty:
        return round(current_expected_strokes - next_expected_strokes - 2, 2)

    else:
        return round(current_expected_strokes - next_expected_strokes - 1, 2)


def convert_raw_input_to_shot(raw_user_input: str) -> dict:
    """Converts raw input data to a dict of Shots keyed by hole number"""

    # split each hole into a string inside one list, print to see what this looks like
    holes = raw_user_input.split(';')

    # need to create an empty dict

    # for each hole in holes (list above), append a Shot object keyed by hole number

    # basically make the below
    # "1:(1,'T',400),(2,'F',100);2:(1,'T',300)"  (this is raw user input)
    # turn into
    #     # golf_round = {
    #     "1": [
    #         Shot(1, "T", 400),
    #         Shot(2, "F", 100),
    #     ],
    #     "2": [Shot(1, "T", 300)],
    # }

    # then return the dict and supply it as input to strokes_gained.py method
    

    return dict(raw_user_input)
