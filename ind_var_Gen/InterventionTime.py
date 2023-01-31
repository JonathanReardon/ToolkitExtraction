from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_time_output
import pandas as pd

# load json file
load_json()

###########################################
# DIGITAL TECHNOLOGY INTERVENTION INCLUSION
###########################################

# Get Intervention Time main data
InterventionTime = get_data(intervention_time_output)
InterventionTime_df = pd.DataFrame(InterventionTime)
InterventionTime_df = InterventionTime_df.T
InterventionTime_df.columns = ["int_when_raw"]

# Get Intervention Time highlighted text
InterventionTime_HT = highlighted_text(intervention_time_output)
InterventionTime_HT_df = pd.DataFrame(InterventionTime_HT)
InterventionTime_HT_df = InterventionTime_HT_df.T
InterventionTime_HT_df.columns = ["int_when_ht"]

# Get Intervention Time user comments
InterventionTime_Comments = comments(intervention_time_output)
InterventionTime_Comments_df = pd.DataFrame(InterventionTime_Comments)
InterventionTime_Comments_df = InterventionTime_Comments_df.T
InterventionTime_Comments_df.columns = ["int_when_info"]

# concatenate data frames
intervention_time_df = pd.concat([
    InterventionTime_df, 
    InterventionTime_HT_df, 
    InterventionTime_Comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_time_df.replace('\r',' ', regex=True, inplace=True)
intervention_time_df.replace('\n',' ', regex=True, inplace=True)
intervention_time_df.replace(':',' ',  regex=True, inplace=True)
intervention_time_df.replace(';',' ',  regex=True, inplace=True)

# fill blanks with NA
intervention_time_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_time_df.to_csv("InterventionTime.csv", index=False) """