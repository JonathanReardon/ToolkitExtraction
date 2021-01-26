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

def get_author_name():
    global author
    author = []
    for section in range(len(data["References"])):
        if data["References"][section]["ShortTitle"]:
            author.append(data["References"][section]["ShortTitle"])
        else:
            author.append(exclude)
            
get_author_name()

author_df = pd.DataFrame(author)
author_df.columns=["pub_author"]

author_df.fillna("NA", inplace=True)

print(author_df)

author_df.to_csv("author.csv", index=False)

