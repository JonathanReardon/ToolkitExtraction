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
        for study in range(2):
            if "Codes" in data["References"][study]:
                if "Outcomes" in data["References"][study]:
                    outerholder = []
                    for item in range(len(data["References"][study]["Outcomes"])):
                        innerholderholder=[]
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
                            for subsection in range(len(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"])):
                                for key,value in strand_codes[var].items():
                                    if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                        innerholderholder.append(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])

                        outerholder.append(innerholderholder)
        strand.append(outerholder)

get_strands(strand_output) 

df = pd.DataFrame(strand)

pprint(df)

# save dataframe to file (.csv)
df.to_csv("Strands.csv", index=False)