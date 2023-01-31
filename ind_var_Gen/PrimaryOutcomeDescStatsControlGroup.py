from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import control_group_number
from AttributeIDList import control_group_pretest_mean
from AttributeIDList import control_group_pretest_sd
from AttributeIDList import control_group_posttest_mean
from AttributeIDList import control_group_posttest_sd
from AttributeIDList import control_group_gain_score_mean
from AttributeIDList import control_group_gain_score_sd
from AttributeIDList import control_group_any_other_info
from AttributeIDList import follow_up_data_reported
import pandas as pd

# load json file
load_json()

###########################
# CONTROL GROUP NUMBER
###########################

# Get Control Group Number highlighted text
ControlGroupNumber_HT = highlighted_text(control_group_number)
ControlGroupNumber_HT_df = pd.DataFrame(ControlGroupNumber_HT)
ControlGroupNumber_HT_df = ControlGroupNumber_HT_df.T
ControlGroupNumber_HT_df.columns = ["n_cont_ht"]

# Get Control Group Number comments
ControlGroupNumber_comments = comments(control_group_number)
ControlGroupNumber_comments_df = pd.DataFrame(ControlGroupNumber_comments)
ControlGroupNumber_comments_df = ControlGroupNumber_comments_df.T
ControlGroupNumber_comments_df.columns = ["n_cont_info"]

#################################
# Control GROUP PRE-TEST MEAN
#################################

# Get Control Group Pre-test Mean highlighted text
ControlGroupPretestMean_HT = highlighted_text(control_group_pretest_mean)
ControlGroupPretestMean_HT_df = pd.DataFrame(ControlGroupPretestMean_HT)
ControlGroupPretestMean_HT_df = ControlGroupPretestMean_HT_df.T
ControlGroupPretestMean_HT_df.columns = ["pre_c_mean_ht"]

# Get Control Group Pre-test Mean comments
ControlGroupPretestMean_comments = comments(control_group_pretest_mean)
ControlGroupPretestMean_comments_df = pd.DataFrame(
    ControlGroupPretestMean_comments)
ControlGroupPretestMean_comments_df = ControlGroupPretestMean_comments_df.T
ControlGroupPretestMean_comments_df.columns = ["pre_c_mean_info"]

################################
# Control GROUP PRE-TEST SD
################################

# Get Control Group Pre-test SD highlighted text
ControlGroupPretestSD_HT = highlighted_text(control_group_pretest_sd)
ControlGroupPretestSD_HT_df = pd.DataFrame(ControlGroupPretestSD_HT)
ControlGroupPretestSD_HT_df = ControlGroupPretestSD_HT_df.T
ControlGroupPretestSD_HT_df.columns = ["pre_c_sd_ht"]

# Get Control Group Pre-test SD comments
ControlGroupPretestSD_comments = comments(control_group_pretest_sd)
ControlGroupPretestSD_comments_df = pd.DataFrame(ControlGroupPretestSD_comments)
ControlGroupPretestSD_comments_df = ControlGroupPretestSD_comments_df.T
ControlGroupPretestSD_comments_df.columns = ["pre_c_sd_info"]

##################################
# Control GROUP POST-TEST MEAN
###################################

# Get Control Group Post-Test Mean highlighted text
ControlGroupPostTestMean_HT = highlighted_text(control_group_posttest_mean)
ControlGroupPostTestMean_HT_df = pd.DataFrame(ControlGroupPostTestMean_HT)
ControlGroupPostTestMean_HT_df = ControlGroupPostTestMean_HT_df.T
ControlGroupPostTestMean_HT_df.columns = ["post_c_mean_ht"]

# Get Control Group Post-Test Mean comments
ControlGroupPostTestMean_comments = comments(control_group_posttest_mean)
ControlGroupPostTestMean_comments_df = pd.DataFrame(ControlGroupPostTestMean_comments)
ControlGroupPostTestMean_comments_df = ControlGroupPostTestMean_comments_df.T
ControlGroupPostTestMean_comments_df.columns = ["post_c_mean_info"]

##################################
# Control GROUP POST-TEST SD
###################################

# Get Control Group Post-test SD highlighted text
ControlGroupPostTestSD_HT = highlighted_text(control_group_posttest_sd)
ControlGroupPostTestSD_HT_df = pd.DataFrame(ControlGroupPostTestSD_HT)
ControlGroupPostTestSD_HT_df = ControlGroupPostTestSD_HT_df.T
ControlGroupPostTestSD_HT_df.columns = ["post_c_sd_ht"]

# Get Control Group Post-test SD comments
ControlGroupPostTestSD_comments = comments(control_group_posttest_sd)
ControlGroupPostTestSD_comments_df = pd.DataFrame(ControlGroupPostTestSD_comments)
ControlGroupPostTestSD_comments_df = ControlGroupPostTestSD_comments_df.T
ControlGroupPostTestSD_comments_df.columns = ["post_c_sd_info"]

####################################
# Control GROUP GAIN SCORE MEAN
####################################

