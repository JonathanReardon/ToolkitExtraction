from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import mentor_identity, mentor_paid_or_compensated, mentor_organisation
from AttributeIDList import mentor_training, mentor_meeting_frequency, mentor_meeting_details_provided, mentor_meeting_location
from AttributeIDList import mentoring_additional_experiences, mentoring_programme_focus
import pandas as pd

load_json()

# get Mentor identity data
ment_ident = get_data(mentor_identity)
ment_ident_df = pd.DataFrame(ment_ident)
ment_ident_df = ment_ident_df.T
ment_ident_df.columns = ["m_identity"]

# Get Mentor identity highlighted text
ment_ident_HT = highlighted_text(mentor_identity)
ment_ident_HT_df = pd.DataFrame(ment_ident_HT)
ment_ident_HT_df = ment_ident_HT_df.T
ment_ident_HT_df.columns = ["m_identity_ht"]

# Get Mentor identity user comments
ment_ident_Comments = comments(mentor_identity)
ment_ident_Comments_df = pd.DataFrame(ment_ident_Comments)
ment_ident_Comments_df = ment_ident_Comments_df.T
ment_ident_Comments_df.columns = ["m_identity_info"]

# get Mentor pay data
ment_pay = get_data(mentor_paid_or_compensated)
ment_pay_df = pd.DataFrame(ment_pay)
ment_pay_df = ment_pay_df.T
ment_pay_df.columns = ["m_pay"]

# Get Mentor pay highlighted text
ment_pay_HT = highlighted_text(mentor_paid_or_compensated)
ment_pay_HT_df = pd.DataFrame(ment_pay_HT)
ment_pay_HT_df = ment_pay_HT_df.T
ment_pay_HT_df.columns = ["m_pay_ht"]

# Get Mentor pay user comments
ment_pay_Comments = comments(mentor_paid_or_compensated)
ment_pay_Comments_df = pd.DataFrame(ment_pay_Comments)
ment_pay_Comments_df = ment_pay_Comments_df.T
ment_pay_Comments_df.columns = ["m_pay_info"]

# get Mentor org data
ment_org = get_data(mentor_organisation)
ment_org_df = pd.DataFrame(ment_org)
ment_org_df = ment_org_df.T
ment_org_df.columns = ["m_org"]

# Get Mentor org highlighted text
ment_org_HT = highlighted_text(mentor_organisation)
ment_org_HT_df = pd.DataFrame(ment_org_HT)
ment_org_HT_df = ment_org_HT_df.T
ment_org_HT_df.columns = ["m_org_ht"]

# Get Mentor org user comments
ment_org_Comments = comments(mentor_organisation)
ment_org_Comments_df = pd.DataFrame(ment_org_Comments)
ment_org_Comments_df = ment_org_Comments_df.T
ment_org_Comments_df.columns = ["m_org_info"]

# get Mentor training data
ment_training = get_data(mentor_training)
ment_training_df = pd.DataFrame(ment_training)
ment_training_df = ment_training_df.T
ment_training_df.columns = ["m_training"]

# Get Mentor training highlighted text
ment_training_HT = highlighted_text(mentor_training)
ment_training_HT_df = pd.DataFrame(ment_training_HT)
ment_training_HT_df = ment_training_HT_df.T
ment_training_HT_df.columns = ["m_training_ht"]

# Get Mentor training user comments
ment_training_Comments = comments(mentor_training)
ment_training_Comments_df = pd.DataFrame(ment_training_Comments)
ment_training_Comments_df = ment_training_Comments_df.T
ment_training_Comments_df.columns = ["m_training_info"]

# get Mentor meeting freq data
ment_meeting_freq = get_data(mentor_meeting_frequency)
ment_meeting_freq_df = pd.DataFrame(ment_meeting_freq)
ment_meeting_freq_df = ment_meeting_freq_df.T
ment_meeting_freq_df.columns = ["m_meeting_freq"]

# Get Mentor meeting freq highlighted text
ment_meeting_freq_HT = highlighted_text(mentor_meeting_frequency)
ment_meeting_freq_HT_df = pd.DataFrame(ment_meeting_freq_HT)
ment_meeting_freq_HT_df = ment_meeting_freq_HT_df.T
ment_meeting_freq_HT_df.columns = ["m_meeting_freq_ht"]

# Get Mentor meeting freq user comments
ment_meeting_freq_Comments = comments(mentor_meeting_frequency)
ment_meeting_freq_Comments_df = pd.DataFrame(ment_meeting_freq_Comments)
ment_meeting_freq_Comments_df = ment_meeting_freq_Comments_df.T
ment_meeting_freq_Comments_df.columns = ["m_meeting_freq_info"]


