from Main import load_json, get_data, comments

from AttributeIDList import pp_incentive_criteria_output
from AttributeIDList import pp_reward_recipient_output
from AttributeIDList import pp_incentive_timing_output
from AttributeIDList import pp_incentive_type_output
from AttributeIDList import pp_incentive_amount_output
from AttributeIDList import pp_teacher_eval_period_output

import pandas as pd

load_json()

# PERFORMANCE PAY

# get incentive criteria data
pp_incent_crit = get_data(pp_incentive_criteria_output)
pp_incent_crit_df = pd.DataFrame(pp_incent_crit)
pp_incent_crit_df = pp_incent_crit_df.T
pp_incent_crit_df.columns = ["pp_incent_criteria"]

# get reward recipient data
pp_reward_recip = get_data(pp_reward_recipient_output)
pp_reward_recip_df = pd.DataFrame(pp_reward_recip)
pp_reward_recip_df = pp_reward_recip_df.T
pp_reward_recip_df.columns = ["pp_reward_recip"]

# get incentive timing data
pp_incent_timing = get_data(pp_incentive_timing_output)
pp_incent_timing_df = pd.DataFrame(pp_incent_timing)
pp_incent_timing_df = pp_incent_timing_df.T
pp_incent_timing_df.columns = ["pp_incent_timing"]

# get incentive type data
pp_incent_type= get_data(pp_incentive_type_output)
pp_incent_type_df = pd.DataFrame(pp_incent_type)
pp_incent_type_df = pp_incent_type_df.T
pp_incent_type_df.columns = ["pp_incent_type"]

# get incentive amount data
pp_incent_amount = comments(pp_incentive_amount_output)
pp_incent_amount_df = pd.DataFrame(pp_incent_amount)
pp_incent_amount_df = pp_incent_amount_df.T
pp_incent_amount_df.columns = ["pp_incent_amount"]

# get teacher evaluation period data
pp_teach_eval_per = get_data(pp_teacher_eval_period_output)
pp_teach_eval_per_df = pd.DataFrame(pp_teach_eval_per)
pp_teach_eval_per_df = pp_teach_eval_per_df.T
pp_teach_eval_per_df.columns = ["pp_teach_eval_per"]

pp_ss_df = pd.concat([
    pp_incent_crit_df,
    pp_reward_recip_df,
    pp_incent_timing_df,
    pp_incent_type_df,
    pp_incent_amount_df,
    pp_teach_eval_per_df,
], axis=1, sort=False)

# fill blanks with NA
pp_ss_df.fillna("NA", inplace=True)

# save to disk
""" pp_ss_df.to_csv("performance_pay_ss.csv", index=False) """