from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import number_of_schools_intervention_CEDIL
from AttributeIDList import number_of_schools_control_CEDIL
from AttributeIDList import number_of_schools_total_CEDIL
from AttributeIDList import number_of_schools_not_provided_CEDIL
import pandas as pd

# load json file
load_json()

##################################
# NUMBER OF SCHOOLS INTERVENTION #
##################################

# get number of school intervention comments data
number_of_schools_intervention_Comments = comments(number_of_schools_intervention_CEDIL)
number_of_schools_intervention_Comments_df = pd.DataFrame(number_of_schools_intervention_Comments)
number_of_schools_intervention_Comments_df = number_of_schools_intervention_Comments_df.T
number_of_schools_intervention_Comments_df.columns = ["school_treat_info"]

# get number of school intervention highlighted text data
number_of_schools_intervention_HT = highlighted_text(number_of_schools_intervention_CEDIL)
number_of_schools_intervention_HT_df = pd.DataFrame(number_of_schools_intervention_HT)
number_of_schools_intervention_HT_df = number_of_schools_intervention_HT_df.T
number_of_schools_intervention_HT_df.columns = ["school_treat_ht"]

#############################
# NUMBER OF SCHOOLS CONTROL #
#############################

# get number of school control comments data
number_of_schools_control_Comments = comments(number_of_schools_control_CEDIL)
number_of_schools_control_Comments_df = pd.DataFrame(number_of_schools_control_Comments)
number_of_schools_control_Comments_df = number_of_schools_control_Comments_df.T
number_of_schools_control_Comments_df.columns = ["school_cont_info"]

# get number of school control highlighted text data
number_of_schools_control_HT = highlighted_text(number_of_schools_control_CEDIL)
number_of_schools_control_HT_df = pd.DataFrame(number_of_schools_control_HT)
number_of_schools_control_HT_df = number_of_schools_control_HT_df.T
number_of_schools_control_HT_df.columns = ["school_cont_ht"]

###########################
# NUMBER OF SCHOOLS TOTAL #
###########################

# get total nnumber of schools comments data
number_of_schools_total_Comments = comments(number_of_schools_total_CEDIL)
number_of_schools_total_Comments_df = pd.DataFrame(number_of_schools_total_Comments)
number_of_schools_total_Comments_df = number_of_schools_total_Comments_df.T
number_of_schools_total_Comments_df.columns = ["school_total_info"]

# get total number of schools highlighted text data
number_of_schools_total_HT = highlighted_text(number_of_schools_total_CEDIL)
number_of_schools_total_HT_df = pd.DataFrame(number_of_schools_total_HT)
number_of_schools_total_HT_df = number_of_schools_total_HT_df.T
number_of_schools_total_HT_df.columns = ["school_total_ht"]

#########################################################
# NUMBER OF SCHOOLS NOT PROVIDED/UNCLEAR/NOT APPLICABLE #
#########################################################

# get number of schools not provided data
number_of_schools_np = get_data(number_of_schools_not_provided_CEDIL)
number_of_schools_np_df = pd.DataFrame(number_of_schools_np)
number_of_schools_np_df = number_of_schools_np_df.T
number_of_schools_np_df.columns = ["school_na_raw"]

# get number of schools not provided comments data
number_of_schools_np_Comments = comments(number_of_schools_not_provided_CEDIL)
number_of_schools_np_Comments_df = pd.DataFrame(number_of_schools_np_Comments)
number_of_schools_np_Comments_df = number_of_schools_np_Comments_df.T
number_of_schools_np_Comments_df.columns = ["school_na_info"]

# get number of schools not provided highlighted text data
number_of_schools_np_HT = highlighted_text(number_of_schools_not_provided_CEDIL)
number_of_schools_np_HT_df = pd.DataFrame(number_of_schools_np_HT)
number_of_schools_np_HT_df = number_of_schools_np_HT_df.T
number_of_schools_np_HT_df.columns = ["school_na_ht"]

# concatenate dataframes
number_of_schools_df = pd.concat([
    number_of_schools_intervention_Comments_df, 
    number_of_schools_intervention_HT_df,
    number_of_schools_control_Comments_df, 
    number_of_schools_control_HT_df,
    number_of_schools_total_Comments_df, 
    number_of_schools_total_HT_df,
    number_of_schools_np_df, 
    number_of_schools_np_Comments_df, 
    number_of_schools_np_HT_df
], axis=1, sort=False)

# remove problematic text
number_of_schools_df.replace('\r', ' ', regex=True, inplace=True)
number_of_schools_df.replace('\n', ' ', regex=True, inplace=True)

# fill blanks with NA
number_of_schools_df.fillna("NA", inplace=True)

# save to disk
""" number_of_schools_df.to_csv("number_of_schools.csv", index=False) """

print(number_of_schools_df)