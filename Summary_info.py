import json
from collections import Counter
from pprint import pprint
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# import dataset (uncomment to select dataset of choice)
with open('/home/jon/json/ToolkitExtraction/data/May12th_2020.json') as f:
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
        "In which country/countries was the study carried out? (Select ALL that apply)": 188,
        "What is the age of the students? (Select ALL that apply)": 18}

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
student_age=all[7]

codelist = [level_assignment_codes, participant_assignment_codes,
            study_realism_codes, student_gender_codes,
            pub_type_codes, edu_setting_codes, country_codes]

# data extraction for variables with one output
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

                if len(holderfind) == 0:
                    holderfind = exclude
                holder.append(holderfind)
            else:
                holder.append("No 'Codes' Section")
        all.append(holder)
    return all

data_extraction = get_data()

# data extraction for variables with multiple outputs (e.g. age)
def get_age():
    all=[]
    exclude="NA"
    holder=[]
    for section in range(len(data["References"])):
        if "Codes" in data["References"][section]:
            holderfind, holdervalue = [], []
            for study in range(len(data["References"][section]["Codes"])):
                for key, value in student_age.items():
                    if key == data["References"][section]["Codes"][study]["AttributeId"]:
                        holderfind.append(value)
            if len(holderfind) == 0:
                holderfind = exclude
            holder.append(holderfind)
        else:
            holder.append(exclude)

    #all.append(holder)
    return holder
age = get_age()

# section checker
def section_checker():
    global codes_check, outcomes_check, outcomecodes_check
    codes_check=[]
    outcomes_check=[]
    outcomecodes_check=[]
    for section in range(len(data["References"])):
        Codes="No"
        Outcomes="No"
        OutcomeCodes="No"
        if "Codes" in data["References"][section]:
            Codes="Yes"
            if "Outcomes" in data["References"][section]:
                Outcomes="Yes"
                if "OutcomeCodes" in data["References"][section]["Outcomes"][0]:
                    OutcomeCodes="Yes"
            
        codes_check.append(Codes)
        outcomes_check.append(Outcomes)
        outcomecodes_check.append(OutcomeCodes)

section_checker()

# get basic info from first outer layer 
itemids=[]
titles=[]
for section in range(len(data["References"])):
    if "ItemId" in data["References"][section]:
        itemids.append(data["References"][section]["ItemId"])
    else:
        itemids.append(exclude)
    if "ShortTitle" in data["References"][section]:
        titles.append(data["References"][section]["ShortTitle"])
    else:
        titles.append(exclude)

# get stats info from 'Outcomes' section
def get_stats():
    global outcometext, interventiontext, SMD, SESMD, CIupperSMD, CIlowerSMD
    outcometext=[]
    interventiontext=[]
    SMD=[]
    SESMD=[]
    CIupperSMD=[]
    CIlowerSMD=[]
    exclude="NA"

    for section in range(len(data["References"])):
        if "Outcomes" in data["References"][section]:
            outcometext.append(data["References"][section]["Outcomes"][0]["OutcomeText"])
            interventiontext.append(data["References"][section]["Outcomes"][0]["InterventionText"])
            SMD.append(data["References"][section]["Outcomes"][0]["SMD"])
            SESMD.append(data["References"][section]["Outcomes"][0]["SESMD"])
            CIupperSMD.append(data["References"][section]["Outcomes"][0]["CIUpperSMD"])
            CIlowerSMD.append(data["References"][section]["Outcomes"][0]["CILowerSMD"])
                    
        else:
            outcometext.append(exclude)
            interventiontext.append(exclude)
            SMD.append(exclude)
            SESMD.append(exclude)
            CIupperSMD.append(exclude)
            CIlowerSMD.append(exclude)
get_stats()


df = pd.DataFrame(list(zip(itemids, titles, data_extraction[0], data_extraction[1], data_extraction[2], data_extraction[3], 
                           data_extraction[4], data_extraction[5], data_extraction[6], age, 
                           outcometext, interventiontext, SMD, SESMD, CIupperSMD, CIlowerSMD,
                           codes_check, outcomes_check, outcomecodes_check)), 
                  columns=['ItemID', 'Author', 'LevelofAssignment','ParticipantAssignment','StudyRealism','StudentGender', 
                           'PublicationType', 'EducationalSetting', 'Country', 'StudentAge', 
                           'Outcome', 'Intervention', 'SMD', 'SESMD', 'CIupper', 'CIlower',
                           'CodesPresent', 'OutcomesPresent',
                           'OutcomeCodesPresent'])
pprint(df)

df.to_csv("test.csv", index=False)
