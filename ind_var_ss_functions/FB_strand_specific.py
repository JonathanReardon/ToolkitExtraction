from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import feedback_source_output
from AttributeIDList import feedback_directed_output
from AttributeIDList import feedback_form_output
from AttributeIDList import feedback_when_output
from AttributeIDList import feedback_kind_output
from AttributeIDList import feedback_emo_tone
from AttributeIDList import feedback_about_outcome_output

# feedback source options for ind column extraction
from AttributeIDList import fsource_teacher
from AttributeIDList import fsource_ta
from AttributeIDList import fsource_volunteer
from AttributeIDList import fsource_parent
from AttributeIDList import fsource_researcher
from AttributeIDList import fsource_peer_sameage_class
from AttributeIDList import fsource_peer_group
from AttributeIDList import fsource_peer_older
from AttributeIDList import fsource_dig_aut
from AttributeIDList import fsource_other_nonhuman
from AttributeIDList import fsource_self
from AttributeIDList import fsource_other

import pandas as pd

load_json()

# FEEDBACK SOURCE

# get feedback source data
feedb_source = get_data(feedback_source_output)
feedb_source_df = pd.DataFrame(feedb_source)
feedb_source_df = feedb_source_df.T
feedb_source_df.columns = ["feedback_Source"]

# Get feedback source highlighted text
feedb_source_HT = highlighted_text(feedback_source_output)
feedb_source_HT_df = pd.DataFrame(feedb_source_HT)
feedb_source_HT_df = feedb_source_HT_df.T
feedb_source_HT_df.columns = ["feedback_Source_ht"]

# Get feedback source user comments
feedb_source_Comments = comments(feedback_source_output)
feedb_source_Comments_df = pd.DataFrame(feedb_source_Comments)
feedb_source_Comments_df = feedb_source_Comments_df.T
feedb_source_Comments_df.columns = ["feedback_Source_info"]

# FEEDBACK SOURCE COMPONENTS SPLIT

# get feedback source teacher data
fsource_teacher = get_data(fsource_teacher)
fsource_teacher_df = pd.DataFrame(fsource_teacher)
fsource_teacher_df = fsource_teacher_df.T
fsource_teacher_df.columns = ["fb_source_teacher"]

# get feedback source teaching assistant data
fsource_ta = get_data(fsource_ta)
fsource_ta_df = pd.DataFrame(fsource_ta)
fsource_ta_df = fsource_ta_df.T
fsource_ta_df.columns = ["fb_source_ta"]

# get feedback source volunteer data
fsource_volunteer = get_data(fsource_volunteer)
fsource_volunteer_df = pd.DataFrame(fsource_volunteer)
fsource_volunteer_df = fsource_volunteer_df.T
fsource_volunteer_df.columns = ["fb_source_volunteer"]

# get feedback source parent data
fsource_parent = get_data(fsource_parent)
fsource_parent_df = pd.DataFrame(fsource_parent)
fsource_parent_df = fsource_parent_df.T
fsource_parent_df.columns = ["fb_source_parent"]

# get feedback source researcher data
fsource_researcher = get_data(fsource_researcher)
fsource_researcher_df = pd.DataFrame(fsource_researcher)
fsource_researcher_df = fsource_researcher_df.T
fsource_researcher_df.columns = ["fb_source_researcher"]

# get feedback source peer same age data
fsource_peer_ssame_Age = get_data(fsource_peer_sameage_class)
fsource_peer_ssame_Age_df = pd.DataFrame(fsource_peer_ssame_Age)
fsource_peer_ssame_Age_df = fsource_peer_ssame_Age_df.T
fsource_peer_ssame_Age_df.columns = ["fb_source_peer_sameage"]

# get feedback source peer group data
fsource_peer_group = get_data(fsource_peer_group)
fsource_peer_group_df = pd.DataFrame(fsource_peer_group)
fsource_peer_group_df = fsource_peer_group_df.T
fsource_peer_group_df.columns = ["fb_source_peer_group"]

