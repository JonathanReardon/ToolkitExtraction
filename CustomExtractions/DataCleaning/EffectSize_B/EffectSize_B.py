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

#################################
# REFACTOR STRAND FILTERING CODE
#################################

record_details_df = pd.concat([
    eppiid_df, 
    author_df, 
    year_df, 
    admin_strand_df
], axis=1)

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

for counter, row in enumerate(df['out_type_1']):
    if 'Toolkit primary outcome' in row:
        toolkit_prim.append(row)
        toolkit_prim_smd.append(df['smd_1'][counter])
        toolkit_prim_se.append(df['se_1'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_1'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_1'][counter])
        toolkit_prim_outcome.append(df['out_label_1'][counter])
        toolkit_prim_sample.append(df['out_samp_1'][counter])
        toolkit_prim_outcomp.append(df['out_comp_1'][counter])
        toolkit_es_type.append(df['out_es_type_1'][counter])
        toolkit_out_measure.append(df['out_measure_1'][counter])
        toolkit_out_strand.append(df['out_strand_1'][counter])
        toolkit_out_tit.append(df['out_tit_1'][counter])
        toolkit_g1_n.append(df['out_g1_n_1'][counter])
        toolkit_g2_n.append(df['out_g2_n_1'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_1'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_1'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_1'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_1'][counter])
        toolkit_out_desc.append(df['out_desc_1'][counter])
    elif 'Toolkit primary outcome' in df['out_type_2'][counter]:
        toolkit_prim.append(df['out_type_2'][counter])
        toolkit_prim_smd.append(df['smd_2'][counter])
        toolkit_prim_se.append(df['se_2'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_2'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_2'][counter])
        toolkit_prim_outcome.append(df['out_label_2'][counter])
        toolkit_prim_sample.append(df['out_samp_2'][counter])
        toolkit_prim_outcomp.append(df['out_comp_2'][counter])
        toolkit_es_type.append(df['out_es_type_2'][counter])
        toolkit_out_measure.append(df['out_measure_2'][counter])
        toolkit_out_strand.append(df['out_strand_2'][counter])
        toolkit_out_tit.append(df['out_tit_2'][counter])
        toolkit_g1_n.append(df['out_g1_n_2'][counter])
        toolkit_g2_n.append(df['out_g2_n_2'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_2'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_2'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_2'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_2'][counter])
        toolkit_out_desc.append(df['out_desc_2'][counter])
    elif 'Toolkit primary outcome' in df['out_type_3'][counter]:
        toolkit_prim.append(df['out_type_3'][counter])
        toolkit_prim_smd.append(df['smd_3'][counter])
        toolkit_prim_se.append(df['se_3'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_3'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_3'][counter])
        toolkit_prim_outcome.append(df['out_label_3'][counter])
        toolkit_prim_sample.append(df['out_samp_3'][counter])
        toolkit_prim_outcomp.append(df['out_comp_3'][counter])
        toolkit_es_type.append(df['out_es_type_3'][counter])
        toolkit_out_measure.append(df['out_measure_3'][counter])
        toolkit_out_strand.append(df['out_strand_3'][counter])
        toolkit_out_tit.append(df['out_tit_3'][counter])
        toolkit_g1_n.append(df['out_g1_n_3'][counter])
        toolkit_g2_n.append(df['out_g2_n_3'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_3'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_3'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_3'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_3'][counter])
        toolkit_out_desc.append(df['out_desc_3'][counter])
    elif 'Toolkit primary outcome' in df['out_type_4'][counter]:
        toolkit_prim.append(df['out_type_4'][counter])
        toolkit_prim_smd.append(df['smd_4'][counter])
        toolkit_prim_se.append(df['se_4'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_4'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_4'][counter])
        toolkit_prim_outcome.append(df['out_label_4'][counter])
        toolkit_prim_sample.append(df['out_samp_4'][counter])
        toolkit_prim_outcomp.append(df['out_comp_4'][counter])
        toolkit_es_type.append(df['out_es_type_4'][counter])
        toolkit_out_measure.append(df['out_measure_4'][counter])
        toolkit_out_strand.append(df['out_strand_4'][counter])
        toolkit_out_tit.append(df['out_tit_4'][counter])
        toolkit_g1_n.append(df['out_g1_n_4'][counter])
        toolkit_g2_n.append(df['out_g2_n_4'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_4'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_4'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_4'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_4'][counter])
        toolkit_out_desc.append(df['out_desc_4'][counter])
    elif 'Toolkit primary outcome' in df['out_type_5'][counter]:
        toolkit_prim.append(df['out_type_5'][counter])
        toolkit_prim_smd.append(df['smd_5'][counter])
        toolkit_prim_se.append(df['se_5'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_5'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_5'][counter])
        toolkit_prim_outcome.append(df['out_label_5'][counter])
        toolkit_prim_sample.append(df['out_samp_5'][counter])
        toolkit_prim_outcomp.append(df['out_comp_5'][counter])
        toolkit_es_type.append(df['out_es_type_5'][counter])
        toolkit_out_measure.append(df['out_measure_5'][counter])
        toolkit_out_strand.append(df['out_strand_5'][counter])
        toolkit_out_tit.append(df['out_tit_5'][counter])
        toolkit_g1_n.append(df['out_g1_n_5'][counter])
        toolkit_g2_n.append(df['out_g2_n_5'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_5'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_5'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_5'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_5'][counter])
        toolkit_out_desc.append(df['out_desc_5'][counter])
    elif 'Toolkit primary outcome' in df['out_type_6'][counter]:
        toolkit_prim.append(df['out_type_6'][counter])
        toolkit_prim_smd.append(df['smd_6'][counter])
        toolkit_prim_se.append(df['se_6'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_6'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_6'][counter])
        toolkit_prim_outcome.append(df['out_label_6'][counter])
        toolkit_prim_sample.append(df['out_samp_6'][counter])
        toolkit_prim_outcomp.append(df['out_comp_6'][counter])
        toolkit_es_type.append(df['out_es_type_6'][counter])
        toolkit_out_measure.append(df['out_measure_6'][counter])
        toolkit_out_strand.append(df['out_strand_6'][counter])
        toolkit_out_tit.append(df['out_tit_6'][counter])
        toolkit_g1_n.append(df['out_g1_n_6'][counter])
        toolkit_g2_n.append(df['out_g2_n_6'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_6'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_6'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_6'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_6'][counter])
        toolkit_out_desc.append(df['out_desc_6'][counter])
    elif 'Toolkit primary outcome' in df['out_type_7'][counter]:
        toolkit_prim.append(df['out_type_7'][counter])
        toolkit_prim_smd.append(df['smd_7'][counter])
        toolkit_prim_se.append(df['se_7'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_7'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_7'][counter])
        toolkit_prim_outcome.append(df['out_label_7'][counter])
        toolkit_prim_sample.append(df['out_samp_7'][counter])
        toolkit_prim_outcomp.append(df['out_comp_7'][counter])
        toolkit_es_type.append(df['out_es_type_7'][counter])
        toolkit_out_measure.append(df['out_measure_7'][counter])
        toolkit_out_strand.append(df['out_strand_7'][counter])
        toolkit_out_tit.append(df['out_tit_7'][counter])
        toolkit_g1_n.append(df['out_g1_n_7'][counter])
        toolkit_g2_n.append(df['out_g2_n_7'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_7'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_7'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_7'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_7'][counter])
        toolkit_out_desc.append(df['out_desc_7'][counter])
    elif 'Toolkit primary outcome' in df['out_type_8'][counter]:
        toolkit_prim.append(df['out_type_8'][counter])
        toolkit_prim_smd.append(df['smd_8'][counter])
        toolkit_prim_se.append(df['se_8'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_8'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_8'][counter])
        toolkit_prim_outcome.append(df['out_label_8'][counter])
        toolkit_prim_sample.append(df['out_samp_8'][counter])
        toolkit_prim_outcomp.append(df['out_comp_8'][counter])
        toolkit_es_type.append(df['out_es_type_8'][counter])
        toolkit_out_measure.append(df['out_measure_8'][counter])
        toolkit_out_strand.append(df['out_strand_8'][counter])
        toolkit_out_tit.append(df['out_tit_8'][counter])
        toolkit_g1_n.append(df['out_g1_n_8'][counter])
        toolkit_g2_n.append(df['out_g2_n_8'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_8'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_8'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_8'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_8'][counter])
        toolkit_out_desc.append(df['out_desc_8'][counter])
    elif 'Toolkit primary outcome' in df['out_type_9'][counter]:
        toolkit_prim.append(df['out_type_9'][counter])
        toolkit_prim_smd.append(df['smd_9'][counter])
        toolkit_prim_se.append(df['se_9'][counter])
        toolkit_prim_ci_lower.append(df['ci_lower_9'][counter])
        toolkit_prim_ci_upper.append(df['ci_upper_9'][counter])
        toolkit_prim_outcome.append(df['out_label_9'][counter])
        toolkit_prim_sample.append(df['out_samp_9'][counter])
        toolkit_prim_outcomp.append(df['out_comp_9'][counter])
        toolkit_es_type.append(df['out_es_type_9'][counter])
        toolkit_out_measure.append(df['out_measure_9'][counter])
        toolkit_out_strand.append(df['out_strand_9'][counter])
        toolkit_out_tit.append(df['out_tit_9'][counter])
        toolkit_g1_n.append(df['out_g1_n_9'][counter])
        toolkit_g2_n.append(df['out_g2_n_9'][counter])
        toolkit_g1_mean.append(df['out_g1_mean_9'][counter])
        toolkit_g2_mean.append(df['out_g2_mean_9'][counter])
        toolkit_g1_sd.append(df['out_g1_sd_9'][counter])
        toolkit_g2_sd.append(df['out_g2_sd_9'][counter])
        toolkit_out_desc.append(df['out_desc_9'][counter])



    else:
        toolkit_prim.append("NA")
        toolkit_prim_smd.append("NA")
        toolkit_prim_se.append("NA")
        toolkit_prim_ci_lower.append("NA")
        toolkit_prim_ci_upper.append("NA")
        toolkit_prim_outcome.append("NA")
        toolkit_prim_sample.append("NA")
        toolkit_prim_outcomp.append("NA")
        toolkit_es_type.append("NA")
        toolkit_out_measure.append("NA")
        toolkit_out_strand.append("NA")
        toolkit_out_tit.append("NA")
        toolkit_g1_n.append("NA")
        toolkit_g2_n.append("NA")
        toolkit_g1_mean.append("NA")
        toolkit_g2_mean.append("NA")
        toolkit_g1_sd.append("NA")
        toolkit_g2_sd.append("NA")
        toolkit_out_desc.append("NA")

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

