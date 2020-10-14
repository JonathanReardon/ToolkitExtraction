# sample size initial
sample_size_intervention_output = [{# What is the sample size for the intervention group?
                                    5407108: ''}]

sample_size_control_output = [{# What is the sample size for the control group?
                               5407109: ''}]

sample_size_second_intervention_output = [{# *What is the sample size for the second intervention group?}
                                           5407120: ''}]

sample_size_third_intervention_output = [{# *What is the sample size for the third intervention group?}
                                          5407121: ''}]

# sample size analyzed
sample_size_analyzed_intervention_output = [{# intervention group Number (n}
                                             5406980: ''}]

sample_size_analyzed_control_output = [{# control* group Number (n}
                                        5406985: ''}]

sample_size_analyzed_second_intervention_output = [{# If yes, please add for a second intervention* group (if needed)
                                                     5407135: ''}]

sample_size_analyzed_second_control_output = [{# If needed, please add for the control group
                                                5447053: ''}]






clustering_output = [{# Is clustering accounted for in the analysis?
                       5407158: "Yes",
                       5407159: "No",
                       5407160: "Unclear"}]

comparabiltiy_vars_reported = [{# Are the variables used for comparability reported?"
                                5406859: 'Yes', 
                                5406862: 'No', 
                                5406863: 'N/A'}]

if_yes_which_comparability_variables_reported_output = [{# If yes, which variables are used for comparability?
                                                         5407122: 'Educational attainment',
                                                         5407123: 'Gender',
                                                         5407124: 'Socio-economic status',
                                                         5407128: 'Special educational needs',
                                                         5407129: 'Other (please specify)'}]

comparability_output = [{# Is comparability taken into account in the analysis?
                          5406855: 'Unclear or details not provided', 
                          5406861: 'Yes', 
                          5406864: 'No'}]

baseline_differences_output = [{# Does the study report any group differences at baseline?
                               5406860: 'No/Unclear', 
                               5406866: 'Yes'}]

attrition_dropout_reported_output = [{# Is attrition or drop out reported?
                                      5407034: 'Yes',
                                      5407035: 'No',
                                      5407036: 'Unclear (please add notes)'}]

treatment_group_attrition = [{# What is the attrition in the treatment group?
                               5407037: ''}]

overall_percent_attrition = [{# What is the total or overall percentage attrition?
                              5407038: ''}]

study_design_output = [{# What was the study design?
                         5406847: 'Individual RCT',
                         5406849: 'Cluster RCT',
                         5406851: 'Multisite RCT',
                         5406852: 'Prospective QED',
                         5406856: 'Retrospective QED',
                         5406853: 'Interrupted time series QED',
                         5407075: 'Regression Discontinuity with randomisation',
                         5406854: 'Regression Discontinuity - not randomised',
                         5406857: 'Regression Continuity  - naturally occurring'}]

#############################
# STRAND SPECIFIC VARIABLES #
#############################

# MENTORING

mentor_identity = [{# Who were the mentors?
                    6120260: 'Older school students',
                    6120258: 'College or University students',
                    6120259: 'Adults (see description)',
                    6120256: 'Other (please specify)'}]

mentor_paid_or_compensated = [{# Were the mentors paid or compensated in any way?
                               6120253: 'Yes',
                               6120257: 'No',
                               6120261: 'Unclear/ No information'}]

mentor_organisation = [{# Who organised the mentoring?
                        6120254: 'The school(s)',
                        6120252: 'A local community group',
                        6120255: 'A charity or other voluntary organisation',
                        6120268: 'The local authority, government or state',
                        6120269: 'Other (please specify'}]

mentor_training = [{# Was training provided for mentors?
                    6120264: 'Yes',
                    6120267: 'No',
                    6120271: 'Unclear/ No information'}]

mentor_meeting_frequency = [{# How frequently did meetings take place?
                      6120232: 'Daily',
                      6120238: 'Weekly',
                      6120239: 'Every two to three weeks',
                      6120270: 'Monthly',
                      6120262: 'Every term',
                      6120263: 'Other (please specify)'}]

