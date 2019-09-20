import pandas as pd
import numpy as np
import argparse

pd.options.mode.chained_assignment = None

parser = argparse.ArgumentParser(description='test file for df')
parser.add_argument('-num_bins', default=3, help='number of pressure bins to use', type=int) # that sets the default argument to 2
parser.add_argument('-maxp', default=1200, help='maximum pressure to include', type=int) # that sets the default argument to 2
args = parser.parse_args()

df_unfiltered = pd.read_pickle('WATER_DATA_FULL.pkl')
df = df_unfiltered
df = df_unfiltered.replace(-9.0, np.nan)
# df.at[0, 0] = '#HOT' #this is to meet header requirements for LSA
df['CTDPRS'] = df['CTDPRS'].mask(df['CTDPRS'] < 0, -9.0) #instead of np.nan
df['CTDPRS'] = df['CTDPRS'].mask(df['CTDPRS'] > args.maxp, -9.0) #instead of np.nan
df = df.drop(df.loc[df['CTDPRS'].isnull()].index)
df['pbin'] = df['CTDPRS'] // (args.maxp / args.num_bins)


time_axis = []
for c in range(1, max(df['CRUISENO'])):
  cruise = df.loc[df['CRUISENO'] == c] #.copy()
  cruise_list = []
  for b in range(args.num_bins):
    bin = cruise.loc[cruise['pbin'] == b].drop(columns=['pbin']).mean(skipna=True).add_suffix("bin" + str(b))
    cruise_list.append(bin)
  time_axis.append(pd.concat(cruise_list))

#pd.concat(time_axis, axis=1).to_csv('lsa.csv')

pd.concat(time_axis, axis = 1).to_csv('lsa.txt')
  
# cruise1['pbin'] = cruise1.apply(lambda row: row['CTDPRS'] // (2000/args.num_bins), axis=1)

# time_series = 

# for val in full_water['CRUISENO']:
#     while prev!= val:
