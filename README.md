
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

All output dataframes will be saved to the 'output' directory under the same name as your input file.

## Dataframe 1 [Study, Research and Design Variables]

| Variable Name | Data Type |
| ------------- | ----------- |
| `Eppi ID`   | `raw` |
| `Author`   | `raw` |
| `Year`   | `raw` |
| `Abstract`   | `raw` |
| `Admin Strand`   | `raw, info` |
| `Toolkit Version`   | `raw` |
| `Publication Type EPPI`   | `raw` |
| `Publication Type`   | `raw, ht, info` |
| `Country`   | `raw` |
| `Educational Setting`   | `raw, ht, info` |
| `Study Realism`   | `raw, ht, info` |
| `Student Age`   | `raw, ht, info` |
| `Number of Schools Intervention`   | `info, ht` |
| `Number of Schools Control`   | `info, ht` |
| `Number of Schools Total`   | `info, ht` |
| `Number of Schools NA`   | `raw, info, ht` |
| `Number of Classes Intervention`   | `info, ht` |
| `Number of Classes Control`   | `info, ht` |
| `Number of Classes Total`   | `info, ht` |
| `Number of Classes NA`   | `raw, info, ht` |
| `Treatment Group`   | `raw, ht, info` |
| `Participant Assignment`   | `raw, ht, info` |
| `Level of Assignment`   | `raw, ht, info` |
| `Study Design`   | `raw, ht, info` |
| `Randomisation`   | `raw, ht, info` |
| `Other Outcomes`   | `raw, ht, info` |
| `Additional Outcomes`   | `raw, ht, info` |

## Dataframe 2 [Intervention Details]

| Variable Name | Data Type |
| ------------- | ----------- |
| `Eppi ID`   | `raw` |
| `Author`   | `raw` |
| `Year`   | `raw` |
| `Admin Strand`   | `raw, info` |
| `Toolkit Version`   | `raw` |
| `Intervention Name`   | `ht, info` |
| `Intervention Description`   | `ht, info` |
| `Intervention Objectives`   | `ht, info` |
| `Intervention Organization Type`   | `raw, ht, info` |
| `Intervention Training Provided`   | `raw, ht, info` |
| `Intervention Focus`   | `raw, ht, info` |
| `Intervention Teaching Approach`   | `raw, ht, info` |
| `Digital Technology`   | `raw, ht, info` |
| `Parent Engagement`   | `raw, ht, info` |
| `Intervention Time`   | `raw, ht, info` |
| `Intervention Delivery`   | `raw, ht, info` |
| `Intervention Duration`   | `ht, info` |
| `Intervention Frequency`   | `ht, info` |
| `Intervention Session Length`   | `ht, info` |
| `Intervention Detail`   | `raw, ht, info` |
| `Intervention Costs`   | `raw, ht, info` |
| `Intervention Evaluation`   | `raw` |
| `Baseline Differences`   | `raw, ht, info` |
| `Comparison Analysis`   | `raw, ht, info` |
| `Comparison Variables Reported`   | `raw, ht, info` |
| `Comparison Variables Reported (Which Ones)`   | `raw, ht, info` |
| `Clustering`   | `raw, ht, info` |

## Sample Size Dataframe [Sample Size Variables]

| Variable Name | Data Type |
| ------------- | ----------- |
| `Eppi ID`   | `raw` |
| `Author`   | `raw` |
| `Year`   | `raw` |
| `Admin Strand`   | `raw, info` |
| `Toolkit Version`   | `raw` |
| `Sample Size Comments`   | `info, ht` |
| `Gender`   | `raw, ht, info` |
| `Low SES Percentage`   | `info, raw` |
| `Further SES Info`   | `info, ht` |
| `No Low SES FSM Info`   | `raw, info` |
| `Sample Size Intervention`   | `ht, info` |
| `Sample Size Control`   | `ht, info` |
| `Sample Size Second Intervention`   | `ht, info` |
| `Sample Size Third Intervention`   | `ht, info` |
| `Sample Size Analysis Intervention`   | `raw, info` |
| `Sample Size Analysis Control`   | `raw, info` |
| `Sample Size Analysis Second Intervention`   | `raw, info` |
| `Sample Size Analysis Second Control`   | `raw, info` |
| `Attrition Dropout Reporting`   | `raw, info` |
| `Attrition Dropout Reporting`   | `info` |
| `Treatment Group Attrition`   | `ht, info` |
| `Overall Percentage Attrition`   | `ht, info` |

## Effect Size A Dataframe [Descriptive Statistics]

