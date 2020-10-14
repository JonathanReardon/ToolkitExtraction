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

def get_outcome_type(sample_codes):
    global outcome_type
    outcome_type = [] 
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
            outcome_type.append(outerholder)

get_outcome_type(outcome_type_codes)

outcometype_df = pd.DataFrame(outcome_type)

outcometype_df.columns=["OutcomeType_"+'{}'.format(column+1) for column in outcometype_df.columns]

outcometype_df.fillna("NA", inplace=True)

outcometype_df.to_csv("outcometype.csv", index=False)