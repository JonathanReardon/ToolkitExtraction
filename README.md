
[<img alt="" src="https://img.shields.io/pypi/v/eef-data?label=PyPI%20Package" />](https://pypi.org/project/eef-data/)


<h1 align="center">

EEF Datafile Extractor

</h1>

The EEF Datafile Extractor is an application designed to streamline the processing of data files from the [EEF](https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit?gclid=CjwKCAjwjMiiBhA4EiwAZe6jQ3WnUgowD16xFwcG_6hZySd_qiKcElx5wRI0BjJAdwj5RkFT_kzz1hoCS_MQAvD_BwE) Education Evidence Database. The database provides JSON files with complex, nested structures, and our toolkit simplifies the process of extracting the necessary data, making it easier to integrate into your broader data processing pipeline. We provide a collection of bespoke dataframes specifically tailored for data cleaning and analysis. In addition to the pre-built dataframes, the tool includes a custom dataframe builder. This feature empowers you to compile your own dataframes based on your specific research requirements.

## Installing

Install with `pip` or your favorite PyPI package manager.

``` bash
>> pip install eef-data
```

and simply run from the command line..

``` bash
>> eef-data
```

When you run eef-data, you will be asked to input a data file. Once you have done so, press enter to proceed to the main menu.

<p align="center">
<img src="/eefdata/img/visual1.png"/>
</p>

When a selection is made, the newly created file location will be displayed in the "Output Files" box at the bottom of the display.

<p align="center">
<img src="/eefdata/img/visual2.png"/>
</p>

Each individual dataframe will be labeled with the original datafile name as a prefix and a dataframe label suffix.

## Dataframe 1: Study, Research and Design Variables

This dataframe contains 'raw', 'ht', 'info', and 'CLEAN' data types.

| Data Type | Description | Number of Columns |
| --- | --- | :----: |
|  `_raw` | raw data as input by the data coders | 21 |
|  `_ht` | text highlighted from the manuscript | 20 |
|  `_info` | any 'user' entered info | 21 |
| `_CLEAN`  | empty columns for data cleaning notes | 23 |
|   | **Total Number of Columns** | **85** |

<details>
<summary>Study, Research, and Design Column Summary</summary>

| Variable                         | Data Type       | Column Name       |
|----------------------------------|-----------------|-------------------|
| `Eppi ID`                        | `raw`           | `id`              |
| `Author`                         | `raw`           | `pub_author`      |
| `Year`                           | `raw`           | `pub_year`        |
| `Abstract`                       | `raw`           | `abstract`        |
| `Admin Strand`                   | `raw, info`     | `strand`      |
| `Toolkit Version`                | `raw`           | `toolkit_version` |
| `Publication Type EPPI`          | `raw`           | `pub_eppi`        |
| `Publication Type`               | `raw, ht, info` | `pub_type_raw`    |
| `Country`                        | `raw`           | `loc_country_raw` |
| `Educational Setting`            | `raw, ht, info` | `int_setting`     |
| `Study Realism`                  | `raw, ht, info` | `eco_valid`       |
| `Student Age`                    | `raw, ht, info` | `part_age`        |
| `Number of Schools Intervention` | `info, ht`      | `school_treat`    |
| `Number of Schools Control`      | `info, ht`      | `school_cont`     |
| `Number of Schools Total`        | `info, ht`      | `school_total`    |
| `Number of Schools NA`           | `raw, info, ht` | `school_na`       |
| `Number of Classes Intervention` | `info, ht`      | `class_treat`     |
| `Number of Classes Control`      | `info, ht`      | `class_cont`      |
| `Number of Classes Total`        | `info, ht`      | `class_total`     |
| `Number of Classes NA`           | `raw, info, ht` | `class_na`        |
| `Treatment Group`                | `raw, ht, info` | `treat_group`     |
| `Participant Assignment`         | `raw, ht, info` | `part_assig`      |
| `Level of Assignment`            | `raw, ht, info` | `level_assig`     |
| `Study Design`                   | `raw, ht, info` | `int_desig`       |
| `Randomisation`                  | `raw, ht, info` | `rand`            |
| `Other Outcomes`                 | `raw, ht, info` | `out_other`       |
| `Additional Outcomes`            | `raw, ht, info` | `out_info`        |
| `Other Participants Outcomes`    | `ht, info`      | `part_other`      |

</details>

## Dataframe 2: Intervention Details

This dataframe contains 'raw', 'ht', 'info', and 'CLEAN' data types.

| Data Type | Description | Number of Columns |
| --- | --- | :----: |
|  `_raw` | raw data as input by the data coders | 23 |
|  `_ht` | text highlighted from the manuscript | 21 |
|  `_info` | any 'user' entered info | 21 |
| `_CLEAN`  | empty columns for data cleaning notes | 22 |
|   | **Total Number of Columns** | **86** |

<details>
<summary>Intervention Details Column Summary</summary>

| Variable                                     | Data Type       | Column Name       |
|----------------------------------------------|-----------------|-------------------|
| `Eppi ID`                                    | `raw`           | `id`              |
| `Author`                                     | `raw`           | `pub_author`      |
| `Year`                                       | `raw`           | `pub_year`        |
| `Admin Strand`                               | `raw, info`     | `strand`      |
| `Toolkit Version`                            | `raw`           | `toolkit_version` |
| `Intervention Name`                          | `ht, info`      | `int_name`        |
| `Intervention Description`                   | `ht, info`      | `int_desc`        |
| `Intervention Objectives`                    | `ht, info`      | `int_objec`       |
| `Intervention Organization Type`             | `raw, ht, info` | `int_prov`        |
| `Intervention Training Provided`             | `raw, ht, info` | `int_training`    |
| `Intervention Focus`                         | `raw, ht, info` | `int_part`        |
| `Intervention Teaching Approach`             | `raw, ht, info` | `int_approach`    |
| `Digital Technology`                         | `raw, ht, info` | `digit_tech`      |
| `Parent Engagement`                          | `raw, ht, info` | `parent_partic`   |
| `Intervention Time`                          | `raw, ht, info` | `int_when`        |
| `Intervention Delivery`                      | `raw, ht, info` | `int_who`         |
| `Intervention Duration`                      | `ht, info`      | `int_dur`         |
| `Intervention Frequency`                     | `ht, info`      | `int_freq`        |
| `Intervention Session Length`                | `ht, info`      | `int_leng`        |
| `Intervention Detail`                        | `raw, ht, info` | `int_fidel`       |
| `Intervention Costs`                         | `raw, ht, info` | `int_cost`        |
| `Intervention Evaluation`                    | `raw`           | `int_eval`        |
| `Baseline Differences`                       | `raw, ht, info` | `base_diff`       |
| `Comparison Analysis`                        | `raw, ht, info` | `comp_anal`       |
| `Comparison Variables Reported`              | `raw, ht, info` | `comp_var`        |
| `Comparison Variables Reported (Which Ones)` | `raw, ht, info` | `comp_var_rep`    |
| `Clustering`                                 | `raw, ht`       | `clust_anal`      |

</details>

## Dataframe 3: Sample Size Variables

This dataframe contains 'raw', 'ht', 'info', and 'CLEAN' data types.

| Data Type | Description | Number of Columns |
| --- | --- | :----: |
|  `_raw` | raw data as input by the data coders | 9 |
|  `_ht` | text highlighted from the manuscript | 15 |
|  `_info` | any 'user' entered info | 16 |
| `_CLEAN`  | empty columns for data cleaning notes | 17 |
|   | **Total Number of Columns** | **57** |

<details>
<summary>Sample Size Column Summary</summary>

| Variable                                   | Data Type       | Column Name       |
|--------------------------------------------|-----------------|-------------------|
| `Eppi ID`                                  | `raw`           | `id`              |
| `Author`                                   | `raw`           | `pub_author`      |
| `Year`                                     | `raw`           | `pub_year`        |
| `Admin Strand`                             | `raw, info`     | `strand`      |
| `Toolkit Version`                          | `raw`           | `toolkit_version` |
| `Sample Size`                              | `info, ht`      | `sample_analysed` |
| `Gender`                                   | `raw, ht, info` | `part_gen`        |
| `Low SES Percentage`                       | `info, raw`     | `fsm_perc`        |
| `Further SES Info`                         | `info, ht`      | `fsm_info`        |
| `No Low SES FSM Info`                      | `raw, info`     | `fsm_na`          |
| `Sample Size Intervention`                 | `ht, info`      | `base_n_treat`    |
| `Sample Size Control`                      | `ht, info`      | `base_n_cont`     |
| `Sample Size Second Intervention`          | `ht, info`      | `base_n_treat2`   |
| `Sample Size Third Intervention`           | `ht, info`      | `base_n_treat3`   |
| `Sample Size Analysis Intervention`        | `raw, info`     | `n_treat`         |
| `Sample Size Analysis Control`             | `raw, info`     | `n_cont`          |
| `Sample Size Analysis Second Intervention` | `raw, info`     | `n_treat2`        |
| `Sample Size Analysis Second Control`      | `raw, info`     | `n_cont2`         |
| `Attrition Dropout Reporting`              | `raw, ht, info` | `attri`           |
| `Treatment Group Attrition`                | `ht, info`      | `attri_treat`     |
| `Overall Percentage Attrition`             | `ht, info`      | `attri_perc`      |

</details>

## Dataframe 4: Effect Size A \[Descriptive Statistics\]

This dataframe contains 'raw', 'ht', 'info', and 'CLEAN' data types.

| Data Type | Description | Number of Columns |
| --- | --- | :----: |
|  `_raw` | raw data as input by the data coders | 7 |
|  `_ht` | text highlighted from the manuscript | 34 |
|  `_info` | any 'user' entered info | 35 |
| `_CLEAN`  | empty columns for data cleaning notes | 34 |
|   | **Total Number of Columns** | **110** |

<details>
<summary>Effect Size A Column Summary</summary>

| Variable                                          | Data Type       | Column Name       |
|---------------------------------------------------|-----------------|-------------------|
| `Eppi ID`                                         | `raw`           | `id`              |
| `Author`                                          | `raw`           | `author`          |
| `Year`                                            | `raw`           | `pub_year`        |
| `Admin Strand`                                    | `raw, info`     | `strand`      |
| `Toolkit Version`                                 | `raw`           | `toolkit_version` |
| `Description Statistics Primary Outcome Reported` | `raw, ht, info` | `desc_stats`      |
| `Intervention Group Number`                       | `ht, info`      | `n_treat`         |
| `Intervention Group Pretest Mean`                 | `ht, info`      | `pre_t_mean`      |
| `Intervention Group Pretest SD`                   | `ht, info`      | `pre_t_sd`        |
| `Intervention Group Posttest Mean`                | `ht, info`      | `post_t_mean`     |
| `Intervention Group Posttest SD`                  | `ht, info`      | `post_t_sd`       |
| `Intervention Group Gain Score Mean`              | `ht, info`      | `gain_t_mean`     |
| `Intervention Group Gain Score SD`                | `ht, info`      | `gain_t_sd`       |
| `Intervention Group Other Info`                   | `ht, info`      | `out_t_other`     |
| `Control Group Number`                            | `ht, info`      | `n_cont`          |
| `Control Group Pretest Mean`                      | `ht, info`      | `pre_c_mean`      |
| `Control Group Pretest SD`                        | `ht, info`      | `pre_c_sd`        |
| `Control Group Posttest Mean`                     | `ht, info`      | `post_c_mean`     |
| `Control Group Posttest SD`                       | `ht, info`      | `post_c_sd`       |
| `Control Group Gain Score Mean`                   | `ht, info`      | `gain_c_mean`     |
| `Control Group Gain Score SD`                     | `ht, info`      | `gain_c_sd`       |
| `Control Group Other Info`                        | `ht, info`      | `out_c_other`     |
| `Intervention Group Number 2`                     | `ht, info`      | `n_treat2`        |
| `Intervention Group Pretest 2 Mean`               | `ht, info`      | `pre_t2_mean`     |
| `Intervention Group Pretest 2 SD`                 | `ht, info`      | `pre_t2_sd`       |
| `Intervention Group Posttest 2 Mean`              | `ht, info`      | `post_t2_mean`    |
| `Intervention Group Posttest 2 SD`                | `ht, info`      | `post_t2_sd`      |
| `Intervention Group Gain Score 2 Mean`            | `ht, info`      | `gain_t2_mean`    |
| `Intervention Group Gain Score 2 SD`              | `ht, info`      | `gain_t2_sd`      |
| `Intervention Group Other 2 Info`                 | `ht, info`      | `out_t2_other`    |
| `Control Group Number 2`                          | `ht, info`      | `n_cont2`         |
| `Control Group Pretest 2 Mean`                    | `ht, info`      | `pre_c2_mean`     |
| `Control Group Pretest 2 SD`                      | `ht, info`      | `pre_c2_sd`       |
| `Control Group Posttest 2 Mean`                   | `ht, info`      | `post_c2_mean`    |
| `Control Group Posttest 2 SD`                     | `ht, info`      | `post_c2_sd`      |
| `Control Group Gain Score 2 Mean`                 | `ht, info`      | `gain_c2_mean`    |
| `Control Group Gain Score 2 SD`                   | `ht, info`      | `gain_c2_sd`      |
| `Control Group Other 2 Info`                      | `ht, info`      | `out_c2_other`    |
| `Follow-up Data`                                  | `raw, ht, info` | `follow_up`       |

</details>

## Dataframe 5: Effect Size B \[Outcome Details\]

This dataframe contains 'raw', 'info', and 'CLEAN' data types.

| Data Type | Description | Number of Columns |
| --- | --- | :----: |
|  `_raw` | raw data as input by the data coders | 118 |
|  `_ht` | text highlighted from the manuscript | 0 |
|  `_info` | any 'user' entered info | 1 |
| `_CLEAN`  | empty columns for data cleaning notes | 113 |
|   | **Total Number of Columns** | **232** |

<details>
<summary>Effect Size B Column Summary</summary>

| Variable                                          | Data Type   | Column Name              |
|---|---|---|
| `Eppi ID`                                         | `raw`       | `id`                     |
| `Author`                                          | `raw`       | `pub_author`             |
| `Year`                                            | `raw`       | `pub_year`               |
| `Admin Strand`                                    | `raw, info` | `strand`                 |
| `Toolkit Version`                                 | `raw`       | `toolkit_version`        |
| `Toolkit Outcome Title`                           | `raw`       | `out_tit_tool`           |
| `Toolkit Outcome Description`                     | `raw`       | `out_desc_tool`          |
| `Toolkit Primary`                                 | `raw`       | `out_type_tool`          |
| `Toolkit Primary SMD`                             | `raw`       | `smd_tool`               |
| `Toolkit Primary SE`                              | `raw`       | `se_tool`                |
| `Toolkit Outcome Measure`                         | `raw`       | `out_measure_tool`       |
| `Toolkit Group 1 Sample Size`                     | `raw`       | `out_g1_n_tool`          |
| `Toolkit Group 1 Mean`                            | `raw`       | `out_g1_mean_tool`       |
| `Toolkit Group 1 Standard Deviation`              | `raw`       | `out_g1_sd_tool`         |
| `Toolkit Group 2 Sample Size`                     | `raw`       | `out_g2_n_tool`          |
| `Toolkit Group 2 Mean`                            | `raw`       | `out_g2_mean_tool`       |
| `Toolkit Group 2 Standard Deviation`              | `raw`       | `out_g2_sd_tool`         |
| `Toolkit Primary CI Lower`                        | `raw`       | `ci_lower_tool`          |
| `Toolkit Primary CI Upper`                        | `raw`       | `ci_upper_tool`          |
| `Toolkit Primary Outcome Label`                   | `raw`       | `out_label_tool`         |
| `Toolkit Primary Sample Size`                     | `raw`       | `out_samp_tool`          |
| `Toolkit Primary Outcome Comparison`              | `raw`       | `out_comp_tool`          |
| `Toolkit Effect Size Type`                        | `raw`       | `out_es_type_tool`       |
| `Toolkit Test Type`                               | `raw`       | `out_test_type_raw_tool` |
| `Reading Outcome Title`                           | `raw`       | `out_tit_red`            |
| `Reading Outcome Description`                     | `raw`       | `out_desc_red`           |
| `Reading Prim`                                    | `raw`       | `out_type_red`           |
| `Reading Primary SMD`                             | `raw`       | `smd_red`                |
| `Reading SE`                                      | `raw`       | `se_red`                 |
| `Reading Outcome Measure`                         | `raw`       | `out_measure_red`        |
| `Reading Group 1 Sample Size`                     | `raw`       | `out_g1_n_red`           |
| `Reading Group 1 Mean`                            | `raw`       | `out_g1_mean_red`        |
| `Reading Group 1 Standard Deviation`              | `raw`       | `out_g1_sd_red`          |
| `Reading Group 2 Sample Size`                     | `raw`       | `out_g2_n_red`           |
| `Reading Group 2 Mean`                            | `raw`       | `out_g2_mean_red`        |
| `Reading Group 2 Standard Deviation`              | `raw`       | `out_g2_sd_red`          |
| `Reading Confidence Interval Lower`               | `raw`       | `ci_lower_red`           |
| `Reading Confidence Interval Upper`               | `raw`       | `ci_upper_red`           |
| `Reading Outcome Label`                           | `raw`       | `out_label_red`          |
| `Reading Sample Size`                             | `raw`       | `out_samp_red`           |
| `Reading Outcome Comparison`                      | `raw`       | `out_comp_red`           |
| `Reading Effect Size Type`                        | `raw`       | `out_es_type_red`        |
| `Reading Test Type`                               | `raw`       | `out_test_type_raw_red`  |
| `Writing and Spelling Outcome Title`              | `raw`       | `out_tit_wri`            |
| `Writing and Spelling Outcome Description`        | `raw`       | `out_desc_wri`           |
| `Writing and Spelling Prim`                       | `raw`       | `out_type_wri`           |
| `Writing and Spelling Primary SMD`                | `raw`       | `smd_wri`                |
| `Writing and Spelling SE`                         | `raw`       | `se_wri`                 |
| `Writing and Spelling Outcome Measure`            | `raw`       | `out_measure_wri`        |
| `Writing and Spelling Group 1 Sample Size`        | `raw`       | `out_g1_n_wri`           |
| `Writing and Spelling Group 1 Mean`               | `raw`       | `out_g1_mean_wri`        |
| `Writing and Spelling Group 1 Standard Deviation` | `raw`       | `out_g1_sd_wri`          |
| `Writing and Spelling Group 2 Sample Size`        | `raw`       | `out_g2_n_wri`           |
| `Writing and Spelling Group 2 Mean`               | `raw`       | `out_g2_mean_wri`        |
| `Writing and Spelling Group 2 Standard Deviation` | `raw`       | `out_g2_sd_wri`          |
| `Writing and Spelling Confidence Interval Lower`  | `raw`       | `ci_lower_wri`           |
| `Writing and Spelling Confidence Interval Upper`  | `raw`       | `ci_upper_wri`           |
| `Writing and Spelling Outcome Label`              | `raw`       | `out_label_wri`          |
| `Writing and Spelling Sample Size`                | `raw`       | `out_samp_wri`           |
| `Writing and Spelling Outcome Comparison`         | `raw`       | `out_comp_wri`           |
| `Writing and Spelling Effect Size Type`           | `raw`       | `out_es_type_wri`        |
| `Writing and Spelling Test Type`                  | `raw`       | `out_test_type_raw_wri`  |
| `Mathematics Outcome Title`                       | `raw`       | `out_tit_math`           |
| `Mathematics Outcome Description`                 | `raw`       | `out_desc_math`          |
| `Mathematics Prim`                                | `raw`       | `out_type_math`          |
| `Mathematics Primary SMD`                         | `raw`       | `smd_math`               |
| `Mathematics SE`                                  | `raw`       | `se_math`                |
| `Mathematics Outcome Measure`                     | `raw`       | `out_measure_math`       |
| `Mathematics Group 1 Sample Size`                 | `raw`       | `out_g1_n_math`          |
| `Mathematics Group 1 Mean`                        | `raw`       | `out_g1_mean_math`       |
| `Mathematics Group 1 Standard Deviation`          | `raw`       | `out_g1_sd_math`         |
| `Mathematics Group 2 Sample Size`                 | `raw`       | `out_g2_n_math`          |
| `Mathematics Group 2 Mean`                        | `raw`       | `out_g2_mean_math`       |
| `Mathematics Group 2 Standard Deviation`          | `raw`       | `out_g2_sd_math`         |
| `Mathematics Confidence Interval Lower`           | `raw`       | `ci_lower_math`          |
| `Mathematics Confidence Interval Upper`           | `raw`       | `ci_upper_math`          |
| `Mathematics Outcome Label`                       | `raw`       | `out_label_math`         |
| `Mathematics Sample Size`                         | `raw`       | `out_samp_math`          |
| `Mathematics Outcome Comparison`                  | `raw`       | `out_comp_math`          |
| `Mathematics Effect Size Type`                    | `raw`       | `out_es_type_math`       |
| `Mathematics Test Type`                           | `raw`       | `out_test_type_raw_math` |
| `Science Outcome Title`                           | `raw`       | `out_tit_sci`            |
| `Science Outcome Description`                     | `raw`       | `out_desc_sci`           |
| `Science Prim`                                    | `raw`       | `out_type_sci`           |
| `Science Primary SMD`                             | `raw`       | `smd_sci`                |
| `Science SE`                                      | `raw`       | `se_sci`                 |
| `Science Outcome Measure`                         | `raw`       | `out_measure_sci`        |
| `Science Group 1 Sample Size`                     | `raw`       | `out_g1_n_sci`           |
| `Science Group 1 Mean`                            | `raw`       | `out_g1_mean_sci`        |
| `Science Group 1 Standard Deviation`              | `raw`       | `out_g1_sd_sci`          |
| `Science Group 2 Sample Size`                     | `raw`       | `out_g2_n_sci`           |
| `Science Group 2 Mean`                            | `raw`       | `out_g2_mean_sci`        |
| `Science Group 2 Standard Deviation`              | `raw`       | `out_g2_sd_sci`          |
| `Science Confidence Interval Lower`               | `raw`       | `ci_lower_sci`           |
| `Science Confidence Interval Upper`               | `raw`       | `ci_upper_sci`           |
| `Science Outcome Label`                           | `raw`       | `out_label_sci`          |
| `Science Sample Size`                             | `raw`       | `out_samp_sci`           |
| `Science Outcome Comparison`                      | `raw`       | `out_comp_sci`           |
| `Science Effect Size Type`                        | `raw`       | `out_es_type_sci`        |
| `Science Test Type`                               | `raw`       | `out_test_type_raw_sci`  |
| `FSM Outcome Title`                               | `raw`       | `out_tit_fsm`            |
| `FSM Outcome Description`                         | `raw`       | `out_desc_fsm`           |
| `FSM Prim`                                        | `raw`       | `out_type_fsm`           |
| `FSM Primary SMD`                                 | `raw`       | `smd_fsm`                |
| `FSM SE`                                          | `raw`       | `se_fsm`                 |
| `FSM Outcome Measure`                             | `raw`       | `out_measure_fsm`        |
| `FSM Group 1 Sample Size`                         | `raw`       | `out_g1_n_fsm`           |
| `FSM Group 1 Mean`                                | `raw`       | `out_g1_mean_fsm`        |
| `FSM Group 1 Standard Deviation`                  | `raw`       | `out_g1_sd_fsm`          |
| `FSM Group 2 Sample Size`                         | `raw`       | `out_g2_n_fsm`           |
| `FSM Group 2 Mean`                                | `raw`       | `out_g2_mean_fsm`        |
| `FSM Group 2 Standard Deviation`                  | `raw`       | `out_g2_sd_fsm`          |
| `FSM Confidence Interval Lower`                   | `raw`       | `ci_lower_fsm`           |
| `FSM Confidence Interval Upper`                   | `raw`       | `ci_upper_fsm`           |
| `FSM Outcome Label`                               | `raw`       | `out_label_fsm`          |
| `FSM Sample Size`                                 | `raw`       | `out_samp_fsm`           |
| `FSM Outcome Comparison`                          | `raw`       | `out_comp_fsm`           |
| `FSM Effect Size Type`                            | `raw`       | `out_es_type_fsm`        |
| `FSM Test Type`                                   | `raw`       | `out_test_type_fsm`      |

</details>

## Main Data Analysis Dataframe

This dataframe contains 'raw' and 'info' data types, as well as one custom defined 'fsm_50' column which returns a value of 'TRUE' where fsm_perc_info (percentage of students on free school meals) is 50 or above, and 'FALSE' for values below  50.

| Data Type | Description | Number of Columns |
| --- | --- | :----: |
|  `_raw` | raw data as input by the data coders | 40 |
|  `_ht` | text highlighted from the manuscript | 0 |
|  `_info` | any 'user' entered info | 7 |
| `_CLEAN`  | empty columns for data cleaning notes | 0 |
| `*custom*`  | user defined calculation | 1 |
|   | **Total Number of Columns** | **48**<sup>1</sup> |

<sup>1</sup>This refers to the total number of columns without the addition of strand specific columns, which will increase the overall column count.

<details>
<summary>Main Analysis Column Summary</summary>

| Variable                         | Data Type   | Column Name         |
|---|---|---|
| `Eppi ID`                        | `raw`       | `id`                |
| `Author`                         | `raw`       | `pub_author`        |
| `Year`                           | `raw`       | `pub_year`          |
| `Publication Type`               | `raw`       | `pub_type`          |
| `Admin Strand`                   | `raw`       | `strand`            |
| `Toolkit Version`                | `raw`       | `toolkit_version`   |
| `Toolkit Outcome`                | `raw`       | `out_out_type_tool` |
| `Toolkit SMD`                    | `raw`       | `smd_tool`          |
| `Toolkit SE`                     | `raw`       | `se_tool`           |
| `Toolkit Effect Size Type`       | `raw`       | `out_es_type`       |
| `Toolkit Outcome Title`          | `raw`       | `out_tit`           |
| `Toolkit Outcome Comparison`     | `raw`       | `out_comp`          |
| `Toolkit Sample`                 | `raw`       | `out_samp`          |
| `Toolkit Outcome Measure`        | `raw`       | `out_measure`       |
| `Toolkit Outcome Test Type`      | `raw`       | `out_test_type_raw` |
| `Reading Outcome`                | `raw`       | `out_out_type_red`  |
| `Reading SMD`                    | `raw`       | `smd_red`           |
| `Reading SE`                     | `raw`       | `se_red`            |
| `Writing and Spelling Outcome`   | `raw`       | `out_out_type_wri`  |
| `Writing and Spelling SMD`       | `raw`       | `smd_wri`           |
| `Writing and Spelling SE`        | `raw`       | `se_wri`            |
| `Mathematics Outcome`            | `raw`       | `out_out_type_math` |
| `Mathematics SMD`                | `raw`       | `smd_math`          |
| `Mathematics SE`                 | `raw`       | `se_math`           |
| `Science Outcome`                | `raw`       | `out_out_type_sci`  |
| `Science SMD`                    | `raw`       | `smd_sci`           |
| `Science SE`                     | `raw`       | `se_sci`            |
| `FSM Outcome`                    | `raw`       | `out_out_type_fsm`  |
| `FSM SMD`                        | `raw`       | `smd_fsm`           |
| `FSM SE`                         | `raw`       | `se_fsm`            |
| `Sample Analyzed`                | `info`      | `sample_analysed`   |
| `Number of Schools Total`        | `info`      | `school_total`      |
| `Number of Classes Total`        | `info`      | `class_total`       |
| `Intervention Setting`           | `raw`       | `int_setting`       |
| `Participant Age`                | `raw`       | `part_age`          |
| `FSM 50`                         | `raw`       | `fsm_50`            |
| `FSM Percentage`                 | `info`      | `fsm_perc`          |
| `Country`                        | `raw`       | `loc_country`       |
| `Study Design`                   | `raw`       | `int_desig`         |
| `Intervention Teaching Approach` | `raw`       | `int_approach`      |
| `Intervention Training Provided` | `raw`       | `int_training`      |
| `Digital Technology`             | `raw`       | `digit_tech`        |
| `Parent Engagement`              | `raw`       | `parent_partic`     |
| `Intervention Time`              | `raw`       | `int_when`          |
| `Intervention Delivery`          | `raw`       | `int_who`           |
| `Intervention Duration`          | `info`      | `int_dur`           |
| `Intervention Frequency`         | `info`      | `int_freq`          |
| `Intervention Session Length`    | `info`      | `int_leng`          |
| `Oucome Strand`                  | `raw`       | `out_strand`        |

</details>

## Outcome Data

This dataframe contains only 'raw' data type, and displays unordered outcome information (outcome type and label).

| Data Type | Description | Number of Columns |
| --- | --- | :----: |
|  `_raw` | raw data as input by the data coders | ALL |
|  `_ht` | text highlighted from the manuscript | 0 |
|  `_info` | any 'user' entered info | 0 |
| `_CLEAN`  | empty columns for data cleaning notes | 0 |
| `*custom*`  | user defined calculation | 0 |
|   | **Total Number of Columns** | **NA**<sup>1</sup> |

<sup>1</sup>Total number of columns will depend on the study with the maximum number of outcomes.

<details>
<summary>Outcome Data Column Summary</summary>

| Variable                         | Data Type   | Column Name         |
|---|---|---|
| `Eppi ID`             | `raw`       | `id`                |
| `Publication Author`  | `raw`       | `pub_author`        |
| `Outcome 1 Type`      | `raw`       | `pub_year`          |
| `Outcome 1 Label`     | `raw`       | `pub_type`          |
| `Outcome 2 Type`      | `raw`       | `strand`            |
| `Outcome 2 Type`      | `raw`       | `toolkit_version`   |
| `...`                 | `...`       | `...` |
</details>

## Study Security

This dataframe contains 'raw' and 'info' data types, as well as 44 custom columns used to assess the variables considered to be at risk of affecting research validity or bias.

| Data Type | Description | Number of Columns |
| --- | --- | :----: |
|  `_raw` | raw data as input by the data coders | 17 |
|  `_ht` | text highlighted from the manuscript | 0 |
|  `_info` | any 'user' entered info | 3 |
| `_CLEAN`  | empty columns for data cleaning notes | 0 |
| `*custom*`  | user defined calculation | 44 |
|   | **Total Number of Columns** | **64** |

### Study Security Risk Assessment

14 variables are currently identified as having the potential to negatively affect study validity or introduce bias. Values associated with these variables are converted to a 3 point scale (high/medium/low risk).

<details>
<summary>Risk Assessment Condition Table</Summary>

| Variable | Condition | Risk |
| --- | --- | --- |
| `Publication Year`                | `< 1980`                                     | `High Risk`      |
|                                   | `> 1979 and < 2000`                          | `Medium Risk`    |
|                                   | `> 1999`                                     | `Low Risk`       |
| `Attrition %`                     | `> 19`                                       | `High Risk`      |
|                                   | `> 9 and < 20`                               | `Medium Risk`    |
|                                   | `< 10`                                       | `Low Risk`       |
| `Cluster Analysis`                | `Yes`                                        | `Medium Risk`    |
|                                   | `No`                                         | `High Risk`      |
| `Outcome Effect Size Type`        | `Post-test unadjusted`                       | `High Risk`      |
|                                   | `Pre-post gain`                              | `Medium Risk`    |
|                                   | `Post-test adjusted for baseline attainment` | `Low Risk`       |
| `Outcome Test Type`               | `Test type: Researcher developed test`       | `High Risk`      |
|                                   | `Test type: School-developed test`           | `Medium Risk`    |
|                                   | `Test type: Standardised test`               | `Low Risk`       |
|                                   | `Test type: National test`                   | `Low Risk`       |
|                                   | `Test type: International tests`             | `Low Risk`       |
| `Sample Size`                     | `<= 30`                                      | `High Risk`      |
|                                   | `> 30 and < 100`                             | `Medium Risk`    |
|                                   | `"Test type: Standardised test`              | `Low Risk`       |
|                                   | `> 99`                                       | `Low Risk`       |
| `Publication Type`                | `Book or book chapter`                       | `Medium Risk`    |
|                                   | `Conference paper`                           | `Medium Risk`    |
|                                   | `Other`                                      | `Medium Risk`    |
|                                   | `Journal article`                            | `Low Risk`       |
|                                   | `Dissertation or thesis`                     | `Low Risk`       |
|                                   | `Technical report`                           | `Low Risk`       |
| `Participant Assignment`          | `Regression discontinuity`                   | `Medium Risk`    |
|                                   | `Retrospective Quasi Experimental Design`    | `Medium Risk`    |
|                                   | `Not assigned - naturally occurring sample`  | `Medium Risk`    |
|                                   | `Unclear`                                    | `Medium Risk`    |
|                                   | `Non-random, not matched prior to treatment` | `Medium Risk`    |
|                                   | `Non-random, but matched`                    | `Medium Risk`    |
|                                   | `Random`                                     | `Low Risk`       |
| `Randomisation`                   | `No/Unclear`                                 | `Medium Risk`    |
|                                   | `Not applicable`                             | `Medium Risk`    |
|                                   | `Yes`                                        | `Low Risk`       |
| `Ecological Validity`             | `Unclear`                                    | `High Risk`      |
|                                   | `Low ecological validity`                    | `High Risk`      |
|                                   | `High ecological validity`                   | `Low Risk`       |
| `Number of Schools`               | `1`                                          | `High Risk`      |
|                                   | `> 1 and < 6`                                | `Medium Risk`    |
|                                   | `> 5`                                        | `Low Risk`       |
| `Number of Classes`               | `1`                                          | `High Risk`      |
|                                   | `> 1 and < 6`                                | `Medium Risk`    |
|                                   | `> 5`                                        | `Low Risk`       |
| `Intervention Delivery`           | `Unclear/not specified`                      | `High Risk`      |
|                                   | `Peers`                                      | `High Risk`      |
|                                   | `Digital technology`                         | `High Risk`      |
|                                   | `Lay persons/volunteers`                     | `Medium Risk`    |
|                                   | `Teaching assistants`                        | `Medium Risk`    |
|                                   | `Digital technology`                         | `Medium Risk`    |
|                                   | `Parents/carers`                             | `Medium Risk`    |
|                                   | `External teachers`                          | `Medium Risk`    |
|                                   | `Class teachers`                             | `Low Risk`       |
| `Intervention Evaluation`         | `The developer`                              | `Medium Risk`    |
|                                   | `A different organization paid by developer` | `Medium Risk`    |
|                                   | `Unclear/not stated`                         | `Medium Risk`    |
|                                   | `An organization commissioned independently to evaluate` | `Low Risk` |
| `Comparability`                   | `No`                                         | `Medium Risk`    |
|                                   | `Unclear or details not provided`            | `Medium Risk`    |
|                                   | `Yes`                                        | `Low Risk`       |
</details>

<details>
<summary>Study Security Column Summary</summary>

| Variable                   | Data Type                                     | Column Name       |
|---|---|---|
| `Eppi ID`                  | `raw`                                         | `id`              |
| `Author`                   | `raw`                                         | `pub_author`      |
| `Toolkit SMD`              | `raw`                                         | `smd_tool`        |
| `Toolkit SE`               | `raw`                                         | `se_tool`         |
| `Publication Year`         | `raw, custom, custom`                         | `pub_year`        |
| `Strand`                   | `raw`                                         | `strand`          |
| `Publication Type`         | `raw, custom, custom`                         | `pub_type`        |
| `Participant Assignment`   | `raw, custom, custom`                         | `part_assig`      |
| `Study Realism`            | `raw, custom, custom`                         | `eco_valid`       |
| `School Treatment Group`   | `raw, raw_adjusted, custom, custom`           | `school_treat`    |
| `Intervention Delivery`    | `raw, custom (ind var split), custom`         | `int_who`         |
| `Number of Classes Total`  | `raw, raw_adjusted, custom, custom`           | `class_total`     |
| `Outcome Evaluation`       | `raw, custom, custom`                         | `out_eval`        |
| `Computational Analysis`   | `raw, custom, custom`                         | `comp_anal`       |
| `Sample Size (Analysed)`   | `raw, custom, custom`                         | `sample_analysed` |
| `Outcome Test Type`        | `raw, custom, custom`                         | `out_test_type`   |
| `Outcome Effect Size Type` | `raw, custom, custom`                         | `out_es_type`     |
| `Attrition Percentage`     | `raw, custom, custom`                         | `attri_perc`      |
| `Cluster Analysis`         | `raw, custom, custom`                         | `clust_anal`      |
| `Randomisation`            | `raw, custom, custom`                         | `rand`            |
| `NA values`                | `raw`                                         | `NA_values`       |
| `Mean`                     | `raw`                                         | `Mean`            |
| `Median`                   | `raw`                                         | `Median`          |
| `Raw Total`                | `raw`                                         | `raw_total`       |

</details>

## Strand Padlocks

This dataframe, consisting of raw and custom data types, contains one strand-specific row where a set of key variables, thought to affect strand quality, are mapped to a 3 point scale: low, medium, and high risk. Each strand begins with an initial padlock value based on the number of studies it contains. For each of the 5 key padlock values, if any are "High Risk", we subtract 1 from the initial padlock value. The end result is the strands final padlock value. If a strand ends on a padlock value of 0 AND contains 10 or more studies (and has therefore been meta-analysed), its value is raised to 1.

This dataframe can be thought of as the overall "strand" version of the study-level "Study Security" dataframe.

| Data Type   | Description                           | Number of Columns |
| ----------- | ------------------------------------- | :---------------: |
|  `_raw`     | raw data as input by the data coders  | 7                 |
|  `_ht`      | text highlighted from the manuscript  | 0                 |
|  `_info`    | any 'user' entered info               | 0                 |
| `_CLEAN`    | empty columns for data cleaning notes | 0                 |
| `*custom*`  | user defined calculation              | 8                 |
|             | **Total Number of Columns**           | **15**            |

### Strand Padlocks Risk Assessment

6 variables are currently identified as having the potential to negatively affect strand-level quality and/or validity. Values associated with these variables are converted to a 3 point risk value scale ('Condition'/'Risk' columns).

<details>
<summary>Strand Padlocks Condition Table</summary>

| Variable | Condition | Risk |
| --- | --- | --- |
| `Number of Studies`                     | `< 10`              | `0`           |
|                                         | `> 9 and < 25`      | `1`           |
|                                         | `> 24 and < 35`     | `2`           |
|                                         | `> 34 and < 60`     | `3`           |
|                                         | `> 59 and < 90`     | `4`           |
|                                         | `> 89`              | `5`           |
| `% Studies since 2000`                  | `> 49`              | `Low Risk`    |
|                                         | `> 25 and < 50`     | `Medium Risk` |
|                                         | `< 25`              | `High Risk`   |
| `% Studies randomised`                  | `< 30`              | `High Risk`   |
|                                         | `> 29 and < 60`     | `Medium Risk` |
|                                         | `> 59`              | `Low Risk`    |
| `% Studies w/ high ecological validity` | `< 50`              | `High Risk`   |
|                                         | `> 49 and < 75`     | `Medium Risk` |
|                                         | `> 74`              | `Low Risk`    |
| `% Studies independently evaluated`     | `< 10`              | `High Risk`   |
|                                         | `< 9 and < 30`      | `Medium Risk` |
|                                         | `> 29`              | `Low Risk`    |
| `% Median attrition reported`           | `< 15`              | `Low Risk`    |
|                                         | `> 14 and   30`     | `Medium Risk` |
|                                         | `> 29`              | `High Risk`   |
</details>

<details>
<summary>Strand Padlocks Column Summary</summary>

| Variable | Data Type | Column Name |
|---|---|---|
| `Strand`                                     | `raw`             | `strand`                    |
| `Filename`                                   | `raw`             | `filename`                  |
| `Number of studies`                          | `raw`             | `num_of_studies`            |
| `Number of studies PS`                       | `custom`          | `num_of_studies_ps`         |
| `% Studies since 2000`                       | `raw`             | `%_since_2000`              |
| `% Studies since 2000 PS`                    | `custom`          | `%_since_2000_ps`           |
| `% Studies randomised`                       | `raw`             | `%_randomised`              |
| `% Studies randomised PS`                    | `custom`          | `%_randomised_ps`           |
| `% Studies w/ high ecological validity`      | `raw`             | `%_high_eco_valid`          |
| `% Studies w/ high ecological validity PS`   | `custom`          | `%_high_eco_valid_ps`       |
| `% Studies independently evaluated`          | `raw`             | `%_indep_eval`              |
| `% Studies independently evaluated PS`       | `custom`          | `%_indep_eval_ps`           |
| `% Median attrition reported`                | `raw`             | `%_med_attrit_reported`     |
| `% Median attrition reporeted PS`            | `custom`          | `%_med_attrit_reported_ps`  |
| `MA floor`                                   | `custom`          | `MA_Floor`                  |
| `Padlock Value`                              | `custom`          | `New_padlock`               |
</details>

## References Dataframe

This dataframe contains only raw values extracted in order to construct study references.

| Data Type   | Description                           | Number of Columns |
| ----------- | ------------------------------------- | :---------------: |
|  `_raw`     | raw data as input by the data coders  | 18                |
|  `_ht`      | text highlighted from the manuscript  | 0                 |
|  `_info`    | any 'user' entered info               | 0                 |
| `_CLEAN`    | empty columns for data cleaning notes | 0                 |
|             | **Total Number of Columns**           | **18**            |

<details>
<summary>References Column Summary</summary>

| Variable         | Data Type | Column Name      |
|------------------|-----------|------------------|
| `Eppi ID`        | `raw`     | `id`             |
| `Admin Strand`   | `raw`     | `toolkit_strand` |
| `Author`         | `raw`     | `short_title`    |
| `Authors`        | `raw`     | `main_authors`   |
| `Year`           | `raw`     | `year`           |
| `Title`          | `raw`     | `main_title`     |
| `Parent Title`   | `raw`     | `parent_title`   |
| `Parent Authors` | `raw`     | `parent_authors` |
| `Type Name`      | `raw`     | `type_name`      |
| `Abstract`       | `raw`     | `abstract`       |
| `Volume`         | `raw`     | `volume`         |
| `Issue`          | `raw`     | `issue`          |
| `Pages`          | `raw`     | `pages`          |
| `DOI`            | `raw`     | `doi`            |
| `URL`            | `raw`     | `url`            |
| `Publisher`      | `raw`     | `publisher`      |
| `City`           | `raw`     | `city`           |
| `Institution`    | `raw`     | `institution`    |

</details>

## Custom Column Selection

Custom column selections consist of the data the user chooses from a pre-defined list of column options.

| Data Type   | Description                           | Number of Columns   |
| ----------- | ------------------------------------- | :-----------------: |
|  `_raw`     | raw data as input by the data coders  | 127                 |
|  `_ht`      | text highlighted from the manuscript  | 43                 |
|  `_info`    | any 'user' entered info               | 43                  |
| `_CLEAN`    | empty columns for data cleaning notes | 0                   |
|             | **Total Number of Columns**           | **213**<sup>1</sup> |

<sup>1</sup>213 is the maximum number of columns where are all data are selected.

<details>
<summary>Custom Dataframe Selection Column Summary</summary>

| Variable                                    | Data Type | Column Name         |
| ------------------------------------------- | --------- | ------------------- |
| `Study ID`                                   | `raw`     | `id`                |
| `Publication Author`                        | `raw`     | `pub_author`        |
| `Publication Year`                          | `raw`     | `pub_year`          |
| `Abstract`                                  | `raw`     | `abstract`          |
| `Strand`                                    | `raw`     | `strand_raw`        |
| `Country`                                   | `raw`     | `loc_country_raw`   |
| `Publication Type (EPPI)`                   | `raw`     | `pub_eppi`          |
| `Publication Type`                          | `raw`     | `pub_type_raw`      |
| `Participant Age`                           | `raw`     | `part_age_raw`      |
| `Ecological Validity`                       | `raw`     | `eco_valid_raw`     |
| `Intervention Number of Schools (info)`     | `info`    | `school_treat_info` |
| `Intervention Number of Schools (ht)`       | `ht`      | `school_treat_ht`   |
| `Control Number of Schools (info)`          | `info`    | `school_cont_info`  |
| `Control Number of Schools (ht)`            | `ht`      | `school_cont_ht`    |
| `Total Number of Schools (info)`            | `info`    | `school_total_info` |
| `Total Number of Schools (ht)`              | `ht`      | `school_total_ht`   |
| `Intervention Number of Classes (info)`     | `info`    | `class_treat_info`  |
| `Intervention Number of Schools (ht)`       | `ht`      | `class_treat_ht`    |
| `Control Number of ClassesClasses (info)`   | `info`    | `class_cont_info`   |
| `Control Number of Schools (ht)`            | `ht`      | `class_cont_ht`     |
| `Total Number of Classes (info)`            | `info`    | `class_total_info`  |
| `Total Number of Classes (ht)`              | `ht`      | `class_total_ht`    |
| `Participant Assignment`                    | `raw`     | `part_assig_raw`    |
| `Participant Assignmen (ht)`                | `ht`      | `part_assig_ht`     |
| `Participant Assignmen (info)`              | `info`    | `part_assig_info`   |
| `Level of Assignment`                       | `raw`     | `level_assig_raw`   |
| `Level of Assignmen (ht)`                   | `ht`      | `level_assig_ht`    |
| `Level of Assignmen (info)`                 | `info`    | `level_assig_info`  |
| `Study Design`                              | `raw`     | `int_desig_raw`     |
| `Study Design (ht)`                         | `ht`      | `int_design_ht`     |
| `Study Design (info)`                       | `info`    | `int_design_info`   |
| `Randomisation`                             | `raw`     | `rand_raw`          |
| `Randomisation (ht)`                        | `ht`      | `rand_ht`           |
| `Randomisation (info)`                      | `info`    | `rand_info`         |
| `Toolkit Primary Outcome Title`             | `raw`  | `out_tit_tool`       |
| `Toolkit Primary Outcome Description`       | `raw`  | `out_desc_tool`      |
| `Toolkit Primary Outcome Type`              | `raw`  | `out_type_tool`      |
| `Toolkit Primary Outcome SMD`               | `raw`  | `smd_tool`           |
| `Toolkit Primary Outcome SE`                | `raw`  | `se_tool`            |
| `Toolkit Primary Outcome CI (lower)`        | `raw`  | `ci_lower_tool`      |
| `Toolkit Primary Outcome CI (upper)`        | `raw`  | `ci_upper_tool`      |
| `Toolkit Primary Outcome Measure`           | `raw`  | `out_measure_tool`   |
| `Toolkit Primary Outcome Group1 N`          | `raw`  | `out_g1_n_tool`      |
| `Toolkit Primary Outcome Group1 Mean`       | `raw`  | `out_g1_mean_tool`   |
| `Toolkit Primary Outcome Group1 SD`         | `raw`  | `out_g1_sd_tool`     |
| `Toolkit Primary Outcome Group2 N`          | `raw`  | `out_g2_n_tool`      |
| `Toolkit Primary Outcome Group2 Mean`       | `raw`  | `out_g2_mean_tool`   |
| `Toolkit Primary Outcome Group2 SD`         | `raw`  | `out_g2_sd_tool`     |
| `Toolkit Primary Outcome Test Type`         | `raw`  | `out_test_type_raw_` |
| `Toolkit Primary Outcome Effect Size Type`  | `raw`  | `out_es_type_tool`   |
| `Reading Outcome Title`                     | `raw`  | `out_tit_red`        |
| `Reading Outcome Description`               | `raw`  | `out_desc_red`       |
| `Reading Outcome Type`                      | `raw`  | `out_type_red`       |
| `Reading Outcome SMD`                       | `raw`  | `smd_red`            |
| `Reading Outcome SE`                        | `raw`  | `se_red`             |
| `Reading Outcome CI (lower)`                | `raw`  | `ci_lower_red`       |
| `Reading Outcome CI (upper)`                | `raw`  | `ci_upper_red`       |
| `Reading Outcome Measure`                   | `raw`  | `out_measure_red`    |
| `Reading Outcome Group1 N`                  | `raw`  | `out_g1_n_red`       |
| `Reading Outcome Group1 Mean`               | `raw`  | `out_g1_mean_red`    |
| `Reading Outcome Group1 SD`                 | `raw`  | `out_g1_sd_red`      |
| `Reading Outcome Group2 N`                  | `raw`  | `out_g2_n_red`       |
| `Reading Outcome Group2 Mean`               | `raw`  | `out_g2_mean_red`    |
| `Reading Outcome Group2 SD`                 | `raw`  | `out_g2_sd_red`      |
| `Reading Outcome Test Type`                 | `raw`  | `out_test_type_raw_red` |
| `Reading Outcome Effect Size Type`          | `raw`  | `out_es_type_red`    |
| `Writing Outcome Title`                     | `raw`  | `out_tit_wri`        |
| `Writing Outcome Description`               | `raw`  | `out_desc_wri`       |
| `Writing Outcome Type`                      | `raw`  | `out_type_wri`       |
| `Writing Outcome SMD`                       | `raw`  | `smd_wri`            |
| `Writing Outcome SE`                        | `raw`  | `se_wri`             |
| `Writing Outcome CI (lower)`                | `raw`  | `ci_lower_wri`       |
| `Writing Outcome CI (upper)`                | `raw`  | `ci_upper_wri`       |
| `Writing Outcome Measure`                   | `raw`  | `out_measure_wri`    |
| `Writing Outcome Group1 N`                  | `raw`  | `out_g1_n_wri`       |
| `Writing Outcome Group1 Mean`               | `raw`  | `out_g1_mean_wri`    |
| `Writing Outcome Group1 SD`                 | `raw`  | `out_g1_sd_wri`      |
| `Writing Outcome Group2 N`                  | `raw`  | `out_g2_n_wri`       |
| `Writing Outcome Group2 Mean`               | `raw`  | `out_g2_mean_wri`    |
| `Writing Outcome Group2 SD`                 | `raw`  | `out_g2_sd_wri`      |
| `Writing Outcome Test Type`                 | `raw`  | `out_test_type_raw_wri` |
| `Writing Outcome Effect Size Type`          | `raw`  | `out_es_type_wri`    |
| `Math Outcome Title`                        | `raw`  | `out_tit_math`       |
| `Math Outcome Description`                  | `raw`  | `out_desc_math`      |
| `Math Outcome Type`                         | `raw`  | `out_type_math`      |
| `Math Outcome SMD`                          | `raw`  | `smd_math`           |
| `Math Outcome SE`                           | `raw`  | `se_math`            |
| `Math Outcome CI (lower)`                   | `raw`  | `ci_lower_math`      |
| `Math Outcome CI (upper)`                   | `raw`  | `ci_upper_math`      |
| `Math Outcome Measure`                      | `raw`  | `out_measure_math`   |
| `Math Outcome Group1 N`                     | `raw`  | `out_g1_n_math`      |
| `Math Outcome Group1 Mean`                  | `raw`  | `out_g1_mean_math`   |
| `Math Outcome Group1 SD`                    | `raw`  | `out_g1_sd_math`     |
| `Math Outcome Group2 N`                     | `raw`  | `out_g2_n_math`      |
| `Math Outcome Group2 Mean`                  | `raw`  | `out_g2_mean_math`   |
| `Math Outcome Group2 SD`                    | `raw`  | `out_g2_sd_math`     |
| `Math Outcome Test Type`                    | `raw`  | `out_test_type_raw_math` |
| `Math Outcome Effect Size Type`             | `raw`  | `out_es_type_math`   |
| `Science Outcome Title`                     | `raw`  | `out_tit_sci`        |
| `Science Outcome Description`               | `raw`  | `out_desc_sci`       |
| `Science Outcome Type`                      | `raw`  | `out_type_sci`       |
| `Science Outcome SMD`                       | `raw`  | `smd_sci`            |
| `Science Outcome SE`                        | `raw`  | `se_sci`             |
| `Science Outcome CI (lower)`                | `raw`  | `ci_lower_sci`       |
| `Science Outcome CI (upper)`                | `raw`  | `ci_upper_sci`       |
| `Science Outcome Measure`                   | `raw`  | `out_measure_sci`    |
| `Science Outcome Group1 N`                  | `raw`  | `out_g1_n_sci`       |
| `Science Outcome Group1 Mean`               | `raw`  | `out_g1_mean_sci`    |
| `Science Outcome Group1 SD`                 | `raw`  | `out_g1_sd_sci`      |
| `Science Outcome Group2 N`                  | `raw`  | `out_g2_n_sci`       |
| `Science Outcome Group2 Mean`               | `raw`  | `out_g2_mean_sci`    |
| `Science Outcome Group2 SD`                 | `raw`  | `out_g2_sd_sci`      |
| `Science Outcome Test Type`                 | `raw`  | `out_test_type_raw_sci` |
| `Science Outcome Effect Size Type`          | `raw`  | `out_es_type_sci`    |
| `FSM Outcome Title`                         | `raw`  | `out_tit_fsm`        |
| `FSM Outcome Description`                   | `raw`  | `out_desc_fsm`       |
| `FSM Outcome Type`                          | `raw`  | `out_type_fsm`       |
| `FSM Outcome SMD`                           | `raw`  | `smd_fsm`            |
| `FSM Outcome SE`                            | `raw`  | `se_fsm`             |
| `FSM Outcome CI (lower)`                    | `raw`  | `ci_lower_fsm`       |
| `FSM Outcome CI (upper)`                    | `raw`  | `ci_upper_fsm`       |
| `FSM Outcome Measure`                       | `raw`  | `out_measure_fsm`    |
| `FSM Outcome Group1 N`                      | `raw`  | `out_g1_n_fsm`       |
| `FSM Outcome Group1 Mean`                   | `raw`  | `out_g1_mean_fsm`    |
| `FSM Outcome Group1 SD`                     | `raw`  | `out_g1_sd_fsm`      |
| `FSM Outcome Group2 N`                      | `raw`  | `out_g2_n_fsm`       |
| `FSM Outcome Group2 Mean`                   | `raw`  | `out_g2_mean_fsm`    |
| `FSM Outcome Group2 SD`                     | `raw`  | `out_g2_sd_fsm`      |
| `FSM Outcome Test Type`                     | `raw`  | `out_test_type_raw_fsm` |
| `FSM Outcome Effect Size Type`              | `raw`  | `out_es_type_fsm`    |
| `Intervention Name (ht)`                     | `ht`  | `int_name_ht`   |
| `Intervention Name (info)`                     | `info`  | `int_name_info`   |
| `Intervention Description (ht)`                     | `ht`  | `int_desc_ht`   |
| `Intervention Description (info)`                     | `info`  | `int_desc_info`   |
| `Intervention Objective (ht)`                     | `ht`  | `int_objec_ht`   |
| `Intervention Objective (info)`                     | `info`  | `int_objec_info`   |
| `Intervention Training`                     | `raw`  | `int_training_raw`   |
| `Intervention Training (ht)`                | `ht`   | `int_training_ht`    |
| `Intervention Training (info)`              | `info` | `int_training_info`  |
| `Intervention Approach`                     | `raw`  | `int_approach_raw`   |
| `Intervention Approach (ht)`                | `ht`   | `int_approach_ht`    |
| `Intervention Approach (info)`              | `info` | `int_approach_info`  |
| `Digital Technology`                        | `raw`  | `digit_tech_raw`     |
| `Digital Technology (ht)`                   | `ht`   | `digit_tech_ht`      |
| `Digital Technology (info)`                 | `info` | `digit_tech_info`    |
| `Parental Participation`                    | `raw`  | `parent_partic_raw`  |
| `Parental Participation (ht)`               | `ht`   | `parent_partic_ht`   |
| `Parental Participation (info)`             | `info` | `parent_partic_info` |
| `Intervention When`                         | `raw`  | `int_when_raw`       |
| `Intervention When (ht)`                    | `ht`   | `int_when_ht`        |
| `Intervention When (info)`                  | `info` | `int_when_info`      |
| `Intervention Delivery`                     | `raw`  | `int_who_raw`        |
| `Intervention Delivery (ht)`                | `ht`   | `int_who_ht`         |
| `Intervention Delivery (info)`              | `info` | `int_who_info`       |
| `Intervention Duration (ht)`                | `ht`   | `int_dur_ht`         |
| `Intervention Duration (info)`              | `info` | `int_dur_info`       |
| `Intervention Length (ht)`                  | `ht`   | `int_leng_ht`        |
| `Intervention Length (info)`                | `info` | `int_leng_info`      |
| `Intervention Setting`                      | `raw`  | `int_setting_raw`    |
| `Intervention Setting (ht)`                 | `ht`   | `int_setting_ht`     |
| `Intervention Setting (info)`               | `info` | `int_setting_info`   |
| `Intervention Focus`                      | `raw`  | `int_part_raw`    |
| `Intervention Focus (ht)`                 | `ht`   | `int_part_ht`     |
| `Intervention Focus (info)`               | `info` | `int_part_info`   |
| `Intervention Detail`                      | `raw`  | `int_fidel_raw`    |
| `Intervention Detail (ht)`                 | `ht`   | `int_fidel_ht`     |
| `Intervention Detail (info)`               | `info` | `int_fidel_info`   |
| `Intervention Cost`                      | `raw`  | `int_cost_raw`    |
| `Intervention Cost (ht)`                 | `ht`   | `int_cost_ht`     |
| `Intervention Cost (info)`               | `info` | `int_cost_info`   |
| `Baseline Differences (raw)`              | `raw`  | `base_diff_raw`    |
| `Baseline Differences (ht)`               | `ht`   | `base_diff_ht`     |
| `Baseline Differences (info)`             | `info` | `base_diff_info`   |
| `Comparability (raw)`              | `raw`  | `comp_anal_raw`    |
| `Comparability (ht)`               | `ht`   | `comp_anal_ht`     |
| `Comparability (info)`             | `info` | `comp_anal_info`   |
| `Comparability Reported`              | `raw`  | `comp_var__raw`    |
| `Comparability Reported (ht)`               | `ht`   | `comp_var__ht`     |
| `Comparability Reported (info)`             | `info` | `comp_var__info`   |
| `Which Comp Var Reported`              | `raw`  | `comp_var_rep_raw`    |
| `Which Comp Var Reported (ht)`               | `ht`   | `comp_var_rep_ht`     |
| `Which Comp Var Reported (info)`             | `info` | `comp_var_rep_info`   |
| `Clustering`              | `raw`  | `clust_anal_raw`    |
| `Clustering (ht)`               | `ht`   | `clust_anal_ht`     |
| `Clustering (info)`             | `info` | `clust_anal_info`   |
| `Student Gender`              | `raw`  | `part_gen_raw`    |
| `Student Gender (ht)`               | `ht`   | `part_gen_ht`     |
| `Student Gender (info)`             | `info` | `part_gen_info`   |
| `Sample Size (ht)`               | `ht`   | `sample_analysed_ht`     |
| `Sample Size (info)`             | `info` | `sample_analysed_info`   |
| `Intervention Sample Size (ht)`             | `ht` | `base_n_treat_ht`   |
| `Intervention Sample Size (info)`             | `info` | `base_n_treat_info`   |
| `Control Sample Size (ht)`             | `ht` | `base_n_cont_ht`   |
| `Control Sample Size (info)`             | `info` | `base_n_cont_info`   |
| `Intervention 2 Sample Size (ht)`             | `ht` | `base_n_treat2_ht`   |
| `Intervention 2 Sample Size (info)`             | `info` | `base_n_treat2_info`   |
| `Intervention 3 Sample Size (ht)`             | `ht` | `base_n_treat3_ht`   |
| `Intervention 3 Sample Size (info)`             | `info` | `base_n_treat3_info`   |
| `Intervention Sample Size Analyzed (ht)`             | `ht` | `n_treat_ht`   |
| `Intervention Sample Size Analyzed (info)`             | `info` | `n_treat_info`   |
| `Control Sample Size Analyzed (ht)`             | `ht` | `n_cont_ht`   |
| `Control Sample Size Analyzed (info)`             | `info` | `n_cont_info`   |
| `Intervention 2 Sample Size Analyzed (ht)`             | `ht` | `n_treat2_ht`   |
| `Intervention 2 Sample Size Analyzed (info)`             | `info` | `n_treat2_info`   |
| `Control 2 Sample Size Analyzed (ht)`             | `ht` | `n_cont2_ht`   |
| `Control 2 Sample Size  (info)`             | `info` | `n_cont2_info`   |
| `Attrition Reported`             | `raw` | `attri_raw`   |
| `Attrition Reported (ht)`             | `ht` | `attri_ht`   |
| `Attrition Reported (info)`             | `info` | `attri_info`   |
| `Treatment Group Attrition (ht)`             | `ht` | `attri_treat_ht`   |
| `Treatment Group Attrition (info)`             | `info` | `attri_treat_info`   |
| `Total % Attrition (ht)`             | `ht` | `attri_perc_ht`   |
| `Total % Attrition (info)`             | `info` | `attri_perc_info`   |
| `All`             | `*all columns` | `*all columns`   |

</details>

## Custom ID Selection

This option produces all columns for one or more user entered EPPI ID's.

## License

Distributed under the MIT License. See LICENSE for more information.