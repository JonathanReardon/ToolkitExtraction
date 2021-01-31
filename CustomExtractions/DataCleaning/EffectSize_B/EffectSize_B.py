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
from ToolkitStrand import toolkitstrand_df
from OutcomeMeasure import outcome_measure_df
from Group1_N import group1N_df
from Group2_N import group2N_df
from Group1_Mean import group1mean_df
from Group2_Mean import group2mean_df
from Group1_SD import group1sd_df
from Group2_SD import group2sd_df

import pandas as pd
import numpy as np
from toolz import interleave
import re

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
    toolkitstrand_df, 
    outcome_title_df, 
    group1N_df, 
    group2N_df, 
    group1mean_df, 
    group2mean_df, 
    group1sd_df, 
    group2sd_df, 
    outcome_description_df
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
    toolkitstrand_df, 
    outcome_title_df, 
    group1N_df,
    group2N_df, 
    group1mean_df, 
    group2mean_df, 
    group1sd_df, 
    group2sd_df, 
    outcome_description_df
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
toolkit_out_strand = []
toolkit_out_tit = []
toolkit_g1_n = []
toolkit_g2_n = []
toolkit_g1_mean = []
toolkit_g2_mean = []
toolkit_g1_sd = []
toolkit_g2_sd = []
toolkit_out_desc = []

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
    toolkit_out_strand, 
    toolkit_out_tit, 
    toolkit_g1_n,
    toolkit_g2_n,
    toolkit_g1_mean, 
    toolkit_g2_mean, 
    toolkit_g1_sd,
    toolkit_g2_sd, 
    toolkit_out_desc
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
    "out_strand_",
    "out_tit_",
    "out_g1_n_",
    "out_g2_n_",
    "out_g1_mean_",
    "out_g2_mean_",
    "out_g1_sd_",
    "out_g2_sd_",
    "out_desc_"
]

for counter, row in enumerate(df['out_type_1']):
    if 'Toolkit primary outcome' in row:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"1"][counter])
    elif 'Toolkit primary outcome' in df['out_type_2'][counter]:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"2"][counter])
    elif 'Toolkit primary outcome' in df['out_type_3'][counter]:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"3"][counter])
    elif 'Toolkit primary outcome' in df['out_type_4'][counter]:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"4"][counter])
    elif 'Toolkit primary outcome' in df['out_type_5'][counter]:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"5"][counter])
    elif 'Toolkit primary outcome' in df['out_type_6'][counter]:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"6"][counter])
    elif 'Toolkit primary outcome' in df['out_type_7'][counter]:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"7"][counter])
    elif 'Toolkit primary outcome' in df['out_type_8'][counter]:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"8"][counter])
    elif 'Toolkit primary outcome' in df['out_type_9'][counter]:
        for counter2, holder in enumerate(toolkit_holders):
            holder.append(df[outcome_vars[counter2]+"9"][counter])
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
reading_prim_out_strand = []
reading_prim_out_tit = []
reading_prim_g1_n = []
reading_prim_g2_n = []
reading_prim_g1_mean = []
reading_prim_g2_mean = []
reading_prim_g1_sd = []
reading_prim_g2_sd = []
reading_prim_out_desc = []

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
    reading_prim_out_strand,
    reading_prim_out_tit,
    reading_prim_g1_n,
    reading_prim_g2_n,
    reading_prim_g1_mean,
    reading_prim_g2_mean,
    reading_prim_g1_sd,
    reading_prim_g2_sd,
    reading_prim_out_desc
]

