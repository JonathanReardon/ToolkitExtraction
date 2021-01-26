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


# Get Descriptive Stats (Primary Outcome) Reported main data
DescStatsPrimaryOutcomeReported = get_data(desc_stats_primary_outcome)
DescStatsPrimaryOutcomeReported_df = pd.DataFrame(
    DescStatsPrimaryOutcomeReported)
DescStatsPrimaryOutcomeReported_df = DescStatsPrimaryOutcomeReported_df.T
DescStatsPrimaryOutcomeReported_df.columns = ["desc_stats_raw"]

# Binarize
""" DescStatsPrimaryOutcomeReported_df["Desc_Stats_(Primary Outcome)_Yes"] = DescStatsPrimaryOutcomeReported_df["Desc_Stats_(Primary Outcome)_Reported_extract"].map(set(["Yes"]).issubset).astype(int)
DescStatsPrimaryOutcomeReported_df["Desc_Stats_(Primary Outcome)_No"] = DescStatsPrimaryOutcomeReported_df["Desc_Stats_(Primary Outcome)_Reported_extract"].map(set(["No"]).issubset).astype(int) """

# Get Descriptive Stats (Primary Outcome) Reported highlighted text
DescStatsPrimaryOutcomeReported_HT = highlighted_text(
    desc_stats_primary_outcome)
DescStatsPrimaryOutcomeReported_HT_df = pd.DataFrame(
    DescStatsPrimaryOutcomeReported_HT)
DescStatsPrimaryOutcomeReported_HT_df = DescStatsPrimaryOutcomeReported_HT_df.T
DescStatsPrimaryOutcomeReported_HT_df.columns = ["desc_stats_ht"]

# Get Descriptive Stats (Primary Outcome) Reported user comments
DescStatsPrimaryOutcomeReported_Comments = comments(desc_stats_primary_outcome)
DescStatsPrimaryOutcomeReported_Comments_df = pd.DataFrame(
    DescStatsPrimaryOutcomeReported_Comments)
DescStatsPrimaryOutcomeReported_Comments_df = DescStatsPrimaryOutcomeReported_Comments_df.T
DescStatsPrimaryOutcomeReported_Comments_df.columns = ["desc_stats_info"]

# concatenate data frames
DescStatsOutcomeReported_df = pd.concat(
    [DescStatsPrimaryOutcomeReported_df, DescStatsPrimaryOutcomeReported_HT_df, DescStatsPrimaryOutcomeReported_Comments_df], axis=1, sort=False)

DescStatsOutcomeReported_df.fillna("NA", inplace=True)

print(DescStatsOutcomeReported_df)

""" DescStatsOutcomeReported_df.to_csv("DescStatsReported.csv", index=False) """
