---
title: 'Master data extraction.Rmd'
author: "Jonathan Reardon"
output:
  html_document:
    keep_md: true
    #df_print: paged
  #pdf_document:
    #keep_md: true
editor_options:
  chunk_output_type: inline
---
**Import R libraries, save figures to "Master_figs/"**

```r
knitr::opts_chunk$set(echo = T,
                      fig.path = "Master_figs/")
library(reticulate)
library(ggplot2)
library(dplyr)
library(reshape2)
library(purrr)
library(gridExtra)
library(kableExtra)
library(forestplot)
library(metafor)
use_python("/usr/local/bin/python3")
rm(list = ls())
```
**Import Python packages and (json) dataset**

```python
# import necessary libraries
import json
from collections import Counter
from pprint import pprint
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('ggplot')

# import dataset (uncomment to select dataset of choice)
with open('/home/jon/json/ToolkitExtraction/data/batch2.json') as f:
#with open('/home/jon/json/ToolkitExtraction/data/Batch1.json') as f:
    data=json.load(f)
```
## CodeSets extraction

These functions extract attribute names and ID's (e.g. strand, educational setting) and return Python dictionaries containing attribute ID's as 'keys' and attribute names as 'values'. The 'Codesets' section at the top of the file does not contain any data, only variable information.

**Example dictionaries**  
strands&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= {5023544: 'Arts participation', 5023545: 'Aspiration interventions', .. }  
edu_setting&nbsp;&nbsp;&nbsp;= {5215410: 'Nursery school/pre-school', 5215411: 'Primary/elementary school', 5215412, .. }

```python
def get_strand_info():
    '''Return a dict of Strand Attribute Names & Attribute ID's'''
    strands={}
    for counter, element in enumerate(data["CodeSets"][0]["Attributes"]["AttributesList"]):
        attribute_name=(data["CodeSets"][0]["Attributes"]["AttributesList"][counter]["AttributeName"])
        attribute_id=(data["CodeSets"][0]["Attributes"]["AttributesList"][counter]["AttributeId"])
        strands.update( {attribute_id:attribute_name} )
    return strands
strands = get_strand_info()

def get_edu_info():
    '''Return a dict of Educational Setting Attribute Names & Attribute ID's'''
    edu_setting={}
    for counter, value in enumerate(data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"]):
        setting_code=data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][counter]["AttributeId"]
        setting_name=data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][counter]["AttributeName"]
        edu_setting.update( {setting_code:setting_name} )
    return edu_setting
edu = get_edu_info()

def get_country_codes():
  '''Return a dict of Country Attribute Names & Attribute ID's'''
  country_codes={}
  for counter, value in enumerate(data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][0]["Attributes"]["AttributesList"]):
      country_code=data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][0]["Attributes"]["AttributesList"][counter]["AttributeId"]
      country_name=data["CodeSets"][2]["Attributes"]["AttributesList"][2]["Attributes"]["AttributesList"][0]["Attributes"]["AttributesList"][counter]["AttributeName"]
      country_codes.update( {country_code:country_name} )
  return country_codes
countries = get_country_codes()

def get_publication_type():
    '''Return a dict of Publication Type Attribute Names & Attribute ID's'''
    publication_type={}
    for counter, element in enumerate(data["CodeSets"][2]["Attributes"]["AttributesList"][0]["Attributes"]["AttributesList"][0]):
        attribute_name=(data["CodeSets"][2]["Attributes"]["AttributesList"][0]["Attributes"]["AttributesList"][counter]["AttributeName"])
        attribute_id=(data["CodeSets"][2]["Attributes"]["AttributesList"][0]["Attributes"]["AttributesList"][counter]["AttributeId"])
        publication_type.update( { attribute_id:attribute_name })
    return publication_type
pub_type = get_publication_type()
```
## Main data extraction function

