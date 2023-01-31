from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get outcome measure data
outcome_measure = get_outcome_lvl1("InterventionText")
outcome_measure_df = pd.DataFrame(outcome_measure)

# name each column (number depends on outcome number)
outcome_measure_df.columns = [
    "out_measure_"+'{}'.format(column+1) for column in outcome_measure_df.columns]

# fill blanks with NA
outcome_measure_df.fillna("NA", inplace=True)

# remove problematic text
outcome_measure_df = outcome_measure_df.replace(r'^\s*$', "NA", regex=True)

# save to disk
""" outcome_measure_df.to_csv("outcome_measure.csv", index=False) """

print(outcome_measure_df)