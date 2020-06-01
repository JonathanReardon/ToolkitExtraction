import json
from collections import Counter
from pprint import pprint
import numpy as np
import pandas as pd

# input data file name (.csv) with full path
datafile = '/home/jon/json/ToolkitExtraction/Data/Batch1.json'

# import dataset (uncomment to select dataset of choice)
with open(datafile) as f:
    data=json.load(f)

# for missing or unavailable data
exclude=np.nan

# flatten json into list of lists
def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []
    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr
    results = extract(obj, arr, key)
    return results

x = extract_values(data,'AttributeName')
y = extract_values(data,'AttributeId')

df=[]
for xs, ys in zip(x, y):
    df.append([xs, ys])

# Variable option counts
""" strand_option = {"Toolkit strand(s) (select at least one Toolkit strand)": 34}

single_option = {"What was the level of assignment?": 7, 
                 "How were participants assigned?": 8,
                 "How realistic was the study?": 4, 
                 "What is the gender of the students?": 5,
                 "Section 1 What is the publication type?": 6,
                 "What is the educational setting (Select ALL that apply)": 12,
                 "Does the study report any group differences at baseline? ": 3,
                 "What was the study design?": 10,
                 "Is comparability taken into account in the analysis?": 4,
                 "Are the variables used for comparability reported?": 4,
                 "If yes, which variables are used for comparability?": 6,
                 "What type of organisation was responsible for providing the intervention?": 7,
                 "Was training for the intervention provided?": 4,
                 "Is attrition or drop out reported?": 4,} 

multi_option = {"In which country/countries was the study carried out? (Select ALL that apply)": 188,
                "What is the age of the students? (Select ALL that apply)": 18,
                "Who is the focus of the intervention? (Select ALL that apply)": 9,
                "What is the intervention teaching approach? (Select ALL that apply)": 7,
                "When did the intervention take place?  (Select ALL that apply)": 7,
                "Who was responsible for the teaching at the point of delivery? (Select ALL that apply)": 11,
                "What is the educational setting (Select ALL that apply)": 12} """

strand_output =   [{#Toolkit strand(s) (select at least one Toolkit strand)
                    5407042: 'Toolkit: Arts participation ',
                    5407043: 'Toolkit: Aspiration interventions',
                    5407044: 'Toolkit: Behaviour interventions',
                    5407045: 'Toolkit: Block scheduling',
                    5407046: 'Toolkit: Built environment',
                    5407047: 'Toolkit: Collaborative learning',
                    5407048: 'Toolkit: Digital technology',
                    5407049: 'Toolkit: Early years intervention',
                    5407050: 'Toolkit: Extending school time',
                    5407051: 'Toolkit: Feedback',
                    5407052: 'Toolkit: Homework',
                    5407053: 'Toolkit: Individualised instruction',
                    5407054: 'Toolkit: Learning styles',
                    5407055: 'Toolkit: Mastery learning',
                    5407056: 'Toolkit: Metacognition and self-regulation',
                    5407057: 'Toolkit: Mentoring',
                    5407058: 'Toolkit: One to one tuition',
                    5407059: 'Toolkit: Oral language interventions',
                    5407060: 'Toolkit: Outdoor adventure learning',
                    5407061: 'Toolkit: Parental engagement',
                    5407062: 'Toolkit: Peer Tutoring',
                    5407063: 'Toolkit: Performance pay',
                    5407064: 'Toolkit: Phonics',
                    5407065: 'Toolkit: Reading comprehension strategies',
                    5407066: 'Toolkit: Reducing class size',
                    5407067: 'Toolkit: Repeating a year',
                    5407068: 'Toolkit: School uniform',
                    5407069: 'Toolkit: Setting or streaming',
                    5407070: 'Toolkit: Small Group Tuition',
                    5407071: 'Toolkit: Social and emotional learning',
                    5407072: 'Toolkit: Sports participation',
                    5407073: 'Toolkit: Summer schools',
                    5407074: 'Toolkit: Teaching assistants'
                }]