mentor_meeting_details_provided = [{# Are details provided of what happened in mentoring meetings?
                                    6120265: 'Yes',
                                    6120266: 'No',
                                    6120236: ''}]

mentor_meeting_location = [{# Where did meetings take place? (Select main setting)
                            6120233: 'In school',
                            6120234: 'In the home',
                            6120235: 'In the community',
                            6120237: 'By phone or online',
                            6120240: 'Other (please specify)',
                            6120244: 'Not specified'}]

mentoring_additional_experiences = [{# Did the mentoring involve additional experiences?
                                     6120251: 'Yes',
                                     6120247: 'No',
                                     6120241: 'Unclear/ not specified'}]

mentoring_programme_focus = [{# What was the focus or goals of the mentoring programme?
                              6120242: 'Improving academic attainment or performance',
                              6120243: 'Improving attendance',
                              6120245: 'Preventing or reducing problem behaviours in school',
                              6120246: 'Improving social interaction or social competence',
                              6120248: 'Preventing or addressing medical or psychological issues',
                              6120249: 'Improving career or employment aspirations and opportunities',
                              6120250: 'Increasing motivation or raising aspirations'}]

# ONE TO ONE
comparisons_available = [{# Which comparisons are available in this study? (Select all that apply)
                           5697922: 'With business as usual comparison (no additional support, but still being taught)',
                           5697923: 'With no equivalent teaching (e.g. summer school)',
                           5697924: 'With alternative tutor (e.g. teaching assistant vs volunteer)',
                           5697925: 'With alternative approach: Small group (2-5 pupils)',
                           5697926: 'With alternative approach: Large group (6-15 pupils)',
                           5697927: 'With alternative approach: computer/ digital technology',
                           5893849: 'With alternative approach: other (please specify)',
                           5697928: 'With pupils at a different level of attainment'}]

# SMALL GROUP

group_size = [{# Group size
                5566314: '2',
                5566308: '3',
                5566311: '4',
                5566316: '5',
                5566317: 'Mixed groups'}]

group_composition = [{# Group composition
                      5566303: 'Same level - low attainers',
                      5566307: 'Same level - average attainers',
                      5566309: 'Same level - high attainers',
                      5566310: 'Mixed attainment - all pupils',
                      5566312: 'Mixed attainment - high and low',
                      5566313: 'Mixed attainment - low and average',
                      5566315: 'Mixed attainment - high and average'}]


# MORE LOCATION INFORMATION

""" more_location_info   = [{# Is there more specific information about the location?
                         5215408: ''}] """
specific_to_location = [{# Specific to the location or place
                         5372848: ''}]
type_of_location     = [{# Information about the type of location
                         5372849: ''}]
no_location_info     = [{# No information provided
                         5372850: ''}]

########################################
# DESCRIPTIVE STATISTICS PRIMARY OUTCOME
########################################

desc_stats_primary_outcome = [{# Are descriptive statistics reported for the primary outcome?
                              5407095: "Yes",
                              5407096: "No"}]

intervention_group_number = [{# intervention group Number (n}
                              5406980: ''}]

intervention_group_pretest_mean = [{# intervention group Pre-test mean
                                    5406981: ''}]

intervention_group_pretest_sd = [{# intervention* group Pre-test SD
                                  5406982: ''}]

intervention_group_posttest_mean = [{# intervention* group Post-test mean
                                    5406983: ''}]

intervention_group_posttest_sd = [{# intervention* group Post-test SD
                                    5406989: ''}]

intervention_group_gain_score_mean = [{# intervention gain score mean
                                       5407130: ''}]

intervention_group_gain_score_sd = [{# intervention gain score sd
                                     5407131: ''}]

intervention_group_any_other_info = [{# intervention -  any other info}]
                                      5406990: ''}]

control_group_number = [{# control* group Number (n}
                         5406985: ''}]

control_group_pretest_mean = [{# control group Pre-test mean
                               5406986: ''}]

control_group_pretest_sd = [{# control group Pre-test SD
                             5406987: ''}]

control_group_posttest_mean = [{# control group Post-test mean
                                5406988: ''}]

control_group_posttest_sd = [{# control group Post-test SD
                              5406984: ''}]

