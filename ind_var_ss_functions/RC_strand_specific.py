from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import rc_components_output
from AttributeIDList import rc_strat_instruct_type_output
from AttributeIDList import rc_instruct_components_output
from AttributeIDList import rc_txt_type_output

from AttributeIDList import rc_comp_strat_output
from AttributeIDList import rc_comp_vocab_output
from AttributeIDList import rc_comp_red_flu_output
from AttributeIDList import rc_comp_phon_output
from AttributeIDList import rc_comp_wri_output
from AttributeIDList import rc_comp_other_output
from AttributeIDList import rc_comp_unclear_output

import pandas as pd

load_json()

# READING COMPREHENSION

# get rc components data
rc_comp = get_data(rc_components_output)
rc_comp_df = pd.DataFrame(rc_comp)
rc_comp_df = rc_comp_df.T
rc_comp_df.columns = ["rc_comp"]

# split rc components for ind col extraction

# rc comp strat data
rc_comp_strat = get_data(rc_comp_strat_output)
rc_comp_strat_df = pd.DataFrame(rc_comp_strat)
rc_comp_strat_df = rc_comp_strat_df.T
rc_comp_strat_df.columns = ["rc_comp_strat"]

# rc comp vocab data
rc_comp_vocab = get_data(rc_comp_vocab_output)
rc_comp_vocab_df = pd.DataFrame(rc_comp_vocab)
rc_comp_vocab_df = rc_comp_vocab_df.T
rc_comp_vocab_df.columns = ["rc_comp_vocab"]

# rc comp reading fluency data
rc_comp_red_flu = get_data(rc_comp_red_flu_output)
rc_comp_red_flu_df = pd.DataFrame(rc_comp_red_flu)
rc_comp_red_flu_df = rc_comp_red_flu_df.T
rc_comp_red_flu_df.columns = ["rc_comp_red_flu"]

# rc comp phonics fluency data
rc_comp_phon = get_data(rc_comp_phon_output)
rc_comp_phon_df = pd.DataFrame(rc_comp_phon)
rc_comp_phon_df = rc_comp_phon_df.T
rc_comp_phon_df.columns = ["rc_comp_phon"]

# rc comp writing data
rc_comp_wri = get_data(rc_comp_wri_output)
rc_comp_wri_df = pd.DataFrame(rc_comp_wri)
rc_comp_wri_df = rc_comp_wri_df.T
rc_comp_wri_df.columns = ["rc_comp_wri"]

# rc comp other data
rc_comp_other = get_data(rc_comp_other_output)
rc_comp_other_df = pd.DataFrame(rc_comp_other)
rc_comp_other_df = rc_comp_other_df.T
rc_comp_other_df.columns = ["rc_comp_other"]

# rc comp unclear data
rc_comp_unclear = get_data(rc_comp_unclear_output)
rc_comp_unclear_df = pd.DataFrame(rc_comp_unclear)
rc_comp_unclear_df = rc_comp_unclear_df.T
rc_comp_unclear_df.columns = ["rc_comp_unclear"]

# ^^ end of individual column extraction ^^*

# get rc strategy instruction data
rc_strat_instr = get_data(rc_strat_instruct_type_output)
rc_strat_instr_df = pd.DataFrame(rc_strat_instr)
rc_strat_instr_df = rc_strat_instr_df.T
rc_strat_instr_df.columns = ["rc_strat_instruc"]

# get rc instructional components data
rc_instruc_comp = get_data(rc_comp_other_output)
rc_instruc_comp_df = pd.DataFrame(rc_instruc_comp)
rc_instruc_comp_df = rc_instruc_comp_df.T
rc_instruc_comp_df.columns = ["rc_instruc_comp"]

# get rc text type / reading materials data
rc_txt_type = get_data(rc_txt_type_output)
rc_txt_type_df = pd.DataFrame(rc_txt_type)
rc_txt_type_df = rc_txt_type_df.T
rc_txt_type_df.columns = ["rc_txt_type_red_mat"]

rc_ss_df = pd.concat([
    rc_comp_df,
    rc_comp_strat_df,
    rc_comp_vocab_df,
    rc_comp_red_flu_df,
    rc_comp_phon_df,
    rc_comp_wri_df,
    rc_comp_other_df,
    rc_comp_unclear_df,

    rc_strat_instr_df,
    rc_instruc_comp_df,
    rc_txt_type_df,
], axis=1, sort=False)

""" rc_ss_df.to_csv("reading_comprehension_ss.csv", index=False, header=True) """