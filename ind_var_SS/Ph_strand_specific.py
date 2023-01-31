from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import ph_targ_pop_output, ph_constit_part_approach_output, ph_central_teach_lit_output, ph_par_invol_output, ph_digit_tech_output

from AttributeIDList import ph_constit_part_approach_synth_ph
from AttributeIDList import ph_constit_part_approach_syst_ph
from AttributeIDList import ph_constit_part_approach_analyt_ph
from AttributeIDList import ph_constit_part_approach_analog_ph
from AttributeIDList import ph_constit_part_approach_emb_ph
from AttributeIDList import ph_constit_part_approach_phon_aware
from AttributeIDList import ph_constit_part_approach_phonol_aware
from AttributeIDList import ph_constit_part_approach_onset_rime
from AttributeIDList import ph_constit_part_approach_syll_instr
from AttributeIDList import ph_constit_part_approach_sight_vocab
from AttributeIDList import ph_constit_part_approach_whole_word

import pandas as pd

load_json()

# PHONICS

# get phonics target population data
ph_tar_pop = get_data(ph_targ_pop_output)
ph_tar_pop_df = pd.DataFrame(ph_tar_pop)
ph_tar_pop_df = ph_tar_pop_df.T
ph_tar_pop_df.columns = ["ph_targ_pop"]

# get phonics constituent part of approach data
ph_const_part = get_data(ph_constit_part_approach_output)
ph_const_part_df = pd.DataFrame(ph_const_part)
ph_const_part_df = ph_const_part_df.T
ph_const_part_df.columns = ["ph_constit_part"]

# split constituent part (above) for individual column extraction

# constituent part of approach: synthetic phonics
ph_const_part_synth = get_data(ph_constit_part_approach_synth_ph)
ph_const_part_synth_df = pd.DataFrame(ph_const_part_synth)
ph_const_part_synth_df = ph_const_part_synth_df.T
ph_const_part_synth_df.columns = ["ph_constit_part_synth_phon"]

# constituent part of approach: systematic phonics
ph_const_part_sys = get_data(ph_constit_part_approach_syst_ph)
ph_const_part_sys_df = pd.DataFrame(ph_const_part_sys)
ph_const_part_sys_df = ph_const_part_sys_df.T
ph_const_part_sys_df.columns = ["ph_constit_part_sys_phon"]

# constituent part of approach: analytic phonics
ph_const_part_analyt = get_data(ph_constit_part_approach_analyt_ph)
ph_const_part_analyt_df = pd.DataFrame(ph_const_part_analyt)
ph_const_part_analyt_df = ph_const_part_analyt_df.T
ph_const_part_analyt_df.columns = ["ph_constit_part_analyt_phon"]

# constituent part of approach: analog phonics
ph_const_part_analog = get_data(ph_constit_part_approach_analog_ph)
ph_const_part_analog_df = pd.DataFrame(ph_const_part_analog)
ph_const_part_analog_df = ph_const_part_analog_df.T
ph_const_part_analog_df.columns = ["ph_constit_part_analog_phon"]

# constituent part of approach: embedded phonics
ph_const_part_emb = get_data(ph_constit_part_approach_emb_ph)
ph_const_part_emb_df = pd.DataFrame(ph_const_part_emb)
ph_const_part_emb_df = ph_const_part_emb_df.T
ph_const_part_emb_df.columns = ["ph_constit_part_emb_phon"]

# constituent part of approach: phonemic awareness
ph_const_part_phon_aware = get_data(ph_constit_part_approach_phon_aware)
ph_const_part_phon_aware_df = pd.DataFrame(ph_const_part_phon_aware)
ph_const_part_phon_aware_df = ph_const_part_phon_aware_df.T
ph_const_part_phon_aware_df.columns = ["ph_constit_part_phonem_aware"]

# constituent part of approach: phonological awareness
ph_const_part_phonol_aware = get_data(ph_constit_part_approach_phonol_aware)
ph_const_part_phonol_aware_df = pd.DataFrame(ph_const_part_phonol_aware)
ph_const_part_phonol_aware_df = ph_const_part_phonol_aware_df.T
ph_const_part_phonol_aware_df.columns = ["ph_constit_part_phonol_aware"]

# constituent part of approach: onset - rime
ph_const_part_onset_rime = get_data(ph_constit_part_approach_onset_rime)
ph_const_part_onset_rime_df = pd.DataFrame(ph_const_part_onset_rime)
ph_const_part_onset_rime_df = ph_const_part_onset_rime_df.T
ph_const_part_onset_rime_df.columns = ["ph_constit_part_onset_rime"]

# constituent part of approach: syllable instruction
ph_const_part_syll_instr = get_data(ph_constit_part_approach_syll_instr)
ph_const_part_syll_instr_df = pd.DataFrame(ph_const_part_syll_instr)
ph_const_part_syll_instr_df = ph_const_part_syll_instr_df.T
ph_const_part_syll_instr_df.columns = ["ph_constit_part_syll_instr"]

# constituent part of approach: sight vocab
ph_const_part_sight_vocab = get_data(ph_constit_part_approach_sight_vocab)
ph_const_part_sight_vocab_df = pd.DataFrame(ph_const_part_sight_vocab)
ph_const_part_sight_vocab_df = ph_const_part_sight_vocab_df.T
ph_const_part_sight_vocab_df.columns = ["ph_constit_part_sight_vocab"]

# constituent part of approach: whole word
ph_const_part_whole_word = get_data(ph_constit_part_approach_whole_word)
ph_const_part_whole_word_df = pd.DataFrame(ph_const_part_whole_word)
ph_const_part_whole_word_df = ph_const_part_whole_word_df.T
ph_const_part_whole_word_df.columns = ["ph_constit_part_whole_word"]

#^^ end of individual column extraction above ^^

# get phonics central to approach data
ph_central_to_approach = get_data(ph_central_teach_lit_output)
ph_central_to_approach_df = pd.DataFrame(ph_central_to_approach)
ph_central_to_approach_df = ph_central_to_approach_df.T
ph_central_to_approach_df.columns = ["ph_central_to_approach"]

# get phonics parental involvement data
ph_par_invol = get_data(ph_par_invol_output)
ph_par_invol_df = pd.DataFrame(ph_par_invol)
ph_par_invol_df = ph_par_invol_df.T
ph_par_invol_df.columns = ["ph_par_invol"]

# get phonics parental involvement data
ph_dig_tech = get_data(ph_digit_tech_output)
ph_dig_tech_df = pd.DataFrame(ph_dig_tech)
ph_dig_tech_df = ph_dig_tech_df.T
ph_dig_tech_df.columns = ["ph_dig_tech"]

ph_ss_df = pd.concat([
    ph_tar_pop_df,
    ph_const_part_df,

    ph_const_part_synth_df,
    ph_const_part_sys_df,
    ph_const_part_analyt_df,
    ph_const_part_analog_df,
    ph_const_part_emb_df,
    ph_const_part_phon_aware_df,
    ph_const_part_phonol_aware_df,
    ph_const_part_onset_rime_df,
    ph_const_part_syll_instr_df,
    ph_const_part_sight_vocab_df,
    ph_const_part_whole_word_df,

    ph_central_to_approach_df,
    ph_par_invol_df,
    ph_dig_tech_df
], axis=1, sort=False)

# fill blanks with NA
ph_ss_df.fillna("NA", inplace=True)

# save to disk
ph_ss_df.to_csv("phonics_ss.csv", index=False)

print(ph_ss_df[0:50])