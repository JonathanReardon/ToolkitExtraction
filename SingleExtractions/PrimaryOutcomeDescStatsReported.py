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

def get_data(codes):
    df=[]
    for var in range(len(codes)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind)==0:
                    holderfind=exclude
                holder.append(holderfind)
        df.append(holder)
    return df

# Get Descriptive Stats (Primary Outcome) Reported main data
DescStatsPrimaryOutcomeReported            = get_data(desc_stats_primary_outcome)
DescStatsPrimaryOutcomeReported_df         = pd.DataFrame(DescStatsPrimaryOutcomeReported)
DescStatsPrimaryOutcomeReported_df         = DescStatsPrimaryOutcomeReported_df.T
DescStatsPrimaryOutcomeReported_df.columns = ["Desc_Stats_(Primary Outcome)_Reported_extract"]

# Binarize 
DescStatsPrimaryOutcomeReported_df["Desc_Stats_(Primary Outcome)_Yes"] = DescStatsPrimaryOutcomeReported_df["Desc_Stats_(Primary Outcome)_Reported_extract"].map(set(["Yes"]).issubset).astype(int)
DescStatsPrimaryOutcomeReported_df["Desc_Stats_(Primary Outcome)_No"] = DescStatsPrimaryOutcomeReported_df["Desc_Stats_(Primary Outcome)_Reported_extract"].map(set(["No"]).issubset).astype(int)

DescStatsPrimaryOutcomeReported_df.to_csv("PrimaryOutcomeDescStatsReported.csv", index=False)