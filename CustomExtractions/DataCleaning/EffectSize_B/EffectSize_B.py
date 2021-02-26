from Main import file
from eppi_ID import eppiid_df
from Author import author_df
from Date import year_df
from AdminStrand import admin_strand_df
from OutcomeType import outcometype_df
from smd import smd_df
from sesmd import sesmd_df
from OutcomeDescription import outcome_description_df
from OutcomeTitle import outcome_title_df
from CIlowerSMD import cilowersmd_df
from CIupperSMD import ciuppersmd_df
from Sample import sample_df
from Outcome import outcome_df
from EffectSizeType import effectsizetype_df
from OutcomeComparison import out_comp_df
from OutcomeMeasure import outcome_measure_df
from Group1_N import group1N_df
from Group2_N import group2N_df
from Group1_Mean import group1mean_df
from Group2_Mean import group2mean_df
from Group1_SD import group1sd_df
from Group2_SD import group2sd_df
from TestType import testtype_outcome_df

import pandas as pd
import numpy as np
from toolz import interleave
import re

# for getting number of outcomes
from toolkit_outcome_check import all_variables

# get number of outcomes
outcome_num = all_variables.shape[1]-1

#################################
# REFACTOR STRAND FILTERING CODE
#################################

# concatenate record detail data frames
record_details_df = pd.concat([
    eppiid_df,
    author_df,
    year_df,
    admin_strand_df
], axis=1)

# concatenate all main dataframes
df = pd.concat([
    outcometype_df,
    smd_df,
    sesmd_df,
    cilowersmd_df,
    ciuppersmd_df,
    outcome_df,
    sample_df,
    out_comp_df,
    effectsizetype_df,
    outcome_measure_df,
    outcome_title_df,
    group1N_df,
    group2N_df,
    group1mean_df,
    group2mean_df,
    group1sd_df,
    group2sd_df,
    outcome_description_df,
    testtype_outcome_df
], axis=1)[list(interleave([
    outcometype_df,
    smd_df,
    sesmd_df,
    cilowersmd_df,
    ciuppersmd_df,
    outcome_df,
    sample_df,
    out_comp_df,
    effectsizetype_df,
    outcome_measure_df,
    outcome_title_df,
    group1N_df,
    group2N_df,
    group1mean_df,
    group2mean_df,
    group1sd_df,
    group2sd_df,
    outcome_description_df,
    testtype_outcome_df
]))]

# empty lists to hold data
toolkit_prim = []
toolkit_prim_smd = []
toolkit_prim_se = []
toolkit_prim_ci_lower = []
toolkit_prim_ci_upper = []
toolkit_prim_outcome = []
toolkit_prim_sample = []
toolkit_prim_outcomp = []
toolkit_es_type = []
toolkit_out_measure = []
toolkit_out_tit = []
toolkit_g1_n = []
toolkit_g2_n = []
toolkit_g1_mean = []
toolkit_g2_mean = []
toolkit_g1_sd = []
toolkit_g2_sd = []
toolkit_out_desc = []
toolkit_test_type = []

toolkit_holders = [
    toolkit_prim,
    toolkit_prim_smd,
    toolkit_prim_se,
    toolkit_prim_ci_lower,
    toolkit_prim_ci_upper,
    toolkit_prim_outcome,
    toolkit_prim_sample,
    toolkit_prim_outcomp,
    toolkit_es_type,
    toolkit_out_measure,
    toolkit_out_tit,
    toolkit_g1_n,
    toolkit_g2_n,
    toolkit_g1_mean,
    toolkit_g2_mean,
    toolkit_g1_sd,
    toolkit_g2_sd,
    toolkit_out_desc,
    toolkit_test_type
]

outcome_vars = [
    "out_type_",
    "smd_",
    "se_",
    "ci_lower_",
    "ci_upper_",
    "out_label_",
    "out_samp_",
    "out_comp_",
    "out_es_type_",
    "out_measure_",
    "out_tit_",
    "out_g1_n_",
    "out_g2_n_",
    "out_g1_mean_",
    "out_g2_mean_",
    "out_g1_sd_",
    "out_g2_sd_",
    "out_desc_",
    "out_test_type_raw_"
]

