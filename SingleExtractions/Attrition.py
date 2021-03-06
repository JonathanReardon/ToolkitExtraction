
from Main import get_data, comments, highlighted_text
from AttributeIDList import attrition_dropout_reported_output
from AttributeIDList import treatment_group_attrition
from AttributeIDList import overall_percent_attrition
import pandas as pd

###############################
# ATTRITION DROP OUT REPORTED #
###############################

# get attrition dropout reported data
attrition_dropout_reported = get_data(attrition_dropout_reported_output)
attrition_dropout_reported_df = pd.DataFrame(attrition_dropout_reported)
attrition_dropout_reported_df = attrition_dropout_reported_df.T
attrition_dropout_reported_df.columns=["attri_raw"]

# highlighted text
attrition_dropout_reported_HT = highlighted_text(attrition_dropout_reported_output)
attrition_dropout_reported_HT_df = pd.DataFrame(attrition_dropout_reported_HT)
attrition_dropout_reported_HT_df = attrition_dropout_reported_HT_df.T
attrition_dropout_reported_HT_df.columns = ["attri_ht"]

# comments
attrition_dropout_reported_Comments = comments(attrition_dropout_reported_output)
attrition_dropout_reported_Comments_df = pd.DataFrame(attrition_dropout_reported_Comments)
attrition_dropout_reported_Comments_df = attrition_dropout_reported_Comments_df.T
attrition_dropout_reported_Comments_df.columns = ["attri_info"]

# binarize output options
""" attrition_dropout_reported_df["Attrition_Dropout_Reported_YES"] = attrition_dropout_reported_df["Attrition_Dopout_Reported_extract"].map(set(['Yes']).issubset).astype(int)
attrition_dropout_reported_df["Attrition_Dropout_Reported_NO"] = attrition_dropout_reported_df["Attrition_Dopout_Reported_extract"].map(set(['No']).issubset).astype(int)
attrition_dropout_reported_df["Attrition Unclear (please add notes)"] = attrition_dropout_reported_df["Attrition_Dopout_Reported_extract"].map(set(['Unclear (please add notes)']).issubset).astype(int) """

#############################
# TREATMENT GROUP ATTRITION #
#############################

# get treatment attrition highlighted text
treatmentgroup_attrition_HT = highlighted_text(treatment_group_attrition)
treatmentgroup_attrition_HT_df = pd.DataFrame(treatmentgroup_attrition_HT)
treatmentgroup_attrition_HT_df = treatmentgroup_attrition_HT_df.T
treatmentgroup_attrition_HT_df.columns = ["attri_treat_ht"]

# get treatment attrition user comments
treatmentgroup_attrition_Comments = comments(treatment_group_attrition)
treatmentgroup_attrition_Comments_df = pd.DataFrame(treatmentgroup_attrition_Comments)
treatmentgroup_attrition_Comments_df = treatmentgroup_attrition_Comments_df.T
treatmentgroup_attrition_Comments_df.columns = ["attri_treat_info"]

#############################
# OVERALL PERCENT ATTRITION #
#############################

# get overall percent attrition highlighted text
overall_percent_attrition_HT = highlighted_text(overall_percent_attrition)
overall_percent_attrition_HT_df = pd.DataFrame(overall_percent_attrition_HT)
overall_percent_attrition_HT_df = overall_percent_attrition_HT_df.T
overall_percent_attrition_HT_df.columns = ["attri_perc_ht"]

# Gget overall percent attrition  user comments
overall_percent_attrition_Comments = comments(overall_percent_attrition)
overall_percent_attrition_Comments_df = pd.DataFrame(overall_percent_attrition_Comments)
overall_percent_attrition_Comments_df = overall_percent_attrition_Comments_df.T
overall_percent_attrition_Comments_df.columns = ["attri_perc_info"]

# concatenate data frames
attrition_df = pd.concat([
    attrition_dropout_reported_df, 
    attrition_dropout_reported_HT_df, 
    attrition_dropout_reported_Comments_df,
    treatmentgroup_attrition_HT_df, 
    treatmentgroup_attrition_Comments_df,
    overall_percent_attrition_HT_df, 
    overall_percent_attrition_Comments_df], axis=1, sort=False)

# fill blank with NA
attrition_df.fillna("NA", inplace=True)

# save to disk
attrition_df.to_csv("Attrition.csv", index=False)
