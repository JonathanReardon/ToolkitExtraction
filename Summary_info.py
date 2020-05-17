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
dict = {"What was the level of assignment?": 7, 
        "How were participants assigned?": 8,
        "How realistic was the study?": 4, 
        "What is the gender of the students?": 5,
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

level_assignment_codes=all[0]
participant_assignment_codes=all[1]
study_realism_codes=all[2]
student_gender_codes=all[3]
pub_type_codes=all[4]
edu_setting_codes=all[5]
country_codes=all[6]

codelist = [level_assignment_codes, participant_assignment_codes,
            study_realism_codes, student_gender_codes,
            pub_type_codes, edu_setting_codes, country_codes]

def get_data():
    all=[]
    exclude="NA"
    for var in range(len(codelist)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codelist[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind, holdervalue = value, key
                holder.append(holderfind)
        all.append(holder)
    return all

data = get_data()
for lst in data:
    print(len(lst))


