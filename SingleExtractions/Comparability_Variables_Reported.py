import os
import json
import pandas as pd

from CODES import *
from DATAFILE import file

exclude = "NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data = json.load(f)


def get_data(codes):
    df = []
    for var in range(len(codes)):
        holder = []
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind) == 0:
                    holderfind = exclude
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
                                        user_highlighted_text.append(
                                            data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"][i]["Text"])
                if not user_highlighted_text:
                    highlighted_text.append(exclude)
                else:
                    highlighted_text.append(user_highlighted_text)
            else:
                highlighted_text.append(exclude)
        all_comments.append(highlighted_text)
        highlighted_text = []
    return all_comments


def comments(codes):
    all_comments, comments = [], []
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
        comments = []
    return all_comments

#####################################################
# Are the variables used for comparability reported?
#####################################################


comparability_vars_reported = get_data(comparabiltiy_vars_reported)
comparability_vars_reported_df = pd.DataFrame(comparability_vars_reported)
comparability_vars_reported_df = comparability_vars_reported_df.T
comparability_vars_reported_df.columns = ["comp_var_rep_raw"]

# Get Comparability Variables Reported highlighted text
comparability_vars_reported_HT = highlighted_text(comparabiltiy_vars_reported)
comparability_vars_reported_HT_df = pd.DataFrame(
    comparability_vars_reported_HT)
comparability_vars_reported_HT_df = comparability_vars_reported_HT_df.T
comparability_vars_reported_HT_df.columns = ["comp_var_rep_ht"]

# Get Comparability Variables Reported user comments
comparability_vars_reported_Comments = comments(comparabiltiy_vars_reported)
comparability_vars_reported_Comments_df = pd.DataFrame(
    comparability_vars_reported_Comments)
comparability_vars_reported_Comments_df = comparability_vars_reported_Comments_df.T
comparability_vars_reported_Comments_df.columns = ["comp_var_rep_info"]

######################################################
# If yes, which variables are used for comparability?
######################################################

which_comparability_vars_reported = get_data(
    if_yes_which_comparability_variables_reported_output)
which_comparability_vars_reported_df = pd.DataFrame(
    which_comparability_vars_reported)
which_comparability_vars_reported_df = which_comparability_vars_reported_df.T
which_comparability_vars_reported_df.columns = ["comp_var_raw"]

# Get Comparability Variables Reported highlighted text
which_comparability_vars_reported_df_HT = highlighted_text(
    if_yes_which_comparability_variables_reported_output)
which_comparability_vars_reported_df_HT_df = pd.DataFrame(
    which_comparability_vars_reported_df_HT)
which_comparability_vars_reported_df_HT_df = which_comparability_vars_reported_df_HT_df.T
which_comparability_vars_reported_df_HT_df.columns = ["comp_var_ht"]

# Get Comparability Variables Reported user comments
which_comparability_vars_reported_Comments = comments(
    if_yes_which_comparability_variables_reported_output)
which_comparability_vars_reported_Comments_df = pd.DataFrame(
    which_comparability_vars_reported_Comments)
which_comparability_vars_reported_Comments_df = which_comparability_vars_reported_Comments_df.T
which_comparability_vars_reported_Comments_df.columns = ["comp_var_info"]

# concatenate data frames
comparability_vars_reported_df = pd.concat([comparability_vars_reported_df, comparability_vars_reported_HT_df, comparability_vars_reported_Comments_df,
                                            which_comparability_vars_reported_df, which_comparability_vars_reported_df_HT_df, which_comparability_vars_reported_Comments_df], axis=1, sort=False)

comparability_vars_reported_df.fillna("NA", inplace=True)

print(comparability_vars_reported_df)

comparability_vars_reported_df.to_csv(
    "comparability_vars_reported.csv", index=False)