```python
def get_all():
  finds=[]
  find=0
  strandfind=0
  countryfind=0
  exclude=np.nan
  
  extracted=0
  null=0
  
  studies=0
  # iterate over each section within each study of 'references'
  for section in range(len(data["References"])):
      find=0
      strandfind=0
      
      if "Codes" in data["References"][section]:
          extracted+=1
          for study in range(len(data["References"][section]["Codes"])):
    
              # get publication type data
              for key, value in pub_type.items():
                  if key == data["References"][section]["Codes"][study]["AttributeId"]:
                      pubfind=value
                      publabel=key
                  elif find==0:
                      pubfind=exclude
                      publabel=exclude
                  
              # get country of study data
              for key, value in countries.items():
                  if key == data["References"][section]["Codes"][study]["AttributeId"]:
                      countryfind=value
                      countrylabel=key
                  elif find==0:
                      countryfind=exclude
                      countrylabel=exclude
          
              # get educational setting data (primary/elementary etc.)
              for key,value in edu.items():
                  if key == data["References"][section]["Codes"][study]["AttributeId"]:
                      find=value
                      label=key
                  elif find==0:
                      find=exclude
                      label=exclude
                  
              # get strand data (feedback, peer tutoring etc.)
              for key,value in strands.items():
                  if key == data["References"][section]["Codes"][study]["AttributeId"]:
                      strandfind=value
                      strandlabel=key
                  elif strandfind==0:
                      strandfind=exclude
                      strandlabel=exclude
                  
              # get outcome data if an "Outcomes" section exists
              if "Outcomes" in data["References"][section]:
                  outcometext=data["References"][section]["Outcomes"][0]["OutcomeText"]
                  interventiontext=data["References"][section]["Outcomes"][0]["InterventionText"]
                  SMD=(data["References"][section]["Outcomes"][0]["SMD"])
                  SESMD=(data["References"][section]["Outcomes"][0]["SESMD"])
                  CIupperSMD=(data["References"][section]["Outcomes"][0]["CIUpperSMD"])
                  CIlowerSMD=(data["References"][section]["Outcomes"][0]["CILowerSMD"])
              else:
                  outcometext=exclude
                  interventiontext=exclude
                  SMD=exclude
                  SESMD=exclude
                  CIupperSMD=exclude
                  CIlowerSMD=exclude
              
              # get year data 
              if "Year" in data["References"][section]:
                  year=int(data["References"][section]["Year"])
              else:
                  year=exclude
              
              # get author data
              if "ShortTitle" in data["References"][section]:
                  author=data["References"][section]["ShortTitle"]
              else:
                  author=exclude
              
          # append all extracted data to our 'finds' list
          finds.append([author, find, strandfind, interventiontext, 
                        outcometext, year, countryfind, pubfind, SMD, SESMD, CIupperSMD, CIlowerSMD])
                        
      else:
          null+=1
      
      # convert data list ('finds') to Pandas dataframe
      df = pd.DataFrame(finds, columns=['Author', 'EducationalSetting', 'Strand', 
                                       'Intervention', 'Outcome', 'Year', 'Country', 'PublicationType', 'SMD', 
                                       'SESMD', 'CIupper', 'CIlower'])
                                    
      #df.fillna(0)
                                    
      # round effect sizes and confidence interbals to four decimal points
      df.loc[:, "SMD"] = df["SMD"].astype(float).round(4)
      df.loc[:, "SESMD"] = df["SESMD"].astype(float, errors='ignore').round(4)
      df.loc[:, "CIupper"] = df["CIupper"].astype(float).round(4)
      df.loc[:, "CIlower"] = df["CIlower"].astype(float).round(4)
         
  print("Number of studies extracted (they have a 'Codes' section): {}".format(extracted),
        "Number of of missing studies (no 'Codes' section found):   {}".format(null),
        sep='\n')

  return df
  
all = get_all()
```

```
## Number of studies extracted (they have a 'Codes' section): 598
## Number of of missing studies (no 'Codes' section found):   18
```
**Pass complete dataset to R (dataframe) and view all for inspection**

```r
complete <- data.frame(py$all)

# view complete dataset in external viewer (Rstudio)
#View(complete)

rownames(complete) <- NULL
# view kable of complete dataset
kable(complete[1:15,1:12], booktabs=T) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed", "responsive", "bordered"), full_width=T, font_size=8)
```

