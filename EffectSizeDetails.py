import json
from collections import Counter
from pprint import pprint
import pandas as pd
import numpy as np
import os

from questions import *

# input data file name (.csv) with full path
""" datafile = '/home/jon/json/ToolkitExtraction/Data/May12th_2020.json' """

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, "May12th_2020.json")

# import dataset (uncomment to select dataset of choice)
with open(datafile) as f:
    data=json.load(f)

# for missing or unavailable data
exclude="NA"

# data admin strand data (possible multiple outputs)
def get_admin_strand(admin_strand_codes):
    global admin_strand
    admin_strand=[]
    for var in range(len(admin_strand_codes)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in admin_strand_codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind)==0:
                    holderfind=exclude
                holder.append(holderfind)
        admin_strand.append(holder)

# get effect size type data from Outcomes
def get_estype(estype_codes):
    global estype
    estype = [] 
    for var in range(len(estype_codes)):
        for study in range(len(data["References"])):
            if "Codes" in data["References"][study]:
                outerholder = []
                if "Outcomes" in data["References"][study]:
                    for item in range(len(data["References"][study]["Outcomes"])):
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
                            innerholderholder = []
                            for subsection in range(12):
                                if subsection < len(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"]):
                                    for key,value in estype_codes[var].items():
                                        if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                            innerholderholder.append(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])
                                else:
                                    pass
                        else:
                            innerholderholder.append(exclude)
                        outerholder.append(innerholderholder)
                else:
                    pass
            estype.append(outerholder)

# get test type data from Outcomes
def get_testtype(testtype_codes):
    global testtype
    testtype = [] 
    for var in range(len(testtype_codes)):
        for study in range(len(data["References"])):
            if "Codes" in data["References"][study]:
                outerholder = []
                if "Outcomes" in data["References"][study]:
                    for item in range(len(data["References"][study]["Outcomes"])):
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
                            innerholderholder = []
                            for subsection in range(12):
                                if subsection < len(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"]):
                                    for key,value in testtype_codes[var].items():
                                        if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                            innerholderholder.append(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])
                                else:
                                    pass
                        else:
                            innerholderholder.append(exclude)
                        outerholder.append(innerholderholder)
                else:
                    pass
            testtype.append(outerholder)