control_group_gain_score_mean = [{# control gain score mean
                                  5407132: ''}]

control_group_gain_score_sd = [{# control gain score sd
                                5407133: ''}]

control_group_any_other_info = [{# control -  any other info}]
                                 5406991: ''}]

follow_up_data_reported = [{# Is there follow up data?
                             5407103: 'Yes',
                             5407104: 'No'}]

# INTERVENTION INFORMATION

intervention_name_output = [{# "What is the intervention name?"
                             5215238: ''}]

intervention_description_output = [{# How is the intervention described?
                                   5215563: ''}]

intervention_objectives_output = [{# What are the intervention objectives?
                                   5215564: ''}]

intervention_organisation_type_output = [{# What type of organisation was responsible for providing the intervention?
                                          5215491: "School or group of schools",
                                          5215492: "Charity or voluntary organisation",
                                          5215493: "University/ researcher design",
                                          5215494: "Local education authority or district",
                                          5215495: "Private or commercial company",
                                          5215496: "Other (please provide details)"}]

intervention_training_provided_output = [{# Was training for the intervention provided?
                                          5215498: "Yes (Please specify)",
                                          5215499: "No",
                                          5215500: "Unclear/ Not specified"}]

intervention_focus_output = [{# Who is the focus of the intervention? (Select ALL that apply)
                             5215502: "Students",
                             5215503: "Teachers",
                             5215504: "Teaching assistants",
                             5215505: "Other education practitioners",
                             5215506: "Non-teaching staff",
                             5215507: "Senior management",
                             5215508: "Parents",
                             5215509: "Other (Please specify)"}]

intervention_teaching_approach = [{# What is the intervention teaching approach? (Select ALL that apply)
                                  5215513: "Large group/class teaching (+6)",
                                  5215512: "Small group/intensive support (3-5)",
                                  5216713: "Paired learning",
                                  5215586: "One to one",
                                  5215511: "Student alone (self-administered)",
                                  5216714: "Other (Explain in notes)"}]

# intervention approach inclusion
intervention_approach_digital_technology = [{# Were any of the following involved in the intervention or approach?
                                             # Digital Technology
                                             5216718: "Yes",
                                             5216719: "No"}]

intervention_approach_parents_or_community_volunteers = [{# Were any of the following involved in the intervention or approach?
                                                          # Parents or community volunteers
                                                          5216720: "Yes",
                                                          5216721: "No"}]

intervention_time_output = [{# When did the intervention take place?  (Select ALL that apply)
                             5215580: "During regular school hours ",
                             5215581: "Before/after school",
                             5215582: "Evenings and/or weekends",
                             5215583: "Summer/ holiday period",
                             5215584: "Other (please specify)",
                             5215585: "Unclear/ not specified"}]

intervention_delivery_output = [{# Who was responsible for the teaching at the point of delivery? (Select ALL that apply)
                                 5215553: "Research staff",
                                 5215554: "Class teachers",
                                 5215555: "Teaching assistants",
                                 5215556: "Other school staff",
                                 5215557: "External teachers",
                                 5215558: "Parents/carers",
                                 5215559: "Lay persons/volunteers",
                                 5215560: "Peers",
                                 5215561: "Digital technology",
                                 5215562: "Unclear/not specified"}]

intervention_duration_output = [{# What was the duration of the intervention? (Please add to info box and specify units)
                                5215517: ''}]

intervention_frequency_output = [{# What was the frequency of the intervention?
                                  5215518: ''}]

intervention_session_length_output = [{# What is the length of intervention sessions? 
                                       5215519: ''}]

intervention_implementation_details = [{# Are implementation details and/or fidelity details provided?
                                        5215521: "Qualitative",
                                        5215522: "Quantitative",
                                        5215523: "No implementation details provided."}]

intervention_costs_reported = [{# Are the costs reported?
                                 5215528: "Yes (Please add details)",
                                 5215529: "No"}]

intervention_evaluation = [{# Who undertook the outcome evaluation?
                            5215533: "The developer",
                            5215532: "A different organization paid by developer",
                            5215531: "An organization commissioned independently to evaluate",
                            5215534: "Unclear/not stated",
                            5215578: "Is this an EEF evaluation?"}]