for counter, row in enumerate(df['out_type_1']):
    for outcome_n in range(1, outcome_num+1):
        if 'Toolkit primary outcome' in df[f'out_type_{outcome_n}'][counter]:
            for counter2, holder in enumerate(toolkit_holders):
                holder.append(
                    df[outcome_vars[counter2] + f"{outcome_n}"][counter])
            break
    else:
        for holder in toolkit_holders:
            holder.append("NA")

reading_prim = []
reading_prim_smd = []
reading_prim_se = []
reading_prim_ci_lower = []
reading_prim_ci_upper = []
reading_prim_outcome = []
reading_prim_sample = []
reading_prim_outcomp = []
reading_prim_es_type = []
reading_prim_out_measure = []
reading_prim_out_tit = []
reading_prim_g1_n = []
reading_prim_g2_n = []
reading_prim_g1_mean = []
reading_prim_g2_mean = []
reading_prim_g1_sd = []
reading_prim_g2_sd = []
reading_prim_out_desc = []
reading_test_type = []

reading_holders = [
    reading_prim,
    reading_prim_smd,
    reading_prim_se,
    reading_prim_ci_lower,
    reading_prim_ci_upper,
    reading_prim_outcome,
    reading_prim_sample,
    reading_prim_outcomp,
    reading_prim_es_type,
    reading_prim_out_measure,
    reading_prim_out_tit,
    reading_prim_g1_n,
    reading_prim_g2_n,
    reading_prim_g1_mean,
    reading_prim_g2_mean,
    reading_prim_g1_sd,
    reading_prim_g2_sd,
    reading_prim_out_desc,
    reading_test_type
]

for counter, row in enumerate(df['out_type_1']):
    for outcome_n in range(1, outcome_num+1):
        if 'Reading primary outcome' in df[f'out_type_{outcome_n}'][counter]:
            for counter2, holder in enumerate(reading_holders):
                holder.append(
                    df[outcome_vars[counter2] + f"{outcome_n}"][counter])
            break
    else:
        for holder in reading_holders:
            holder.append("NA")

Writing_and_spelling_prim = []
Writing_and_spelling_prim_smd = []
Writing_and_spelling_prim_se = []
Writing_and_spelling_prim_ci_lower = []
Writing_and_spelling_prim_ci_upper = []
Writing_and_spelling_prim_outcome = []
Writing_and_spelling_prim_sample = []
Writing_and_spelling_prim_outcomp = []
Writing_and_spelling_prim_es_type = []
Writing_and_spelling_prim_out_measure = []
Writing_and_spelling_prim_out_tit = []
Writing_and_spelling_prim_g1_n = []
Writing_and_spelling_prim_g2_n = []
Writing_and_spelling_prim_g1_mean = []
Writing_and_spelling_prim_g2_mean = []
Writing_and_spelling_prim_g1_sd = []
Writing_and_spelling_prim_g2_sd = []
Writing_and_spelling_prim_out_desc = []
Writing_and_spelling_test_type = []

writing_holders = [
    Writing_and_spelling_prim,
    Writing_and_spelling_prim_smd,
    Writing_and_spelling_prim_se,
    Writing_and_spelling_prim_ci_lower,
    Writing_and_spelling_prim_ci_upper,
    Writing_and_spelling_prim_outcome,
    Writing_and_spelling_prim_sample,
    Writing_and_spelling_prim_outcomp,
    Writing_and_spelling_prim_es_type,
    Writing_and_spelling_prim_out_measure,
    Writing_and_spelling_prim_out_tit,
    Writing_and_spelling_prim_g1_n,
    Writing_and_spelling_prim_g2_n,
    Writing_and_spelling_prim_g1_mean,
    Writing_and_spelling_prim_g2_mean,
    Writing_and_spelling_prim_g1_sd,
    Writing_and_spelling_prim_g2_sd,
    Writing_and_spelling_prim_out_desc,
    Writing_and_spelling_test_type
]

for counter, row in enumerate(df['out_type_1']):
    for outcome_n in range(1, outcome_num+1):
        if 'Writing and spelling primary outcome' in df[f'out_type_{outcome_n}'][counter]:
            for counter2, holder in enumerate(writing_holders):
                holder.append(
                    df[outcome_vars[counter2] + f"{outcome_n}"][counter])
            break
    else:
        for holder in writing_holders:
            holder.append("NA")

