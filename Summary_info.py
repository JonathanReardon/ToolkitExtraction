import json
from collections import Counter
from pprint import pprint
import numpy as np
import pandas as pd

# import dataset (uncomment to select dataset of choice)
with open('/home/jon/json/ToolkitExtraction/data/May12th_2020.json') as f:
    data=json.load(f)

# for missing or unavailable data
exclude=np.nan

# flatten json into list of lists
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
strand_option = {"Toolkit strand(s) (select at least one Toolkit strand)": 34}

single_option = {"What was the level of assignment?": 7, 
                 "How were participants assigned?": 8,
                 "How realistic was the study?": 4, 
                 "What is the gender of the students?": 5,
                 "Section 1 What is the publication type?": 6,
                 "What is the educational setting (Select ALL that apply)": 12,
                 "In which country/countries was the study carried out? (Select ALL that apply)": 188,
                 "Does the study report any group differences at baseline? ": 3,
                 "What was the study design?": 10,
                 "Is comparability taken into account in the analysis?": 4,
                 "Are the variables used for comparability reported?": 4,
                 "If yes, which variables are used for comparability?": 6,
                 "What type of organisation was responsible for providing the intervention?": 7,
                 "Was training for the intervention provided?": 4} 

multi_option = {"What is the age of the students? (Select ALL that apply)": 18,
                "Is attrition or drop out reported?": 4,
                "Who is the focus of the intervention? (Select ALL that apply)": 9,
                "What is the intervention teaching approach? (Select ALL that apply)": 7,
                "When did the intervention take place?  (Select ALL that apply)": 7,
                "Who was responsible for the teaching at the point of delivery? (Select ALL that apply)": 11}


def get_info(question_dict):
    fullset=[]
    for question, option_count in question_dict.items():
        for counter, item in enumerate(df):
            if item[0] == question:
                holder={}
                for i in range(1,option_count):
                    holder.update( {df[counter+i][1]:df[counter+i][0]} )
                fullset.append(holder)
    return fullset

strand_output = get_info(strand_option)
single_output = get_info(single_option)
multi_output  = get_info(multi_option)