<table class="table table-striped table-hover table-condensed table-responsive table-bordered" style="font-size: 8px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> Author </th>
   <th style="text-align:left;"> EducationalSetting </th>
   <th style="text-align:left;"> Strand </th>
   <th style="text-align:left;"> Intervention </th>
   <th style="text-align:left;"> Outcome </th>
   <th style="text-align:right;"> Year </th>
   <th style="text-align:left;"> Country </th>
   <th style="text-align:left;"> PublicationType </th>
   <th style="text-align:right;"> SMD </th>
   <th style="text-align:right;"> SESMD </th>
   <th style="text-align:right;"> CIupper </th>
   <th style="text-align:right;"> CIlower </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Aarnoutse (1997) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Oral language interventions </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:right;"> 1997 </td>
   <td style="text-align:left;"> The Netherlands </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Aarnoutse (1998) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Oral language interventions </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:right;"> 1998 </td>
   <td style="text-align:left;"> The Netherlands </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Abbondanza (2013) </td>
   <td style="text-align:left;"> Secondary/High school </td>
   <td style="text-align:left;"> Peer tutoring </td>
   <td style="text-align:left;"> Literacy: reading comprehension </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 2013 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.5174 </td>
   <td style="text-align:right;"> 0.1767 </td>
   <td style="text-align:right;"> 0.8637 </td>
   <td style="text-align:right;"> 0.1712 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Acalin (1995) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> One to one tuition </td>
   <td style="text-align:left;"> Literacy: reading comprehension </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1995 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> -0.1119 </td>
   <td style="text-align:right;"> 0.2464 </td>
   <td style="text-align:right;"> 0.3710 </td>
   <td style="text-align:right;"> -0.5948 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Adler (1998) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1998 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.1650 </td>
   <td style="text-align:right;"> 0.2230 </td>
   <td style="text-align:right;"> 0.6021 </td>
   <td style="text-align:right;"> -0.2721 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Ahlfors (1979) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Oral language interventions </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:right;"> 1979 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Allen (2003) </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:left;"> Summer schools </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:right;"> 2003 </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
   <td style="text-align:right;"> NaN </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Allor (2004) </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:left;"> One to one tuition </td>
   <td style="text-align:left;"> Literacy: reading comprehension </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 2004 </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:left;"> NaN </td>
   <td style="text-align:right;"> 0.5300 </td>
   <td style="text-align:right;"> 0.2400 </td>
   <td style="text-align:right;"> 1.0004 </td>
   <td style="text-align:right;"> 0.0596 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Allsopp (1995) </td>
   <td style="text-align:left;"> Middle school </td>
   <td style="text-align:left;"> Peer tutoring </td>
   <td style="text-align:left;"> Mathematics </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1995 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.1596 </td>
   <td style="text-align:right;"> 0.1241 </td>
   <td style="text-align:right;"> 0.4027 </td>
   <td style="text-align:right;"> -0.0835 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Ammon (1971) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Oral language interventions </td>
   <td style="text-align:left;"> Literacy: reading other </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1971 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.0000 </td>
   <td style="text-align:right;"> 0.2949 </td>
   <td style="text-align:right;"> 0.5780 </td>
   <td style="text-align:right;"> -0.5780 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Anders (1984) </td>
   <td style="text-align:left;"> Secondary/High school </td>
   <td style="text-align:left;"> Oral language interventions </td>
   <td style="text-align:left;"> Literacy: reading comprehension </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1984 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Conference paper </td>
   <td style="text-align:right;"> 1.6616 </td>
   <td style="text-align:right;"> 0.2971 </td>
   <td style="text-align:right;"> 2.2439 </td>
   <td style="text-align:right;"> 1.0792 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Anderson (1973) </td>
   <td style="text-align:left;"> Middle school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Mathematics </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1973 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 1.1547 </td>
   <td style="text-align:right;"> 0.2310 </td>
   <td style="text-align:right;"> 1.6074 </td>
   <td style="text-align:right;"> 0.7020 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Andrade (2008) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Secondary outcome(s) </td>
   <td style="text-align:right;"> 2008 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.8300 </td>
   <td style="text-align:right;"> 0.2000 </td>
   <td style="text-align:right;"> 1.2220 </td>
   <td style="text-align:right;"> 0.4380 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Aram (2004) OL </td>
   <td style="text-align:left;"> Nursery school/pre-school </td>
   <td style="text-align:left;"> Oral language interventions </td>
   <td style="text-align:left;"> Literacy: reading other </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 2004 </td>
   <td style="text-align:left;"> Israel </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.3624 </td>
   <td style="text-align:right;"> 0.2673 </td>
   <td style="text-align:right;"> 0.8862 </td>
   <td style="text-align:right;"> -0.1614 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Aram (2006) </td>
   <td style="text-align:left;"> Nursery school/pre-school </td>
   <td style="text-align:left;"> Oral language interventions </td>
   <td style="text-align:left;"> Literacy: reading comprehension </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 2006 </td>
   <td style="text-align:left;"> Israel </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.0396 </td>
   <td style="text-align:right;"> 0.2310 </td>
   <td style="text-align:right;"> 0.4923 </td>
   <td style="text-align:right;"> -0.4131 </td>
  </tr>
