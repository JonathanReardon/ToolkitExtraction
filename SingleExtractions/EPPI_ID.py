import os
import json
import pandas as pd

from AttributeIDList import *
from DATAFILE import file

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data=json.load(f)

def get_EPPI_IDs():
    global eppiids
    eppiids = []
    for section in range(len(data["References"])):
        if data["References"][section]["ItemId"]:
            eppiids.append(data["References"][section]["ItemId"])
        else:
            eppiids.append("NA")
            
get_EPPI_IDs()

eppiid_df = pd.DataFrame(eppiids)
eppiid_df.columns=["id"]

eppiid_df.to_csv("eppiid.csv", index=False)


