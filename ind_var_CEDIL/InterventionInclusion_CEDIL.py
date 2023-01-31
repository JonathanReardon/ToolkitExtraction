from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import intervention_approach_digital_technology_CEDIL
from AttributeIDList import intervention_approach_parents_or_community_volunteers_CEDIL
import pandas as pd

# load json file
load_json()

###########################################
# DIGITAL TECHNOLOGY INTERVENTION INCLUSION
###########################################

# Get Digital Technology (inclusion) main data
DigitalTechnology = get_data(intervention_approach_digital_technology_CEDIL)
DigitalTechnology_df = pd.DataFrame(DigitalTechnology)
DigitalTechnology_df = DigitalTechnology_df.T
DigitalTechnology_df.columns = ["digit_tech_raw"]

# Get Digital Technology (inclusion) highlighted text
DigitalTechnology_HT = highlighted_text(intervention_approach_digital_technology_CEDIL)
DigitalTechnology_HT_df = pd.DataFrame(DigitalTechnology_HT)
DigitalTechnology_HT_df = DigitalTechnology_HT_df.T
DigitalTechnology_HT_df.columns = ["digit_tech_ht"]

# Get Digital Technology (inclusion) user comments
DigitalTechnology_Comments = comments(intervention_approach_digital_technology_CEDIL)
DigitalTechnology_Comments_df = pd.DataFrame(DigitalTechnology_Comments)
DigitalTechnology_Comments_df = DigitalTechnology_Comments_df.T
DigitalTechnology_Comments_df.columns = ["digit_tech_info"]

###########################################
# PARENTS OR COMMUNITY VOLUNTEERS INCLUSION
###########################################

# Get Parents/Community volunteers (inclusion) main data
Parents_or_Community_Volunteers = get_data(intervention_approach_parents_or_community_volunteers_CEDIL)
Parents_or_Community_Volunteers_df = pd.DataFrame(Parents_or_Community_Volunteers)
Parents_or_Community_Volunteers_df = Parents_or_Community_Volunteers_df.T
Parents_or_Community_Volunteers_df.columns = ["parent_partic_raw"]

# Get Parents/Community volunteers (inclusion) highlighted text
Parents_or_Community_Volunteers_HT = highlighted_text(intervention_approach_parents_or_community_volunteers_CEDIL)
Parents_or_Community_Volunteers_HT_df = pd.DataFrame(Parents_or_Community_Volunteers_HT)
Parents_or_Community_Volunteers_HT_df  = Parents_or_Community_Volunteers_HT_df.T
Parents_or_Community_Volunteers_HT_df.columns = ["parent_partic_ht"]

# Get Parents/Community volunteers (inclusion) user comments
Parents_or_Community_Volunteers = comments(intervention_approach_parents_or_community_volunteers_CEDIL)
Parents_or_Community_Volunteers_comments_df = pd.DataFrame(Parents_or_Community_Volunteers)
Parents_or_Community_Volunteers_comments_df = Parents_or_Community_Volunteers_comments_df.T
Parents_or_Community_Volunteers_comments_df.columns = ["parent_partic_info"]

# concatenate data frames
intervention_inclusion_df = pd.concat([
    DigitalTechnology_df, 
    DigitalTechnology_HT_df, 
    DigitalTechnology_Comments_df,
    Parents_or_Community_Volunteers_df,
    Parents_or_Community_Volunteers_HT_df, 
    Parents_or_Community_Volunteers_comments_df
], axis=1, sort=False)

# Remove problematic text (potential escape sequences) from text input
intervention_inclusion_df.replace('\r',' ', regex=True, inplace=True)
intervention_inclusion_df.replace('\n',' ', regex=True, inplace=True)
intervention_inclusion_df.replace(':',' ',  regex=True, inplace=True)
intervention_inclusion_df.replace(';',' ',  regex=True, inplace=True)

# fill blanks with NS
intervention_inclusion_df.fillna("NA", inplace=True)

# Save to file (.csv)
""" intervention_inclusion_df.to_csv("InterventionInclusion.csv", index=False) """

print(intervention_inclusion_df)