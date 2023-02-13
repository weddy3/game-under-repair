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
sample_hole = {'1': [('T', 452), ('F', 164), ('NA'), ('P', 24)]}

sgOTT = 0

# TODO obviously need a cleaner way to group all shots relative to a SG group (solved above?)
# Might not need to store 'T' and 'P' since order, depends on DB creation I guess
# ie all shots that would be in the approach category togther while maintaining data, ('F', 250, 'F', 110)
# to make the belove cleaner
# Could do something similar to below and assume this "lineraity", ie all tee shots, then all approach, then all short, then putting
# would obviously have to populate nulls for when a ctageory has no shots for that hole, but I think would remove a loop and if check

for hole in sample_hole:
    for group in sample_hole[hole]:
        if group[0] == 'T':
            # SG Off The Tee for a hole is equal to expected number of strokes for that given yardage minus
            # the expected number of strokes to hole out for the following shot minus 1 to account for the actual shot
            sgOTT += lookup_tee[group[1]] - lookup_fairway[sample_hole[hole][1][1]] - 1

print(round(sgOTT,2))