single_output =   [{# What was the level of assignment?
                    5215244: 'Individual',
                    5215245: 'Class',
                    5215246: 'School - cluster',
                    5215247: 'School - multi-site',
                    5215248: 'Region or district',
                    5215249: 'Not provided/ not available'},
                    {# How were participants assigned?
                    5215251: 'Random (please specify)',
                    5215252: 'Non-random, but matched',
                    5215253: 'Non-random, not matched prior to treatment',
                    5215565: 'Unclear',
                    5641086: 'Not assigned - naturally occurring sample',
                    5641087: 'Retrospective Quasi Experimental Design (QED)',
                    5641088: 'Regression discontinuity'},
                    {# How realistic was the study?
                    5215255: 'High ecological validity',
                    5215256: 'Low ecological validity',
                    5215257: 'Unclear'},
                    {# What is the gender of the students?
                    5215642: 'Female only',
                    5215643: 'Male only',
                    5215644: 'Mixed gender',
                    5513032: 'No information provided'},
                    {# Section 1 What is the publication type?
                    5215227: 'Journal article',
                    5215228: 'Dissertation or thesis',
                    5215229: 'Technical report',
                    5215230: 'Book or book chapter',
                    5215231: 'Conference paper'},
                    {# What is the educational setting (Select ALL that apply)
                    5215410: 'Nursery school/pre-school',
                    5215411: 'Primary/elementary school',
                    5215412: 'Middle school',
                    5215413: 'Secondary/High school',
                    5215414: 'Residential/boarding school',
                    5215415: 'Independent/private school',
                    5215416: 'Home',
                    5215417: 'Other educational setting (please specify)',
                    5215418: 'Outdoor adventure setting',
                    5215566: 'Further education/junior or community college',
                    5513033: 'No information provided'},
                    {# Does the study report any group differences at baseline?
                    5406860: 'No/Unclear', 
                    5406866: 'Yes'},
                    {# What was the study design?
                    5406847: 'Individual RCT',
                    5406849: 'Cluster RCT',
                    5406851: 'Multisite RCT',
                    5406852: 'Prospective QED',
                    5406853: 'Interrupted time series QED',
                    5406854: 'Regression Discontinuity - not randomised',
                    5406856: 'Retrospective QED  ',
                    5406857: 'Regression Continuity  - naturally occurring',
                    5407075: 'Regression Discontinuity with randomisation'},
                    {# Is comparability taken into account in the analysis?
                    5406855: 'Unclear or details not provided', 
                    5406861: 'Yes', 
                    5406864: 'No'},
                    {# Are the variables used for comparability reported?"
                    5406859: 'Yes', 
                    5406862: 'No', 
                    5406863: 'N/A'},
                    {# If yes, which variables are used for comparability?
                    5407122: 'Educational attainment',
                    5407123: 'Gender',
                    5407124: 'Socio-economic status',
                    5407128: 'Special educational needs',
                    5407129: 'Other (please specify)'},
                    {# What type of organisation was responsible for providing the intervention?
                    5215491: 'School or group of schools',
                    5215492: 'Charity or voluntary organisation',
                    5215493: 'University/ researcher design',
                    5215494: 'Local education authority or district',
                    5215495: 'Private or commercial company',
                    5215496: 'Other (please provide details)'},
                    {# Was training for the intervention provided?
                    5215498: 'Yes (Please specify)',
                    5215499: 'No',
                    5215500: 'Unclear/ Not specified'},
                    {# Is attrition or drop out reported?
                    5407034: 'Yes', 
                    5407035: 'No', 
                    5407036: 'Unclear (please add notes)'}]


