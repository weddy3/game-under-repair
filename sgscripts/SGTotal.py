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
all_shots = {'1': [('T', 452), ('F', 164), ('NA'), ('P', 24)]}

sgOTT = 0

# TODO obviously need a cleaner way to group all shots relative to a SG group (solved above?)
# Might not need to store 'T' and 'P' since order, depends on DB creation I guess
# ie all shots that would be in the approach category togther while maintaining data, ('F', 250, 'F', 110)
# to make the below cleaner
# Could do something similar to below and assume this "lineraity", ie all tee shots, then all approach, then all short, then putting
# would obviously have to populate nulls for when a ctageory has no shots for that hole, but I think would remove a loop and if check

for hole in all_shots:
    for group in all_shots[hole]:
        if group[0] == 'T':
            # SG Off The Tee for a hole is equal to expected number of strokes for that given yardage minus
            # the expected number of strokes to hole out for the following shot minus 1 to account for the actual shot
            sgOTT += lookup_tee[group[1]] - lookup_fairway[all_shots[hole][1][1]] - 1


# conditonal for lie on approach and conditonals for checking for next value
sg_ott = round(sum([lookup_tee[all_shots[hole][0][1]] - lookup_fairway[all_shots[hole][1][1]] - 1 for hole in all_shots]), 2)
sg_approach = round(sum([lookup_fairway[all_shots[hole][1][1]] - lookup_pro2[all_shots[hole][3][1]] - 1 for hole in all_shots]), 2)
sg_atg = 0.0
sg_putting = round(sum([lookup_pro2[all_shots[hole][3][1]] - len(all_shots[hole][3]) + 1 for hole in all_shots]), 2)

sg_total = round(sg_ott + sg_approach + sg_atg + sg_putting, 2)
print(sg_total)