####################################
# SETTING & SAMPLE CHARACTERISTICS #
####################################

# NUMBER OF SCHOOLS
number_of_schools_intervention_output=[{# What is the number of schools involved in the intervention group(s)?
                                        5407111: ''}]
number_of_schools_control_output=[{# What is the number of schools involved in the control or comparison group?
                                   5407106: ''}]
number_of_schools_total_output=[{# What is the total number of schools involved?
                                 5407115: ''}]
number_of_schools_not_provided_output=[{# Not provided/ unclear / not applicable
                                         5407113: 'not_provided'}]

# NUMBER OF CLASSES
number_of_classes_intervention_output=[{# What is the total number of classes involved in the intervention group?
                                        5407105: ''}]
number_of_classes_control_output=[{# What is the total number of classes involved in the control or comparison group?
                                   5407107: ''}]
number_of_classes_total_output=[{# What is the total number of classes involved?
                                 5407153: ''}]
number_of_classes_not_provided_output=[{# Not provided/ unclear / not applicable
                                  5407114: 'not_provided'}]

# SAMPLE SIZE
sample_size_output=[{# What is the overall sample analysed?
                     5215428: ''}]

# GENDER SPLIT
gender_split_output=[{# Provide the percentage or number of female pupils in the study
                      5215644: ''}]

# STUDENT AGES
student_age_output=[{# What is the age of the students? (Select ALL that apply)
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
                    5513031: 'No information provided'}]

# PROPORTION LOW SES/FSM STUDENTS IN SAMPLE
proportion_low_fsm_output=[{# What is the proportion of low SES/FSM students in the sample?
                            5215454: ''}]
# PERCENTAGE LOW SES_FSM STUDENTS IN SAMPLE
percentage_low_fsm_output=[{# FSM or low SES student percentage
                            5376693: ''}]
# FURTHER SES/FSM INFORMATION IN SAMPLE
further_ses_fsm_info_output=[{# Further information about FSM or SES in the study sample.
                              5376694: ''}]
# NO SES/FSM INFO PROVIDED
no_ses_fsm_info_provided_output=[{# No SES/FSM information provided
                                 5366637: 'No SES/FSM Information Provided'}]

study_realism_output = [{# How realistic was the study?
                         5215255: 'High ecological validity',
                         5215256: 'Low ecological validity',
                         5215257: 'Unclear'}]

study_design_output = [{# What was the study design?
                        5406847: 'Individual RCT',
                        5406849: 'Cluster RCT',
                        5406851: 'Multisite RCT',
                        5406852: 'Prospective QED',
                        5406853: 'Interrupted time series QED',
                        5406854: 'Regression Discontinuity - not randomised',
                        5406856: 'Retrospective QED  ',
                        5406857: 'Regression Continuity  - naturally occurring',
                        5407075: 'Regression Discontinuity with randomisation'}]