multi_output =    [{# In which country/countries was the study carried out? (Select ALL that apply)
                    5215276: 'USA',
                    5215277: 'UK (Select all that apply)',
                    5215278: 'Afghanistan',
                    5215279: 'Angola',
                    5215280: 'Armenia',
                    5215281: 'Argentina',
                    5215282: 'Australia',
                    5215283: 'Austria',
                    5215284: 'Bahamas, The',
                    5215285: 'Bahrain',
                    5215286: 'Bangladesh',
                    5215287: 'Barbados',
                    5215288: 'Belgium',
                    5215289: 'Belarus',
                    5215290: 'Belize',
                    5215291: 'Bolivia',
                    5215292: 'Brazil',
                    5215293: 'Botswana',
                    5215294: 'Bulgaria',
                    5215295: 'Burkina Faso',
                    5215296: 'Cambodia',
                    5215297: 'Cameroon',
                    5215298: 'Canada',
                    5215299: 'Chile',
                    5215300: 'China',
                    5215301: 'Congo',
                    5215302: 'Croatia',
                    5215303: 'Cuba',
                    5215304: 'Colombia',
                    5215305: 'Cyprus',
                    5215306: 'Czech Republic',
                    5215307: 'Dominican Republic',
                    5215308: 'Denmark',
                    5215309: 'Egypt',
                    5215310: 'Ecuador',
                    5215311: 'Eritrea',
                    5215312: 'Estonia',
                    5215313: 'Finland',
                    5215314: 'Gambia, The',
                    5215315: 'France',
                    5215316: 'Georgia',
                    5215317: 'Ghana',
                    5215318: 'Germany',
                    5215319: 'Greece',
                    5215320: 'Guatemala',
                    5215321: 'Guinea-Bissau',
                    5215322: 'Haiti',
                    5215323: 'Honduras',
                    5215324: 'Hong Kong (see China)',
                    5215325: 'Hungary',
                    5215326: 'Iceland',
                    5215327: 'India',
                    5215328: 'Indonesia',
                    5215329: 'Iran',
                    5215330: 'Ireland',
                    5215331: 'Israel',
                    5215332: 'Italy',
                    5215333: "Côte d'Ivoire / Ivory Coast",
                    5215334: 'Kazakhstan ',
                    5215335: 'Jordan',
                    5215336: 'Kenya',
                    5215337: 'South Korea / Republic of Korea',
                    5215338: 'Kuwait',
                    5215339: 'Japan',
                    5215340: 'Jamaica',
                    5215341: 'Lao (or Laos)',
                    5215342: 'Lebanon',
                    5215343: 'Lesotho',
                    5215344: 'Liberia',
                    5215345: 'Lithuania',
                    5215346: 'Luxembourg',
                    5215347: 'Malawi',
                    5215348: 'Madagascar',
                    5215349: 'Malaysia',
                    5215350: 'Mali',
                    5215351: 'Mexico',
                    5215352: 'Micronesia',
                    5215353: 'Marshall Islands',
                    5215354: 'Mozambique',
                    5215355: 'Mongolia ',
                    5215356: 'Myanmar (Burma)',
                    5215357: 'Namibia',
                    5215358: 'Nepal',
                    5215359: 'New Zealand',
                    5215360: 'The Netherlands',
                    5215361: 'Nicaragua',
                    5215362: 'Niger',
                    5215363: 'Nigeria',
                    5215364: 'Pakistan',
                    5215365: 'Norway',
                    5215366: 'Panama',
                    5215367: 'Papua New Guinea',
                    5215368: 'Peru',
                    5215369: 'Philippines',
                    5215370: 'Poland',
                    5215371: 'Portugal',
                    5215372: 'Puerto Rico (US dependency)',
                    5215373: 'Romania',
                    5215374: 'Russia',
                    5215375: 'Rwanda',
                    5215376: 'Samoa',
                    5215377: 'San Marino',
                    5215378: 'Saudi Arabia',
                    5215379: 'Serbia',
                    5215380: 'Senegal',
                    5215381: 'Singapore',
                    5215382: 'Sierra Leone',
                    5215383: 'Slovakia',
                    5215384: 'Slovenia',
                    5215385: 'South Africa',
                    5215386: 'Spain',
                    5215387: 'Sri Lanka',
                    5215388: 'Suriname',
                    5215389: 'Swaziland / Eswatini',
                    5215390: 'Sweden',
                    5215391: 'Switzerland',
                    5215392: 'Syria',
                    5215393: 'Taiwan',
                    5215394: 'Thailand',
                    5215395: 'Tanzania',
                    5215396: 'Trinidad and Tobago',
                    5215397: 'Tunisia',
                    5215398: 'Uganda',
                    5215399: 'Ukraine',
                    5215400: 'Uzbekistan',
                    5215401: 'Vanuatu',
                    5215402: 'Venezuela',
                    5215403: 'Vietnam',
                    5215404: 'West Indies (Use for Caribbean colonial dependencies)',
                    5215405: 'Yemen',
                    5215406: 'Zambia',
                    5215407: 'Zimbabwe',
                    5215587: 'England',
                    5215588: 'Scotland',
                    5215589: 'Northern Ireland',
                    5215590: 'Wales',
                    5215591: 'South Sudan',
                    5215592: 'Tuvalu',
                    5215593: 'Albania',
                    5215594: 'Azerbaijan',
                    5215595: 'Benin',
                    5215596: 'Bhutan',
                    5215597: 'Bosnia and Herzegovina',
                    5215598: 'Brunei Darussalam',
                    5215599: 'Cabo Verde',
                    5215600: 'Central African Republic',
                    5215601: 'Chad',
                    5215602: 'Costa Rica',
                    5215603: 'El Salvador',
                    5215604: 'Equatorial Guinea',
                    5215605: 'Ethiopia',
                    5215606: 'Fiji',
                    5215607: 'Gabon',
                    5215608: 'Grenada',
                    5215609: 'Guinea',
                    5215610: 'Guyana',
                    5215611: 'Iraq',
                    5215612: 'Kiribati',
                    5215613: 'Kyrgyzstan',
                    5215614: 'Latvia',
                    5215615: 'Libya',
                    5215616: 'Liechtenstein',
                    5215617: 'Maldives',
                    5215618: 'Malta',
                    5215619: 'Mauritania',
                    5215620: 'Mauritius',
                    5215621: 'Nauru',
                    5215622: 'Palau',
                    5215623: 'Qatar',
                    5215624: 'Moldova',
                    5215625: 'Saint Kitts and Nevis',
                    5215626: 'Saint Lucia',
                    5215627: 'Saint Vincent and the Grenadines',
                    5215628: 'São Tomé and Príncipe',
                    5215629: 'Seychelles',
                    5215630: 'Solomon Islands',
                    5215631: 'Somalia',
                    5215632: 'Sudan',
                    5215633: 'Tajikistan',
                    5215634: 'Macedonia',
                    5215635: 'Timor-Leste',
                    5215636: 'Togo',
                    5215637: 'Tonga',
                    5215638: 'Turkey',
                    5215639: 'Turkmenistan',
                    5215640: 'United Arab Emirates',
                    5215641: 'Uruguay'}
                    {# What is the age of the students? (Select ALL that apply)
                    5215433: '3',
                    5215434: '4',
                    5215435: '5',
                    5215436: '6',
                    5215437: '7',
                    5215438: '8',
                    5215439: '9',
                    5215440: '10',
                    5215441: '11',
                    5215442: '12',
                    5215443: '13',
                    5215444: '14',
                    5215445: '15',
                    5215446: '16',
                    5215447: '17',
                    5215448: '18',
                    5513031: 'No information provided'},
                    {# Who is the focus of the intervention? (Select ALL that apply)
                    5215502: 'Students',
                    5215503: 'Teachers',
                    5215504: 'Teaching assistants',
                    5215505: 'Other education practitioners',
                    5215506: 'Non-teaching staff',
                    5215507: 'Senior management',
                    5215508: 'Parents',
                    5215509: 'Other (Please specify)'},
                    {# What is the intervention teaching approach? (Select ALL that apply)
                    5215511: 'Student alone (self-administered)',
                    5215512: 'Small group/intensive support (3-5)',
                    5215513: 'Large group/class teaching (+6)',
                    5215586: 'One to one',
                    5216713: 'Paired learning',
                    5216714: 'Other (Explain in notes)'},
                    {# When did the intervention take place?  (Select ALL that apply)
                    5215580: 'During regular school hours ',
                    5215581: 'Before/after school',
                    5215582: 'Evenings and/or weekends',
                    5215583: 'Summer/ holiday period',
                    5215584: 'Other (please specify)',
                    5215585: 'Unclear/ not specified'},
                    {# Who was responsible for the teaching at the point of delivery? (Select ALL that apply)
                    5215553: 'Research staff',
                    5215554: 'Class teachers',
                    5215555: 'Teaching assistants',
                    5215556: 'Other school staff',
                    5215557: 'External teachers',
                    5215558: 'Parents/carers',
                    5215559: 'Lay persons/volunteers',
                    5215560: 'Peers',
                    5215561: 'Digital technology',
                    5215562: 'Unclear/not specified'},
                    {# What is the educational setting (Select ALL that apply)
                    5215410: 'Nursery school/pre-school',
                    5215411: 'Primary/elementary school',
                    5215412: 'Middle school',
                    5215413: 'Secondary/High school',
                    5215414: 'Residential/boarding school',
                    5215415: 'Independent/private school',
                    5215416: 'Home',
                    5215417: 'Other educational setting (please specify)',
                    5215418: 'Outdoor adventure setting',
                    5215566: 'Further education/junior or community college',
                    5513033: 'No information provided'}]