Mathematics_prim = []
Mathematics_prim_smd = []
Mathematics_prim_se = []
Mathematics_prim_ci_lower = []
Mathematics_prim_ci_upper = []
Mathematics_prim_outcome = []
Mathematics_prim_sample = []
Mathematics_prim_outcomp = []
Mathematics_prim_es_type = []
Mathematics_prim_out_measure = []
Mathematics_prim_out_tit = []
Mathematics_prim_g1_n = []
Mathematics_prim_g2_n = []
Mathematics_prim_g1_mean = []
Mathematics_prim_g2_mean = []
Mathematics_prim_g1_sd = []
Mathematics_prim_g2_sd = []
Mathematics_prim_out_desc = []
Mathematics_test_type = []

mathematics_holders = [
    Mathematics_prim,
    Mathematics_prim_smd,
    Mathematics_prim_se,
    Mathematics_prim_ci_lower,
    Mathematics_prim_ci_upper,
    Mathematics_prim_outcome,
    Mathematics_prim_sample,
    Mathematics_prim_outcomp,
    Mathematics_prim_es_type,
    Mathematics_prim_out_measure,
    Mathematics_prim_out_tit,
    Mathematics_prim_g1_n,
    Mathematics_prim_g2_n,
    Mathematics_prim_g1_mean,
    Mathematics_prim_g2_mean,
    Mathematics_prim_g1_sd,
    Mathematics_prim_g2_sd,
    Mathematics_prim_out_desc,
    Mathematics_test_type
]

for counter, row in enumerate(df['out_type_1']):
    for outcome_n in range(1, outcome_num+1):
        if 'Mathematics primary outcome' in df[f'out_type_{outcome_n}'][counter]:
            for counter2, holder in enumerate(mathematics_holders):
                holder.append(
                    df[outcome_vars[counter2] + f"{outcome_n}"][counter])
            break
    else:
        for holder in mathematics_holders:
            holder.append("NA")

Science_prim = []
Science_prim_smd = []
Science_prim_se = []
Science_prim_ci_lower = []
Science_prim_ci_upper = []
Science_prim_outcome = []
Science_prim_sample = []
Science_prim_outcomp = []
Science_prim_es_type = []
Science_prim_out_measure = []
Science_prim_out_tit = []
Science_prim_g1_n = []
Science_prim_g2_n = []
Science_prim_g1_mean = []
Science_prim_g2_mean = []
Science_prim_g1_sd = []
Science_prim_g2_sd = []
Science_prim_out_desc = []
Science_test_type = []

science_holders = [
    Science_prim,
    Science_prim_smd,
    Science_prim_se,
    Science_prim_ci_lower,
    Science_prim_ci_upper,
    Science_prim_outcome,
    Science_prim_sample,
    Science_prim_outcomp,
    Science_prim_es_type,
    Science_prim_out_measure,
    Science_prim_out_tit,
    Science_prim_g1_n,
    Science_prim_g2_n,
    Science_prim_g1_mean,
    Science_prim_g2_mean,
    Science_prim_g1_sd,
    Science_prim_g2_sd,
    Science_prim_out_desc,
    Science_test_type
]

for counter, row in enumerate(df['out_type_1']):
    for outcome_n in range(1, outcome_num+1):
        if 'Science primary outcome' in df[f'out_type_{outcome_n}'][counter]:
            for counter2, holder in enumerate(science_holders):
                holder.append(
                    df[outcome_vars[counter2] + f"{outcome_n}"][counter])
            break
    else:
        for holder in science_holders:
            holder.append("NA")

FSM_prim = []
FSM_prim_smd = []
FSM_prim_se = []
FSM_prim_ci_lower = []
FSM_prim_ci_upper = []
FSM_prim_outcome = []
FSM_prim_sample = []
FSM_prim_outcomp = []
FSM_prim_es_type = []
FSM_prim_out_measure = []
FSM_prim_out_tit = []
FSM_prim_g1_n = []
FSM_prim_g2_n = []
FSM_prim_g1_mean = []
FSM_prim_g2_mean = []
FSM_prim_g1_sd = []
FSM_prim_g2_sd = []
FSM_prim_out_desc = []
FSM_test_type = []