edu_setting_output = [{# What is the educational setting (Select ALL that apply)
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

publication_type_output = [{# Section 1 What is the publication type?
                             5215227: 'Journal article',
                             5215228: 'Dissertation or thesis',
                             5215229: 'Technical report',
                             5215230: 'Book or book chapter',
                             5215231: 'Conference paper'}]

level_of_assignment_output = [{# What was the level of assignment?
                               5215244: 'Individual',
                               5215245: 'Class',
                               5215246: 'School - cluster',
                               5215247: 'School - multi-site',
                               5215248: 'Region or district',
                               5215249: 'Not provided/ not available'}]

participant_assignment_output = [{# How were participants assigned?
                                  5215251: 'Random (please specify)',
                                  5215252: 'Non-random, but matched',
                                  5215253: 'Non-random, not matched prior to treatment',
                                  5215565: 'Unclear',
                                  5641086: 'Not assigned - naturally occurring sample',
                                  5641087: 'Retrospective Quasi Experimental Design (QED)',
                                  5641088: 'Regression discontinuity'}]

student_gender =   [{# What is the gender of the students?
                    5215642: 'Female only',
                    5215643: 'Male only',
                    5215644: 'Mixed gender',
                    5513032: 'No information provided'}]

outcome_type_codes = [{# Outcome type (select all that apply)
                 7755570: "Toolkit primary outcome",
                 7755571: "Reading primary outcome",
                 7755572: "Writing and spelling primary outcome.",
                 7755573: "Mathematics primary outcome",
                 7755574: "Science primary outcome",
                 7755575: "Other outcome"}]

sample_output = [{# Sample (select one from this group)
                  5407009: 'Sample: All',
                  5407041: 'Sample: Exceptional',
                  5407006: 'Sample: High achievers',
                  5407008: 'Sample: Average',
                  5407007: 'Sample: Low achievers'}]

curriculum_subjects = [{# Curriculum subjects tested
                        5215543: "Literacy (first language)",
                        5215544: "Reading comprehension",
                        5215567: "Decoding/phonics",
                        5215568: "Spelling",
                        5215545: "Reading other",
                        5215546: "Speaking and listening/Oral language",
                        5215547: "Writing",
                        5215548: "Mathematics",
                        5215549: "Science",
                        5215550: "Social studies",
                        5215569: "Arts",
                        5215570: "Languages",
                        5215551: "Other curriculum test"}]

other_outcomes_output = [{# In addition to the primary educational attainment outcome, are there other outcomes reported?
                           5215572: "Yes",
                           5215573: "No"}]

which_other_outcomes_output = [{# If yes, which other outcomes are reported?
                                 5215575: 'Cognitive outcomes measured (Please specify)',
                                 5215576: 'Other types of student outcomes (Please specify)'}]

other_participants_output = [{# [part of the above 'which other outcomes output' list, but separated for its own column]]
                              5215577: 'Other participants (i.e. not students) outcomes (Please specify)'}]

randomisation_details = [{# Are details of randomisation provided?
                          5407117: "Yes",
                          5407119: "Not applicable",
                          5407118: "No/Unclear"}]

treatment_group = [{# Is there more than one treatment group?
                    5215240: "Yes (Please specify)",
                    5215241: "No",
                    5215242: "Not specified or N/A"}]












admin_strand_output = [{# Admin Strand
                       5023544: 'Arts participation',
                       5023545: 'Aspiration interventions',
                       5023546: 'Behaviour interventions',
                       5023547: 'Block scheduling',
                       5023550: 'Built environment',
                       5023551: 'Collaborative learning',
                       5023552: 'Digital technology',
                       5023554: 'Early years intervention',
                       5023553: 'Extending school time',
                       5023555: 'Feedback',
                       5023556: 'Homework',
                       5023557: 'Individualised instruction',
                       5023558: 'Learning styles',
                       5023559: 'Mastery learning',
                       5023560: 'Mentoring',
                       5023561: 'Metacognition and self-regulation',
                       5023562: 'One to one tuition',
                       5023563: 'Oral language interventions',
                       5023564: 'Outdoor adventure learning',
                       5023565: 'Parental engagement',
                       5023548: 'Peer tutoring',
                       5023566: 'Performance pay',
                       5023567: 'Phonics',
                       5023568: 'Reading comprehension strategies',
                       5023569: 'Reducing class size',
                       5023570: 'Repeating a year',
                       5023571: 'School uniform',
                       5023572: 'Setting or streaming',
                       5023549: 'Small group tuition',
                       5023573: 'Social and emotional learning',
                       5023574: 'Sports participation',
                       5023575: 'Summer schools',
                       5023576: 'Teaching assistants'}]

admin_strand_secondary = [{# other admin strand data
                           7291837: "Feedback"}]

toolkit_strand_codes =   [{#Toolkit strand(s) (select at least one Toolkit strand)
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
                    5407074: 'Toolkit: Teaching assistants'}]

test_type_output = [{# Test type (select one from this group)
                    5407028: 'Test type: Standardised test ',
                    5407029: 'Test type: Researcher developed test',
                    5407031: 'Test type: National test',
                    5407030: 'Test type: School-developed test',
                    5407032: 'Test type: International tests'}]

test_type_main = [{# What kind of tests were used? (Select ALL that apply)
                    5215537: 'Standardised test',
                    5215538: 'Researcher developed test',
                    5215539: 'School-developed test',
                    5215540: 'National test or examination',
                    5215541: 'International tests'}]

effect_size_type_output = [{# Effect size calculation (select one from this group)
                            5407010: 'Post-test unadjusted (select one from this group)',
                            5407011: 'Post-test adjusted for baseline attainment',
                            5407152: 'Post-test adjusted for baseline attainment AND clustering',
                            5407012: 'Pre-post gain'}]

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
                    5407036: 'Unclear (please add notes)'},
                    {# What is the number of schools involved in the study?
                    5407110: ''},
                    {# What is the number of schools involved in the intervention group(s)?
                    5407111: ''},
                    {# What is the number of schools involved in the control or comparison group?
                    5407106: ''},
                    {# What is the total number of schools involved?
                    5407115: ''},
                    {# Not provided/ unclear / not applicable
                    5407113: ''},
                    {# What is the number of classes involved?
                    5407112: ''},
                    {# What is the total number of classes involved in the intervention group?
                    5407105: ''},
                    {# What is the total number of classes involved in the control or comparison group?
                    5407107: ''},
                    {# What is the total number of classes involved?
                    5407153: ''},
                    {# Not provided/ unclear / not applicable
                    5407114: ''},
                    {# What is the overall sample analysed?
                    5215428: ''},
                    {# What is the proportion of low SES/FSM students in the sample?
                    5215454: ''},
                    {# FSM or low SES student percentage
                    5376693: ''},
                    {# Further information about FSM or SES in the study sample.
                    5376694: ''},
                    {# No SES/FSM information provided
                    5366637: ''},
                    {# What kind of tests were used? (Select ALL that apply)
                    5215536: ''},
                    {# Standardised test (Please specify)
                    5215537: ''},
                    {# Researcher developed test (Please add details)
                    5215538: ''},
                    {# School-developed test (Please add details)
                    5215539: ''},
                    {# National test or examination (Please specify)
                    5215540: ''},
                    {# International tests (Please specify)
                    5215541: ''},
                    {# Section 6 What kind of primary outcomes are reported?)
                    5215535: ''},
                    ################################################################
                    # STUDY OUTCOMES
                    ################################################################
                    {# Curriculum subjects tested (Select ALL that apply)
                    5215542: ''},
                    {# Curriculum Subjects
                    5215543: 'Literacy (first language',
                    5215544: 'Reading comprehension',
                    5215567: 'Decoding/phonics',
                    5215568: 'Spelling',
                    5215545: 'Reading other',
                    5215546: 'Speaking and listening/Oral language',
                    5215547: 'Writing',
                    5215548: 'Mathematics',
                    5215549: 'Science',
                    5215550: 'Social studies',
                    5215569: 'Arts',
                    5215570: 'Languages',
                    5215551: 'Other curriculum test'},
                    {# In addition to the primary educational attainment outcome, are there other outcomes reported?
                    5215572: 'Yes',
                    5215573: 'No'},
                    {# If yes, which other outcomes are reported?
                    5215575: 'Cognitive outcomes measured (Please specify)',
                    5215576: 'Other types of student outcomes (Please specify)',
                    5215577: 'Other participants (i.e. not students) outcomes (Please specify)'}]

countries =       [{# In which country/countries was the study carried out? (Select ALL that apply)
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
                    5215641: 'Uruguay'}]

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
                    5215641: 'Uruguay'},
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
                    5513033: 'No information provided'},
                    {# Curriculum Subjects
                    5215543: 'Literacy (first language)',
                    5215544: 'Reading comprehension',
                    5215567: 'Decoding/phonics',
                    5215568: 'Spelling',
                    5215545: 'Reading other',
                    5215546: 'Speaking and listening/Oral language',
                    5215547: 'Writing',
                    5215548: 'Mathematics',
                    5215549: 'Science',
                    5215550: 'Social studies',
                    5215569: 'Arts',
                    5215570: 'Languages',
                    5215551: 'Other curriculum test'}]