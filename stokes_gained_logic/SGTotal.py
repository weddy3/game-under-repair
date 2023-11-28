import pandas as pd
from collections import Counter
from pprint import pprint
from shot import Shot

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
    """
    INPUT: round_dict -> Dictionary containing shot classes
    OUTPUT: sg_df -> dataframe which contains SG shot value for each of your shots for every hole
    TODO account for penalty strokes
    """
    sg_df = make_sg_df()

    add_expected_strokes(round_dict)

    # need to figure out what can be put in shot class, how we still want to look forward to next shot
    # do this inside of a round class, or do we simply have a list of shots? <-- probs this for now

    # TODO need to remove mopst oif the index, figuring out how to add in expected shots nicely

    for hole in round_dict:
        number_of_putts = 0
        for index, shot in enumerate(round_dict[hole]):
            # gets index of first P, gets remaining length for nuumber of putts, my solution to degreening
            if 'P' in shot:
                number_of_putts = len(round_dict[hole][index:])
            current_shot_lie = shot.lie
            current_shot_distance = shot.distnace_remaining
            current_expected_strokes = shot[3]

            if (index < len(round_dict[hole]) - 1):
                next_expected_strokes = round_dict[hole][index+1][3]
            else:
                next_expected_strokes = 0

            category = shot.get_category()

            match category:
                case 'ATG':
                    sg_df.at[(int(hole)-1), 'SG_ATG'].append(get_sg_nonputting(current_expected_strokes, next_expected_strokes))
                case 'APP':
                    sg_df.at[int(hole)-1, 'SG_APP'].append(get_sg_nonputting(current_expected_strokes, next_expected_strokes))
                case 'OTT':
                    sg_df.at[int(hole)-1, 'SG_OTT'].append(get_sg_nonputting(current_expected_strokes, next_expected_strokes))
                case 'PUT':
                    sg_df.at[int(hole)-1, 'SG_PUT'].append(get_sg_putting(current_expected_strokes, number_of_putts))
                    print(number_of_putts)
                    break
                            
    return sg_df

def add_expected_strokes(round: dict) -> dict:
    """Appends expected number of strokes to hole out for PGA player to the round data dict"""
    for hole in round.values():
        [shot.append(get_expected_strokes(shot[1], shot[2])) for shot in hole]

    return round


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
    # each hole is represented by list of shot classes
    # (shot number, lie type, distance remaining (yards, excpet for putting))
    # 'T' = Tee shot
    # 'F' = Fairway, 'R' = Rough, 'S' = Sand, 'X' = Recovery
    # 'P' = Putting
    round_dict = {
        '1': [Shot(1, 'T', 400), Shot(2, 'F', 100), Shot(3, 'P', 10)],
        '2': [Shot(1, 'T', 400), Shot(2, 'F', 100), Shot(3, 'P', 10)],
        '3': [Shot(1, 'T', 400), Shot(2, 'F', 100), Shot(3, 'P', 10)]
    }

    sg_df = strokes_gained(round_dict)
    #pprint(sg_df)

if __name__ == '__main__':
    main()