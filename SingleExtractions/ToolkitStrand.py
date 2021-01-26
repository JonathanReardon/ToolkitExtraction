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


def get_toolkit_strand(sample_codes):
    global toolkit_strand
    toolkit_strand = []
    for var in range(len(sample_codes)):
        for study in range(len(data["References"])):
            if "Codes" in data["References"][study]:
                if "Outcomes" in data["References"][study]:
                    outerholder = []
                    for item in range(len(data["References"][study]["Outcomes"])):
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
                            innerholderholder = []
                            for subsection in range(len(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"])):
                                for key, value in sample_codes[var].items():
                                    if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                        innerholderholder.append(
                                            data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])
                        else:
                            innerholderholder = exclude
                        if len(innerholderholder) == 0:
                            innerholderholder = exclude
                        outerholder.append(innerholderholder)
                else:
                    outerholder = [exclude]
            toolkit_strand.append(outerholder)


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


get_toolkit_strand(toolkit_strand_codes)

toolkitstrand_Comments = comments(toolkit_strand_codes)
toolkitstrand_Comments_df = pd.DataFrame(toolkitstrand_Comments)
toolkitstrand_Comments_df = toolkitstrand_Comments_df.T
toolkitstrand_Comments_df.columns = ["_info"]
toolkitstrand_df = pd.DataFrame(toolkit_strand)

toolkitstrand_df.fillna("NA", inplace=True)
toolkitstrand_df.columns = [
    "out_strand_"+'{}'.format(column+1) for column in toolkitstrand_df.columns]

print(toolkitstrand_df)
toolkitstrand_df.to_csv("toolkitstrand.csv", index=False)
