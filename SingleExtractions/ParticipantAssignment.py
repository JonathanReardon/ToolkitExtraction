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
                    holderfind = [exclude]
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


participantassignment = get_data(participant_assignment_output)
participantassignment_df = pd.DataFrame(participantassignment)
participantassignment_df = participantassignment_df.T
participantassignment_df.columns = ["part_assig_raw"]

# remove square brackets
participantassignment_df['part_assig_raw'] = participantassignment_df['part_assig_raw'].str[0]

# convert each variable to binary
""" participantassignment_df["part_assig_raw_random_(please_specify)"]                       = participantassignment_df['part_assig_raw'].isin(["Random (please specify)"]).astype(int)
participantassignment_df["part_assig_raw_non-random_but_matched"]                        = participantassignment_df['part_assig_raw'].isin(["Non-random, but matched"]).astype(int)
participantassignment_df["part_assig_raw_non-random_not_matched_prior_to_treatment"]     = participantassignment_df['part_assig_raw'].isin(['Non-random, not matched prior to treatment']).astype(int)
participantassignment_df["part_assig_raw_unclear"]                                       = participantassignment_df['part_assig_raw'].isin(['Unclear']).astype(int)
participantassignment_df["part_assig_raw_not_assigned_-_naturally_occurring_sample"]     = participantassignment_df['part_assig_raw'].isin(['Not assigned - naturally occurring sample']).astype(int)
participantassignment_df["part_assig_raw_retrospective_quasi_experimental_design_(QED)"] = participantassignment_df['part_assig_raw'].isin(['Retrospective Quasi Experimental Design (QED)']).astype(int)
participantassignment_df["part_assig_raw_regression_discontinuity"]                      = participantassignment_df['part_assig_raw'].isin(['Regression discontinuity']).astype(int) """

# Get Level of Assignment highlighted text
participantassignment_HT = highlighted_text(participant_assignment_output)
participantassignment_HT_df = pd.DataFrame(participantassignment_HT)
participantassignment_HT_df = participantassignment_HT_df.T
participantassignment_HT_df.columns = ["part_assig_ht"]

# Get Level of Assignment user comments
participantassignment_Comments = comments(participant_assignment_output)
participantassignment_Comments_df = pd.DataFrame(
    participantassignment_Comments)
participantassignment_Comments_df = participantassignment_Comments_df.T
participantassignment_Comments_df.columns = ["part_assig_info"]

# concatenate data frames
participant_assignment_df = pd.concat(
    [participantassignment_df, participantassignment_HT_df, participantassignment_Comments_df], axis=1, sort=False)

participant_assignment_df.fillna("NA", inplace=True)

participant_assignment_df.replace('\r', ' ', regex=True, inplace=True)
participant_assignment_df.replace('\n', ' ', regex=True, inplace=True)
participant_assignment_df.replace(':', ' ',  regex=True, inplace=True)
participant_assignment_df.replace(';', ' ',  regex=True, inplace=True)

participant_assignment_df.to_csv("participantassignment.csv", index=False)