# get toolkit strand data from Outcomes
def get_strands(strand_codes):
    global strand
    strand = [] 
    for var in range(len(strand_codes)):
        # for study in range(len(data["References"])):
        for study in range(len(data["References"])):
            if "Codes" in data["References"][study]:
                outerholder = []
                if "Outcomes" in data["References"][study]:
                    for item in range(len(data["References"][study]["Outcomes"])):
                        if "OutcomeCodes" in data["References"][study]["Outcomes"][item]:
                            innerholderholder = []
                            for subsection in range(12):
                                if subsection < len(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"]):
                                    for key,value in strand_codes[var].items():
                                        if key == data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeId"]:
                                            innerholderholder.append(data["References"][study]["Outcomes"][item]["OutcomeCodes"]["OutcomeItemAttributesList"][subsection]["AttributeName"])
                                else:
                                    pass
                        else:
                            innerholderholder.append(exclude)
                        outerholder.append(innerholderholder)
            strand.append(outerholder)

# get SMD info from 'Outcomes' section for all studies and outcomes
def get_SMD():
    global SMD
    SMD = []
    for section in range(len(data["References"])):
        smdholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    smdholder.append(data["References"][section]["Outcomes"][subsection]["SMD"])
                else:
                    smdholder.append(exclude)
            SMD.append(smdholder)
        else:
            for i in range(10):
                smdholder.append(exclude)
            SMD.append(smdholder)

# get Title info from 'Outcomes' section for all studies and outcomes
def get_title():
    global title
    title = []
    for section in range(len(data["References"])):
        titleholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    titleholder.append(data["References"][section]["Outcomes"][subsection]["Title"])
                else:
                    titleholder.append(exclude)
            title.append(titleholder)
        else:
            for i in range(10):
                titleholder.append(exclude)
            title.append(titleholder)

# get SESMD info from 'Outcomes' section for all studies and outcomes
def get_SESMD():
    global SESMD
    SESMD = []
    for section in range(len(data["References"])):
        sesmdholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    sesmdholder.append(data["References"][section]["Outcomes"][subsection]["SESMD"])
                else:
                    sesmdholder.append(exclude)
            SESMD.append(sesmdholder)
        else:
            for i in range(10):
                sesmdholder.append(exclude)
            SESMD.append(sesmdholder)

# get CIupperSMD info from 'Outcomes' section for all studies and outcomes
def get_CIupperSMD():
    global CIupperSMD
    CIupperSMD = []
    for section in range(len(data["References"])):
        ciupperholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    ciupperholder.append(data["References"][section]["Outcomes"][subsection]["CIUpperSMD"])
                else:
                    ciupperholder.append(exclude)
            CIupperSMD.append(ciupperholder)
        else:
            for i in range(10):
                ciupperholder.append(exclude)
            CIupperSMD.append(ciupperholder)

# get CIlowerSMD info from 'Outcomes' section for all studies and outcomes
def get_CIlowerSMD():
    global CIlowerSMD
    CIlowerSMD = []
    for section in range(len(data["References"])):
        cilowerholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    cilowerholder.append(data["References"][section]["Outcomes"][subsection]["CILowerSMD"])
                else:
                    cilowerholder.append(exclude)
            CIlowerSMD.append(cilowerholder)
        else:
            for i in range(10):
                cilowerholder.append(exclude)
            CIlowerSMD.append(cilowerholder)

# get InterventionText info from 'Outcomes' section for all studies and outcomes
def get_InterventionText():
    global InterventionText
    InterventionText = []
    for section in range(len(data["References"])):
        interventiontextholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    interventiontextholder.append(data["References"][section]["Outcomes"][subsection]["InterventionText"])
                else:
                    interventiontextholder.append(exclude)
            InterventionText.append(interventiontextholder)
        else:
            for i in range(10):
                interventiontextholder.append(exclude)
            InterventionText.append(interventiontextholder)

# get get_ControlText info from 'Outcomes' section for all studies and outcomes
def get_ControlText():
    global ControlText
    ControlText = []
    for section in range(len(data["References"])):
        controltextholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    controltextholder.append(data["References"][section]["Outcomes"][subsection]["ControlText"])
                else:
                    controltextholder.append(exclude)
            ControlText.append(controltextholder)
        else:
            for i in range(10):
                controltextholder.append(exclude)
            ControlText.append(controltextholder)

# get Outcome (primary/secondary) info from 'Outcomes' section for all studies and outcomes
def get_Outcome():
    global Outcome
    Outcome = []
    for section in range(len(data["References"])):
        outcomeholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcomeholder.append(data["References"][section]["Outcomes"][subsection]["OutcomeText"])
                else:
                    outcomeholder.append(exclude)
            Outcome.append(outcomeholder)
        else:
            for i in range(10):
                outcomeholder.append(exclude)
            Outcome.append(outcomeholder)

# get OutcomeID info from 'Outcomes' section for all studies and outcomes
def get_OutcomeID():
    global OutcomeID
    OutcomeID = []
    for section in range(len(data["References"])):
        outcomeidholder = []
        if "Outcomes" in data["References"][section]:
            for subsection in range(10):
                if subsection < len(data["References"][section]["Outcomes"]):
                    outcomeidholder.append(data["References"][section]["Outcomes"][subsection]["OutcomeId"])
                else:
                    outcomeidholder.append(exclude)
            OutcomeID.append(outcomeidholder)
        else:
            for i in range(10):
                outcomeidholder.append(exclude)
            OutcomeID.append(outcomeidholder)

def get_basic_info():
    global author, itemids
    author, itemids = [], []
    for section in range(len(data["References"])):
        if data["References"][section]["ShortTitle"]:
            author.append(data["References"][section]["ShortTitle"])
        else:
            author.append(exclude)
        if data["References"][section]["ItemId"]:
            itemids.append(data["References"][section]["ItemId"])
        else:
            itemids.append(exclude)

def make_dataframe():
    global df
    # make admin strand data frame
    admin_strand_df = pd.DataFrame(admin_strand)
    admin_strand_df = admin_strand_df.T
    # make effect size type dataframe
    estype_df       = pd.DataFrame(estype)
    estype_df       = estype_df.iloc[:, :-2]
    # make strand dataframe
    strand_df       = pd.DataFrame(strand)
    strand_df       = strand_df.iloc[:, :-2] # look into why this produced 12 columns (though it works)
    # make test type dataframe
    testtype_df     = pd.DataFrame(testtype)
    testtype_df     = testtype_df.iloc[:, :-2]
    # make other dataframes
    title_df        = pd.DataFrame(title)
    smd_df          = pd.DataFrame(SMD)
    sesmd_df        = pd.DataFrame(SESMD)
    author_df       = pd.DataFrame(author)
    itemids_df      = pd.DataFrame(itemids)
    ciupper_df      = pd.DataFrame(CIupperSMD)
    cilower_df      = pd.DataFrame(CIlowerSMD)
    outcome_df      = pd.DataFrame(Outcome)
    outcomeid_df    = pd.DataFrame(OutcomeID)
    intervtext_df   = pd.DataFrame(InterventionText)
    controltext_df  = pd.DataFrame(ControlText)

    df = pd.concat([itemids_df, admin_strand_df, author_df, title_df, testtype_df, estype_df, strand_df, smd_df, sesmd_df, ciupper_df, 
                    cilower_df, outcome_df, outcomeid_df, intervtext_df, controltext_df], axis=1, sort=False)

    df.columns = ['StudyID', 'Admin_Strand', 'Author',
                 'OutcomeLabel_1',  'OutcomeLabel_2', 'OutcomeLabel_3', 'OutcomeLabel_4', 'OutcomeLabel_5', 
                 'OutcomeLabel_6', 'OutcomeLabel_7', 'OutcomeLabel_8', 'OutcomeLabel_9', 'OutcomeLabel_10',
                 'EffectSizeType_Outcome_1', 'EffectSizeType_Outcome_2', 'EffectSizeType_Outcome_3', 'EffectSizeType_Outcome_4', 'EffectSizeType_Outcome_5', 
                 'EffectSizeType_Outcome_6', 'EffectSizeType_Outcome_7', 'EffectSizeType_Outcome_8', 'EffectSizeType_Outcome_9', 'EffectSizeType_Outcome_10', 
                 'TestType_Outcome_1', 'TestType_Outcome_2','TestType_Outcome_3','TestType_Outcome_4','TestType_Outcome_5',
                 'TestType_Outcome_6','TestType_Outcome_7','TestType_Outcome_8','TestType_Outcome_9','TestType_Outcome_10',
                 'ToolkitStrand_Outcome_1', 'ToolkitStrand_Outcome_2', 'ToolkitStrand_Outcome_3', 'ToolkitStrand_Outcome_4', 'ToolkitStrand_Outcome_5', 
                 'ToolkitStrand_Outcome_6', 'ToolkitStrand_Outcome_7', 'ToolkitStrand_Outcome_8', 'ToolkitStrand_Outcome_9', 'ToolkitStrand_Outcome_10', 
                 'SMD_1', 'SMD_2', 'SMD_3', 'SMD_4', 'SMD_5', 'SMD_6', 'SMD_7', 'SMD_8', 'SMD_9', 'SMD_10',
                 'SESMD_1', 'SESMD_2', 'SESMD_3', 'SESMD_4', 'SESMD_5', 'SESMD_6', 'SESMD_7', 'SESMD_8', 'SESMD_9', 'SESMD_10',
                 'CIupperSMD_1', 'CIupperSMD_2', 'CIupperSMD_3', 'CIupperSMD_4', 'CIupperSMD_5', 'CIupperSMD_6', 'CIupperSMD_7', 'CIupperSMD_8', 'CIupperSMD_9', 'CIupperSMD_10',
                 'CIlowerSMD_1', 'CIlowerSMD_2', 'CIlowerSMD_3', 'CIlowerSMD_4', 'CIlowerSMD_5', 'CIlowerSMD_6', 'CIlowerSMD_7', 'CIlowerSMD_8', 'CIlowerSMD_9', 'CIlowerSMD_10',
                 'Outcome_1', 'Outcome_2', 'Outcome_3', 'Outcome_4', 'Outcome_5', 'Outcome_6', 'Outcome_7', 'Outcome_8', 'Outcome_9', 'Outcome_10',
                 'OutcomeID_1', 'OutcomeID_2', 'OutcomeID_3', 'OutcomeID_4', 'OutcomeID_5', 'OutcomeID_6', 'OutcomeID_7', 'OutcomeID_8', 'OutcomeID_9', 'OutcomeID_10',
                 'InterventionText_1', 'InterventionText_2', 'InterventionText_3', 'InterventionText_4', 'InterventionText_5', 'InterventionText_6', 'InterventionText_7', 'InterventionText_8', 'InterventionText_9', 'InterventionText_10',
                 'ControlText_1', 'ControlText_2', 'ControlText_3', 'ControlText_4', 'ControlText_5', 'ControlText_6', 'ControlText_7', 'ControlText_8', 'ControlText_9', 'ControlText_10'] 

    df = df[['StudyID', 'Admin_Strand', 'Author', 
            'OutcomeID_1', 'OutcomeLabel_1', 'TestType_Outcome_1', 'EffectSizeType_Outcome_1', 'ToolkitStrand_Outcome_1',  'InterventionText_1', 'ControlText_1', 'Outcome_1', 'SMD_1', 'SESMD_1', 'CIupperSMD_1', 'CIlowerSMD_1', 
            'OutcomeID_2', 'OutcomeLabel_2', 'TestType_Outcome_2', 'EffectSizeType_Outcome_2', 'ToolkitStrand_Outcome_2',  'InterventionText_2', 'ControlText_2', 'Outcome_2', 'SMD_2', 'SESMD_2', 'CIupperSMD_2', 'CIlowerSMD_2', 
            'OutcomeID_3', 'OutcomeLabel_3', 'TestType_Outcome_3', 'EffectSizeType_Outcome_3', 'ToolkitStrand_Outcome_3',  'InterventionText_3', 'ControlText_3', 'Outcome_3', 'SMD_3', 'SESMD_3', 'CIupperSMD_3', 'CIlowerSMD_3', 
            'OutcomeID_4', 'OutcomeLabel_4', 'TestType_Outcome_4', 'EffectSizeType_Outcome_4', 'ToolkitStrand_Outcome_4',  'InterventionText_4', 'ControlText_4', 'Outcome_4', 'SMD_4', 'SESMD_4', 'CIupperSMD_4', 'CIlowerSMD_4', 
            'OutcomeID_5', 'OutcomeLabel_5', 'TestType_Outcome_5', 'EffectSizeType_Outcome_5', 'ToolkitStrand_Outcome_5',  'InterventionText_5', 'ControlText_5', 'Outcome_5', 'SMD_5', 'SESMD_5', 'CIupperSMD_5', 'CIlowerSMD_5', 
            'OutcomeID_6', 'OutcomeLabel_6', 'TestType_Outcome_6', 'EffectSizeType_Outcome_6', 'ToolkitStrand_Outcome_6',  'InterventionText_6', 'ControlText_6', 'Outcome_6', 'SMD_6', 'SESMD_6', 'CIupperSMD_6', 'CIlowerSMD_6', 
            'OutcomeID_7', 'OutcomeLabel_7', 'TestType_Outcome_7', 'EffectSizeType_Outcome_7', 'ToolkitStrand_Outcome_7',  'InterventionText_7', 'ControlText_7', 'Outcome_7', 'SMD_7', 'SESMD_7', 'CIupperSMD_7', 'CIlowerSMD_7', 
            'OutcomeID_8', 'OutcomeLabel_8', 'TestType_Outcome_8', 'EffectSizeType_Outcome_8', 'ToolkitStrand_Outcome_8',  'InterventionText_8', 'ControlText_8', 'Outcome_8', 'SMD_8', 'SESMD_8', 'CIupperSMD_8', 'CIlowerSMD_8', 
            'OutcomeID_9', 'OutcomeLabel_9', 'TestType_Outcome_9', 'EffectSizeType_Outcome_9', 'ToolkitStrand_Outcome_9',  'InterventionText_9', 'ControlText_9', 'Outcome_9', 'SMD_9', 'SESMD_9', 'CIupperSMD_9', 'CIlowerSMD_9', 
            'OutcomeID_10', 'OutcomeLabel_10', 'TestType_Outcome_10', 'EffectSizeType_Outcome_10', 'ToolkitStrand_Outcome_10',  'InterventionText_10', 'ControlText_10', 'Outcome_10', 'SMD_10', 'SESMD_10', 'CIupperSMD_10', 'CIlowerSMD_10']]

    df = df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)
    df.replace('NaN','NA', regex=True, inplace=True)
    df.replace('','NA', regex=True, inplace=True)


