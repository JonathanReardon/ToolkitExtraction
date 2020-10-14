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

# data admin strand data (possible multiple outputs)
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

def var_comments(codes):
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

# extract highlighted text for each var
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

#######################################
# PERCENTAGE OF LOW SES/FSM IN SAMPLE #
#######################################

low_ses_percentage=var_comments(percentage_low_fsm_output)

low_ses_percentage_df=pd.DataFrame(low_ses_percentage)
low_ses_percentage_df=low_ses_percentage_df.T
low_ses_percentage_df.columns=["fsm_perc_info"]

low_ses_percentage_comments=var_highlighted_text(percentage_low_fsm_output)

low_ses_percentage_comments_df=pd.DataFrame(low_ses_percentage_comments)
low_ses_percentage_comments_df=low_ses_percentage_comments_df.T
low_ses_percentage_comments_df.columns=["fsm_perc_ht"]

#############################################
# FURTHER LOW SES/FSM INFORMATION IN SAMPLE #
#############################################

further_ses_info=var_comments(further_ses_fsm_info_output)

further_ses_fsm_info_df=pd.DataFrame(further_ses_info)
further_ses_fsm_info_df=further_ses_fsm_info_df.T
further_ses_fsm_info_df.columns=["fsm_info_info"]

further_ses_fsm_info_comments=var_highlighted_text(further_ses_fsm_info_output)

further_ses_fsm_info_comments_df=pd.DataFrame(further_ses_fsm_info_comments)
further_ses_fsm_info_comments_df=further_ses_fsm_info_comments_df.T
further_ses_fsm_info_comments_df.columns=["fsm_info_ht"]

#######################################
# NO LOW SES/FSM INFORMATION PROVIDED #
#######################################

no_low_ses_fsm_info = get_data(no_ses_fsm_info_provided_output)

no_low_ses_fsm_info_df=pd.DataFrame(no_low_ses_fsm_info)
no_low_ses_fsm_info_df=no_low_ses_fsm_info_df.T
no_low_ses_fsm_info_df.columns=["fsm_na"]

""" no_low_ses_fsm_info_df["No_SES_FSM_Info"]=no_low_ses_fsm_info_df["No_SES_FSM_Info_Provided"].map(set(['No SES/FSM Information Provided']).issubset).astype(int) """

# CONCATENATE ALL DATAFREAMES
ses_fsm_df = pd.concat([low_ses_percentage_df, low_ses_percentage_comments_df,
                        further_ses_fsm_info_df, further_ses_fsm_info_comments_df,
                        no_low_ses_fsm_info_df], axis=1, sort=False)

# REPLACE (REMOVE) ESCAPE SEQUENCES FROM TEXT
ses_fsm_df.replace('\r',' ', regex=True, inplace=True)
ses_fsm_df.replace('\n',' ', regex=True, inplace=True)
ses_fsm_df.replace(':',' ',  regex=True, inplace=True)
ses_fsm_df.replace(';',' ',  regex=True, inplace=True)

ses_fsm_df.fillna("NA", inplace=True)

# SAVE DATAFRANE TO FILE
ses_fsm_df.to_csv("sesfsm.csv", index=False)