for counter, row in enumerate(df['out_type_1']):
    if 'Reading primary outcome' in row:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"1"][counter])
    elif 'Reading primary outcome' in df['out_type_2'][counter]:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"2"][counter])
    elif 'Reading primary outcome' in df['out_type_3'][counter]:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"3"][counter])
    elif 'Reading primary outcome' in df['out_type_4'][counter]:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"4"][counter])
    elif 'Reading primary outcome' in df['out_type_5'][counter]:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"5"][counter])
    elif 'Reading primary outcome' in df['out_type_6'][counter]:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"6"][counter])
    elif 'Reading primary outcome' in df['out_type_7'][counter]:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"7"][counter])
    elif 'Reading primary outcome' in df['out_type_8'][counter]:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"8"][counter])
    elif 'Reading primary outcome' in df['out_type_9'][counter]:
        for counter2, holder in enumerate(reading_holders):
            holder.append(df[outcome_vars[counter2]+"9"][counter])
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
Writing_and_spelling_prim_out_strand = []
Writing_and_spelling_prim_out_tit = []
Writing_and_spelling_prim_g1_n = []
Writing_and_spelling_prim_g2_n = []
Writing_and_spelling_prim_g1_mean = []
Writing_and_spelling_prim_g2_mean = []
Writing_and_spelling_prim_g1_sd = []
Writing_and_spelling_prim_g2_sd = []
Writing_and_spelling_prim_out_desc = []

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
    Writing_and_spelling_prim_out_strand,
    Writing_and_spelling_prim_out_tit,
    Writing_and_spelling_prim_g1_n,
    Writing_and_spelling_prim_g2_n,
    Writing_and_spelling_prim_g1_mean,
    Writing_and_spelling_prim_g2_mean,
    Writing_and_spelling_prim_g1_sd,
    Writing_and_spelling_prim_g2_sd,
    Writing_and_spelling_prim_out_desc
]

for counter, row in enumerate(df['out_type_1']):
    if 'Writing and spelling primary outcome' in row:
        for counter2, holder in enumerate(writing_holders):
            holder.append(df[outcome_vars[counter2]+"1"][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_2'][counter]:
        for counter2, holder in enumerate(writing_holders):
            holder.append(df[outcome_vars[counter2]+"2"][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_3'][counter]:
        for counter2, holder in enumerate(writing_holders):
            holder.append(df[outcome_vars[counter2]+"3"][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_4'][counter]:
        for counter2, holder in enumerate(writing_holders):
            holder.append(df[outcome_vars[counter2]+"4"][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_5'][counter]:
        for counter2, holder in enumerate(writing_holders):
            holder.append(df[outcome_vars[counter2]+"5"][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_6'][counter]:
        for counter2, holder in enumerate(writing_holders):
            holder.append(df[outcome_vars[counter2]+"6"][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_7'][counter]:
        for counter2, holder in enumerate(writing_holders):
            holder.append(df[outcome_vars[counter2]+"7"][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_8'][counter]:
        for counter2, holder in enumerate(writing_holders):
            holder.append(df[outcome_vars[counter2]+"8"][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_9'][counter]:
         for counter2, holder in enumerate(writing_holders):
                holder.append(df[outcome_vars[counter2]+"9"][counter])
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
Mathematics_prim_out_strand = []
Mathematics_prim_out_tit = []
Mathematics_prim_g1_n = []
Mathematics_prim_g2_n = []
Mathematics_prim_g1_mean = []
Mathematics_prim_g2_mean = []
Mathematics_prim_g1_sd = []
Mathematics_prim_g2_sd = []
Mathematics_prim_out_desc = []

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
    Mathematics_prim_out_strand,
    Mathematics_prim_out_tit,
    Mathematics_prim_g1_n,
    Mathematics_prim_g2_n,
    Mathematics_prim_g1_mean,
    Mathematics_prim_g2_mean,
    Mathematics_prim_g1_sd,
    Mathematics_prim_g2_sd,
    Mathematics_prim_out_desc
]

for counter, row in enumerate(df['out_type_1']):
    if 'Mathematics primary outcome' in row:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"1"][counter])
    elif 'Mathematics primary outcome' in df['out_type_2'][counter]:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"2"][counter])
    elif 'Mathematics primary outcome' in df['out_type_3'][counter]:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"3"][counter])
    elif 'Mathematics primary outcome' in df['out_type_4'][counter]:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"4"][counter])
    elif 'Mathematics primary outcome' in df['out_type_5'][counter]:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"5"][counter])
    elif 'Mathematics primary outcome' in df['out_type_6'][counter]:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"6"][counter])
    elif 'Mathematics primary outcome' in df['out_type_7'][counter]:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"7"][counter])
    elif 'Mathematics primary outcome' in df['out_type_8'][counter]:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"8"][counter])
    elif 'Mathematics primary outcome' in df['out_type_9'][counter]:
        for counter2, holder in enumerate(mathematics_holders):
            holder.append(df[outcome_vars[counter2]+"9"][counter])
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
Science_prim_out_strand = []
Science_prim_out_tit = []
Science_prim_g1_n = []
Science_prim_g2_n = []
Science_prim_g1_mean = []
Science_prim_g2_mean = []
Science_prim_g1_sd = []
Science_prim_g2_sd = []
Science_prim_out_desc = []

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
    Science_prim_out_strand,
    Science_prim_out_tit,
    Science_prim_g1_n,
    Science_prim_g2_n,
    Science_prim_g1_mean,
    Science_prim_g2_mean,
    Science_prim_g1_sd,
    Science_prim_g2_sd,
    Science_prim_out_desc
]

