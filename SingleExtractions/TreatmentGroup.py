from Main import get_data, comments, highlighted_text
from AttributeIDList import treatment_group
import pandas as pd

# get treatment group data
treatmentgroup = get_data(treatment_group)
treatmentgroup_df = pd.DataFrame(treatmentgroup)
treatmentgroup_df = treatmentgroup_df.T
treatmentgroup_df.columns = ["treat_group_raw"]

""" treatmentgroup_df["treat_group_more_than_one_treatment_group_yes"] = treatmentgroup_df["treat_group_raw"].map(set(['Yes (Please specify)']).issubset).astype(int)
treatmentgroup_df["treat_group_more_than_one_treatment_group_no"]  = treatmentgroup_df["treat_group_raw"].map(set(['No']).issubset).astype(int)
treatmentgroup_df["treat_group_more_than_one_treatment_group_NA"]  = treatmentgroup_df["treat_group_raw"].map(set(['Not specified or N/A']).issubset).astype(int) """

# get treatment group highlighted text
treatmentgroup_HT = highlighted_text(treatment_group)
treatmentgroup_HT_df = pd.DataFrame(treatmentgroup_HT)
treatmentgroup_HT_df = treatmentgroup_HT_df.T
treatmentgroup_HT_df.columns = ["treat_group_ht"]

# get treatment group user comments
treatmentgroup_Comments = comments(treatment_group)
treatmentgroup_Comments_df = pd.DataFrame(treatmentgroup_Comments)
treatmentgroup_Comments_df = treatmentgroup_Comments_df.T
treatmentgroup_Comments_df.columns = ["treat_group_info"]

# concatenate data frames
treatment_group_df = pd.concat(
    [treatmentgroup_df, treatmentgroup_HT_df, treatmentgroup_Comments_df], axis=1, sort=False)

# fill blanks with NA
treatment_group_df.fillna("NA", inplace=True)

# save to difk
treatment_group_df.to_csv("treatmentgroup.csv", index=False)