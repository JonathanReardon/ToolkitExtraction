from Main import load_json, comments, highlighted_text
from AttributeIDList import sample_size_intervention_output
from AttributeIDList import sample_size_control_output
from AttributeIDList import sample_size_second_intervention_output
from AttributeIDList import sample_size_third_intervention_output
import pandas as pd

# load json file
load_json()

#############################################
# Initial sample size for intervention group
#############################################

# get sample size intervention highlighted text
sample_size_intervention_HT = highlighted_text(sample_size_intervention_output)
sample_size_intervention_HT_df = pd.DataFrame(sample_size_intervention_HT)
sample_size_intervention_HT_df = sample_size_intervention_HT_df.T
sample_size_intervention_HT_df.columns = ["base_n_treat_ht"]

# get sample size intervention 
sample_size_intervention_Comments = comments(sample_size_intervention_output)
sample_size_intervention_Comments_df = pd.DataFrame(sample_size_intervention_Comments)
sample_size_intervention_Comments_df = sample_size_intervention_Comments_df.T
sample_size_intervention_Comments_df.columns = ["base_n_treat_info"]

############################################
# Initial sample size for the control group
############################################

# get sample size control highlighted text
sample_size_control_HT = highlighted_text(sample_size_control_output)
sample_size_control_HT_df = pd.DataFrame(sample_size_control_HT)
sample_size_control_HT_df = sample_size_control_HT_df.T
sample_size_control_HT_df.columns = ["base_n_cont_ht"]

# get sample size control comments
sample_size_control_Comments = comments(sample_size_control_output)
sample_size_control_Comments_df = pd.DataFrame(sample_size_control_Comments)
sample_size_control_Comments_df = sample_size_control_Comments_df.T
sample_size_control_Comments_df.columns = ["base_n_cont_info"]

########################################################
# Initial sample size for the second intervention group
########################################################

# get sample size 2nd intervention highlighted text
sample_size_second_intervention_HT = highlighted_text(sample_size_second_intervention_output)
sample_size_second_intervention_HT_df = pd.DataFrame(sample_size_second_intervention_HT)
sample_size_second_intervention_HT_df = sample_size_second_intervention_HT_df.T
sample_size_second_intervention_HT_df.columns = ["base_n_treat2_ht"]

# get sample size 2nd intervention comments
sample_size_second_intervention_Comments = comments(sample_size_second_intervention_output)
sample_size_second_intervention_Comments_df = pd.DataFrame(sample_size_second_intervention_Comments)
sample_size_second_intervention_Comments_df = sample_size_second_intervention_Comments_df.T
sample_size_second_intervention_Comments_df.columns = ["base_n_treat2_info"]

#######################################################
# Initial sample size for the third intervention group
#######################################################

# get sample size 3rd intervention highlighted text
sample_size_third_intervention_HT = highlighted_text(sample_size_third_intervention_output)
sample_size_third_intervention_HT_df = pd.DataFrame(sample_size_third_intervention_HT)
sample_size_third_intervention_HT_df = sample_size_third_intervention_HT_df.T
sample_size_third_intervention_HT_df.columns = ["base_n_treat3_ht"]

# get sample size 3rd intervention comments
sample_size_third_intervention_Comments = comments(sample_size_third_intervention_output)
sample_size_third_intervention_Comments_df = pd.DataFrame(sample_size_third_intervention_Comments)
sample_size_third_intervention_Comments_df = sample_size_third_intervention_Comments_df.T
sample_size_third_intervention_Comments_df.columns = ["base_n_treat3_info"]

# concatenate dataframes
initial_sample_size_df = pd.concat([
    sample_size_intervention_HT_df, 
    sample_size_intervention_Comments_df,
    sample_size_control_HT_df, 
    sample_size_control_Comments_df,
    sample_size_second_intervention_HT_df,
    sample_size_second_intervention_Comments_df,
    sample_size_third_intervention_HT_df, 
    sample_size_third_intervention_Comments_df
], axis=1, sort=False)

# remove problematic text
initial_sample_size_df.replace('\r', ' ', regex=True, inplace=True)
initial_sample_size_df.replace('\n', ' ', regex=True, inplace=True)

# fill blanks with NA
initial_sample_size_df.fillna("NA", inplace=True)

# save to disk
""" initial_sample_size_df.to_csv("initial_sample_size.csv", index=False) """