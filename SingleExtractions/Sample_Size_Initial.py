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

#############################################
# Initial sample size for intervention group
#############################################

# highlighted text
sample_size_intervention=var_highlighted_text(sample_size_intervention_output)
sample_size_intervention_df=pd.DataFrame(sample_size_intervention)
sample_size_intervention_df=sample_size_intervention_df.T
sample_size_intervention_df.columns=["base_n_treat_ht"]

# comments
sample_size_intervention_comments=var_comments(sample_size_intervention_output)
sample_size_intervention_comments_df=pd.DataFrame(sample_size_intervention_comments)
sample_size_intervention_comments_df=sample_size_intervention_comments_df.T
sample_size_intervention_comments_df.columns=["base_n_treat_info"]

############################################
# Initial sample size for the control group
############################################

# highlighted text
sample_size_control=var_highlighted_text(sample_size_control_output)
sample_size_control_df=pd.DataFrame(sample_size_control)
sample_size_control_df=sample_size_control_df.T
sample_size_control_df.columns=["base_n_cont_ht"]

# comments
sample_size_control_comments=var_comments(sample_size_control_output)
sample_size_control_comments_df=pd.DataFrame(sample_size_control_comments)
sample_size_control_comments_df=sample_size_control_comments_df.T
sample_size_control_comments_df.columns=["base_n_cont_info"]

########################################################
# Initial sample size for the second intervention group
########################################################

# highlighted text
sample_size_second_intervention=var_highlighted_text(sample_size_second_intervention_output)
sample_size_second_intervention_df=pd.DataFrame(sample_size_second_intervention)
sample_size_second_intervention_df=sample_size_second_intervention_df.T
sample_size_second_intervention_df.columns=["base_n_treat2_ht"]

# comments
sample_size_second_intervention_comments=var_comments(sample_size_second_intervention_output)
sample_size_second_intervention_comments_df=pd.DataFrame(sample_size_second_intervention_comments)
sample_size_second_intervention_comments_df=sample_size_second_intervention_comments_df.T
sample_size_second_intervention_comments_df.columns=["base_n_treat2_info"]

#######################################################
# Initial sample size for the third intervention group
#######################################################

# highlighted text
sample_size_third_intervention=var_highlighted_text(sample_size_third_intervention_output)
sample_size_third_intervention_df=pd.DataFrame(sample_size_third_intervention)
sample_size_third_intervention_df=sample_size_third_intervention_df.T
sample_size_third_intervention_df.columns=["base_n_treat3_ht"]

# comments
sample_size_third_intervention_comments=var_comments(sample_size_third_intervention_output)
sample_size_third_intervention_comments_df=pd.DataFrame(sample_size_third_intervention_comments)
sample_size_third_intervention_comments_df=sample_size_third_intervention_comments_df.T
sample_size_third_intervention_comments_df.columns=["base_n_treat3_info"]

# CONCATENATE ALL DATAFREAMES
initial_sample_size_df = pd.concat([sample_size_intervention_df, sample_size_intervention_comments_df,
                                    sample_size_control_df, sample_size_control_comments_df,
                                    sample_size_second_intervention_df, sample_size_second_intervention_comments_df,
                                    sample_size_third_intervention_df, sample_size_third_intervention_comments_df], axis=1, sort=False)

# REPLACE (REMOVE) ESCAPE SEQUENCES FROM TEXT
initial_sample_size_df.replace('\r',' ', regex=True, inplace=True)
initial_sample_size_df.replace('\n',' ', regex=True, inplace=True)

initial_sample_size_df.fillna("NA", inplace=True)

print(initial_sample_size_df)

initial_sample_size_df.to_csv("initial_sample_size.csv", index=False)