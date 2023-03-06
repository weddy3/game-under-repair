import pandas as pd
from collections import Counter
from pprint import pprint

nonputting_df = pd.read_csv('/Users/wil/Code/golf/touraverages/NonPutting.csv')
putting_df = pd.read_csv('/Users/wil/Code/golf/touraverages/Putting.csv')

rounded_nonputting_df = nonputting_df.round(2)
rounded_putting_df = putting_df.round(2)

lookup_tee = dict(zip(rounded_nonputting_df.Distance, rounded_nonputting_df.TeeExt))
lookup_fairway = dict(zip(rounded_nonputting_df.Distance, rounded_nonputting_df.FairwayExt))
lookup_rough = dict(zip(rounded_nonputting_df.Distance, rounded_nonputting_df.RoughExt))
lookup_sand = dict(zip(rounded_nonputting_df.Distance, rounded_nonputting_df.SandExt))
lookup_recovery = dict(zip(rounded_nonputting_df.Distance, rounded_nonputting_df.RecoveryExt))
# Uses a more recent graphic about putts by pros
lookup_pro1 = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsPro))
# Only found limited table, had to extrapolate to get all averages between 0 and 90
lookup_pro2 = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsProExt))
lookup_scratch = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsScratchExt))
lookup_90s = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPutts90Ext))


def strokes_gained(round_dict: dict) -> pd.DataFrame:
    sg_df = make_sg_df()

    # get expected number of strokes for each shot sublist
    for hole in round_dict.values():
        [shot.append(get_expected_strokes(shot[1], shot[2])) for shot in hole]

    # add strokes gained for each category to correct list
    for hole in round_dict:
        number_of_putts = sum(x.count('P') for x in round_dict[hole])
        for index, shot in enumerate(round_dict[hole]):
            current_shot_lie = shot[1]
            current_shot_distance = shot[2]
            current_expected_strokes = shot[3]

            # TODO account for penalty shots, hole outs, using only first putt, degreening (how to calculate SG of a putt that degreens)

            # not letting one putt holes through, fix
            if (index < len(round_dict[hole]) - 1):
                next_expected_strokes = round_dict[hole][index+1][3]
            else:
                # I think this accounts for hole outs, please test
                next_expected_strokes = 0

            if current_shot_distance < 100 and current_shot_lie != 'P':
                sg_df.at[(int(hole)-1), 'SG_ATG'].append(get_sg_nonputting(current_expected_strokes, next_expected_strokes))
            elif current_shot_distance >= 100 and current_shot_lie not in ['T', 'P']:
                sg_df.at[int(hole)-1, 'SG_APP'].append(get_sg_nonputting(current_expected_strokes, next_expected_strokes))
            elif current_shot_distance >= 100 and current_shot_lie == 'T':
                sg_df.at[int(hole)-1, 'SG_OTT'].append(get_sg_nonputting(current_expected_strokes, next_expected_strokes))
            else:
                # use only first putt, add test
                sg_df.at[int(hole)-1, 'SG_PUT'].append(get_sg_putting(current_expected_strokes, number_of_putts))
                            

    pprint(sg_df)

def get_sg_putting(current_expected_strokes: float, number_of_putts: float) -> float:
    """ Returns your SG for an individual shot for off the tee or approach"""
    return round(current_expected_strokes - number_of_putts, 2)


def get_sg_nonputting(current_expected_strokes: float, next_expected_strokes: float) -> float:
    """ Returns your SG for an individual shot for off the tee or approach"""
    return round(current_expected_strokes - next_expected_strokes - 1, 2)


def get_expected_strokes(shot_lie: str, shot_distance: int) -> float:
    """ Depending on the lie type, use the correct lookup dictionary to get the expected strokes to hole """

    strokes_to_hole = 0.0
    match shot_lie:
        case 'T':
            strokes_to_hole = lookup_tee[shot_distance]
        case 'F':
            strokes_to_hole = lookup_fairway[shot_distance]
        case 'R':
            strokes_to_hole = lookup_rough[shot_distance]
        case 'S':
            strokes_to_hole = lookup_sand[shot_distance]
        case 'X':
            strokes_to_hole = lookup_recovery[shot_distance]
        case 'P':
            strokes_to_hole = lookup_pro2[shot_distance]
    
    return strokes_to_hole


def make_sg_df():
    """Generate an empty pandas df to hold converted sg info"""

    data = {
        'SG_OTT': [[] for x in range(18)],
        'SG_APP': [[] for x in range(18)],
        'SG_ATG': [[] for x in range(18)],
        'SG_PUT': [[] for x in range(18)]
    }
    return pd.DataFrame(data=data)


def main():
    # each hole is represented by a tuple of shots
    # (shot number, lie type, distance remaining (yards, excpet for putting))
    # 'T' = Tee shot
    # 'F' = Fairway, 'R' = Rough, 'S' = Sand, 'X' = Recovery
    # 'P' = Putting
    round_dict = {
        '1': [[1, 'T', 452], [2, 'F', 164], [3, 'P', 24]],
        '2': [[1, 'F', 132], [2, 'R', 60], [3, 'S', 15], [4, 'P', 32], [5, 'P', 4]]
    }

    strokes_gained(round_dict)

if __name__ == '__main__':
    main()