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


def get_pubtype_eppi():
    global pubtype_eppi
    pubtype_eppi = []
    for section in range(len(data["References"])):
        if data["References"][section]["TypeName"]:
            pubtype_eppi.append(data["References"][section]["TypeName"])
        else:
            pubtype_eppi.append(exclude)


get_pubtype_eppi()

pubtype_eppi_df = pd.DataFrame(pubtype_eppi)
pubtype_eppi_df.columns = ["pub_eppi"]

pubtype_eppi_df.fillna("NA", inplace=True)

print(pubtype_eppi_df)

pubtype_eppi_df.to_csv("pubtype_eppi.csv", index=False)
