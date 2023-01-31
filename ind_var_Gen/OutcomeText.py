from Main import load_json, get_outcome_lvl1
import pandas as pd

# load json file
load_json()

# get outcome text data
outcome_text = get_outcome_lvl1("OutcomeText")
outcome_text_df = pd.DataFrame(outcome_text)

# round data to 4 decimal places
outcome_text_df = outcome_text_df.applymap(lambda x: round(
    x, 4) if isinstance(x, (int, float)) else x)

# name each column (number depends on outcome number)
outcome_text_df.columns = [
    "out_text_"+'{}'.format(column+1) for column in outcome_text_df.columns]

# fill blanks with NA
outcome_text_df.fillna("NA", inplace=True)

# replace problematic text
outcome_text_df = outcome_text_df.replace(r'^\s*$', "NA", regex=True)

# save to disk
""" outcome_text_df.to_csv("Outcome_Text.csv", index=False) """