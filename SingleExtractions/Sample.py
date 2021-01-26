import os
import json
import pandas as pd

from CODES import *
from DATAFILE import file

from eppi_ID import eppiid_df

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


def get_sample(sample_codes):
    global sample
    sample = []
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
            sample.append(outerholder)


get_sample(sample_output)
sample_df = pd.DataFrame(sample)
sample_df.columns = ["out_samp_" +
                     '{}'.format(column+1) for column in sample_df.columns]

print(sample_df)

sample_main_check = get_data(sample_output)
sample_main_check_df = pd.DataFrame(sample_main_check)
sample_main_check_df = sample_main_check_df.T
sample_main_check_df.columns = ["main_check"]

all_variables = pd.concat(
    [eppiid_df, sample_df, sample_main_check_df], axis=1, sort=False)

all_variables.fillna("NA", inplace=True)

all_variables.to_csv("Sample.csv", index=False)
