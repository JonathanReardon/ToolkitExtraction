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

# replace problematic text
Intervention_Name_Comments_df.replace('\r', ' ', regex=True, inplace=True)
Intervention_Name_Comments_df.replace('\n', ' ', regex=True, inplace=True)
Intervention_Name_Comments_df.replace(':', ' ', regex=True, inplace=True)
Intervention_Name_Comments_df.replace(';', ' ', regex=True, inplace=True)

''' Intervention_Name_Comments_df.replace(',', '', regex=True, inplace=True)

Intervention_Name_Comments_df['int_name_info'] = Intervention_Name_Comments_df['int_name_info'].astype(str)
Intervention_Name_Comments_df['int_name_info'] = Intervention_Name_Comments_df['int_name_info'].apply(
    lambda x: "'" + str(x) + "'") '''

# concatenate dataframes
intervention_name_df = pd.concat([
    Intervention_NameHT_df, 
    Intervention_Name_Comments_df
], axis=1, sort=False)

# fill blanks with NA
intervention_name_df.fillna("NA", inplace=True)

# save to disk
""" intervention_name_df.to_csv("InterventionName.csv", index=False) """
