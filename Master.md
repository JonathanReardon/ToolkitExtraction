---
title: 'Master data extraction.Rmd'
author: "Jonathan Reardon"
output:
  html_document:
    keep_md: true
    df_print: paged
  #pdf_document:
    #keep_md: true
editor_options:
  chunk_output_type: inline
---


```r
knitr::opts_chunk$set(echo = T,
                      fig.path = "Master_figs/")
library(reticulate)
library(ggplot2)
library(dplyr)
library(reshape2)
library(purrr)
use_python("/usr/local/bin/python3")
```


```python
# import necessary libraries
import json
from collections import Counter
from pprint import pprint
from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('ggplot')

# import dataset
with open('/home/jon/json/ToolkitExtraction/data/Batch1.json') as f:
    data=json.load(f)

def get_strand_info():
    ''' 
    a function that returns
    a dict containing strand labels
    and corresponding attribute ids
    '''
    strands={}
    for counter, element in enumerate(data["CodeSets"][0]["Attributes"]["AttributesList"]):
        attribute_name=(data["CodeSets"][0]["Attributes"]["AttributesList"][counter]["AttributeName"])
        attribute_id=(data["CodeSets"][0]["Attributes"]["AttributesList"][counter]["AttributeId"])
        strands.update( {attribute_id:attribute_name} )
    return strands

strands = get_strand_info()

def get_edu_info():
    edu_setting={}
    for counter, value in enumerate(data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"]):
        setting_code=data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][counter]["AttributeId"]
        setting_name=data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][counter]["AttributeName"]
        edu_setting.update( {setting_code:setting_name} )
    return edu_setting

edu = get_edu_info()

def get_all():
  finds=[]
  
  find=0
  strandfind=0
  
  studies=0
  # iterate over each section within each study of 'references'
  for section in range(len(data["References"])):
      studies+=1
      find=0
      strandfind=0
      for study in range(len(data["References"][section]["Codes"])):
          
          # get educational setting data (prmiary/elementary etc.)
          for key,value in edu.items():
              if key == data["References"][section]["Codes"][study]["AttributeId"]:
                  find=value
                  label=key
              elif find==0:
                  find="NaN"
                  label="NaN"
                  
          # get strand data (feedback, peer tutoring etc.)
          for key,value in strands.items():
              if key == data["References"][section]["Codes"][study]["AttributeId"]:
                  strandfind=value
                  strandlabel=key
              elif strandfind==0:
                  strandfind="NaN"
                  strandlabel="NaN"
                  
          # get outcome data
          if "Outcomes" in data["References"][section]:
              outcometext=data["References"][section]["Outcomes"][0]["OutcomeText"]
              interventiontext=data["References"][section]["Outcomes"][0]["InterventionText"]
              SMD=(data["References"][section]["Outcomes"][0]["SMD"])
              SESMD=(data["References"][section]["Outcomes"][0]["SESMD"])
              CIupperSMD=(data["References"][section]["Outcomes"][0]["CIUpperSMD"])
              CIlowerSMD=(data["References"][section]["Outcomes"][0]["CILowerSMD"])
          else:
              outcometext="NaN"
              interventiontext="NaN"
              SMD="NaN"
              SESMD="NaN"
              CIupperSMD="NaN"
              CIlowerSMD="NaN"
              
          # get year data
          if "Year" in data["References"][section]:
              year=data["References"][section]["Year"]
          else:
              year="NaN"
              
          # get author data
          if "ShortTitle" in data["References"][section]:
              author=data["References"][section]["ShortTitle"]
          else:
              author="NaN"
              
      finds.append([author, find, label, strandfind, strandlabel, interventiontext, 
                    outcometext, year, SMD, SESMD, CIupperSMD, CIlowerSMD])
      
  df = pd.DataFrame(finds, columns=['Author', 'EduSetting', 'EduID', 'Strand', 'Strand ID', 
                                    'Intervention', 'Outcome', 'Year', 'SMD', 'SESMD', 'CIupper', 'CIlower'])
                                    
  df.fillna(0)
                                    
  # round effect sizes to two decimal points
  df.loc[:, "SMD"] = df["SMD"].astype(float).round(4)
  df.loc[:, "SESMD"] = df["SESMD"].astype(float).round(4)
  df.loc[:, "CIupper"] = df["CIupper"].astype(float).round(4)
  df.loc[:, "CIlower"] = df["CIlower"].astype(float).round(4)
                                    
  return df
  
all = get_all()
all.head(10)
```

