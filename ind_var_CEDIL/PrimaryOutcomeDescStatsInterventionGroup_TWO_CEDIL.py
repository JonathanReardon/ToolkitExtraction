from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_group_two_number_CEDIL
from AttributeIDList import intervention_group_two_pretest_mean_CEDIL
from AttributeIDList import intervention_group_two_pretest_sd_CEDIL
from AttributeIDList import intervention_group_two_posttest_mean_CEDIL
from AttributeIDList import intervention_group_two_posttest_sd_CEDIL
from AttributeIDList import intervention_group_two_gain_score_mean_CEDIL
from AttributeIDList import intervention_group_two_gain_score_sd_CEDIL
from AttributeIDList import intervention_group_two_any_other_info_CEDIL
import pandas as pd

# load json file
load_json()

###########################
# INTERVENTION GROUP NUMBER
###########################

# Get Intervention Group Number highlighted text
InterventionGroupNumber_HT = highlighted_text(intervention_group_two_number_CEDIL)
InterventionGroupNumber_HT_df = pd.DataFrame(InterventionGroupNumber_HT)
InterventionGroupNumber_HT_df = InterventionGroupNumber_HT_df.T
InterventionGroupNumber_HT_df.columns = ["n_treat2_ht"]

# Get Intervention Group Number comments
InterventionGroupNumber_comments = comments(intervention_group_two_number_CEDIL)
InterventionGroupNumber_comments_df = pd.DataFrame(InterventionGroupNumber_comments)
InterventionGroupNumber_comments_df = InterventionGroupNumber_comments_df.T
InterventionGroupNumber_comments_df.columns = ["n_treat2_info"]

#################################
# INTERVENTION GROUP PRE-TEST MEAN
#################################

# Get Intervention Group Pre-test Mean highlighted text
InterventionGroupPretestMean_HT = highlighted_text(intervention_group_two_pretest_mean_CEDIL)
InterventionGroupPretestMean_HT_df = pd.DataFrame(InterventionGroupPretestMean_HT)
InterventionGroupPretestMean_HT_df = InterventionGroupPretestMean_HT_df.T
InterventionGroupPretestMean_HT_df.columns = ["pre_t2_mean_ht"]

# Get Intervention Group Pre-test Mean comments
InterventionGroupPretestMean_comments = comments(intervention_group_two_pretest_mean_CEDIL)
InterventionGroupPretestMean_comments_df = pd.DataFrame(InterventionGroupPretestMean_comments)
InterventionGroupPretestMean_comments_df = InterventionGroupPretestMean_comments_df.T
InterventionGroupPretestMean_comments_df.columns = ["pre_t2_mean_info"]

################################
# INTERVENTION GROUP PRE-TEST SD
################################

# Get Intervention Group Pre-test SD highlighted text
InterventionGroupPretestSD_HT = highlighted_text(intervention_group_two_pretest_sd_CEDIL)
InterventionGroupPretestSD_HT_df = pd.DataFrame(InterventionGroupPretestSD_HT)
InterventionGroupPretestSD_HT_df = InterventionGroupPretestSD_HT_df.T
InterventionGroupPretestSD_HT_df.columns = ["pre_t2_sd_ht"]

# Get Intervention Group Pre-test SD comments
InterventionGroupPretestSD_comments = comments(intervention_group_two_pretest_sd_CEDIL)
InterventionGroupPretestSD_comments_df = pd.DataFrame(InterventionGroupPretestSD_comments)
InterventionGroupPretestSD_comments_df = InterventionGroupPretestSD_comments_df.T
InterventionGroupPretestSD_comments_df.columns = ["pre_t2_sd_info"]

##################################
# INTERVENTION GROUP POST-TEST MEAN
###################################

# Get Intervention Group Post-Test Mean highlighted text
InterventionGroupPostTestMean_HT = highlighted_text(intervention_group_two_posttest_mean_CEDIL)
InterventionGroupPostTestMean_HT_df = pd.DataFrame(InterventionGroupPostTestMean_HT)
InterventionGroupPostTestMean_HT_df = InterventionGroupPostTestMean_HT_df.T
InterventionGroupPostTestMean_HT_df.columns = ["post_t2_mean_ht"]

# Get Intervention Group Post-Test Mean comments
InterventionGroupPostTestMean_comments = comments(intervention_group_two_posttest_mean_CEDIL)
InterventionGroupPostTestMean_comments_df = pd.DataFrame(InterventionGroupPostTestMean_comments)
InterventionGroupPostTestMean_comments_df = InterventionGroupPostTestMean_comments_df.T
InterventionGroupPostTestMean_comments_df.columns = ["post_t2_mean_info"]

##################################
# INTERVENTION GROUP POST-TEST SD
###################################

# Get Intervention Group Post-test SD highlighted text
InterventionGroupPostTestSD_HT = highlighted_text(intervention_group_two_posttest_sd_CEDIL)
InterventionGroupPostTestSD_HT_df = pd.DataFrame(InterventionGroupPostTestSD_HT)
InterventionGroupPostTestSD_HT_df = InterventionGroupPostTestSD_HT_df.T
InterventionGroupPostTestSD_HT_df.columns = ["post_t2_sd_ht"]

