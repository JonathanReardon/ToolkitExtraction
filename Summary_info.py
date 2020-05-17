import json
from collections import Counter
from pprint import pprint
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('ggplot')

# import dataset (uncomment to select dataset of choice)
with open('/home/jon/json/ToolkitExtraction/data/May 12th_2020.json') as f:
    data=json.load(f)

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []
    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

x = extract_values(data,'AttributeName')
y = extract_values(data,'AttributeId')

df=[]
for xs, ys in zip(x, y):
    df.append([xs, ys])

# Variable option counts
dict = {"Toolkit strand(s) (select at least one Toolkit strand)": 34,
        "What was the level of assignment?": 7, 
        "How were participants assigned?": 8,
        "How realistic was the study?": 4, 
        "What is the gender of the students?": 5,
        "What is the age of the students? (Select ALL that apply)": 18, 
        "Section 1 What is the publication type?": 6,
        "What is the educational setting (Select ALL that apply)": 12,
        "In which country/countries was the study carried out? (Select ALL that apply)": 188}

def get_info():
    fullset=[]
    for question, option_count in dict.items():
        for counter, item in enumerate(df):
            if item[0] == question:
                holder={}
                for i in range(1,option_count):
                    holder.update( {df[counter+i][1]:df[counter+i][0]} )
                fullset.append(holder)
    return fullset

all = get_info()

for dict in all:
    pprint(dict)