| Variable Name | Data Type |
| ------------- | ----------- |
| `Eppi ID`   | `raw` |
| `Author`   | `raw` |
| `Year`   | `raw` |
| `Admin Strand`   | `raw, info` |
| `Toolkit Version`   | `raw` |
| `Description Statistics Primary Outcome Reported`   | `raw, ht, info` |
| `Intervention Group Number`   | `ht, info` |
| `Intervention Group Pretest Mean`   | `ht, info` |
| `Intervention Group Pretest SD`   | `ht, info` |
| `Intervention Group Posttest Mean`   | `ht, info` |
| `Intervention Group Posttest SD`   | `ht, info` |
| `Intervention Group Gain Score Mean`   | `ht, info` |
| `Intervention Group Gain Score SD`   | `ht, info` |
| `Intervention Group Other Info`   | `ht, info` |
| `Control Group Number`   | `ht, info` |
| `Control Group Pretest Mean`   | `ht, info` |
| `Control Group Pretest SD`   | `ht, info` |
| `Control Group Posttest Mean`   | `ht, info` |
| `Control Group Posttest SD`   | `ht, info` |
| `Control Group Gain Score Mean`   | `ht, info` |
| `Control Group Gain Score SD`   | `ht, info` |
| `Control Group Other Info`   | `ht, info` |
| `Intervention Group Number 2`   | `ht, info` |
| `Intervention Group Pretest 2 Mean`   | `ht, info` |
| `Intervention Group Pretest 2 SD`   | `ht, info` |
| `Intervention Group Posttest 2 Mean`   | `ht, info` |
| `Intervention Group Posttest 2 SD`   | `ht, info` |
| `Intervention Group Gain Score 2 Mean`   | `ht, info` |
| `Intervention Group Gain Score 2 SD`   | `ht, info` |
| `Intervention Group Other 2 Info`   | `ht, info` |
| `Control Group Number 2`   | `ht, info` |
| `Control Group Pretest 2 Mean`   | `ht, info` |
| `Control Group Pretest 2 SD`   | `ht, info` |
| `Control Group Posttest 2 Mean`   | `ht, info` |
| `Control Group Posttest 2 SD`   | `ht, info` |
| `Control Group Gain Score 2 Mean`   | `ht, info` |
| `Control Group Gain Score 2 SD`   | `ht, info` |
| `Control Group Other 2 Info`   | `ht, info` |
| `Follow-up Data`   | `raw, ht, info` |

## Effect Size B Dataframe [Outcome Details]

