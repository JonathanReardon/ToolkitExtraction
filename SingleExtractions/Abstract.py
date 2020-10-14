import os
import json
import pandas as pd

from AttributeIDList import *
from DATAFILE import file

exclude="NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data=json.load(f)

def get_abstract():
    global abstract
    abstract = []
    for section in range(len(data["References"])):
        if data["References"][section]["Abstract"]:
            abstract.append(data["References"][section]["Abstract"])
        else:
            abstract.append(exclude)
            
get_abstract()

abstract_df = pd.DataFrame(abstract)
abstract_df.columns=["abstract"]

abstract_df.fillna("NA", inplace=True)

abstract_df.to_csv("abstract.csv", index=False)