from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import redc_avg_small_class_size_output
from AttributeIDList import redc_avg_large_class_size_output
from AttributeIDList import redc_small_class_teacher_number_output
from AttributeIDList import redc_large_class_teacher_number_output
from AttributeIDList import redc_large_class_adaption_output
from AttributeIDList import redc_reduc_for_limited_num_sub_output
from AttributeIDList import redc_impl_for_all_or_most_output

import pandas as pd

load_json()

# REDUCING CLASS SIZE

# get typical or average small class size info
redc_avg_small_class_size = comments(redc_avg_small_class_size_output)
redc_avg_small_class_size_df = pd.DataFrame(redc_avg_small_class_size)
redc_avg_small_class_size_df = redc_avg_small_class_size_df.T
redc_avg_small_class_size_df.columns = ["redc_avg_small_class_size_info"]

# get typical or average large class size info
redc_avg_large_class_size = comments(redc_avg_large_class_size_output)
redc_avg_large_class_size_df = pd.DataFrame(redc_avg_large_class_size)
redc_avg_large_class_size_df = redc_avg_large_class_size_df.T
redc_avg_large_class_size_df.columns = ["redc_avg_large_class_size_info"]

# get small class teacher numb data
redc_small_class_teach_num = get_data(redc_small_class_teacher_number_output)
redc_small_class_teach_num_df = pd.DataFrame(redc_small_class_teach_num)
redc_small_class_teach_num_df = redc_small_class_teach_num_df.T
redc_small_class_teach_num_df.columns = ["redc_small_class_teach_num"]

# get large class teacher numb data
redc_large_class_teach_num = get_data(redc_large_class_teacher_number_output)
redc_large_class_teach_num_df = pd.DataFrame(redc_large_class_teach_num)
redc_large_class_teach_num_df = redc_large_class_teach_num_df.T
redc_large_class_teach_num_df.columns = ["redc_large_class_teach_num"]

# get large class adaption data
redc_large_class_adapt = get_data(redc_large_class_adaption_output)
redc_large_class_adapt_df = pd.DataFrame(redc_large_class_adapt)
redc_large_class_adapt_df = redc_large_class_adapt_df.T
redc_large_class_adapt_df.columns = ["redc_large_class_adapt"]

# get limited number of subjects data
redc_lim_num_subj = get_data(redc_reduc_for_limited_num_sub_output)
redc_lim_num_subj_df = pd.DataFrame(redc_lim_num_subj)
redc_lim_num_subj_df = redc_lim_num_subj_df.T
redc_lim_num_subj_df.columns = ["redc_lim_num_subj"]

# get reduction for all or most lessons across curriculum data
redc_impl_all_or_most_lessons = get_data(redc_impl_for_all_or_most_output)
redc_impl_all_or_most_lessons_df = pd.DataFrame(redc_impl_all_or_most_lessons)
redc_impl_all_or_most_lessons_df = redc_impl_all_or_most_lessons_df.T
redc_impl_all_or_most_lessons_df.columns = ["redc_impl_all_or_most_lessons"]

redc_ss_df = pd.concat([
    redc_avg_small_class_size_df,
    redc_avg_large_class_size_df,
    redc_small_class_teach_num_df,
    redc_large_class_teach_num_df,
    redc_large_class_adapt_df,
    redc_lim_num_subj_df,
    redc_impl_all_or_most_lessons_df,
], axis=1, sort=False)

""" redc_ss_df.to_csv("reducing_class_size.csv", index=False, header=True) """