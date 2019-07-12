import pandas as pd
import numpy as np
import argparse

pd.options.mode.chained_assignment = None

parser = argparse.ArgumentParser(description='test file for df')
parser.add_argument('num_bins', action='store_true', default=2, help='number of pressure bins to use') # that sets the default argument to 2
args = parser.parse_args()

df_unfiltered = pd.read_pickle('WATER_DATA_FULL.pkl')
df = df_unfiltered.replace(-9.0, np.nan)
df['CTDPRS'] = df['CTDPRS'].mask(df['CTDPRS'] < 0, np.nan)
df['CTDPRS'] = df['CTDPRS'].mask(df['CTDPRS'] > 2000, np.nan)
df = df.drop(df.loc[df['CTDPRS'].isnull()].index)
df['pbin'] = df['CTDPRS'] // (2000 / args.num_bins)

for i in range(args.num_bins)
  cruise1 = df.loc[df['CRUISENO'] == 1]
  cruise1 = cruise1.copy()


# cruise1['pbin'] = cruise1.apply(lambda row: row['CTDPRS'] // (2000/args.num_bins), axis=1)
bin1 = cruise1.loc[cruise1['pbin'] == 0] # get first pressure bin
print(bin1.mean(skipna=True))

# time_series = 

# for val in full_water['CRUISENO']:
#     while prev!= val:
