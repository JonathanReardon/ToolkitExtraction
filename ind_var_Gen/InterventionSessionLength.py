from Main import load_json, comments, highlighted_text
from AttributeIDList import intervention_session_length_output
import pandas as pd

# load json file
load_json()

# get intervention session length highlighted text
InterventionSessionLength_HT = highlighted_text(intervention_session_length_output)
InterventionSessionLength_HT_df = pd.DataFrame(InterventionSessionLength_HT)
InterventionSessionLength_HT_df = InterventionSessionLength_HT_df.T
InterventionSessionLength_HT_df.columns = ["int_leng_ht"]

# get intervention session length user comments
InterventionSessionLength_Comments = comments(intervention_session_length_output)
InterventionSessionLength_Comments_df = pd.DataFrame(InterventionSessionLength_Comments)
InterventionSessionLength_Comments_df = InterventionSessionLength_Comments_df.T
InterventionSessionLength_Comments_df.columns = ["int_leng_info"]

# concatenate data frames
intervention_session_length_df = pd.concat([
    InterventionSessionLength_HT_df, 
    InterventionSessionLength_Comments_df
], axis=1, sort=False)

# remove problematic text
intervention_session_length_df.replace('\r',' ', regex=True, inplace=True)
intervention_session_length_df.replace('\n',' ', regex=True, inplace=True)
intervention_session_length_df.replace(':',' ',  regex=True, inplace=True)
intervention_session_length_df.replace(';',' ',  regex=True, inplace=True)

intervention_session_length_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_session_length_df.to_csv("InterventionSessionLength.csv", index=False) """