for counter, row in enumerate(df['out_type_1']):
    if 'Science primary outcome' in row:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"1"][counter])
    elif 'Science primary outcome' in df['out_type_2'][counter]:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"2"][counter])
    elif 'Science primary outcome' in df['out_type_3'][counter]:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"3"][counter])
    elif 'Science primary outcome' in df['out_type_4'][counter]:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"4"][counter])
    elif 'Science primary outcome' in df['out_type_5'][counter]:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"5"][counter])
    elif 'Science primary outcome' in df['out_type_6'][counter]:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"6"][counter])
    elif 'Science primary outcome' in df['out_type_7'][counter]:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"7"][counter])
    elif 'Science primary outcome' in df['out_type_8'][counter]:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"8"][counter])
    elif 'Science primary outcome' in df['out_type_9'][counter]:
        for counter2, holder in enumerate(science_holders):
            holder.append(df[outcome_vars[counter2]+"9"][counter])
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
FSM_prim_out_strand = []
FSM_prim_out_tit = []
FSM_prim_g1_n = []
FSM_prim_g2_n = []
FSM_prim_g1_mean = []
FSM_prim_g2_mean = []
FSM_prim_g1_sd = []
FSM_prim_g2_sd = []
FSM_prim_out_desc = []

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
    FSM_prim_out_strand,
    FSM_prim_out_tit,
    FSM_prim_g1_n,
    FSM_prim_g2_n,
    FSM_prim_g1_mean,
    FSM_prim_g2_mean,
    FSM_prim_g1_sd,
    FSM_prim_g2_sd,
    FSM_prim_out_desc
]

for counter, row in enumerate(df['out_type_1']):
    if 'SES/FSM outcome' in row:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"1"][counter])
    elif 'SES/FSM outcome' in df['out_type_2'][counter]:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"2"][counter])
    elif 'SES/FSM outcome' in df['out_type_3'][counter]:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"3"][counter])
    elif 'SES/FSM outcome' in df['out_type_4'][counter]:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"4"][counter])
    elif 'SES/FSM outcome' in df['out_type_5'][counter]:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"5"][counter])
    elif 'SES/FSM outcome' in df['out_type_6'][counter]:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"6"][counter])
    elif 'SES/FSM outcome' in df['out_type_7'][counter]:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"7"][counter])
    elif 'SES/FSM outcome' in df['out_type_8'][counter]:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"8"][counter])
    elif 'SES/FSM outcome' in df['out_type_9'][counter]:
        for counter2, holder in enumerate(fsm_holders):
            holder.append(df[outcome_vars[counter2]+"9"][counter])
    else:
        for holder in fsm_holders:
            holder.append("NA")

