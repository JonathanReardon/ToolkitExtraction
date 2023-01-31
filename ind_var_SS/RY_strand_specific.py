from Main import load_json, get_data, highlighted_text, comments

from AttributeIDList import ry_ret_stu_identify_output
from AttributeIDList import ry_ret_stu_age_output
from AttributeIDList import ry_ret_basis_output
from AttributeIDList import ry_impact_measure_delay_output
from AttributeIDList import ry_stu_ret_number_output
from AttributeIDList import ry_ret_stud_compared_with_output
from AttributeIDList import ry_prom_count_characteristics_output
from AttributeIDList import ry_comparison
from AttributeIDList import ry_comp_grp_school

import pandas as pd

load_json()

# REPEATING A YEAR

# get identify retained students data
ry_identify_ret_stu = get_data(ry_ret_stu_identify_output)
ry_identify_ret_stu_df = pd.DataFrame(ry_identify_ret_stu)
ry_identify_ret_stu_df = ry_identify_ret_stu_df.T
ry_identify_ret_stu_df.columns = ["ry_identify_ret_stu"]

# get retained students age data
ry_ret_stu_age = get_data(ry_ret_stu_age_output)
ry_ret_stu_age_df = pd.DataFrame(ry_ret_stu_age)
ry_ret_stu_age_df = ry_ret_stu_age_df.T
ry_ret_stu_age_df.columns = ["ry_ret_stu_age"]

# get retention basis data
ry_ret_basis = get_data(ry_ret_basis_output)
ry_ret_basis_df = pd.DataFrame(ry_ret_basis)
ry_ret_basis_df = ry_ret_basis_df.T
ry_ret_basis_df.columns = ["ry_ret_basis"]

# get impact measure data
ry_impact_meas = get_data(ry_impact_measure_delay_output)
ry_impact_meas_df = pd.DataFrame(ry_impact_meas)
ry_impact_meas_df = ry_impact_meas_df.T
ry_impact_meas_df.columns = ["ry_impact_meas"]

# get number of times students were retained data
ry_stu_ret_num = get_data(ry_stu_ret_number_output)
ry_stu_ret_num_df = pd.DataFrame(ry_stu_ret_num)
ry_stu_ret_num_df = ry_stu_ret_num_df.T
ry_stu_ret_num_df.columns = ["ry_stu_ret_num"]

# get retained students compared with data
ry_ret_stu_comparison = get_data(ry_ret_stud_compared_with_output)
ry_ret_stu_comparison_df = pd.DataFrame(ry_ret_stu_comparison)
ry_ret_stu_comparison_df = ry_ret_stu_comparison_df.T
ry_ret_stu_comparison_df.columns = ["ry_ret_stud_comp"]

# get promoted counterpart characteristics data
ry_prom_count_char = get_data(ry_prom_count_characteristics_output)
ry_prom_count_char_df = pd.DataFrame(ry_prom_count_char)
ry_prom_count_char_df = ry_prom_count_char_df.T
ry_prom_count_char_df.columns = ["ry_matching_char"]

# get comparison data
ry_comp = get_data(ry_comparison)
ry_comp_df = pd.DataFrame(ry_comp)
ry_comp_df = ry_comp_df.T
ry_comp_df.columns = ["ry_comp"]

# get comparison group same school as retained students data
ry_comp_grp_school = get_data(ry_comp_grp_school)
ry_comp_grp_school_df = pd.DataFrame(ry_comp_grp_school)
ry_comp_grp_school_df = ry_comp_grp_school_df.T
ry_comp_grp_school_df.columns = ["ry_comp_grp_school"]

# concatenate data frames
ry_ss_df = pd.concat([
    ry_identify_ret_stu_df,
    ry_ret_stu_age_df,
    ry_ret_basis_df,
    ry_impact_meas_df,
    ry_stu_ret_num_df,
    ry_ret_stu_comparison_df,
    ry_prom_count_char_df,
    ry_comp_df,
    ry_comp_grp_school_df,
], axis=1, sort=False)

# remove problematic text from outputs
ry_ss_df.replace('\r', ' ', regex=True, inplace=True)
ry_ss_df.replace('\n', ' ', regex=True, inplace=True)
ry_ss_df.replace(':', ' ',  regex=True, inplace=True)
ry_ss_df.replace(';', ' ',  regex=True, inplace=True)

ry_ss_df.to_csv("repeating_a_year_ss.csv", index=False, header=True)

print(ry_ss_df[0:15])