def move_primary():
    # column data to swap (by row)
    effectsizetype_col = ['EffectSizeType_Outcome_1', 'EffectSizeType_Outcome_2', 'EffectSizeType_Outcome_3', 'EffectSizeType_Outcome_4',
                          'EffectSizeType_Outcome_5', 'EffectSizeType_Outcome_6', 'EffectSizeType_Outcome_7', 'EffectSizeType_Outcome_8',
                          'EffectSizeType_Outcome_9', 'EffectSizeType_Outcome_10']
    testtype_col       = ['TestType_Outcome_1', 'TestType_Outcome_2', 'TestType_Outcome_3', 'TestType_Outcome_4', 'TestType_Outcome_5', 
                          'TestType_Outcome_6', 'TestType_Outcome_7', 'TestType_Outcome_8', 'TestType_Outcome_9', 'TestType_Outcome_10']
    title_col          = ['OutcomeLabel_1', 'OutcomeLabel_2', 'OutcomeLabel_3', 'OutcomeLabel_4', 'OutcomeLabel_5', 
                         'OutcomeLabel_6', 'OutcomeLabel_7', 'OutcomeLabel_8', 'OutcomeLabel_9', 'OutcomeLabel_10']
    toolkitstrand_col = ['ToolkitStrand_Outcome_1', 'ToolkitStrand_Outcome_2', 'ToolkitStrand_Outcome_3', 
                         'ToolkitStrand_Outcome_4', 'ToolkitStrand_Outcome_5', 'ToolkitStrand_Outcome_6', 
                         'ToolkitStrand_Outcome_7', 'ToolkitStrand_Outcome_8', 'ToolkitStrand_Outcome_9', 
                         'ToolkitStrand_Outcome_10']
    smd_col           = ['SMD_2', 'SMD_3', 'SMD_4', 'SMD_5', 'SMD_6', 'SMD_7', 'SMD_7', 'SMD_9', 'SMD_10']
    sesmd_col         = ['SESMD_2', 'SESMD_3', 'SESMD_4', 'SESMD_5', 'SESMD_6', 'SESMD_7', 'SESMD_8', 'SESMD_9', 'SESMD_10']
    cilower_col       = ['CIlowerSMD_2', 'CIlowerSMD_3', 'CIlowerSMD_4', 'CIlowerSMD_5',
                         'CIlowerSMD_6', 'CIlowerSMD_7', 'CIlowerSMD_8', 'CIlowerSMD_9', 'CIlowerSMD_10']
    ciupper_col       = ['CIupperSMD_2', 'CIupperSMD_3', 'CIupperSMD_4', 'CIupperSMD_5',
                         'CIupperSMD_6', 'CIupperSMD_7', 'CIupperSMD_8', 'CIupperSMD_9', 'CIupperSMD_10']
    outcome_col       = ['Outcome_2', 'Outcome_3', 'Outcome_4', 'Outcome_5',
                         'Outcome_6', 'Outcome_7', 'Outcome_8', 'Outcome_9', 'Outcome_10']
    outcomeid_col     = ['OutcomeID_1', 'OutcomeID_2', 'OutcomeID_3', 'OutcomeID_4', 'OutcomeID_5', 
                         'OutcomeID_6', 'OutcomeID_7', 'OutcomeID_8', 'OutcomeID_9', 'OutcomeID_10']
    itervtext_col     = ['InterventionText_1', 'InterventionText_2', 'InterventionText_3', 'InterventionText_4', 'InterventionText_5', 
                         'InterventionText_6', 'InterventionText_7', 'InterventionText_8', 'InterventionText_9', 'InterventionText_10']
    controltext_col   = ['ControlText_1', 'ControlText_2', 'ControlText_3', 'ControlText_4', 'ControlText_5', 
                         'ControlText_6', 'ControlText_7', 'ControlText_8', 'ControlText_9', 'ControlText_10']

    ######################
    # FIRST COLUMN CHECK 
    ######################

    # set rules for checking first column against others
    check_first    = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_2"] == 'Primary outcome'))
    check_second   = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_3"] == 'Primary outcome'))
    check_third    = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_4"] == 'Primary outcome'))
    check_fourth   = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_5"] == 'Primary outcome'))
    check_fifth    = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_6"] == 'Primary outcome'))
    check_sixth    = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_7"] == 'Primary outcome'))
    check_seventh  = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_8"] == 'Primary outcome'))
    check_eighth   = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_9"] == 'Primary outcome'))
    check_ninth    = ((df["Outcome_1"] != 'Primary outcome') & (df["Outcome_10"] == 'Primary outcome'))

    rules = [check_first, check_second, check_third, check_fourth, check_fifth,
             check_sixth, check_seventh, check_eighth, check_ninth]

    # check against first column
    for i in range(len(rules)):
        df.loc[rules[i],['EffectSizeType_Outcome_1', effectsizetype_col[i]]] = df.loc[rules[i],[effectsizetype_col[i], 'EffectSizeType_Outcome_1']].values
        df.loc[rules[i],['TestType_Outcome_1', testtype_col[i]]]             = df.loc[rules[i],[testtype_col[i], 'TestType_Outcome_1']].values
        df.loc[rules[i],['OutcomeLabel_1', title_col[i]]]                    = df.loc[rules[i],[title_col[i], 'OutcomeLabel_1']].values
        df.loc[rules[i],['ToolkitStrand_Outcome_1', toolkitstrand_col[i]]]   = df.loc[rules[i],[toolkitstrand_col[i], 'ToolkitStrand_Outcome_1']].values
        df.loc[rules[i],['Outcome_1', outcome_col[i]]]                       = df.loc[rules[i],[outcome_col[i], 'Outcome_1']].values
        df.loc[rules[i],['SMD_1', smd_col[i]]]                               = df.loc[rules[i],[smd_col[i], 'SMD_1']].values
        df.loc[rules[i],['SESMD_1', ciupper_col[i]]]                         = df.loc[rules[i],[sesmd_col[i], 'SESMD_1']].values
        df.loc[rules[i],['CIupperSMD_1', ciupper_col[i]]]                    = df.loc[rules[i],[ciupper_col[i], 'CIupperSMD_1']].values
        df.loc[rules[i],['CIlowerSMD_1', cilower_col[i]]]                    = df.loc[rules[i],[cilower_col[i], 'CIlowerSMD_1']].values
        df.loc[rules[i],['OutcomeID_1', outcomeid_col[i]]]                   = df.loc[rules[i],[outcomeid_col[i], 'OutcomeID_1']].values
        df.loc[rules[i],['InterventionText_1', itervtext_col[i]]]            = df.loc[rules[i],[itervtext_col[i], 'InterventionText_1']].values
        df.loc[rules[i],['ControlText_1', controltext_col[i]]]               = df.loc[rules[i],[controltext_col[i], 'ControlText_1']].values
 
    ######################
    # SECOND COLUMN CHECK 
    ######################

    # set rules for checking second column against others
    check_first    = ((df["Outcome_2"] != 'Primary outcome') & (df["Outcome_3"] == 'Primary outcome'))
    check_second   = ((df["Outcome_2"] != 'Primary outcome') & (df["Outcome_4"] == 'Primary outcome'))
    check_third    = ((df["Outcome_2"] != 'Primary outcome') & (df["Outcome_5"] == 'Primary outcome'))
    check_fourth   = ((df["Outcome_2"] != 'Primary outcome') & (df["Outcome_6"] == 'Primary outcome'))
    check_fifth    = ((df["Outcome_2"] != 'Primary outcome') & (df["Outcome_7"] == 'Primary outcome'))
    check_sixth    = ((df["Outcome_2"] != 'Primary outcome') & (df["Outcome_8"] == 'Primary outcome'))
    check_seventh  = ((df["Outcome_2"] != 'Primary outcome') & (df["Outcome_9"] == 'Primary outcome'))
    check_eighth   = ((df["Outcome_2"] != 'Primary outcome') & (df["Outcome_10"] == 'Primary outcome'))

    rules = [check_first, check_second, check_third, check_fourth, check_fifth,
                 check_sixth, check_seventh, check_eighth]

    effectsizetype_col.pop(0)
    testtype_col.pop(0)
    title_col.pop(0)
    toolkitstrand_col.pop(0)
    outcome_col.pop(0)
    smd_col.pop(0)
    sesmd_col.pop(0)
    cilower_col.pop(0)
    ciupper_col.pop(0)
    itervtext_col.pop(0)
    controltext_col.pop(0)

    # check against second column
    for i in range(len(rules)):
        df.loc[rules[i],['EffectSizeType_Outcome_2', effectsizetype_col[i]]] = df.loc[rules[i],[effectsizetype_col[i], 'EffectSizeType_Outcome_2']].values
        df.loc[rules[i],['TestType_Outcome_2', testtype_col[i]]]             = df.loc[rules[i],[testtype_col[i], 'TestType_Outcome_2']].values
        df.loc[rules[i],['OutcomeLabel_2', title_col[i]]]                    = df.loc[rules[i],[title_col[i], 'OutcomeLabel_2']].values
        df.loc[rules[i],['ToolkitStrand_Outcome_2', toolkitstrand_col[i]]]   = df.loc[rules[i],[toolkitstrand_col[i], 'ToolkitStrand_Outcome_2']].values
        df.loc[rules[i],['Outcome_2', outcome_col[i]]]                       = df.loc[rules[i],[outcome_col[i], 'Outcome_2']].values
        df.loc[rules[i],['SMD_2', smd_col[i]]]                               = df.loc[rules[i],[smd_col[i], 'SMD_2']].values
        df.loc[rules[i],['SESMD_2', ciupper_col[i]]]                         = df.loc[rules[i],[sesmd_col[i], 'SESMD_2']].values
        df.loc[rules[i],['CIupperSMD_2', ciupper_col[i]]]                    = df.loc[rules[i],[ciupper_col[i], 'CIupperSMD_2']].values
        df.loc[rules[i],['CIlowerSMD_2', cilower_col[i]]]                    = df.loc[rules[i],[cilower_col[i], 'CIlowerSMD_2']].values
        df.loc[rules[i],['OutcomeID_2', outcomeid_col[i]]]                   = df.loc[rules[i],[outcomeid_col[i], 'OutcomeID_2']].values
        df.loc[rules[i],['InterventionText_2', itervtext_col[i]]]            = df.loc[rules[i],[itervtext_col[i], 'InterventionText_2']].values
        df.loc[rules[i],['ControlText_2', controltext_col[i]]]               = df.loc[rules[i],[controltext_col[i], 'ControlText_2']].values

    ######################
    # THIRD COLUMN CHECK 
    ######################

    # set rules for checking second column against others
    check_first    = ((df["Outcome_3"] != 'Primary outcome') & (df["Outcome_4"] == 'Primary outcome'))
    check_second   = ((df["Outcome_3"] != 'Primary outcome') & (df["Outcome_5"] == 'Primary outcome'))
    check_third    = ((df["Outcome_3"] != 'Primary outcome') & (df["Outcome_6"] == 'Primary outcome'))
    check_fourth   = ((df["Outcome_3"] != 'Primary outcome') & (df["Outcome_7"] == 'Primary outcome'))
    check_fifth    = ((df["Outcome_3"] != 'Primary outcome') & (df["Outcome_8"] == 'Primary outcome'))
    check_sixth    = ((df["Outcome_3"] != 'Primary outcome') & (df["Outcome_9"] == 'Primary outcome'))
    check_seventh  = ((df["Outcome_3"] != 'Primary outcome') & (df["Outcome_10"] == 'Primary outcome'))

    rules = [check_first, check_second, check_third, check_fourth, check_fifth,
             check_sixth, check_seventh]

    effectsizetype_col.pop(0)
    testtype_col.pop(0)
    title_col.pop(0)
    toolkitstrand_col.pop(0)
    outcome_col.pop(0)
    smd_col.pop(0)
    sesmd_col.pop(0)
    cilower_col.pop(0)
    ciupper_col.pop(0)
    itervtext_col.pop(0)
    controltext_col.pop(0)

    # check against third column
    for i in range(len(rules)):
        df.loc[rules[i],['EffectSizeType_Outcome_3', effectsizetype_col[i]]] = df.loc[rules[i],[effectsizetype_col[i], 'EffectSizeType_Outcome_3']].values
        df.loc[rules[i],['TestType_Outcome_3', testtype_col[i]]]             = df.loc[rules[i],[testtype_col[i], 'TestType_Outcome_3']].values
        df.loc[rules[i],['OutcomeLabel_3', title_col[i]]]                    = df.loc[rules[i],[title_col[i], 'OutcomeLabel_3']].values
        df.loc[rules[i],['ToolkitStrand_Outcome_3', toolkitstrand_col[i]]]   = df.loc[rules[i],[toolkitstrand_col[i], 'ToolkitStrand_Outcome_3']].values
        df.loc[rules[i],['Outcome_3', outcome_col[i]]]                       = df.loc[rules[i],[outcome_col[i], 'Outcome_3']].values
        df.loc[rules[i],['SMD_3', smd_col[i]]]                               = df.loc[rules[i],[smd_col[i], 'SMD_3']].values
        df.loc[rules[i],['SESMD_3', sesmd_col[i]]]                           = df.loc[rules[i],[sesmd_col[i], 'SESMD_3']].values
        df.loc[rules[i],['CIupperSMD_3', cilower_col[i]]]                    = df.loc[rules[i],[ciupper_col[i], 'CIupperSMD_3']].values
        df.loc[rules[i],['CIlowerSMD_3', cilower_col[i]]]                    = df.loc[rules[i],[cilower_col[i], 'CIlowerSMD_3']].values
        df.loc[rules[i],['OutcomeID_3', outcomeid_col[i]]]                   = df.loc[rules[i],[outcomeid_col[i], 'OutcomeID_3']].values
        df.loc[rules[i],['InterventionText_3', itervtext_col[i]]]            = df.loc[rules[i],[itervtext_col[i], 'InterventionText_3']].values
        df.loc[rules[i],['ControlText_3', controltext_col[i]]]               = df.loc[rules[i],[controltext_col[i], 'ControlText_3']].values

    ######################
    # FOURTH COLUMN CHECK 
    ######################

    # set rules for checking second column against others
    check_first    = ((df["Outcome_4"] != 'Primary outcome') & (df["Outcome_5"] == 'Primary outcome'))
    check_second   = ((df["Outcome_4"] != 'Primary outcome') & (df["Outcome_6"] == 'Primary outcome'))
    check_third    = ((df["Outcome_4"] != 'Primary outcome') & (df["Outcome_7"] == 'Primary outcome'))
    check_fourth   = ((df["Outcome_4"] != 'Primary outcome') & (df["Outcome_8"] == 'Primary outcome'))
    check_fifth    = ((df["Outcome_4"] != 'Primary outcome') & (df["Outcome_9"] == 'Primary outcome'))
    check_sixth    = ((df["Outcome_4"] != 'Primary outcome') & (df["Outcome_10"] == 'Primary outcome'))

    rules = [check_first, check_second, check_third, check_fourth, check_fifth,
             check_sixth]

    effectsizetype_col.pop(0)
    testtype_col.pop(0)
    title_col.pop(0)
    toolkitstrand_col.pop(0)
    outcome_col.pop(0)
    smd_col.pop(0)
    sesmd_col.pop(0)
    cilower_col.pop(0)
    ciupper_col.pop(0)
    itervtext_col.pop(0)
    controltext_col.pop(0)

    # check against fourth column
    for i in range(len(rules)):
        df.loc[rules[i],['EffectSizeType_Outcome_4', effectsizetype_col[i]]] = df.loc[rules[i],[effectsizetype_col[i], 'EffectSizeType_Outcome_4']].values
        df.loc[rules[i],['TestType_Outcome_4', testtype_col[i]]]             = df.loc[rules[i],[testtype_col[i], 'TestType_Outcome_4']].values
        df.loc[rules[i],['OutcomeLabel_4', title_col[i]]]                    = df.loc[rules[i],[title_col[i], 'OutcomeLabel_4']].values
        df.loc[rules[i],['ToolkitStrand_Outcome_4', toolkitstrand_col[i]]]   = df.loc[rules[i],[toolkitstrand_col[i], 'ToolkitStrand_Outcome_4']].values
        df.loc[rules[i],['Outcome_4', outcome_col[i]]]                       = df.loc[rules[i],[outcome_col[i], 'Outcome_4']].values
        df.loc[rules[i],['SMD_4', smd_col[i]]]                               = df.loc[rules[i],[smd_col[i], 'SMD_4']].values
        df.loc[rules[i],['SESMD_4', sesmd_col[i]]]                           = df.loc[rules[i],[sesmd_col[i], 'SESMD_4']].values
        df.loc[rules[i],['CIupperSMD_4', cilower_col[i]]]                    = df.loc[rules[i],[ciupper_col[i], 'CIupperSMD_4']].values
        df.loc[rules[i],['CIlowerSMD_4', cilower_col[i]]]                    = df.loc[rules[i],[cilower_col[i], 'CIlowerSMD_4']].values
        df.loc[rules[i],['OutcomeID_4', outcomeid_col[i]]]                   = df.loc[rules[i],[outcomeid_col[i], 'OutcomeID_4']].values
        df.loc[rules[i],['InterventionText_4', itervtext_col[i]]]            = df.loc[rules[i],[itervtext_col[i], 'InterventionText_4']].values
        df.loc[rules[i],['ControlText_4', controltext_col[i]]]               = df.loc[rules[i],[controltext_col[i], 'ControlText_4']].values

# call all functions
get_admin_strand(admin_strand_output)
get_estype(effect_size_type_output)
get_testtype(test_type_output)
get_strands(strand_output) 
get_basic_info()
get_title()
get_SMD()
get_SESMD()
get_CIupperSMD()
get_CIlowerSMD()
get_Outcome()
get_OutcomeID()
get_InterventionText()
get_ControlText()
make_dataframe()
""" move_primary() """

# save dataframe to file (.csv)
df.to_csv("EffectSizeDetails.csv", index=False)

