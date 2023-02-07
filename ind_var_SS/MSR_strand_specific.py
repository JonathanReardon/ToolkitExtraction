from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import msr_knowl_type_output
from AttributeIDList import msr_task_stage_output
from AttributeIDList import msr_strategy_type_output
from AttributeIDList import msr_self_reg_mot_aspects_output
from AttributeIDList import msr_teaching_approach_output
from AttributeIDList import msr_digit_tech

import pandas as pd

load_json()

# METACOGNITION AND SELF REGULATION

# get msr knowledge type data
msr_knowl_type = get_data(msr_knowl_type_output)
msr_knowl_type_df = pd.DataFrame(msr_knowl_type)
msr_knowl_type_df = msr_knowl_type_df.T
msr_knowl_type_df.columns = ["msr_knowl_type"]

# get msr task stage data
msr_task_stage = get_data(msr_task_stage_output)
msr_task_stage_df = pd.DataFrame(msr_task_stage)
msr_task_stage_df = msr_task_stage_df.T
msr_task_stage_df.columns = ["msr_task_stage"]

# get msr strategy type data
msr_strategy = get_data(msr_strategy_type_output)
msr_strategy_df = pd.DataFrame(msr_strategy)
msr_strategy_df = msr_strategy_df.T
msr_strategy_df.columns = ["msr_strategy"]

# get msr motivational aspects data
msr_motiv_aspects = get_data(msr_self_reg_mot_aspects_output)
msr_motiv_aspects_df = pd.DataFrame(msr_motiv_aspects)
msr_motiv_aspects_df = msr_motiv_aspects_df.T
msr_motiv_aspects_df.columns = ["msr_motiv_aspects"]

# get msr teaching approach data
msr_teaching_approach = get_data(msr_teaching_approach_output)
msr_teaching_approach_df = pd.DataFrame(msr_teaching_approach)
msr_teaching_approach_df = msr_teaching_approach_df.T
msr_teaching_approach_df.columns = ["msr_teaching_approach"]

# get msr dig tech data
msr_digit_tech = get_data(msr_digit_tech)
msr_digit_tech_df = pd.DataFrame(msr_digit_tech)
msr_digit_tech_df = msr_digit_tech_df.T
msr_digit_tech_df.columns = ["msr_digit_tech"]

msr_ss_df = pd.concat([
    msr_knowl_type_df,
    msr_task_stage_df,
    msr_strategy_df,
    msr_motiv_aspects_df,
    msr_teaching_approach_df,
    msr_digit_tech_df
], axis=1, sort=False)

# fill blanks with NA
msr_ss_df.fillna("NA", inplace=True)

# save to disk
""" msr_ss_df.to_csv("metacog_self_reg_ss.csv", index=False) """