# get feedback source peer older data
fsource_peer_older = get_data(fsource_peer_older)
fsource_peer_older_df = pd.DataFrame(fsource_peer_older)
fsource_peer_older_df = fsource_peer_older_df.T
fsource_peer_older_df.columns = ["fb_source_peer_older"]

# get feedback source digital automated data
fsource_digit_aut = get_data(fsource_dig_aut)
fsource_digit_aut_df = pd.DataFrame(fsource_digit_aut)
fsource_digit_aut_df = fsource_digit_aut_df.T
fsource_digit_aut_df.columns = ["fb_source_dig_aut"]

# get feedback source other non-human data
fsource_non_human = get_data(fsource_other_nonhuman)
fsource_non_human_df = pd.DataFrame(fsource_non_human)
fsource_non_human_df = fsource_non_human_df.T
fsource_non_human_df.columns = ["fb_source_non_human"]

# get feedback source self data
fsource_self = get_data(fsource_self)
fsource_self_df = pd.DataFrame(fsource_self)
fsource_self_df = fsource_self_df.T
fsource_self_df.columns = ["fb_source_self"]

# get feedback source other data
fsource_other = get_data(fsource_other)
fsource_other_df = pd.DataFrame(fsource_other)
fsource_other_df = fsource_other_df.T
fsource_other_df.columns = ["fb_source_other"]

# FEEDBACK DIRECTED OUTPUT

# get feedback directed data
feedb_directed = get_data(feedback_directed_output)
feedb_directed_df = pd.DataFrame(feedb_directed)
feedb_directed_df = feedb_directed_df.T
feedb_directed_df.columns = ["fb_directed"]

# Get feedback directed highlighted text
feedb_directed_df_HT = highlighted_text(feedback_directed_output)
feedb_directed_df_HT_df = pd.DataFrame(feedb_directed_df_HT)
feedb_directed_df_HT_df = feedb_directed_df_HT_df.T
feedb_directed_df_HT_df.columns = ["fb_directed_ht"]

# Get feedback directed user comments
feedb_directed_Comments = comments(feedback_directed_output)
feedb_directed_Comments_df = pd.DataFrame(feedb_directed_Comments)
feedb_directed_Comments_df = feedb_directed_Comments_df.T
feedb_directed_Comments_df.columns = ["fb_directed_info"]

# FEEDBACK FORM OUTPUT

# get feedback form data
feedb_form = get_data(feedback_form_output)
feedb_form_df = pd.DataFrame(feedb_form)
feedb_form_df = feedb_form_df.T
feedb_form_df.columns = ["fb_form"]

# Get feedback form highlighted text
feedb_form_HT = highlighted_text(feedback_form_output)
feedb_form_HT_df = pd.DataFrame(feedb_form_HT)
feedb_form_HT_df = feedb_form_HT_df.T
feedb_form_HT_df.columns = ["fb_form_ht"]

# Get feedback form user comments
feedb_form_Comments = comments(feedback_form_output)
feedb_form_Comments_df = pd.DataFrame(feedb_form_Comments)
feedb_form_Comments_df = feedb_form_Comments_df.T
feedb_form_Comments_df.columns = ["fb_form_info"]

# FEEDBACK WHEN OUTPUT

# get feedback when data
feedb_when = get_data(feedback_when_output)
feedb_when_df = pd.DataFrame(feedb_when)
feedb_when_df = feedb_when_df.T
feedb_when_df.columns = ["fb_when"]

# Get feedback when highlighted text
feedb_when_HT = highlighted_text(feedback_when_output)
feedb_when_HT_df = pd.DataFrame(feedb_when_HT)
feedb_when_HT_df = feedb_when_HT_df.T
feedb_when_HT_df.columns = ["fb_when_ht"]

# Get feedback when user comments
feedb_when_Comments = comments(feedback_when_output)
feedb_when_Comments_df = pd.DataFrame(feedb_when_Comments)
feedb_when_Comments_df = feedb_when_Comments_df.T
feedb_when_Comments_df.columns = ["fb_when_info"]