```
##               Author                 EduSetting  ... CIupper CIlower
## 0   Aarnoutse (1997)  Primary/elementary school  ...     NaN     NaN
## 1   Aarnoutse (1998)  Primary/elementary school  ...     NaN     NaN
## 2  Abbondanza (2013)      Secondary/High school  ...  0.8637  0.1712
## 3       Adler (1998)  Primary/elementary school  ...  0.6021 -0.2721
## 4     Ahlfors (1979)  Primary/elementary school  ...     NaN     NaN
## 5     Allsopp (1995)              Middle school  ...  0.4027 -0.0835
## 6       Ammon (1971)  Primary/elementary school  ...  0.5780 -0.5780
## 7      Anders (1984)      Secondary/High school  ...  2.2439  1.0792
## 8    Anderson (1973)              Middle school  ...  1.6074  0.7020
## 9     Andrade (2008)  Primary/elementary school  ...  1.2220  0.4380
## 
## [10 rows x 12 columns]
```


```r
master_df <- py$all
#View(master_df)
master_df <- as.data.frame(lapply(master_df, unlist))
head(master_df)
```

<div data-pagedtable="false">
  <script data-pagedtable-source type="application/json">
{"columns":[{"label":[""],"name":["_rn_"],"type":[""],"align":["left"]},{"label":["Author"],"name":[1],"type":["fctr"],"align":["left"]},{"label":["EduSetting"],"name":[2],"type":["fctr"],"align":["left"]},{"label":["EduID"],"name":[3],"type":["fctr"],"align":["left"]},{"label":["Strand"],"name":[4],"type":["fctr"],"align":["left"]},{"label":["Strand.ID"],"name":[5],"type":["dbl"],"align":["right"]},{"label":["Intervention"],"name":[6],"type":["fctr"],"align":["left"]},{"label":["Outcome"],"name":[7],"type":["fctr"],"align":["left"]},{"label":["Year"],"name":[8],"type":["fctr"],"align":["left"]},{"label":["SMD"],"name":[9],"type":["dbl"],"align":["right"]},{"label":["SESMD"],"name":[10],"type":["dbl"],"align":["right"]},{"label":["CIupper"],"name":[11],"type":["dbl"],"align":["right"]},{"label":["CIlower"],"name":[12],"type":["dbl"],"align":["right"]}],"data":[{"1":"Aarnoutse (1997)","2":"Primary/elementary school","3":"5215411","4":"Oral language interventions","5":"5023563","6":"NaN","7":"NaN","8":"1997","9":"NaN","10":"NaN","11":"NaN","12":"NaN","_rn_":"1"},{"1":"Aarnoutse (1998)","2":"Primary/elementary school","3":"5215411","4":"Oral language interventions","5":"5023563","6":"NaN","7":"NaN","8":"1998","9":"NaN","10":"NaN","11":"NaN","12":"NaN","_rn_":"2"},{"1":"Abbondanza (2013)","2":"Secondary/High school","3":"5215413","4":"Peer tutoring","5":"5023548","6":"Literacy: reading comprehension","7":"Primary outcome","8":"2013","9":"0.5174","10":"0.1767","11":"0.8637","12":"0.1712","_rn_":"3"},{"1":"Adler (1998)","2":"Primary/elementary school","3":"5215411","4":"Feedback","5":"5023555","6":"Literacy: writing","7":"Primary outcome","8":"1998","9":"0.1650","10":"0.2230","11":"0.6021","12":"-0.2721","_rn_":"4"},{"1":"Ahlfors (1979)","2":"Primary/elementary school","3":"5215411","4":"Oral language interventions","5":"5023563","6":"NaN","7":"NaN","8":"1979","9":"NaN","10":"NaN","11":"NaN","12":"NaN","_rn_":"5"},{"1":"Allsopp (1995)","2":"Middle school","3":"5215412","4":"Peer tutoring","5":"5023548","6":"Mathematics","7":"Primary outcome","8":"1995","9":"0.1596","10":"0.1241","11":"0.4027","12":"-0.0835","_rn_":"6"}],"options":{"columns":{"min":{},"max":[10]},"rows":{"min":[10],"max":[10]},"pages":{}}}
  </script>
</div>
