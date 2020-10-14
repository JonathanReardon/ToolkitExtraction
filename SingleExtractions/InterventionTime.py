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

###########################################
# DIGITAL TECHNOLOGY INTERVENTION INCLUSION
###########################################

# Get Intervention Time main data
InterventionTime            = get_data(intervention_time_output)
InterventionTime_df         = pd.DataFrame(InterventionTime)
InterventionTime_df         = InterventionTime_df.T
InterventionTime_df.columns = ["int_when_raw"]

# Binarize Intervention Time data
""" InterventionTime_df["int_when_during_regular_school_hours"]  = InterventionTime_df["int_when_raw"].map(set(["During regular school hours "]).issubset).astype(int)
InterventionTime_df["int_when_before/after_school"]          = InterventionTime_df["int_when_raw"].map(set(["Before/after school"]).issubset).astype(int)
InterventionTime_df["int_when_evenings_and/or_weekends"]     = InterventionTime_df["int_when_raw"].map(set(["Evenings and/or weekends"]).issubset).astype(int)
InterventionTime_df["int_when_summer/holiday_period"]        = InterventionTime_df["int_when_raw"].map(set(["Summer/ holiday period"]).issubset).astype(int)
InterventionTime_df["int_when_other_(please_specify)"]       = InterventionTime_df["int_when_raw"].map(set(["Other (please specify)"]).issubset).astype(int)
InterventionTime_df["int_when_unclear/_not_specified"]       = InterventionTime_df["int_when_raw"].map(set(["Unclear/ not specified"]).issubset).astype(int) """

# Get Intervention Time highlighted text
InterventionTime_HT            = highlighted_text(intervention_time_output)
InterventionTime_HT_df         = pd.DataFrame(InterventionTime_HT)
InterventionTime_HT_df         = InterventionTime_HT_df.T
InterventionTime_HT_df.columns = ["int_when_ht"]

# Get Intervention Time user comments
InterventionTime_Comments            = comments(intervention_time_output)
InterventionTime_Comments_df         = pd.DataFrame(InterventionTime_Comments)
InterventionTime_Comments_df         = InterventionTime_Comments_df.T
InterventionTime_Comments_df.columns = ["int_when_info"]

# concatenate data frames
intervention_time_df = pd.concat([InterventionTime_df, InterventionTime_HT_df, InterventionTime_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_time_df.replace('\r',' ', regex=True, inplace=True)
intervention_time_df.replace('\n',' ', regex=True, inplace=True)
intervention_time_df.replace(':',' ',  regex=True, inplace=True)
intervention_time_df.replace(';',' ',  regex=True, inplace=True)

intervention_time_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_time_df.to_csv("InterventionTime.csv", index=False)