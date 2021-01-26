import os
import json
import pandas as pd

from CODES import other_outcomes_output
from CODES import additional_outcomes_output
from CODES import other_participants_output
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
                holderfind = []
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

#################
# Other outcomes
#################

# raw data
other_outcomes = get_data(other_outcomes_output)
other_outcomes_df = pd.DataFrame(other_outcomes)
other_outcomes_df = other_outcomes_df.T
other_outcomes_df.columns = ["out_other_raw"]

# highlighted text
other_outcomes_HT = highlighted_text(other_outcomes_output)
other_outcomes_HT_df = pd.DataFrame(other_outcomes_HT)
other_outcomes_HT_df = other_outcomes_HT_df.T
other_outcomes_HT_df.columns = ["out_other_ht"]

# comments
other_outcomes_info = comments(other_outcomes_output)
other_outcomes_info_df = pd.DataFrame(other_outcomes_info)
other_outcomes_info_df = other_outcomes_info_df.T
other_outcomes_info_df.columns = ["out_other_info"]

######################
# Additional outcomes
######################

# raw data
additional_outcomes = get_data(additional_outcomes_output)
additional_outcomes_df = pd.DataFrame(additional_outcomes)
additional_outcomes_df = additional_outcomes_df.T
additional_outcomes_df.columns = ["out_info_raw"]

# highlighted text
additional_outcomes_ht = highlighted_text(additional_outcomes_output)
additional_outcomes_ht_df = pd.DataFrame(additional_outcomes_ht)
additional_outcomes_ht_df = additional_outcomes_ht_df.T
additional_outcomes_ht_df.columns = ["out_info_raw"]

# comments
additional_outcomes_info = comments(additional_outcomes_output)
additional_outcomes_info_df = pd.DataFrame(additional_outcomes_info)
additional_outcomes_info_df = additional_outcomes_info_df.T
additional_outcomes_info_df.columns = ["out_info_info"]

#####################
# Other participants
#####################

# highlighted text
other_participants_ht = highlighted_text(other_participants_output)
other_participants_ht_df = pd.DataFrame(other_participants_ht)
other_participants_ht_df = other_participants_ht_df.T
other_participants_ht_df.columns = ["part_other_ht"]

# comments
other_participants_info = comments(other_participants_output)
other_participants_info_df = pd.DataFrame(other_participants_info)
other_participants_info_df = other_participants_info_df.T
other_participants_info_df.columns = ["part_other_info"]

# concatenate data frames
other_outcomes_df = pd.concat([other_outcomes_df, other_outcomes_HT_df, other_outcomes_info_df,
                additional_outcomes_df, additional_outcomes_ht_df, additional_outcomes_info_df,
                other_participants_ht_df, other_participants_info_df], axis=1, sort=False)

other_outcomes_df.fillna("NA", inplace=True)

print(other_outcomes_df)

other_outcomes_df.to_csv(
    "other_outcomes.csv", index=False)