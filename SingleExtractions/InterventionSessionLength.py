import os
import json
import pandas as pd

from CODES import *
from DATAFILE import file

exclude="NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data=json.load(f)

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

# Get Intervention Session Length highlighted text
InterventionSessionLength_HT            = highlighted_text(intervention_session_length_output)
InterventionSessionLength_HT_df         = pd.DataFrame(InterventionSessionLength_HT)
InterventionSessionLength_HT_df         = InterventionSessionLength_HT_df.T
InterventionSessionLength_HT_df.columns = ["int_leng_ht"]

# Get Intervention Session Length user comments
InterventionSessionLength_Comments            = comments(intervention_session_length_output)
InterventionSessionLength_Comments_df         = pd.DataFrame(InterventionSessionLength_Comments)
InterventionSessionLength_Comments_df         = InterventionSessionLength_Comments_df.T
InterventionSessionLength_Comments_df.columns = ["int_leng_info"]

# concatenate data frames
intervention_session_length_df = pd.concat([InterventionSessionLength_HT_df, InterventionSessionLength_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_session_length_df.replace('\r',' ', regex=True, inplace=True)
intervention_session_length_df.replace('\n',' ', regex=True, inplace=True)
intervention_session_length_df.replace(':',' ',  regex=True, inplace=True)
intervention_session_length_df.replace(';',' ',  regex=True, inplace=True)

intervention_session_length_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_session_length_df.to_csv("InterventionSessionLength.csv", index=False)

print(intervention_session_length_df)