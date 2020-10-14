import json
from collections import Counter
from pprint import pprint
import numpy as np
import pandas as pd

from questions import *

# input data file name (.csv) with full path
datafile = '/home/jon/json/ToolkitExtraction/Data/May12th_2020.json'

# import dataset (uncomment to select dataset of choice)
with open(datafile) as f:
    data=json.load(f)

# for missing or unavailable data
exclude="NA"

# get toolkit strand data from Outcomes
def get_strands(strand_codes):
    global strand
    strand = [] 
    for var in range(len(strand_codes)):
        # for study in range(len(data["References"])):
        for study in range(len(data["References"])):
            if "Codes" in data["References"][study]:
                if "Outcomes" in data["References"][study]:
                    outerholder = []
                    for item in range(len(data["References"][study]["Outcomes"])):
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
                            innerholderholder = []
                            for subsection in range(10):
                                if subsection < len(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"]):
                                    for key,value in strand_codes[var].items():
                                        if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                            innerholderholder.append(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])
                                else:
                                    pass
                        outerholder.append(innerholderholder)
            strand.append(outerholder)

get_strands(strand_output) 

df = pd.DataFrame(strand)

df = df.iloc[:, :-2]

df.columns = ["ToolkitStrand_Outcome_1", "ToolkitStrand_Outcome_2", "ToolkitStrand_Outcome_3", "ToolkitStrand_Outcome_4",
              "ToolkitStrand_Outcome_5", "ToolkitStrand_Outcome_6", "ToolkitStrand_Outcome_7", "ToolkitStrand_Outcome_8",
              "ToolkitStrand_Outcome_9", "ToolkitStrand_Outcome_10"]

pprint(df)

# save dataframe to file (.csv)
df.to_csv("Strands.csv", index=False)