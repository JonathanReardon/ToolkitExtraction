from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_teaching_approach
import pandas as pd

# load json file
load_json()

# get intervention teaching approach data
InterventionTeachingApproach = get_data(intervention_teaching_approach)
InterventionTeachingApproach_df = pd.DataFrame(InterventionTeachingApproach)
InterventionTeachingApproach_df = InterventionTeachingApproach_df.T
InterventionTeachingApproach_df.columns = ["int_approach_raw"]

# get intervention teaching approach highlighted text
InterventionTeachingApproach_HT = highlighted_text(intervention_teaching_approach)
InterventionTeachingApproach_HT_df = pd.DataFrame(InterventionTeachingApproach_HT)
InterventionTeachingApproach_HT_df = InterventionTeachingApproach_HT_df.T
InterventionTeachingApproach_HT_df.columns = ["int_approach_ht"]

# get intervention teaching approach user comments
InterventionTeachingApproach_Comments = comments(intervention_teaching_approach)
InterventionTeachingApproach_Comments_df = pd.DataFrame(InterventionTeachingApproach_Comments)
InterventionTeachingApproach_Comments_df = InterventionTeachingApproach_Comments_df.T
InterventionTeachingApproach_Comments_df.columns = ["int_approach_info"]

# concatenate data frames
intervention_teaching_approach_df = pd.concat([
    InterventionTeachingApproach_df, 
    InterventionTeachingApproach_HT_df, 
    InterventionTeachingApproach_Comments_df
], axis=1, sort=False)

# remove problematic text
intervention_teaching_approach_df.replace('\r',' ', regex=True, inplace=True)
intervention_teaching_approach_df.replace('\n',' ', regex=True, inplace=True)
intervention_teaching_approach_df.replace(':',' ',  regex=True, inplace=True)
intervention_teaching_approach_df.replace(';',' ',  regex=True, inplace=True)

# fill blanks with NA
intervention_teaching_approach_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_teaching_approach_df.to_csv("InterventionTeachingApproach.csv", index=False) """