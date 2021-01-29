from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get outcome description data
outcome_description = get_outcome_lvl1("OutcomeDescription")
outcome_description_df = pd.DataFrame(outcome_description)

# name each column (number depends on outcome number)
outcome_description_df.columns = [
    "out_desc_"+'{}'.format(column+1) for column in outcome_description_df.columns]

""" outcome_description_df = outcome_description_df.fillna("NA") """

outcome_description_df = outcome_description_df.replace(
    r'^\s*$', "NA", regex=True)

# replace problematic text
outcome_description_df.replace('\r', ' ', regex=True, inplace=True)
outcome_description_df.replace('\n', ' ', regex=True, inplace=True)
outcome_description_df.replace(':', ' ', regex=True, inplace=True)
outcome_description_df.replace(';', ' ', regex=True, inplace=True)

# save to disk
""" outcome_description_df.to_csv("outcomedescription.csv", index=False) """