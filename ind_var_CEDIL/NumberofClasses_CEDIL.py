from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import number_of_classes_intervention_CEDIL
from AttributeIDList import number_of_classes_control_CEDIL
from AttributeIDList import number_of_classes_total_CEDIL
from AttributeIDList import number_of_classes_not_provided_CEDIL
import pandas as pd

# load json file
load_json()

##################################
# NUMBER OF CLASSES INTERVENTION #
##################################

# get number of classes intervention comments data
number_of_classes_intervention_Comments = comments(number_of_classes_intervention_CEDIL)
number_of_classes_intervention_Comments_df = pd.DataFrame(number_of_classes_intervention_Comments)
number_of_classes_intervention_Comments_df = number_of_classes_intervention_Comments_df.T
number_of_classes_intervention_Comments_df.columns = ["class_treat_info"]

# get number of classes intervention highlighted text data
number_of_classes_intervention_HT = highlighted_text(number_of_classes_intervention_CEDIL)
number_of_classes_intervention_HT_df = pd.DataFrame(number_of_classes_intervention_HT)
number_of_classes_intervention_HT_df = number_of_classes_intervention_HT_df.T
number_of_classes_intervention_HT_df.columns = ["class_treat_ht"]

#############################
# NUMBER OF CLASSES CONTROL #
#############################

# get number of classes control comments data
number_of_classes_control_Comments = comments(number_of_classes_control_CEDIL)
number_of_classes_control_Comments_df = pd.DataFrame(number_of_classes_control_Comments)
number_of_classes_control_Comments_df = number_of_classes_control_Comments_df.T
number_of_classes_control_Comments_df.columns = ["class_cont_info"]

# get number of classes control highlighted text data
number_of_classes_control_HT = highlighted_text(number_of_classes_control_CEDIL)
number_of_classes_control_HT_df = pd.DataFrame(number_of_classes_control_HT)
number_of_classes_control_HT_df = number_of_classes_control_HT_df.T
number_of_classes_control_HT_df.columns = ["class_cont_ht"]

###########################
# NUMBER OF CLASSES TOTAL #
###########################

# get number of classes total comments data
number_of_classes_total_Comments = comments(number_of_classes_total_CEDIL)
number_of_classes_total_Comments_df = pd.DataFrame(number_of_classes_total_Comments)
number_of_classes_total_Comments_df = number_of_classes_total_Comments_df.T
number_of_classes_total_Comments_df.columns = ["class_total_info"]

# get number of classes total highlighted text data
number_of_classes_total_HT = highlighted_text(number_of_classes_total_CEDIL)
number_of_classes_total_HT_df = pd.DataFrame(number_of_classes_total_HT)
number_of_classes_total_HT_df = number_of_classes_total_HT_df.T
number_of_classes_total_HT_df.columns = ["class_total_ht"]

#########################################################
# NUMBER OF CLASSES NOT PROVIDED/UNCLEAR/NOT APPLICABLE #
#########################################################

# get number of classes not provided data
number_of_classes_np = get_data(number_of_classes_not_provided_CEDIL)
number_of_classes_np_df = pd.DataFrame(number_of_classes_np)
number_of_classes_np_df = number_of_classes_np_df.T
number_of_classes_np_df.columns = ["class_na_raw"]

# get number of classes not provided comments data
number_of_classes_not_provided_Comments = comments(number_of_classes_not_provided_CEDIL)
number_of_classes_not_provided_Comments_df = pd.DataFrame(number_of_classes_not_provided_Comments)
number_of_classes_not_provided_Comments_df = number_of_classes_not_provided_Comments_df.T
number_of_classes_not_provided_Comments_df.columns = ["class_na_info"]

# get number of classes not provided highlighted text data
number_of_classes_not_provided_HT = highlighted_text(number_of_classes_not_provided_CEDIL)
number_of_classes_not_provided_HT_df = pd.DataFrame(number_of_classes_not_provided_HT)
number_of_classes_not_provided_HT_df = number_of_classes_not_provided_HT_df.T
number_of_classes_not_provided_HT_df.columns = ["class_na_ht"]

# concatenate dataframes
number_of_classes_df = pd.concat([
    number_of_classes_intervention_Comments_df, 
    number_of_classes_intervention_HT_df,
    number_of_classes_control_Comments_df, 
    number_of_classes_control_HT_df,
    number_of_classes_total_Comments_df, 
    number_of_classes_total_HT_df,
    number_of_classes_np_df, 
    number_of_classes_not_provided_Comments_df, 
    number_of_classes_not_provided_HT_df
], axis=1, sort=False)

# replace problematic text
number_of_classes_df.replace('\r', ' ', regex=True, inplace=True)
number_of_classes_df.replace('\n', ' ', regex=True, inplace=True)

# fill blanks with NA
number_of_classes_df.fillna("NA", inplace=True)

# save to disk
""" number_of_classes_df.to_csv("number_of_classes.csv", index=False) """

print(number_of_classes_df)