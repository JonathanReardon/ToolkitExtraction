## Data frame 1: Study, research and design variables

| Description | Question | Coding options | Columns |
| ------------- | ------------- | ------------- | ------------- |
| Record ID  | || id |
| Short Title || | pub_author |
| Publication Year  | || pub_year |
| Abstract | Abstract || | abstract |
| Toolkit strand | Toolkitstrand | strand_raw<br>strand_info |
| Publication type in EPPI || pub_eppi |
| Publication Type  | What is the publication type? | 1=Journal Article<br>2=Dissertation or thesis<br>3=Technical report<br>Book or book chapter<br>5-Conference paper<6>Other (Please specify) |pub_type_raw<br>put_type_ht<br>put_type_info |
| Country | In which country/countries was the study carried out? | List of countries | loc_country_raw<br>loc_country_ht<br>loc_country_info |
| Educational Setting | What is the educational settings? | 1=Nursery school/pre-school<br>2=Primary/elementary school<br>3=Middle school<br>4=Secondary/High school<br>5=Residential/boarding school<br>6=Independent/private school<br>7=Home<br>8=Further education/junior or community college<br>9=Other educational setting (please specify><br>10=Outdoor adventure settings<br>11=No information provided | int_setting_raw<br>int_setting_ht<br>int_setting_info |
| Ecological Validity | How realistic was the study? | 1=High ecological validity<Br>2=Low ecological validity<br>3=Unclear | eco_valid_raw<br>eco_valid_ht<br>eco_calid_info |
| Age of participants | What is the age of the students? | 3-18<br>No information provided |part_age_raw<br>part_age_ht<br>part_age_info |
| Number of schools treatment | What is the number of schools involved in the intervention group(s)? | Open answer (HT) |school_treat_ht<br>school_treat_info |
| Number schools control | What is the number of schools involved in the control or comparison group? | Open answer (HT) | school_cont_ht<br>school_cont_info |
| Number schools total | What is the total number of schools involved | Open answer (HT) | school_total_ht<br>school_total_info |
| NA | Not provided/unclear/not applicable | School NA | school_na |
| Number classes treatment | What is the total number of classes involved in the intervention group? | Open answer (HT) | class_treat_ht<br>class_treat_info |
| Number classes control | What is the number of classes involved in the control or comparison group? | Open answer (HT) | class_cont_ht<br>class_cont_info |
  
| Number classes total | What is the total number of classes involved? | Open answer (HT) | class_total_ht<br>class_total_info |
| NA | Not provided/unclear/not applicable | class NA | class_na |

| Treatment groups | is there more than one treatment group? | 1=Yes<br>2=No<br>3=Not specified or N/A | treat_group_raw<br>treat_group_ht<br>treat_group_info |

| Participant assignment | How were participants assigned | 1=Random(please specify)<br>2=Non-random, but matched<br>3=Non-random - naturally occuring sample<br>4=Unclear<br>5=Not assigned - naturally occuring sample<br>6=Retrospective Quasi Experimental Design (QED)<br>7=Regression discontinuity |part_assig_raw<br>part_assig_ht<br>part_assig_info |

| Level of assignment | What was the level of assignment? | 1=Individual<br>2=Class<br>3=School - cluster<br>4=School - multi-site<br>5=Region or district<br>6=Not provided/not available<br>7=Not applicable |level_assig_raw<br>level_assig_ht<br>level_assig_info |

| Intervention design | What was the study design? | 1=Individual RCT<br>2=Cluster RCT<br>3=Multisite RCT<br>4=Prospective QED<br>5=Retrospective QED<br>6=Interrupted time series QED<br>7=Regression discontinuity with randomisation<br>8=Regression Discontinuity - not randomised<br>9=Regression Continuity - naturally occuring| int_desig_raw<br>int_desig_ht<br>int_desig_info |

| Randomisation | Are details of randomisation provided? | 1=Yes<br>2=Not applicable<br>3=No/Unclear| rand_raw<br>rand_ht<br>rand_info |