# get Mentor meeting details data
ment_meeting_details = get_data(mentor_meeting_details_provided)
ment_meeting_details_df = pd.DataFrame(ment_meeting_details)
ment_meeting_details_df = ment_meeting_details_df.T
ment_meeting_details_df.columns = ["m_meeting_details"]

# Get Mentor meeting details highlighted text
ment_meeting_details_HT = highlighted_text(mentor_meeting_details_provided)
ment_meeting_details_HT_df = pd.DataFrame(ment_meeting_details_HT)
ment_meeting_details_HT_df = ment_meeting_details_HT_df.T
ment_meeting_details_HT_df.columns = ["m_meeting_details_ht"]

# Get Mentor meeting details user comments
ment_meeting_details_Comments = comments(mentor_meeting_details_provided)
ment_meeting_details_Comments_df = pd.DataFrame(ment_meeting_details_Comments)
ment_meeting_details_Comments_df = ment_meeting_details_Comments_df.T
ment_meeting_details_Comments_df.columns = ["m_meeting_details_info"]

# get Mentor meeting location data
ment_meeting_location = get_data(mentor_meeting_location)
ment_meeting_location_df = pd.DataFrame(ment_meeting_location)
ment_meeting_location_df = ment_meeting_location_df.T
ment_meeting_location_df.columns = ["m_meeting_location"]

# Get Mentor meeting location highlighted text
ment_meeting_location_HT = highlighted_text(mentor_meeting_location)
ment_meeting_location_HT_df = pd.DataFrame(ment_meeting_location_HT)
ment_meeting_location_HT_df = ment_meeting_location_HT_df.T
ment_meeting_location_HT_df.columns = ["m_meeting_location_ht"]

# Get Mentor meeting location user comments
ment_meeting_location_Comments = comments(mentor_meeting_location)
ment_meeting_location_Comments_df = pd.DataFrame(ment_meeting_location_Comments)
ment_meeting_location_Comments_df = ment_meeting_location_Comments_df.T
ment_meeting_location_Comments_df.columns = ["m_meeting_location_info"]

# get Mentor additional experiences data
ment_addit_exp = get_data(mentoring_additional_experiences)
ment_addit_exp_df = pd.DataFrame(ment_addit_exp)
ment_addit_exp_df = ment_addit_exp_df.T
ment_addit_exp_df.columns = ["m_addit_exp"]

# Get Mentor additional experiences highlighted text
ment_addit_exp_HT = highlighted_text(mentoring_additional_experiences)
ment_addit_exp_HT_df = pd.DataFrame(ment_addit_exp_HT)
ment_addit_exp_HT_df = ment_addit_exp_HT_df.T
ment_addit_exp_HT_df.columns = ["m_addit_exp_ht"]

# Get Mentor additional experiences user comments
ment_addit_exp_Comments = comments(mentoring_additional_experiences)
ment_addit_exp_Comments_df = pd.DataFrame(ment_addit_exp_Comments)
ment_addit_exp_Comments_df = ment_addit_exp_Comments_df.T
ment_addit_exp_Comments_df.columns = ["m_addit_exp_info"]

# get Mentor prog focus data
ment_prog_focus = get_data(mentoring_programme_focus)
ment_prog_focus_df = pd.DataFrame(ment_prog_focus)
ment_prog_focus_df = ment_prog_focus_df.T
ment_prog_focus_df.columns = ["m_prog_focus"]

# Get Mentor prog focus highlighted text
ment_prog_focus_HT = highlighted_text(mentoring_programme_focus)
ment_prog_focus_HT_df = pd.DataFrame(ment_prog_focus_HT)
ment_prog_focus_HT_df = ment_prog_focus_HT_df.T
ment_prog_focus_HT_df.columns = ["m_prog_focus_ht"]

# Get Mentor prog focus user comments
ment_prog_focus_Comments = comments(mentoring_programme_focus)
ment_prog_focus_Comments_df = pd.DataFrame(ment_prog_focus_Comments)
ment_prog_focus_Comments_df = ment_prog_focus_Comments_df.T
ment_prog_focus_Comments_df.columns = ["m_prog_focus_info"]

# concatenate data frames
mentoring_ss_df = pd.concat([
    ment_ident_df,

    ment_pay_df,

    ment_org_df,

    ment_training_df,

    ment_meeting_freq_df,

    ment_meeting_details_df,

    ment_meeting_location_df,

    ment_addit_exp_df,

    ment_prog_focus_df,

], axis=1, sort=False)

# fill blanks with NA
mentoring_ss_df.fillna("NA", inplace=True)

# save to disk
# mentoring_ss_df.to_csv("mentoring_ss_df.csv", index=False)

print(ment_meeting_details_df)