# FEEDBACK KIND OUTPUT

# get feedback kind data
feedb_kind = get_data(feedback_kind_output)
feedb_kind_df = pd.DataFrame(feedb_kind)
feedb_kind_df = feedb_kind_df.T
feedb_kind_df.columns = ["fb_kind"]

# get feedback kind "about the outcome" nested data (correct / incorrect"
feedb_kind_abt_outcome = get_data(feedback_about_outcome_output)
feedb_kind_abt_outcome_df = pd.DataFrame(feedb_kind_abt_outcome)
feedb_kind_abt_outcome_df = feedb_kind_abt_outcome_df.T
feedb_kind_abt_outcome_df.columns = ["fb_kind_about_outcome"]

# Get feedback kind highlighted text
feedb_kind_HT = highlighted_text(feedback_kind_output)
feedb_kind_HT_df = pd.DataFrame(feedb_kind_HT)
feedb_kind_HT_df = feedb_kind_HT_df.T
feedb_kind_HT_df.columns = ["fb_kind_ht"]

# Get feedback kind user comments
feedb_kind_Comments = comments(feedback_kind_output)
feedb_kind_Comments_df = pd.DataFrame(feedb_kind_Comments)
feedb_kind_Comments_df = feedb_kind_Comments_df.T
feedb_kind_Comments_df.columns = ["fbkind_info"]

# FEEDBACK EMOTIONAL TONE OUTPUT

# get feedback emotional tone data
feedb_emo_tone = get_data(feedback_emo_tone)
feedb_emo_tone_df = pd.DataFrame(feedb_emo_tone)
feedb_emo_tone_df = feedb_emo_tone_df.T
feedb_emo_tone_df.columns = ["fb_emo_tone"]

# Get feedback emotional tone highlighted text
feedb_emo_tone_HT = highlighted_text(feedback_emo_tone)
feedb_emo_tone_HT_df = pd.DataFrame(feedb_emo_tone_HT)
feedb_emo_tone_HT_df = feedb_emo_tone_HT_df.T
feedb_emo_tone_HT_df.columns = ["fb_emo_tone_ht"]

# Get feedback emotional tone user comments
feedb_emo_tone_Comments = comments(feedback_emo_tone)
feedb_emo_tone_Comments_df = pd.DataFrame(feedb_emo_tone_Comments)
feedb_emo_tone_Comments_df = feedb_emo_tone_Comments_df.T
feedb_emo_tone_Comments_df.columns = ["fb_emo_tone_info"]

# concatenate data frames
feedback_ss_df = pd.concat([
    feedb_source_df,

    fsource_teacher_df,
    fsource_ta_df,
    fsource_volunteer_df,
    fsource_parent_df,
    fsource_researcher_df,
    fsource_peer_ssame_Age_df,
    fsource_peer_group_df,
    fsource_peer_older_df,
    fsource_digit_aut_df,
    fsource_non_human_df,
    fsource_self_df,
    fsource_other_df,

    feedb_directed_df,
    feedb_form_df,
    feedb_when_df,
    feedb_kind_df,
    feedb_kind_abt_outcome_df,
    feedb_emo_tone_df,
], axis=1, sort=False)

# remove problematic text from outputs
feedback_ss_df.replace('\r', ' ', regex=True, inplace=True)
feedback_ss_df.replace('\n', ' ', regex=True, inplace=True)
feedback_ss_df.replace(':', ' ',  regex=True, inplace=True)
feedback_ss_df.replace(';', ' ',  regex=True, inplace=True)

""" feedback_ss_df.to_csv("feedback_ss.csv", index=False, header=True) """

""" if feedb_form_df["feedback_form_SS"].str.contains('Written verbal').any():
    print("yes")

if "Written verbal" in feedb_form_df["feedback_form_SS"].values:
    print("Yep")

feedb_form_df['new'] = feedb_form_df["feedback_form_SS"].str.contains('Written verbal') """

