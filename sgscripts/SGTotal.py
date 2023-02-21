import pandas as pd

def main():
    nonputting_df = pd.read_csv('touraverages/NonPutting.csv')
    putting_df = pd.read_csv('touraverages/Putting.csv')

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

    # each hole is represented by a tuple of shots
    # (shot number, lie type, distance remaining (yards, excpet for putting))
    # 'T' = Tee shot
    # 'F' = Fairway, 'R' = Rough, 'S' = Sand, 'X' = Recovery
    # 'P' = Putting
    round_dict = {
        '1': [(1, 'T', 452), (2, 'F', 164), (3, 'P', 24)],
        '2': [(1, 'F', 132), (2, 'R', 60), (3, 'S', 15), (4, 'P', 32), (5, 'P', 4)]
    }

    sg_OTT = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    sg_approach = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    sg_short = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    sg_putting = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    for hole in round_dict:
        for i in range(len(round_dict[hole])):
            # TODO account for penalty shots, hole outs, using only first putt, degreening (how to calculate SG of a putt that degreens), <100 yards on tee shot, which SG category
            # TODO assess if top match block is necessary/ optimal?

            next_shot_lie = round_dict[hole][i+1][1] if i+1 < len(round_dict[hole]) else 0
            next_shot_strokes_to_hole = 0
            match next_shot_lie:
                case 'T':
                    # account for penalty shots here?
                    print(round_dict[hole][i][2])
                case 'F':
                    # clean this up via above to not have this if else
                    next_shot_strokes_to_hole = lookup_fairway[round_dict[hole][i+1][2]] if i+1 < len(round_dict[hole]) else 0
                case 'R':
                    next_shot_strokes_to_hole = lookup_rough[round_dict[hole][i+1][2]] if i+1 < len(round_dict[hole]) else 0
                case 'S':
                    next_shot_strokes_to_hole = lookup_sand[round_dict[hole][i+1][2]] if i+1 < len(round_dict[hole]) else 0
                case 'X':
                    next_shot_strokes_to_hole = lookup_recovery[round_dict[hole][i+1][2]] if i+1 < len(round_dict[hole]) else 0
                # case 'P':
                #     # handle degreening here? Remove?
                #     print(-100)

            current_shot_lie = round_dict[hole][i][1]
            current_shot_distance = round_dict[hole][i][2]
            # this doesnt account for degreening, this also skews for second putts, not sure if we want to ignore all putts after first
            number_of_putts = sum([1 for shot in round_dict[hole] if shot[1] == 'P'])
            match current_shot_lie:
                case 'T':
                    # maybe look up why this decimal is getting thrown off and fix earlier?
                    sg_OTT[int(hole)-1].append(round(lookup_tee[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                case 'F':
                    # need to check distance to determine SG category
                    if current_shot_distance > 99:
                        sg_approach[int(hole)-1].append(round(lookup_fairway[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                    else:
                        sg_short[int(hole)-1].append(round(lookup_fairway[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                case 'R':
                    if current_shot_distance > 99:
                        sg_approach[int(hole)-1].append(round(lookup_rough[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                    else:
                        sg_short[int(hole)-1].append(round(lookup_rough[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                case 'S':
                    if current_shot_distance > 99:
                        sg_approach[int(hole)-1].append(round(lookup_sand[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                    else:
                        sg_short[int(hole)-1].append(round(lookup_sand[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                case 'X':
                    if current_shot_distance > 99:
                        sg_approach[int(hole)-1].append(round(lookup_recovery[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                    else:
                        sg_short[int(hole)-1].append(round(lookup_recovery[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
                case 'P':
                    sg_putting[int(hole)-1].append(round(lookup_pro2[current_shot_distance] - number_of_putts, 2))

    print(sg_OTT)
    print(sg_approach)
    print(sg_short)
    print(sg_putting)

    # sg_total calculations here, by hole or just by category then total?

if __name__ == '__main__':
    main()