</tbody>
</table>
**Get 'feedback' 'peer tutoring' 'oral lang interventions' strand data, Primary Outcomes only**

```python
Primary = all[all['Outcome'] == "Primary outcome"]
Secondary = all[all['Outcome'] == "Secondary outcome(s)"]

feedback = Primary[Primary['Strand'] == "Feedback"]
peertut = Primary[Primary['Strand'] == "Peer tutoring"]

print("Number of Primary outcome studies overall:                {}".format(len(Primary)),
      "Number of Secondary outcome studies overall:              {}".format(len(Secondary)),
      "Number of Feedback strand (Primary outcome) studies:      {}".format(len(feedback)),
      "Number of Peer Tutoring strand (Primary outcome) studies: {}".format(len(peertut)),
      sep='\n')
```

```
## Number of Primary outcome studies overall:                366
## Number of Secondary outcome studies overall:              63
## Number of Feedback strand (Primary outcome) studies:      66
## Number of Peer Tutoring strand (Primary outcome) studies: 86
```
**Pass Feedback and Peer tutoring data frames from Python to R and inspect with kable**

```r
all_df <- data.frame(py$all)
View(all_df)

feedback <- data.frame(py$feedback)
peertut <- data.frame(py$peertut)

rownames(feedback) <- NULL
kable(feedback[1:10,1:12]) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed", "responsive", "bordered"), full_width=T, font_size=8)
```

