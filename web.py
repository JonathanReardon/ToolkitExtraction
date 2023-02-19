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
from src.Author import author_df
from src.Date import year_df
from src.Abstract import abstract_df
from src.AdminStrand import admin_strand_df
from src.OutcomeType import outcometype_df
from src.smd import smd_df
from src.sesmd import sesmd_df
from src.OutcomeDescription import outcome_description_df
from src.OutcomeTitle import outcome_title_df
from src.CIlowerSMD import cilowersmd_df
from src.CIupperSMD import ciuppersmd_df
from src.Sample import sample_df
from src.Outcome import outcome_df
from src.EffectSizeType import effectsizetype_df
from src.OutcomeComparison import out_comp_df
from src.OutcomeMeasure import outcome_measure_df
from src.Group1_N import group1N_df
from src.Group2_N import group2N_df
from src.Group1_Mean import group1mean_df
from src.Group2_Mean import group2mean_df
from src.Group1_SD import group1sd_df
from src.Group2_SD import group2sd_df
from src.TestType import testtype_outcome_df
from src.PublicationType_EPPI import pubtype_eppi_df
from src.PublicationType import publication_type_df
from src.Country import country_df
from src.EducationalSetting import educational_setting_df
from src.StudyRealism import study_realism_df
from src.Age import student_age
from src.Gender import gender_df
from src.NumberofSchools import number_of_schools_df
from src.NumberofClasses import number_of_classes_df
from src.TreatmentGroup import treatment_group_df
from src.ParticipantAssignment import participant_assignment_df
from src.LevelofAssignment import level_of_assignment_df
from src.StudyDesign import study_design_df
from src.Randomisation import randomisation_df
from src.Other_Outcomes import other_outcomes_df
from src.InterventionName import intervention_name_df
from src.InterventionDescription import intervention_description_df
from src.InterventionObjectives import intervention_objectives_df
from src.InterventionTrainingProvided import intervention_training_provided_df
from src.InterventionOrganizationType import intervention_org_type
from src.InterventionFocus import intervention_focus_df
from src.InterventionTeachingApproach import intervention_teaching_approach_df
from src.InterventionInclusion import intervention_inclusion_df
from src.InterventionTime import intervention_time_df
from src.InterventionDelivery import intervention_delivery_df
from src.InterventionDuration import intervention_duration_df
from src.InterventionFrequency import intervention_frequency_df
from src.InterventionSessionLength import intervention_session_length_df
from src.InterventionDetail import intervention_detail_df
from src.InterventionCostsReported import intervention_costs_df
from src.InterventionEvaluation import intervention_evaluation_df
from src.Baseline_Differences import baseline_differences_df
from src.Comparability import comparability_df
from src.Comparability_Variables_Reported import comparability_vars_reported_df
from src.Clustering import clustering_df
from src.ses_fsm import ses_fsm_df
from src.Sample_Size_Initial import initial_sample_size_df
from src.Sample_Size_Analyzed import analyzed_sample_size_df
from src.Attrition import attrition_df
from src.PrimaryOutcomeDescStatsReported import DescStatsOutcomeReported_df
from src.PrimaryOutcomeDescStatsInterventionGroup import DescStatsPrimaryOutcomeReported_Intervention_df
from src.PrimaryOutcomeDescStatsControlGroup import DescStatsPrimaryOutcomeReported_Control_df
from src.PrimaryOutcomeDescStatsInterventionGroup_TWO import DescStatsPrimaryOutcomeReported_Intervention_TWO_df
from src.PrimaryOutcomeDescStatsControlGroup_TWO import DescStatsPrimaryOutcomeReported_Control_TWO_df

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