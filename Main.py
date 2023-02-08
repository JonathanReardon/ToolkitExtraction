#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Jonathan Reardon
"""

import os
import sys
import json

data_file = sys.argv[1]

#/****************/
#/ CORE FUNCTIONS /
#/****************/

EXCLUDE = "NA"

def load_json():
    global data
    script_dir = os.path.dirname(__file__)
    datafile = os.path.join(script_dir, data_file)

    with open(datafile) as f:
        data = json.load(f)

def get_metadata(var):
    ''' """ 
    Extracts study-level metadata. """
    Params: Variable name e.g. "Year", "ShortTitle".
    Returns: A list of extracted data. One datapoint per study.
    '''
    varlist = []
    for section in range(len(data["References"])):
        if data["References"][section][var]:
            varlist.append(data["References"][section][var])
        else:
            varlist.append(EXCLUDE)
    return varlist

""" def get_data(codes):
    '''
    Extract study-level main data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. One or more datapoints per study.
    '''
    df = []
    for var in range(len(codes)):
        holder = []
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind) == 0:
                    holderfind = EXCLUDE
                holder.append(holderfind)
        df.append(holder)
    return df """

def comments(codes):
    ''' 
    Extracts study level "comment" data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. One or more datapoints per study.
    '''
    all_comments, comments = [], []
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
                    comments.append(EXCLUDE)
                else:
                    comments.append(user_comments)
            else:
                comments.append(EXCLUDE)
        all_comments.append(comments)
        comments = []
    return all_comments

def highlighted_text(codes):
    ''' 
    Extracts Study level "highlighted text" data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. One or more datapoints per study.
    '''
    all_highlighted_text, highlighted_text = [], []
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
                                        user_highlighted_text.append(
                                            data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"][i]["Text"])
                if not user_highlighted_text:
                    highlighted_text.append(EXCLUDE)
                else:
                    highlighted_text.append(user_highlighted_text)
            else:
                highlighted_text.append(EXCLUDE)
        all_highlighted_text.append(highlighted_text)
        highlighted_text = []
    return all_highlighted_text

def get_outcome_lvl1(var):
    ''' 
    Extracts first-level outcome data.
    Params: Variable name (str) e.g. "SMD", "OutcomeID".
    Returns: A list of extracted data. One datapoint per outcome, 
    multiple possible outcomes per study.
    '''
    outcome_number=[]
    for study in range(len(data["References"])):
        if "Outcomes" in data["References"][study]:
            outcome_number.append(len(data["References"][study]["Outcomes"]))
    varlist = []
    for section in range(len(data["References"])):
        holder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(max(outcome_number)):
                if subsection < len(data["References"][section]["Outcomes"]):
                    holder.append(data["References"][section]["Outcomes"][subsection][var])
                else:
                    holder.append(EXCLUDE)
            varlist.append(holder)
        else:
            for i in range(max(outcome_number)):
                holder.append(EXCLUDE)
            varlist.append(holder)
    return varlist

def get_outcome_lvl2(var):
    '''
    Extracts second-level (nested) outcome data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. Multiple possible datapoints per outcome,
    multiple possible outcomes per study.  
    '''
    varlist = []
    for variable in range(len(var)):
        for study in range(len(data["References"])):
            if "Codes" in data["References"][study]:
                if "Outcomes" in data["References"][study]:
                    outerholder = []
                    for item in range(len(data["References"][study]["Outcomes"])):
                        innerholderholder = []
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
                            for subsection in range(len(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"])):
                                for key, value in var[variable].items():
                                    if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                        innerholderholder.append(
                                            data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])
                        else:
                            innerholderholder = EXCLUDE
                        if len(innerholderholder) == 0:
                            innerholderholder = EXCLUDE
                        outerholder.append(innerholderholder)
                else:
                    outerholder = EXCLUDE
            varlist.append(outerholder)
    return varlist

# CEDIL Project

def get_data(codes):
    '''
    Extract study-level main data.
    Params: List/dict [{..}] of one or more AttributeID's and Attribute labels.
    Returns: A list of extracted data. One or more datapoints per study.
    '''
    df = []
    for var in range(len(codes)):
        holder = []
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind = []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind) == 0:
                    holderfind = EXCLUDE
                holder.append(holderfind)
        df.append(holder)
    return df


#/*********************/
#/ SECONDARY FUNCTIONS /
#/*********************/

def getOutcomeData(dataframe, out_label, out_container, var_names):
    '''
    Extract strand level outcome data for main analysis dataframe
    '''
    from Toolkit_Outcome_Check import outcome_num
    for counter, row in enumerate(dataframe['out_type_1']):
            found = False
            for outcome_n in range(1, outcome_num + 1):
                if out_label in dataframe[f'out_type_{outcome_n}'][counter]:
                    found = True
                    for counter2, holder in enumerate(out_container):
                        holder.append(dataframe[var_names[counter2] + f"{outcome_n}"][counter])
                    break
            if not found:
                for holder in out_container:
                    holder.append("NA")

def save_dataframe(df, df_name):
    '''
    Saves a .csv of the dataframe to Extractions/
    '''
    # get current working dir
    cw = os.getcwd() + "/Extractions"
    # get file name for output
    outfile_name_pre = data_file.rsplit('/')[-1] # 
    outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
    outfile_name = outfile_name_mid + df_name
    outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)
    # create dir (filename)
    try:
        os.mkdir("Extractions/" + outfile_name_mid)
    except OSError:
        pass
    else:
        print("Successfully created {} directory".format("Extractions/" + outfile_name_mid))
    # write to disk
    print("Input file: {}\n".format(data_file))
    print("Saving extracted output to: {}\n".format(outfile))
    df.to_csv(outfile, index=False)

def verbose_display(df):
    '''
    Displays further info
    '''
    # print dataframe
    print(df)
    print("\n")
    # list column names and position
    for counter, i in enumerate(df):
        print(counter, i)
    print("\n")
    # print dataframe info
    print("Columns: {}".format(df.shape[1]))
    print("Rows: {}".format(df.shape[0]))
    print("Datapoints: {}".format(df.shape[0] * df.shape[1]))
    print("\n")

def clean_up(df):
    '''
    Replaces problematic character with empty space
    '''
    df.replace('\r', ' ', regex=True, inplace=True)
    df.replace('\n', ' ', regex=True, inplace=True)
    df.replace(':', ' ',  regex=True, inplace=True)
    df.replace(';', ' ',  regex=True, inplace=True)