fsm_holders = [
    FSM_prim,
    FSM_prim_smd,
    FSM_prim_se,
    FSM_prim_ci_lower,
    FSM_prim_ci_upper,
    FSM_prim_outcome,
    FSM_prim_sample,
    FSM_prim_outcomp,
    FSM_prim_es_type,
    FSM_prim_out_measure,
    FSM_prim_out_tit,
    FSM_prim_g1_n,
    FSM_prim_g2_n,
    FSM_prim_g1_mean,
    FSM_prim_g2_mean,
    FSM_prim_g1_sd,
    FSM_prim_g2_sd,
    FSM_prim_out_desc,
    FSM_test_type
]

for counter, row in enumerate(df['out_type_1']):
    for outcome_n in range(1, outcome_num+1):
        if 'SES/FSM outcome' in df[f'out_type_{outcome_n}'][counter]:
            for counter2, holder in enumerate(fsm_holders):
                holder.append(
                    df[outcome_vars[counter2] + f"{outcome_n}"][counter])
            break
    else:
        for holder in fsm_holders:
            holder.append("NA")

df_zip = list(zip(
    toolkit_out_tit,
    toolkit_out_desc,
    toolkit_prim,
    toolkit_prim_smd,
    toolkit_prim_se,
    toolkit_out_measure,
    toolkit_g1_n,
    toolkit_g1_mean,
    toolkit_g1_sd,
    toolkit_g2_n,
    toolkit_g2_mean,
    toolkit_g2_sd,
    toolkit_prim_ci_lower,
    toolkit_prim_ci_upper,
    toolkit_prim_outcome,
    toolkit_prim_sample,
    toolkit_prim_outcomp,
    toolkit_es_type,
    toolkit_test_type,

    reading_prim_out_tit,
    reading_prim_out_desc,
    reading_prim,
    reading_prim_smd,
    reading_prim_se,
    reading_prim_out_measure,
    reading_prim_g1_n,
    reading_prim_g1_mean,
    reading_prim_g1_sd,
    reading_prim_g2_n,
    reading_prim_g2_mean,
    reading_prim_g2_sd,
    reading_prim_ci_lower,
    reading_prim_ci_upper,
    reading_prim_outcome,
    reading_prim_sample,
    reading_prim_outcomp,
    reading_prim_es_type,
    reading_test_type,

    Writing_and_spelling_prim_out_tit,
    Writing_and_spelling_prim_out_desc,
    Writing_and_spelling_prim,
    Writing_and_spelling_prim_smd,
    Writing_and_spelling_prim_se,
    Writing_and_spelling_prim_out_measure,
    Writing_and_spelling_prim_g1_n,
    Writing_and_spelling_prim_g1_mean,
    Writing_and_spelling_prim_g1_sd,
    Writing_and_spelling_prim_g2_n,
    Writing_and_spelling_prim_g2_mean,
    Writing_and_spelling_prim_g2_sd,
    Writing_and_spelling_prim_ci_lower,
    Writing_and_spelling_prim_ci_upper,
    Writing_and_spelling_prim_outcome,
    Writing_and_spelling_prim_sample,
    Writing_and_spelling_prim_outcomp,
    Writing_and_spelling_prim_es_type,
    Writing_and_spelling_test_type,

    Mathematics_prim_out_tit,
    Mathematics_prim_out_desc,
    Mathematics_prim,
    Mathematics_prim_smd,
    Mathematics_prim_se,
    Mathematics_prim_out_measure,
    Mathematics_prim_g1_n,
    Mathematics_prim_g1_mean,
    Mathematics_prim_g1_sd,
    Mathematics_prim_g2_n,
    Mathematics_prim_g2_mean,
    Mathematics_prim_g2_sd,
    Mathematics_prim_ci_lower,
    Mathematics_prim_ci_upper,
    Mathematics_prim_outcome,
    Mathematics_prim_sample,
    Mathematics_prim_outcomp,
    Mathematics_prim_es_type,
    Mathematics_test_type,

    Science_prim_out_tit,
    Science_prim_out_desc,
    Science_prim,
    Science_prim_smd,
    Science_prim_se,
    Science_prim_out_measure,
    Science_prim_g1_n,
    Science_prim_g1_mean,
    Science_prim_g1_sd,
    Science_prim_g2_n,
    Science_prim_g2_mean,
    Science_prim_g2_sd,
    Science_prim_ci_lower,
    Science_prim_ci_upper,
    Science_prim_outcome,
    Science_prim_sample,
    Science_prim_outcomp,
    Science_prim_es_type,
    Science_test_type,

    FSM_prim_out_tit,
    FSM_prim_out_desc,
    FSM_prim,
    FSM_prim_smd,
    FSM_prim_se,
    FSM_prim_out_measure,
    FSM_prim_g1_n,
    FSM_prim_g1_mean,
    FSM_prim_g1_sd,
    FSM_prim_g2_n,
    FSM_prim_g2_mean,
    FSM_prim_g2_sd,
    FSM_prim_ci_lower,
    FSM_prim_ci_upper,
    FSM_prim_outcome,
    FSM_prim_sample,
    FSM_prim_outcomp,
    FSM_prim_es_type,
    FSM_test_type
))