<table class="table table-striped table-hover table-condensed table-responsive table-bordered" style="font-size: 8px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> Author </th>
   <th style="text-align:left;"> EducationalSetting </th>
   <th style="text-align:left;"> Strand </th>
   <th style="text-align:left;"> Intervention </th>
   <th style="text-align:left;"> Outcome </th>
   <th style="text-align:right;"> Year </th>
   <th style="text-align:left;"> Country </th>
   <th style="text-align:left;"> PublicationType </th>
   <th style="text-align:right;"> SMD </th>
   <th style="text-align:right;"> SESMD </th>
   <th style="text-align:right;"> CIupper </th>
   <th style="text-align:right;"> CIlower </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Adler (1998) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1998 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.1650 </td>
   <td style="text-align:right;"> 0.2230 </td>
   <td style="text-align:right;"> 0.6021 </td>
   <td style="text-align:right;"> -0.2721 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Anderson (1973) </td>
   <td style="text-align:left;"> Middle school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Mathematics </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1973 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 1.1547 </td>
   <td style="text-align:right;"> 0.2310 </td>
   <td style="text-align:right;"> 1.6074 </td>
   <td style="text-align:right;"> 0.7020 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Arter (1994) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1994 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Conference paper </td>
   <td style="text-align:right;"> 0.3000 </td>
   <td style="text-align:right;"> 0.1800 </td>
   <td style="text-align:right;"> 0.6528 </td>
   <td style="text-align:right;"> -0.0528 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Aumiller (1963) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: spelling </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1963 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> -0.0058 </td>
   <td style="text-align:right;"> 0.1451 </td>
   <td style="text-align:right;"> 0.2786 </td>
   <td style="text-align:right;"> -0.2903 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Baechie (1990) </td>
   <td style="text-align:left;"> Middle school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: reading comprehension </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1990 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.6548 </td>
   <td style="text-align:right;"> 0.2855 </td>
   <td style="text-align:right;"> 1.2143 </td>
   <td style="text-align:right;"> 0.0952 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Benson (1979) 1_1 </td>
   <td style="text-align:left;"> Middle school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1979 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.2200 </td>
   <td style="text-align:right;"> 0.1200 </td>
   <td style="text-align:right;"> 0.4552 </td>
   <td style="text-align:right;"> -0.0152 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Benson (1979) 1_2 </td>
   <td style="text-align:left;"> Middle school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1979 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.2115 </td>
   <td style="text-align:right;"> 0.1455 </td>
   <td style="text-align:right;"> 0.4967 </td>
   <td style="text-align:right;"> -0.0737 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Bethge (1982) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Cognitive: other </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1982 </td>
   <td style="text-align:left;"> Germany </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.8552 </td>
   <td style="text-align:right;"> 0.3027 </td>
   <td style="text-align:right;"> 1.4485 </td>
   <td style="text-align:right;"> 0.2619 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Bilsky (1978) </td>
   <td style="text-align:left;"> Secondary/High school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Mathematics </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1978 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 2.4289 </td>
   <td style="text-align:right;"> 0.4056 </td>
   <td style="text-align:right;"> 3.2239 </td>
   <td style="text-align:right;"> 1.6338 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Block (1970) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Mathematics </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1970 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.5191 </td>
   <td style="text-align:right;"> 0.2479 </td>
   <td style="text-align:right;"> 1.0050 </td>
   <td style="text-align:right;"> 0.0331 </td>
  </tr>
</tbody>
</table>
**Make Feedback and Peer Tutoring Forest plots and display them**

```r
feedback_plot <- ggplot(data=na.omit(subset(feedback, select=c(Author, SMD, CIlower, CIupper))),
                    aes(y=Author, x=SMD, xmin=CIlower, xmax=CIupper))+
                    geom_point(color='black', shape=15) +
                    geom_errorbarh(height=.7, linetype=1) +
                    scale_x_continuous(limits=c(-4,4), name='Standardized Mean Difference (95% CI)') +
                    ylab('Reference') +
                    geom_vline(xintercept=0, color='black', linetype='dashed') +
                    theme_classic() +
                    ggtitle("Feedback Strand")

peertut_plot <- ggplot(data=na.omit(subset(peertut, select=c(Author, SMD, CIlower, CIupper))),
                    aes(y=Author, x=SMD, xmin=CIlower, xmax=CIupper))+
                    geom_point(color='black', shape=15) +
                    geom_errorbarh(height=.7, linetype=1) +
                    scale_x_continuous(limits=c(-4,4), name='Standardized Mean Difference (95% CI)') +
                    ylab('Reference') +
                    geom_vline(xintercept=0, color='black', linetype='dashed') +
                    theme_classic() +
                    ggtitle("Peer Tutoring strand")
grid.arrange(feedback_plot, peertut_plot, ncol=2)
```

![](Master_figs/unnamed-chunk-7-1.png)<!-- -->
**Get 'Primary/elementary school' & 'Secondary/High school' data (Primary outcomes only), then from each of those get "Feedback" strand data only**

```python
Elementary = Primary[Primary['EducationalSetting'] == "Primary/elementary school"]
Sec = Primary[Primary['EducationalSetting'] == "Secondary/High school"]

feedback_elementary = Elementary[Elementary['Strand'] == "Feedback"]
feedback_secondary = Sec[Sec['Strand'] == "Feedback"]

print("Number of Primary/elementary school, primary outcome, feedbacks strand studies: {}".format(len(feedback_elementary)),
      "Number of Secondary/High school, primary outcome, feedbacks strand studies:     {}".format(len(feedback_secondary)),
      sep='\n')
```

