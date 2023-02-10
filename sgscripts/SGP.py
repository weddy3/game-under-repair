import pandas as pd

putting_df = pd.read_csv('touraverages/Putting.csv')

rounded_putting_df = putting_df.round(2)

# Uses a more recent graphic about putts by pros
lookup_pro1 = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsPro))
# Only found limited table, had to extrapolate to get all averages between 0 and 90
lookup_pro2 = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsProExt))
lookup_scratch = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPuttsScratchExt))
lookup_90s = dict(zip(rounded_putting_df.Distance, rounded_putting_df.AvgPutts90Ext))

# Sample putting round from book, first position is number of putts, second is distance of first putt
tigers_round = [[1,4],[1,3],[2,3],[1,3],[1,1],[1,6],[2,22],[2,45],[2,6],[1,12],[2,4],[2,42],[2,15],[1,6],[1,5],[1,4],[2,13],[2,13]]

# calculate sg for round related list
sg = sum([lookup_pro2[hole[1]] - hole[0] for hole in tigers_round])

print(round(sg, 2))