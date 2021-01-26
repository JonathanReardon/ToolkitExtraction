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


def get_test_type(sample_codes):
    global testtype_outcome
    testtype_outcome = []
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
                    outerholder = exclude
            testtype_outcome.append(outerholder)


# get test type main extraction data
test_type_main = get_data(test_type_main)
test_type_main_df = pd.DataFrame(test_type_main)
test_type_main_df = test_type_main_df.T
test_type_main_df.columns = ["test_type_raw"]

test_type_main_df["test_type_standardised_test"] = test_type_main_df["test_type_raw"].map(
    set(['Standardised test']).issubset).astype(int)
test_type_main_df["test_type_researcher_developed_test"] = test_type_main_df["test_type_raw"].map(
    set(['Researcher developed test']).issubset).astype(int)
test_type_main_df["test_type_school_developed_test"] = test_type_main_df["test_type_raw"].map(
    set(['School-developed test']).issubset).astype(int)
test_type_main_df["test_type_normal_test_or_examination"] = test_type_main_df["test_type_raw"].map(
    set(['National test or examination']).issubset).astype(int)
test_type_main_df["test_type_international_tests"] = test_type_main_df["test_type_raw"].map(
    set(['International tests']).issubset).astype(int)

# get test type outcome data
get_test_type(test_type_output)
testtype_outcome_df = pd.DataFrame(testtype_outcome)
testtype_outcome_df.columns = [
    "out_test_type_raw_"+'{}'.format(column+1) for column in testtype_outcome_df.columns]

# concatenate data frames
""" testtype_df = pd.concat([test_type_main_df, testtype_outcome_df], axis=1, sort=False) """

testtype_outcome_df.fillna("NA", inplace=True)

print(testtype_outcome_df)

testtype_outcome_df.to_csv("testtype.csv", index=False)
