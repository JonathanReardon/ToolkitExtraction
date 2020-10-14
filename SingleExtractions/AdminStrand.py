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

admin_strand = get_data(admin_strand_output) 

# Get Admin Strand main data
adminstrand_df = pd.DataFrame(admin_strand)
adminstrand_df = adminstrand_df.T
adminstrand_df.columns=["strand_raw"]

# Get Admin Strand Update 2020 data
admin_strand_other = get_data(admin_strand_secondary)

adminstrand_secondary_df = pd.DataFrame(admin_strand_other)
adminstrand_secondary_df = adminstrand_secondary_df.T
adminstrand_secondary_df.columns=["FB_Update_2020"]

# Get Strand comment data
""" admin_strand_comments            = comments(admin_strand_output)
admin_strand_comments_df         = pd.DataFrame(admin_strand_comments)
admin_strand_comments_df         = admin_strand_comments_df.T
admin_strand_comments_df.columns = ["strand_info"] """

# concatenate data frames
admin_strand_df = pd.concat([adminstrand_df, adminstrand_secondary_df], axis=1, sort=False)

admin_strand_df.replace('\r',' ', regex=True, inplace=True)
admin_strand_df.replace('\n',' ', regex=True, inplace=True)
admin_strand_df.replace(':',' ',  regex=True, inplace=True)
admin_strand_df.replace(';',' ',  regex=True, inplace=True)

admin_strand_df.fillna("NA", inplace=True)

admin_strand_df.to_csv("adminstrand.csv", index=False)