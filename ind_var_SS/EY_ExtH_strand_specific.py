from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import time_organsised
from AttributeIDList import addit_time_struct

import pandas as pd
import os
import sys

load_json()

""" data_files = sys.argv[1] """

# get additional time organised data
time_org = get_data(time_organsised)
time_org_df = pd.DataFrame(time_org)
time_org_df = time_org_df.T
time_org_df.columns = ["time_org"]

# get structure of additional time data
addit_time_struc= get_data(addit_time_struct)
addit_time_struc_df = pd.DataFrame(addit_time_struc)
addit_time_struc_df = addit_time_struc_df.T
addit_time_struc_df.columns = ["addit_time_struct"]



ey_eh_df = pd.concat([
    time_org_df,
    addit_time_struc_df
], axis=1, sort=False)

# fill blanks with NA
ey_eh_df.fillna("NA", inplace=True)

# save to disk
#ey_eh_df.to_csv("ey_pbl_ss_df.csv", index=False)

""" print(ey_eh_df[0:25]) """

print(ey_eh_df)