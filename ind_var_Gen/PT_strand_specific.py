from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import tutor_age_output
from AttributeIDList import tutor_same_age_output
from AttributeIDList import tutor_cross_age_output
from AttributeIDList import tutor_from_output
from AttributeIDList import tutor_role_output
from AttributeIDList import tutee_attainment_output
from AttributeIDList import digit_tech_output
from AttributeIDList import tutor_tutee_incentive_output
from AttributeIDList import tutor_age_same
from AttributeIDList import tutor_age_cross
from eppi_ID import eppiid_df

import pandas as pd

load_json()

# TUTOR AGE

# get tutor desc data
tut_desc = get_data(tutor_age_output)
tut_desc_df = pd.DataFrame(tut_desc)
tut_desc_df = tut_desc_df.T
tut_desc_df.columns = ["pt_tut_desc"]

# split tutor desc components for ind col extraction

# tutor same age
tut_desc_same_age = get_data(tutor_age_same)
tut_desc_same_age_df = pd.DataFrame(tut_desc_same_age)
tut_desc_same_age_df = tut_desc_same_age_df.T
tut_desc_same_age_df.columns = ["pt_tut_desc_same_age"]

# tutor cross age
tut_desc_cross_age = get_data(tutor_age_cross)
tut_desc_cross_age_df = pd.DataFrame(tut_desc_cross_age)
tut_desc_cross_age_df = tut_desc_cross_age_df.T
tut_desc_cross_age_df.columns = ["pt_tut_desc_cross_age"]

# nested tutor same age responses
tut_same_age = get_data(tutor_same_age_output)
tut_same_age_df = pd.DataFrame(tut_same_age)
tut_same_age_df = tut_same_age_df.T
tut_same_age_df.columns = ["pt_same_age_attainment"]

# nested tutor cross age responses
tut_cross_age = get_data(tutor_cross_age_output)
tut_cross_age_df = pd.DataFrame(tut_cross_age)
tut_cross_age_df = tut_cross_age_df.T
tut_cross_age_df.columns = ["pt_cross_age_attainment"]

# get tutor where from data
tut_from = get_data(tutor_from_output)
tut_from_df = pd.DataFrame(tut_from)
tut_from_df = tut_from_df.T
tut_from_df.columns = ["pt_tut_from"]

# get tutor role data
tut_role = get_data(tutor_role_output)
tut_role_df = pd.DataFrame(tut_role)
tut_role_df = tut_role_df.T
tut_role_df.columns = ["pt_tut_role"]

# get tutee attainment level data
tut_tutee_attain_lev = get_data(tutee_attainment_output)
tut_tutee_attain_lev_df = pd.DataFrame(tut_tutee_attain_lev)
tut_tutee_attain_lev_df = tut_tutee_attain_lev_df.T
tut_tutee_attain_lev_df.columns = ["pt_tutee_attain_level"]

# get digit tech data
digit_tech = get_data(digit_tech_output)
digit_tech_df = pd.DataFrame(digit_tech)
digit_tech_df = digit_tech_df.T
digit_tech_df.columns = ["pt_digit_tech"]

# get incentive data
tut_incentive = get_data(tutor_tutee_incentive_output)
tut_incentive_df = pd.DataFrame(tut_incentive)
tut_incentive_df = tut_incentive_df.T
tut_incentive_df.columns = ["pt_incentive"]

peer_tut_ss_df = pd.concat([
    eppiid_df,
    tut_desc_df,
    tut_desc_same_age_df,
    tut_desc_cross_age_df,

    tut_same_age_df,
    tut_cross_age_df,
    tut_from_df,
    tut_role_df,
    tut_tutee_attain_lev_df,
    digit_tech_df,
    tut_incentive_df,
], axis=1, sort=False)

print(peer_tut_ss_df[0:25])

""" peer_tut_ss_df.to_csv("peer_tutoring_ss.csv", index=False, header=True) """