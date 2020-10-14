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
                                for key,value in sample_codes[var].items():
                                    if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                        innerholderholder.append(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])
                        else:
                            innerholderholder=exclude
                        if len(innerholderholder)==0:
                            innerholderholder=exclude
                        outerholder.append(innerholderholder)
                else:
                    outerholder=exclude
            sample.append(outerholder)

get_sample(sample_output)

sample_df = pd.DataFrame(sample)

sample_df.columns=["Sample_Outcome_"+'{}'.format(column+1) for column in sample_df.columns]

sample_df.fillna("NA", inplace=True)

print(sample_df)

sample_df.to_csv("Sample.csv", index=False)