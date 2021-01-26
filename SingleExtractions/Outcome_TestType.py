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

def get_test_type(sample_codes):
    global test_type
    test_type = []
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
            test_type.append(outerholder)

get_test_type(test_type_output)
testtype_df = pd.DataFrame(test_type)

testtype_df.fillna("NA", inplace=True)
testtype_df.columns = [
    "out_test_type_raw_"+'{}'.format(column+1) for column in testtype_df.columns]

print(testtype_df)
testtype_df.to_csv("outcome_testtype.csv", index=False)