```
## Number of Primary/elementary school, primary outcome, feedbacks strand studies: 34
## Number of Secondary/High school, primary outcome, feedbacks strand studies:     11
```
**Pass 'Primary/elementary school' & 'Secondary/High school' (Feedback Strand, Primary outcome) data frames from Python to R and inspect with kable**

```r
Primary_feedback <- data.frame(py$feedback_elementary)
High_feedback <- data.frame(py$feedback_secondary)

rownames(Primary_feedback) <- NULL
kable(Primary_feedback[1:10,1:12]) %>%
  kable_styling(bootstrap_options = c("striped", "hover", "condensed", "responsive", "bordered"), full_width=T, font_size=8)
```

<table class="table table-striped table-hover table-condensed table-responsive table-bordered" style="font-size: 8px; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> Author </th>
   <th style="text-align:left;"> EducationalSetting </th>
   <th style="text-align:left;"> Strand </th>
   <th style="text-align:left;"> Intervention </th>
   <th style="text-align:left;"> Outcome </th>
   <th style="text-align:right;"> Year </th>
   <th style="text-align:left;"> Country </th>
   <th style="text-align:left;"> PublicationType </th>
   <th style="text-align:right;"> SMD </th>
   <th style="text-align:right;"> SESMD </th>
   <th style="text-align:right;"> CIupper </th>
   <th style="text-align:right;"> CIlower </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Adler (1998) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1998 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.1650 </td>
   <td style="text-align:right;"> 0.2230 </td>
   <td style="text-align:right;"> 0.6021 </td>
   <td style="text-align:right;"> -0.2721 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Arter (1994) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1994 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Conference paper </td>
   <td style="text-align:right;"> 0.3000 </td>
   <td style="text-align:right;"> 0.1800 </td>
   <td style="text-align:right;"> 0.6528 </td>
   <td style="text-align:right;"> -0.0528 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Aumiller (1963) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: spelling </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1963 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> -0.0058 </td>
   <td style="text-align:right;"> 0.1451 </td>
   <td style="text-align:right;"> 0.2786 </td>
   <td style="text-align:right;"> -0.2903 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Bethge (1982) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Cognitive: other </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1982 </td>
   <td style="text-align:left;"> Germany </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.8552 </td>
   <td style="text-align:right;"> 0.3027 </td>
   <td style="text-align:right;"> 1.4485 </td>
   <td style="text-align:right;"> 0.2619 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Block (1970) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Mathematics </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1970 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 0.5191 </td>
   <td style="text-align:right;"> 0.2479 </td>
   <td style="text-align:right;"> 1.0050 </td>
   <td style="text-align:right;"> 0.0331 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Boggiano (1985) 1_1 </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1985 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.8454 </td>
   <td style="text-align:right;"> 0.3026 </td>
   <td style="text-align:right;"> 1.4385 </td>
   <td style="text-align:right;"> 0.2523 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Bohannon (1975) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: decoding/phonics </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1975 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Dissertation or thesis </td>
   <td style="text-align:right;"> 2.7500 </td>
   <td style="text-align:right;"> 0.6600 </td>
   <td style="text-align:right;"> 4.0436 </td>
   <td style="text-align:right;"> 1.4564 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Brandstetter (1978) 1_2 </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: reading comprehension </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1978 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.3700 </td>
   <td style="text-align:right;"> 1.0700 </td>
   <td style="text-align:right;"> 2.4672 </td>
   <td style="text-align:right;"> -1.7272 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Brookhart (2008) </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: decoding/phonics </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 2010 </td>
   <td style="text-align:left;"> USA </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 0.1738 </td>
   <td style="text-align:right;"> 0.2101 </td>
   <td style="text-align:right;"> 0.5857 </td>
   <td style="text-align:right;"> -0.2381 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Butler (1986) 1_1 </td>
   <td style="text-align:left;"> Primary/elementary school </td>
   <td style="text-align:left;"> Feedback </td>
   <td style="text-align:left;"> Literacy: writing </td>
   <td style="text-align:left;"> Primary outcome </td>
   <td style="text-align:right;"> 1986 </td>
   <td style="text-align:left;"> Israel </td>
   <td style="text-align:left;"> Journal article </td>
   <td style="text-align:right;"> 1.5390 </td>
   <td style="text-align:right;"> 0.1742 </td>
   <td style="text-align:right;"> 1.8804 </td>
   <td style="text-align:right;"> 1.1976 </td>
  </tr>
