from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_focus_output
import pandas as pd

# load json file
load_json()

# get intervention focus data
InterventionFocus = get_data(intervention_focus_output)
InterventionFocus_df = pd.DataFrame(InterventionFocus)
InterventionFocus_df = InterventionFocus_df.T
InterventionFocus_df.columns = ["int_part_raw"]

# get intervention focus highlighted text
InterventionFocus_HT = highlighted_text(intervention_focus_output)
InterventionFocus_HT_df = pd.DataFrame(InterventionFocus_HT)
InterventionFocus_HT_df  = InterventionFocus_HT_df.T
InterventionFocus_HT_df.columns = ["int_part_ht"]

# get intervention focus user comments
InterventionFocus_Comments = comments(intervention_focus_output)
InterventionFocus_Comments_df = pd.DataFrame(InterventionFocus_Comments)
InterventionFocus_Comments_df  = InterventionFocus_Comments_df.T
InterventionFocus_Comments_df.columns = ["int_part_info"]

# concatenate data frames
intervention_focus_df = pd.concat([
    InterventionFocus_df, 
    InterventionFocus_HT_df, 
    InterventionFocus_Comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_focus_df.replace('\r',' ', regex=True, inplace=True)
intervention_focus_df.replace('\n',' ', regex=True, inplace=True)
intervention_focus_df.replace(':',' ', regex=True, inplace=True)
intervention_focus_df.replace(';',' ', regex=True, inplace=True)

# fill blanks with NA
intervention_focus_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_focus_df.to_csv("InterventionFocus.csv", index=False) """