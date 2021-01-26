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


publicationtype = get_data(publication_type_output)

publicationtype_df = pd.DataFrame(publicationtype)
publicationtype_df = publicationtype_df.T
publicationtype_df.columns = ["pub_type_raw"]

""" publicationtype_df["pub_type_journal_article"]        = publicationtype_df["pub_type"].map(set(['Journal article']).issubset).astype(int)
publicationtype_df["pub_type_dissertation_or_thesis"] = publicationtype_df["pub_type"].map(set(['Dissertation or thesis']).issubset).astype(int)
publicationtype_df["pub_type_technical_report"]       = publicationtype_df["pub_type"].map(set(['Technical report']).issubset).astype(int)
publicationtype_df["pub_type_book_or_book_chapter"]   = publicationtype_df["pub_type"].map(set(['Book or book chapter']).issubset).astype(int)
publicationtype_df["pub_type_conference_paper"]       = publicationtype_df["pub_type"].map(set(['Conference paper']).issubset).astype(int) """

# Get Publication Type highlighted text
publicationtype_HT = highlighted_text(publication_type_output)
publicationtype_HT_df = pd.DataFrame(publicationtype_HT)
publicationtype_HT_df = publicationtype_HT_df.T
publicationtype_HT_df.columns = ["pubtype_ht"]

# Get Publication Type user comments
publicationtype_Comments = comments(publication_type_output)
publicationtype_Comments_df = pd.DataFrame(publicationtype_Comments)
publicationtype_Comments_df = publicationtype_Comments_df.T
publicationtype_Comments_df.columns = ["pubtype_info"]

# concatenate data frames
publication_type_df = pd.concat(
    [publicationtype_df, publicationtype_HT_df, publicationtype_Comments_df], axis=1, sort=False)

publication_type_df.fillna("NA", inplace=True)

print(publication_type_df)

publication_type_df.to_csv("publicationtype.csv", index=False)