for counter, row in enumerate(df['out_type_1']):
    if 'Reading primary outcome' in row:
        reading_prim.append(row)
        reading_prim_smd.append(df['smd_1'][counter])
        reading_prim_se.append(df['se_1'][counter])
        reading_prim_ci_lower.append(df['ci_lower_1'][counter])
        reading_prim_ci_upper.append(df['ci_upper_1'][counter])
        reading_prim_outcome.append(df['out_label_1'][counter])
        reading_prim_sample.append(df['out_samp_1'][counter])
        reading_prim_outcomp.append(df['out_comp_1'][counter])
        reading_prim_es_type.append(df['out_es_type_1'][counter])
        reading_prim_out_measure.append(df['out_measure_1'][counter])
        reading_prim_out_strand.append(df['out_strand_1'][counter])
        reading_prim_out_tit.append(df['out_tit_1'][counter])
        reading_prim_g1_n.append(df['out_g1_n_1'][counter])
        reading_prim_g2_n.append(df['out_g2_n_1'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_1'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_1'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_1'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_1'][counter])
        reading_prim_out_desc.append(df['out_desc_1'][counter])
    elif 'Reading primary outcome' in df['out_type_2'][counter]:
        reading_prim.append(df['out_type_2'][counter])
        reading_prim_smd.append(df['smd_2'][counter])
        reading_prim_se.append(df['se_2'][counter])
        reading_prim_ci_lower.append(df['ci_lower_2'][counter])
        reading_prim_ci_upper.append(df['ci_upper_2'][counter])
        reading_prim_outcome.append(df['out_label_2'][counter])
        reading_prim_sample.append(df['out_samp_2'][counter])
        reading_prim_outcomp.append(df['out_comp_2'][counter])
        reading_prim_es_type.append(df['out_es_type_2'][counter])
        reading_prim_out_measure.append(df['out_measure_2'][counter])
        reading_prim_out_strand.append(df['out_strand_2'][counter])
        reading_prim_out_tit.append(df['out_tit_2'][counter])
        reading_prim_g1_n.append(df['out_g1_n_2'][counter])
        reading_prim_g2_n.append(df['out_g2_n_2'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_2'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_2'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_2'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_2'][counter])
        reading_prim_out_desc.append(df['out_desc_2'][counter])
    elif 'Reading primary outcome' in df['out_type_3'][counter]:
        reading_prim.append(df['out_type_3'][counter])
        reading_prim_smd.append(df['smd_3'][counter])
        reading_prim_se.append(df['se_3'][counter])
        reading_prim_ci_lower.append(df['ci_lower_3'][counter])
        reading_prim_ci_upper.append(df['ci_upper_3'][counter])
        reading_prim_outcome.append(df['out_label_3'][counter])
        reading_prim_sample.append(df['out_samp_3'][counter])
        reading_prim_outcomp.append(df['out_comp_3'][counter])
        reading_prim_es_type.append(df['out_es_type_3'][counter])
        reading_prim_out_measure.append(df['out_measure_3'][counter])
        reading_prim_out_strand.append(df['out_strand_3'][counter])
        reading_prim_out_tit.append(df['out_tit_3'][counter])
        reading_prim_g1_n.append(df['out_g1_n_3'][counter])
        reading_prim_g2_n.append(df['out_g2_n_3'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_3'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_3'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_3'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_3'][counter])
        reading_prim_out_desc.append(df['out_desc_3'][counter])
    elif 'Reading primary outcome' in df['out_type_4'][counter]:
        reading_prim.append(df['out_type_4'][counter])
        reading_prim_smd.append(df['smd_4'][counter])
        reading_prim_se.append(df['se_4'][counter])
        reading_prim_ci_lower.append(df['ci_lower_4'][counter])
        reading_prim_ci_upper.append(df['ci_upper_4'][counter])
        reading_prim_outcome.append(df['out_label_4'][counter])
        reading_prim_sample.append(df['out_samp_4'][counter])
        reading_prim_outcomp.append(df['out_comp_4'][counter])
        reading_prim_es_type.append(df['out_es_type_4'][counter])
        reading_prim_out_measure.append(df['out_measure_4'][counter])
        reading_prim_out_strand.append(df['out_strand_4'][counter])
        reading_prim_out_tit.append(df['out_tit_4'][counter])
        reading_prim_g1_n.append(df['out_g1_n_4'][counter])
        reading_prim_g2_n.append(df['out_g2_n_4'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_4'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_4'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_4'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_4'][counter])
        reading_prim_out_desc.append(df['out_desc_4'][counter])
    elif 'Reading primary outcome' in df['out_type_5'][counter]:
        reading_prim.append(df['out_type_5'][counter])
        reading_prim_smd.append(df['smd_5'][counter])
        reading_prim_se.append(df['se_5'][counter])
        reading_prim_ci_lower.append(df['ci_lower_5'][counter])
        reading_prim_ci_upper.append(df['ci_upper_5'][counter])
        reading_prim_outcome.append(df['out_label_5'][counter])
        reading_prim_sample.append(df['out_samp_5'][counter])
        reading_prim_outcomp.append(df['out_comp_5'][counter])
        reading_prim_es_type.append(df['out_es_type_5'][counter])
        reading_prim_out_measure.append(df['out_measure_5'][counter])
        reading_prim_out_strand.append(df['out_strand_5'][counter])
        reading_prim_out_tit.append(df['out_tit_5'][counter])
        reading_prim_g1_n.append(df['out_g1_n_5'][counter])
        reading_prim_g2_n.append(df['out_g2_n_5'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_5'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_5'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_5'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_5'][counter])
        reading_prim_out_desc.append(df['out_desc_5'][counter])
    elif 'Reading primary outcome' in df['out_type_6'][counter]:
        reading_prim.append(df['out_type_6'][counter])
        reading_prim_smd.append(df['smd_6'][counter])
        reading_prim_se.append(df['se_6'][counter])
        reading_prim_ci_lower.append(df['ci_lower_6'][counter])
        reading_prim_ci_upper.append(df['ci_upper_6'][counter])
        reading_prim_outcome.append(df['out_label_6'][counter])
        reading_prim_sample.append(df['out_samp_6'][counter])
        reading_prim_outcomp.append(df['out_comp_6'][counter])
        reading_prim_es_type.append(df['out_es_type_6'][counter])
        reading_prim_out_measure.append(df['out_measure_6'][counter])
        reading_prim_out_strand.append(df['out_strand_6'][counter])
        reading_prim_out_tit.append(df['out_tit_6'][counter])
        reading_prim_g1_n.append(df['out_g1_n_6'][counter])
        reading_prim_g2_n.append(df['out_g2_n_6'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_6'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_6'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_6'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_6'][counter])
        reading_prim_out_desc.append(df['out_desc_6'][counter])
    elif 'Reading primary outcome' in df['out_type_7'][counter]:
        reading_prim.append(df['out_type_7'][counter])
        reading_prim_smd.append(df['smd_7'][counter])
        reading_prim_se.append(df['se_7'][counter])
        reading_prim_ci_lower.append(df['ci_lower_7'][counter])
        reading_prim_ci_upper.append(df['ci_upper_7'][counter])
        reading_prim_outcome.append(df['out_label_7'][counter])
        reading_prim_sample.append(df['out_samp_7'][counter])
        reading_prim_outcomp.append(df['out_comp_7'][counter])
        reading_prim_es_type.append(df['out_es_type_7'][counter])
        reading_prim_out_measure.append(df['out_measure_7'][counter])
        reading_prim_out_strand.append(df['out_strand_7'][counter])
        reading_prim_out_tit.append(df['out_tit_7'][counter])
        reading_prim_g1_n.append(df['out_g1_n_7'][counter])
        reading_prim_g2_n.append(df['out_g2_n_7'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_7'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_7'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_7'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_7'][counter])
        reading_prim_out_desc.append(df['out_desc_7'][counter])
    elif 'Reading primary outcome' in df['out_type_8'][counter]:
        reading_prim.append(df['out_type_8'][counter])
        reading_prim_smd.append(df['smd_8'][counter])
        reading_prim_se.append(df['se_8'][counter])
        reading_prim_ci_lower.append(df['ci_lower_8'][counter])
        reading_prim_ci_upper.append(df['ci_upper_8'][counter])
        reading_prim_outcome.append(df['out_label_8'][counter])
        reading_prim_sample.append(df['out_samp_8'][counter])
        reading_prim_outcomp.append(df['out_comp_8'][counter])
        reading_prim_es_type.append(df['out_es_type_8'][counter])
        reading_prim_out_measure.append(df['out_measure_8'][counter])
        reading_prim_out_strand.append(df['out_strand_8'][counter])
        reading_prim_out_tit.append(df['out_tit_8'][counter])
        reading_prim_g1_n.append(df['out_g1_n_8'][counter])
        reading_prim_g2_n.append(df['out_g2_n_8'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_8'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_8'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_8'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_8'][counter])
        reading_prim_out_desc.append(df['out_desc_8'][counter])
    elif 'Reading primary outcome' in df['out_type_9'][counter]:
        reading_prim.append(df['out_type_9'][counter])
        reading_prim_smd.append(df['smd_9'][counter])
        reading_prim_se.append(df['se_9'][counter])
        reading_prim_ci_lower.append(df['ci_lower_9'][counter])
        reading_prim_ci_upper.append(df['ci_upper_9'][counter])
        reading_prim_outcome.append(df['out_label_9'][counter])
        reading_prim_sample.append(df['out_samp_9'][counter])
        reading_prim_outcomp.append(df['out_comp_9'][counter])
        reading_prim_es_type.append(df['out_es_type_9'][counter])
        reading_prim_out_measure.append(df['out_measure_9'][counter])
        reading_prim_out_strand.append(df['out_strand_9'][counter])
        reading_prim_out_tit.append(df['out_tit_9'][counter])
        reading_prim_g1_n.append(df['out_g1_n_9'][counter])
        reading_prim_g2_n.append(df['out_g2_n_9'][counter])
        reading_prim_g1_mean.append(df['out_g1_mean_9'][counter])
        reading_prim_g2_mean.append(df['out_g2_mean_9'][counter])
        reading_prim_g1_sd.append(df['out_g1_sd_9'][counter])
        reading_prim_g2_sd.append(df['out_g2_sd_9'][counter])
        reading_prim_out_desc.append(df['out_desc_9'][counter])



    else:
        reading_prim.append("NA")
        reading_prim_smd.append("NA")
        reading_prim_se.append("NA")
        reading_prim_ci_lower.append("NA")
        reading_prim_ci_upper.append("NA")
        reading_prim_outcome.append("NA")
        reading_prim_sample.append("NA")
        reading_prim_outcomp.append("NA")
        reading_prim_es_type.append("NA")
        reading_prim_out_measure.append("NA")
        reading_prim_out_strand.append("NA")
        reading_prim_out_tit.append("NA")
        reading_prim_g1_n.append("NA")
        reading_prim_g2_n.append("NA")
        reading_prim_g1_mean.append("NA")
        reading_prim_g2_mean.append("NA")
        reading_prim_g1_sd.append("NA")
        reading_prim_g2_sd.append("NA")
        reading_prim_out_desc.append("NA")

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

