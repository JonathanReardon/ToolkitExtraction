from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import cl_approach_spec_output
from AttributeIDList import cl_group_size_output
from AttributeIDList import cl_collab_kind_output
from AttributeIDList import cl_stud_collab_output
from AttributeIDList import cl_extr_rewards_output
from AttributeIDList import cl_if_yes_rewards_output
from AttributeIDList import cl_comp_elem_output
from AttributeIDList import cl_teacher_role_info_output
from AttributeIDList import cl_pupil_feedback_output
from AttributeIDList import cl_pupil_feedback_who_output

import pandas as pd

load_json()

# COLLABORATIVE LEARNING

# get approach specified data
cl_approach_spec = get_data(cl_approach_spec_output)
cl_approach_spec_df = pd.DataFrame(cl_approach_spec)
cl_approach_spec_df = cl_approach_spec_df.T
cl_approach_spec_df.columns = ["cl_approach_spec"]

# get group size data
cl_grp_size = get_data(cl_group_size_output)
cl_grp_size_df = pd.DataFrame(cl_grp_size)
cl_grp_size_df = cl_grp_size_df.T
cl_grp_size_df.columns = ["cl_grp_size"]

# get collab kind data
cl_collab_kind = get_data(cl_collab_kind_output)
cl_collab_kind_df = pd.DataFrame(cl_collab_kind)
cl_collab_kind_df = cl_collab_kind_df.T
cl_collab_kind_df.columns = ["cl_collab_kind"]

# get student collab data
cl_stud_collab = get_data(cl_stud_collab_output)
cl_stud_collab_df = pd.DataFrame(cl_stud_collab)
cl_stud_collab_df = cl_stud_collab_df.T
cl_stud_collab_df.columns = ["cl_stud_collab"]

# get student collab highlighted text
cl_stud_collab_HT = highlighted_text(cl_stud_collab_output)
cl_stud_collab_HT_df = pd.DataFrame(cl_stud_collab_HT)
cl_stud_collab_HT_df = cl_stud_collab_HT_df.T
cl_stud_collab_HT_df.columns = ["cl_stud_collab_HT"]

# get extrinsic rewards data
cl_extr_rewards = get_data(cl_extr_rewards_output)
cl_extr_rewards_df = pd.DataFrame(cl_extr_rewards)
cl_extr_rewards_df = cl_extr_rewards_df.T
cl_extr_rewards_df.columns = ["cl_extr_rewards"]

# get extrinsic rewards highlighted text
cl_extr_rewards_HT = highlighted_text(cl_extr_rewards_output)
cl_extr_rewards_HT_df = pd.DataFrame(cl_extr_rewards_HT)
cl_extr_rewards_HT_df = cl_extr_rewards_HT_df.T
cl_extr_rewards_HT_df.columns = ["cl_extr_rewards_HT"]

# get if yes rewards, where they.. data
cl_if_yes_rewards = get_data(cl_if_yes_rewards_output)
cl_if_yes_rewards_df = pd.DataFrame(cl_if_yes_rewards)
cl_if_yes_rewards_df = cl_if_yes_rewards_df.T
cl_if_yes_rewards_df.columns = ["cl_what_rewards"]

# get if yes rewards, where they.. highlighted text
cl_if_yes_rewards_HT = highlighted_text(cl_if_yes_rewards_output)
cl_if_yes_rewards_HT_df = pd.DataFrame(cl_if_yes_rewards_HT)
cl_if_yes_rewards_HT_df = cl_if_yes_rewards_HT_df.T
cl_if_yes_rewards_HT_df.columns = ["cl_what_rewards_HT"]

# get competitive element data
cl_comp_elem = get_data(cl_comp_elem_output)
cl_comp_elem_df = pd.DataFrame(cl_comp_elem)
cl_comp_elem_df = cl_comp_elem_df.T
cl_comp_elem_df.columns = ["cl_comp_elem"]

# get competitive element highlighted text
cl_comp_elem_HT = highlighted_text(cl_comp_elem_output)
cl_comp_elem_HT_df = pd.DataFrame(cl_comp_elem_HT)
cl_comp_elem_HT_df = cl_comp_elem_HT_df.T
cl_comp_elem_HT_df.columns = ["cl_comp_elem_HT"]

# get teacher role info data
cl_teach_role_info = get_data(cl_teacher_role_info_output)
cl_teach_role_info_df = pd.DataFrame(cl_teach_role_info)
cl_teach_role_info_df = cl_teach_role_info_df.T
cl_teach_role_info_df.columns = ["cl_teacher_role_info"]

# get teacher role info highlighted text
cl_teach_role_info_HT = highlighted_text(cl_teacher_role_info_output)
cl_teach_role_info_HT_df = pd.DataFrame(cl_teach_role_info_HT)
cl_teach_role_info_HT_df = cl_teach_role_info_HT_df.T
cl_teach_role_info_HT_df.columns = ["cl_teacher_role_info_HT"]

# get pupil feedback data
cl_pup_feedback = get_data(cl_pupil_feedback_output)
cl_pup_feedback_df = pd.DataFrame(cl_pup_feedback)
cl_pup_feedback_df = cl_pup_feedback_df.T
cl_pup_feedback_df.columns = ["cl_pup_feedback"]

# get pupil feedback highlighted text
cl_pup_feedback_HT = highlighted_text(cl_pupil_feedback_output)
cl_pup_feedback_HT_df = pd.DataFrame(cl_pup_feedback_HT)
cl_pup_feedback_HT_df = cl_pup_feedback_HT_df.T
cl_pup_feedback_HT_df.columns = ["cl_pup_feedback_HT"]

# get pupil feedback who data
cl_pup_feedback_who = get_data(cl_pupil_feedback_who_output)
cl_pup_feedback_who_df = pd.DataFrame(cl_pup_feedback_who)
cl_pup_feedback_who_df = cl_pup_feedback_who_df.T
cl_pup_feedback_who_df.columns = ["cl_pup_feedback_who"]

# get pupil feedback who highlighted text
cl_pup_feedback_who_HT = highlighted_text(cl_pupil_feedback_who_output)
cl_pup_feedback_who_HT_df = pd.DataFrame(cl_pup_feedback_who_HT)
cl_pup_feedback_who_HT_df = cl_pup_feedback_who_HT_df.T
cl_pup_feedback_who_HT_df.columns = ["cl_pup_feedback_who_HT"]


cl_ss_df = pd.concat([
    cl_approach_spec_df,
    cl_grp_size_df,
    cl_collab_kind_df,
    cl_stud_collab_df,
    cl_extr_rewards_df,
    cl_if_yes_rewards_df,
    cl_comp_elem_df,
    cl_teach_role_info_df,
    cl_pup_feedback_df,
    cl_pup_feedback_who_df,
], axis=1, sort=False)

# fill blanks with NA
cl_ss_df.fillna("NA", inplace=True)

# save to disk
cl_ss_df.to_csv("collaborative_learning_ss.csv", index=False)

print(cl_ss_df[0:50])