| Variable Name | Data Type |
| ------------- | ----------- |
| `Eppi ID`   | `raw` |
| `Author`   | `raw` |
| `Year`   | `raw` |
| `Admin Strand`   | `raw, info` |
| `Toolkit Outcome Title` | `raw` |
| `Toolkit Outcome Description` | `raw` |
| `Toolkit Primary` | `raw` |
| `Toolkit Primary SMD` | `raw` |
| `Toolkit Primary SE`| `raw` |
| `Toolkit Outcome Measure` | `raw` |
| `Toolkit Group 1 Sample Size` | `raw` |
| `Toolkit Group 1 Mean` | `raw` |
| `Toolkit Group 1 Standard Deviation` | `raw` |
| `Toolkit Group 2 Sample Size` | `raw` |
| `Toolkit Group 2 Mean` | `raw` |
| `Toolkit Group 2 Standard Deviation` | `raw` |
| `Toolkit Primary CI Lower` | `raw` |
| `Toolkit Primary CI Upper` | `raw` |
| `Toolkit Primary Outcome` | `raw` |
| `Toolkit Primary Sample Size` | `raw` |
| `Toolkit Primary Outcome Comparison` | `raw` |
| `Toolkit Effect Size Type`| `raw` |
| `Toolkit Test Type`| `raw` |
| `Reading Outcome Title` | `raw` |
| `Reading Outcome Description` | `raw` |
| `Reading Prim` | `raw` |
| `Reading Primary SMD` | `raw` |
| `Reading SE` | `raw` |
| `Reading Outcome Measure` | `raw` |
| `Reading Group 1 Sample Size` | `raw` |
| `Reading Group 1 Mean` | `raw` |
| `Reading Group 1 Standard Deviation` | `raw` |
| `Reading Group 2 Sample Size` | `raw` |
| `Reading Group 2 Mean` | `raw` |
| `Reading Group 2 Standard Deviation` | `raw` |
| `Reading Confidence Interval Lower` | `raw` |
| `Reading Confidence Interval Upper` | `raw` |
| `Reading Outcome` | `raw` |
| `Reading Sample Size` | `raw` |
| `Reading Outcome Comparison` | `raw` |
| `Reading Effect Size Type` | `raw` |
| `Reading Test Type` | `raw` |
| `Writing and Spelling Outcome Title` | `raw` |
| `Writing and Spelling Outcome Description` | `raw` |
| `Writing and Spelling Prim` | `raw` |
| `Writing and Spelling Primary SMD` | `raw` |
| `Writing and Spelling SE` | `raw` |
| `Writing and Spelling Outcome Measure` | `raw` |
| `Writing and Spelling Group 1 Sample Size` | `raw` |
| `Writing and Spelling Group 1 Mean` | `raw` |
| `Writing and Spelling Group 1 Standard Deviation` | `raw` |
| `Writing and Spelling Group 2 Sample Size` | `raw` |
| `Writing and Spelling Group 2 Mean` | `raw` |
| `Writing and Spelling Group 2 Standard Deviation` | `raw` |
| `Writing and Spelling Confidence Interval Lower` | `raw` |
| `Writing and Spelling Confidence Interval Upper` | `raw` |
| `Writing and Spelling Outcome` | `raw` |
| `Writing and Spelling Sample Size` | `raw` |
| `Writing and Spelling Outcome Comparison` | `raw` |
| `Writing and Spelling Effect Size Type` | `raw` |
| `Writing and Spelling Test Type` | `raw` |
| `Mathematics Outcome Title` | `raw` |
| `Mathematics Outcome Description` | `raw` |
| `Mathematics Prim` | `raw` |
| `Mathematics Primary SMD` | `raw` |
| `Mathematics SE` | `raw` |
| `Mathematics Outcome Measure` | `raw` |
| `Mathematics Group 1 Sample Size` | `raw` |
| `Mathematics Group 1 Mean` | `raw` |
| `Mathematics Group 1 Standard Deviation` | `raw` |
| `Mathematics Group 2 Sample Size` | `raw` |
| `Mathematics Group 2 Mean` | `raw` |
| `Mathematics Group 2 Standard Deviation` | `raw` |
| `Mathematics Confidence Interval Lower` | `raw` |
| `Mathematics Confidence Interval Upper` | `raw` |
| `Mathematics Outcome` | `raw` |
| `Mathematics Sample Size` | `raw` |
| `Mathematics Outcome Comparison` | `raw` |
| `Mathematics Effect Size Type` | `raw` |
| `Mathematics Test Type` | `raw` |
| `Science Outcome Title` | `raw` |
| `Science Outcome Description` | `raw` |
| `Science Prim` | `raw` |
| `Science Primary SMD` | `raw` |
| `Science SE` | `raw` |
| `Science Outcome Measure` | `raw` |
| `Science Group 1 Sample Size` | `raw` |
| `Science Group 1 Mean` | `raw` |
| `Science Group 1 Standard Deviation` | `raw` |
| `Science Group 2 Sample Size` | `raw` |
| `Science Group 2 Mean` | `raw` |
| `Science Group 2 Standard Deviation` | `raw` |
| `Science Confidence Interval Lower` | `raw` |
| `Science Confidence Interval Upper` | `raw` |
| `Science Outcome` | `raw` |
| `Science Sample Size` | `raw` |
| `Science Outcome Comparison` | `raw` |
| `Science Effect Size Type` | `raw` |
| `Science Test Type` | `raw` |
| `FSM Outcome Title` | `raw` |
| `FSM Outcome Description` | `raw` |
| `FSM Prim` | `raw` |
| `FSM Primary SMD` | `raw` |
| `FSM SE` | `raw` |
| `FSM Outcome Measure` | `raw` |
| `FSM Group 1 Sample Size` | `raw` |
| `FSM Group 1 Mean` | `raw` |
| `FSM Group 1 Standard Deviation` | `raw` |
| `FSM Group 2 Sample Size` | `raw` |
| `FSM Group 2 Mean` | `raw` |
| `FSM Group 2 Standard Deviation` | `raw` |
| `FSM Confidence Interval Lower` | `raw` |
| `FSM Confidence Interval Upper` | `raw` |
| `FSM Outcome` | `raw` |
| `FSM Sample Size` | `raw` |
| `FSM Outcome Comparison` | `raw` |
| `FSM Effect Size Type` | `raw` |
| `FSM Test Type` | `raw` |


## Main Data Analysis Dataframe

