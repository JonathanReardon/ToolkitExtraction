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

# Get Intervention Frequency highlighted text
InterventionFrequency_HT            = highlighted_text(intervention_frequency_output)
InterventionFrequency_HT_df         = pd.DataFrame(InterventionFrequency_HT)
InterventionFrequency_HT_df         = InterventionFrequency_HT_df.T
InterventionFrequency_HT_df.columns = ["int_freq_ht"]

# Get Intervention Frequency user comments
InterventionFrequency_Comments            = comments(intervention_frequency_output)
InterventionFrequency_Comments_df         = pd.DataFrame(InterventionFrequency_Comments)
InterventionFrequency_Comments_df         = InterventionFrequency_Comments_df.T
InterventionFrequency_Comments_df.columns = ["int_freq_info"]

# concatenate data frames
intervention_frequency_df = pd.concat([InterventionFrequency_HT_df, InterventionFrequency_Comments_df], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_frequency_df.replace('\r',' ', regex=True, inplace=True)
intervention_frequency_df.replace('\n',' ', regex=True, inplace=True)
intervention_frequency_df.replace(':',' ',  regex=True, inplace=True)
intervention_frequency_df.replace(';',' ',  regex=True, inplace=True)

intervention_frequency_df.fillna("NA", inplace=True)

# Save to file (.csv)
intervention_frequency_df.to_csv("InterventionFrequency.csv", index=False)

print(intervention_frequency_df)