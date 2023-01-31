from Main import load_json, get_outcome_lvl2
from AttributeIDList import test_type_output
import pandas as pd

# load json file
load_json()

# get test type data
testtype = get_outcome_lvl2(test_type_output)
testtype_df = pd.DataFrame(testtype)

# name each column (number depends on outcome number)
testtype_df.columns = [
    "out_test_type_raw_"+'{}'.format(column+1) for column in testtype_df.columns]

# fill blanks with NA
testtype_df.fillna("NA", inplace=True)

# save to disk
""" testtype_df.to_csv("outcome_testtype.csv", index=False) """

""" print(testtype_df) """