# Get Control Group Grain Score Mean highlighted text
ControlGroupGainScoreMean_HT = highlighted_text(control_group_gain_score_mean)
ControlGroupGainScoreMean_HT_df = pd.DataFrame(ControlGroupGainScoreMean_HT)
ControlGroupGainScoreMean_HT_df = ControlGroupGainScoreMean_HT_df.T
ControlGroupGainScoreMean_HT_df.columns = ["gain_c_mean_ht"]

# Get Control Group Gain Score Mean comments
ControlGroupGainScoreMean_comments = comments(control_group_gain_score_mean)
ControlGroupGainScoreMean_comments_df = pd.DataFrame(ControlGroupGainScoreMean_comments)
ControlGroupGainScoreMean_comments_df = ControlGroupGainScoreMean_comments_df.T
ControlGroupGainScoreMean_comments_df.columns = ["gain_c_mean_info"]

##################################
# Control GROUP GAIN SCORE SD
##################################

# Get Control Group Grain Score SD highlighted text
ControlGroupGainScoreSD_HT = highlighted_text(control_group_gain_score_sd)
ControlGroupGainScoreSD_HT_df = pd.DataFrame(ControlGroupGainScoreSD_HT)
ControlGroupGainScoreSD_HT_df = ControlGroupGainScoreSD_HT_df.T
ControlGroupGainScoreSD_HT_df.columns = ["gain_c_sd_ht"]

# Get Control Group Gain Score SD comments
ControlGroupGainScoreSD_comments = comments(control_group_gain_score_sd)
ControlGroupGainScoreSD_comments_df = pd.DataFrame(ControlGroupGainScoreSD_comments)
ControlGroupGainScoreSD_comments_df = ControlGroupGainScoreSD_comments_df.T
ControlGroupGainScoreSD_comments_df.columns = ["gain_c_sd_info"]

###############################
# Control GROUP OTHER INFO
###############################

# Get Control Group Other Information highlighted text
ControlGroupOtherInfo_HT = highlighted_text(control_group_any_other_info)
ControlGroupOtherInfo_HT_df = pd.DataFrame(ControlGroupOtherInfo_HT)
ControlGroupOtherInfo_HT_df = ControlGroupOtherInfo_HT_df.T
ControlGroupOtherInfo_HT_df.columns = ["out_c_other_ht"]

# Get Control Group Other Information comments
ControlGroupOtherInfo_comments = comments(control_group_any_other_info)
ControlGroupOtherInfo_comments_df = pd.DataFrame(ControlGroupOtherInfo_comments)
ControlGroupOtherInfo_comments_df = ControlGroupOtherInfo_comments_df.T
ControlGroupOtherInfo_comments_df.columns = ["out_c_other_info"]

""" ########################
# Follow up data?
########################
followupdata = get_data(follow_up_data_reported)
followupdata_df = pd.DataFrame(followupdata)
followupdata_df = followupdata_df.T
followupdata_df.columns=["Follow_Up_Data_Reported"]

followupdata_df["Follow_Up_Data_Reported_YES"] = followupdata_df["Follow_Up_Data_Reported"].map(set(['Yes']).issubset).astype(int)
followupdata_df["Follow_Up_Data_Reported_NO"] = followupdata_df["Follow_Up_Data_Reported"].map(set(['No']).issubset).astype(int)

# Get Follow Up Data highlighted text
followupdata_HT = highlighted_text(follow_up_data_reported)
followupdata_HT_df = pd.DataFrame(followupdata_HT)
followupdata_HT_df = followupdata_HT_df.T
followupdata_HT_df.columns = ["Follow_Up_Data_Reported_HT"]

# Get Follow Up Data comments
followupdata_comments = comments(follow_up_data_reported)
followupdata_comments_df = pd.DataFrame(followupdata_comments)
followupdata_comments_df = followupdata_comments_df.T
followupdata_comments_df.columns = ["Follow_Up_Data_Reported_comments"]

print(followupdata_df)
 """

# concatenate data frames
DescStatsPrimaryOutcomeReported_Control_df = pd.concat([
    ControlGroupNumber_HT_df, 
    ControlGroupNumber_comments_df,
    ControlGroupPretestMean_HT_df, 
    ControlGroupPretestMean_comments_df,
    ControlGroupPretestSD_HT_df, 
    ControlGroupPretestSD_comments_df,
    ControlGroupPostTestMean_HT_df, 
    ControlGroupPostTestMean_comments_df,
    ControlGroupPostTestSD_HT_df, 
    ControlGroupPostTestSD_comments_df,
    ControlGroupGainScoreMean_HT_df, 
    ControlGroupGainScoreMean_comments_df,
    ControlGroupGainScoreSD_HT_df, 
    ControlGroupGainScoreSD_comments_df,
    ControlGroupOtherInfo_HT_df, 
    ControlGroupOtherInfo_comments_df
], axis=1, sort=False)

# fill blanks with NA
DescStatsPrimaryOutcomeReported_Control_df.fillna("NA", inplace=True)

# save to disk
#DescStatsPrimaryOutcomeReported_Control_df.to_csv("DescriptiveStatsPrimary_Control.csv", index=False)
