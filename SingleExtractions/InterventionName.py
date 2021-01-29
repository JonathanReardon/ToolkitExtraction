from Main import load_json, comments, highlighted_text
from AttributeIDList import intervention_name_output
import pandas as pd

# load json file
load_json()

# get intervention name highlighted text
Intervention_NameHT = highlighted_text(intervention_name_output)
Intervention_NameHT_df = pd.DataFrame(Intervention_NameHT)
Intervention_NameHT_df = Intervention_NameHT_df.T
Intervention_NameHT_df.columns=["int_name_ht"]

# get intervention name user comments
Intervention_Name_Comments = comments(intervention_name_output)
Intervention_Name_Comments_df = pd.DataFrame(Intervention_Name_Comments)
Intervention_Name_Comments_df = Intervention_Name_Comments_df.T
Intervention_Name_Comments_df.columns=["int_name_info"]

# concatenate dataframes
intervention_name_df = pd.concat([
    Intervention_NameHT_df, 
    Intervention_Name_Comments_df
], axis=1, sort=False)

# replace problematic text
intervention_name_df.replace('\r',' ', regex=True, inplace=True)
intervention_name_df.replace('\n',' ', regex=True, inplace=True)
intervention_name_df.replace(':',' ', regex=True, inplace=True)
intervention_name_df.replace(';',' ', regex=True, inplace=True)

# fill blanks with NA
intervention_name_df.fillna("NA", inplace=True)

# save to disk
""" intervention_name_df.to_csv("InterventionName.csv", index=False) """