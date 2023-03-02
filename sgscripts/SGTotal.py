import pandas as pd

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

# TODO break down into smaller more testable functions

def strokes_gained(round_dict: dict) -> list:
    sg_OTT = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    sg_approach = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    sg_short = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    sg_putting = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    # get expected number of strokes for each shot sublist
    for hole in round_dict.values():
        [shot.append(get_expected_strokes(shot[1], shot[2])) for shot in hole]

    #print(round_dict)

    for hole in round_dict:
        for index, shot in enumerate(round_dict[hole]):
            current_shot_lie = shot[1]
            current_shot_distance = shot[2]

            # TODO account for penalty shots, hole outs, using only first putt, degreening (how to calculate SG of a putt that degreens), <100 yards on tee shot, which SG category
            # this doesnt account for degreening, this also skews for second putts, not sure if we want to ignore all putts after first

            if (index < len(round_dict[hole]) - 1):
                next_strokes_to_hole = round_dict[hole][index+1][3]
                match current_shot_lie:
                    case 'T':
                        # maybe look up why this decimal is getting thrown off and fix earlier?
                        sg_OTT[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                    case 'F':
                        # need to check distance to determine SG category
                        if current_shot_distance > 99:
                            sg_approach[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                        else:
                            sg_short[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                    case 'R':
                        if current_shot_distance > 99:
                            sg_approach[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                        else:
                            sg_short[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                    case 'S':
                        if current_shot_distance > 99:
                            sg_approach[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                        else:
                            sg_short[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                    case 'X':
                        if current_shot_distance > 99:
                            sg_approach[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                        else:
                            sg_short[int(hole)-1].append(round(shot[3] - next_strokes_to_hole - 1, 2))
                    case 'P':
                        pass
                        #sg_putting[int(hole)-1].append(round(shot[3] - next(shot[3]), 2))

    print(sg_OTT)
    print(sg_approach)
    print(sg_short)
    # print(sg_putting)

    # # sg_total calculations here, by hole or just by category then total?   


def get_expected_strokes(next_shot_lie: str, next_shot_distance: int) -> float:
    """ Depending on the lie type, use the correct lookup dictionary to get the expected strokes to hole """

    strokes_to_hole = 0.0
    match next_shot_lie:
        case 'T':
            strokes_to_hole = lookup_tee[next_shot_distance]
        case 'F':
            strokes_to_hole = lookup_fairway[next_shot_distance]
        case 'R':
            strokes_to_hole = lookup_rough[next_shot_distance]
        case 'S':
            strokes_to_hole = lookup_sand[next_shot_distance]
        case 'X':
            strokes_to_hole = lookup_recovery[next_shot_distance]
        case 'P':
            strokes_to_hole = lookup_pro2[next_shot_distance]
    
    return strokes_to_hole


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