df = pd.DataFrame(df_zip)

df.rename(columns={
    0: "out_tit_tool",
    1: "out_desc_tool",
    2: "out_type_tool",
    3: "smd_tool",
    4: "se_tool",
    5: "out_measure_tool",
    6: "out_g1_n_tool",
    7: "out_g1_mean_tool",
    8: "out_g1_sd_tool",
    9: "out_g2_n_tool",
    10: "out_g2_mean_tool",
    11: "out_g2_sd_tool",
    12: "ci_lower_tool",
    13: "ci_upper_tool",
    14: "out_label_tool",
    15: "out_samp_tool",
    16: "out_comp_tool",
    17: "out_es_type_tool",
    18: "out_test_type_raw_tool",

    19: "out_tit_red",
    20: "out_desc_red",
    21: "out_type_red",
    22: "smd_red",
    23: "se_red",
    24: "out_measure_red",
    25: "out_g1_n_red",
    26: "out_g1_mean_red",
    27: "out_g1_sd_red",
    28: "out_g2_n_red",
    29: "out_g2_mean_red",
    30: "out_g2_sd_red",
    31: "ci_lower_red",
    32: "ci_upper_red",
    33: "out_label_red",
    34: "out_samp_red",
    35: "out_comp_red",
    36: "out_es_type_red",
    37: "out_test_type_raw_red",

    38: "out_tit_wri",
    39: "out_desc_wri",
    40: "out_type_wri",
    41: "smd_wri",
    42: "se_wri",
    43: "out_measure_wri",
    44: "out_g1_n_wri",
    45: "out_g1_mean_wri",
    46: "out_g1_sd_wri",
    47: "out_g2_n_wri",
    48: "out_g2_mean_wri",
    49: "out_g2_sd_wri",
    50: "ci_lower_wri",
    51: "ci_upper_wri",
    52: "out_label_wri",
    53: "out_samp_wri",
    54: "out_comp_wri",
    55: "out_es_type_wri",
    56: "out_test_type_raw_wri",

    57: "out_tit_math",
    58: "out_desc_math",
    59: "out_type_math",
    60: "smd_math",
    61: "se_math",
    62: "out_measure_math",
    63: "out_g1_n_math",
    64: "out_g1_mean_math",
    65: "out_g1_sd_math",
    66: "out_g2_n_math",
    67: "out_g2_mean_math",
    68: "out_g2_sd_math",
    69: "ci_lower_math",
    70: "ci_upper_math",
    71: "out_label_math",
    72: "out_samp_math",
    73: "out_comp_math",
    74: "out_es_type_math",
    75: "out_test_type_raw_math",

    76: "out_tit_sci",
    77: "out_desc_sci",
    78: "out_type_sci",
    79: "smd_sci",
    80: "se_sci",
    81: "out_measure_sci",
    82: "out_g1_n_sci",
    83: "out_g1_mean_sci",
    84: "out_g1_sd_sci",
    85: "out_g2_n_sci",
    86: "out_g2_mean_sci",
    87: "out_g2_sd_sci",
    88: "ci_lower_sci",
    89: "ci_upper_sci",
    90: "out_label_sci",
    91: "out_samp_sci",
    92: "out_comp_sci",
    93: "out_es_type_sci",
    94: "out_test_type_raw_sci",

    95: "out_tit_fsm",
    96: "out_desc_fsm",
    97: "out_type_fsm",
    98: "smd_fsm",
    99: "se_fsm",
    100: "out_measure_fsm",
    101: "out_g1_n_fsm",
    102: "out_g1_mean_fsm",
    103: "out_g1_sd_fsm",
    104: "out_g2_n_fsm",
    105: "out_g2_mean_fsm",
    106: "out_g2_sd_fsm",
    107: "ci_lower_fsm",
    108: "ci_upper_fsm",
    109: "out_label_fsm",
    110: "out_samp_fsm",
    111: "out_comp_fsm",
    112: "out_es_type_fsm",
    113: "out_test_type_raw_fsm"

}, inplace=True)