# extract user inputted comments for each var
def var_comments(codes):
    all_comments = []
    comments, text = [], []
    for var in range(len(codes)):
        user_comments_holder, highlight_text_holder = [], []
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                user_comments, highlighted_text =  [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            if data["References"][section]["Codes"][study]["AdditionalText"]:
                                user_comments.append(data["References"][section]["Codes"][study]["AdditionalText"])
                            if "ItemAttributeFullTextDetails" in data["References"][section]["Codes"][study]:
                                if data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"]:
                                    for i in range(len(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"])):
                                        highlighted_text.append(data["References"][section]["Codes"][study]["ItemAttributeFullTextDetails"][i]["Text"])
                if len(user_comments)==0:
                    user_comments=exclude 
                if len(highlighted_text)==0:
                    highlighted_text=exclude
                user_comments_holder.append(user_comments)
                highlight_text_holder.append(highlighted_text)
            else:
                user_comments_holder.append(exclude)
                highlight_text_holder.append(exclude)

        comments.append(user_comments_holder)
        text.append(highlight_text_holder)
    all_comments.append(comments)
    all_comments.append(text)
    return all_comments

single_output_text = var_comments(single_output)
multi_output_text  = var_comments(multi_output)

# data extraction for variables with one output
def get_data(data_codes):
    all=[]
    for var in range(len(data_codes)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in data_codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind, holdervalue = value, key
                if len(holderfind) == 0:
                    holderfind = exclude
                holder.append(holderfind)
            else:
                holder.append("No 'Codes' Section")
        all.append(holder)
    return all
data_single = get_data(single_output)

# data extraction for variables with multiple outputs (e.g. age)
def get_multi_data(data_codes):
    all=[]
    for var in range(len(data_codes)):
        holder=[]
        for section in range(len(data["References"])):
            if "Codes" in data["References"][section]:
                holderfind, holdervalue = [], []
                for study in range(len(data["References"][section]["Codes"])):
                    for key, value in data_codes[var].items():
                        if key == data["References"][section]["Codes"][study]["AttributeId"]:
                            holderfind.append(value)
                if len(holderfind)==0:
                    holderfind=exclude
                holder.append(holderfind)
        all.append(holder)
    return all
data_multi = get_multi_data(multi_output)

# get strand data
def get_strands(strand_codes):
  finds=[]
  for var in range(len(strand_codes)):
    for section in range(len(data["References"])):
        if "Codes" in data["References"][section]["Codes"]:
            if "Outcomes" in data["References"][section]:
                if "OutcomeCodes" in data["References"][section]["Outcomes"][0]:
                    for study in range(len(data["References"][section]["Outcomes"][0]["OutcomeCodes"]["OutcomeItemAttributesList"])):
                        for key,value in strand_codes[var].items():
                                if key == data["References"][section]["Outcomes"][0]["OutcomeCodes"]["OutcomeItemAttributesList"][study]["AttributeId"]:
                                    strandfind=value
                    finds.append(strandfind)
                else:
                    finds.append(exclude)
            else:
                finds.append(exclude)
        else:
            finds.append(exclude)
  return finds
strand_data = get_strands(strand_output) 

# section checker
def section_checker():
    global codes_check, outcomes_check, outcomecodes_check
    codes_check=[]
    outcomes_check=[]
    outcomecodes_check=[]
    for section in range(len(data["References"])):
        Codes="No"
        Outcomes="No"
        OutcomeCodes="No"
        if "Codes" in data["References"][section]:
            Codes="Yes"
            if "Outcomes" in data["References"][section]:
                Outcomes="Yes"
                if "OutcomeCodes" in data["References"][section]["Outcomes"][0]:
                    OutcomeCodes="Yes"
            
        codes_check.append(Codes)
        outcomes_check.append(Outcomes)
        outcomecodes_check.append(OutcomeCodes)
section_checker()

# get basic info from first outer layer 
def get_basic_info():
    global itemids, titles, year, abstract
    itemids, titles, year, abstract = [], [], [], []
    for section in range(len(data["References"])):
        if data["References"][section]["ItemId"]:
            itemids.append(data["References"][section]["ItemId"])
        else:
            itemids.append(exclude)
        if data["References"][section]["ShortTitle"]:
            titles.append(data["References"][section]["ShortTitle"])
        else:
            titles.append(exclude)
        if data["References"][section]["Year"]:
            year.append(int(data["References"][section]["Year"]))
        else:
            year.append(exclude)
        if data["References"][section]["Abstract"]:
            abstract.append(data["References"][section]["Abstract"])
        else:
            abstract.append(exclude)
get_basic_info()

# get stats info from 'Outcomes' section
def get_stats():
    global outcometext, interventiontext, SMD, SESMD, CIupperSMD, CIlowerSMD
    outcometext, interventiontext, SMD, SESMD, CIupperSMD, CIlowerSMD = [], [], [], [], [], []
    for section in range(len(data["References"])):
        if "Outcomes" in data["References"][section]:
            outcometext.append(data["References"][section]["Outcomes"][0]["OutcomeText"])
            interventiontext.append(data["References"][section]["Outcomes"][0]["InterventionText"])
            SMD.append(data["References"][section]["Outcomes"][0]["SMD"])
            SESMD.append(data["References"][section]["Outcomes"][0]["SESMD"])
            CIupperSMD.append(data["References"][section]["Outcomes"][0]["CIUpperSMD"])
            CIlowerSMD.append(data["References"][section]["Outcomes"][0]["CILowerSMD"])
                    
        else:
            outcometext.append(exclude)
            interventiontext.append(exclude)
            SMD.append(exclude)
            SESMD.append(exclude)
            CIupperSMD.append(exclude)
            CIlowerSMD.append(exclude)
get_stats()

# create full dataframe (all data extracted [verbose])
""" data_frame_verbose = pd.DataFrame(list(zip(itemids, 
                                            titles, 
                                            year, 
                                            strand_data,
                                            outcometext,
                                            interventiontext,
                                            data_single[0],  single_output_text[0][0], single_output_text[1][0],
                                            data_single[1],  single_output_text[0][1], single_output_text[1][1],
                                            data_single[2],  single_output_text[0][2], single_output_text[1][2],
                                            data_single[3],  single_output_text[0][3], single_output_text[1][3],
                                            data_single[4],  single_output_text[0][4], single_output_text[1][4],
                                            data_single[5],  single_output_text[0][5], single_output_text[1][5],
                                            data_single[6],  single_output_text[0][6], single_output_text[1][6],
                                            data_single[7],  single_output_text[0][7], single_output_text[1][7],
                                            data_single[8],  single_output_text[0][8], single_output_text[1][8],
                                            data_single[9],  single_output_text[0][9], single_output_text[1][9],
                                            data_single[10],  single_output_text[0][10], single_output_text[1][10],
                                            data_single[11],  single_output_text[0][11], single_output_text[1][11],
                                            data_single[12],  single_output_text[0][12], single_output_text[1][12],
                                            data_single[13],  single_output_text[0][13], single_output_text[1][13],
                                            data_multi[0], multi_output_text[0][0], multi_output_text[1][0],
                                            data_multi[1], multi_output_text[0][1], multi_output_text[1][1],
                                            data_multi[2], multi_output_text[0][2], multi_output_text[1][2],
                                            data_multi[3], multi_output_text[0][3], multi_output_text[1][3],
                                            data_multi[4], multi_output_text[0][4], multi_output_text[1][4],
                                            data_multi[5], multi_output_text[0][5], multi_output_text[1][5],
                                            data_multi[6], multi_output_text[0][6], multi_output_text[1][6],
                                            SMD, 
                                            SESMD, 
                                            CIupperSMD, 
                                            CIlowerSMD,
                                            codes_check, 
                                            outcomes_check, 
                                            outcomecodes_check)), 
                                    columns=['ItemID', 
                                             'Author', 
                                             'Year', 
                                             'Strand',
                                             'Outcome', 
                                             'Intervention',
                                             # VARIABLE                       USER COMMENTS                           HIGHLIGHTED TEXT
                                             'LevelofAssignment',            'LevelofAssignmentComments',            'LevelofAssignmentHighlightedText',
                                             'ParticipantAssignment',        'ParticipantAssignmentComents',         'ParticipantAssignmentHighlightedText',
                                             'StudyRealism',                 'StudyRealismComments',                 'StudyRealismHighlightedText',
                                             'StudentGender',                'StudentGenderComments',                'StudentGenderHighlightedText',
                                             'PublicationType',              'PublicationTypeComments',              'PublicationTypeHighlightedText',
                                             'EducationalSetting',           'EducationalSettingComments',           'EducationalSettingHighlightedText',
                                             'Country',                      'CountryComments',                      'CountryHighlightedText',
                                             'GroupBaselineDifferences',     'GroupBaselineDifferencesComments',     'GroupBaselineDifferencesHighlightedText',
                                             'StudyDesign',                  'StudyDesignComments',                  'StudyDesignHighlightedText',
                                             'Comparability',                'ComparabilityComments',                'ComparabilityHighlightedText',
                                             'CompVariablesReported',        'CompVariablesReportedComments',        'CompVariablesReportedHighlightedText',
                                             'ComparabilityVariables',       'ComparabilityVariablesComments',       'ComparabilityVariablesHighlightedText',
                                             'InterventionOrg',              'InterventionOrgComments',              'InterventionOrgHighlightedText',
                                             'InterventionTrainingProvided', 'InterventionTrainingProvidedComments', 'InterventionTrainingProvidedHighlightedText',
                                             'StudentAge',                   'StudentAgeComments',                   'StudentAgeHighlightedText',
                                             'Attrition/DropOutReported',    'Attrition/DropOutReportedComments',    'Attrition/DropOutReportedHighlightedText', 
                                             'FocusofIntervention',          'FocusofInterventionComments',          'FocusofInterventionHighlightedText',
                                             'InterventionTeachingApproach', 'InterventionTeachingApproachComments', 'InterventionTeachingApproachHighlightedText',
                                             'InterventionTime',             'InterventionTimeComments',             'InterventionTimeHighlightedText',
                                             'WhoDeliveredTeaching',         'WhoDeliveredTeachingComments',         'WhoDeliveredTeachingHighlightedText',
                                             'EducationalSetting',           'EducationalSettingComments',           'EducationalSettingHighlightedText',
                                             'SMD', 
                                             'SESMD', 
                                             'CIupper', 
                                             'CIlower',
                                             'CodesSectionPresent', 
                                             'OutcomesSectionPresent', 
                                             'OutcomeCodesSectionPresent']) """

# create full dataframe (all data extracted [verbose])
data_frame_standard = pd.DataFrame(list(zip(itemids, titles, year, strand_data, outcometext, abstract, interventiontext,
                                            data_single[0],  data_single[1],   data_single[2],  data_single[3],  data_single[4], 
                                            data_single[5],  data_single[6],   data_single[7],  data_single[8],  data_single[9],  
                                            data_single[10], data_single[11],  data_single[12], data_single[13], data_multi[0],
                                            data_multi[1],   data_multi[2],    data_multi[3],   data_multi[4],   data_multi[5], 
                                            data_multi[6], 
                                            SMD, SESMD, CIupperSMD, CIlowerSMD,
                                            codes_check, outcomes_check, outcomecodes_check)), 
                                    columns=['ItemID', 'Author', 'Year', 'Strand','Outcome', 'Abstract','Intervention',
                                             'LevelofAssignment', 'ParticipantAssignment', 'StudyRealism', 'StudentGender', 'PublicationType',          
                                             'EducationalSetting', 'Country','GroupBaselineDifferences', 'StudyDesign', 'Comparability',               
                                             'CompVariablesReported', 'ComparabilityVariables', 'InterventionOrg', 'InterventionTrainingProvided','StudentAge',                
                                             'Attrition/DropOutReported', 'FocusofIntervention', 'InterventionTeachingApproach', 'InterventionTime', 'WhoDeliveredTeaching',        
                                             'EducationalSetting',         
                                             'SMD', 'SESMD', 'CIupper','CIlower',
                                             'CodesSectionPresent', 'OutcomesSectionPresent', 'OutcomeCodesSectionPresent'])

# convert all numerical data to float [verbose extraction]
""" data_frame_verbose["SMD"]     = data_frame_verbose["SMD"].astype(float)
data_frame_verbose["SESMD"]   = data_frame_verbose["SESMD"].astype(float)
data_frame_verbose["CIupper"] = data_frame_verbose["CIupper"].astype(float)
data_frame_verbose["CIlower"] = data_frame_verbose["CIlower"].astype(float)

# round statistical output to 4 decimal places [verbose extraction]
data_frame_verbose["SMD"]     = data_frame_verbose["SMD"].round(4)
data_frame_verbose["SESMD"]   = data_frame_verbose["SESMD"].round(4)
data_frame_verbose["CIupper"] = data_frame_verbose["CIupper"].round(4)
data_frame_verbose["CIlower"] = data_frame_verbose["CIlower"].round(4) """

# convert all numerical data to float [standard extraction]
data_frame_standard["SMD"]     = data_frame_standard["SMD"].astype(float)
data_frame_standard["SESMD"]   = data_frame_standard["SESMD"].astype(float)
data_frame_standard["CIupper"] = data_frame_standard["CIupper"].astype(float)
data_frame_standard["CIlower"] = data_frame_standard["CIlower"].astype(float)

# round statistical output to 4 decimal places [standard extraction]
data_frame_standard["SMD"]     = data_frame_standard["SMD"].round(4)
data_frame_standard["SESMD"]   = data_frame_standard["SESMD"].round(4)
data_frame_standard["CIupper"] = data_frame_standard["CIupper"].round(4)
data_frame_standard["CIlower"] = data_frame_standard["CIlower"].round(4)

# save verbose data (to .csv)
""" data_frame_verbose.to_csv("Sample_Output/May12th_verbose.csv", index=False, na_rep="NA")
 """
# save standard data (to .csv)
""" data_frame_standard.to_csv("test.csv", index=False, na_rep="NA") """