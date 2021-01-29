from Main import load_json, get_data, get_outcome_lvl2
from AttributeIDList import sample_output
import pandas as pd

# load json file
load_json()

# get sample data
sample = get_outcome_lvl2(sample_output)
sample_df = pd.DataFrame(sample)

# name each column (number depends on outcome number)
sample_df.columns = [
    "out_samp_" +'{}'.format(column+1) for column in sample_df.columns]

# get sample main check data
sample_main_check = get_data(sample_output)
sample_main_check_df = pd.DataFrame(sample_main_check)
sample_main_check_df = sample_main_check_df.T
sample_main_check_df.columns = ["main_check"]

# concatenate dataframes
all_variables = pd.concat([ 
    sample_df, 
    sample_main_check_df
], axis=1, sort=False)

# fill blanks with NA
all_variables.fillna("NA", inplace=True)

# save to disk
""" all_variables.to_csv("Sample.csv", index=False) """