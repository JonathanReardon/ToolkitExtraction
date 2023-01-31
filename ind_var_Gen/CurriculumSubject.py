from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import curriculum_subjects
from AttributeIDList import other_outcomes_output
from AttributeIDList import which_other_outcomes_output
from AttributeIDList import other_participants_output
import pandas as pd

load_json()

# get curriculum subjects data
curriculumsubjects = get_data(curriculum_subjects)
curriculumsubjects_df = pd.DataFrame(curriculumsubjects)
curriculumsubjects_df = curriculumsubjects_df.T
curriculumsubjects_df.columns = ["test_subject_raw"]

# binarize curriculum subject options
''' curriculumsubjects_df["test_subject_literacy_(first_language)"] = curriculumsubjects_df["test_subject_raw"].map(set(['Literacy (first language)']).issubset).astype(int)
curriculumsubjects_df["test_subject_reading_Comprehension"] = curriculumsubjects_df["test_subject_raw"].map(set(['Reading comprehension']).issubset).astype(int)
curriculumsubjects_df["test_subject_decoding/phonics"] = curriculumsubjects_df["test_subject_raw"].map(set(['Decoding/phonics']).issubset).astype(int)
curriculumsubjects_df["test_subject_spelling"] = curriculumsubjects_df["test_subject_raw"].map(set(['Spelling']).issubset).astype(int)
curriculumsubjects_df["test_subject_reading_other"] = curriculumsubjects_df["test_subject_raw"].map(set(['Reading other']).issubset).astype(int)
curriculumsubjects_df["test_subject_speaking_and_listening/oral_language"] = curriculumsubjects_df["test_subject_raw"].map(set(['Speaking and listening/Oral language']).issubset).astype(int)
curriculumsubjects_df["test_subject_writing"] = curriculumsubjects_df["test_subject_raw"].map(set(['Writing']).issubset).astype(int)
curriculumsubjects_df["test_subject_mathematics"] = curriculumsubjects_df["test_subject_raw"].map(set(['Mathematics']).issubset).astype(int)
curriculumsubjects_df["test_subject_science"] = curriculumsubjects_df["test_subject_raw"].map(set(['Science']).issubset).astype(int)
curriculumsubjects_df["test_subject_social_studies"] = curriculumsubjects_df["test_subject_raw"].map(set(['Social studies']).issubset).astype(int)
curriculumsubjects_df["test_subject_arts"] = curriculumsubjects_df["test_subject_raw"].map(set(['Arts']).issubset).astype(int)
curriculumsubjects_df["test_subject_languages"] = curriculumsubjects_df["test_subject_raw"].map(set(['Languages']).issubset).astype(int)
curriculumsubjects_df["test_subject_other_curriculum_test"] = curriculumsubjects_df["test_subject_raw"].map(set(['Other curriculum test']).issubset).astype(int) '''

# Get Country highlighted text
curriculumsubjects_HT = highlighted_text(curriculum_subjects)
curriculumsubjects_HT_df = pd.DataFrame(curriculumsubjects_HT)
curriculumsubjects_HT_df = curriculumsubjects_HT_df.T
curriculumsubjects_HT_df.columns = ["test_subject_ht"]

# Get Country user comments
curriculumsubjects_Comments = comments(curriculum_subjects)
curriculumsubjects_Comments_df = pd.DataFrame(curriculumsubjects_Comments)
curriculumsubjects_Comments_df = curriculumsubjects_Comments_df.T
curriculumsubjects_Comments_df.columns = ["test_subject_info"]

###########################
# OTHER OUTCOMES REPORTED #
###########################

# get other outcomes data
other_outcomes = get_data(other_outcomes_output)
other_outcomes_df = pd.DataFrame(other_outcomes)
other_outcomes_df = other_outcomes_df.T
other_outcomes_df.columns = ["out_other_raw"]

# get other outcomes highlighted text
other_outcomes_HT = highlighted_text(other_outcomes_output)
other_outcomes_HT_df = pd.DataFrame(other_outcomes_HT)
other_outcomes_HT_df = other_outcomes_HT_df.T
other_outcomes_HT_df.columns = ["out_other_ht"]

# get other outcomes comments
other_outcomes_comments = highlighted_text(other_outcomes_output)
other_outcomes_comments_df = pd.DataFrame(other_outcomes_comments)
other_outcomes_comments_df = other_outcomes_comments_df.T
other_outcomes_comments_df.columns = ["out_other_info"]

########################
# WHICH OTHER OUTCOMES #
########################

# get other outcomes data
which_outcomes = get_data(which_other_outcomes_output)
which_outcomes_df = pd.DataFrame(which_outcomes)
which_outcomes_df = which_outcomes_df.T
which_outcomes_df.columns = ["out_info_raw"]

# get other outcomes highlighted text
which_outcomes_HT = highlighted_text(which_other_outcomes_output)
which_outcomes_HT_df = pd.DataFrame(which_outcomes_HT)
which_outcomes_HT_df = which_outcomes_HT_df.T
which_outcomes_HT_df.columns = ["out_info_ht"]

# get other outcomes comments
which_outcomes_comments = comments(which_other_outcomes_output)
which_outcomes_comments_df = pd.DataFrame(which_outcomes_comments)
which_outcomes_comments_df = which_outcomes_comments_df.T
which_outcomes_comments_df.columns = ["out_info_info"]

#######################
#  OTHER PARTICIPANTS #
#######################

# get other participants highlighted text
other_participants_HT = highlighted_text(other_participants_output)
other_participants_HT_df = pd.DataFrame(other_participants_HT)
other_participants_HT_df = other_participants_HT_df.T
other_participants_HT_df.columns = ["part_other_ht"]

# get other participants comments
other_participants_comments = comments(other_participants_output)
other_participants_comments_df = pd.DataFrame(other_participants_comments)
other_participants_comments_df = other_participants_comments_df.T
other_participants_comments_df.columns = ["part_other_info"]

# concatenate data frames
curriculum_subject_df = pd.concat([
    curriculumsubjects_df, 
    curriculumsubjects_HT_df, 
    curriculumsubjects_Comments_df,
    other_outcomes_df, 
    other_outcomes_HT_df, 
    other_outcomes_comments_df,
    which_outcomes_df, 
    which_outcomes_HT_df, 
    which_outcomes_comments_df,
    other_participants_HT_df, 
    other_participants_comments_df
], axis=1, sort=False)

# fill blanks with NA
curriculum_subject_df.fillna("NA", inplace=True)

# replace problematic text
curriculum_subject_df.replace('\r', ' ', regex=True, inplace=True)
curriculum_subject_df.replace('\n', ' ', regex=True, inplace=True)
curriculum_subject_df.replace(':', ' ', regex=True, inplace=True)
curriculum_subject_df.replace(';', ' ', regex=True, inplace=True)

# save to disk
# curriculum_subject_df.to_csv("curriculumsubjects.csv", index=False)

""" print(curriculum_subject_df) """