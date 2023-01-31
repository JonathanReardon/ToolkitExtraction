from Main import load_json, get_data
from AttributeIDList import pe_involved_output
from AttributeIDList import pe_activity_location_output
from AttributeIDList import pe_prog_training_output
from AttributeIDList import pe_prog_support_output
from AttributeIDList import pe_children_output
from AttributeIDList import pe_focus_output

import pandas as pd

load_json()

# PARENTAL ENGAGEMENT

# get who was involved data
pe_involved = get_data(pe_involved_output)
pe_involved_df = pd.DataFrame(pe_involved)
pe_involved_df = pe_involved_df.T
pe_involved_df.columns = ["pe_involved"]

# get activiyt location data
pe_act_loc = get_data(pe_activity_location_output)
pe_act_loc_df = pd.DataFrame(pe_act_loc)
pe_act_loc_df = pe_act_loc_df.T
pe_act_loc_df.columns = ["pe_act_loc"]

# get programme training data
pe_prog_train = get_data(pe_prog_training_output)
pe_prog_train_df = pd.DataFrame(pe_prog_train)
pe_prog_train_df = pe_prog_train_df.T
pe_prog_train_df.columns = ["pe_prog_training"]

# get programme support data
pe_prog_support = get_data(pe_prog_support_output)
pe_prog_support_df = pd.DataFrame(pe_prog_support)
pe_prog_support_df = pe_prog_support_df.T
pe_prog_support_df.columns = ["pe_prog_support"]

# get children data
pe_children_work_with = get_data(pe_children_output)
pe_children_work_with_df = pd.DataFrame(pe_children_work_with)
pe_children_work_with_df = pe_children_work_with_df.T
pe_children_work_with_df.columns = ["pe_children"]

# get engagement focus data
pe_focus = get_data(pe_focus_output)
pe_focus_df = pd.DataFrame(pe_focus)
pe_focus_df = pe_focus_df.T
pe_focus_df.columns = ["pe_focus"]

pe_ss_df = pd.concat([
    pe_involved_df,
    pe_act_loc_df,
    pe_prog_train_df,
    pe_prog_support_df,
    pe_children_work_with_df,
    pe_focus_df,
], axis=1, sort=False)

# fill blanks with NA
pe_ss_df.fillna("NA", inplace=True)

# save to disk
pe_ss_df.to_csv("parental_engagement_ss.csv", index=False)

print(pe_ss_df[0:50])