# Get Intervention Group Post-test SD comments
InterventionGroupPostTestSD_comments = comments(intervention_group_two_posttest_sd_CEDIL)
InterventionGroupPostTestSD_comments_df = pd.DataFrame(InterventionGroupPostTestSD_comments)
InterventionGroupPostTestSD_comments_df = InterventionGroupPostTestSD_comments_df.T
InterventionGroupPostTestSD_comments_df.columns = ["post_t2_sd_info"]

####################################
# INTERVENTION GROUP GAIN SCORE MEAN
####################################

# Get Intervention Group Grain Score Mean highlighted text
InterventionGroupGainScoreMean_HT = highlighted_text(intervention_group_two_gain_score_mean_CEDIL)
InterventionGroupGainScoreMean_HT_df = pd.DataFrame(InterventionGroupGainScoreMean_HT)
InterventionGroupGainScoreMean_HT_df = InterventionGroupGainScoreMean_HT_df.T
InterventionGroupGainScoreMean_HT_df.columns = ["gain_t2_mean_ht"]

# Get Intervention Group Gain Score Mean comments
InterventionGroupGainScoreMean_comments = comments(intervention_group_two_gain_score_mean_CEDIL)
InterventionGroupGainScoreMean_comments_df = pd.DataFrame(InterventionGroupGainScoreMean_comments)
InterventionGroupGainScoreMean_comments_df = InterventionGroupGainScoreMean_comments_df.T
InterventionGroupGainScoreMean_comments_df.columns = ["gain_t2_mean_info"]

##################################
# INTERVENTION GROUP GAIN SCORE SD
##################################

# Get Intervention Group Grain Score SD highlighted text
InterventionGroupGainScoreSD_HT = highlighted_text(intervention_group_two_gain_score_sd_CEDIL)
InterventionGroupGainScoreSD_HT_df = pd.DataFrame(InterventionGroupGainScoreSD_HT)
InterventionGroupGainScoreSD_HT_df = InterventionGroupGainScoreSD_HT_df.T
InterventionGroupGainScoreSD_HT_df.columns = ["gain_t2_sd_ht"]

# Get Intervention Group Gain Score SD comments
InterventionGroupGainScoreSD_comments = comments(intervention_group_two_gain_score_sd_CEDIL)
InterventionGroupGainScoreSD_comments_df = pd.DataFrame(InterventionGroupGainScoreSD_comments)
InterventionGroupGainScoreSD_comments_df = InterventionGroupGainScoreSD_comments_df.T
InterventionGroupGainScoreSD_comments_df.columns = ["gain_t2_sd_info"]

###############################
# INTERVENTION GROUP OTHER INFO
###############################

# Get Intervention Group Other Information highlighted text
InterventionGroupOtherInfo_HT = highlighted_text(intervention_group_two_any_other_info_CEDIL)
InterventionGroupOtherInfo_HT_df = pd.DataFrame(InterventionGroupOtherInfo_HT)
InterventionGroupOtherInfo_HT_df = InterventionGroupOtherInfo_HT_df.T
InterventionGroupOtherInfo_HT_df.columns = ["out_t2_other_ht"]

# Get Intervention Group Other Information comments
InterventionGroupOtherInfo_comments = comments(intervention_group_two_any_other_info_CEDIL)
InterventionGroupOtherInfo_comments_df = pd.DataFrame(InterventionGroupOtherInfo_comments)
InterventionGroupOtherInfo_comments_df = InterventionGroupOtherInfo_comments_df.T
InterventionGroupOtherInfo_comments_df.columns = ["out_t2_other_info"]

# concatenate data frames
DescStatsPrimaryOutcomeReported_Intervention_TWO_df = pd.concat([
    InterventionGroupNumber_HT_df, 
    InterventionGroupNumber_comments_df,
    InterventionGroupPretestMean_HT_df, 
    InterventionGroupPretestMean_comments_df,
    InterventionGroupPretestSD_HT_df,
    InterventionGroupPretestSD_comments_df,
    InterventionGroupPostTestMean_HT_df, 
    InterventionGroupPostTestMean_comments_df,
    InterventionGroupPostTestSD_HT_df, 
    InterventionGroupPostTestSD_comments_df,
    InterventionGroupGainScoreMean_HT_df, 
    InterventionGroupGainScoreMean_comments_df,
    InterventionGroupGainScoreSD_HT_df, 
    InterventionGroupGainScoreSD_comments_df,
    InterventionGroupOtherInfo_HT_df, 
    InterventionGroupOtherInfo_comments_df
], axis=1, sort=False)

# fill blanks with NA
DescStatsPrimaryOutcomeReported_Intervention_TWO_df.fillna("NA", inplace=True)

# save to disk
""" DescStatsPrimaryOutcomeReported_Intervention_TWO_df.to_csv(
    "DescriptiveStatsPrimary_Intervention_TWO.csv", index=False) """

print(DescStatsPrimaryOutcomeReported_Intervention_TWO_df)