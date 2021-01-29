from Main import load_json, comments, highlighted_text
from AttributeIDList import intervention_duration_output
import pandas as pd

# load json file
load_json()

# get intervention duration highlighted text
InterventionDuration_HT = highlighted_text(intervention_duration_output)
InterventionDuration_HT_df = pd.DataFrame(InterventionDuration_HT)
InterventionDuration_HT_df = InterventionDuration_HT_df.T
InterventionDuration_HT_df.columns = ["int_dur_ht"]

# get intervention duration user comments
InterventionDuration_Comments = comments(intervention_duration_output)
InterventionDuration_Comments_df = pd.DataFrame(InterventionDuration_Comments)
InterventionDuration_Comments_df = InterventionDuration_Comments_df.T
InterventionDuration_Comments_df.columns = ["int_dur_info"]

# concatenate data frames
intervention_duration_df = pd.concat([
    InterventionDuration_HT_df, 
    InterventionDuration_Comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_duration_df.replace('\r',' ', regex=True, inplace=True)
intervention_duration_df.replace('\n',' ', regex=True, inplace=True)
intervention_duration_df.replace(':',' ',  regex=True, inplace=True)
intervention_duration_df.replace(';',' ',  regex=True, inplace=True)

# fill blanks with NA
intervention_duration_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_duration_df.to_csv("InterventionDuration.csv", index=False) """