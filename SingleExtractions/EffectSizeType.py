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

def get_effect_size_type(sample_codes):
    global effectsizetype
    effectsizetype = [] 
    for var in range(len(sample_codes)):
        for study in range(len(data["References"])):
            if "Codes" in data["References"][study]:
                if "Outcomes" in data["References"][study]:
                    outerholder = []
                    for item in range(len(data["References"][study]["Outcomes"])):
                        innerholderholder = []
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
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
            effectsizetype.append(outerholder)

get_effect_size_type(effect_size_type_output)

effectsizetype_df = pd.DataFrame(effectsizetype)

effectsizetype_df.columns=["Effect_Size_Type_Outcome_"+'{}'.format(column+1) for column in effectsizetype_df.columns]

effectsizetype_df.fillna("NA", inplace=True)

effectsizetype_df.to_csv("effectsizetype.csv", index=False)