# concatenate record details and main dataframes
df = pd.concat([record_details_df, df], axis=1, sort=False)

# insert empty columns per variable for data checkers to log changes
df.insert(6, 'out_tit_tool_CLEAN', '')
df.insert(8, 'out_desc_tool_CLEAN', '')
df.insert(10, 'out_type_tool_CLEAN', '')
df.insert(12, 'smd_tool_CLEAN', '')
df.insert(14, 'se_tool_CLEAN', '')
df.insert(16, 'out_measure_tool_CLEAN', '')
df.insert(18, 'out_g1_n_tool_CLEAN', '')
df.insert(20, 'out_g1_mean_tool_CLEAN', '')
df.insert(22, 'out_g1_sd_tool_CLEAN', '')
df.insert(24, 'out_g2_n_tool_CLEAN', '')
df.insert(26, 'out_g2_mean_tool_CLEAN', '')
df.insert(28, 'out_g2_sd_tool_CLEAN', '')
df.insert(30, 'ci_lower_tool_CLEAN', '')
df.insert(32, 'ci_upper_tool_CLEAN', '')
df.insert(34, 'out_label_tool_CLEAN', '')
df.insert(36, 'out_samp_tool_CLEAN', '')
df.insert(38, 'out_comp_tool_CLEAN', '')
df.insert(40, 'out_es_type_tool_CLEAN', '')
df.insert(42, 'out_test_type_raw_tool_CLEAN', '')

df.insert(44, 'out_tit_red_CLEAN', '')
df.insert(46, 'out_desc_red_CLEAN', '')
df.insert(48, 'out_type_red_CLEAN', '')
df.insert(50, 'smd_red_CLEAN', '')
df.insert(52, 'se_red_CLEAN', '')
df.insert(54, 'out_measure_red_CLEAN', '')
df.insert(56, 'out_g1_n_red_CLEAN', '')
df.insert(58, 'out_g1_mean_red_CLEAN', '')
df.insert(60, 'out_g1_sd_red_CLEAN', '')
df.insert(62, 'out_g2_n_red_CLEAN', '')
df.insert(64, 'out_g2_mean_red_CLEAN', '')
df.insert(66, 'out_g2_sd_red_CLEAN', '')
df.insert(68, 'ci_lower_red_CLEAN', '')
df.insert(70, 'ci_upper_red_CLEAN', '')
df.insert(72, 'out_label_red_CLEAN', '')
df.insert(74, 'out_samp_red_CLEAN', '')
df.insert(76, 'out_comp_red_CLEAN', '')
df.insert(78, 'out_es_type_red_CLEAN', '')
df.insert(80, 'out_test_type_raw_red_CLEAN', '')

df.insert(82, 'out_tit_wri_CLEAN', '')
df.insert(84, 'out_desc_wri_CLEAN', '')
df.insert(86, 'out_type_wri_CLEAN', '')
df.insert(88, 'smd_wri_CLEAN', '')
df.insert(90, 'se_wri_CLEAN', '')
df.insert(92, 'out_measure_wri_CLEAN', '')
df.insert(94, 'out_g1_n_wri_CLEAN', '')
df.insert(96, 'out_g1_mean_wri_CLEAN', '')
df.insert(98, 'out_g1_sd_wri_CLEAN', '')
df.insert(100, 'out_g2_n_wri_CLEAN', '')
df.insert(102, 'out_g2_mean_wri_CLEAN', '')
df.insert(104, 'out_g2_sd_wri_CLEAN', '')
df.insert(106, 'ci_lower_wri_CLEAN', '')
df.insert(108, 'ci_upper_wri_CLEAN', '')
df.insert(110, 'out_label_wri_CLEAN', '')
df.insert(112, 'out_samp_wri_CLEAN', '')
df.insert(114, 'out_comp_wri_CLEAN', '')
df.insert(116, 'out_es_type_wri_CLEAN', '')
df.insert(118, 'out_test_type_wri_CLEAN', '')