df_zip = list(zip(
    toolkit_out_tit, 
    toolkit_out_desc, 
    toolkit_prim, 
    toolkit_g1_n, 
    toolkit_g1_mean, 
    toolkit_g1_sd, 
    toolkit_g2_n, 
    toolkit_g2_mean, 
    toolkit_g2_sd,
    toolkit_prim_smd, 
    toolkit_prim_se, 
    toolkit_prim_ci_lower, 
    toolkit_prim_ci_upper, 
    toolkit_prim_outcome, 
    toolkit_prim_sample, 
    toolkit_prim_outcomp,
    toolkit_es_type, 
    toolkit_out_measure, 
    toolkit_out_strand,

    reading_prim_out_tit, 
    reading_prim_out_desc, 
    reading_prim, 
    reading_prim_g1_n, 
    reading_prim_g1_mean, 
    reading_prim_g1_sd,
    reading_prim_g2_n, 
    reading_prim_g2_mean, 
    reading_prim_g2_sd, 
    reading_prim_smd, 
    reading_prim_se, 
    reading_prim_ci_lower,
    reading_prim_ci_upper, 
    reading_prim_outcome, 
    reading_prim_sample, 
    reading_prim_outcomp, 
    reading_prim_es_type, 
    reading_prim_out_measure,
    reading_prim_out_strand,
              
    Writing_and_spelling_prim_out_tit, 
    Writing_and_spelling_prim_out_desc, 
    Writing_and_spelling_prim, 
    Writing_and_spelling_prim_g1_n,
    Writing_and_spelling_prim_g1_mean, 
    Writing_and_spelling_prim_g1_sd, 
    Writing_and_spelling_prim_g2_n, 
    Writing_and_spelling_prim_g2_mean,
    Writing_and_spelling_prim_g2_sd, 
    Writing_and_spelling_prim_smd, 
    Writing_and_spelling_prim_se, 
    Writing_and_spelling_prim_ci_lower,
    Writing_and_spelling_prim_ci_upper, 
    Writing_and_spelling_prim_outcome, 
    Writing_and_spelling_prim_sample, 
    Writing_and_spelling_prim_outcomp,
    Writing_and_spelling_prim_es_type, 
    Writing_and_spelling_prim_out_measure, 
    Writing_and_spelling_prim_out_strand,

    Mathematics_prim_out_tit, 
    Mathematics_prim_out_desc, 
    Mathematics_prim, 
    Mathematics_prim_g1_n, 
    Mathematics_prim_g1_mean, 
    Mathematics_prim_g1_sd,
    Mathematics_prim_g2_n, 
    Mathematics_prim_g2_mean, 
    Mathematics_prim_g2_sd, 
    Mathematics_prim_smd, 
    Mathematics_prim_se, 
    Mathematics_prim_ci_lower,
    Mathematics_prim_ci_upper, 
    Mathematics_prim_outcome, 
    Mathematics_prim_sample, 
    Mathematics_prim_outcomp, 
    Mathematics_prim_es_type, 
    Mathematics_prim_out_measure,
    Mathematics_prim_out_strand,
              
    Science_prim_out_tit, 
    Science_prim_out_desc, 
    Science_prim, 
    Science_prim_g1_n, 
    Science_prim_g1_mean, 
    Science_prim_g1_sd, 
    Science_prim_g2_n, 
    Science_prim_g2_mean,
    Science_prim_g2_sd, 
    Science_prim_smd, 
    Science_prim_se, 
    Science_prim_ci_lower, 
    Science_prim_ci_upper, 
    Science_prim_outcomp, 
    Science_prim_sample, 
    Science_prim_outcomp, 
    Science_prim_es_type, 
    Science_prim_out_measure, 
    Science_prim_out_strand,

    FSM_prim_out_tit,
    FSM_prim_out_desc,
    FSM_prim,
    FSM_prim_g1_n,
    FSM_prim_g1_mean,
    FSM_prim_g1_sd,
    FSM_prim_g2_n,
    FSM_prim_g2_mean,
    FSM_prim_g2_sd,
    FSM_prim_smd,
    FSM_prim_se,
    FSM_prim_ci_lower,
    FSM_prim_ci_upper,
    FSM_prim_outcome,
    FSM_prim_sample,
    FSM_prim_outcomp,
    FSM_prim_es_type,
    FSM_prim_out_measure,
    FSM_prim_out_strand,
))

df = pd.DataFrame(df_zip)

