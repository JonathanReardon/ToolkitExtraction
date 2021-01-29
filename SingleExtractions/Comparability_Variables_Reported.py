from Main import get_data, highlighted_text, comments
from AttributeIDList import comparabiltiy_vars_reported
from AttributeIDList import if_yes_which_comparability_variables_reported_output
import pandas as pd

#####################################################
# Are the variables used for comparability reported?
#####################################################

# get comparability variables reported data
comparability_vars_reported = get_data(comparabiltiy_vars_reported)
comparability_vars_reported_df = pd.DataFrame(comparability_vars_reported)
comparability_vars_reported_df = comparability_vars_reported_df.T
comparability_vars_reported_df.columns = ["comp_var_rep_raw"]

# Get Comparability Variables Reported highlighted text
comparability_vars_reported_HT = highlighted_text(comparabiltiy_vars_reported)
comparability_vars_reported_HT_df = pd.DataFrame(comparability_vars_reported_HT)
comparability_vars_reported_HT_df = comparability_vars_reported_HT_df.T
comparability_vars_reported_HT_df.columns = ["comp_var_rep_ht"]

# Get Comparability Variables Reported user comments
comparability_vars_reported_Comments = comments(comparabiltiy_vars_reported)
comparability_vars_reported_Comments_df = pd.DataFrame(comparability_vars_reported_Comments)
comparability_vars_reported_Comments_df = comparability_vars_reported_Comments_df.T
comparability_vars_reported_Comments_df.columns = ["comp_var_rep_info"]

######################################################
# If yes, which variables are used for comparability?
######################################################

# get "which" variables are used for comparability data
which_comparability_vars_reported = get_data(if_yes_which_comparability_variables_reported_output)
which_comparability_vars_reported_df = pd.DataFrame(which_comparability_vars_reported)
which_comparability_vars_reported_df = which_comparability_vars_reported_df.T
which_comparability_vars_reported_df.columns = ["comp_var_raw"]

# Get Comparability Variables Reported highlighted text
which_comparability_vars_reported_df_HT = highlighted_text(if_yes_which_comparability_variables_reported_output)
which_comparability_vars_reported_df_HT_df = pd.DataFrame(which_comparability_vars_reported_df_HT)
which_comparability_vars_reported_df_HT_df = which_comparability_vars_reported_df_HT_df.T
which_comparability_vars_reported_df_HT_df.columns = ["comp_var_ht"]

# Get Comparability Variables Reported user comments
which_comparability_vars_reported_Comments = comments(if_yes_which_comparability_variables_reported_output)
which_comparability_vars_reported_Comments_df = pd.DataFrame(which_comparability_vars_reported_Comments)
which_comparability_vars_reported_Comments_df = which_comparability_vars_reported_Comments_df.T
which_comparability_vars_reported_Comments_df.columns = ["comp_var_info"]

# concatenate data frames
comparability_vars_reported_df = pd.concat([
    comparability_vars_reported_df, 
    comparability_vars_reported_HT_df, 
    comparability_vars_reported_Comments_df,
    which_comparability_vars_reported_df, 
    which_comparability_vars_reported_df_HT_df, 
    which_comparability_vars_reported_Comments_df
], axis=1, sort=False)

# fill blanks with NA
comparability_vars_reported_df.fillna("NA", inplace=True)

# savce to disk
comparability_vars_reported_df.to_csv("comparability_vars_reported.csv", index=False)