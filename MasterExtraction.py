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

# extract user inputted comments for each var
def var_comments(codes):
    all_comments, comments= [], []
    for var in range(len(codes)):
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                user_comments = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            if "AdditionalText" in data["References"][section]["Codes"][study]:
                                user_comments = data["References"][section]["Codes"][study]["AdditionalText"]
                if not user_comments:
                    comments.append(exclude)
                else:
                    comments.append(user_comments)
            else:
                comments.append(exclude)
        all_comments.append(comments)
        comments=[]
    return all_comments

single_output_comments = var_comments(single_output)

# extract highlighted text for each var
def var_highlighted_text(codes):
    all_comments, highlighted_text = [], []
    for var in range(len(codes)):
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                user_highlighted_text = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            if "ItemAttributeFullTextDetails" in data["References"][section]["Codes"][study]:
                                if data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"]:
                                    for i in range(len(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"])):
                                        user_highlighted_text.append(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"][i]["Text"])
                if not user_highlighted_text:
                    highlighted_text.append(exclude)
                else:
                    highlighted_text.append(user_highlighted_text)
            else:
                highlighted_text.append(exclude)
        all_comments.append(highlighted_text)
        highlighted_text=[]
    return all_comments

single_output_highlighted_text = var_highlighted_text(single_output)

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
    global itemids, titles, year, abstract
    itemids, titles, year, abstract = [], [], [], []
    for section in range(len(data["References"])):
        if data["References"][section]["ItemId"]:
            itemids.append(data["References"][section]["ItemId"])
        else:
            itemids.append(exclude)
        if data["References"][section]["ShortTitle"]:
            titles.append(data["References"][section]["ShortTitle"])
        else:
            titles.append(exclude)
        if data["References"][section]["Year"]:
            year.append(int(data["References"][section]["Year"]))
        else:
            year.append(exclude)
        if data["References"][section]["Abstract"]:
            abstract.append(data["References"][section]["Abstract"])
        else:
            abstract.append(exclude)
get_basic_info()

# get stats info from 'Outcomes' section
def get_stats():
    global outcometext, interventiontext, SMD, SESMD, CIupperSMD, CIlowerSMD
    outcometext, interventiontext, SMD, SESMD, CIupperSMD, CIlowerSMD = [], [], [], [], [], []
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

# select data with which to make dataframe
def low_FSM_verbose():
    df = pd.DataFrame({'StudyID': itemids, 'Strand': strand_data, 
                       'lowSESFSMstudents': single_output_comments[-4], 'lowSESFSMstudentsHighlightedText': single_output_highlighted_text[-4],
                       'lowSESFSM%': single_output_comments[-3], 'lowSESFSM%HighlightedText': single_output_highlighted_text[-3],
                       'lowSESFSMfurtherinfo': single_output_comments[-2], 'lowSESFSMfurtherinfoHighlightedText': single_output_highlighted_text[-2],
                       'NoSESFSMinformation': single_output_comments[-1], 'NoSESFSMinformationHighlightedText': single_output_highlighted_text[-1]})
    # remove toolkit label from strand
    df['Strand'] = df['Strand'].str.replace('Toolkit: ', '')
    # remove escape sequences from strings
    df.replace('\r',' ', regex=True, inplace=True)
    df.replace('\n',' ', regex=True, inplace=True)
    # save dataframe to .csv
    df.to_csv("LowSESFSM_verbose.csv", index=False)

# select data with which to make dataframe
def number_of_classes_verbose():
    df = pd.DataFrame({'StudyID': itemids, 'Strand': strand_data, 
                       'NumberofClasses':  single_output_comments[-10], 'NumberofClassesHighlightedText': single_output_highlighted_text[-10],
                       'TotalNumberofClasses': single_output_comments[-7], 'TotalNumberofClassesHighlightedText': single_output_highlighted_text[-7]})
    # remove toolkit label from strand
    df['Strand'] = df['Strand'].str.replace('Toolkit: ', '')
    # remove escape sequences from strings
    df.replace('\r',' ', regex=True, inplace=True)
    df.replace('\n',' ', regex=True, inplace=True)
    # save dataframe to .csv
    df.to_csv("NumberofClasses.csv", index=False)

def test_type_verbose():
    df = pd.DataFrame({'StudyID': itemids, 'Strand': strand_data, 
                       'TypeofTest': single_output_comments[-6], 'TypeofTestHighlightedText': single_output_highlighted_text[-6],
                       'StandardisedTest': single_output_comments[-5], 'StandardisedTestHighlightedText': single_output_highlighted_text[-5],
                       'ResearcherDevelopedTest': single_output_comments[-4], 'ResearcherDevelopedTestHighlightedTest': single_output_highlighted_text[-4],
                       'SchoolDevelopedTest': single_output_comments[-3], 'SchoolDevelopedTestHighlightedTest': single_output_highlighted_text[-3],
                       'NationalTestorExam': single_output_comments[-2], 'NationalTestorExamHighlightedTest': single_output_highlighted_text[-2],
                       'InternationalTests': single_output_comments[-1], 'InternationalTestsHighlightedTest': single_output_highlighted_text[-1]})
    # remove toolkit label from strand
    df['Strand'] = df['Strand'].str.replace('Toolkit: ', '')
    # remove escape sequences from strings
    df.replace('\r',' ', regex=True, inplace=True)
    df.replace('\n',' ', regex=True, inplace=True)
    # save dataframe to .csv
    df.to_csv("TestType_verbose.csv", index=False)


def curriculum_subj_verbose():
    df = pd.DataFrame({'StudyID': itemids, 'Strand': strand_data, 
                    'CurriculumSubjectsTested': data_multi[-1],
                    'CurriculumSubjectsTestedComments': single_output_comments[-1],
                    'CurriculumSubjectsTestedCommentsHT': single_output_highlighted_text[-1]})

    df['Strand'] = df['Strand'].str.replace('Toolkit: ', '')

    df.replace('\r',' ', regex=True, inplace=True)
    df.replace('\n',' ', regex=True, inplace=True)

    df.to_csv("CurriculumSubjectsTested_verbose.csv", index=False)

curriculum_subj_verbose()


""" # convert all numerical data to float [verbose extraction]
data_frame_verbose["SMD"]     = data_frame_verbose["SMD"].astype(float)
data_frame_verbose["SESMD"]   = data_frame_verbose["SESMD"].astype(float)
data_frame_verbose["CIupper"] = data_frame_verbose["CIupper"].astype(float)
data_frame_verbose["CIlower"] = data_frame_verbose["CIlower"].astype(float)

# round statistical output to 4 decimal places [verbose extraction]
data_frame_verbose["SMD"]     = data_frame_verbose["SMD"].round(4)
data_frame_verbose["SESMD"]   = data_frame_verbose["SESMD"].round(4)
data_frame_verbose["CIupper"] = data_frame_verbose["CIupper"].round(4)
data_frame_verbose["CIlower"] = data_frame_verbose["CIlower"].round(4)

# convert all numerical data to float [standard extraction]
data_frame_standard["SMD"]     = data_frame_standard["SMD"].astype(float)
data_frame_standard["SESMD"]   = data_frame_standard["SESMD"].astype(float)
data_frame_standard["CIupper"] = data_frame_standard["CIupper"].astype(float)
data_frame_standard["CIlower"] = data_frame_standard["CIlower"].astype(float)

# round statistical output to 4 decimal places [standard extraction]
data_frame_standard["SMD"]     = data_frame_standard["SMD"].round(4)
data_frame_standard["SESMD"]   = data_frame_standard["SESMD"].round(4)
data_frame_standard["CIupper"] = data_frame_standard["CIupper"].round(4)
data_frame_standard["CIlower"] = data_frame_standard["CIlower"].round(4) """