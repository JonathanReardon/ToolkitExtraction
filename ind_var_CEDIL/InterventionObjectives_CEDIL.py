from Main import load_json, comments, highlighted_text
from AttributeIDList import intervention_objectives_CEDIL
import pandas as pd

# load json file
load_json()

# Get Intervention Name highlighted text
Intervention_ObjectivesHT = highlighted_text(intervention_objectives_CEDIL)
Intervention_ObjectivesHT_df = pd.DataFrame(Intervention_ObjectivesHT)
Intervention_ObjectivesHT_df = Intervention_ObjectivesHT_df.T
Intervention_ObjectivesHT_df.columns=["int_objec_ht"]

# Get Intervention Description user comments
Intervention_Objectives_Comments = comments(intervention_objectives_CEDIL)
Intervention_Objectives_Comments_df = pd.DataFrame(Intervention_Objectives_Comments)
Intervention_Objectives_Comments_df = Intervention_Objectives_Comments_df.T
Intervention_Objectives_Comments_df.columns = ["int_objec_info"]

# concatenate data frames
intervention_objectives_df = pd.concat([
    Intervention_ObjectivesHT_df, 
    Intervention_Objectives_Comments_df
], axis=1, sort=False)

# remove problematic text
intervention_objectives_df.replace('\r',' ', regex=True, inplace=True)
intervention_objectives_df.replace('\n',' ', regex=True, inplace=True)
intervention_objectives_df.replace(':',' ', regex=True, inplace=True)
intervention_objectives_df.replace(';',' ', regex=True, inplace=True)

# fill blanks with NA
intervention_objectives_df.fillna("NA", inplace=True)

# save to disk
""" intervention_objectives_df.to_csv("InterventionObjectives.csv", index=False) """

print(intervention_objectives_df)