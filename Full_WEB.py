from Main import load_json, get_metadata, get_data, get_outcome_lvl1, get_outcome_lvl2

# standard imports
import os
import sys
import pandas as pd

# local imports
from ind_var_Gen.Author import author_df
from ind_var_Gen.Date import year_df
from ind_var_Gen.Abstract import abstract_df
from ind_var_Gen.AdminStrand import admin_strand_df
from ind_var_Gen.OutcomeType import outcometype_df
from ind_var_Gen.smd import smd_df
from ind_var_Gen.sesmd import sesmd_df
from ind_var_Gen.OutcomeDescription import outcome_description_df
from ind_var_Gen.OutcomeTitle import outcome_title_df
from ind_var_Gen.CIlowerSMD import cilowersmd_df
from ind_var_Gen.CIupperSMD import ciuppersmd_df
from ind_var_Gen.Sample import sample_df
from ind_var_Gen.Outcome import outcome_df
from ind_var_Gen.EffectSizeType import effectsizetype_df
from ind_var_Gen.OutcomeComparison import out_comp_df
from ind_var_Gen.OutcomeMeasure import outcome_measure_df
from ind_var_Gen.Group1_N import group1N_df
from ind_var_Gen.Group2_N import group2N_df
from ind_var_Gen.Group1_Mean import group1mean_df
from ind_var_Gen.Group2_Mean import group2mean_df
from ind_var_Gen.Group1_SD import group1sd_df
from ind_var_Gen.Group2_SD import group2sd_df
from ind_var_Gen.TestType import testtype_outcome_df
from ind_var_Gen.PublicationType_EPPI import pubtype_eppi_df
from ind_var_Gen.PublicationType import publication_type_df
from ind_var_Gen.Country import country_df
from ind_var_Gen.EducationalSetting import educational_setting_df
from ind_var_Gen.StudyRealism import study_realism_df
from ind_var_Gen.Age import student_age
from ind_var_Gen.Gender import gender_df
from ind_var_Gen.NumberofSchools import number_of_schools_df
from ind_var_Gen.NumberofClasses import number_of_classes_df
from ind_var_Gen.TreatmentGroup import treatment_group_df
from ind_var_Gen.ParticipantAssignment import participant_assignment_df
from ind_var_Gen.LevelofAssignment import level_of_assignment_df
from ind_var_Gen.StudyDesign import study_design_df
from ind_var_Gen.Randomisation import randomisation_df
from ind_var_Gen.Other_Outcomes import other_outcomes_df
from ind_var_Gen.InterventionName import intervention_name_df
from ind_var_Gen.InterventionDescription import intervention_description_df
from ind_var_Gen.InterventionObjectives import intervention_objectives_df
from ind_var_Gen.InterventionTrainingProvided import intervention_training_provided_df
from ind_var_Gen.InterventionOrganizationType import intervention_org_type
from ind_var_Gen.InterventionFocus import intervention_focus_df
from ind_var_Gen.InterventionTeachingApproach import intervention_teaching_approach_df
from ind_var_Gen.InterventionInclusion import intervention_inclusion_df
from ind_var_Gen.InterventionTime import intervention_time_df
from ind_var_Gen.InterventionDelivery import intervention_delivery_df
from ind_var_Gen.InterventionDuration import intervention_duration_df
from ind_var_Gen.InterventionFrequency import intervention_frequency_df
from ind_var_Gen.InterventionSessionLength import intervention_session_length_df
from ind_var_Gen.InterventionDetail import intervention_detail_df
from ind_var_Gen.InterventionCostsReported import intervention_costs_df
from ind_var_Gen.InterventionEvaluation import intervention_evaluation_df
from ind_var_Gen.Baseline_Differences import baseline_differences_df
from ind_var_Gen.Comparability import comparability_df
from ind_var_Gen.Comparability_Variables_Reported import comparability_vars_reported_df
from ind_var_Gen.Clustering import clustering_df
from ind_var_Gen.ses_fsm import ses_fsm_df
from ind_var_Gen.Sample_Size_Initial import initial_sample_size_df
from ind_var_Gen.Sample_Size_Analyzed import analyzed_sample_size_df
from ind_var_Gen.Attrition import attrition_df
from ind_var_Gen.PrimaryOutcomeDescStatsReported import DescStatsOutcomeReported_df
from ind_var_Gen.PrimaryOutcomeDescStatsInterventionGroup import DescStatsPrimaryOutcomeReported_Intervention_df
from ind_var_Gen.PrimaryOutcomeDescStatsControlGroup import DescStatsPrimaryOutcomeReported_Control_df
from ind_var_Gen.PrimaryOutcomeDescStatsInterventionGroup_TWO import DescStatsPrimaryOutcomeReported_Intervention_TWO_df
from ind_var_Gen.PrimaryOutcomeDescStatsControlGroup_TWO import DescStatsPrimaryOutcomeReported_Control_TWO_df

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