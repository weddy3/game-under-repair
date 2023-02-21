import pandas as pd
from pprint import pprint

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

# This represents a single hole of shots, the 4 tuples in order represent each SG category
# from left to right, Off the Tee, Approach, Around the Green, Putting
# 'T' = Tee shot
# 'F' = Fairway, 'R' = Rough, 'S' = Sand, 'W' = Recovery
# 'P' = Putting
round_dict = {
    '1': [(1, 'T', 452), (2, 'F', 164), (3, 'P', 24)],
    '2': [(1, 'F', 132), (2, 'R', 60), (3, 'S', 15), (4, 'P', 32), (5, 'P', 4)]
}

sg_OTT = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
sg_approach = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
sg_short = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
sg_putting = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for hole in round_dict:
    for i in range(len(round_dict[hole])):
        # TODO account for penalty shots, hole outs, using only first putt, degreening

        next_shot_lie = round_dict[hole][i+1][1] if i+1 < len(round_dict[hole]) else 0
        next_shot_strokes_to_hole = 0
        match next_shot_lie:
            case 'T':
                print(round_dict[hole][i][2])
            case 'F':
                # clean this up via above to not have this if else
                next_shot_strokes_to_hole = lookup_fairway[round_dict[hole][i+1][2]] if i+1 < len(round_dict[hole]) else 0
            case 'R':
                print(round_dict[hole][i][2])
            case 'S':
                print(round_dict[hole][i][2])
            case 'X':
                print(round_dict[hole][i][2])
            case 'P':
                print(round_dict[hole][i][2])

        current_shot_lie = round_dict[hole][i][1]
        match current_shot_lie:
            case 'T':
                # maybe look up why this decimal is getting thrown off and fix earlier?
                sg_OTT[int(hole)-1].append(round(lookup_tee[round_dict[hole][i][2]] - next_shot_strokes_to_hole - 1, 2))
            case 'F':
                print(round_dict[hole][i][2])
            case 'R':
                print(round_dict[hole][i][2])
            case 'S':
                print(round_dict[hole][i][2])
            case 'X':
                print(round_dict[hole][i][2])
            case 'P':
                print(round_dict[hole][i][2])

print(sg_OTT)