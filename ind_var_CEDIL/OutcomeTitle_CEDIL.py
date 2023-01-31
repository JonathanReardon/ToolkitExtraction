from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get outcome title data
outcome_title = get_outcome_lvl1("Title")
outcome_title_df = pd.DataFrame(outcome_title)

# name each column (number depends on outcome number)
outcome_title_df.columns = [
    "out_tit_"+'{}'.format(column+1) for column in outcome_title_df.columns]

""" outcome_label_text_df.fillna("NA", inplace=True) """

# replace problematic text
outcome_title_df = outcome_title_df.replace(r'^\s*$', "NA", regex=True)

# save to disk
""" outcome_title_df.to_csv("out_tit.csv", index=False) """

print(outcome_title_df)