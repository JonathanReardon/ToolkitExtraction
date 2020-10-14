import os
import json
import pandas as pd

from AttributeIDList import *
from DATAFILE import file

exclude="NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data=json.load(f)

def get_data(codes):
    df=[]
    for var in range(len(codes)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind)==0:
                    holderfind=exclude
                holder.append(holderfind)
        df.append(holder)
    return df

def highlighted_text(codes):
    all_comments, highlighted_text = [], []
    for var in range(len(codes)):
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                user_highlighted_text = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            if "ItemAttributeFullTextDetails" in data["References"][section]["Codes"][study]:
                                if data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"]:
                                    for i in range(len(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"])):
                                        user_highlighted_text.append(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"][i]["Text"])
                if not user_highlighted_text:
                    highlighted_text.append(exclude)
                else:
                    highlighted_text.append(user_highlighted_text)
            else:
                highlighted_text.append(exclude)
        all_comments.append(highlighted_text)
        highlighted_text=[]
    return all_comments

def comments(codes):
    all_comments, comments= [], []
    for var in range(len(codes)):
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                user_comments = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            if "AdditionalText" in data["References"][section]["Codes"][study]:
                                user_comments = data["References"][section]["Codes"][study]["AdditionalText"]
                if not user_comments:
                    comments.append(exclude)
                else:
                    comments.append(user_comments)
            else:
                comments.append(exclude)
        all_comments.append(comments)
        comments=[]
    return all_comments

###########################
# CONTROL GROUP NUMBER
###########################
# Get Control Group Number highlighted text
ControlGroupNumber_HT            = highlighted_text(control_group_number)
ControlGroupNumber_HT_df         = pd.DataFrame(ControlGroupNumber_HT)
ControlGroupNumber_HT_df         = ControlGroupNumber_HT_df.T
ControlGroupNumber_HT_df.columns = ["n_cont_ht"]

# Get Control Group Number comments
ControlGroupNumber_comments            = comments(control_group_number)
ControlGroupNumber_comments_df         = pd.DataFrame(ControlGroupNumber_comments)
ControlGroupNumber_comments_df         = ControlGroupNumber_comments_df.T
ControlGroupNumber_comments_df.columns = ["n_cont_info"]

#################################
# Control GROUP PRE-TEST MEAN
#################################
# Get Control Group Pre-test Mean highlighted text
ControlGroupPretestMean_HT            = highlighted_text(control_group_pretest_mean)
ControlGroupPretestMean_HT_df         = pd.DataFrame(ControlGroupPretestMean_HT)
ControlGroupPretestMean_HT_df         = ControlGroupPretestMean_HT_df.T
ControlGroupPretestMean_HT_df.columns = ["Control_Group_Pre-test_Mean_HT"]

# Get Control Group Pre-test Mean comments
ControlGroupPretestMean_comments            = comments(control_group_pretest_mean)
ControlGroupPretestMean_comments_df         = pd.DataFrame(ControlGroupPretestMean_comments)
ControlGroupPretestMean_comments_df         = ControlGroupPretestMean_comments_df.T
ControlGroupPretestMean_comments_df.columns = ["Control_Group_Pre-test_Mean_comments"]

################################
# Control GROUP PRE-TEST SD
################################
# Get Control Group Pre-test SD highlighted text
ControlGroupPretestSD_HT            = highlighted_text(control_group_pretest_sd)
ControlGroupPretestSD_HT_df         = pd.DataFrame(ControlGroupPretestSD_HT)
ControlGroupPretestSD_HT_df         = ControlGroupPretestSD_HT_df.T
ControlGroupPretestSD_HT_df.columns = ["Control_Group_Pre-test_SD_HT"]

# Get Control Group Pre-test SD comments
ControlGroupPretestSD_comments            = comments(control_group_pretest_sd)
ControlGroupPretestSD_comments_df         = pd.DataFrame(ControlGroupPretestSD_comments)
ControlGroupPretestSD_comments_df         = ControlGroupPretestSD_comments_df.T
ControlGroupPretestSD_comments_df.columns = ["Control_Group_Pre-test_SD_comments"]

##################################
# Control GROUP POST-TEST MEAN
###################################
# Get Control Group Post-Test Mean highlighted text
ControlGroupPostTestMean_HT            = highlighted_text(control_group_posttest_mean)
ControlGroupPostTestMean_HT_df         = pd.DataFrame(ControlGroupPostTestMean_HT)
ControlGroupPostTestMean_HT_df         = ControlGroupPostTestMean_HT_df.T
ControlGroupPostTestMean_HT_df.columns = ["Control_Group_Post-test_Mean_HT"]

# Get Control Group Post-Test Mean comments
ControlGroupPostTestMean_comments            = comments(control_group_posttest_mean)
ControlGroupPostTestMean_comments_df         = pd.DataFrame(ControlGroupPostTestMean_comments)
ControlGroupPostTestMean_comments_df         = ControlGroupPostTestMean_comments_df.T
ControlGroupPostTestMean_comments_df.columns = ["Control_Group_Post-test_Mean_comments"]

##################################
# Control GROUP POST-TEST SD
###################################
# Get Control Group Post-test SD highlighted text
ControlGroupPostTestSD_HT            = highlighted_text(control_group_posttest_sd)
ControlGroupPostTestSD_HT_df         = pd.DataFrame(ControlGroupPostTestSD_HT)
ControlGroupPostTestSD_HT_df         = ControlGroupPostTestSD_HT_df.T
ControlGroupPostTestSD_HT_df.columns = ["Control_Group_Post-test_SD_HT"]

# Get Control Group Post-test SD comments
ControlGroupPostTestSD_comments            = comments(control_group_posttest_sd)
ControlGroupPostTestSD_comments_df         = pd.DataFrame(ControlGroupPostTestSD_comments)
ControlGroupPostTestSD_comments_df         = ControlGroupPostTestSD_comments_df.T
ControlGroupPostTestSD_comments_df.columns = ["Control_Group_Post-test_SD_comments"]

####################################
# Control GROUP GAIN SCORE MEAN
####################################
# Get Control Group Grain Score Mean highlighted text
ControlGroupGainScoreMean_HT            = highlighted_text(control_group_gain_score_mean)
ControlGroupGainScoreMean_HT_df         = pd.DataFrame(ControlGroupGainScoreMean_HT)
ControlGroupGainScoreMean_HT_df         = ControlGroupGainScoreMean_HT_df.T
ControlGroupGainScoreMean_HT_df.columns = ["Control_Group_Gain_Score_Mean_HT"]

# Get Control Group Gain Score Mean comments
ControlGroupGainScoreMean_comments            = comments(control_group_gain_score_mean)
ControlGroupGainScoreMean_comments_df         = pd.DataFrame(ControlGroupGainScoreMean_comments)
ControlGroupGainScoreMean_comments_df         = ControlGroupGainScoreMean_comments_df.T
ControlGroupGainScoreMean_comments_df.columns = ["Control_Group_Gain_Score_Mean_comments"]

##################################
# Control GROUP GAIN SCORE SD
##################################
# Get Control Group Grain Score SD highlighted text
ControlGroupGainScoreSD_HT            = highlighted_text(control_group_gain_score_sd)
ControlGroupGainScoreSD_HT_df         = pd.DataFrame(ControlGroupGainScoreSD_HT)
ControlGroupGainScoreSD_HT_df         = ControlGroupGainScoreSD_HT_df.T
ControlGroupGainScoreSD_HT_df.columns = ["Control_Group_Gain_Score_SD_HT"]

# Get Control Group Gain Score SD comments
ControlGroupGainScoreSD_comments            = comments(control_group_gain_score_sd)
ControlGroupGainScoreSD_comments_df         = pd.DataFrame(ControlGroupGainScoreSD_comments)
ControlGroupGainScoreSD_comments_df         = ControlGroupGainScoreSD_comments_df.T
ControlGroupGainScoreSD_comments_df.columns = ["Control_Group_Gain_Score_SD_comments"]

###############################
# Control GROUP OTHER INFO
###############################
# Get Control Group Other Information highlighted text
ControlGroupOtherInfo_HT            = highlighted_text(control_group_any_other_info)
ControlGroupOtherInfo_HT_df         = pd.DataFrame(ControlGroupOtherInfo_HT)
ControlGroupOtherInfo_HT_df         = ControlGroupOtherInfo_HT_df.T
ControlGroupOtherInfo_HT_df.columns = ["Control_Group_Other_Info_HT"]

# Get Control Group Other Information comments
ControlGroupOtherInfo_comments            = comments(control_group_any_other_info)
ControlGroupOtherInfo_comments_df         = pd.DataFrame(ControlGroupOtherInfo_comments)
ControlGroupOtherInfo_comments_df         = ControlGroupOtherInfo_comments_df.T
ControlGroupOtherInfo_comments_df.columns = ["Control_Group_Other_Info_comments"]

########################
# Follow up data?
########################
followupdata = get_data(follow_up_data_reported)
followupdata_df = pd.DataFrame(followupdata)
followupdata_df = followupdata_df.T
followupdata_df.columns=["Follow_Up_Data_Reported"]

followupdata_df["Follow_Up_Data_Reported_YES"] = followupdata_df["Follow_Up_Data_Reported"].map(set(['Yes']).issubset).astype(int)
followupdata_df["Follow_Up_Data_Reported_NO"] = followupdata_df["Follow_Up_Data_Reported"].map(set(['No']).issubset).astype(int)

# Get Follow Up Data highlighted text
followupdata_HT            = highlighted_text(follow_up_data_reported)
followupdata_HT_df         = pd.DataFrame(followupdata_HT)
followupdata_HT_df         = followupdata_HT_df.T
followupdata_HT_df.columns = ["Follow_Up_Data_Reported_HT"]

# Get Follow Up Data comments
followupdata_comments            = comments(follow_up_data_reported)
followupdata_comments_df         = pd.DataFrame(followupdata_comments)
followupdata_comments_df         = followupdata_comments_df.T
followupdata_comments_df.columns = ["Follow_Up_Data_Reported_comments"]

# concatenate data frames
DescStatsPrimaryOutcomeReported_Control_df = pd.concat([ControlGroupNumber_HT_df, ControlGroupNumber_comments_df,
                                                        ControlGroupPretestMean_HT_df, ControlGroupPretestMean_comments_df,
                                                        ControlGroupPretestSD_HT_df, ControlGroupPretestSD_comments_df,
                                                        ControlGroupPostTestMean_HT_df, ControlGroupPostTestMean_comments_df,
                                                        ControlGroupPostTestSD_HT_df, ControlGroupPostTestSD_comments_df,
                                                        ControlGroupGainScoreMean_HT_df, ControlGroupGainScoreMean_comments_df,
                                                        ControlGroupGainScoreSD_HT_df, ControlGroupGainScoreSD_comments_df,
                                                        ControlGroupOtherInfo_HT_df, ControlGroupOtherInfo_comments_df,
                                                        followupdata_df, followupdata_HT_df, followupdata_comments_df], axis=1, sort=False)

DescStatsPrimaryOutcomeReported_Control_df.fillna("NA", inplace=True)

DescStatsPrimaryOutcomeReported_Control_df.to_csv("PrimaryOutcomeDescStats_Control.csv", index=False)
