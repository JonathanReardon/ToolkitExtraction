from Main import load_json, comments, highlighted_text
from AttributeIDList import sample_size_analyzed_intervention_output
from AttributeIDList import sample_size_analyzed_control_output
from AttributeIDList import sample_size_analyzed_second_intervention_output
from AttributeIDList import sample_size_analyzed_second_control_output
import pandas as pd

# load json file
load_json()

#############################################
# Analyzed sample size for intervention group
#############################################

# highlighted text
sample_size_analyzed_intervention = highlighted_text(sample_size_analyzed_intervention_output)
sample_size_analyzed_intervention_df = pd.DataFrame(sample_size_analyzed_intervention)
sample_size_analyzed_intervention_df = sample_size_analyzed_intervention_df.T
sample_size_analyzed_intervention_df.columns = ["n_treat_ht"]

# comments
sample_size_analyzed_intervention_Comments = comments(sample_size_analyzed_intervention_output)
sample_size_analyzed_intervention_Comments_df = pd.DataFrame(sample_size_analyzed_intervention_Comments)
sample_size_analyzed_intervention_Comments_df = sample_size_analyzed_intervention_Comments_df.T
sample_size_analyzed_intervention_Comments_df.columns = ["n_treat_info"]

############################################
# Analyzed sample size for the control group
############################################

# highlighted text
sample_size_analyzed_control = highlighted_text(sample_size_analyzed_control_output)
sample_size_analyzed_control_df = pd.DataFrame(sample_size_analyzed_control)
sample_size_analyzed_control_df = sample_size_analyzed_control_df.T
sample_size_analyzed_control_df.columns = ["n_cont_ht"]

# comments
sample_size__anazlyed_control_Comments = comments(sample_size_analyzed_control_output)
sample_size__anazlyed_control_Comments_df = pd.DataFrame(sample_size__anazlyed_control_Comments)
sample_size__anazlyed_control_Comments_df = sample_size__anazlyed_control_Comments_df.T
sample_size__anazlyed_control_Comments_df.columns = ["n_cont_info"]

########################################################
# Analyzed sample size for the second intervention group
########################################################

# highlighted text
sample_size_analyzed_second_intervention = highlighted_text(sample_size_analyzed_second_intervention_output)
sample_size_analyzed_second_intervention_df = pd.DataFrame(sample_size_analyzed_second_intervention)
sample_size_analyzed_second_intervention_df = sample_size_analyzed_second_intervention_df.T
sample_size_analyzed_second_intervention_df.columns = ["n_treat2_ht"]

# comments
sample_size_analyzed_second_intervention_Comments = comments(sample_size_analyzed_second_intervention_output)
sample_size_analyzed_second_intervention_Comments_df = pd.DataFrame(sample_size_analyzed_second_intervention_Comments)
sample_size_analyzed_second_intervention_Comments_df = sample_size_analyzed_second_intervention_Comments_df.T
sample_size_analyzed_second_intervention_Comments_df.columns = ["n_treat2_info"]

#######################################################
# Analyzed sample size for the second control group
#######################################################

# highlighted text
sample_size_analyzed_second_control = highlighted_text(sample_size_analyzed_second_control_output)
sample_size_analyzed_second_control_df = pd.DataFrame(sample_size_analyzed_second_control)
sample_size_analyzed_second_control_df = sample_size_analyzed_second_control_df.T
sample_size_analyzed_second_control_df.columns = ["n_cont2_ht"]

# comments
sample_size_analyzed_second_control_Comments = comments(sample_size_analyzed_second_control_output)
sample_size_analyzed_second_control_Comments_df = pd.DataFrame(sample_size_analyzed_second_control_Comments)
sample_size_analyzed_second_control_Comments_df = sample_size_analyzed_second_control_Comments_df.T
sample_size_analyzed_second_control_Comments_df.columns = ["n_cont2_info"]

# concatenate dataframes
analyzed_sample_size_df = pd.concat([
    sample_size_analyzed_intervention_df, 
    sample_size_analyzed_intervention_Comments_df,
    sample_size_analyzed_control_df, 
    sample_size__anazlyed_control_Comments_df,
    sample_size_analyzed_second_intervention_df, 
    sample_size_analyzed_second_intervention_Comments_df,
    sample_size_analyzed_second_control_df, 
    sample_size_analyzed_second_control_Comments_df
], axis=1, sort=False)

# remover problematic text
analyzed_sample_size_df.replace('\r', ' ', regex=True, inplace=True)
analyzed_sample_size_df.replace('\n', ' ', regex=True, inplace=True)

# fill blanks with NA
analyzed_sample_size_df.fillna("NA", inplace=True)

# save to disk
""" analyzed_sample_size_df.to_csv("analyzed_sample_size.csv", index=False) """