df.rename(columns={
    0:"out_tit_tool", 
    1:"out_desc_tool", 
    2:"out_type_tool", 
    3:"out_g1_n_tool", 
    4:"out_g1_mean_tool", 
    5:"out_g1_sd_tool", 
    6:"out_g2_n_tool", 
    7:"out_g2_mean_tool", 
    8:"out_g2_sd_tool", 
    9:"smd_tool", 
    10:"se_tool", 
    11:"ci_lower_tool", 
    12:"ci_upper_tool",
    13:"out_label_tool",
    14:"out_samp_tool", 
    15:"out_comp_tool", 
    16:"out_es_type_tool", 
    17:"out_measure_tool", 
    18:"out_strand_tool",

    19:"out_tit_red", 
    20:"out_desc_red", 
    21:"out_type_red", 
    22:"out_g1_n_red", 
    23:"out_g1_mean_red", 
    24:"out_g1_sd_red", 
    25:"out_g2_n_red", 
    26:"out_g2_mean_red", 
    27:"out_g2_sd_red", 
    28:"smd_red", 
    29:"se_red", 
    30:"ci_lower_red", 
    31:"ci_upper_red",
    32:"out_label_red",
    33:"out_samp_red", 
    34:"out_comp_red", 
    35:"out_es_type_red", 
    36:"out_measure_red", 
    37:"out_strand_red",
    
    38:"out_tit_wri", 
    39:"out_desc_wri", 
    40:"out_type_wri", 
    41:"out_g1_n_wri", 
    42:"out_g1_mean_wri", 
    43:"out_g1_sd_wri", 
    44:"out_g2_n_wri", 
    45:"out_g2_mean_wri", 
    46:"out_g2_sd_wri", 
    47:"smd_wri", 
    48:"se_wri", 
    49:"ci_lower_wri", 
    50:"ci_upper_wri",
    51:"out_label_wri",
    52:"out_samp_wri", 
    53:"out_comp_wri", 
    54:"out_es_type_wri", 
    55:"out_measure_wri", 
    56:"out_strand_wri",

    57:"out_tit_math", 
    58:"out_desc_math", 
    59:"out_type_math", 
    60:"out_g1_n_math", 
    61:"out_g1_mean_math", 
    62:"out_g1_sd_math", 
    63:"out_g2_n_math", 
    64:"out_g2_mean_math", 
    65:"out_g2_sd_math", 
    66:"smd_math", 
    67:"se_math", 
    68:"ci_lower_math", 
    69:"ci_upper_math",
    70:"out_label_math",
    71:"out_samp_math", 
    72:"out_comp_math", 
    73:"out_es_type_math", 
    74:"out_measure_math", 
    75:"out_strand_math",

    76:"out_tit_sci", 
    77:"out_desc_sci", 
    78:"out_type_sci", 
    79:"out_g1_n_sci", 
    80:"out_g1_mean_sci", 
    81:"out_g1_sd_sci", 
    82:"out_g2_n_sci", 
    83:"out_g2_mean_sci", 
    84:"out_g2_sd_sci", 
    85:"smd_sci", 
    86:"se_sci", 
    87:"ci_lower_sci", 
    88:"ci_upper_sci",
    89:"out_label_sci",
    90:"out_samp_sci", 
    91:"out_comp_sci", 
    92:"out_es_type_sci", 
    93:"out_measure_sci", 
    94:"out_strand_sci",

    95:"out_tit_fsm", 
    96:"out_desc_fsm", 
    97:"out_type_fsm", 
    98:"out_g1_n_fsm", 
    99:"out_g1_mean_fsm", 
    100:"out_g1_sd_fsm", 
    101:"out_g2_n_fsm", 
    102:"out_g2_mean_fsm", 
    103:"out_g2_sd_fsm", 
    104:"smd_fsm", 
    105:"se_fsm", 
    106:"ci_lower_fsm", 
    107:"ci_upper_fsm",
    108:"out_label_fsm",
    109:"out_samp_fsm", 
    110:"out_comp_fsm", 
    111:"out_es_type_fsm", 
    112:"out_measure_fsm", 
    113:"out_strand_fsm",
    
}, inplace=True)

# concatenate record details and main dataframes
df = pd.concat([record_details_df, df], axis=1, sort=False)

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
outfile_name = outfile_name + "_Effect_Size_B_edit7.csv"

# write to disk
print("saving {}".format(outfile_name))
df.to_csv(outfile_name, index=False, header=True)