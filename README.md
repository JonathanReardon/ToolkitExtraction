
<h1 align="center">EEF Toolkit Datafile Extractor</h1>

This command line application is designed to process data files from the [Teaching and Learning Toolkit](https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit?gclid=CjwKCAjwjMiiBhA4EiwAZe6jQ3WnUgowD16xFwcG_6hZySd_qiKcElx5wRI0BjJAdwj5RkFT_kzz1hoCS_MQAvD_BwE) database. It allows you to extract specific dataframes required for data cleaning and analysis purposes. The database provides JSON files with nested structures, and this application simplifies the process of extracting the necessary data, making it easier to integrate into your broader data processing pipeline.

## Dependencies

- Python 3.7 or higher
- numpy 1.22.0
- pandas 1.5.0
- prompt_toolkit 3.0.30
- rich 12.4.4
- toolz 0.11.2

Please make sure you have the above dependencies installed before running the application.

## How to Run

To run the application, follow these steps.

1. Clone this repository:

```bash
>> git clone https://github.com/JonathanReardon/ToolkitExtraction
>> cd ToolkitExtraction
```

2. Install the required dependencies by executing the following command:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
>> python3 main.py
```

<p align="center">
    <img src="/img/visual1.png">
</p>

All output dataframes will be saved within the 'output' directory, with the directory named after the original datafile. Each individual dataframe will be labeled with the original datafile name as a prefix and a dataframe label suffix.

<p align="center">
    <img src="/img/visual2.png">
</p>

## Dataframe 1: Study, Research and Design Variables

<details>
<summary>Further details</summary>

| Variable | Data Type | Column Name |
| ------------- | ----------- | ----------- |
| `Eppi ID`   | `raw` | `id` |
| `Author`   | `raw` | `pub_author` |
| `Year`   | `raw` | `pub_year` |
| `Abstract`   | `raw` | `abstract` |
| `Admin Strand`   | `raw, info` | `strand` |
| `Toolkit Version`   | `raw` | `toolkit_version` |
| `Publication Type EPPI`   | `raw` | `pub_eppi` |
| `Publication Type`   | `raw, ht, info` | `pub_type_raw` |
| `Country`   | `raw` | `loc_country_raw` |
| `Educational Setting`   | `raw, ht, info` | `int_setting` |
| `Study Realism`   | `raw, ht, info` | `eco_valid` |
| `Student Age`   | `raw, ht, info` | `part_age` |
| `Number of Schools Intervention`   | `info, ht` | `school_treat` |
| `Number of Schools Control`   | `info, ht` | `school_cont` |
| `Number of Schools Total`   | `info, ht` | `school_total` |
| `Number of Schools NA`   | `raw, info, ht` | `school_na` |
| `Number of Classes Intervention`   | `info, ht` | `class_treat` |
| `Number of Classes Control`   | `info, ht` | `class_cont` |
| `Number of Classes Total`   | `info, ht` | `class_total` |
| `Number of Classes NA`   | `raw, info, ht` | `class_na` |
| `Treatment Group`   | `raw, ht, info` | `treat_group` |
| `Participant Assignment`   | `raw, ht, info` | `part_assig` |
| `Level of Assignment`   | `raw, ht, info` | `level_assig` |
| `Study Design`   | `raw, ht, info` | `int_desig` |
| `Randomisation`   | `raw, ht, info` | `rand` |
| `Other Outcomes`   | `raw, ht, info` | `out_other` |
| `Additional Outcomes`   | `raw, ht, info` | `out_info` |
| `Other Participants Outcomes`   | `ht, info` | `part_other` |

</details>

## Dataframe 2: Intervention Details

<details>
<summary>Further details</summary>

| Variable | Data Type | Column Name |
| ------------- | ----------- | ----------- |
| `Eppi ID`   | `raw` | `id` |
| `Author`   | `raw` | `pub_author` |
| `Year`   | `raw` | `pub_year` |
| `Admin Strand`   | `raw, info` | `strand` |
| `Toolkit Version`   | `raw` | `toolkit_version` |
| `Intervention Name`   | `ht, info` | `int_name` |
| `Intervention Description`   | `ht, info` | `int_desc` |
| `Intervention Objectives`   | `ht, info` | `int_objec` |
| `Intervention Organization Type`   | `raw, ht, info` | `int_prov` |
| `Intervention Training Provided`   | `raw, ht, info` | `int_training` |
| `Intervention Focus`   | `raw, ht, info` | `int_part` |
| `Intervention Teaching Approach`   | `raw, ht, info` | `int_approach` |
| `Digital Technology`   | `raw, ht, info` | `digit_tech` |
| `Parent Engagement`   | `raw, ht, info` | `parent_partic` |
| `Intervention Time`   | `raw, ht, info` | `int_when` |
| `Intervention Delivery`   | `raw, ht, info` | `int_who` |
| `Intervention Duration`   | `ht, info` | `int_dur` |
| `Intervention Frequency`   | `ht, info` |`int_freq` |
| `Intervention Session Length`   | `ht, info` |`int_leng` |
| `Intervention Detail`   | `raw, ht, info` | `int_fidel` |
| `Intervention Costs`   | `raw, ht, info` | `int_cost` |
| `Intervention Evaluation`   | `raw` | `int_eval` |
| `Baseline Differences`   | `raw, ht, info` | `base_diff` |
| `Comparison Analysis`   | `raw, ht, info` | `comp_anal` |
| `Comparison Variables Reported`   | `raw, ht, info` | `comp_var` |
| `Comparison Variables Reported (Which Ones)` | `raw, ht, info` | `comp_var_rep` |
| `Clustering`   | `raw, ht` | `clust_anal` |

</details>

## Dataframe 3: Sample Size Variables

<details>
<summary>Further details</summary>

| Variable | Data Type | Column Name |
| ------------- | ----------- | ----------- |
| `Eppi ID`   | `raw` | `id` |
| `Author`   | `raw` | `pub_author` |
| `Year`   | `raw` | `pub_year` |
| `Admin Strand`   | `raw, info` | `strand` |
| `Toolkit Version`   | `raw` | `toolkit_version` |
| `Sample Size`   | `info, ht` | `sample_analysed` |
| `Gender`   | `raw, ht, info` | `part_gen` |
| `Low SES Percentage`   | `info, raw` | `fsm_perc` |
| `Further SES Info`   | `info, ht` | `fsm_info` |
| `No Low SES FSM Info`   | `raw, info` | `fsm_na` |
| `Sample Size Intervention`   | `ht, info` | `base_n_treat` |
| `Sample Size Control`   | `ht, info` | `base_n_cont` |
| `Sample Size Second Intervention`   | `ht, info` | `base_n_treat2` |
| `Sample Size Third Intervention`   | `ht, info` | `base_n_treat3` |
| `Sample Size Analysis Intervention`   | `raw, info` | `n_treat` |
| `Sample Size Analysis Control`   | `raw, info` | `n_cont` |
| `Sample Size Analysis Second Intervention`   | `raw, info` | `n_treat2` |
| `Sample Size Analysis Second Control`   | `raw, info` | `n_cont2` |
| `Attrition Dropout Reporting`   | `raw, ht, info` | `attri` |
| `Treatment Group Attrition`   | `ht, info` | `attri_treat` |
| `Overall Percentage Attrition`   | `ht, info` | `attri_perc` |

</details>

## Dataframe 4: Effect Size A [Descriptive Statistics]

<details>
<summary>Further details</summary>

| Variable | Data Type | Column Name |
| ------------- | ----------- | ----------- |
| `Eppi ID`   | `raw` | `id` |
| `Author`   | `raw` | `author` |
| `Year`   | `raw` | `pub_year` |
| `Admin Strand`   | `raw, info` | `strand` |
| `Toolkit Version`   | `raw` | `toolkit_version` |
| `Description Statistics Primary Outcome Reported`   | `raw, ht, info` | `desc_stats` |
| `Intervention Group Number`   | `ht, info` | `n_treat` |
| `Intervention Group Pretest Mean`   | `ht, info` | `pre_t_mean` |
| `Intervention Group Pretest SD`   | `ht, info` | `pre_t_sd` |
| `Intervention Group Posttest Mean`   | `ht, info` | `post_t_mean` |
| `Intervention Group Posttest SD`   | `ht, info` | `post_t_sd` |
| `Intervention Group Gain Score Mean`   | `ht, info` | `gain_t_mean` |
| `Intervention Group Gain Score SD`   | `ht, info` | `gain_t_sd` |
| `Intervention Group Other Info`   | `ht, info` | `out_t_other` |
| `Control Group Number`   | `ht, info` | `n_cont` |
| `Control Group Pretest Mean`   | `ht, info` | `pre_c_mean` |
| `Control Group Pretest SD`   | `ht, info` | `pre_c_sd` |
| `Control Group Posttest Mean`   | `ht, info` | `post_c_mean` |
| `Control Group Posttest SD`   | `ht, info` | `post_c_sd` |
| `Control Group Gain Score Mean`   | `ht, info` | `gain_c_mean` |
| `Control Group Gain Score SD`   | `ht, info` | `gain_c_sd` |
| `Control Group Other Info`   | `ht, info` | `out_c_other` |
| `Intervention Group Number 2`   | `ht, info` | `n_treat2` |
| `Intervention Group Pretest 2 Mean`   | `ht, info` | `pre_t2_mean` |
| `Intervention Group Pretest 2 SD`   | `ht, info` | `pre_t2_sd` |
| `Intervention Group Posttest 2 Mean`   | `ht, info` | `post_t2_mean` |
| `Intervention Group Posttest 2 SD`   | `ht, info` | `post_t2_sd` |
| `Intervention Group Gain Score 2 Mean`   | `ht, info` | `gain_t2_mean` |
| `Intervention Group Gain Score 2 SD`   | `ht, info` | `gain_t2_sd` |
| `Intervention Group Other 2 Info`   | `ht, info` | `out_t2_other` |
| `Control Group Number 2`   | `ht, info` | `n_cont2` |
| `Control Group Pretest 2 Mean`   | `ht, info` | `pre_c2_mean` |
| `Control Group Pretest 2 SD`   | `ht, info` | `pre_c2_sd` |
| `Control Group Posttest 2 Mean`   | `ht, info` | `post_c2_mean` |
| `Control Group Posttest 2 SD`   | `ht, info` | `post_c2_sd` |
| `Control Group Gain Score 2 Mean`   | `ht, info` | `gain_c2_mean` |
| `Control Group Gain Score 2 SD`   | `ht, info` | `gain_c2_sd` |
| `Control Group Other 2 Info`   | `ht, info` | `out_c2_other` |
| `Follow-up Data`   | `raw, ht, info` | `follow_up` |

</details>

## Dataframe 5: Effect Size B [Outcome Details]

<details>
<summary>Further details</summary>

| Variable | Data Type | Column Name |
| ------------- | ----------- | ----------- |
| `Eppi ID`   | `raw` | `id` |
| `Author`   | `raw` | `pub_author` |
| `Year`   | `raw` | `pub_year` |
| `Admin Strand`   | `raw, info` | `strand` |
| `Toolkit Version`   | `raw` | `toolkit_version` |
| `Toolkit Outcome Title` | `raw` | `out_tit_tool` |
| `Toolkit Outcome Description` | `raw` | `out_desc_tool` |
| `Toolkit Primary` | `raw` | `out_type_tool` |
| `Toolkit Primary SMD` | `raw` | `smd_tool` |
| `Toolkit Primary SE`| `raw` | `se_tool` |
| `Toolkit Outcome Measure` | `raw` | `out_measure_tool` |
| `Toolkit Group 1 Sample Size` | `raw` | `out_g1_n_tool` |
| `Toolkit Group 1 Mean` | `raw` | `out_g1_mean_tool` |
| `Toolkit Group 1 Standard Deviation` | `raw` | `out_g1_sd_tool` |
| `Toolkit Group 2 Sample Size` | `raw` | `out_g2_n_tool` |
| `Toolkit Group 2 Mean` | `raw` | `out_g2_mean_tool` |
| `Toolkit Group 2 Standard Deviation` | `raw` | `out_g2_sd_tool` |
| `Toolkit Primary CI Lower` | `raw` | `ci_lower_tool` |
| `Toolkit Primary CI Upper` | `raw` | `ci_upper_tool` |
| `Toolkit Primary Outcome Label` | `raw` | `out_label_tool` |
| `Toolkit Primary Sample Size` | `raw` | `out_samp_tool` |
| `Toolkit Primary Outcome Comparison` | `raw` | `out_comp_tool` |
| `Toolkit Effect Size Type`| `raw` | `out_es_type_tool` |
| `Toolkit Test Type`| `raw` | `out_test_type_raw_tool` |
| `Reading Outcome Title` | `raw` | `out_tit_red` |
| `Reading Outcome Description` | `raw` | `out_desc_red` |
| `Reading Prim` | `raw` | `out_type_red` |
| `Reading Primary SMD` | `raw` | `smd_red` |
| `Reading SE` | `raw` | `se_red` |
| `Reading Outcome Measure` | `raw` | `out_measure_red` |
| `Reading Group 1 Sample Size` | `raw` | `out_g1_n_red` |
| `Reading Group 1 Mean` | `raw` | `out_g1_mean_red` |
| `Reading Group 1 Standard Deviation` | `raw` | `out_g1_sd_red` |
| `Reading Group 2 Sample Size` | `raw` | `out_g2_n_red` |
| `Reading Group 2 Mean` | `raw` | `out_g2_mean_red` |
| `Reading Group 2 Standard Deviation` | `raw` | `out_g2_sd_red` |
| `Reading Confidence Interval Lower` | `raw` | `ci_lower_red` |
| `Reading Confidence Interval Upper` | `raw` | `ci_upper_red` |
| `Reading Outcome Label` | `raw` | `out_label_red` |
| `Reading Sample Size` | `raw` | `out_samp_red` |
| `Reading Outcome Comparison` | `raw` | `out_comp_red` |
| `Reading Effect Size Type` | `raw` | `out_es_type_red` |
| `Reading Test Type` | `raw` | `out_test_type_raw_red` |
| `Writing and Spelling Outcome Title` | `raw` | `out_tit_wri` |
| `Writing and Spelling Outcome Description` | `raw` | `out_desc_wri` |
| `Writing and Spelling Prim` | `raw` | `out_type_wri` |
| `Writing and Spelling Primary SMD` | `raw` | `smd_wri` |
| `Writing and Spelling SE` | `raw` | `se_wri` |
| `Writing and Spelling Outcome Measure` | `raw` | `out_measure_wri` |
| `Writing and Spelling Group 1 Sample Size` | `raw` | `out_g1_n_wri` |
| `Writing and Spelling Group 1 Mean` | `raw` | `out_g1_mean_wri` |
| `Writing and Spelling Group 1 Standard Deviation` | `raw` | `out_g1_sd_wri` |
| `Writing and Spelling Group 2 Sample Size` | `raw` | `out_g2_n_wri` |
| `Writing and Spelling Group 2 Mean` | `raw` | `out_g2_mean_wri` |
| `Writing and Spelling Group 2 Standard Deviation` | `raw` | `out_g2_sd_wri` |
| `Writing and Spelling Confidence Interval Lower` | `raw` | `ci_lower_wri` |
| `Writing and Spelling Confidence Interval Upper` | `raw` | `ci_upper_wri` |
| `Writing and Spelling Outcome Label` | `raw` | `out_label_wri` |
| `Writing and Spelling Sample Size` | `raw` | `out_samp_wri` |
| `Writing and Spelling Outcome Comparison` | `raw` | `out_comp_wri` |
| `Writing and Spelling Effect Size Type` | `raw` | `out_es_type_wri` |
| `Writing and Spelling Test Type` | `raw` | `out_test_type_raw_wri` |
| `Mathematics Outcome Title` | `raw` | `out_tit_math` |
| `Mathematics Outcome Description` | `raw` | `out_desc_math` |
| `Mathematics Prim` | `raw` | `out_type_math` |
| `Mathematics Primary SMD` | `raw` | `smd_math` |
| `Mathematics SE` | `raw` | `se_math` |
| `Mathematics Outcome Measure` | `raw` | `out_measure_math` |
| `Mathematics Group 1 Sample Size` | `raw` | `out_g1_n_math` |
| `Mathematics Group 1 Mean` | `raw` | `out_g1_mean_math` |
| `Mathematics Group 1 Standard Deviation` | `raw` | `out_g1_sd_math` |
| `Mathematics Group 2 Sample Size` | `raw` | `out_g2_n_math` |
| `Mathematics Group 2 Mean` | `raw` | `out_g2_mean_math` |
| `Mathematics Group 2 Standard Deviation` | `raw` | `out_g2_sd_math` |
| `Mathematics Confidence Interval Lower` | `raw` | `ci_lower_math` |
| `Mathematics Confidence Interval Upper` | `raw` | `ci_upper_math` |
| `Mathematics Outcome Label` | `raw` | `out_label_math` |
| `Mathematics Sample Size` | `raw` | `out_samp_math` |
| `Mathematics Outcome Comparison` | `raw` | `out_comp_math` |
| `Mathematics Effect Size Type` | `raw` | `out_es_type_math` |
| `Mathematics Test Type` | `raw` | `out_test_type_raw_math` |
| `Science Outcome Title` | `raw` | `out_tit_sci` |
| `Science Outcome Description` | `raw` | `out_desc_sci` |
| `Science Prim` | `raw` | `out_type_sci` |
| `Science Primary SMD` | `raw` | `smd_sci` |
| `Science SE` | `raw` | `se_sci` |
| `Science Outcome Measure` | `raw` | `out_measure_sci` |
| `Science Group 1 Sample Size` | `raw` | `out_g1_n_sci` |
| `Science Group 1 Mean` | `raw` | `out_g1_mean_sci` |
| `Science Group 1 Standard Deviation` | `raw` | `out_g1_sd_sci` |
| `Science Group 2 Sample Size` | `raw` | `out_g2_n_sci` |
| `Science Group 2 Mean` | `raw` | `out_g2_mean_sci` |
| `Science Group 2 Standard Deviation` | `raw` | `out_g2_sd_sci` |
| `Science Confidence Interval Lower` | `raw` | `ci_lower_sci` |
| `Science Confidence Interval Upper` | `raw` | `ci_upper_sci` |
| `Science Outcome Label` | `raw` | `out_label_sci` |
| `Science Sample Size` | `raw` | `out_samp_sci` |
| `Science Outcome Comparison` | `raw` | `out_comp_sci` |
| `Science Effect Size Type` | `raw` | `out_es_type_sci` |
| `Science Test Type` | `raw` | `out_test_type_raw_sci` |
| `FSM Outcome Title` | `raw` | `out_tit_fsm` |
| `FSM Outcome Description` | `raw` | `out_desc_fsm` |
| `FSM Prim` | `raw` | `out_type_fsm` |
| `FSM Primary SMD` | `raw` | `smd_fsm` |
| `FSM SE` | `raw` | `se_fsm` |
| `FSM Outcome Measure` | `raw` | `out_measure_fsm` |
| `FSM Group 1 Sample Size` | `raw` | `out_g1_n_fsm` |
| `FSM Group 1 Mean` | `raw` | `out_g1_mean_fsm` |
| `FSM Group 1 Standard Deviation` | `raw` | `out_g1_sd_fsm` |
| `FSM Group 2 Sample Size` | `raw` | `out_g2_n_fsm` |
| `FSM Group 2 Mean` | `raw` | `out_g2_mean_fsm` |
| `FSM Group 2 Standard Deviation` | `raw` | `out_g2_sd_fsm` |
| `FSM Confidence Interval Lower` | `raw` | `ci_lower_fsm` |
| `FSM Confidence Interval Upper` | `raw` | `ci_upper_fsm` |
| `FSM Outcome Label` | `raw` | `out_label_fsm` |
| `FSM Sample Size` | `raw` | `out_samp_fsm` |
| `FSM Outcome Comparison` | `raw` | `out_comp_fsm` |
| `FSM Effect Size Type` | `raw` | `out_es_type_fsm` |
| `FSM Test Type` | `raw` | `out_test_type_fsm` |

</details>

## Main Data Analysis Dataframe

<details>
<summary>Further details</summary>

| Variable | Data Type | Column Name |
| ------------- | ----------- | ----------- |
| `Eppi ID`   | `raw` | `id` |
| `Author`   | `raw` | `pub_author` |
| `Year`   | `raw` | `pub_year` |
| `Publication Type`   | `raw` | `pub_type` |
| `Admin Strand`   | `raw, info` | `strand` |
| `Toolkit Version`   | `raw` | `toolkit_version` |
| `Toolkit Outcome`   | `raw` | `out_out_type_tool` |
| `Toolkit SMD`   | `raw` | `smd_tool` |
| `Toolkit SE`   | `raw` | `se_tool` |
| `Toolkit Effect Size Type`   | `raw` | `out_es_type` |
| `Toolkit Outcome Title`   | `raw` | `out_tit` |
| `Toolkit Outcome Comparison`   | `raw` | `out_comp` |
| `Toolkit Sample`   | `raw` | `out_samp` |
| `Toolkit Outcome Measure`   | `raw` | `out_measure` |
| `Toolkit Outcome Test Type`   | `raw` | `out_test_type_raw` |
| `Reading Outcome`   | `raw` | `out_out_type_red` |
| `Reading SMD`   | `raw` | `smd_red` |
| `Reading SE`   | `raw` | `se_red` |
| `Writing and Spelling Outcome`   | `raw` | `out_out_type_wri` |
| `Writing and Spelling SMD`   | `raw` | `smd_wri` |
| `Writing and Spelling SE`   | `raw` | `se_wri` |
| `Mathematics Outcome`   | `raw` | `out_out_type_math` |
| `Mathematics SMD`   | `raw` | `smd_math` |
| `Mathematics SE`   | `raw` | `se_math` |
| `Science Outcome`   | `raw` | `out_out_type_sci` |
| `Science SMD`   | `raw` | `smd_sci` |
| `Science SE`   | `raw` | `se_sci` |
| `FSM Outcome`   | `raw` | `out_out_type_fsm` |
| `FSM SMD`   | `raw` | `smd_fsm` |
| `FSM SE`   | `raw` | `se_fsm` |
| `Sample Analyzed`   | `info` | `sample_analysed` |
| `Number of Schools Total`   | `info` | `school_total` |
| `Number of Classes Total`  | `info` | `class_total` |
| `Intervention Setting`  | `raw` | `int_setting` |
| `Participant Age`  | `raw` | `part_age` |
| `FSM 50` | `raw` | `fsm_50` |
| `FSM Percentage`  | `info` | `fsm_perc` |
| `Country`  | `raw` | `loc_country` |
| `Study Design`  | `raw` | `int_desig` |
| `Intervention Teaching Approach`  | `raw` | `int_approach` |
| `Intervention Training Provided`  | `raw` | `int_training` |
| `Digital Technology`   | `raw` | `digit_tech` |
| `Parent Engagement`   | `raw` | `parent_partic` |
| `Intervention Time`   | `raw` | `int_when` |
| `Intervention Delivery`   | `raw` | `int_who` |
| `Intervention Duration`   | `info` | `int_dur` |
| `Intervention Frequency`   | `info` | `int_freq` |
| `Intervention Session Length`   | `info` | `int_leng` |
| `Oucome Strand`   | `raw` | `out_strand` |

</details>

## Risk of Bias Dataframe

<details>
<summary>Further details</summary>

| Variable | Data Type | Column Name |
| ------------- | ----------- | ----------- |
| `Eppi ID`   | `raw` | `id` |
| `Author`   | `raw` | `pub_author` |
| `Toolkit SMD`   | `raw` | `smd_tool` |
| `Toolkit SE`   | `raw` | `se_tool` |
| `Publication Year`   | `raw, risk label, risk value` | `pub_year` |
| `Strand`   | `raw` | `strand` |
| `Publication Type`   | `raw, risk label, risk value` | `pub_type` |
| `Participant Assignment`   | `raw, risk label, risk value` | `part_assig` |
| `Study Realism`   | `raw, risk label, risk value` | `eco_valid` |
| `School Treatment Group`   | `raw, raw_adjusted, risk label, risk value` | `school_treat` |
| `Intervention Delivery`   | `raw, risk label (ind var split), risk value` | `int_who` |
| `Number of Classes Total`   | `raw, raw_adjusted, risk label, risk value` | `class_total` |
| `Outcome Evaluation`   | `raw, risk label, risk value` | `out_eval` |
| `Computational Analysis`   | `raw, risk label, risk value` | `comp_anal` |
| `Sample Size (Analysed)`   | `raw, risk label, risk value` | `sample_analysed` |
| `Outcome Test Type`   | `raw, risk label, risk value` | `out_test_type` | 
| `Outcome Effect Size Type`   | `raw, risk label, risk value` | `out_es_type` |
| `Attrition Percentage`   | `raw, risk label, risk value` | `attri_perc` |
| `Cluster Analysis`   | `raw, risk label, risk value` | `clust_anal` |
| `Randomisation`   | `raw, risk label, risk value` | `rand` |
| `NA values`   | `raw` | `NA_values` |
| `Mean`   | `raw` | `Mean` |
| `Median`   | `raw` | `Median` |
| `Raw Total`   | `raw` | `raw_total` |

</details>

## References Dataframe

<details>
<summary>Further details</summary>

| Variable | Data Type | Column Name |
| ------------- | ----------- | ----------- |
| `Eppi ID`   | `raw` | `id` |
| `Admin Strand`   | `raw` | `toolkit_strand` |
| `Author`   | `raw` | `short_title` |
| `Authors`   | `raw` | `main_authors` |
| `Year`   | `raw` | `year` |
| `Title`   | `raw` | `main_title` |
| `Parent Title`   | `raw` | `parent_title` |
| `Parent Authors`   | `raw` | `parent_authors` |
| `Type Name`   | `raw` | `type_name` |
| `Abstract`   | `raw` | `abstract` |
| `Volume`   | `raw` | `volume` |
| `Issue`   | `raw` | `issue` |
| `Pages`   | `raw` | `pages` |
| `DOI`   | `raw` | `doi` |
| `URL`   | `raw` | `url` |
| `Publisher`   | `raw` | `publisher` |
| `City`   | `raw` | `city` |
| `Institution`   | `raw` | `institution` |

</details>

## License

Distributed under the MIT License. See LICENSE for more information.