# extract user inputted comments for each var
def var_comments(codes):
    all_comments=[]
    for var in range(len(codes)):
        comment=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                perstudy=[]
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            if data["References"][section]["Codes"][study]["AdditionalText"]:
                                perstudy.append(data["References"][section]["Codes"][study]["AdditionalText"])
                            if "ItemAttributeFullTextDetails" in data["References"][section]["Codes"][study]:
                                if data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"]:
                                    for i in range(len(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"])):
                                        perstudy.append(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"][i]["Text"])
                if len(perstudy) ==0:
                    perstudy=exclude 
                comment.append(perstudy)
            else:
                comment.append(exclude)
        all_comments.append(comment)
    return all_comments

single_output_comments = var_comments(single_output)
multi_output_comments  = var_comments(multi_output)

# data extraction for variables with one output
def get_data(data_codes):
    all=[]
    for var in range(len(data_codes)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in data_codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind, holdervalue = value, key
                if len(holderfind) == 0:
                    holderfind = exclude
                holder.append(holderfind)
            else:
                holder.append("No 'Codes' Section")
        all.append(holder)
    return all
data_single = get_data(single_output)

# data extraction for variables with multiple outputs (e.g. age)
def get_multi_data(data_codes):
    all=[]
    for var in range(len(data_codes)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in data_codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind)==0:
                    holderfind=exclude
                holder.append(holderfind)
        all.append(holder)
    return all
data_multi = get_multi_data(multi_output)

# get strand data
def get_strands(strand_codes):
  finds=[]
  for var in range(len(strand_codes)):
    for section in range(len(data["References"])):
        if "Codes" in data["References"][section]:
            if "Outcomes" in data["References"][section]:
                if "OutcomeCodes" in data["References"][section]["Outcomes"][0]:
                    for study in range(len(data["References"][section]["Outcomes"][0]["OutcomeCodes"]["OutcomeItemAttributesList"])):
                        for key,value in strand_codes[var].items():
                                if key == data["References"][section]["Outcomes"][0]["OutcomeCodes"]["OutcomeItemAttributesList"][study]["AttributeId"]:
                                    strandfind=value
                    finds.append(strandfind)
                else:
                    finds.append(exclude)
            else:
                finds.append(exclude)
        else:
            finds.append(exclude)
  return finds
strand_data = get_strands(strand_output) 

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
def get_basic_info():
    global itemids, titles, year
    itemids, titles, year = [], [], []
    for section in range(len(data["References"])):
        if "ItemId" in data["References"][section]:
            itemids.append(data["References"][section]["ItemId"])
        else:
            itemids.append(exclude)
        if "ShortTitle" in data["References"][section]:
            titles.append(data["References"][section]["ShortTitle"])
        else:
            titles.append(exclude)
        if "Year" in data["References"][section]:
            year.append(int(data["References"][section]["Year"]))
        else:
            year.append(exclude)
get_basic_info()

# get stats info from 'Outcomes' section
def get_stats():
    global outcometext, interventiontext, SMD, SESMD, CIupperSMD, CIlowerSMD
    outcometext=[]
    interventiontext=[]
    SMD=[]
    SESMD=[]
    CIupperSMD=[]
    CIlowerSMD=[]
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

# dataframe that includes user comments (additional text etc.) 
data_frame_standard = pd.DataFrame(list(zip(itemids, titles, year, strand_data,
                                            outcometext, 
                                            data_single[3], data_single[6], data_single[0], data_single[1],
                                            data_single[8], data_single[4], data_single[2], data_single[6],
                                            data_multi[1], data_multi[0], data_single[7], data_single[9],
                                            data_single[10], data_single[11], interventiontext,
                                            data_single[12], data_single[13],
                                            data_multi[2], data_multi[3], data_multi[4], data_multi[5],
                                            SMD, SESMD, CIupperSMD, CIlowerSMD,
                                            codes_check, outcomes_check, outcomecodes_check)), 
                                    columns=['ItemID', 'Author', 'Year', 'Strand',
                                             'Outcome',  
                                            'StudentGender', 'Country', 'LevelofAssignment', 'ParticipantAssignment', 
                                            'StudyDesign', 'PublicationType', 'StudyRealism', 'EducationalSetting', 
                                            'Attrition/DropoutReported', 'StudentAge', 'BaselineGroupDiff', 'Comparability',
                                            'ComparabilityVarReported', 'ComparabilityVariables', 'Intervention',
                                            'InterventionOrg', 'InterventionTrainingProvided',
                                            'InterventionFocus', 'InterventionTeachingApproach', 'InterventionTime', 'WhoDeliveredTeaching',
                                            'SMD', 'SESMD', 'CIupper', 'CIlower',
                                            'CodesSectionPresent', 'OutcomesSectionPresent', 'OutcomeCodesSectionPresent', 
                                            ])

# round statistical output to 4 decimal places
data_frame_standard["SMD"]     = data_frame_standard["SMD"].astype(float)
data_frame_standard["SESMD"]   = data_frame_standard["SESMD"].astype(float)
data_frame_standard["CIupper"] = data_frame_standard["CIupper"].astype(float)
data_frame_standard["CIlower"] = data_frame_standard["CIlower"].astype(float)

data_frame_standard["SMD"]     = data_frame_standard["SMD"].round(4)
data_frame_standard["SESMD"]   = data_frame_standard["SESMD"].round(4)
data_frame_standard["CIupper"] = data_frame_standard["CIupper"].round(4)
data_frame_standard["CIlower"] = data_frame_standard["CIlower"].round(4)

# save standard dataframe to .csv
data_frame_standard.to_csv("test.csv", index=False, na_rep="NA")

