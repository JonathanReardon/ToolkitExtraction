#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Jonathan Reardon
"""

import os
import sys

# Third party imports
import os
import sys

# Local imports
from Main import load_json
from Main import get_metadata
from Main import get_data
from Main import get_outcome_lvl1
from Main import get_outcome_lvl2

# Local imports
from ind_var_functions.Author import author_df
from ind_var_functions.Date import year_df
from ind_var_functions.Abstract import abstract_df
from ind_var_functions.AdminStrand import admin_strand_df
from ind_var_functions.OutcomeType import outcometype_df
from ind_var_functions.smd import smd_df
from ind_var_functions.sesmd import sesmd_df
from ind_var_functions.OutcomeDescription import outcome_description_df
from ind_var_functions.OutcomeTitle import outcome_title_df
from ind_var_functions.CIlowerSMD import cilowersmd_df
from ind_var_functions.CIupperSMD import ciuppersmd_df
from ind_var_functions.Sample import sample_df
from ind_var_functions.Outcome import outcome_df
from ind_var_functions.EffectSizeType import effectsizetype_df
from ind_var_functions.OutcomeComparison import out_comp_df
from ind_var_functions.OutcomeMeasure import outcome_measure_df
from ind_var_functions.Group1_N import group1N_df
from ind_var_functions.Group2_N import group2N_df
from ind_var_functions.Group1_Mean import group1mean_df
from ind_var_functions.Group2_Mean import group2mean_df
from ind_var_functions.Group1_SD import group1sd_df
from ind_var_functions.Group2_SD import group2sd_df
from ind_var_functions.TestType import testtype_outcome_df
from ind_var_functions.PublicationType_EPPI import pubtype_eppi_df
from ind_var_functions.PublicationType import publication_type_df
from ind_var_functions.Country import country_df
from ind_var_functions.EducationalSetting import educational_setting_df
from ind_var_functions.StudyRealism import study_realism_df
from ind_var_functions.Age import student_age
from ind_var_functions.Gender import gender_df
from ind_var_functions.NumberofSchools import number_of_schools_df
from ind_var_functions.NumberofClasses import number_of_classes_df
from ind_var_functions.TreatmentGroup import treatment_group_df
from ind_var_functions.ParticipantAssignment import participant_assignment_df
from ind_var_functions.LevelofAssignment import level_of_assignment_df
from ind_var_functions.StudyDesign import study_design_df
from ind_var_functions.Randomisation import randomisation_df
from ind_var_functions.Other_Outcomes import other_outcomes_df
from ind_var_functions.InterventionName import intervention_name_df
from ind_var_functions.InterventionDescription import intervention_description_df
from ind_var_functions.InterventionObjectives import intervention_objectives_df
from ind_var_functions.InterventionTrainingProvided import intervention_training_provided_df
from ind_var_functions.InterventionOrganizationType import intervention_org_type
from ind_var_functions.InterventionFocus import intervention_focus_df
from ind_var_functions.InterventionTeachingApproach import intervention_teaching_approach_df
from ind_var_functions.InterventionInclusion import intervention_inclusion_df
from ind_var_functions.InterventionTime import intervention_time_df
from ind_var_functions.InterventionDelivery import intervention_delivery_df
from ind_var_functions.InterventionDuration import intervention_duration_df
from ind_var_functions.InterventionFrequency import intervention_frequency_df
from ind_var_functions.InterventionSessionLength import intervention_session_length_df
from ind_var_functions.InterventionDetail import intervention_detail_df
from ind_var_functions.InterventionCostsReported import intervention_costs_df
from ind_var_functions.InterventionEvaluation import intervention_evaluation_df
from ind_var_functions.Baseline_Differences import baseline_differences_df
from ind_var_functions.Comparability import comparability_df
from ind_var_functions.Comparability_Variables_Reported import comparability_vars_reported_df
from ind_var_functions.Clustering import clustering_df
from ind_var_functions.ses_fsm import ses_fsm_df
from ind_var_functions.Sample_Size_Initial import initial_sample_size_df
from ind_var_functions.Sample_Size_Analyzed import analyzed_sample_size_df
from ind_var_functions.Attrition import attrition_df
from ind_var_functions.PrimaryOutcomeDescStatsReported import DescStatsOutcomeReported_df
from ind_var_functions.PrimaryOutcomeDescStatsInterventionGroup import DescStatsPrimaryOutcomeReported_Intervention_df
from ind_var_functions.PrimaryOutcomeDescStatsControlGroup import DescStatsPrimaryOutcomeReported_Control_df
from ind_var_functions.PrimaryOutcomeDescStatsInterventionGroup_TWO import DescStatsPrimaryOutcomeReported_Intervention_TWO_df
from ind_var_functions.PrimaryOutcomeDescStatsControlGroup_TWO import DescStatsPrimaryOutcomeReported_Control_TWO_df

data_files = sys.argv[1]

all_variables = pd.concat([
    author_df,
    year_df,
    abstract_df,
    admin_strand_df,
    country_df,
    outcometype_df,
    smd_df,
    outcome_description_df,
    outcome_title_df,
    cilowersmd_df,
    ciuppersmd_df,
    sample_df,
    outcome_df,
    effectsizetype_df,
    out_comp_df,
    outcome_measure_df,
    group1N_df,
    group2N_df,
    group1mean_df,
    group2mean_df,
    group1sd_df,
    group2sd_df,
    testtype_outcome_df,
    pubtype_eppi_df,
    publication_type_df,
    educational_setting_df,
    study_realism_df,
    student_age,
    gender_df,
    number_of_schools_df,
    number_of_classes_df,
    treatment_group_df,
    participant_assignment_df,
    level_of_assignment_df,
    study_design_df,
    randomisation_df,
    other_outcomes_df,
    intervention_name_df,
    intervention_description_df,
    intervention_objectives_df,
    intervention_training_provided_df,
    intervention_org_type,
    intervention_focus_df,
    intervention_teaching_approach_df,
    intervention_inclusion_df,
    intervention_time_df,
    intervention_delivery_df,
    intervention_duration_df,
    intervention_frequency_df,
    intervention_session_length_df,
    intervention_detail_df,
    intervention_costs_df,
    intervention_evaluation_df,
    baseline_differences_df,
    comparability_df,
    comparability_vars_reported_df,
    clustering_df,
    ses_fsm_df,
    initial_sample_size_df,
    analyzed_sample_size_df,
    attrition_df,
    DescStatsOutcomeReported_df,
    DescStatsPrimaryOutcomeReported_Intervention_df,
    DescStatsPrimaryOutcomeReported_Control_df,
    DescStatsPrimaryOutcomeReported_Intervention_TWO_df,
    DescStatsPrimaryOutcomeReported_Control_TWO_df,
], axis=1, sort=False)

print(all_variables)