</tbody>
</table>
**Make Primary/Elementary and High school forest plots and display them**

```r
Primary_plot <- ggplot(data=na.omit(subset(Primary_feedback, select=c(Author, SMD, CIlower, CIupper))),
                    aes(y=Author, x=SMD, xmin=CIlower, xmax=CIupper))+
                    geom_point(color='black', shape=15) +
                    geom_errorbarh(height=.7, linetype=1) +
                    scale_x_continuous(limits=c(-4,4), name='Standardized Mean Difference (95% CI)') +
                    ylab('Reference') +
                    geom_vline(xintercept=0, color='black', linetype='dashed') +
                    theme_classic() +
                    ggtitle("Primary School, Feedback Strand, Primary outcome")

High_plot <- ggplot(data=na.omit(subset(High_feedback, select=c(Author, SMD, CIlower, CIupper))),
                    aes(y=Author, x=SMD, xmin=CIlower, xmax=CIupper))+
                    geom_point(color='black', shape=15) +
                    geom_errorbarh(height=.7, linetype=1) +
                    scale_x_continuous(limits=c(-4,4), name='Standardized Mean Difference (95% CI)') +
                    ylab('Reference') +
                    geom_vline(xintercept=0, color='black', linetype='dashed') +
                    theme_classic() +
                    ggtitle("High School, Feeback Strand, Primary Outcome")

Primary_plot
```

![](Master_figs/unnamed-chunk-10-1.png)<!-- -->
  
**Get all study data (Primary outcome only), convert all missing data to NA. Remove "No information" cells (from educational setting column). Plot SMD/SESMD scatter plots groups by intervention, educational setting, strand, and country**

