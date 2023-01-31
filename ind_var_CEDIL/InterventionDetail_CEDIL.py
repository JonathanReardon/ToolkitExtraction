from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_implementation_details_CEDIL
import pandas as pd

# load json file
load_json()

# get intervention implementation detail data
InterventionDetail = get_data(intervention_implementation_details_CEDIL)
InterventionDetail_df  = pd.DataFrame(InterventionDetail)
InterventionDetail_df = InterventionDetail_df.T
InterventionDetail_df.columns = ["int_fidel_raw"]

# get intervention implementation detail highlighted text
InterventionDetail_HT = highlighted_text(intervention_implementation_details_CEDIL)
InterventionDetail_HT_df = pd.DataFrame(InterventionDetail_HT)
InterventionDetail_HT_df = InterventionDetail_HT_df.T
InterventionDetail_HT_df.columns = ["int_fidel_ht"]

# get intervention implementation detail user comments
InterventionDetail_Comments = comments(intervention_implementation_details_CEDIL)
InterventionDetail_Comments_df = pd.DataFrame(InterventionDetail_Comments)
InterventionDetail_Comments_df = InterventionDetail_Comments_df.T
InterventionDetail_Comments_df.columns = ["int_fidel_info"]

# concatenate data frames
intervention_detail_df = pd.concat([
    InterventionDetail_df, 
    InterventionDetail_HT_df, 
    InterventionDetail_Comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_detail_df.replace('\r',' ', regex=True, inplace=True)
intervention_detail_df.replace('\n',' ', regex=True, inplace=True)
intervention_detail_df.replace(':',' ',  regex=True, inplace=True)
intervention_detail_df.replace(';',' ',  regex=True, inplace=True)

# fill blanks with NA
intervention_detail_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_detail_df.to_csv("InterventionDetail.csv", index=False) """

print(intervention_detail_df)