| Variable Name | Data Type |
| ------------- | ----------- |
| `Eppi ID`   | `raw` |
| `Author`   | `raw` |
| `Year`   | `raw` |
| `Publication Type`   | `raw` |
| `Admin Strand`   | `raw, info` |
| `Toolkit Version`   | `raw` |
| `Toolkit Outcome Strand`   | `raw` |
| `Toolkit SMD`   | `raw` |
| `Toolkit SE`   | `raw` |
| `Toolkit Outcome Title`   | `raw` |
| `Toolkit Outcome Type`   | `raw` |
| `Toolkit Sample`   | `raw` |
| `Toolkit Outcome Comparison`   | `raw` |
| `Toolkit Effect Size Type`   | `raw` |
| `Toolkit Outcome Measure`   | `raw` |
| `Toolkit Outcome Test Type`   | `raw` |
| `Reading Outcome Type`   | `raw` |
| `Reading SMD`   | `raw` |
| `Reading SE`   | `raw` |
| `Writing and Spelling Outcome Type`   | `raw` |
| `Writing and Spelling SMD`   | `raw` |
| `Writing and Spelling SE`   | `raw` |
| `Mathematics Outcome Type`   | `raw` |
| `Mathematics SMD`   | `raw` |
| `Mathematics SE`   | `raw` |
| `Science Outcome Type`   | `raw` |
| `Science SMD`   | `raw` |
| `Science SE`   | `raw` |
| `FSM Outcome Type`   | `raw` |
| `FSM SMD`   | `raw` |
| `FSM SE`   | `raw` |
| `Sample Analyzed`   | `info` |
| `Number of Schools Total`   | `info` |
| `Number of Classes Total`   | `info` |
| `Intervention Setting`   | `raw` |
  `FSM 50`   | `raw` |
| `FSM Percentage`   | `info` |
| `Country`   | `raw` |
| `Study Design`   | `raw` |
| `Intervention Teaching Approach`   | `raw` |
| `Intervention Training Provided`   | `raw` |
| `Digital Technology`   | `raw` |
| `Parent Engagement`   | `raw` |
| `Intervention Time`   | `raw` |
| `Intervention Delivery`   | `raw` |
| `Intervention Duration`   | `info` |
| `Intervention Frequency`   | `info` |
| `Intervention Session Length`   | `info` |
| `Oucome Strand`   | `raw` |

## Risk of Bias Dataframe

| Variable Name | Data Type |
| ------------- | ----------- |
| `Eppi ID`   | `raw` |
| `Author`   | `raw` |
| `Toolkit SMD`   | `raw` |
| `Toolkit SE`   | `raw` |
| `Publication Year`   | `raw, risk label, risk value` |
| `Strand`   | `raw` |
| `Publication Type`   | `raw, risk label, risk value` |
| `Participant Assignment`   | `raw, risk label, risk value` |
| `Study Realism`   | `raw, risk label, risk value` |
| `School Treatment Group`   | `raw, raw_adjusted, risk label, risk value` |
| `Intervention Delivery`   | `raw, risk label (ind var split), risk value` |
| `Number of Classes Total`   | `raw, raw_adjusted, risk label, risk value` |
| `Outcome Evaluation`   | `raw, risk label, risk value` |
| `Computational Analysis`   | `raw, risk label, risk value` |
| `Sample Size (Analysed)`   | `raw, risk label, risk value` |
| `Outcome Test Type`   | `raw, risk label, risk value` |
| `Outcome Effect Size Type`   | `raw, risk label, risk value` |
| `Attrition Percentage`   | `raw, risk label, risk value` |
| `Cluster Analysis`   | `raw, risk label, risk value` |
| `Randomisation`   | `raw, risk label, risk value` |
| `NA values`   | `raw` |
| `Mean`   | `raw` |
| `Median`   | `raw` |
| `Raw Total`   | `raw` |

## References Dataframe

| Variable Name | Data Type |
| ------------- | ----------- |
| `Eppi ID`   | `raw` |
| `Admin Strand`   | `raw` |
| `Author`   | `raw` |
| `Authors`   | `raw` |
| `Year`   | `raw` |
| `Title`   | `raw` |
| `Parent Title`   | `raw` |
| `Parent Authors`   | `raw` |
| `Type Name`   | `raw` |
| `Abstract`   | `raw` |
| `Volume`   | `raw` |
| `Issue`   | `raw` |
| `Pages`   | `raw` |
| `DOI`   | `raw` |
| `URL`   | `raw` |
| `Publisher`   | `raw` |
| `City`   | `raw` |
| `Institution`   | `raw` |

## License

Distributed under the MIT License. See LICENSE for more information.
