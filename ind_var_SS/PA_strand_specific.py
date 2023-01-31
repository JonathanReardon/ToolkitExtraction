from Main import load_json, get_data

from AttributeIDList import pha_when_output
from AttributeIDList import pha_lessons_included_output
from AttributeIDList import pha_activity_type_output
from AttributeIDList import pha_exercise_level_output

import pandas as pd

load_json()

# PHYSICAL ACTIVITY

# get when? data
pha_when = get_data(pha_when_output)
pha_when_df = pd.DataFrame(pha_when)
pha_when_df = pha_when_df.T
pha_when_df.columns = ["pa_when"]

# get lessons included data
pha_lessons = get_data(pha_lessons_included_output)
pha_lessons_df = pd.DataFrame(pha_lessons)
pha_lessons_df = pha_lessons_df.T
pha_lessons_df.columns = ["pa_lessons"]

# get activity type data
pha_act_type = get_data(pha_activity_type_output)
pha_act_type_df = pd.DataFrame(pha_act_type)
pha_act_type_df = pha_act_type_df.T
pha_act_type_df.columns = ["pa_act_type"]

# get exercise level data
pha_exer_level = get_data(pha_exercise_level_output)
pha_exer_level_df = pd.DataFrame(pha_exer_level)
pha_exer_level_df = pha_exer_level_df.T
pha_exer_level_df.columns = ["pa_exer_level"]

pha_ss_df = pd.concat([
    pha_when_df,
    pha_lessons_df,
    pha_act_type_df,
    pha_exer_level_df,
], axis=1, sort=False)

# fill blanks with NA
pha_ss_df.fillna("NA", inplace=True)

# save to disk
pha_ss_df.to_csv("physical_activity_ss.csv", index=False)

print(pha_ss_df[0:50])