for counter, row in enumerate(df['out_type_1']):
    if 'Writing and spelling primary outcome' in row:
        Writing_and_spelling_prim.append(df['out_type_1'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_1'][counter])
        Writing_and_spelling_prim_se.append(df['se_1'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_1'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_1'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_1'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_1'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_1'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_1'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_1'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_1'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_1'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_1'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_1'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_1'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_1'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_1'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_1'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_1'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_2'][counter]:
        Writing_and_spelling_prim.append(df['out_type_2'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_2'][counter])
        Writing_and_spelling_prim_se.append(df['se_2'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_2'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_2'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_2'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_2'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_2'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_2'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_2'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_2'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_2'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_2'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_2'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_2'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_2'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_2'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_2'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_2'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_3'][counter]:
        Writing_and_spelling_prim.append(df['out_type_3'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_3'][counter])
        Writing_and_spelling_prim_se.append(df['se_3'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_3'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_3'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_3'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_3'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_3'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_3'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_3'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_3'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_3'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_3'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_3'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_3'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_3'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_3'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_3'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_3'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_4'][counter]:
        Writing_and_spelling_prim.append(df['out_type_4'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_4'][counter])
        Writing_and_spelling_prim_se.append(df['se_4'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_4'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_4'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_4'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_4'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_4'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_4'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_4'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_4'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_4'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_4'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_4'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_4'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_4'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_4'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_4'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_4'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_5'][counter]:
        Writing_and_spelling_prim.append(df['out_type_5'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_5'][counter])
        Writing_and_spelling_prim_se.append(df['se_5'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_5'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_5'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_5'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_5'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_5'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_5'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_5'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_5'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_5'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_5'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_5'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_5'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_5'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_5'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_5'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_5'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_6'][counter]:
        Writing_and_spelling_prim.append(df['out_type_6'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_6'][counter])
        Writing_and_spelling_prim_se.append(df['se_6'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_6'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_6'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_6'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_6'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_6'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_6'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_6'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_6'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_6'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_6'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_6'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_6'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_6'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_6'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_6'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_6'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_7'][counter]:
        Writing_and_spelling_prim.append(df['out_type_7'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_7'][counter])
        Writing_and_spelling_prim_se.append(df['se_7'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_7'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_7'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_7'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_7'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_7'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_7'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_7'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_7'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_7'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_7'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_7'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_7'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_7'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_7'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_7'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_7'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_8'][counter]:
        Writing_and_spelling_prim.append(df['out_type_8'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_8'][counter])
        Writing_and_spelling_prim_se.append(df['se_8'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_8'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_8'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_8'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_8'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_8'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_8'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_8'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_8'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_8'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_8'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_8'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_8'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_8'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_8'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_8'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_8'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_9'][counter]:
        Writing_and_spelling_prim.append(df['out_type_9'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_9'][counter])
        Writing_and_spelling_prim_se.append(df['se_9'][counter])
        Writing_and_spelling_prim_ci_lower.append(df['ci_lower_9'][counter])
        Writing_and_spelling_prim_ci_upper.append(df['ci_upper_9'][counter])
        Writing_and_spelling_prim_outcome.append(df['out_label_9'][counter])
        Writing_and_spelling_prim_sample.append(df['out_samp_9'][counter])
        Writing_and_spelling_prim_outcomp.append(df['out_comp_9'][counter])
        Writing_and_spelling_prim_es_type.append(df['out_es_type_9'][counter])
        Writing_and_spelling_prim_out_measure.append(df['out_measure_9'][counter])
        Writing_and_spelling_prim_out_strand.append(df['out_strand_9'][counter])
        Writing_and_spelling_prim_out_tit.append(df['out_tit_9'][counter])
        Writing_and_spelling_prim_g1_n.append(df['out_g1_n_9'][counter])
        Writing_and_spelling_prim_g2_n.append(df['out_g2_n_9'][counter])
        Writing_and_spelling_prim_g1_mean.append(df['out_g1_mean_9'][counter])
        Writing_and_spelling_prim_g2_mean.append(df['out_g2_mean_9'][counter])
        Writing_and_spelling_prim_g1_sd.append(df['out_g1_sd_9'][counter])
        Writing_and_spelling_prim_g2_sd.append(df['out_g2_sd_9'][counter])
        Writing_and_spelling_prim_out_desc.append(df['out_desc_9'][counter])



    else:
        Writing_and_spelling_prim.append("NA")
        Writing_and_spelling_prim_smd.append("NA")
        Writing_and_spelling_prim_se.append("NA")
        Writing_and_spelling_prim_ci_lower.append("NA")
        Writing_and_spelling_prim_ci_upper.append("NA")
        Writing_and_spelling_prim_outcome.append("NA")
        Writing_and_spelling_prim_sample.append("NA")
        Writing_and_spelling_prim_outcomp.append("NA")
        Writing_and_spelling_prim_es_type.append("NA")
        Writing_and_spelling_prim_out_measure.append("NA")
        Writing_and_spelling_prim_out_strand.append("NA")
        Writing_and_spelling_prim_out_tit.append("NA")
        Writing_and_spelling_prim_g1_n.append("NA")
        Writing_and_spelling_prim_g2_n.append("NA")
        Writing_and_spelling_prim_g1_mean.append("NA")
        Writing_and_spelling_prim_g2_mean.append("NA")
        Writing_and_spelling_prim_g1_sd.append("NA")
        Writing_and_spelling_prim_g2_sd.append("NA")
        Writing_and_spelling_prim_out_desc.append("NA")

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

for counter, row in enumerate(df['out_type_1']):
    if 'Mathematics primary outcome' in row:
        Mathematics_prim.append(row)
        Mathematics_prim_smd.append(df['smd_1'][counter])
        Mathematics_prim_se.append(df['se_1'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_1'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_1'][counter])
        Mathematics_prim_outcome.append(df['out_label_1'][counter])
        Mathematics_prim_sample.append(df['out_samp_1'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_1'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_1'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_1'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_1'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_1'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_1'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_1'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_1'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_1'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_1'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_1'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_1'][counter])
    elif 'Mathematics primary outcome' in df['out_type_2'][counter]:
        Mathematics_prim.append(df['out_type_2'][counter])
        Mathematics_prim_smd.append(df['smd_2'][counter])
        Mathematics_prim_se.append(df['se_2'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_2'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_2'][counter])
        Mathematics_prim_outcome.append(df['out_label_2'][counter])
        Mathematics_prim_sample.append(df['out_samp_2'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_2'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_2'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_2'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_2'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_2'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_2'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_2'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_2'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_2'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_2'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_2'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_2'][counter])
    elif 'Mathematics primary outcome' in df['out_type_3'][counter]:
        Mathematics_prim.append(df['out_type_3'][counter])
        Mathematics_prim_smd.append(df['smd_3'][counter])
        Mathematics_prim_se.append(df['se_3'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_3'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_3'][counter])
        Mathematics_prim_outcome.append(df['out_label_3'][counter])
        Mathematics_prim_sample.append(df['out_samp_3'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_3'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_3'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_3'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_3'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_3'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_3'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_3'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_3'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_3'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_3'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_3'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_3'][counter])
    elif 'Mathematics primary outcome' in df['out_type_4'][counter]:
        Mathematics_prim.append(df['out_type_4'][counter])
        Mathematics_prim_smd.append(df['smd_4'][counter])
        Mathematics_prim_se.append(df['se_4'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_4'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_4'][counter])
        Mathematics_prim_outcome.append(df['out_label_4'][counter])
        Mathematics_prim_sample.append(df['out_samp_4'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_4'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_4'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_4'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_4'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_4'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_4'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_4'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_4'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_4'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_4'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_4'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_4'][counter])
    elif 'Mathematics primary outcome' in df['out_type_5'][counter]:
        Mathematics_prim.append(df['out_type_5'][counter])
        Mathematics_prim_smd.append(df['smd_5'][counter])
        Mathematics_prim_se.append(df['se_5'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_5'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_5'][counter])
        Mathematics_prim_outcome.append(df['out_label_5'][counter])
        Mathematics_prim_sample.append(df['out_samp_5'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_5'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_5'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_5'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_5'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_5'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_5'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_5'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_5'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_5'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_5'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_5'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_5'][counter])
    elif 'Mathematics primary outcome' in df['out_type_6'][counter]:
        Mathematics_prim.append(df['out_type_6'][counter])
        Mathematics_prim_smd.append(df['smd_6'][counter])
        Mathematics_prim_se.append(df['se_6'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_6'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_6'][counter])
        Mathematics_prim_outcome.append(df['out_label_6'][counter])
        Mathematics_prim_sample.append(df['out_samp_6'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_6'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_6'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_6'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_6'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_6'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_6'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_6'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_6'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_6'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_6'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_6'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_6'][counter])
    elif 'Mathematics primary outcome' in df['out_type_7'][counter]:
        Mathematics_prim.append(df['out_type_7'][counter])
        Mathematics_prim_smd.append(df['smd_7'][counter])
        Mathematics_prim_se.append(df['se_7'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_7'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_7'][counter])
        Mathematics_prim_outcome.append(df['out_label_7'][counter])
        Mathematics_prim_sample.append(df['out_samp_7'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_7'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_7'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_7'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_7'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_7'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_7'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_7'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_7'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_7'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_7'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_7'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_7'][counter])
    elif 'Mathematics primary outcome' in df['out_type_8'][counter]:
        Mathematics_prim.append(df['out_type_8'][counter])
        Mathematics_prim_smd.append(df['smd_8'][counter])
        Mathematics_prim_se.append(df['se_8'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_8'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_8'][counter])
        Mathematics_prim_outcome.append(df['out_label_8'][counter])
        Mathematics_prim_sample.append(df['out_samp_8'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_8'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_8'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_8'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_8'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_8'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_8'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_8'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_8'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_8'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_8'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_8'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_8'][counter])
    elif 'Mathematics primary outcome' in df['out_type_9'][counter]:
        Mathematics_prim.append(df['out_type_9'][counter])
        Mathematics_prim_smd.append(df['smd_9'][counter])
        Mathematics_prim_se.append(df['se_9'][counter])
        Mathematics_prim_ci_lower.append(df['ci_lower_9'][counter])
        Mathematics_prim_ci_upper.append(df['ci_upper_9'][counter])
        Mathematics_prim_outcome.append(df['out_label_9'][counter])
        Mathematics_prim_sample.append(df['out_samp_9'][counter])
        Mathematics_prim_outcomp.append(df['out_comp_9'][counter])
        Mathematics_prim_es_type.append(df['out_es_type_9'][counter])
        Mathematics_prim_out_measure.append(df['out_measure_9'][counter])
        Mathematics_prim_out_strand.append(df['out_strand_9'][counter])
        Mathematics_prim_out_tit.append(df['out_tit_9'][counter])
        Mathematics_prim_g1_n.append(df['out_g1_n_9'][counter])
        Mathematics_prim_g2_n.append(df['out_g2_n_9'][counter])
        Mathematics_prim_g1_mean.append(df['out_g1_mean_9'][counter])
        Mathematics_prim_g2_mean.append(df['out_g2_mean_9'][counter])
        Mathematics_prim_g1_sd.append(df['out_g1_sd_9'][counter])
        Mathematics_prim_g2_sd.append(df['out_g2_sd_9'][counter])
        Mathematics_prim_out_desc.append(df['out_desc_9'][counter])



    else:
        Mathematics_prim.append("NA")
        Mathematics_prim_smd.append("NA")
        Mathematics_prim_se.append("NA")
        Mathematics_prim_ci_lower.append("NA")
        Mathematics_prim_ci_upper.append("NA")
        Mathematics_prim_outcome.append("NA")
        Mathematics_prim_sample.append("NA")
        Mathematics_prim_outcomp.append("NA")
        Mathematics_prim_es_type.append("NA")
        Mathematics_prim_out_measure.append("NA")
        Mathematics_prim_out_strand.append("NA")
        Mathematics_prim_out_tit.append("NA")
        Mathematics_prim_g1_n.append("NA")
        Mathematics_prim_g2_n.append("NA")
        Mathematics_prim_g1_mean.append("NA")
        Mathematics_prim_g2_mean.append("NA")
        Mathematics_prim_g1_sd.append("NA")
        Mathematics_prim_g2_sd.append("NA")
        Mathematics_prim_out_desc.append("NA")

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

for counter, row in enumerate(df['out_type_1']):
    if 'Science primary outcome' in row:
        Science_prim.append(row)
        Science_prim_smd.append(df['smd_1'][counter])
        Science_prim_se.append(df['se_1'][counter])
        Science_prim_ci_lower.append(df['ci_lower_1'][counter])
        Science_prim_ci_upper.append(df['ci_upper_1'][counter])
        Science_prim_outcome.append(df['out_label_1'][counter])
        Science_prim_sample.append(df['out_samp_1'][counter])
        Science_prim_outcomp.append(df['out_comp_1'][counter])
        Science_prim_es_type.append(df['out_es_type_1'][counter])
        Science_prim_out_measure.append(df['out_measure_1'][counter])
        Science_prim_out_strand.append(df['out_strand_1'][counter])
        Science_prim_out_tit.append(df['out_tit_1'][counter])
        Science_prim_g1_n.append(df['out_g1_n_1'][counter])
        Science_prim_g2_n.append(df['out_g2_n_1'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_1'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_1'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_1'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_1'][counter])
        Science_prim_out_desc.append(df['out_desc_1'][counter])
    elif 'Science primary outcome' in df['out_type_2'][counter]:
        Science_prim.append(df['out_type_2'][counter])
        Science_prim_smd.append(df['smd_2'][counter])
        Science_prim_se.append(df['se_2'][counter])
        Science_prim_ci_lower.append(df['ci_lower_2'][counter])
        Science_prim_ci_upper.append(df['ci_upper_2'][counter])
        Science_prim_outcome.append(df['out_label_2'][counter])
        Science_prim_sample.append(df['out_samp_2'][counter])
        Science_prim_outcomp.append(df['out_comp_2'][counter])
        Science_prim_es_type.append(df['out_es_type_2'][counter])
        Science_prim_out_measure.append(df['out_measure_2'][counter])
        Science_prim_out_strand.append(df['out_strand_2'][counter])
        Science_prim_out_tit.append(df['out_tit_2'][counter])
        Science_prim_g1_n.append(df['out_g1_n_2'][counter])
        Science_prim_g2_n.append(df['out_g2_n_2'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_2'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_2'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_2'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_2'][counter])
        Science_prim_out_desc.append(df['out_desc_2'][counter])
    elif 'Science primary outcome' in df['out_type_3'][counter]:
        Science_prim.append(df['out_type_3'][counter])
        Science_prim_smd.append(df['smd_3'][counter])
        Science_prim_se.append(df['se_3'][counter])
        Science_prim_ci_lower.append(df['ci_lower_3'][counter])
        Science_prim_ci_upper.append(df['ci_upper_3'][counter])
        Science_prim_outcome.append(df['out_label_3'][counter])
        Science_prim_sample.append(df['out_samp_3'][counter])
        Science_prim_outcomp.append(df['out_comp_3'][counter])
        Science_prim_es_type.append(df['out_es_type_3'][counter])
        Science_prim_out_measure.append(df['out_measure_3'][counter])
        Science_prim_out_strand.append(df['out_strand_3'][counter])
        Science_prim_out_tit.append(df['out_tit_3'][counter])
        Science_prim_g1_n.append(df['out_g1_n_3'][counter])
        Science_prim_g2_n.append(df['out_g2_n_3'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_3'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_3'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_3'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_3'][counter])
        Science_prim_out_desc.append(df['out_desc_3'][counter])
    elif 'Science primary outcome' in df['out_type_4'][counter]:
        Science_prim.append(df['out_type_4'][counter])
        Science_prim_smd.append(df['smd_4'][counter])
        Science_prim_se.append(df['se_4'][counter])
        Science_prim_ci_lower.append(df['ci_lower_4'][counter])
        Science_prim_ci_upper.append(df['ci_upper_4'][counter])
        Science_prim_outcome.append(df['out_label_4'][counter])
        Science_prim_sample.append(df['out_samp_4'][counter])
        Science_prim_outcomp.append(df['out_comp_4'][counter])
        Science_prim_es_type.append(df['out_es_type_4'][counter])
        Science_prim_out_measure.append(df['out_measure_4'][counter])
        Science_prim_out_strand.append(df['out_strand_4'][counter])
        Science_prim_out_tit.append(df['out_tit_4'][counter])
        Science_prim_g1_n.append(df['out_g1_n_4'][counter])
        Science_prim_g2_n.append(df['out_g2_n_4'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_4'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_4'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_4'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_4'][counter])
        Science_prim_out_desc.append(df['out_desc_4'][counter])
    elif 'Science primary outcome' in df['out_type_5'][counter]:
        Science_prim.append(df['out_type_5'][counter])
        Science_prim_smd.append(df['smd_5'][counter])
        Science_prim_se.append(df['se_5'][counter])
        Science_prim_ci_lower.append(df['ci_lower_5'][counter])
        Science_prim_ci_upper.append(df['ci_upper_5'][counter])
        Science_prim_outcome.append(df['out_label_5'][counter])
        Science_prim_sample.append(df['out_samp_5'][counter])
        Science_prim_outcomp.append(df['out_comp_5'][counter])
        Science_prim_es_type.append(df['out_es_type_5'][counter])
        Science_prim_out_measure.append(df['out_measure_5'][counter])
        Science_prim_out_strand.append(df['out_strand_5'][counter])
        Science_prim_out_tit.append(df['out_tit_5'][counter])
        Science_prim_g1_n.append(df['out_g1_n_5'][counter])
        Science_prim_g2_n.append(df['out_g2_n_5'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_5'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_5'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_5'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_5'][counter])
        Science_prim_out_desc.append(df['out_desc_5'][counter])
    elif 'Science primary outcome' in df['out_type_6'][counter]:
        Science_prim.append(df['out_type_6'][counter])
        Science_prim_smd.append(df['smd_6'][counter])
        Science_prim_se.append(df['se_6'][counter])
        Science_prim_ci_lower.append(df['ci_lower_6'][counter])
        Science_prim_ci_upper.append(df['ci_upper_6'][counter])
        Science_prim_outcome.append(df['out_label_6'][counter])
        Science_prim_sample.append(df['out_samp_6'][counter])
        Science_prim_outcomp.append(df['out_comp_6'][counter])
        Science_prim_es_type.append(df['out_es_type_6'][counter])
        Science_prim_out_measure.append(df['out_measure_6'][counter])
        Science_prim_out_strand.append(df['out_strand_6'][counter])
        Science_prim_out_tit.append(df['out_tit_6'][counter])
        Science_prim_g1_n.append(df['out_g1_n_6'][counter])
        Science_prim_g2_n.append(df['out_g2_n_6'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_6'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_6'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_6'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_6'][counter])
        Science_prim_out_desc.append(df['out_desc_6'][counter])
    elif 'Science primary outcome' in df['out_type_7'][counter]:
        Science_prim.append(df['out_type_7'][counter])
        Science_prim_smd.append(df['smd_7'][counter])
        Science_prim_se.append(df['se_7'][counter])
        Science_prim_ci_lower.append(df['ci_lower_7'][counter])
        Science_prim_ci_upper.append(df['ci_upper_7'][counter])
        Science_prim_outcome.append(df['out_label_7'][counter])
        Science_prim_sample.append(df['out_samp_7'][counter])
        Science_prim_outcomp.append(df['out_comp_7'][counter])
        Science_prim_es_type.append(df['out_es_type_7'][counter])
        Science_prim_out_measure.append(df['out_measure_7'][counter])
        Science_prim_out_strand.append(df['out_strand_7'][counter])
        Science_prim_out_tit.append(df['out_tit_7'][counter])
        Science_prim_g1_n.append(df['out_g1_n_7'][counter])
        Science_prim_g2_n.append(df['out_g2_n_7'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_7'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_7'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_7'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_7'][counter])
        Science_prim_out_desc.append(df['out_desc_7'][counter])
    elif 'Science primary outcome' in df['out_type_8'][counter]:
        Science_prim.append(df['out_type_8'][counter])
        Science_prim_smd.append(df['smd_8'][counter])
        Science_prim_se.append(df['se_8'][counter])
        Science_prim_ci_lower.append(df['ci_lower_8'][counter])
        Science_prim_ci_upper.append(df['ci_upper_8'][counter])
        Science_prim_outcome.append(df['out_label_8'][counter])
        Science_prim_sample.append(df['out_samp_8'][counter])
        Science_prim_outcomp.append(df['out_comp_8'][counter])
        Science_prim_es_type.append(df['out_es_type_8'][counter])
        Science_prim_out_measure.append(df['out_measure_8'][counter])
        Science_prim_out_strand.append(df['out_strand_8'][counter])
        Science_prim_out_tit.append(df['out_tit_8'][counter])
        Science_prim_g1_n.append(df['out_g1_n_8'][counter])
        Science_prim_g2_n.append(df['out_g2_n_8'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_8'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_8'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_8'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_8'][counter])
        Science_prim_out_desc.append(df['out_desc_8'][counter])
    elif 'Science primary outcome' in df['out_type_9'][counter]:
        Science_prim.append(df['out_type_9'][counter])
        Science_prim_smd.append(df['smd_9'][counter])
        Science_prim_se.append(df['se_9'][counter])
        Science_prim_ci_lower.append(df['ci_lower_9'][counter])
        Science_prim_ci_upper.append(df['ci_upper_9'][counter])
        Science_prim_outcome.append(df['out_label_9'][counter])
        Science_prim_sample.append(df['out_samp_9'][counter])
        Science_prim_outcomp.append(df['out_comp_9'][counter])
        Science_prim_es_type.append(df['out_es_type_9'][counter])
        Science_prim_out_measure.append(df['out_measure_9'][counter])
        Science_prim_out_strand.append(df['out_strand_9'][counter])
        Science_prim_out_tit.append(df['out_tit_9'][counter])
        Science_prim_g1_n.append(df['out_g1_n_9'][counter])
        Science_prim_g2_n.append(df['out_g2_n_9'][counter])
        Science_prim_g1_mean.append(df['out_g1_mean_9'][counter])
        Science_prim_g2_mean.append(df['out_g2_mean_9'][counter])
        Science_prim_g1_sd.append(df['out_g1_sd_9'][counter])
        Science_prim_g2_sd.append(df['out_g2_sd_9'][counter])
        Science_prim_out_desc.append(df['out_desc_9'][counter])



    else:
        Science_prim.append("NA")
        Science_prim_smd.append("NA")
        Science_prim_se.append("NA")
        Science_prim_ci_lower.append("NA")
        Science_prim_ci_upper.append("NA")
        Science_prim_outcome.append("NA")
        Science_prim_sample.append("NA")
        Science_prim_outcomp.append("NA")
        Science_prim_es_type.append("NA")
        Science_prim_out_measure.append("NA")
        Science_prim_out_strand.append("NA")
        Science_prim_out_tit.append("NA")
        Science_prim_g1_n.append("NA")
        Science_prim_g2_n.append("NA")
        Science_prim_g1_mean.append("NA")
        Science_prim_g2_mean.append("NA")
        Science_prim_g1_sd.append("NA")
        Science_prim_g2_sd.append("NA")
        Science_prim_out_desc.append("NA")

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

for counter, row in enumerate(df['out_type_1']):
    if 'SES/FSM outcome' in row:
        FSM_prim.append(row)
        FSM_prim_smd.append(df['smd_1'][counter])
        FSM_prim_se.append(df['se_1'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_1'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_1'][counter])
        FSM_prim_outcome.append(df['out_label_1'][counter])
        FSM_prim_sample.append(df['out_samp_1'][counter])
        FSM_prim_outcomp.append(df['out_comp_1'][counter])
        FSM_prim_es_type.append(df['out_es_type_1'][counter])
        FSM_prim_out_measure.append(df['out_measure_1'][counter])
        FSM_prim_out_strand.append(df['out_strand_1'][counter])
        FSM_prim_out_tit.append(df['out_tit_1'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_1'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_1'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_1'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_1'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_1'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_1'][counter])
        FSM_prim_out_desc.append(df['out_desc_1'][counter])
    elif 'SES/FSM outcome' in df['out_type_2'][counter]:
        FSM_prim.append(df['out_type_2'][counter])
        FSM_prim_smd.append(df['smd_2'][counter])
        FSM_prim_se.append(df['se_2'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_2'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_2'][counter])
        FSM_prim_outcome.append(df['out_label_2'][counter])
        FSM_prim_sample.append(df['out_samp_2'][counter])
        FSM_prim_outcomp.append(df['out_comp_2'][counter])
        FSM_prim_es_type.append(df['out_es_type_2'][counter])
        FSM_prim_out_measure.append(df['out_measure_2'][counter])
        FSM_prim_out_strand.append(df['out_strand_2'][counter])
        FSM_prim_out_tit.append(df['out_tit_2'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_2'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_2'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_2'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_2'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_2'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_2'][counter])
        FSM_prim_out_desc.append(df['out_desc_2'][counter])
    elif 'SES/FSM outcome' in df['out_type_3'][counter]:
        FSM_prim.append(df['out_type_3'][counter])
        FSM_prim_smd.append(df['smd_3'][counter])
        FSM_prim_se.append(df['se_3'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_3'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_3'][counter])
        FSM_prim_outcome.append(df['out_label_3'][counter])
        FSM_prim_sample.append(df['out_samp_3'][counter])
        FSM_prim_outcomp.append(df['out_comp_3'][counter])
        FSM_prim_es_type.append(df['out_es_type_3'][counter])
        FSM_prim_out_measure.append(df['out_measure_3'][counter])
        FSM_prim_out_strand.append(df['out_strand_3'][counter])
        FSM_prim_out_tit.append(df['out_tit_3'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_3'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_3'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_3'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_3'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_3'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_3'][counter])
        FSM_prim_out_desc.append(df['out_desc_3'][counter])
    elif 'SES/FSM outcome' in df['out_type_4'][counter]:
        FSM_prim.append(df['out_type_4'][counter])
        FSM_prim_smd.append(df['smd_4'][counter])
        FSM_prim_se.append(df['se_4'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_4'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_4'][counter])
        FSM_prim_outcome.append(df['out_label_4'][counter])
        FSM_prim_sample.append(df['out_samp_4'][counter])
        FSM_prim_outcomp.append(df['out_comp_4'][counter])
        FSM_prim_es_type.append(df['out_es_type_4'][counter])
        FSM_prim_out_measure.append(df['out_measure_4'][counter])
        FSM_prim_out_strand.append(df['out_strand_4'][counter])
        FSM_prim_out_tit.append(df['out_tit_4'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_4'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_4'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_4'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_4'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_4'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_4'][counter])
        FSM_prim_out_desc.append(df['out_desc_4'][counter])
    elif 'SES/FSM outcome' in df['out_type_5'][counter]:
        FSM_prim.append(df['out_type_5'][counter])
        FSM_prim_smd.append(df['smd_5'][counter])
        FSM_prim_se.append(df['se_5'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_5'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_5'][counter])
        FSM_prim_outcome.append(df['out_label_5'][counter])
        FSM_prim_sample.append(df['out_samp_5'][counter])
        FSM_prim_outcomp.append(df['out_comp_5'][counter])
        FSM_prim_es_type.append(df['out_es_type_5'][counter])
        FSM_prim_out_measure.append(df['out_measure_5'][counter])
        FSM_prim_out_strand.append(df['out_strand_5'][counter])
        FSM_prim_out_tit.append(df['out_tit_5'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_5'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_5'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_5'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_5'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_5'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_5'][counter])
        FSM_prim_out_desc.append(df['out_desc_5'][counter])
    elif 'SES/FSM outcome' in df['out_type_6'][counter]:
        FSM_prim.append(df['out_type_6'][counter])
        FSM_prim_smd.append(df['smd_6'][counter])
        FSM_prim_se.append(df['se_6'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_6'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_6'][counter])
        FSM_prim_outcome.append(df['out_label_6'][counter])
        FSM_prim_sample.append(df['out_samp_6'][counter])
        FSM_prim_outcomp.append(df['out_comp_6'][counter])
        FSM_prim_es_type.append(df['out_es_type_6'][counter])
        FSM_prim_out_measure.append(df['out_measure_6'][counter])
        FSM_prim_out_strand.append(df['out_strand_6'][counter])
        FSM_prim_out_tit.append(df['out_tit_6'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_6'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_6'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_6'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_6'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_6'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_6'][counter])
        FSM_prim_out_desc.append(df['out_desc_6'][counter])
    elif 'SES/FSM outcome' in df['out_type_7'][counter]:
        FSM_prim.append(df['out_type_7'][counter])
        FSM_prim_smd.append(df['smd_7'][counter])
        FSM_prim_se.append(df['se_7'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_7'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_7'][counter])
        FSM_prim_outcome.append(df['out_label_7'][counter])
        FSM_prim_sample.append(df['out_samp_7'][counter])
        FSM_prim_outcomp.append(df['out_comp_7'][counter])
        FSM_prim_es_type.append(df['out_es_type_7'][counter])
        FSM_prim_out_measure.append(df['out_measure_7'][counter])
        FSM_prim_out_strand.append(df['out_strand_7'][counter])
        FSM_prim_out_tit.append(df['out_tit_7'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_7'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_7'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_7'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_7'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_7'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_7'][counter])
        FSM_prim_out_desc.append(df['out_desc_7'][counter])
    elif 'SES/FSM outcome' in df['out_type_8'][counter]:
        FSM_prim.append(df['out_type_8'][counter])
        FSM_prim_smd.append(df['smd_8'][counter])
        FSM_prim_se.append(df['se_8'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_8'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_8'][counter])
        FSM_prim_outcome.append(df['out_label_8'][counter])
        FSM_prim_sample.append(df['out_samp_8'][counter])
        FSM_prim_outcomp.append(df['out_comp_8'][counter])
        FSM_prim_es_type.append(df['out_es_type_8'][counter])
        FSM_prim_out_measure.append(df['out_measure_8'][counter])
        FSM_prim_out_strand.append(df['out_strand_8'][counter])
        FSM_prim_out_tit.append(df['out_tit_8'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_8'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_8'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_8'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_8'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_8'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_8'][counter])
        FSM_prim_out_desc.append(df['out_desc_8'][counter])
    elif 'SES/FSM outcome' in df['out_type_9'][counter]:
        FSM_prim.append(df['out_type_9'][counter])
        FSM_prim_smd.append(df['smd_9'][counter])
        FSM_prim_se.append(df['se_9'][counter])
        FSM_prim_ci_lower.append(df['ci_lower_9'][counter])
        FSM_prim_ci_upper.append(df['ci_upper_9'][counter])
        FSM_prim_outcome.append(df['out_label_9'][counter])
        FSM_prim_sample.append(df['out_samp_9'][counter])
        FSM_prim_outcomp.append(df['out_comp_9'][counter])
        FSM_prim_es_type.append(df['out_es_type_9'][counter])
        FSM_prim_out_measure.append(df['out_measure_9'][counter])
        FSM_prim_out_strand.append(df['out_strand_9'][counter])
        FSM_prim_out_tit.append(df['out_tit_9'][counter])
        FSM_prim_g1_n.append(df['out_g1_n_9'][counter])
        FSM_prim_g2_n.append(df['out_g2_n_9'][counter])
        FSM_prim_g1_mean.append(df['out_g1_mean_9'][counter])
        FSM_prim_g2_mean.append(df['out_g2_mean_9'][counter])
        FSM_prim_g1_sd.append(df['out_g1_sd_9'][counter])
        FSM_prim_g2_sd.append(df['out_g2_sd_9'][counter])
        FSM_prim_out_desc.append(df['out_desc_9'][counter])



    else:
        FSM_prim.append("NA")
        FSM_prim_smd.append("NA")
        FSM_prim_se.append("NA")
        FSM_prim_ci_lower.append("NA")
        FSM_prim_ci_upper.append("NA")
        FSM_prim_outcome.append("NA")
        FSM_prim_sample.append("NA")
        FSM_prim_outcomp.append("NA")
        FSM_prim_es_type.append("NA")
        FSM_prim_out_measure.append("NA")
        FSM_prim_out_strand.append("NA")
        FSM_prim_out_tit.append("NA")
        FSM_prim_g1_n.append("NA")
        FSM_prim_g2_n.append("NA")
        FSM_prim_g1_mean.append("NA")
        FSM_prim_g2_mean.append("NA")
        FSM_prim_g1_sd.append("NA")
        FSM_prim_g2_sd.append("NA")
        FSM_prim_out_desc.append("NA")

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
outfile_name = outfile_name + "_Effect_Size_B.csv"

# write to disk
print("saving {}".format(outfile_name))
df.to_csv(outfile_name, index=False, header=True)