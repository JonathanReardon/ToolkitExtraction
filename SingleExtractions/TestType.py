from Main import load_json, get_data, get_outcome_lvl2
from AttributeIDList import test_type_main, test_type_output
import pandas as pd

# load json file
load_json()

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
testtype_outcome = get_outcome_lvl2(test_type_output)
testtype_outcome_df = pd.DataFrame(testtype_outcome)

# name each column (number depends on outcome number)
testtype_outcome_df.columns = [
    "out_test_type_raw_"+'{}'.format(column+1) for column in testtype_outcome_df.columns]

# concatenate data frames
""" testtype_df = pd.concat([test_type_main_df, testtype_outcome_df], axis=1, sort=False) """

# fill blanks with NA
testtype_outcome_df.fillna("NA", inplace=True)

# save to disk
""" testtype_outcome_df.to_csv("testtype.csv", index=False) """
