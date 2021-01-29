from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import proportion_low_fsm_output
from AttributeIDList import percentage_low_fsm_output
from AttributeIDList import further_ses_fsm_info_output
from AttributeIDList import no_ses_fsm_info_provided_output
import pandas as pd

# load json file
load_json()

#######################################
# PROPORTION OF LOW SES/FSM IN SAMPLE #
#######################################

# get low ses proportion comments
low_ses_proportion_Comments = comments(proportion_low_fsm_output)
low_ses_proportion_Comments_df = pd.DataFrame(low_ses_proportion_Comments)
low_ses_proportion_Comments_df = low_ses_proportion_Comments_df.T
low_ses_proportion_Comments_df.columns = ["fsm_prop_info"]

# get low ses highlighted text
low_ses_proportion_HT = highlighted_text(proportion_low_fsm_output)
low_ses_proportion_HT_df = pd.DataFrame(low_ses_proportion_HT)
low_ses_proportion_HT_df = low_ses_proportion_HT_df.T
low_ses_proportion_HT_df.columns = ["fsm_prop_ht"]

#######################################
# PERCENTAGE OF LOW SES/FSM IN SAMPLE #
#######################################

# get low ses perc comments
low_ses_percentage_Comments = comments(percentage_low_fsm_output)
low_ses_percentage_Comments_df = pd.DataFrame(low_ses_percentage_Comments)
low_ses_percentage_Comments_df = low_ses_percentage_Comments_df.T
low_ses_percentage_Comments_df.columns = ["fsm_perc_info"]

# get low ses perc highlighted text
low_ses_percentage_HT = highlighted_text(percentage_low_fsm_output)
low_ses_percentage_HT_df = pd.DataFrame(low_ses_percentage_HT)
low_ses_percentage_HT_df = low_ses_percentage_HT_df.T
low_ses_percentage_HT_df.columns = ["fsm_perc_ht"]

#############################################
# FURTHER LOW SES/FSM INFORMATION IN SAMPLE #
#############################################

# get further low ses info comments
further_ses_info_Comments = comments(further_ses_fsm_info_output)
further_ses_info_Comments_df = pd.DataFrame(further_ses_info_Comments)
further_ses_info_Comments_df = further_ses_info_Comments_df.T
further_ses_info_Comments_df.columns = ["fsm_info_info"]

# get further low ses info highlighted text
further_ses_fsm_info_HT = highlighted_text(further_ses_fsm_info_output)
further_ses_fsm_info_HT_df = pd.DataFrame(further_ses_fsm_info_HT)
further_ses_fsm_info_HT_df = further_ses_fsm_info_HT_df.T
further_ses_fsm_info_HT_df.columns = ["fsm_info_ht"]

#######################################
# NO LOW SES/FSM INFORMATION PROVIDED #
#######################################

# get now low ses info data
no_low_ses_fsm_info = get_data(no_ses_fsm_info_provided_output)
no_low_ses_fsm_info_df = pd.DataFrame(no_low_ses_fsm_info)
no_low_ses_fsm_info_df = no_low_ses_fsm_info_df.T
no_low_ses_fsm_info_df.columns = ["fsm_na_raw"]

# get no low ses info comments
no_low_ses_fsm_info_comments = comments(no_ses_fsm_info_provided_output)
no_low_ses_fsm_info_comments_df = pd.DataFrame(no_low_ses_fsm_info_comments)
no_low_ses_fsm_info_comments_df = no_low_ses_fsm_info_comments_df.T
no_low_ses_fsm_info_comments_df.columns = ["fsm_na_info"]

""" no_low_ses_fsm_info_df["No_SES_FSM_Info"]=no_low_ses_fsm_info_df["No_SES_FSM_Info_Provided"].map(set(['No SES/FSM Information Provided']).issubset).astype(int) """

# concatenate datafeames
ses_fsm_df = pd.concat([
    low_ses_proportion_Comments_df, 
    low_ses_proportion_HT_df,
    low_ses_percentage_Comments_df, 
    low_ses_percentage_HT_df,
    further_ses_info_Comments_df, 
    further_ses_fsm_info_HT_df,
    no_low_ses_fsm_info_df, 
    no_low_ses_fsm_info_comments_df
], axis=1, sort=False)

# remove problematic text
ses_fsm_df.replace('\r', ' ', regex=True, inplace=True)
ses_fsm_df.replace('\n', ' ', regex=True, inplace=True)
ses_fsm_df.replace(':', ' ',  regex=True, inplace=True)
ses_fsm_df.replace(';', ' ',  regex=True, inplace=True)

# fill blanks with NA
ses_fsm_df.fillna("NA", inplace=True)

# save to disk
""" ses_fsm_df.to_csv("sesfsm.csv", index=False) """
