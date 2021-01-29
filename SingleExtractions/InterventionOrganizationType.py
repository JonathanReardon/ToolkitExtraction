from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_organisation_type_output
import pandas as pd

# load json file
load_json()

# get intervention organisation type main data
InterventionOrgType = get_data(intervention_organisation_type_output)
InterventionOrgType_df = pd.DataFrame(InterventionOrgType)
InterventionOrgType_df = InterventionOrgType_df.T
InterventionOrgType_df.columns = ["int_prov_raw"]

# get intervention organisation type highlighted text
InterventionOrgType_HT = highlighted_text(intervention_organisation_type_output)
InterventionOrgType_HT_df = pd.DataFrame(InterventionOrgType_HT)
InterventionOrgType_HT_df = InterventionOrgType_HT_df.T
InterventionOrgType_HT_df.columns=["int_prov_ht"]

# get intervention organisation type user comments
InterventionOrgType_Comments = comments(intervention_organisation_type_output)
InterventionOrgType_Comments_df = pd.DataFrame(InterventionOrgType_Comments)
InterventionOrgType_Comments_df = InterventionOrgType_Comments_df.T
InterventionOrgType_Comments_df.columns=["int_prov_info"]

# concatenate data frames
intervention_org_type = pd.concat([
    InterventionOrgType_df, 
    InterventionOrgType_HT_df, 
    InterventionOrgType_Comments_df
], axis=1, sort=False)

# replace problematic text
intervention_org_type.replace('\r',' ', regex=True, inplace=True)
intervention_org_type.replace('\n',' ', regex=True, inplace=True)
intervention_org_type.replace(':',' ', regex=True, inplace=True)
intervention_org_type.replace(';',' ', regex=True, inplace=True)

# fill blanks with NA
intervention_org_type.fillna("NA", inplace=True)

# save to disk
""" intervention_org_type.to_csv("InterventionOrgType.csv", index=False) """