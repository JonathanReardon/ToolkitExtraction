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

def var_highlighted_text(codes):
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

##################################
# NUMBER OF CLASSES INTERVENTION #
##################################

number_of_classes_intervention=comments(number_of_classes_intervention_output)
number_of_classes_intervention_df=pd.DataFrame(number_of_classes_intervention)
number_of_classes_intervention_df=number_of_classes_intervention_df.T
number_of_classes_intervention_df.columns=["class_treat_info"]

number_of_classes_intervention_comments=var_highlighted_text(number_of_classes_intervention_output)
number_of_classes_intervention_comments_df=pd.DataFrame(number_of_classes_intervention_comments)
number_of_classes_intervention_comments_df=number_of_classes_intervention_comments_df.T
number_of_classes_intervention_comments_df.columns=["class_treat_ht"]

#############################
# NUMBER OF CLASSES CONTROL #
#############################

number_of_classes_control=comments(number_of_classes_control_output)
number_of_classes_control_df=pd.DataFrame(number_of_classes_control)
number_of_classes_control_df=number_of_classes_control_df.T
number_of_classes_control_df.columns=["class_cont_info"]

number_of_classes_control_comments=var_highlighted_text(number_of_classes_control_output)
number_of_classes_control_comments_df=pd.DataFrame(number_of_classes_control_comments)
number_of_classes_control_comments_df=number_of_classes_control_comments_df.T
number_of_classes_control_comments_df.columns=["class_cont_ht"]

###########################
# NUMBER OF CLASSES TOTAL #
###########################

number_of_classes_total=comments(number_of_classes_total_output)
number_of_classes_total_df=pd.DataFrame(number_of_classes_total)
number_of_classes_total_df=number_of_classes_total_df.T
number_of_classes_total_df.columns=["class_total_info"]

number_of_classes_total_comments=var_highlighted_text(number_of_classes_total_output)
number_of_classes_total_comments_df=pd.DataFrame(number_of_classes_total_comments)
number_of_classes_total_comments_df=number_of_classes_total_comments_df.T
number_of_classes_total_comments_df.columns=["class_total_ht"]

#########################################################
# NUMBER OF CLASSES NOT PROVIDED/UNCLEAR/NOT APPLICABLE #
#########################################################

number_of_classes_np = get_data(number_of_classes_not_provided_output)
number_of_classes_np_df = pd.DataFrame(number_of_classes_np)
number_of_classes_np_df=number_of_classes_np_df.T
number_of_classes_np_df.columns=["class_na_raw"]

number_of_classes_not_provided=comments(number_of_classes_not_provided_output)
number_of_classes_not_provided_df=pd.DataFrame(number_of_classes_not_provided)
number_of_classes_not_provided_df=number_of_classes_not_provided_df.T
number_of_classes_not_provided_df.columns=["class_na_info"]

number_of_classes_not_provided_comments=var_highlighted_text(number_of_classes_not_provided_output)
number_of_classes_not_provided_comments_df=pd.DataFrame(number_of_classes_not_provided_comments)
number_of_classes_not_provided_comments_df=number_of_classes_not_provided_comments_df.T
number_of_classes_not_provided_comments_df.columns=["class_na_ht"]

# CONCATENATE ALL DATAFREAMES
number_of_classes_df = pd.concat([number_of_classes_intervention_df, number_of_classes_intervention_comments_df,
                                  number_of_classes_control_df, number_of_classes_control_comments_df,
                                  number_of_classes_total_df, number_of_classes_total_comments_df,
                                  number_of_classes_np_df, number_of_classes_not_provided_df, number_of_classes_not_provided_comments_df], axis=1, sort=False)

# REPLACE (REMOVE) ESCAPE SEQUENCES FROM TEXT
number_of_classes_df.replace('\r',' ', regex=True, inplace=True)
number_of_classes_df.replace('\n',' ', regex=True, inplace=True)

number_of_classes_df.fillna("NA", inplace=True)

# SAVE DATAFRANE TO FILE
number_of_classes_df.to_csv("number_of_classes.csv", index=False)