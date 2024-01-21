import pandas as pd
from shot import Shot
from collections import defaultdict

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
    """
    Converts raw input data to a dict of Shots keyed by hole number
    input: "1:[1,'T',400],[2,'F',100];2:[1,'T',300]"
    output: {'1': [Shot(...), Shot(...)], '2': Shot(...)}
    """

    # Default dict to represent eventual Shots keyed by hole number
    round_dict = defaultdict(list)

    # split each hole (hole number: shot info) into separate strings inside one list
    split_hole_data = raw_user_input.split(";")

    for hole in split_hole_data:
        # separates hole number from shot data list for each hole
        hole_number_and_shots = hole.split(":")
        # grabs just hole number for eventual keying of dict
        hole_number = hole_number_and_shots[0]
        # transform from messy, post-split data, to a list of of string lists
        # ['[shot_number, lie, distance_remaining_penalty]'] is the eventual goal
        shots = hole_number_and_shots[1].split(",[")
        fixed_shots = [shots[0]] + ["[" + x for x in shots[1:]]
        # takes list of string lists and turns to list of lists
        list_shots = [eval(i) for i in fixed_shots]
        for shot in list_shots:
            # check existence of penalty boolean
            penalty = True if len(shot) == 4 else False
            # create shot object based of the shot we are looking at for this hole
            current_shot = Shot(
                stroke=shot[0], lie=shot[1], distance_remaining=shot[2], penalty=penalty
            )
            # default dict allows use of append which creates if key doesn't exist, else appends
            round_dict[hole_number].append(current_shot)

    return round_dict