df.insert(120, 'out_tit_math_CLEAN', '')
df.insert(122, 'out_desc_math_CLEAN', '')
df.insert(124, 'out_type_math_CLEAN', '')
df.insert(126, 'smd_math_CLEAN', '')
df.insert(128, 'se_math_CLEAN', '')
df.insert(130, 'out_measure_math_CLEAN', '')
df.insert(132, 'out_g1_n_math_CLEAN', '')
df.insert(134, 'out_g1_mean_math_CLEAN', '')
df.insert(136, 'out_g1_sd_math_CLEAN', '')
df.insert(138, 'out_g2_n_math_CLEAN', '')
df.insert(140, 'out_g2_mean_math_CLEAN', '')
df.insert(142, 'out_g2_sd_math_CLEAN', '')
df.insert(144, 'ci_lower_math_CLEAN', '')
df.insert(146, 'ci_upper_math_CLEAN', '')
df.insert(148, 'out_label_math_CLEAN', '')
df.insert(150, 'out_samp_math_CLEAN', '')
df.insert(152, 'out_comp_math_CLEAN', '')
df.insert(154, 'out_es_type_math_CLEAN', '')
df.insert(156, 'out_test_type_math_CLEAN', '')

df.insert(158, 'out_tit_sci_CLEAN', '')
df.insert(160, 'out_desc_sci_CLEAN', '')
df.insert(162, 'out_type_sci_CLEAN', '')
df.insert(164, 'smd_sci_CLEAN', '')
df.insert(166, 'se_sci_CLEAN', '')
df.insert(168, 'out_measure_sci_CLEAN', '')
df.insert(170, 'out_g1_n_sci_CLEAN', '')
df.insert(172, 'out_g1_mean_sci_CLEAN', '')
df.insert(174, 'out_g1_sd_sci_CLEAN', '')
df.insert(176, 'out_g2_n_sci_CLEAN', '')
df.insert(178, 'out_g2_mean_sci_CLEAN', '')
df.insert(180, 'out_g2_sd_sci_CLEAN', '')
df.insert(182, 'ci_lower_sci_CLEAN', '')
df.insert(184, 'ci_upper_sci_CLEAN', '')
df.insert(186, 'out_label_sci_CLEAN', '')
df.insert(188, 'out_samp_sci_CLEAN', '')
df.insert(190, 'out_comp_sci_CLEAN', '')
df.insert(192, 'out_es_type_sci_CLEAN', '')
df.insert(194, 'out_test_type_sci_CLEAN', '')

df.insert(196, 'out_tit_fsm_CLEAN', '')
df.insert(198, 'out_desc_fsm_CLEAN', '')
df.insert(200, 'out_type_fsm_CLEAN', '')
df.insert(202, 'smd_fsm_CLEAN', '')
df.insert(204, 'se_fsm_CLEAN', '')
df.insert(206, 'out_measure_fsm_CLEAN', '')
df.insert(208, 'out_g1_n_fsm_CLEAN', '')
df.insert(210, 'out_g1_mean_fsm_CLEAN', '')
df.insert(212, 'out_g1_sd_fsm_CLEAN', '')
df.insert(214, 'out_g2_n_fsm_CLEAN', '')
df.insert(216, 'out_g2_mean_fsm_CLEAN', '')
df.insert(218, 'out_g2_sd_fsm_CLEAN', '')
df.insert(220, 'ci_lower_fsm_CLEAN', '')
df.insert(222, 'ci_upper_fsm_CLEAN', '')
df.insert(224, 'out_label_fsm_CLEAN', '')
df.insert(226, 'out_samp_fsm_CLEAN', '')
df.insert(228, 'out_comp_fsm_CLEAN', '')
df.insert(230, 'out_es_type_fsm_CLEAN', '')
df.insert(232, 'out_test_type_fsm_CLEAN', '')

# list column names and position
for counter, i in enumerate(df):
    print(counter, i)

# useful info
print("Columns:", df.shape[1])
print("Rows:", df.shape[0])
print("Datapoints:", df.shape[0] * df.shape[1])

# get file name for output
outfile_name = file.rsplit('/')[-1]
outfile_name = outfile_name.rsplit('.')[0]
outfile_name = outfile_name + "_Effect_Size_B.csv"

# write to disk
print("saving {}".format(outfile_name))
df.to_csv(outfile_name, index=False, header=True)