```r
# Pass all Primary outcome studies to R dataframe (from Python)
master_df <- data.frame(py$Primary)

# Clean data (insert NA for missing values and remove 'no info' cells)
master_df$Intervention <- as.character(master_df$Intervention)
master_df$Intervention[master_df$Intervention=="NaN"] <- NA
master_df$Intervention <- as.factor(master_df$Intervention)

master_df$EducationalSetting <- as.character(master_df$EducationalSetting)
master_df$EducationalSetting[master_df$EducationalSetting=="NaN"] <- NA
master_df$EducationalSetting[master_df$EducationalSetting=="No information provided"] <- NA
master_df$EducationalSetting[master_df$EducationalSetting=="Other educational setting (please specify)"] <- NA
master_df$EducationalSetting <- as.factor(master_df$EducationalSetting)

master_df$Strand <- as.character(master_df$Strand)
master_df$Strand[master_df$Strand=="NaN"] <- NA
master_df$Strand <- as.factor(master_df$Strand)

master_df$Country <- as.character(master_df$Country)
master_df$Country[master_df$Country=="NaN"] <- NA
master_df$Country <- as.factor(master_df$Country)

master_df$Outcome <- as.character(master_df$Outcome)
master_df$Outcome[master_df$Outcome=="NaN"] <- NA
master_df$Outcome <- as.factor(master_df$Outcome)

master_df$Country <- as.character(master_df$Country)
master_df$Country[master_df$Country=="UK (Select all that apply)"] <- "UK"

# get means for SMD and SESMD
master_df_mean_SMD <- mean(master_df$SMD, na.rm=TRUE)
master_dfk_mean_SESMD <- mean(master_df$SESMD, na.rm=TRUE)

# uncomment to view data in dataviewer
#View(master_df) 

# Make SMD/SESMD scatter plot, (color) grouped by Intervention
smd_intervention <- ggplot(data=subset(master_df, !is.na(Intervention)), aes(SMD, SESMD, color=Intervention)) + 
    geom_point(alpha=1, na.rm=TRUE, size=1.5) +
    theme_grey() +
    geom_vline(xintercept=master_df_mean_SMD, linetype="dotted", color="black", size=1) +
    theme(legend.title = element_text(color = "black", size = 10),
          legend.text = element_text(color = "black", size = 11)) +
    theme(legend.position="right") +
    guides(fill=guide_legend(nrow=5, byrow=TRUE)) +
    theme(legend.title=element_blank()) +
    annotate(geom="text", x=master_df_mean_SMD+.15, y=-.1, label=round(master_df_mean_SMD, 2), color="black") +
    ylim(-0.2, 1.75) +
    xlim(-1.5, 2.5) +
    ggtitle("SMD by SESMD grouped by Intervention")

# Make SMD/SESMD scatter plot, (color) grouped by Educational Setting
smd_edusetting <- ggplot(data=subset(master_df, !is.na(EducationalSetting)), aes(SMD, SESMD, color=EducationalSetting)) + 
    geom_point(alpha=1, na.rm=TRUE, size=1.5) +
    theme_grey() +
    geom_vline(xintercept=master_df_mean_SMD, linetype="dotted", color="black", size=1) +
    theme(legend.title = element_text(color = "black", size = 10),
          legend.text = element_text(color = "black", size = 11)) +
    theme(legend.position="right") +
    guides(fill=guide_legend(nrow=5, byrow=TRUE)) +
    theme(legend.title=element_blank()) +
    annotate(geom="text", x=master_df_mean_SMD+.15, y=-.1, label=round(master_df_mean_SMD, 2), color="black") +
    ylim(-0.2, 1.75) +
    xlim(-1.5, 2.5) +
    ggtitle("SMD by SESMD grouped by Educational Setting")

# Make SMD/SESMD scatter plot, (color) grouped by Strand
smd_strand <- ggplot(data=subset(master_df, !is.na(Strand)), aes(SMD, SESMD, color=Strand)) + 
    geom_point(alpha=1, na.rm=TRUE, size=1.5) +
    theme_grey() +
    geom_vline(xintercept=master_df_mean_SMD, linetype="dotted", color="black", size=1) +
    theme(legend.title = element_text(color = "black", size = 10),
          legend.text = element_text(color = "black", size = 11)) +
    theme(legend.position="right") +
    guides(fill=guide_legend(nrow=5, byrow=TRUE)) +
    theme(legend.title=element_blank()) +
    annotate(geom="text", x=master_df_mean_SMD+.15, y=-.1, label=round(master_df_mean_SMD, 2), color="black") +
    ylim(-0.2, 1.75) +
    xlim(-1.5, 2.5) +
    ggtitle("SMD by SESMD grouped by Strand")

# Make SMD/SESMD scatter plot, (color) grouped by Country
smd_country <- ggplot(data=subset(master_df, !is.na(Country)), aes(SMD, SESMD, color=Country)) + 
    geom_point(alpha=1, na.rm=TRUE, size=1.5) +
    theme_grey() +
    geom_vline(xintercept=master_df_mean_SMD, linetype="dotted", color="black", size=1) +
    theme(legend.title = element_text(color = "black", size = 10),
          legend.text = element_text(color = "black", size = 11)) +
    theme(legend.position="right") +
    guides(fill=guide_legend(nrow=5, byrow=TRUE)) +
    theme(legend.title=element_blank()) +
    annotate(geom="text", x=master_df_mean_SMD+.15, y=-.1, label=round(master_df_mean_SMD, 2), color="black") +
    ylim(-0.2, 1.75) +
    xlim(-1.5, 2.5) +
    ggtitle("SMD by SESMD grouped by Country")

# use GridExtra to display all 4 plots neatly
grid.arrange(smd_intervention, smd_edusetting, smd_strand, smd_country, nrow=4)
```

![](Master_figs/unnamed-chunk-11-1.png)<!-- -->



