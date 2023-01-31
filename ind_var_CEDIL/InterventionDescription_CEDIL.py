from Main import load_json, comments, highlighted_text
from AttributeIDList import intervention_description_CEDIL
import pandas as pd

# load json file
load_json()

# get intervention description highlighted text
Intervention_DescriptionHT = highlighted_text(intervention_description_CEDIL)
Intervention_DescriptionHT_df = pd.DataFrame(Intervention_DescriptionHT)
Intervention_DescriptionHT_df = Intervention_DescriptionHT_df.T
Intervention_DescriptionHT_df.columns=["int_desc_ht"]

# get intervention description user comments
Intervention_Description_Comments = comments(intervention_description_CEDIL)
Intervention_Description_Comments_df = pd.DataFrame(Intervention_Description_Comments)
Intervention_Description_Comments_df = Intervention_Description_Comments_df.T
Intervention_Description_Comments_df.columns=["int_desc_info"]

# concatenate dataframes
intervention_description_df = pd.concat([
    Intervention_DescriptionHT_df, 
    Intervention_Description_Comments_df
], axis=1, sort=False)

# remove problematic text
intervention_description_df.replace('\r',' ', regex=True, inplace=True)
intervention_description_df.replace('\n',' ', regex=True, inplace=True)
intervention_description_df.replace(':',' ', regex=True, inplace=True)
intervention_description_df.replace(';',' ', regex=True, inplace=True)

# replace blanks with NA
intervention_description_df.fillna("NA", inplace=True)

# save to disk
""" intervention_description_df.to_csv("InterventionDescription.csv", index=False) """

print(intervention_description_df)