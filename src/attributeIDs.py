#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "Jonathan Reardon"

# START: FOR SOMEONE ELSE'S STUDY #

#  STUDY PLACE

location_info = [{
    # Section 3 Where did the study take place? (ID = 5215274) [Not selectable (no checkbox)]
    # Please add specific information about the location. (ID = 5215408) 
    5372848: "Specific to the location or place",
    5372849: "Information about the type of location",
    5372850: "No information provided",
}]

# NEW [SOURCE]

source_output = [{
    # Source where reference was retrieved. Linked to RIS files
    5114201: "From Toolkit single study",
    5114200: "From Toolkit meta-analysis",
    5114202: "From EY Toolkit",
    7288430: "From update 2020",
    9367797: "From Update 2021",
    10306451: "From update 2022",
    5114203: "From review:Teaching assistants, Aug 2018",
    5122767: "From review: Peer tutoring, July 2017",
    7681494: "From review: Homework, Dec 2019",
    7922819: "From review: School uniform 2020",
    8550794: "From review: Aspirations Interventions Dec, 2020",
    5412814: "EEF reports",
    5762939: "Multiple records from batch 1",
    6345222: "Multiple records from Batch 2",
    6903100: "Multiple records from batch 3",
    7689852: "Multiple records from batches 4 & 5",
    9475233: "Multiple records - Batch 7",
    10110631: "Multiple records - Batch 8",
    7689853: "Multiple records - Mixed batches",
    7392385: "Cross-referenced studies",
    10266185: "Network Graph Searches",
    10837253: "3ie studies",
    8112952: "Manual search (non systematic)",
    10848380: "From EEF Feedback review team",
}]

source_EEF_Report_options = [{
    5431305: "Strand specific - in Toolkit",
    5431306: "Effect size - in EEF meta-analysis",
    5431307: "Main data extraction",
    5431308: "Not codeable"
}]

# END: FOR SOMEONE ELSE'S STUDY #

# WEB MAPPING APP

study_loc = [{
    5372848: "",
}]

study_loc_type = [{
    5372849: "",
}]

##################
# STRAND SPECIFIC 
##################

# Early Years (EY) - Extra hours

time_organsised = [{
    # How was the additional time organised?
    10780471: "From no time to half-day attendance at nursery/ kindergarten (5 days per week)",
    10780472: "From half-day to full day nursery/ kindergarten (5 days per week)",
    10780473: "Additional hours each day (but less than half a day extra each day)",
    10780474: "Additional days each week (e.g. from 3 days to 5 days)",
    10780475: "Additional weeks in the year (e.g. from 40 weeks to 45 weeks)",
    10780476: "Other (please specify)",
}]

""" # nested within time_organised (above), check 'other' input
time_organised_other = [{
    10780476: "",
}] """

addit_time_struct = [{
    10780478: "Same activities",
    10780480: "Different activities",
    10780481: "Not specified/ unclear",
}]

# Early Years (EY) - Early starting age

ey_esa_prev_starting_age = [{
    # What was the previous starting age?
    11037258:'3',
    11037259:'4',
    11037260:'5',
    11037261:'6',
    11037262:'Not specified / unclear',
}]

ey_esa_new_starting_age = [{
    # What is the new starting age?
    11037263:'2',
    11037264:'3',
    11037265:'4',
    11037266:'5',
    11037267:'Not specified / unclear',
}]

ey_esa_addit_time_f_pt = [{
    # Was the additional time in Nursery or Kindergarten full or part time?
    11037268:'Full time',
    11037270:'Part time',
    11037271:'Other (please specify)',
    11037272:'Not specified/ Unclear',
}]

""" ey_esa_addit_time_other = {
    # nested 'other' option from 'addit_time' (above)
    11037271: '',
} """

ey_esa_addit_time_struct = [{
    # Was additional time in Nursery or Kindergarten structured the in the same way as previously or different from the usual activities?
    11037273:'Same activities',
    11037274:'Different activities',
    11037275:'Not specified/ Unclear',
}]

ey_esa_earlier_child_addit_time = [{
    # What was the duration of the additional time experienced by children who started earlier (in months)?
    11037276:'Six months or half an academic year',
    11037277:'One full academic year (12 months)',
    11037278:'Two full academic years (24 months)',
    11037279:'Other (Please add a numeric value only, in whole number of months)',
}]

ey_esa_earlier_child_addit_time_other = [{
    # nested within ey_esa_earlier_child_addit_time (above), check 'other' input
    11037279:'',
}]

ey_esa_setting_type = [{
    # What type of early years setting did the children attend?
    11085238:'Nursery school or class (state funded)',
    11085239:'Private nursery class or school',
    11085241:'Reception class (state funded)',
    11085240:'Private Reception class or school',
    11085242: 'Other (please specify)',
    11085243: 'Unclear/ not specified',
}]

# Early Years (EY) - Play-based learning

kind_of_play = [{
    # What kind of play is involved in the study?
    10780484: "Free play",
    10780485: "Guided or facilitated play",
    10780486: "Socio-dramatic or pretend play",
    10780487: "Outdoor play",
    10780488: "Games or other structured or directed play activities",
    10780489: "Other (please specify)",
}]

who_involved = [{
    # Who was involved in the play activities?
    10780491: "Early years children only",
    10780492: "Children and adult staff",
    10780493: "Children and parents",
    10780494: "Other (please specify)",
}]

play_focus = [{
    # What was the main focus for the play activities?
    10780496: "Language/ literacy",
    10780497: "Mathematics",
    10780498: "Science/ exploring the natural world",
    10780499: "Physical development (gross or fine motor skills)",
    10780500: "Social/ emotional development",
}]

# Early Literacy Approaches

ela_literacy_activities = [{
    # What literacy activities were included in the programme or approach?
    10340022: "Oral or spoken language",
    10340023: "Reading",
    10340024: "Writing",
    10340025: "Unclear/ not specified",
}]

ela_comprehensive = [{
    # How comprehensive was the programme or approach?
    10340027: "A complete literacy and language curriculum",
    10340028: "Supplementary literacy activities only",
    10340029:  "Unclear/ not specified",
}]

ela_prog_desc = [{
    # Which of the following activities are mentioned in the description of the programme or approach?
    10340031: "Phonics, phonemic/phonological awareness or other sound to symbol/ symbol to sound correspondence",
    10340032: "Letter recognition, letter name knowledge or alphabet skills",
    10340033: "Rhyme (or rime) activities",
    10340034: "Whole language instruction",
    10340035: "Play or play-based learning, dramatic play",
    10340036: "Small group activities or instruction",
    10340037: "One to one interaction or instruction",
    10340038: "Parental involvement, family literacy",
}]

# Early Numeracy Approaches

ena_maths_included = [{
    # What mathematics was included in the programme or approach? (Please select one option and highlight the relevant text in the study report.)
    10262420: "Number and operations/ numeracy only",
    10262421: "Broad mathematics curriculum",
    10262422: "Unclear/ not specified",
}]

ena_prog_comp = [{
    # How comprehensive was the programme or approach?
    10262424: "A complete mathematics curriculum",
    10262425: "Supplementary mathematics activities only",
    10262426: "Unclear/ not specified",
}]

ena_prog_activities = [{
    # Which of the following activities are mentioned in the description of the programme or approach?
    10262429: "Guided interaction",
    10262430: "Direct teaching and/or instruction",
    10262431: "Feedback",
    10262432: "Mastery/ fluency",
    10262434: "Practice/ reinforcement",
    10262435: "Investigations/ exploration/ inquiry/discovery",
    10262436: "Concrete materials/ manipulatives",
    10262437: "Digital technology/ computers",
    10262438: "Games",
    10262440: "Parents/home activities",
    10262441: "None of the above mentioned",
    10266213: "Not specified / no details",
}]

# WITHIN CLASS GROUPING

wcg_dir_grouping_change_output = [{
    #  "What is the direction of the grouping change investigated in the research? "
    9093097: "Heterogeneous to homogeneous",
    9093100: "Homogeneous groups to heterogeneous",
    9093102: "Not specified/ unclear",
}]

wcg_curr_taught_attain_grp_output = [{
    # "Which areas of the curriculum are taught in attainment groups within the class? "
    9093104: "Literacy",
    9093105: "Mathematics",
    9093106: "Other (please specify)",
    9093107: "Not specified/ Unclear",
}]

wcg_pupils_affected_by_wcg_output = [{
    # "Which pupils in the classes are affected by the within class grouping"
    9093109: "All pupils",
    9093110: "Low attainers only",
    9093111: "Gifted and talented only",
    9093112: "Other (please specify)",
}]

wcg_attain_grouping_level = [{
    # "How many grouping levels are there for attainment?",
    9096737: "4 groups",
    9096738: "3 groups",
    9096739: "2 groups",
    9096740: "Other (please specify)",
    9096741: "Not specified/ Unclear",
}]

wcg_follow_same_curr = [{
    # Do all pupils follow the same curriculum in the different attainment groups?
    9096743: "No - different curriculum",
    9096745: "Yes - same curriculum",
    9096746: "Unclear/ Not specified",
}]

wcg_approach_name = [{
    # "Does the approach have a specific name or description?",
    9096748: "Yes (please specify)",
    9096749: "No",
}]

wcg_pupil_assignment = [{
    # "How are pupils assigned to groups?",
    9096751: "Using test results (please add details)",
    9096752: "By the teacher(s)",
    9096753: "Other (please specify)",
    9096754: "Not specified/ Unclear",
}]

# SETTING OR STREAMING

sets_dir_grouping_change = [{
    # What is the direction of the grouping change investigated? (Select one)
    6177366: "Heterogeneous to homogeneous",
    6177367: "Homogeneous groups to heterogeneous",
    6177368: "Not specified/ unclear",
}]

""" sets_dir_grouping_type_within_attain = [{
    # "Within class attainment-based grouping ",
    6177369: "Within class attainment-based grouping",
}] """

""" # nested within from dir_grouping_type
sets_curr_taught_in_attain_grp = [{
    # Which areas of the curriculum are taught in attainment groups within the class?
    6177376: "Literacy",
    6177377: "Mathematics",
    6177378: "Other (please specify)",
    6177383: "Not specified/ Unclear",
}] """

sets_dir_grouping_type_regroup = [{
    # What is the direction of the grouping change investigated? (Select one)
    6177365: "Re-grouping or partial setting between classes",
}]

# nested within from dir_grouping_type_regroup
sets_curr_taught_in_regroup = [{
    # "Which areas of the curriculum are taught in the re-grouped classes?
    6177380: "Literacy",
    6177381: "Mathematics",
    6177382: "Other (please specify)",
    6177379: "Not specified/ Unclear",
}]

sets_dir_grouping_stream = [{
    # Where more homogeneous classes in separate classrooms are usually or permanently organized on the basis of the pupils attainment
    6177373: "Streaming or tracking",
}]

sets_dir_grouping_gifted = [{
    # Where more homogeneous classes in separate classrooms are usually or permanently organized on the basis of the pupils attainment
    6177371: "Gifted and talented",
}]

sets_school_groupings = [{
    # "What are the school or academic year groupings of pupils involved?",
    6177354: "Same age only",
    6177370: "Cross age grouping",
    6177372: "Promotion (younger with older)",
}]

sets_attain_grouping_level = [{
    # "How many grouping levels are there for attainment?",
    6177351: "4 groups",
    6177352: "3 groups",
    6177353: "2 groups",
    6177357: "Other (please specify)",
    6177355: "Not specified/ Unclear",
}]

sets_follow_same_curr = [{
    # Do all pupils follow the same curriculum in the different attainment groups?
    6177350: "No - different curriculum",
    6177362: "Yes - same curriculum",
    6177363: "Unclear/ Not specified",
}]

sets_approach_name = [{
    # "Does the approach have a specific name or description?",
    6177358: "Yes (please specify)",
    6177364: "No",
}]

sets_pupil_assignment = [{
    # "How are pupils assigned to groups?",
    6177359: "Using test results (please add details)",
    6177360: "By the teacher(s)",
    6177361: "Other (please specify)",
    6177356: "Not specified/ Unclear",
}]


# REDUCING CLASS SIZE

redc_avg_small_class_size_output = [{
    # "What is the typical or average size of the small classes?
    # highlighted text and info for this option
    7094722: "",
}]

redc_avg_large_class_size_output = [{
    # "What is the typical or average size of the large classes?
    # highlighted text and info for this option
    7094723: "",
}]

redc_small_class_teacher_number_output = [{
    # "How many teachers were assigned to the smaller classes?"
    7094735: "1",
    7094736: "2",
    7094737: "More than 2",
}]

redc_large_class_teacher_number_output = [{
    # "How many teachers were assigned to the larger classes?"
    7094732: "1",
    7094739: "2",
    7094740: "More than 2",
}]

redc_large_class_adaption_output = [{
    # "Were there any adaptions made to support the larger classes (such as additional teaching assistants or other support)?
    7094738: "Yes",
    7094734: "No",
}]

redc_reduc_for_limited_num_sub_output = [{
    # "Was the class size reduction implemented for a limited number of subjects (e.g. reading and maths)?
    7094729: "Yes",
    7094733: "No",
}]

redc_impl_for_all_or_most_output = [{
    # "Was the class size reduction implemented for all or most lessons across the curriculum?"
    7094730: "Yes",
    7094731: "No",
}]

# METACOGNITION AND SELF-REGULATION

msr_knowl_type_output = [{
    # "Type of metacognitive knowledge (select all that apply)
    5586777: "Knowledge of learning strategies/ techniques",
    5586778: "Knowledge of when to use particular approaches",
    5586780: "Knowledge of self",
}]

msr_task_stage_output = [{
    # "Metacognitive task stage (select all that apply)"
    5586779: "Planning",
    5586776: "Monitoring",
    5586785: "Evaluating",
}]

msr_strategy_type_output = [{
    # "Type of metacognitive strategy (select all that apply)"
    5586768: "General learning strategies",
    5586781: "Reading and/or comprehension strategies",
    5586782: "Problem-solving strategies",
    5586783: "Recall or metamemory strategies",
    5586784: "Critical thinking, reasoning and argumentation strategies",
}]

msr_self_reg_mot_aspects_output = [{
    # "Self-regulation and motivational aspects (select all that apply)"
    5586769: "Personal capability/ self efficacy",
    5586770: "Task value/ success",
    5586773: "Managing motivation and effort",
    5586775: "Mastery approaches/ goal orientation",
}]

msr_teaching_approach_output = [{
    # "Teaching approach (select ONE of the first 2)"
    5586771: "Individual",
    5586774: "Collaborative",
    5586772: "With digital technology",
}]

msr_digit_tech = [{
    # "With digital technology", nested from msr_teaching_approach_output option
    5589253: "Yes",
    5589254: "No",
}]

# LEARNING STYLES

ls_type_output = [{
    # "Type of learning styles model (select all that apply)"
    5697939: "Dunn & Dunn Learning Style model",
    5697940: "Gardner’s Theory of Multiple Intelligences",
    5697941: "Gregorc’s Mind Styles Model",
    5697937: "Kolb learning cycle (also 4MAT, Honey & Mumford)",
    5697942: "Myers Briggs Type Indicator",
    5697943: "Perceptual learning style (Visual, Auditory, Kinaesthetic/ VAK/ VAKT)",
    5697944: "Riding’s Cognitive Styles Analysis",
    5697945: "Witkin’s field dependent/independent cognitive style",
    5697946: "Other (please specify)",
}]

ls_design_approach_output = [{
    # "Design approach (select all that apply)"
    5697934: "Learning style activities matched to learner preference",
    5697935: "Random allocation of task to learner (no match)",
    5697936: "Mismatch of learner and style (deliberate mismatch)",
    5697938: "Learner style matched to teacher style",
}]

# REPEATING A YEAR

ry_ret_stu_identify_output = [{
    # "How are retained students idenftified for the research?"
    6198391: "A specific year group/groups or grade/grades for retention are identified in the research",
    6198392: "Mixed year groups or grades",
}]

ry_ret_stu_age_output = [{
    # "How old were the pupils when they were retained? (Mark all that apply)"
    6198394: "3 – 7 years",
    6208441: "8- 11 years",
    6208442: "12 years or older",
    6208443: "Not clear/ unspecified (please add any details)",
}]

ry_ret_basis_output = [{
    # On what basis were students selected for retention by the schools?
    6208445: "A formal test or assessment",
    6208446: "Teacher assessment, teacher judgement or grades",
    6208447: "Other (please specify)",
}]

ry_impact_measure_delay_output = [{
    # How long after retention is the impact measured?
    6208449: "1 year",
    6208450: "2 years",
    6208451: "3 years",
    6208452: "4 years",
    6208453: "5 years",
    6208454: "6 years",
    6208455: "7 years",
    6208456: "8 years",
    6208457: "Other (Please specify)",
    6208458: "Multiple (mixed sample)",
}]

ry_stu_ret_number_output = [{
    # How many times were students retained?
    6208460: "Once",
    6208461: "Twice",
    6208462: "At least once, but unspecified",
    6208463: "Other (please specify)",
}]

ry_ret_stud_compared_with_output = [{
    # Who are retained students being compared with?
    6208465: "Promoted 'regular' students",
    6208466: "Promoted similar students (low attaining or 'underachieving' students)",
    6208467: "Promoted matched students (where specific characteristics are used to identify a specific match)",
    6208468: "Grade equivalent scores",
    6208469: "Other (Please specify)",
}]

ry_prom_count_characteristics_output = [{
    # "If retained students were matched with a promoted counterpart which characteristics are used for the matching ? (Please select all that apply)"
    6208471: "Achievement test score",
    6208472: "Age",
    6208473: "Attendance",
    6208474: "Ethnicity",
    6208475: "Free school meals (FSM) Reduced price/ free lunch",
    6208476: "Gender",
    6208477: "IQ/ Cognitive tests",
    6208478: "Language status (e.g. ESL, E2L)",
    6208479: "Socio economic status (SES) including parental income",
}]

ry_comparison = [{
    # "Comparison"
    6208969: "Same age",
    6208970: "Same grade",
}]

ry_comp_grp_school = [{
    # "Are the comparison group from the same school as the retained students or a different school (or somewhere else)?
    6208972: "Same school",
    6208973: "Different school",
    6208974: "Grade equivalent scores (population comparison)",
    6208975: "Other (please specify)",
    6208976: "Unclear/ not provided",
}]

# OUTDOOR ADVENTURE LEARNING

oal_prog_type_output = [{
    # What type of programme is being evaluated? (Please mark one only)
    6650703: "Expedition based",
    6650705: "Basecamp",
    6650706: "Residential",
    6650707: "Day visits/ trips",
    6650710: "Other (Please specify)",
    6650709: "Unclear/ not specified",
}]

oal_Activities_output = [{
    # "What kind of activities are involved? (Mark all that apply)"
    6650687: "Survival skills",
    6650698: "Rope skills/ climbing",
    6650695: "Camping",
    6650699: "Hiking",
    6650700: "Sailing",
    6650702: "Canoeing",
    6650704: "Skiing/ Winter climbing",
    6650708: "Other (Please add details)",
    6650711: "Unclear/ not specified",
}]

oal_aims_output = [{
    # "What are the broad aims of the programme? (Please mark one only)"
    6650701: "Therapeutic",
    6650688: "Educational/ developmental ",
    6650689: "Recreational",
    6650690: "Other (Please add details)",
    6650691: "Unclear/ not specified",
}]

oal_pop_descr_output = [{
    # "How is the population described? (Please mark one only)"
    6650692: "Normal",
    6650693: "Suffered abuse",
    6650694: "Problematic behaviours",
    6650696: "Other (Please add details)",
    6650697: "Unclear/ not specified",
}]

# SCHOOL UNIFORM

su_dress_require_details_output = [{
    # "Are there any details of the uniform or dress code policy in terms of what clothes are required or expected?"
    7921749: "Yes",
    7921751: "No",
}]

su_policy_output = [{
    # "Was the school uniform policy mandatory or voluntary?"
    7921750: "Mandatory",
    7921748: "Voluntary",
    7921754: "Unclear/ No information",
}]

su_cost_info_output = [{
    # "Is there any information about the cost of the uniform to parents?"
    7921747: "Yes",
    7921755: "No",
}]

su_enforce_policy_info_output = [{
    # "Is there any information about how the school uniform policy was enforced?"
    7921752: "Yes",
    7921753: "No",
}]

su_attend_impact_output = [{
    # "Did the school uniform policy have an impact on attendance?"
    7921741: "Yes",
    7921744: "No",
    7921745: "Not mentioned",
}]

su_behav_impact_output = [{
    # "Did the school uniform policy have an impact on student behavior (e.g. suspensions, exclusions)?"
    7921742: "Yes",
    7921746: "No",
    7921743: "Not mentioned",
}]

# INDIVIDUALISED INSTRUCTION

ii_approach_output = [{
    # "Which of the following were involved in the individualized approach? (Mark all that apply and highlight the relevant text where possible)"
    6650769: "Individual work",
    6650770: "Individual pace",
    6650771: "Individual feedback",
}]

ii_also_included_output = [{
    # "Are any of the following included in the approach? (Mark all that apply and highlight the relevant text where possible)
    6650764: "Collaboration",
    6650765: "Peer feedback",
    6650766: "Digital technology",
    6650767: "Pre-testing of content",
    6650773: "Testing for mastery",
    6650774: "Self-checking/ self-marking",
}]

ii_also_mentioned_output = [{
    # "Are any of the following mentioned as being involved in the approach? (Mark all that apply and highlight the relevant text where possible)"
    6650772: "Mastery learning",
    6650768: "Personalized System of Instruction (Keller)",
    6650758: "Programmed instruction",
    6650759: "Individually Prescribed Instruction (IPI)",
    6650760: "Program for Learning in Accordance with Needs (PLAN)",
    6650761: "Computer-assisted instruction",
    6650762: "Audio-tutorial instruction",
    6650763: "Intelligent tutoring",
}]

# PHYSICAL ACTIVITY

pha_when_output = [{
    # "When did the physical activity take place?
    8301857: "During the school day",
    8301858: "Before or after school",
    8301859: "During the holidays",
    8301860: "Other (please specify)",
}]

pha_lessons_included_output = [{
    # "Which lessons included the physical activity?
    8302336: "Timetabled physical education (PE) lessons",
    8302401: "Additional lessons",
    8302402: "Cross-curricular (i.e. included in other lessons)",
    8302404: "Break time or lunchtime (during the school day)",
    8302405: "Other (please specify)",
}]

pha_activity_type_output = [{
    # "What type of physical activity was involved?
    8302413: "Increased activity (e.g. movement during the day tracked with an accelerometer)",
    8302414: "Exercises (e.g. aerobics, calisthenics)",
    8302415: "Dance and/or rhythmic movement",
    8302416: "Weights or resistance training",
    8302417: "Sports/games (e.g. football, playground games)",
    8302418: "Other (please specify)",
}]

pha_exercise_level_output = [{
    # "What was the level of exercise?
    8302420: "Very light or Light (e.g. walking/ little effect on breathing)",
    8302421: "Moderate (e.g. jogging/ breathing harder)",
    8302422: "Hard or Very hard (sprinting/ getting out of breath)",
    8302423: "Not specified/ unclear",
}]

# PERFORMANCE PAY

pp_incentive_criteria_output = [{
    # What were the criteria for the reward or incentive? (Please select all that apply)
    8249989: "Teacher performance (e.g. observation or portfolio based",
    8249990: "Pupil performance (e.g. test or examination results)",
    8249991: "Not specified/unclear",
    8249992: "Other",
}]

pp_reward_recipient_output = [{
    # "Who received the reward or incentive?"
    8249994: "Individual reward to the teacher",
    8249995: "Group or team reward to teachers",
    8249996: "Headteacher or senior management",
    8249997: "Other",
}]

pp_incentive_timing_output = [{
    # "What was the timing of the incentive?"
    8249999: "Payment by results (i.e. a retrospective reward or payment contingent on test scores)",
    8250000: "Payment up front",
    8250001: "Other",
}]

pp_incentive_type_output = [{
    # "What type of incentive or reward was offered?"
    8250003: "A one off payment",
    8250004: "An increase in salary",
    8250006: "Other",
}]

pp_incentive_amount_output = [{
    # "What was the amount of the incentive or increase in salary?
    8250007: "",
}]

pp_teacher_eval_period_output = [{
    # "Over what time period was teacher performance evaluated?"
    8250009: "Less than one school year",
    8250010: "One school year",
    8250011: "More than one school year",
}]

# ARTS PARTICIPATION

ap_focus_output = [{
    # What was the focus of the Arts participation programme or approach?
    6855349: "Multi-component or integrated programme",
    6855357: "Music",
    6855352: "Dance",
    6855353: "Drama",
    6855355: "Visual or other Fine arts",
    6855350: "Other (Please specify)",
}]

ap_who_output = [{
    # "Who was involved in the delivery or teaching of the intervention or approach?
    6855345: "Classroom teachers",
    6855351: "Other staff in the school(s)",
    6855354: "Outside experts or specialists",
    6855356: "Other (please specify)",
}]

ap_where_output = [{
    # "Where did the activities mainly take place?
    6855346: "School",
    6855347: "Specialist arts venue",
    6855348: "Other (Please specify)",
}]

# PARENTAL ENGAGEMENT

pe_involved_output = [{
    # "Who was involved? (Select one)"
    6650669: "Parents (unspecified)",
    6650670: "All or both parents",
    6650671: "Mothers only",
    6650672: "Fathers only",
    6650673: "Wider family involvement",
    6650674: "Other (Please specify)",
}]

pe_activity_location_output = [{
    # "Where did the activities mainly take place (Please select only one if possible)"
    6650675: "Home",
    6650677: "School",
    6650679: "Community centre or other local setting",
    6650680: "Other (Please specify)",
}]

pe_prog_training_output = [{
    # "Did the programme of approach involve training for the intervention or approach?"
    6650655: "Yes",
    6650656: "No",
    6650681: "Unclear/ not specified",
}]

pe_prog_support_output = [{
    # "Did the programme or approach involve ongoing support?"
    6650676: "Yes",
    6650678: "No",
    6650668: "Unclear/ not specified",
}]

pe_children_output = [{
    # "Whose children did the parents work with?"
    6650657: "Their own children only",
    6650660: "Their own children and other children",
    6650667: "Other children only (not their own)",
    6650663: "Unclear / not specified",
}]

pe_focus_output = [{
    # "What was the focus of the engagement?
    6650662: "Reading/ early literacy",
    6650664: "Homework",
    6650658: "Improving children's social skills or behaviour",
    6650665: "Parenting skills (being a better parent)",
    6650666: "Parents’ personal skills (e.g. literacy, digital technology, employability)",
    6650661: "General volunteering",
    6650659: "Other",
}]

# MASTERY LEARNING

ml_theor_output = [{
    # "Which educational theorists or approaches to mastery are mentioned as underpinning the approach in the research (mark all that apply)?",
    6469547: "Ark’s Mathematics Mastery and/or Helen Drury's Mastering Mathematics",
    6469548: "Benjamin Bloom and/ or Bloom’s Learning for Mastery",
    6469549: "James H. Block and/or L.W. Anderson and/or Group-Based Learning for Mastery",
    6469550: "John B. Carroll and/ or Carroll’s Model of School Learning",
    6469551: "Siegfried Engelmann and/or Wesley C. Becker and/or Direct Instruction and/or DISTAR",
    6469552: "Fred S. Keller and or the Keller Plan and/or Keller’s Personalized System of Instruction (PSI)",
    6469553: "Shanghai maths and/or Bianshi theory",
    6469554: "Singapore maths",
    6469555: "B. F. Skinner and/or Programmed Instruction",
    6469556: "Carleton Washburne and/or the Winnetka plan",
    6469559: "Other (please add notes)",
    6469557: "None mentioned",
}]

ml_age_group_output = [{
    # "How are the learners grouped for mastery learning in terms of age?
    6469544: "Same age (i.e. pupils from the same school year)",
    6469545: "Mixed age (i.e. pupils from different school years)",
    6469546: "Unclear/ confusing",
}]

ml_ability_group_output = [{
    # "How are the learners grouped for mastery learning in terms of ability?
    6469535: "Mixed attainment / heterogeneous grouping",
    6469543: "Grouping by attainment or ability / homogeneous grouping",
}]

ml_if_attain_what_grouping_type_output = [{
    # "If grouped by attainment or ability, what was the type of grouping?
    6469560: "High attainers/ ability",
    6469561: "Average attainment/ ability",
    6469562: "Low attainment/ ability",
    6469563: "Special educational needs (SEN/ SEND) (please add details).",
    6469564: "Unclear/ confusing",
}]

ml_goal_level = [{
    # At what level are the mastery goals set?
    6469531: "For individuals",
    6469532: "Collaborative groups",
    6469540: "Unclear/ confusing (Please add details.)",
}]

ml_assess_detail = [{
    # "Are there details about the testing procedures to assess mastery?"
    6469539: "Yes (please add details)",
    6469542: "No/ unclear",
}]

ml_fb_detail_prov = [{
    # "Are details of the feedback and corrective procedures provided?",
    6469537: "Yes (please add details or highlight in the text)",
    6469538: "No/ unclear",
}]

ml_mastery_level = [{
    # "What level of mastery is set or specified?"
    6469541: "90% or above",
    6469533: "80% (between 80% and 89%)",
    6469536: "Other (please specify)",
    6469534: "None / Not specified / Unclear",
}]

# HOMEWORK

hw_dur_info_output = [{
    # "Is there information about how long students spent on homework?"
    7921720: "Yes (Please highlight the relevant text in the study report)",
    7921722: "No",
}]

hw_total_time = [{
    # If yes, what was the total time in hours per week?
    7921708: "",
}]

hw_who_involved_output = [{
    # Who was involved in the homework programme? (Select all that apply.)
    7921721: "Individual students working on their own",
    7921719: "Students working together (collaborative homework)",
    7921726: "Parents or other family members.",
}]

hw_if_parents_describe_role_output = [{
    # "If parents or other family members were involved, please describe their role. (Select all that apply and highlight the relevant text in the study report.)",
    7921723: "Direct help or involvement with the homework",
    7921724: "Encouragement and general support",
    7921725: "Monitoring/ checking completion",
}]

hw_completed_where_output = [{
    # "Where was the homework completed?
    7921714: "At home",
    7921713: "At school",
    7921717: "In another setting",
    7921727: "Not especified / Unclear",
}]

hw_mark_method_info_output = [{
    # "Is there information about how the homework was marked or responded to?"
    7921715: "Yes (Please highlight the relevant text in the study report)",
    7921718: "No",
    7921716: "Unclear",
}]

# ORAL LANGUAGE

ol_focus = [{
    # What is the oral language focus in teaching? (Choose one)
    5516024: "Listening (language reception)",
    5516025: "Speaking (language production)",
    5516026: "Both speaking and listening (interaction)",
}]

ol_target= [{
    # What is the explicit target of the oral language development? (Choose best overall)
    5516023: "General talk and articulation",
    5516027: "Vocabulary development",
    5516029: "Subject knowledge or information acquisition",
    5516030: "Improved comprehension or understanding (Select one)",
    5516022: "Improved writing outcomes",
    5516019: "Improved thinking and reasoning (dialogic)",
    5516014: "Other/ Unclear (please add details to info box)",
}]

# nested option for 'improved comprehension" ^
ol_imp_comp_type = [{
    # Improved comprehension or understanding (Select one)
    5516031: "Listening comprehension",
    5516032: "Reading comprehension",
}]

ol_activity_invol = [{
    # Who is involved in the oral language activities? (Check all that apply)
    5516015: "Individual learner (e.g. self talk)",
    5516016: "Pupils (same age)",
    5516017: "Pupils (mixed ages)",
    5516018: "Teacher or other education professional",
    5516020: "Volunteer",
    5516021: "Parent, carer or other relative",
    5516028: "Other/ not clear",
}]

# COLLABORATIVE LEARNING

cl_approach_spec_output = [{
    # Are any of these researchers or approaches specified in the definition or explanation of the collaborative learning approach?
    6963923: "Aronson: JIGSAW groups or Home/Expert groups",
    6963934: "Slavin: Student Team Learning (STL )or Student-Teams-Achievement Divisions (STAD) or Team Games Tournament (TGT) or Team Assisted Individualisation (TAI)",
    6963932: "Slavin & Madden: Cooperative Integrated Reading and Composition (CIRC)",
    6963948: "Sharan and Sharan: Group investigation model",
    6963942: "Mercer and Wegerif: Thinking together",
    6963946: "Other (please specify)",
    6963940: "No research basis mentioned",
}]

cl_group_size_output = [{
    # What was the size of the groups that the pupils worked in?
    6963938: "2",
    6963939: "3",
    6963941: "4",
    6963943: "5",
    6963944: "6",
    6963945: "7",
    6963947: "8",
    6963954: "More than 8",
}]

cl_collab_kind_output = [{
    # What kind of collaboration occurred during the tasks or activities?
    6963949: "Peer collaboration on the task or during the activities, AND with a joint collaborative outcome AND with the same groups throughout",
    6963952: "Peer collaboration during the task or process of the activity AND with a joint collaborative outcome BUT with different collaborative groups at different stages of the activity",
    6963953: "Peer collaboration during the tasks or activities, BUT with an individual outcome",
    6963955: "No peer collaboration on during the process of the task or activity AND with a co-operative outcome",
}]

cl_stud_collab_output = [{
    # Was there any student or peer collaboration in the assessment or evaluation of the task after it was completed?
    6963956: "Yes (Please highlight the relevant text.)",
    6963950: "No",
}]

cl_extr_rewards_output = [{
    # Were there Extrinsic rewards for the outcome?
    6963951: "Yes (Please highlight the relevant text.)",
    6963937: "No",
}]

cl_if_yes_rewards_output = [{
    # If yes, were these rewards..
    6963921: "Individual rewards for group performance?  (Please highlight the relevant text.)",
    6963922: "Individual rewards for individual performance? (Please highlight the relevant text.)",
    6963926: "Group rewards for group performance? (Please highlight the relevant text.)",
    6963924: "Group rewards for individual performance? (Please highlight the relevant text.)",
    6963927: "Other (Please highlight the relevant text.)",
}]

cl_comp_elem_output = [{
    # "Was there a competitive element?"
    6963920: "Yes (Please highlight the relevant text.)",
    6963933: "No",
}]

cl_teacher_role_info_output = [{
    # Is there information about the teacher’s role during the collaborative activities?
    6963929: "Yes (Please highlight the relevant text.)",
    6963935: "No",
}]

cl_pupil_feedback_output = [{
    # Were pupils given feedback about their collaborative skills?
    6963928: "Yes (Please highlight the relevant text.)",
    6963930: "No",
}]

cl_pupil_feedback_who_output = [{
    # If yes, who provided the feedback?
    6963931: "Teacher",
    6963925: "Students",
    6963936: "Other (Please highlight the relevant text.)",
}]













































# SUMMER SCHOOL

ss_aim_output = [{
    # "Purpose or aims (select all that apply)"
    5633840: "Catch-up or remediation",
    5633843: "Enrichment or compensation for disadvantage",
    5633829: "School transition",
    5633835: "Acceleration and/of gifted and talented",
    5633833: "Not specified or unclear",
}]

# individual columns extraction for ss_aim_output
ss_aim_output_catch_up = [{
    5633840: "Catch-up or remediation",
}]

ss_aim_output_enrich = [{
   5633843: "Enrichment or compensation for disadvantage",
}]

ss_aim_output_school_trans = [{
    5633829: "School transition",
}]

ss_aim_output_gifted= [{
    5633835: "Acceleration and/of gifted and talented",
}]

ss_aim_output_unclear= [{
    5633833: "Not specified or unclear",
}]
#^^end of individual column extraction for ss_Aim_output^^

ss_pupil_part_output = [{
    # "Participation by pupils (select one)",
    5633831: "Voluntary or optional",
    5633834: "Compulsory or required",
    5633836: "Not mentioned",
}]

ss_resid_comp_output = [{
    # Did the summer school involve overnight stays or had a residential component?
    5633830: "Yes",
    5633832: "No",
    5633837: "Unsure",
}]

ss_group_size_output = [{
    # Class or group size (select all that apply)
    5633839: "One-to-one or individual teaching",
    5633842: "Small group (2 - 5 pupils)",
    5633844: "Large group (6-15 pupils)",
    5633845: "Class size (16+)",
}]

ss_activity_focus_output = [{
    # Activity focus (select best option)
    5633819: "Adademic only",
    5633820: "Academic and sports",
    5633828: "Academic and cultural or artistic",
    5633841: "Academic and vocational skills",
    5633838: "Academic and social",
}]

ss_staff_kind_output = [{
    # "Indicate what kind of staff were involved in the teaching of any academic content
    5633815: "Qualified teachers",
    5633816: "Teaching assistants/ paraprofessionals",
    5633817: "Young people/adults (paid)",
    5633821: "Volunteers (unpaid)",
    5633825: "Other (please specify)",
}]

ss_parent_invol = [{
    # Parental involvement (select one
    5633824: "Yes",
    5633827: "No / not mentioned",
}]

ss_digit_tech = [{
    # Digital technology (select one)
    5633822: "Yes",
    5633823: "No / not mentioned",
}]

ss_attendance = [{
    # "Attendance (select one)"
    5633818: "Yes",
    5633826: "No / not mentioned",
}]


# PHONICS

ph_targ_pop_output = [{
    # "What is the target population for the phonics approach? (Please select one)"
    6886306: "Universal",
    6886307: "Low attaining",
    6886308: "Children identified as having special or particular needs",
}]

ph_constit_part_approach_output = [{
    # Which of the following are mentioned as constituent parts of the phonics approach? (Please select all that apply)
    6886297: "Synthetic phonics",
    6886295: "Systematic phonics",
    6886298: "Analytic phonics",
    6886300: "Analogy phonics or analogy-based phonics",
    6886301: "Embedded phonics",
    6886302: "Phonemic awareness",
    6886304: "Phonological awareness",
    6886305: "Onset - rime",
    6886310: "Syllable instruction",
    6886311: "Sight vocabulary",
    6886312: "Whole word",
}]

# split constituent part of approach data (above) for individual column extraction
ph_constit_part_approach_synth_ph = [{
    6886297: "Synthetic phonics",
}]

ph_constit_part_approach_syst_ph = [{
    6886295: "Systematic phonics",
}]

ph_constit_part_approach_analyt_ph = [{
    6886298: "Analytic phonics",
}]

ph_constit_part_approach_analog_ph = [{
    6886300: "Analogy phonics or analogy-based phonics",
}]

ph_constit_part_approach_emb_ph = [{
    6886301: "Embedded phonics",
}]

ph_constit_part_approach_phon_aware = [{
    6886302: "Phonemic awareness",
}]

ph_constit_part_approach_phonol_aware = [{
    6886304: "Phonological awareness",
}]

ph_constit_part_approach_onset_rime = [{
    6886305: "Onset - rime",
}]

ph_constit_part_approach_syll_instr = [{
    6886310: "Syllable instruction",
}]

ph_constit_part_approach_sight_vocab = [{
    6886311: "Sight vocabulary",
}]

ph_constit_part_approach_whole_word = [{
    6886312: "Whole word",
}]

ph_central_teach_lit_output = [{
    # How central is phonics to the overall approach to teaching literacy?
    6886309: "Phonics instruction only",
    6886296: "Phonics as the central or main approach",
    6886292: "Phonics as supplemental or additional to the usual approach to teaching literacy.",
}]

ph_par_invol_output = [{
    # Does the approach involve parents?
    6886293: "Yes",
    6886294: "No",
}]

ph_digit_tech_output = [{
    # Does the approach involve digital technology?
    6886303: "Yes",
    6886299: "No",
}]



# READING COMPREHENSION

rc_components_output = [{
    # "Reading components (select all that apply)"
    5804316: "Strategy instruction/ metacognitive approach (see also next section)",
    5804317: "Vocabulary and/or word study",
    5804323: "Reading fluency (e.g. practice or re-reading)",
    5804321: "Phonics or explicit decoding strategies",
    5804319: "Writing or writing to read approaches",
    5804320: "Other (please specify)",
    5804322: "Unclear/ not specified",
}]

# rc_components split for individual column extraction (per option)

rc_comp_strat_output = [{
    5804316: "Strategy instruction/ metacognitive approach (see also next section)",
}]

rc_comp_vocab_output = [{
    5804317: "Vocabulary and/or word study",
}]

rc_comp_red_flu_output = [{
    5804323: "Reading fluency (e.g. practice or re-reading)",
}]

rc_comp_phon_output = [{
    5804321: "Phonics or explicit decoding strategies",
}]

rc_comp_wri_output = [{
    5804319: "Writing or writing to read approaches",
}]

rc_comp_other_output = [{
    5804320: "Other (please specify)",
}]

rc_comp_unclear_output = [{
    5804322: "Unclear/ not specified",
}]

rc_strat_instruct_type_output = [{
    # If strategy instruction is included, what type? (Select all that apply)
    5804324: "Reciprocal reading/ reciprocal teaching",
    5804325: "Self-questioning",
    5804326: "Graphic organisers and/or diagrams",
    5804327: "Note taking",
    5804328: "Verbalisation and discussion techniques",
    5804329: "Visualisation technqiues",
    5804318: "Self-regulation and/or attribution training",
    5804330: "Other (please specify)",
    5804331: "Unclear/ not specified"
}]

rc_instruct_components_output = [{
    # Instructional components (select all that apply)
    5804332: "Direct instruction",
    5804333: "Demonstration and modelling",
    5804334: "Pupil practice - collaborative",
    5804336: "Pupil practice - individual",
    5804338: "Other (please specify)",
}]

rc_txt_type_output= [{
    # "Text type/ reading materials (select all that apply)"
    5804339: "Narrative text",
    5804340: "Expository text",
    5804341: "Argumentation texts",
    5804342: "Mixed text types",
    5804343: "Not specified/ unclear",
}]


# SOCIAL AND EMOTIONAL LEARNING

sel_involvement_output = [{
    # Who was involved? Select all that apply
    6823381: "All pupils",
    6823396: "Targeted groups of pupils or identified individuals",
    6823391: "Specific classes in a school",
    6823388: "Whole school",
    6823392: "Classroom teachers",
    6823394: "Other staff in the school(s)",
    6823395: "Outside experts or specialists",
    6823389: "Other (Please specify)"
}]

# social and emotional components (as above) split for individual columns
sel_invol_all_pupils = [{
    6823381: "All pupils",
}]

sel_invol_targ_grp = [{
    6823396: "Targeted groups of pupils or identified individuals",
}]

sel_invol_classes = [{
    6823391: "Specific classes in a school",
}]

sel_invol_school = [{
    6823388: "Whole school",
}]

sel_invol_teachers = [{
    6823392: "Classroom teachers",
}]

sel_invol_other_staff = [{
    6823394: "Other staff in the school(s)",
}]

sel_invol_outside_experts = [{
    6823395: "Outside experts or specialists",
}]

sel_invol_other = [{
    6823389: "Other (Please specify)",
}]

sel_focus_output = [{
    # What was the main focus of the programme? 
    6823385: "Improving social interaction",
    6823387: "Reducing antisocial or problematic behaviour",
    6823390: "Developing individual social and emotional capability",
    6823393: "Academic achievement",
    6823397: "Other (Please specify)",
}]

sel_location_output = [{
    # Where did the activities mainly take place 
    6823382: "School",
    6823383: "Home",
    6823384: "Community centre or other local setting",
    6823386: "Other (Please specify)",
}]

# BEHAVIOUR INTERVENTION

bi_target_group_output = [{
    # How is the intervention or approach targeted? Who receives the intervention? 
    5804296: "Universal/ whole class",
    5804297: "Selected or pull out (individual or small group)",
    5804298: "Family group",
    5804299: "Other (please specify)",
    5804300: "Unclear/ not specified (please add notes)"
}]

bi_intervention_approach_output = [{
    # What is the approach used in the intervention? What kinds of behaviours are included?
    5804301: "Social skills / social problem solving",
    5804302: "Anger management/ behavioural treatment",
    5804303: "Other (please specify)"
}]

bi_intervention_components_output = [{
    # What are the components of the intervention? What is included in the approach?
    5804304: "Counselling, discussion or therapy",
    5804305: "Monitoring and/ or feedback",
    5804306: "Self-management techniques",
    5804307: "Role play and/or rehearsal",
    5804308: "Parental/ family involvement",
    5804309: "Academic focus (coaching, mentoring or tutoring)",
    5804310: "Digital technology"
}]

# intervention components (as above) split for individual columns
ind_comp_counselling = [{
    5804304: "Counselling, discussion or therapy"
}]

ind_comp_monitoring = [{
    5804305: "Monitoring and/ or feedback"
}]

ind_comp_self_management = [{
    5804306: "Self-management techniques"
}]

ind_comp_role_play = [{
    5804307: "Role play and/or rehearsal"
}]

ind_comp_parental_involv = [{
    5804308: "Parental/ family involvement"
}]

ind_comp_academic_focus = [{
    5804309: "Academic focus (coaching, mentoring or tutoring)"
}]

ind_comp_digit_tech = [{
    5804310: "Digital technology"
}]

# EXTENDED SCHOOL TIME

extended_how_output = [{
    # How was school time extended? 
    5861598: "Before school",
    5861596: "After school",
    5861597: "At weekends",
    5861594: "During holidays",
    5861593: "Extended school calendar"
}]

time_Added_output = [{
    # How much time was added? (Select best)
    5861590: "Hours per week (add numeric value to info box)",
    5861595: "Days per year (add numeric value to info box)",
    5861599: "Not mentioned/ unclear"
}]

purpose_or_aim_output = [{
    # Purpose or aims (select all that apply) 
    5861591: "Catch-up or remediation",
    5861589: "Enrichment or compensation for disadvantage",
    5861592: "Improving attainment",
    5861600: "Acceleration and/of gifted and talented",
    5861608: "Other (please add details)",
    5861610: "Not specified or unclear"
}]

target_group_output = [{
    # who was the target group?
    5861601: "All pupils",
    5861604: "Disadvantaged pupils",
    5861607: "At risk pupils - academic",
    5861609: "At risk pupils - behaviour",
    5861611: "High achieving/ gifted and talented"
}]

pupil_participation_output = [{
    # pupil participation
    5861577: "Voluntary or optional",
    5861602: "Compulsory or required",
    5861603: "Not mentioned/ unclear"
}]

activity_focus_output = [{
    # activity focus
    5861576: "Adademic only",
    5861578: "Academic and sports or physical activities",
    5861573: "Academic and cultural or artistic",
    5861572: "Academic and vocational skills",
    5861585: "Academic and social"
}]

staff_kind_output = [{
    # teachers and/or staff (staff kind)
    5861571: "Qualified teachers",
    5861570: "Teaching assistants/ paraprofessionals",
    5861584: "Young people/adults (paid)",
    5861586: "Volunteers (unpaid)",
    5861588: "Other (please specify)"
}]

parental_involvement_output = [{
    # parental involvement
    5861583: "Yes",
    5861587: "No / not mentioned",
}]

digital_tech_output = [{
    # digital technology
    5861579: "Yes",
    5861581: "No / not mentioned",
}]

attendance_monitored_output = [{
    # attendance monitored
    5861580: "Yes",
    5861582: "No / not mentioned",
}]

# PEER TUTORING

tutor_age_output = [{
    # Describe the type of tutors involved
    5159578: "Same-age as tutees (if yes, select one from drop down)",
    5159580: "Cross-age (i.e. different school year from tutees)"
}]

# split tutor age components for individual column extraction

tutor_age_same = [{
    5159578: "Same-age as tutees (if yes, select one from drop down)",
}]

tutor_age_cross = [{
    5159580: "Cross-age (i.e. different school year from tutees)",
}]

tutor_same_age_output = [{
    # nested option for 'same-age tutor' from "tutor age"
    5159584: "matched to same level of attainment",
    5159585: "matched to different level of attainment",
    5159586: "not matched on attainment"
}]

tutor_cross_age_output = [{
    # nested option for 'same-age tutor' from 'tutor age'
    5338982: "Matched to same relative level of attainment",
    5338983: "Not matched on attainment"
}]

tutor_from_output = [{
	# Were the tutors…
    5338985: "From the same school",
    5159582: "From a different school"
}]	

tutor_role_output = [{
    # Was the teaching role alternating/reciprocal?
    5159571: "Yes",
    5159579: "No"
}]

tutee_attainment_output = [{
    # What is the level of academic attainment of the tutees?
    5159583: "Low attaining",
    5159577: "Average",
    5159569: "High attaining",
    5159570: "Mixed",
    5159575: "Not mentioned"
}]

digit_tech_output = [{
    # Was digital technology involved?
    5159573: "Yes",
    5159576: "No"
}]

tutor_tutee_incentive_output = [{
    # "Was an incentive provided for the tutors and/or tutees?"
    5159574: "Yes",
    5159572: "No"
}]

# FEEDBACK

feedback_source_output = [{
    # What was the source of the feedback?
    5322873: "Teacher",
    5322875: "Teaching assistant",
    5322876: "Volunteer",
    5322877: "Parent(s) or other relatives",
    5322878: "Researcher",
    5322879: "Peer (same age/ class)",
    5322880: "Peer (group)",
    5322881: "Peer (older)",
    5322882: "Digital or automated",
    5322885: "Other non-human",
    5322887: "Self",
    5322888: "Other (please specify"
}]

# feedback source (above) extraction into individual columns

fsource_teacher = [{
    5322873: "Teacher",
}]

fsource_ta = [{
    5322875: "Teaching assistant",
}]

fsource_volunteer = [{
    5322876: "Volunteer",
}]

fsource_parent = [{
    5322877: "Parent(s) or other relatives",
}]

fsource_researcher = [{
    5322878: "Researcher",
}]

fsource_peer_sameage_class = [{
    5322879: "Peer (same age/ class)",
}]

fsource_peer_group = [{
    5322880: "Peer (group)",
}]

fsource_peer_older = [{
    5322881: "Peer (older)",
}]

fsource_dig_aut = [{
    5322882: "Digital or automated",
}]

fsource_other_nonhuman = [{
    5322885: "Other non-human",
}]

fsource_self = [{
    5322887: "Self",
}]

fsource_other = [{
    5322888: "Other (please specify",
}]


feedback_directed_output = [{
    # Who was the feedback directed to?
    5322871: "Individual pupil",
    5322872: "General (group or class)",
    5322874: "Teacher",
}]

feedback_form_output = [{
    # What form did the feedback take? (Select one)
    5322870: "Spoken verbal",
    5322886: "Non-verbal",
    5322883: "Written verbal",
    5322884: "Written, non-verbal"
}]

feedback_when_output = [{
    # When did the feedback happen? (Select one)
    5322859: "Prior to the task",
    5322862: "During the task",
    5322860: "Immediate",
    5322861: "Delayed (short)",
    5322866: "Delayed (long)"
}]

feedback_kind_output = [{
    # "What kind of feedback was provided?"
    5322863: "About the outcome",
    5322864: "About the process of the task",
    5322867: "About the learner's strategies or approach",
    5322869: "About the person"
}]

# nested info from variable above ^
feedback_about_outcome_output = [{
    5322889: "Correct",
    5322890: "Incorrect"
}]

feedback_emo_tone = [{
    # What was the emotional tone of the feedback?
    5322865: "Positive",
    5322868: "Neutral",
    5322858: "Negative"
}]

# TEACHING ASSISTANTS

ta_description_output = [{
    # How are the teaching assistants described?
    5159744: "Teaching or classroom assistant",
    5159739: "Higher level teaching assistant",
    5159740: "Teacher's aide",
    5159736: "Paraprofessional or paraeducator",
    5159737: "Educational or instructional assistant",
    5159742: "Pupil support worker or student support worker",
    5159743: "Other (please specify)"
}]

ta_role_output = [{
    # What is the teaching assistants' role?
    5159730: "Curriculum instruction (please specify)",
    5159734: "Behaviour support",
    5159738: "Assessment",
    5159741: "General classroom support",
    5159745: "Not specified/ unclear"
}]

ta_group_size_output = [{
    # How many pupils is the teaching assistant working with?
    5159731: "One to one",
    5159732: "Small group (2-4 pupils)",
    5159733: "Large group (5 - 12 pupils)",
    5159735: "Whole class"
}]

# MENTORING

mentor_identity = [{
    # Who were the mentors?
    6120260: 'Older school students',
    6120258: 'College or University students',
    6120259: 'Adults (see description)',
    6120256: 'Other (please specify)'
}]

mentor_paid_or_compensated = [{
    # Were the mentors paid or compensated in any way?
    6120253: 'Yes',
    6120257: 'No',
    6120261: 'Unclear/ No information'
}]

mentor_organisation = [{
    # Who organised the mentoring?
    6120254: 'The school(s)',
    6120252: 'A local community group',
    6120255: 'A charity or other voluntary organisation',
    6120268: 'The local authority, government or state',
    6120269: 'Other (please specify'
}]

mentor_training = [{
    # Was training provided for mentors?
    6120264: 'Yes',
    6120267: 'No',
    6120271: 'Unclear/ No information'
}]

mentor_meeting_frequency = [{
    # How frequently did meetings take place?
    6120232: 'Daily',
    6120238: 'Weekly',
    6120239: 'Every two to three weeks',
    6120270: 'Monthly',
    6120262: 'Every term',
    6120263: 'Other (please specify)'
}]

mentor_meeting_details_provided = [{
    # Are details provided of what happened in mentoring meetings?
    6120265: 'Yes',
    6120266: 'No',
    6120236: 'Unclear/Not specified'
}]

mentor_meeting_location = [{
    # Where did meetings take place? (Select main setting)
    6120233: 'In school',
    6120234: 'In the home',
    6120235: 'In the community',
    6120237: 'By phone or online',
    6120240: 'Other (please specify)',
    6120244: 'Not specified'
}]

mentoring_additional_experiences = [{
    # Did the mentoring involve additional experiences?
    6120251: 'Yes',
    6120247: 'No',
    6120241: 'Unclear/ not specified'
}]

mentoring_programme_focus = [{
    # What was the focus or goals of the mentoring programme?
    6120242: 'Improving academic attainment or performance',
    6120243: 'Improving attendance',
    6120245: 'Preventing or reducing problem behaviours in school',
    6120246: 'Improving social interaction or social competence',
    6120248: 'Preventing or addressing medical or psychological issues',
    6120249: 'Improving career or employment aspirations and opportunities',
    6120250: 'Increasing motivation or raising aspirations'
}]

# ONE TO ONE
comparisons_available = [{
    # Which comparisons are available in this study? (Select all that apply)
    5697922: 'With business as usual comparison (no additional support, but still being taught)',
    5697923: 'With no equivalent teaching (e.g. summer school)',
    5697924: 'With alternative tutor (e.g. teaching assistant vs volunteer)',
    5697925: 'With alternative approach: Small group (2-5 pupils)',
    5697926: 'With alternative approach: Large group (6-15 pupils)',
    5697927: 'With alternative approach: computer/ digital technology',
    5893849: 'With alternative approach: other (please specify)',
    5697928: 'With pupils at a different level of attainment'
}]

# SMALL GROUP
group_size_output = [{
    # Group size
    5566314: '2',
    5566308: '3',
    5566311: '4',
    5566316: '5',
    5566317: 'Mixed groups'
}]

group_composition_output = [{
    # Group composition
    5566303: 'Same level - low attainers',
    5566307: 'Same level - average attainers',
    5566309: 'Same level - high attainers',
    5566310: 'Mixed attainment - all pupils',
    5566312: 'Mixed attainment - high and low',
    5566313: 'Mixed attainment - low and average',
    5566315: 'Mixed attainment - high and average'
}]

group_teaching_lead_output = [{
    # Group size
    5566302: 'Teacher',
    5566304: 'Teaching assistant',
    5566305: 'Researcher',
    5566306: 'Digital technology'
}]

##########################################################

other_outcomes_output = [{ 
    # In addition to the primary educational attainment outcome, are there other outcomes reported? 
    5215572: 'Yes',
    5215573: 'No'
}]   

addit_out_output = [{ 
    # If yes, which other outcomes are reported? 
    5215575: 'Cognitive outcomes measured (Please specify)',
    5215576: 'Other types of student outcomes (Please specify)'
}] 

other_part_output = [{ 
    # Other participants (i.e. not students) outcomes
    5215577: 'Other participants (i.e. not students) outcomes (Please specify)'
}]

sample_size_intervention_output = [{  
    # What is the sample size for the intervention group?
    5407108: ''
}]

sample_size_control_output = [{  
    # What is the sample size for the control group?
    5407109: ''
}]

sample_size_second_intervention_output = [{  
    # *What is the sample size for the second intervention group?}
    5407120: ''
}]

sample_size_third_intervention_output = [{  
    # *What is the sample size for the third intervention group?}
    5407121: ''
}]

samp_size_anal_int_output = [{  
    # intervention group Number (n}
    5406980: ''
}]

samp_size_anal_cont_output = [{  
    # control* group Number (n}
    5406985: ''
}]

samp_size_anal_sec_int_output = [{  
    # If yes, please add for a second intervention* group (if needed)
    5407135: ''
}]

samp_size_anal_sec_cont_output = [{  
    # If needed, please add for the control group
    5447053: ''
}]

clustering_output = [{  
    # Is clustering accounted for in the analysis?
    5407158: "Yes",
    5407159: "No",
    5407160: "Unclear"
}]

comp_vars_rep = [{  
    # Are the variables used for comparability reported?"
    5406859: 'Yes',
    5406862: 'No',
    5406863: 'N/A'
}]

which_comp_vars_rep_output = [{  
    # If yes, which variables are used for comparability?
    5407122: 'Educational attainment',
    5407123: 'Gender',
    5407124: 'Socio-economic status',
    5407128: 'Special educational needs',
    5407129: 'Other (please specify)'
}]

comparability_output = [{  
    # Is comparability taken into account in the analysis?
    5406855: 'Unclear or details not provided',
    5406861: 'Yes',
    5406864: 'No'
}]

baseline_diff_output = [{  
    # Does the study report any group differences at baseline?
    5406860: 'No/Unclear',
    5406866: 'Yes'
}]

attr_dropout_rep_output = [{ 
     # Is attrition or drop out reported?
    5407034: 'Yes',
    5407035: 'No',
    5407036: 'Unclear (please add notes)'
}]

treat_grp_attr = [{  
    # What is the attrition in the treatment group?
    5407037: ''
}]

overall_perc_attr = [{  
    # What is the total or overall percentage attrition?
    5407038: ''
}]

study_design_output = [{  
    # What was the study design?
    5406847: 'Individual RCT',
    5406849: 'Cluster RCT',
    5406851: 'Multisite RCT',
    5406852: 'Prospective QED',
    5406856: 'Retrospective QED',
    5406853: 'Interrupted time series QED',
    5407075: 'Regression Discontinuity with randomisation',
    5406854: 'Regression Discontinuity - not randomised',
    5406857: 'Regression Continuity  - naturally occurring'
}]

# MORE LOCATION INFORMATION
specific_to_location = [{  
    # Specific to the location or place
    5372848: ''
}]

type_of_location = [{  
    # Information about the type of location
    5372849: ''
}]

no_location_info = [{  
    # No information provided
    5372850: ''
}]

########################################
# DESCRIPTIVE STATISTICS PRIMARY OUTCOME
########################################

desc_stats_primary_outcome = [{  
    # Are descriptive statistics reported for the primary outcome?
    5407095: "Yes",
    5407096: "No"
}]

# INTERVENTION (TREATMENT) GROUP

int_grp_number = [{  
    # intervention group Number (n}
    5406980: ''
}]

int_grp_pretest_mean = [{  
    # intervention group Pre-test mean
    5406981: ''
}]

int_grp_pretest_sd = [{  
    # intervention* group Pre-test SD
    5406982: ''
}]

intn_grp_posttest_mean = [{  
    # intervention* group Post-test mean
    5406983: ''
}]

int_grp_posttest_sd = [{ 
    # intervention* group Post-test SD
    5406989: ''
}]

int_grp_gain_score_mean = [{  
    # intervention gain score mean
    5407130: ''
}]

int_grp_gain_score_sd = [{ 
     # intervention gain score sd
    5407131: ''
}]

int_grp_any_other_info = [{  
    # intervention -  any other info}]
    5406990: ''
}]

# control group

ctrl_grp_number = [{  
    # control* group Number (n}
    5406985: ''
}]

ctrl_grp_pretest_mean = [{  
    # control group Pre-test mean
    5406986: ''
}]

ctrl_grp_pretest_sd = [{  
    # control group Pre-test SD
    5406987: ''
}]

ctrl_grp_posttest_mean = [{  
    # control group Post-test mean
    5406988: ''
}]

ctrl_grp_posttest_sd = [{  
    # control group Post-test SD
    5406984: ''
}]

ctrl_grp_gain_score_mean = [{ 
     # control gain score mean
    5407132: ''
}]

ctrl_grp_gain_score_sd = [{  
    # control gain score sd
    5407133: ''
}]

ctrl_grp_any_other_info = [{  
    # control -  any other info
    5406991: ''
}]

# intervention (treatment) group two

int_grp_two_number = [{  
    # intervention group Number (n)
    5407135: ''
}]

int_grp_two_pretest_mean = [{  
    # intervention group Pre-test mean
    5407136: ''
}]

int_grp_two_pretest_sd = [{  
    # intervention* group Pre-test SD
    5407137: ''
}]

int_grp_two_posttest_mean = [{  
    # intervention* group Post-test mean
    5407138: ''
}]

int_grp_two_posttest_sd = [{  
    # intervention* group Post-test SD
    5407139: ''
}]

int_grp_two_gain_score_mean = [{  
    # intervention gain score mean
    5407141: ''
}]

int_grp_two_gain_score_sd = [{  
    # intervention gain score sd
    5407142: ''
}]

int_grp_two_any_other_info = [{  
    # intervention - any other info
    5407140: ''
}]

# control group two

control_group_two_number = [{  
    # control* group Number (n)
    5447053: ''
}]

control_group_two_pretest_mean = [{  
    # control group Pre-test mean
    5447054: ''
}]

control_group_two_pretest_sd = [{  
    # control group Pre-test SD
    5447055: ''
}]

control_group_two_posttest_mean = [{  
    # control group Post-test mean
    5447056: ''
}]

control_group_two_posttest_sd = [{  
    # control group Post-test SD
    5447057: ''
}]

control_group_two_gain_score_mean = [{  
    # control gain score mean
    5447058: ''
}]

control_group_two_gain_score_sd = [{  
    # control gain score sd
    5447059: ''
}]

control_group_two_any_other_info = [{  
    # control -  any other info}]
    5447060: ''
}]

follow_up_data_reported = [{  
    # Is there follow up data?
    5407103: 'Yes',
    5407104: 'No'
}]

###########################
# INTERVENTION INFORMATION
###########################

int_name_output = [{  
    # "What is the intervention name?"
    5215238: ''
}]

intervention_description_output = [{  
    # How is the intervention described?
    5215563: ''
}]

intervention_objectives_output = [{  
    # What are the intervention objectives?
    5215564: ''
}]

int_org_type_output = [{  
    # What type of organisation was responsible for providing the intervention?
    5215491: "School or group of schools",
    5215492: "Charity or voluntary organisation",
    5215493: "University/ researcher design",
    5215494: "Local education authority or district",
    5215495: "Private or commercial company",
    5215496: "Other (please provide details)"
}]

int_training_provided_output = [{  
    # Was training for the intervention provided?
    5215498: "Yes (Please specify)",
    5215499: "No",
    5215500: "Unclear/ Not specified"
}]

int_focus_output = [{  
    # Who is the focus of the intervention? (Select ALL that apply)
    5215502: "Students",
    5215503: "Teachers",
    5215504: "Teaching assistants",
    5215505: "Other education practitioners",
    5215506: "Non-teaching staff",
    5215507: "Senior management",
    5215508: "Parents",
    5215509: "Other (Please specify)"
}]

intervention_teaching_approach = [{  
    # What is the intervention teaching approach? (Select ALL that apply)
    5215513: "Large group/class teaching (+6)",
    5215512: "Small group/intensive support (3-5)",
    5216713: "Paired learning",
    5215586: "One to one",
    5215511: "Student alone (self-administered)",
    5216714: "Other (Explain in notes)"
}]

# intervention approach inclusion
int_appr_dig_tech = [{  
    # Were any of the following involved in the intervention or approach?
    # Digital Technology
    5216718: "Yes",
    5216719: "No"
}]

int_appr_par_or_comm_vol = [{  
    # Were any of the following involved in the intervention or approach?
    # Parents or community volunteers
    5216720: "Yes",
    5216721: "No"
}]

intervention_time_output = [{  
    # When did the intervention take place?  (Select ALL that apply)
    5215580: "During regular school hours ",
    5215581: "Before/after school",
    5215582: "Evenings and/or weekends",
    5215583: "Summer/ holiday period",
    5215584: "Other (please specify)",
    5215585: "Unclear/ not specified"
}]

intervention_delivery_output = [{  
    # Who was responsible for the teaching at the point of delivery? (Select ALL that apply)
    5215553: "Research staff",
    5215554: "Class teachers",
    5215555: "Teaching assistants",
    5215556: "Other school staff",
    5215557: "External teachers",
    5215558: "Parents/carers",
    5215559: "Lay persons/volunteers",
    5215560: "Peers",
    5215561: "Digital technology",
    5215562: "Unclear/not specified"
}]

int_dur_output = [{  
    # What was the duration of the intervention? (Please add to info box and specify units)
    5215517: ''
}]

inte_freq_output = [{  
    # What was the frequency of the intervention?
    5215518: ''
}]

intervention_session_length_output = [{  
    # What is the length of intervention sessions?
    5215519: ''
}]

int_impl_details = [{  # Are implementation details and/or fidelity details provided?
    5215521: "Qualitative",
    5215522: "Quantitative",
    5215523: "No implementation details provided."
}]

int_costs_reported = [{  # Are the costs reported?
    5215528: "Yes (Please add details)",
    5215529: "No"
}]

int_eval_output = [{  # Who undertook the outcome evaluation?
    5215533: "The developer",
    5215532: "A different organization paid by developer",
    5215531: "An organization commissioned independently to evaluate",
    5215534: "Unclear/not stated",
    5215578: "Is this an EEF evaluation?"
}]

####################################
# SETTING & SAMPLE CHARACTERISTICS #
####################################

# NUMBER OF SCHOOLS
number_of_schools_intervention_output = [{  
    # What is the number of schools involved in the intervention group(s)?
    5407111: ''
}]

number_of_schools_control_output = [{  
    # What is the number of schools involved in the control or comparison group?
    5407106: ''
}]

number_of_schools_total_output = [{  
    # What is the total number of schools involved?
    5407115: ''
}]

number_of_schools_not_provided_output = [{  
    # Not provided/ unclear / not applicable
    5407113: 'not_provided'
}]

# NUMBER OF CLASSES
num_of_class_int_output = [{  
    # What is the total number of classes involved in the intervention group?
    5407105: ''
}]

num_of_class_cont_output = [{  
    # What is the total number of classes involved in the control or comparison group?
    5407107: ''
}]

num_of_class_tot_output = [{  
    # What is the total number of classes involved?
    5407153: ''
}]

numb_of_class_np_output = [{  
    # Not provided/ unclear / not applicable
    5407114: 'not_provided'
}]

# SAMPLE SIZE
sample_size_output = [{  
    # What is the overall sample analysed?
    5215428: ''}]

# GENDER SPLIT
gender_split_output = [{  
    # Provide the percentage or number of female pupils in the study
    5215644: ''}]

# STUDENT AGES
student_age_output = [{  
    # What is the age of the students? (Select ALL that apply)
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
    5513031: 'No information provided'
}]

# PROPORTION LOW SES/FSM STUDENTS IN SAMPLE
proportion_low_fsm_output = [{  
    # What is the proportion of low SES/FSM students in the sample?
    5215454: ''
}]

# PERCENTAGE LOW SES_FSM STUDENTS IN SAMPLE
percentage_low_fsm_output = [{  
    # FSM or low SES student percentage
    5376693: ''
}]

# FURTHER SES/FSM INFORMATION IN SAMPLE
further_ses_fsm_info_output = [{  
    # Further information about FSM or SES in the study sample.
    5376694: ''
}]

# NO SES/FSM INFO PROVIDED
no_ses_fsm_info_provided_output = [{  
    # No SES/FSM information provided
    5366637: 'No SES/FSM Information Provided'
}]

study_realism_output = [{  # How realistic was the study?
    5215255: 'High ecological validity',
    5215256: 'Low ecological validity',
    5215257: 'Unclear'
}]

study_design_output = [{  # What was the study design?
    5406847: 'Individual RCT',
    5406849: 'Cluster RCT',
    5406851: 'Multisite RCT',
    5406852: 'Prospective QED',
    5406853: 'Interrupted time series QED',
    5406854: 'Regression Discontinuity - not randomised',
    5406856: 'Retrospective QED  ',
    5406857: 'Regression Continuity  - naturally occurring',
    5407075: 'Regression Discontinuity with randomisation'
}]

edu_setting_output = [{  # What is the educational setting (Select ALL that apply)
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
    5513033: 'No information provided'
}]

publication_type_output = [{  # Section 1 What is the publication type?
    5215227: 'Journal article',
    5215228: 'Dissertation or thesis',
    5215229: 'Technical report',
    5215230: 'Book or book chapter',
    5215231: 'Conference paper'
}]

level_of_assignment_output = [{  # What was the level of assignment?
    5215244: 'Individual',
    5215245: 'Class',
    5215246: 'School - cluster',
    5215247: 'School - multi-site',
    5215248: 'Region or district',
    5215249: 'Not provided/ not available'
}]

part_assign_output = [{  # How were participants assigned?
    5215251: 'Random (please specify)',
    5215252: 'Non-random, but matched',
    5215253: 'Non-random, not matched prior to treatment',
    5215565: 'Unclear',
    5641086: 'Not assigned - naturally occurring sample',
    5641087: 'Retrospective Quasi Experimental Design (QED)',
    5641088: 'Regression discontinuity'
}]

student_gender = [{  # What is the gender of the students?
    5215642: 'Female only',
    5215643: 'Male only',
    5215644: 'Mixed gender',
    5513032: 'No information provided'
}]

# standard academic outcome codes
outcome_type_codes = [{  # Outcome type (select all that apply)
    7755570: "Toolkit primary outcome",
    7755571: "Reading primary outcome",
    7755572: "Writing and spelling primary outcome.",
    7755573: "Mathematics primary outcome",
    7755574: "Science primary outcome",
    7755575: "Other outcome"
}]

# CEDIL standard academic outcome codes
""" outcome_type_codes = [{  # Outcome type (select all that apply)
    8934475: "Toolkit primary outcome",
    8934476: "Reading primary outcome",
    8934477: "Writing and spelling primary outcome.",
    8934478: "Mathematics primary outcome",
    8934479: "Science primary outcome",
    8934480: "Other outcome"
}] """

sample_output = [{  
    # Sample (select one from this group)
    5407009: 'Sample: All',
    5407041: 'Sample: Exceptional',
    5407006: 'Sample: High achievers',
    5407008: 'Sample: Average',
    5407007: 'Sample: Low achievers'
}]

curriculum_subjects = [{  
    # Curriculum subjects tested
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
    5215551: "Other curriculum test"
}]

other_out_output = [{  
    # In addition to the primary educational attainment outcome, are there other outcomes reported?
    5215572: "Yes",
    5215573: "No"
}]

which_other_outcomes_output = [{  
    # If yes, which other outcomes are reported?
    5215575: 'Cognitive outcomes measured (Please specify)',
    5215576: 'Other types of student outcomes (Please specify)'}]

other_participants_output = [{  
    # [part of the above 'which other outcomes output' list, but separated for its own column]]
    5215577: 'Other participants (i.e. not students) outcomes (Please specify)'
}]

randomisation_details = [{  
    # Are details of randomisation provided?
    5407117: "Yes",
    5407119: "Not applicable",
    5407118: "No/Unclear"
}]

treatment_group = [{ 
    # Is there more than one treatment group?
    5215240: "Yes (Please specify)",
    5215241: "No",
    5215242: "Not specified or N/A"
}]


admin_strand_output = [{  
    # Admin Strand
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
    5023574: 'Physical activity',
    5023568: 'Reading comprehension strategies',
    5023569: 'Reducing class size',
    5023570: 'Repeating a year',
    5023571: 'School uniform',
    5023572: 'Setting or streaming',
    5023549: 'Small group tuition',
    5023573: 'Social and emotional learning',
    5023575: 'Summer schools',
    5023576: 'Teaching assistants',
    8840447: 'Within-class attainment grouping',
    11237538: 'EY_Communication and language approaches',
    10723728: 'EY_Earlier starting age',
    10215932: 'EY_Early literacy approaches',
    10215931: 'EY_Early numeracy approaches',
    10700240: 'EY_Extra hours',
    11237553: 'EY_Parental engagement',
    11640334: 'EY_Physical development approaches',
    10699481: 'EY_Play-based learning',
    11237556: 'EY_Self-regulation strategies',
    11237560: 'EY_Social and emotional strategies'
}]

toolkit_strand_codes = [{  
    # Toolkit strand(s) (select at least one Toolkit strand)
    5407042: 'Toolkit: Arts participation ',
    5407043: 'Toolkit: Aspiration interventions',
    5407044: 'Toolkit: Behaviour interventions',
    5407045: 'Toolkit: Block scheduling',
    5407046: 'Toolkit: Built environment',
    5407047: 'Toolkit: Collaborative learning',
    5407048: 'Toolkit: Digital technology',
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
    5407072: 'Toolkit: Physical activity',
    5407065: 'Toolkit: Reading comprehension strategies',
    5407066: 'Toolkit: Reducing class size',
    5407067: 'Toolkit: Repeating a year',
    5407068: 'Toolkit: School uniform',
    5407069: 'Toolkit: Setting or streaming',
    5407070: 'Toolkit: Small Group Tuition',
    5407071: 'Toolkit: Social and emotional learning',
    5407073: 'Toolkit: Summer schools',
    5407074: 'Toolkit: Teaching assistants',
    8931762: 'Toolkit: Within-class attainment grouping',
    11183748: 'EY_Communication and language approaches',
    11183743: 'EY_Earlier starting age',
    11183744: 'EY_Early literacy approaches',
    11183745: 'EY_Early numeracy approaches',
    11183746: 'EY_Extra hours',
    11710297: 'EY_Parental engagement',
    11710298: 'EY_Physical development approaches',
    11183747: 'EY_Play-based learning',
    11710299: 'EY_Self-regulation strategies',
    11710301: 'EY_Social and emotional strategies'
}]

test_type_output = [{  
    # Test type (select one from this group)
    5407028: 'Test type: Standardised test ',
    5407029: 'Test type: Researcher developed test',
    5407031: 'Test type: National test',
    5407030: 'Test type: School-developed test',
    5407032: 'Test type: International tests'
}]

test_type_main = [{  
    # What kind of tests were used? (Select ALL that apply)
    5215537: 'Standardised test',
    5215538: 'Researcher developed test',
    5215539: 'School-developed test',
    5215540: 'National test or examination',
    5215541: 'International tests'
}]

es_type_output = [{  
    # Effect size calculation (select one from this group)
    5407010: 'Post-test unadjusted (select one from this group)',
    5407011: 'Post-test adjusted for baseline attainment',
    5407152: 'Post-test adjusted for baseline attainment AND clustering',
    5407012: 'Pre-post gain'
}]

countries = [{  
    # In which country/countries was the study carried out? (Select ALL that apply)
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
    5215641: 'Uruguay'
}]


# CEDIL #1 = cash transfer #2 = menstrual hygiene
# 1
""" publication_type_CEDIL = [{  # Section 1 What is the publication type?
    8067971: 'Journal article',
    8067972: 'Dissertation or thesis',
    8067973: 'Technical report',
    8067974: 'Book or book chapter',
    8067975: 'Conference paper',
}] """

# 2
publication_type_CEDIL = [{  # Section 1 What is the publication type?
    8349803: 'Journal article',
    8349804: 'Dissertation or thesis',
    8349805: 'Technical report',
    8349806: 'Book or book chapter',
    8349807: 'Conference paper',
    8349808: 'Other (Please specify)',
}]


# 1
admin_strand_CEDIL = [{  # Admin Strand
    8934821: 'Arts participation',
    8934822: 'Aspiration interventions',
    8934823: 'Behaviour interventions',
    8934824: 'Block scheduling',
    8934825: 'Built environment',
    8934826: 'Collaborative learning',
    8934827: 'Digital technology',
    8934828: 'Early years intervention',
    8934829: 'Extending school time',
    8934830: 'Feedback',
    8934831: 'Homework',
    8934832: 'Individualised instruction',
    8934833: 'Learning styles',
    8934834: 'Mastery learning',
    8934836: 'Mentoring',
    8934835: 'Metacognition and self-regulation',
    8934837: 'One to one tuition',
    8934838: 'Oral language interventions',
    8934839: 'Outdoor adventure learning',
    8934840: 'Parental engagement',
    8934841: 'Peer tutoring',
    8934842: 'Performance pay',
    8934843: 'Phonics',
    8934844: 'Reading comprehension strategies',
    8934845: 'Reducing class size',
    8934846: 'Repeating a year',
    8934847: 'School uniform',
    8934848: 'Setting or streaming',
    8934849: 'Small group tuition',
    8934850: 'Social and emotional learning',
    8934851: 'Sports participation',
    8934852: 'Summer schools',
    8934853: 'Teaching assistants',
    8934854: 'CEDIL: Cash Transfer',
    8934855: 'CEDIL: Menstrual Hygiene Intervention',
    8934856: 'CEDIL: Corporal Punishment',
}]


# 1
""" country_CEDIL = [{  
    # In which country/countries was the study carried out? (Select ALL that apply)
    8068012: 'USA',
    8068007: 'UK (Select all that apply)',
    8068013: 'Afghanistan',
    8068014: 'Albania',
    8068016: 'Angola',
    8068017: 'Armenia',
    8068015: 'Argentina',
    8068019: 'Australia',
    8068018: 'Austria',
    8068020: 'Azerbaijan',
    8068021: 'Bahamas, The',
    8068022: 'Bahrain',
    8068023: 'Bangladesh',
    8068025: 'Barbados',
    8068027: 'Belgium',
    8068024: 'Belarus',
    8068026: 'Belize',
    8068028: 'Benin',
    8068033: 'Bolivia',
    8068032: 'Brazil',
    8068031: 'Botswana',
    8068030: 'Bosnia and Herzegovina',
    8068031: 'Botswana',
    8068034: 'Brunei Darussalam',
    8068036: 'Bulgaria',
    8068035: 'Burkina Faso',
    8068029: 'Bhutan',
    8068037: 'Cabo Verde',
    8068038: 'Cambodia',
    8068040: 'Cameroon',
    8068039: 'Canada',
    8068041: 'Central African Republic',
    8068042: 'Chad',
    8068043: 'Chile',
    8068049: 'China',
    8068045: 'Congo',
    8068046: 'Costa Rica',
    8068047: "Côte d'Ivoire / Ivory Coast",
    8068048: 'Croatia',
    8068050: 'Cuba',
    8068044: 'Colombia',
    8068051: 'Cyprus',
    8068053: 'Czech Republic',
    8068054: 'Dominican Republic',
    8068052: 'Denmark',
    8068055: 'Egypt',
    8068056: 'Ecuador',
    8068057: 'El Salvador',
    8068058: 'Equatorial Guinea', 
    8068060: 'Eritrea',
    8068059: 'Estonia',
    8068061: "Ethiopia",
    8068062: 'Finland',
    8068063: 'Fiji',
    8068064: 'France',
    8068065: "Gabon",
    8068067: 'Gambia, The',
    8068066: 'Georgia',
    8068070: 'Ghana',
    8068068: 'Germany',
    8068069: 'Greece',
    8068072: 'Grenada',
    8068071: 'Guatemala',
    8068074: 'Guinea',
    8068073: 'Guinea-Bissau',
    8068075: 'Guyana',
    8068076: 'Haiti',
    8068077: 'Honduras',
    8068078: 'Hong Kong (see China)',
    8068079: 'Hungary',
    8068080: 'Iceland',
    8068082: 'India',
    8068081: 'Indonesia',
    8068083: 'Iran',
    8068084: 'Iraq',
    8068085: 'Ireland',
    8068087: 'Israel',
    8068086: 'Italy',
    8068047: "Côte d'Ivoire / Ivory Coast",
    8068092: 'Kazakhstan ',
    8068090: 'Jordan',
    8068091: 'Kenya',
    8068160: 'South Korea / Republic of Korea',
    8068094: 'Kirkibati',
    8068093: 'Kuwait',
    8068096: 'Kyrgystan',
    8068089: 'Japan',
    8068088: 'Jamaica',
    8068095: 'Lao (or Laos)',
    8068097: 'Latvia',
    8068098: 'Lebanon',
    8068100: 'Lesotho',
    8068099: 'Liberia',
    8068102: 'Liechtenstein',
    8068101: 'Lybia',
    8068104: 'Lithuania',
    8068103: 'Luxembourg',
    8068108: 'Malawi',
    8068106: 'Macedonia',
    8068105: 'Madagascar',
    8068107: 'Malaysia',
    8068110: 'Maldives',
    8068109: 'Mali',
    8068111: 'Malta',
    8068113: 'Mauritania',
    8068114: 'Mauritius',
    8068116: 'Mexico',
    8068115: 'Micronesia',
    8068112: 'Marshall Islands',
    8068119: 'Mozambique',
    8068117: 'Moldova',
    8068118: 'Mongolia ',
    8068121: 'Myanmar (Burma)',
    8068120: 'Namibia',
    8068123: 'Nauru',
    8068122: 'Nepal',
    8068125: 'New Zealand',
    8068124: 'The Netherlands',
    8068023: 'Nicaragua',
    8068128: 'Niger',
    8068127: 'Nigeria',
    8068129: 'Pakistan',
    8068130: 'Norway',
    8068131: 'Palau',
    8068132: 'Panama',
    8068133: 'Papua New Guinea',
    8068134: 'Peru',
    8068135: 'Philippines',
    8068136: 'Poland',
    8068138: 'Portugal',
    8068137: 'Puerto Rico (US dependency)',
    8068139: 'Quatar',
    8068140: 'Romania',
    8068142: 'Russia',
    8068141: 'Rwanda',
    8068143: 'Saint Kitts and Nevis',
    8068144: 'Saint Lucia',
    8068145: 'Saint Vincent and the Grenadines',
    8068147: 'Samoa',
    8068149: 'São Tomé and Príncipe',
    8068146: 'San Marino',
    8068148: 'Saudi Arabia',
    8068150: 'Serbia',
    8068151: 'Senegal',
    8068152: 'Seychelles',
    8068155: 'Singapore',
    8068153: 'Sierra Leone',
    8068154: 'Slovakia',
    8068156: 'Slovenia',
    8068157: 'Solomon Islands',
    8068159: 'Somalia',
    8068158: 'South Africa',
    8068160: 'South Korea / Republic of Korea',
    8068161: 'South Sudan',
    8068163: 'Spain',
    8068162: 'Sri Lanka',
    8068164: 'Sudan',
    8068165: 'Suriname',
    8068166: 'Swaziland / Eswatini',
    8068167: 'Sweden',
    8068168: 'Switzerland',
    8068170: 'Syria',
    8068169: 'Taiwan',
    8068172: 'Tajikistan',
    8068173: 'Thailand',
    8068171: 'Tanzania',
    8068174: 'Timor-Leste',
    8068175: 'Togo',
    8068176: 'Tonga',
    8068178: 'Trinidad and Tobago',
    8068177: 'Tunisia',
    8068179: 'Turkey',
    8068180: 'Turkmenistan',
    8068181: 'Tuvalu',
    8068183: 'Uganda',
    8068182: 'Ukraine',
    8068184: 'United Arab Emirates',
    8068185: 'Uruguay',
    8068186: 'Uzbekistan',
    8068187: 'Vanuatu',
    8068188: 'Venezuela',
    8068189: 'Vietnam',
    8068190: 'West Indies (Use for Caribbean colonial dependencies)',
    8068191: 'Yemen',
    8068192: 'Zambia',
    8068193: 'Zimbabwe',
    8068008: 'England',
    8068010: 'Scotland',
    8068009: 'Northern Ireland',
    8068011: 'Wales',
}] """

# 2
country_CEDIL = [{
    # In which country/countries was the study carried out? (Select ALL that apply)
    8349844: 'USA',
    8349839: 'UK (Select all that apply)',
    8349845: 'Afghanistan',
    8349846: 'Albania',
    8349848: 'Angola',
    8349849: 'Armenia',
    8349847: 'Argentina',
    8349851: 'Australia',
    8349850: 'Austria',
    8349852: 'Azerbaijan',
    8349853: 'Bahamas, The',
    8349854: 'Bahrain',
    8349855: 'Bangladesh',
    8349857: 'Barbados',
    8349859: 'Belgium',
    8349856: 'Belarus',
    8349858: 'Belize',
    8349860: 'Benin',
    8349865: 'Bolivia',
    8349864: 'Brazil',
    8068031: 'Botswana',
    8349862: 'Bosnia and Herzegovina',
    8349863: 'Botswana',
    8349866: 'Brunei Darussalam',
    8349868: 'Bulgaria',
    8349867: 'Burkina Faso',
    8349861: 'Bhutan',
    8349869: 'Cabo Verde',
    8349870: 'Cambodia',
    8349872: 'Cameroon',
    8349871: 'Canada',
    8349873: 'Central African Republic',
    8349874: 'Chad',
    8349875: 'Chile',
    8349881: 'China',
    8349877: 'Congo',
    8349878: 'Costa Rica',
    8349879: "Côte d'Ivoire / Ivory Coast",
    8349880: 'Croatia',
    8349882: 'Cuba',
    8349876: 'Colombia',
    8349883: 'Cyprus',
    8349885: 'Czech Republic',
    8349886: 'Dominican Republic',
    8349884: 'Denmark',
    8349887: 'Egypt',
    8349888: 'Ecuador',
    8349889: 'El Salvador',
    8349890: 'Equatorial Guinea',
    8349892: 'Eritrea',
    8349891: 'Estonia',
    8349893: "Ethiopia",
    8349894: 'Finland',
    8349895: 'Fiji',
    8349896: 'France',
    8349897: "Gabon",
    8349899: 'Gambia, The',
    8349898: 'Georgia',
    8349902: 'Ghana',
    8349900: 'Germany',
    8349901: 'Greece',
    8349904: 'Grenada',
    8349903: 'Guatemala',
    8349906: 'Guinea',
    8349905: 'Guinea-Bissau',
    8349907: 'Guyana',
    8349908: 'Haiti',
    8349909: 'Honduras',
    8349910: 'Hong Kong (see China)',
    8349911: 'Hungary',
    8349912: 'Iceland',
    8349914: 'India',
    8349913: 'Indonesia',
    8349915: 'Iran',
    8349916: 'Iraq',
    8349917: 'Ireland',
    8349919: 'Israel',
    8068086: 'Italy',
    8068047: "Côte d'Ivoire / Ivory Coast",
    8349924: 'Kazakhstan ',
    8349922: 'Jordan',
    8349923: 'Kenya',
    8068160: 'South Korea / Republic of Korea',
    8349926: 'Kirkibati',
    8349925: 'Kuwait',
    8349928: 'Kyrgystan',
    8349921: 'Japan',
    8349920: 'Jamaica',
    8349927: 'Lao (or Laos)',
    8349929: 'Latvia',
    8349930: 'Lebanon',
    8349932: 'Lesotho',
    8349931: 'Liberia',
    8349934: 'Liechtenstein',
    8349933: 'Lybia',
    8349936: 'Lithuania',
    8349935: 'Luxembourg',
    8349940: 'Malawi',
    8349938: 'Macedonia',
    8349937: 'Madagascar',
    8349939: 'Malaysia',
    8349942: 'Maldives',
    8349941: 'Mali',
    8349943: 'Malta',
    8349945: 'Mauritania',
    8349946: 'Mauritius',
    8349948: 'Mexico',
    8349947: 'Micronesia',
    8349944: 'Marshall Islands',
    8349951: 'Mozambique',
    8349949: 'Moldova',
    8349950: 'Mongolia ',
    8349953: 'Myanmar (Burma)',
    8349952: 'Namibia',
    8349955: 'Nauru',
    8349954: 'Nepal',
    8349957: 'New Zealand',
    8349956: 'The Netherlands',
    8349958: 'Nicaragua',
    8349960: 'Niger',
    8349959: 'Nigeria',
    8349961: 'Pakistan',
    8349962: 'Norway',
    8349963: 'Palau',
    8349964: 'Panama',
    8349965: 'Papua New Guinea',
    8349966: 'Peru',
    8349967: 'Philippines',
    8349968: 'Poland',
    8349970: 'Portugal',
    8349969: 'Puerto Rico (US dependency)',
    8349971: 'Quatar',
    8349972: 'Romania',
    8349974: 'Russia',
    8349973: 'Rwanda',
    8349975: 'Saint Kitts and Nevis',
    8349976: 'Saint Lucia',
    8349977: 'Saint Vincent and the Grenadines',
    8349979: 'Samoa',
    8349981: 'São Tomé and Príncipe',
    8349978: 'San Marino',
    8349980: 'Saudi Arabia',
    8349982: 'Serbia',
    8349983: 'Senegal',
    8349984: 'Seychelles',
    8349987: 'Singapore',
    8349985: 'Sierra Leone',
    8349986: 'Slovakia',
    8349988: 'Slovenia',
    8349989: 'Solomon Islands',
    8349991: 'Somalia',
    8349990: 'South Africa',
    8349992: 'South Korea / Republic of Korea',
    8349993: 'South Sudan',
    8349995: 'Spain',
    8349994: 'Sri Lanka',
    8349996: 'Sudan',
    8349997: 'Suriname',
    8349998: 'Swaziland / Eswatini',
    8349999: 'Sweden',
    8350000: 'Switzerland',
    8350002: 'Syria',
    8350001: 'Taiwan',
    8350004: 'Tajikistan',
    8350005: 'Thailand',
    8350003: 'Tanzania',
    8350006: 'Timor-Leste',
    8350007: 'Togo',
    8350008: 'Tonga',
    8350010: 'Trinidad and Tobago',
    8350009: 'Tunisia',
    8350011: 'Turkey',
    8350012: 'Turkmenistan',
    8350013: 'Tuvalu',
    8350015: 'Uganda',
    8350014: 'Ukraine',
    8350016: 'United Arab Emirates',
    8350017: 'Uruguay',
    8350018: 'Uzbekistan',
    8350019: 'Vanuatu',
    8350020: 'Venezuela',
    8350021: 'Vietnam',
    8350022: 'West Indies (Use for Caribbean colonial dependencies)',
    8350023: 'Yemen',
    8350024: 'Zambia',
    8350025: 'Zimbabwe',

    # not done yet for mh
    8068008: 'England',
    8068010: 'Scotland',
    8068009: 'Northern Ireland',
    8068011: 'Wales',
}]


# 1
""" edu_setting_CEDIL = [{  # What is the educational setting (Select ALL that apply)
    8068199: 'Nursery school/pre-school',
    8068200: 'Primary/elementary school',
    8068201: 'Middle school',
    8068202: 'Secondary/High school',
    8068203: 'Residential/boarding school',
    8068204: 'Independent/private school',
    8068205: 'Home',
    8068207: 'Other educational setting (please specify)',
    8068208: 'Outdoor adventure setting',
    8068206: 'Further education/junior or community college',
    8068209: 'No information provided'
}] """

# 2
edu_setting_CEDIL = [{  # What is the educational setting (Select ALL that apply)
    8350031: 'Nursery school/pre-school',
    8350032: 'Primary/elementary school',
    8350033: 'Middle school',
    8350034: 'Secondary/High school',
    8350035: 'Residential/boarding school',
    8350036: 'Independent/private school',
    8350037: 'Home',
    8350039: 'Other educational setting (please specify)',
    8350040: 'Outdoor adventure setting',
    8350038: 'Further education/junior or community college',
    8350041: 'No information provided'
}]


# 1
""" study_realism_CEDIL = [{  # How realistic was the study?
    8068002: 'High ecological validity',
    8068003: 'Low ecological validity',
    8068004: 'Unclear'
}] """

# 2
study_realism_CEDIL = [{  # How realistic was the study?
    8349834: 'High ecological validity',
    8349835: 'Low ecological validity',
    8349836: 'Unclear'
}]


# 1
""" student_age_CEDIL = [{  
    # What is the age of the students? (Select ALL that apply)
    8068218: '3',
    8068219: '4',
    8068220: '5',
    8068221: '6',
    8068222: '7',
    8068223: '8',
    8068224: '9',
    8068225: '10',
    8068226: '11',
    8068227: '12',
    8068228: '13',
    8068229: '14',
    8068230: '15',
    8068231: '16',
    8068232: '17',
    8068233: '18',
    8068234: 'No information provided'
}] """

# 2
student_age_CEDIL = [{
    # What is the age of the students? (Select ALL that apply)
    8350050: '3',
    8350051: '4',
    8350052: '5',
    8350053: '6',
    8350054: '7',
    8350055: '8',
    8350056: '9',
    8350057: '10',
    8350058: '11',
    8350059: '12',
    8350060: '13',
    8350061: '14',
    8350062: '15',
    8350063: '16',
    8350064: '17',
    8350065: '18',
    8068234: 'No information provided'  # fix
}]


# 1
# NUMBER OF SCHOOLS
""" number_of_schools_intervention_CEDIL = [{  
    # What is the number of schools involved in the intervention group(s)?
    8934346: ''
}]

number_of_schools_control_CEDIL = [{  
    # What is the number of schools involved in the control or comparison group?
    8934347: ''
}]

number_of_schools_total_CEDIL = [{  
    # What is the total number of schools involved?
    8934348: ''
}]

number_of_schools_not_provided_CEDIL = [{  
    # Not provided/ unclear / not applicable
    8934349: 'not_provided'
}]

# NUMBER OF CLASSES
number_of_classes_intervention_CEDIL = [{  
    # What is the total number of classes involved in the intervention group?
    8934351: ''
}]

number_of_classes_control_CEDIL = [{  
    # What is the total number of classes involved in the control or comparison group?
    8934352: ''
}]

number_of_classes_total_CEDIL = [{  
    # What is the total number of classes involved?
    8934353: ''
}]

number_of_classes_not_provided_CEDIL = [{  
    # Not provided/ unclear / not applicable
    8934354: 'not_provided'
}] """

# 2
# NUMBER OF SCHOOLS
number_of_schools_intervention_CEDIL = [{
    # What is the number of schools involved in the intervention group(s)?
    9096538: ''
}]

number_of_schools_control_CEDIL = [{
    # What is the number of schools involved in the control or comparison group?
    9096539: ''
}]

number_of_schools_total_CEDIL = [{
    # What is the total number of schools involved?
    9096540: ''
}]

number_of_schools_not_provided_CEDIL = [{
    # Not provided/ unclear / not applicable
    9096541: 'not_provided'
}]

# NUMBER OF CLASSES
number_of_classes_intervention_CEDIL = [{
    # What is the total number of classes involved in the intervention group?
    9096543: ''
}]

number_of_classes_control_CEDIL = [{
    # What is the total number of classes involved in the control or comparison group?
    9096545: ''
}]

number_of_classes_total_CEDIL = [{
    # What is the total number of classes involved?
    9096545: ''
}]

number_of_classes_not_provided_CEDIL = [{
    # Not provided/ unclear / not applicable
    9096546: 'not_provided'
}]


# 1
treatment_group_CEDIL = [{
    # Is there more than one treatment group?
    8067982: "Yes (Please specify)",
    8067983: "No",
    8067984: "Not specified or N/A"
}]

# 2
treatment_group_CEDIL = [{
    # Is there more than one treatment group?
    8349814: "Yes (Please specify)",
    8349815: "No",
    8349816: "Not specified or N/A"
}]


# 1
participant_assignment_CEDIL = [{
    # How were participants assigned?
    8067986: 'Random (please specify)',
    8067987: 'Non-random, but matched',
    8067988: 'Non-random, not matched prior to treatment',
    8067989: 'Unclear',
    8067990: 'Not assigned - naturally occurring sample',
    8067991: 'Retrospective Quasi Experimental Design (QED)',
    8067992: 'Regression discontinuity'
}]

# 2
participant_assignment_CEDIL = [{
    # How were participants assigned?
    8349818: 'Random (please specify)',
    8349819: 'Non-random, but matched',
    8349820: 'Non-random, not matched prior to treatment',
    8349821: 'Unclear',
    8349822: 'Not assigned - naturally occurring sample',
    8349823: 'Retrospective Quasi Experimental Design (QED)',
    8349824: 'Regression discontinuity'
}]


# 1
""" level_of_assignment_CEDIL = [{  
    # What was the level of assignment?
    8067994: 'Individual',
    8067995: 'Class',
    8067996: 'School - cluster',
    8067997: 'School - multi-site',
    8067998: 'Region or district',
    8067999: 'Not provided/ not available',
    8068000: 'Not applicable',
}] """

# 2
level_of_assignment_CEDIL = [{
    # What was the level of assignment?
    8349826: 'Individual',
    8349827: 'Class',
    8349828: 'School - cluster',
    8349829: 'School - multi-site',
    8349830: 'Region or district',
    8349831: 'Not provided/ not available',
    8349832: 'Not applicable',
}]


# 1
""" study_design_CEDIL = [{  
    # What was the study design?
    8934336: 'Individual RCT',
    8934337: 'Cluster RCT',
    8934338: 'Multisite RCT',
    8934339: 'Prospective QED',
    8934340: 'Retrospective QED',
    8934341: 'Interrupted time series QED',
    8934342: 'Regression Discontinuity with randomisation',
    8934343: 'Regression Discontinuity - not randomised',
    8934344: 'Regression Continuity  - naturally occurring'
}] """

# 2
study_design_CEDIL = [{
    # What was the study design?
    9096528: 'Individual RCT',
    9096529: 'Cluster RCT',
    9096530: 'Multisite RCT',
    9096531: 'Prospective QED',
    9096532: 'Retrospective QED',
    9096533: 'Interrupted time series QED',
    9096534: 'Regression Discontinuity with randomisation',
    9096535: 'Regression Discontinuity - not randomised',
    9096536: 'Regression Continuity  - naturally occurring'
}]


# 1
""" randomisation_details_CEDIL = [{  
    # Are details of randomisation provided?
    8934356: "Yes",
    8934357: "Not applicable",
    8934358: "No/Unclear"
}] """

# 2
randomisation_details_CEDIL = [{
    # Are details of randomisation provided?
    9096548: "Yes",
    9096549: "Not applicable",
    9096550: "No/Unclear"
}]


# 1
""" other_outcomes_CEDIL = [{ 
    # In addition to the primary educational attainment outcome, are there other outcomes reported? 
    8068330: 'Yes',
    8068331: 'No'
}]    """

# 2
other_outcomes_CEDIL = [{
    # In addition to the primary educational attainment outcome, are there other outcomes reported?
    8350162: 'Yes',
    8350163: 'No'
}]


# 1
""" additional_outcomes_CEDIL = [{ 
    # If yes, which other outcomes are reported? 
    8068333: 'Cognitive outcomes measured (Please specify)',
    8068334: 'Other types of student outcomes (Please specify)',
}] """

# 2
additional_outcomes_CEDIL = [{
    # If yes, which other outcomes are reported?
    8350165: 'Cognitive outcomes measured (Please specify)',
    8350166: 'Other types of student outcomes (Please specify)',
}]


# 1
""" other_participants_CEDIL = [{ 
    # Other participants (i.e. not students) outcomes
    8068335: 'Other participants (i.e. not students) outcomes (Please specify)',
}] """

# 2
other_participants_CEDIL = [{
    # Other participants (i.e. not students) outcomes
    8350167: 'Other participants (i.e. not students) outcomes (Please specify)',
}]


# 1
""" intervention_name_CEDIL = [{  
    # "What is the intervention name?"
    8067978: ''
}]

intervention_description_CEDIL = [{  
    # How is the intervention described?
    8067979: ''
}]

intervention_objectives_CEDIL = [{  
    # What are the intervention objectives?
    8067980: ''
}] """

# 2
intervention_name_CEDIL = [{
    # "What is the intervention name?"
    8349810: ''
}]

intervention_description_CEDIL = [{
    # How is the intervention described?
    8349811: ''
}]

intervention_objectives_CEDIL = [{
    # What are the intervention objectives?
    8349812: ''
}]


# 1
""" intervention_training_provided_CEDIL = [{  
    # Was training for the intervention provided?
    8068248: "Yes (Please specify)",
    8068249: "No",
    8068250: "Unclear/ Not specified",
}] """

# 2
intervention_training_provided_CEDIL = [{
    # Was training for the intervention provided?
    8350080: "Yes (Please specify)",
    8350081: "No",
    8350082: "Unclear/ Not specified",
}]


# 1
""" intervention_organisation_type_CEDIL = [{  
    # What type of organisation was responsible for providing the intervention?
    8068241: "School or group of schools",
    8068242: "Charity or voluntary organisation",
    8068243: "University/ researcher design",
    8068244: "Local education authority or district",
    8068245: "Private or commercial company",
    8068246: "Other (please provide details)",
}] """

# 2
intervention_organisation_type_CEDIL = [{
    # What type of organisation was responsible for providing the intervention?
    8350073: "School or group of schools",
    8350074: "Charity or voluntary organisation",
    8350075: "University/ researcher design",
    8350076: "Local education authority or district",
    8350077: "Private or commercial company",
    8350078: "Other (please provide details)",
}]


# 1
""" intervention_focus_CEDIL = [{  
    # Who is the focus of the intervention? (Select ALL that apply)
    8068252: "Students",
    8068253: "Teachers",
    8068254: "Teaching assistants",
    8068255: "Other education practitioners",
    8068256: "Non-teaching staff",
    8068257: "Senior management",
    8068258: "Parents",
    8068259: "Other (Please specify)"
}] """

# 2
intervention_focus_CEDIL = [{
    # Who is the focus of the intervention? (Select ALL that apply)
    8350084: "Students",
    8350085: "Teachers",
    8350086: "Teaching assistants",
    8350087: "Other education practitioners",
    8350088: "Non-teaching staff",
    8350089: "Senior management",
    8350090: "Parents",
    8350091: "Other (Please specify)"
}]


# 1
""" intervention_teaching_approach_CEDIL = [{  
    # What is the intervention teaching approach? (Select ALL that apply)
    8068261: "Large group/class teaching (+6)",
    8068262: "Small group/intensive support (3-5)",
    8068263: "Paired learning",
    8068264: "One to one",
    8068265: "Student alone (self-administered)",
    8068266: "Other (Explain in notes)"
}] """

# 2
intervention_teaching_approach_CEDIL = [{
    # What is the intervention teaching approach? (Select ALL that apply)
    8350093: "Large group/class teaching (+6)",
    8350094: "Small group/intensive support (3-5)",
    8350095: "Paired learning",
    8350096: "One to one",
    8350097: "Student alone (self-administered)",
    8350098: "Other (Explain in notes)"
}]


# 1
# intervention approach inclusion
""" intervention_approach_digital_technology_CEDIL = [{  
    # Were any of the following involved in the intervention or approach?
    # Digital Technology
    8068269: "Yes",
    8068270: "No"
}] """

# 2
intervention_approach_digital_technology_CEDIL = [{
    # Were any of the following involved in the intervention or approach?
    # Digital Technology
    8350101: "Yes",
    8350102: "No"
}]


# 1
""" intervention_approach_parents_or_community_volunteers_CEDIL = [{  
    # Were any of the following involved in the intervention or approach?
    # Parents or community volunteers
    8068272: "Yes",
    8068273: "No"
}] """

# 2
intervention_approach_parents_or_community_volunteers_CEDIL = [{
    # Were any of the following involved in the intervention or approach?
    # Parents or community volunteers
    8350104: "Yes",
    8350105: "No"
}]


# 1
""" intervention_time_CEDIL = [{  
    # When did the intervention take place?  (Select ALL that apply)
    8068275: "During regular school hours ",
    8068276: "Before/after school",
    8068277: "Evenings and/or weekends",
    8068278: "Summer/ holiday period",
    8068279: "Other (please specify)",
    8068280: "Unclear/ not specified"
}] """

# 2
intervention_time_CEDIL = [{
    # When did the intervention take place?  (Select ALL that apply)
    8350107: "During regular school hours ",
    8350108: "Before/after school",
    8350109: "Evenings and/or weekends",
    8350110: "Summer/ holiday period",
    8350111: "Other (please specify)",
    8350112: "Unclear/ not specified"
}]


# 1
""" intervention_delivery_CEDIL = [{  
    # Who was responsible for the teaching at the point of delivery? (Select ALL that apply)
    8068282: "Research staff",
    8068283: "Class teachers",
    8068284: "Teaching assistants",
    8068285: "Other school staff",
    8068286: "External teachers",
    8068287: "Parents/carers",
    8068288: "Lay persons/volunteers",
    8068289: "Peers",
    8068290: "Digital technology",
    8068291: "Unclear/not specified"
}] """

# 2
intervention_delivery_CEDIL = [{
    # Who was responsible for the teaching at the point of delivery? (Select ALL that apply)
    8350114: "Research staff",
    8350115: "Class teachers",
    8350116: "Teaching assistants",
    8350117: "Other school staff",
    8350118: "External teachers",
    8350119: "Parents/carers",
    8350120: "Lay persons/volunteers",
    8350121: "Peers",
    8350122: "Digital technology",
    8350123: "Unclear/not specified"
}]


# 1
""" intervention_duration_CEDIL = [{  
    # What was the duration of the intervention? (Please add to info box and specify units)
    8068292: ''
}]

intervention_frequency_CEDIL = [{  
    # What was the frequency of the intervention?
    8068293: ''
}]

intervention_session_length_CEDIL = [{  
    # What is the length of intervention sessions?
    8068294: ''
}] """

# 2
intervention_duration_CEDIL = [{
    # What was the duration of the intervention? (Please add to info box and specify units)
    8350124: ''
}]

intervention_frequency_CEDIL = [{
    # What was the frequency of the intervention?
    8350125: ''
}]

intervention_session_length_CEDIL = [{
    # What is the length of intervention sessions?
    8350126: ''
}]


# 1
""" intervention_implementation_details_CEDIL = [{ 
    # Are implementation details and/or fidelity details provided?
    8068296: "Qualitative",
    8068297: "Quantitative",
    8068298: "No implementation details provided."
}]

intervention_costs_reported_CEDIL = [{ 
    # Are the costs reported?
    8068300: "Yes (Please add details)",
    8068301: "No"
}]

intervention_evaluation_CEDIL = [{ 
    # Who undertook the outcome evaluation?
    8068303: "The developer",
    8068304: "A different organization paid by developer",
    8068305: "An organization commissioned independently to evaluate",
    8068306: "Unclear/not stated",
    8068307: "Is this an EEF evaluation?"
}]

baseline_differences_CEDIL = [{  
    # Does the study report any group differences at baseline?
    8934366: 'No/Unclear',
    8934365: 'Yes'
}]

comparability_CEDIL = [{  
    # Is comparability taken into account in the analysis?
    8934370: 'Unclear or details not provided',
    8934368: 'Yes',
    8934369: 'No'
}]

comparabiltiy_vars_reported_CEDIL = [{  
    # Are the variables used for comparability reported?"
    8934377: 'Yes',
    8934378: 'No',
    8934379: 'N/A'
}] """

# 2
intervention_implementation_details_CEDIL = [{
    # Are implementation details and/or fidelity details provided?
    8350128: "Qualitative",
    8350129: "Quantitative",
    8350130: "No implementation details provided."
}]

intervention_costs_reported_CEDIL = [{
    # Are the costs reported?
    8350132: "Yes (Please add details)",
    8350133: "No"
}]

intervention_evaluation_CEDIL = [{
    # Who undertook the outcome evaluation?
    8350135: "The developer",
    8350136: "A different organization paid by developer",
    8350137: "An organization commissioned independently to evaluate",
    8350138: "Unclear/not stated",
    8350139: "Is this an EEF evaluation?"
}]

baseline_differences_CEDIL = [{
    # Does the study report any group differences at baseline?
    9096558: 'No/Unclear',
    9096557: 'Yes'
}]

comparability_CEDIL = [{
    # Is comparability taken into account in the analysis?
    9096562: 'Unclear or details not provided',
    9096560: 'Yes',
    9096561: 'No'
}]

comparabiltiy_vars_reported_CEDIL = [{
    # Are the variables used for comparability reported?"
    9096569: 'Yes',
    9096570: 'No',
    9096571: 'N/A'
}]


# 1
""" if_yes_which_comparability_variables_reported_CEDIL = [{  
    # If yes, which variables are used for comparability?
    8934381: 'Educational attainment',
    8934382: 'Gender',
    8934383: 'Socio-economic status',
    8934384: 'Special educational needs',
    8934385: 'Other (please specify)'
}]

clustering_CEDIL = [{  
    # Is clustering accounted for in the analysis?
    8934388: "Yes",
    8934389: "No",
    8934390: "Unclear"
}] """

# 2

if_yes_which_comparability_variables_reported_CEDIL = [{
    # If yes, which variables are used for comparability?
    9096573: 'Educational attainment',
    9096574: 'Gender',
    9096575: 'Socio-economic status',
    9096576: 'Special educational needs',
    9096577: 'Other (please specify)'
}]

clustering_CEDIL = [{
    # Is clustering accounted for in the analysis?
    9096580: "Yes",
    9096581: "No",
    9096582: "Unclear"
}]


# 1
""" # SAMPLE SIZE
sample_size_CEDIL = [{  
    # What is the overall sample analysed?
    8068211: ''
}]

student_gender_CEDIL = [{  
    # What is the gender of the students?
    8068213: 'Female only',
    8068214: 'Male only',
    8068215: 'Mixed gender',
    8068216: 'No information provided'
}]

# PROPORTION LOW SES/FSM STUDENTS IN SAMPLE
proportion_low_fsm_CEDIL = [{  
    # What is the proportion of low SES/FSM students in the sample?
    8068235: ''
}]

# PERCENTAGE LOW SES_FSM STUDENTS IN SAMPLE
percentage_low_fsm_CEDIL = [{  
    # FSM or low SES student percentage
    8068236: ''
}]

# FURTHER SES/FSM INFORMATION IN SAMPLE
further_ses_fsm_info_CEDIL = [{  
    # Further information about FSM or SES in the study sample.
    8068237: ''
}]

# NO SES/FSM INFO PROVIDED
no_ses_fsm_info_provided_CEDIL = [{  
    # No SES/FSM information provided
    8068238: 'No SES/FSM Information Provided'
}]

sample_size_intervention_CEDIL = [{  
    # What is the sample size for the intervention group?
    8934360: ''
}] """

# 2
# SAMPLE SIZE
sample_size_CEDIL = [{
    # What is the overall sample analysed?
    8350043: ''
}]

student_gender_CEDIL = [{
    # What is the gender of the students?
    8350045: 'Female only',
    8350046: 'Male only',
    8350047: 'Mixed gender',
    8350048: 'No information provided'
}]

# PROPORTION LOW SES/FSM STUDENTS IN SAMPLE
proportion_low_fsm_CEDIL = [{
    # What is the proportion of low SES/FSM students in the sample?
    8350067: ''
}]

# PERCENTAGE LOW SES_FSM STUDENTS IN SAMPLE
percentage_low_fsm_CEDIL = [{
    # FSM or low SES student percentage
    8350068: ''
}]

# FURTHER SES/FSM INFORMATION IN SAMPLE
further_ses_fsm_info_CEDIL = [{
    # Further information about FSM or SES in the study sample.
    8350069: ''
}]

# NO SES/FSM INFO PROVIDED
no_ses_fsm_info_provided_CEDIL = [{
    # No SES/FSM information provided
    8350070: 'No SES/FSM Information Provided'
}]

sample_size_intervention_CEDIL = [{
    # What is the sample size for the intervention group?
    9096552: ''
}]


# 1
""" sample_size_control_CEDIL = [{  
    # What is the sample size for the control group?
    8934361: ''
}]

sample_size_second_intervention_CEDIL = [{  
    # *What is the sample size for the second intervention group?}
    8934362: ''
}]

sample_size_third_intervention_CEDIL = [{  
    # *What is the sample size for the third intervention group?}
    8934363: ''
}]

sample_size_analyzed_intervention_CEDIL = [{  
    # intervention group Number (n)
    5406980: ''
}]

sample_size_analyzed_control_CEDIL = [{  
    # control* group Number (n}
    8934408: ''
}]

sample_size_analyzed_second_intervention_CEDIL = [{  
    # If yes, please add for a second intervention* group (if needed)
    8934417: ''
}]

sample_size_analyzed_second_control_CEDIL = [{  
    # If needed, please add for the control group
    8934426: ''
}]

attrition_dropout_reported_CEDIL = [{ 
     # Is attrition or drop out reported?
    8934372: 'Yes',
    8934373: 'No',
    8934374: 'Unclear (please add notes)'
}] """

# 2
sample_size_control_CEDIL = [{
    # What is the sample size for the control group?
    9096553: ''
}]

sample_size_second_intervention_CEDIL = [{
    # *What is the sample size for the second intervention group?}
    9096554: ''
}]

sample_size_third_intervention_CEDIL = [{
    # *What is the sample size for the third intervention group?}
    9096555: ''
}]

sample_size_analyzed_intervention_CEDIL = [{
    # intervention group Number (n)
    5406980: ''
}]

sample_size_analyzed_control_CEDIL = [{
    # control* group Number (n}
    8934408: ''
}]

sample_size_analyzed_second_intervention_CEDIL = [{
    # If yes, please add for a second intervention* group (if needed)
    8934417: ''
}]

sample_size_analyzed_second_control_CEDIL = [{
    # If needed, please add for the control group
    8934426: ''
}]

attrition_dropout_reported_CEDIL = [{
    # Is attrition or drop out reported?
    9096564: 'Yes',
    9096565: 'No',
    9096566: 'Unclear (please add notes)'
}]


# 1
""" treatment_group_attrition_CEDIL = [{  
    # What is the attrition in the treatment group?
    8934375: ''
}]

overall_percent_attrition_CEDIL = [{  
    # What is the total or overall percentage attrition?
    8934386: ''
}]

desc_stats_primary_CEDIL = [{  
    # Are descriptive statistics reported for the primary outcome?
    8934397: "Yes",
    8934452: "No"
}]

intervention_group_number_CEDIL = [{  
    # intervention group Number (n}
    8934399: ''
}]

intervention_group_pretest_mean_CEDIL = [{  
    # intervention group Pre-test mean
    8934400: ''
}]

intervention_group_pretest_sd_CEDIL = [{  
    # intervention* group Pre-test SD
    8934401: ''
}]

intervention_group_posttest_mean_CEDIL = [{  
    # intervention* group Post-test mean
    8934402: ''
}]

intervention_group_posttest_sd_CEDIL = [{ 
    # intervention* group Post-test SD
    8934403: ''
}]

intervention_group_gain_score_mean_CEDIL = [{  
    # intervention gain score mean
    8934404: ''
}] """

# 2
treatment_group_attrition_CEDIL = [{
    # What is the attrition in the treatment group?
    9096567: ''
}]

overall_percent_attrition_CEDIL = [{
    # What is the total or overall percentage attrition?
    9096578: ''
}]

desc_stats_primary_CEDIL = [{
    # Are descriptive statistics reported for the primary outcome?
    9096589: "Yes",
    9096644: "No"
}]

intervention_group_number_CEDIL = [{
    # intervention group Number (n}
    9096591: ''
}]

intervention_group_pretest_mean_CEDIL = [{
    # intervention group Pre-test mean
    9096592: ''
}]

intervention_group_pretest_sd_CEDIL = [{
    # intervention* group Pre-test SD
    9096593: ''
}]

intervention_group_posttest_mean_CEDIL = [{
    # intervention* group Post-test mean
    9096594: ''
}]

intervention_group_posttest_sd_CEDIL = [{
    # intervention* group Post-test SD
    9096595: ''
}]

intervention_group_gain_score_mean_CEDIL = [{
    # intervention gain score mean
    9096596: ''
}]


# 1
""" intervention_group_gain_score_sd_CEDIL = [{ 
     # intervention gain score sd
    8934405: ''
}]

intervention_group_any_other_info_CEDIL = [{  
    # intervention -  any other info}]
    8934406: ''
}]

control_group_number_CEDIL = [{  
    # control* group Number (n}
    8934408: ''
}]

control_group_pretest_mean_CEDIL = [{  
    # control group Pre-test mean
    8934409: ''
}]

control_group_pretest_sd_CEDIL = [{  
    # control group Pre-test SD
    8934410: ''
}]

control_group_posttest_mean_CEDIL = [{  
    # control group Post-test mean
    8934411: ''
}]

control_group_posttest_sd_CEDIL = [{  
    # control group Post-test SD
    8934412: ''
}]

control_group_gain_score_mean_CEDIL = [{ 
     # control gain score mean
    8934413: ''
}]

control_group_gain_score_sd_CEDIL = [{  
    # control gain score sd
    8934414: ''
}] """

# 2
intervention_group_gain_score_sd_CEDIL = [{
    # intervention gain score sd
    9096597: ''
}]

intervention_group_any_other_info_CEDIL = [{
    # intervention -  any other info}]
    9096598: ''
}]

control_group_number_CEDIL = [{
    # control* group Number (n}
    9096600: ''
}]

control_group_pretest_mean_CEDIL = [{
    # control group Pre-test mean
    9096601: ''
}]

control_group_pretest_sd_CEDIL = [{
    # control group Pre-test SD
    9096602: ''
}]

control_group_posttest_mean_CEDIL = [{
    # control group Post-test mean
    9096603: ''
}]

control_group_posttest_sd_CEDIL = [{
    # control group Post-test SD
    9096604: ''
}]

control_group_gain_score_mean_CEDIL = [{
    # control gain score mean
    9096605: ''
}]

control_group_gain_score_sd_CEDIL = [{
    # control gain score sd
    9096606: ''
}]


# 1
""" control_group_any_other_info_CEDIL = [{  
    # control -  any other info}]
    8934415: ''
}]

follow_up_data_reported_CEDIL = [{  
    # Is there follow up data?
    8934454: 'Yes',
    8934455: 'No'
}]

intervention_group_two_number_CEDIL = [{  
    # intervention group Number (n}
    8934417: ''
}]

intervention_group_two_pretest_mean_CEDIL = [{  
    # intervention group Pre-test mean
    8934418: ''
}]

intervention_group_two_pretest_sd_CEDIL = [{  
    # intervention* group Pre-test SD
    8934419: ''
}]

intervention_group_two_posttest_mean_CEDIL = [{  
    # intervention* group Post-test mean
    8934420: ''
}]

intervention_group_two_posttest_sd_CEDIL = [{  
    # intervention* group Post-test SD
    8934421: ''
}]

intervention_group_two_gain_score_mean_CEDIL = [{  
    # intervention gain score mean
    8934422: ''
}]

intervention_group_two_gain_score_sd_CEDIL = [{  
    # intervention gain score sd
    8934423: ''
}] """

# 2
control_group_any_other_info_CEDIL = [{
    # control -  any other info}]
    9096607: ''
}]

follow_up_data_reported_CEDIL = [{
    # Is there follow up data?
    8934454: 'Yes',
    8934455: 'No'
}]

intervention_group_two_number_CEDIL = [{
    # intervention group Number (n}
    9096609: ''
}]

intervention_group_two_pretest_mean_CEDIL = [{
    # intervention group Pre-test mean
    9096610: ''
}]

intervention_group_two_pretest_sd_CEDIL = [{
    # intervention* group Pre-test SD
    9096611: ''
}]

intervention_group_two_posttest_mean_CEDIL = [{
    # intervention* group Post-test mean
    9096612: ''
}]

intervention_group_two_posttest_sd_CEDIL = [{
    # intervention* group Post-test SD
    9096613: ''
}]

intervention_group_two_gain_score_mean_CEDIL = [{
    # intervention gain score mean
    9096614: ''
}]

intervention_group_two_gain_score_sd_CEDIL = [{
    # intervention gain score sd
    9096615: ''
}]


# 1
""" intervention_group_two_any_other_info_CEDIL = [{  
    # intervention -  any other info}]
    8934424: ''
}]

control_group_two_number_CEDIL = [{  
    # control* group Number (n}
    8934426: ''
}]

control_group_two_pretest_mean_CEDIL = [{  
    # control group Pre-test mean
    8934427: ''
}]

control_group_two_pretest_sd_CEDIL = [{  
    # control group Pre-test SD
    8934428: ''
}]

control_group_two_posttest_mean_CEDIL = [{  
    # control group Post-test mean
    8934429: ''
}]

control_group_two_posttest_sd_CEDIL = [{  
    # control group Post-test SD
    8934430: ''
}]

control_group_two_gain_score_mean_CEDIL = [{  
    # control gain score mean
    8934431: ''
}]

control_group_two_gain_score_sd_CEDIL = [{  
    # control gain score sd
    8934432: ''
}]

control_group_two_any_other_info_CEDIL = [{  
    # control -  any other info}]
    8934433: ''
}] """

# 2
intervention_group_two_any_other_info_CEDIL = [{
    # intervention -  any other info}]
    9096616: ''
}]

control_group_two_number_CEDIL = [{
    # control* group Number (n}
    9096618: ''
}]

control_group_two_pretest_mean_CEDIL = [{
    # control group Pre-test mean
    9096619: ''
}]

control_group_two_pretest_sd_CEDIL = [{
    # control group Pre-test SD
    9096620: ''
}]

control_group_two_posttest_mean_CEDIL = [{
    # control group Post-test mean
    9096621: ''
}]

control_group_two_posttest_sd_CEDIL = [{
    # control group Post-test SD
    9096622: ''
}]

control_group_two_gain_score_mean_CEDIL = [{
    # control gain score mean
    9096623: ''
}]

control_group_two_gain_score_sd_CEDIL = [{
    # control gain score sd
    9096624: ''
}]

control_group_two_any_other_info_CEDIL = [{
    # control -  any other info}]
    9096625: ''
}]


# 1
""" follow_up_data_reported_CEDIL = [{  
    # Is there follow up data?
    8934454: 'Yes',
    8934455: 'No'
}]

outcome_type_CEDIL = [{  # Outcome type (select all that apply)
    8934475: "Toolkit primary outcome",
    8934476: "Reading primary outcome",
    8934477: "Writing and spelling primary outcome.",
    8934478: "Mathematics primary outcome",
    8934479: "Science primary outcome",
    8934480: "Other outcome"
}]

sample_CEDIL = [{  
    # Sample (select one from this group)
    8934458: 'Sample: All',
    8934459: 'Sample: Exceptional',
    8934460: 'Sample: High achievers',
    8934461: 'Sample: Average',
    8934462: 'Sample: Low achievers'
}]

effect_size_type_CEDIL = [{  
    # Effect size calculation (select one from this group)
    8934470: 'Post-test unadjusted (select one from this group)',
    8934471: 'Post-test adjusted for baseline attainment',
    8934472: 'Post-test adjusted for baseline attainment AND clustering',
    8934473: 'Pre-post gain'
}]

test_type_main_CEDIL = [{  
    # What kind of tests were used? (Select ALL that apply)
    8068310: 'Standardised test',
    8068311: 'Researcher developed test',
    8068312: 'School-developed test',
    8068313: 'National test or examination',
    8068314: 'International tests'
}] """

# 2
follow_up_data_reported_CEDIL = [{
    # Is there follow up data?
    9096646: 'Yes',
    9096647: 'No'
}]

""" outcome_type_codes = [{  # Outcome type (select all that apply)
    9096667: "Toolkit primary outcome",
    9096668: "Reading primary outcome",
    9096669: "Writing and spelling primary outcome.",
    9096670: "Mathematics primary outcome",
    9096671: "Science primary outcome",
    9096672: "Other outcome"
}] """

sample_CEDIL = [{
    # Sample (select one from this group)
    9096650: 'Sample: All',
    9096651: 'Sample: Exceptional',
    9096652: 'Sample: High achievers',
    9096653: 'Sample: Average',
    9096654: 'Sample: Low achievers'
}]

effect_size_type_CEDIL = [{
    # Effect size calculation (select one from this group)
    9096662: 'Post-test unadjusted (select one from this group)',
    9096663: 'Post-test adjusted for baseline attainment',
    9096664: 'Post-test adjusted for baseline attainment AND clustering',
    9096665: 'Pre-post gain'
}]

test_type_main_CEDIL = [{
    # What kind of tests were used? (Select ALL that apply)
    9096656: 'Standardised test',
    9096657: 'Researcher developed test',
    9096659: 'School-developed test',
    9096658: 'National test or examination',
    9096660: 'International tests'
}]


# 1
""" test_type_CEDIL = [{  
    # Test type (select one from this group)
    8934464: 'Test type: Standardised test ',
    8934465: 'Test type: Researcher developed test',
    8934466: 'Test type: National test',
    8934467: 'Test type: School-developed test',
    8934468: 'Test type: International tests'
}] """

# 2
test_type_CEDIL = [{
    # Test type (select one from this group)
    8934464: 'Test type: Standardised test ',
    8934465: 'Test type: Researcher developed test',
    8934466: 'Test type: National test',
    8934467: 'Test type: School-developed test',
    8934468: 'Test type: International tests',
}]


# CEDIL UNIQUE OPTIONS

""" out_edu_CEDIL = [{  
    # Are there any additional educational outcomes reported?
    8350375: 'Yes',
    8934743: 'No',
}] """

out_edu_CEDIL = [{
    # Are there any additional educational outcomes reported?
    8934742: 'Yes',
    8350376: 'No',
}]

""" out_edu_type_CEDIL = [{  
    # Test type (select one from this group)
    8934745: 'Enrolment',
    8934746: 'Return to education',
    8934747: 'Attendance',
    8934748: 'Absenteeism',
    8934749: 'Time in school',
    8934750: 'Drop-out',
    8934751: 'Pupil retention',
    8934752: 'Grade completion',
    8934753: 'School graduation',
    8934754: 'Next grade progression',
    8934755: 'Grade repetition',
    8934756: 'Other',
    8934757: 'None reported',
}] """

out_edu_type_CEDIL = [{
    # Test type (select one from this group)
    8350378: 'Enrolment',
    8350379: 'Return to education',
    8350380: 'Attendance',
    8350381: 'Absenteeism',
    8350382: 'Time in school',
    8350383: 'Drop-out',
    8350384: 'Pupil retention',
    8350385: 'Grade completion',
    8350386: 'School graduation',
    8350387: 'Next grade progression',
    8350388: 'Grade repetition',
    8350389: 'Other',
    8350390: 'None reported',
}]

""" sch_complete_level_CEDIL = [{
    # School Completion Level
    8934759: 'Early childhood education (ISCED Level 0)',
    8934760: 'Primary education (ISCED Level 1)',
    8934761: 'Lower secondary education (ISCED Level 2)',
    8934762: 'Upper secondary education (ISCED level 3)',
    8934763: 'Secondary education (ISCED levels 2 and 3)',
}] """

sch_complete_level_CEDIL = [{
    # School Completion Level
    8350392: 'Early childhood education (ISCED Level 0)',
    8350393: 'Primary education (ISCED Level 1)',
    8350394: 'Lower secondary education (ISCED Level 2)',
    8350395: 'Upper secondary education (ISCED level 3)',
    8350396: 'Secondary education (ISCED levels 2 and 3)',
}]

""" out_unders_pop_CEDIL = [{
    # Are outcomes reported for underserved populations?
    8934767: 'Yes',
    8934768: 'No',
}] """

out_unders_pop_CEDIL = [{
    # Are outcomes reported for underserved populations?
    8350400: 'Yes',
    8350401: 'No',
}]

""" out_unders_type_CEDIL = [{
    # Underserved outcome (open answers: HT)
    8934769: "",
}] """

out_unders_type_CEDIL = [{
    # Underserved outcome (open answers: HT)
    8350402: "",
}]

out_teach_CEDIL = [{
    # Are outcomes reported for teachers?
    8934772: 'Yes',
    8934773: 'No',
}]

out_teach_CEDIL = [{
    # Are outcomes reported for teachers?
    8350405: 'Yes',
    8350406: 'No',
}]

""" out_teach_type_CEDIL = [{
    # What teacher outcomes are reported?
    8934775: 'Attendance',
    8934776: 'Performance',
    8934777: 'Other',
    8934778: 'None reported',
}] """

out_teach_type_CEDIL = [{
    # What teacher outcomes are reported?
    8350408: 'Attendance',
    8350409: 'Performance',
    8350410: 'Other',
    8350411: 'None reported',
}]


""" follow_up_CEDIL = [{
    # Is there follow up data?
    8934782: 'Yes',
    8934783: 'No',
}] """

follow_up_CEDIL = [{
    # Is there follow up data?
    8350415: 'Yes',
    8350416: 'No',
}]

""" out_out_type_CEDIL = [{
    # Outcome classification: Outcome type
    8934808: 'School enrolment outcome', #
    8934809: 'Return to education outcome', #
    8934810: 'Attendance outcome', #
    8934811: 'Absence outcome', #
    8934812: 'Time in school outcome',
    8934813: 'Drop-out outcome', #
    8934814: 'Retention outcome', #
    8934815: 'Grade completion outcome', #
    8934816: 'School completion outcome', #
    8934817: 'Next grade outcome',#
    8934818: 'Grade repetition outcome',#
    8934819: 'Other outcome',
}]
 """
out_out_type_CEDIL = [{
    # Outcome classification: Outcome type
    8350439: 'School enrolment outcome',
    8350440: 'Return to education outcome',
    8350441: 'Attendance outcome',
    8350442: 'Absence outcome',
    8350443: 'Time in school outcome',
    8350444: 'Drop-out outcome',
    8350445: 'Retention outcome',
    8350446: 'Grade completion outcome',
    8350447: 'School completion outcome',
    8350448: 'Next grade outcome',
    8350449: 'Grade repetition outcome',
    8350450: 'Other outcome',
}]

""" toolkit_strand_CEDIL = [{  
    # Toolkit strand(s) (select at least one Toolkit strand)
    8934482: 'Toolkit: Arts participation ',
    8934483: 'Toolkit: Aspiration interventions',
    8934484: 'Toolkit: Behaviour interventions',
    8934485: 'Toolkit: Block scheduling',
    8934486: 'Toolkit: Built environment',
    8934487: 'Toolkit: Collaborative learning',
    8934488: 'Toolkit: Digital technology',
    8934489: 'Toolkit: Early years intervention',
    8934490: 'Toolkit: Extending school time',
    8934491: 'Toolkit: Feedback',
    8934492: 'Toolkit: Homework',
    8934493: 'Toolkit: Individualised instruction',
    8934494: 'Toolkit: Learning styles',
    8934495: 'Toolkit: Mastery learning',
    8934496: 'Toolkit: Metacognition and self-regulation',
    8934497: 'Toolkit: Mentoring',
    8934498: 'Toolkit: One to one tuition',
    8934499: 'Toolkit: Oral language interventions',
    8934500: 'Toolkit: Outdoor adventure learning',
    8934501: 'Toolkit: Parental engagement',
    8934502: 'Toolkit: Peer Tutoring',
    8934503: 'Toolkit: Performance pay',
    8934378: 'Toolkit: Phonics',
    8934505: 'Toolkit: Reading comprehension strategies',
    8934506: 'Toolkit: Reducing class size',
    8934507: 'Toolkit: Repeating a year',
    8934508: 'Toolkit: School uniform',
    8934509: 'Toolkit: Setting or streaming',
    8934510: 'Toolkit: Small Group Tuition',
    8934511: 'Toolkit: Social and emotional learning',
    8934512: 'Toolkit: Sports participation',
    8934387: 'Toolkit: Summer schools',
    8934514: 'Toolkit: Teaching assistants',
    8934515: 'Toolkit: Within-class attainment grouping',
    8990094: 'CEDIL: Cash Transfer',
}] """

toolkit_strand_CEDIL = [{
    # Toolkit strand(s) (select at least one Toolkit strand)
    8350452: 'Toolkit: Arts participation ',
    8350453: 'Toolkit: Aspiration interventions',
    8350454: 'Toolkit: Behaviour interventions',
    8350455: 'Toolkit: Block scheduling',
    8350456: 'Toolkit: Built environment',
    8350457: 'Toolkit: Collaborative learning',
    8350458: 'Toolkit: Digital technology',
    8350459: 'Toolkit: Early years intervention',
    8350460: 'Toolkit: Extending school time',
    8350461: 'Toolkit: Feedback',
    8350462: 'Toolkit: Homework',
    8350463: 'Toolkit: Individualised instruction',
    8350464: 'Toolkit: Learning styles',
    8350465: 'Toolkit: Mastery learning',
    8350466: 'Toolkit: Metacognition and self-regulation',
    8350467: 'Toolkit: Mentoring',
    8350468: 'Toolkit: One to one tuition',
    8350469: 'Toolkit: Oral language interventions',
    8350470: 'Toolkit: Outdoor adventure learning',
    8350471: 'Toolkit: Parental engagement',
    8350472: 'Toolkit: Peer Tutoring',
    8350473: 'Toolkit: Performance pay',
    8350474: 'Toolkit: Phonics',
    8350475: 'Toolkit: Reading comprehension strategies',
    8350476: 'Toolkit: Reducing class size',
    8350477: 'Toolkit: Repeating a year',
    8350478: 'Toolkit: School uniform',
    8350479: 'Toolkit: Setting or streaming',
    8350480: 'Toolkit: Small Group Tuition',
    8350481: 'Toolkit: Social and emotional learning',
    8350482: 'Toolkit: Sports participation',
    8350483: 'Toolkit: Summer schools',
    8350484: 'Toolkit: Teaching assistants',
    8934515: 'Toolkit: Within-class attainment grouping',
    8350485: 'CEDIL: Cash Transfer',
    8350486: "CEDIL: Menstrual Hygiene Intervention",
    8350487: "CEDIL: Corporal Punishment",
}]


#############################################
# CEDIL CASH TRANSFER STRAND SPECIFIC CODING
############################################

school_target_CEDIL = [{
    # School target of cash transfer program
    8934879: "Nursery/Kindergarten",
    8934880: "Primary only",
    8934881: "Secondary only",
    8934882: "Primary and secondary",
    8935024: "Other",
    8934883: "Not reported/Unclear",
}]

eligibility_CEDIL = [{
    # Eligibility for cash transfer program
    8934885: "Village/neighbourhood income",
    8934886: "Household income",
    8934887: "Targeted population (please provide details in info box)",
    8934888: "Not reported/Unclear",
    8935025: "Other",
}]

elig_targeted_population_CEDIL = [{
    # option from 'eligibility_CEDIL', 'info' column
    8934887: '',
}]

means_tested_CEDIL = [{
    # Means tested program?
    8934890: "Yes",
    8934891: "No",
    8934892: "Not reported/Unclear",
    8934893: "If means testing was conducted, what was the threshold? (details in info box)",
}]

means_tested_threshold_CEDIL = [{
    # option from 'means tested_CEDIL', 'info' column
    8934893: '',
}]

recipient_CEDIL = [{
    # Recipient of cash transfer program
    8934895: "Mother or female head of household",
    8934896: "Father or male head of household",
    8934897: "Parent or head of household",
    8934898: "Student (or student and parent/guardian)",
    8935026: "Other",
    8934899: "Not reported/Unclear",
}]

monthly_avg_cash_transfer_amount_CEDIL = [{
    # Monthly average amount of cash transfer per child
    8934901: "Primary recipient",
    8934902: "Secondary recipients (details in info box)",
    8934903: "Not reported/Unclear",
}]

primary_recipient_CEDIL = [{
    # option from 'monthly_avg_cash_transfer_amount'
    8939949: "Transfer in US $ (numeric value only)",
    8939951: "Transfer in domestic currency (numeric value only)",
}]

prim_rec_dom_curr_type_CEDIL = [{
    # nested within 'primary_recipient_CEDIL', 'info' column
    8939952: "Domestic currency type (in info box)"
}]

secondary_recipient_CEDIL = [{
    # option from 'monthly_avg_cash_transfer_amount'
    8939954: "Transfer in US $ (numeric value only)",
    8939955: "Transfer in domestic currency (numeric value only)",
}]

sec_rec_dom_curr_type_CEDIL = [{
    # nested within 'secondary', 'info' column
    8939957: "Domestic currency type (in info box)",
}]

transfer_limit_CEDIL = [{
    # Limit on total amount of family transfer 
    8934905: "No limit",
    8934906: "Yes, maximum amount per family (details in info box)",
    8934907: "Yes, maximum number of beneficiaries (details in info box)",
    8934908: "Not reported/Unclear",
}]

transfer_limit_yes_max_per_fam = [{
    # option from 'transfer_limit_CEDIL', 'info' columns
    8934906: '',
}]

transfer_limit_yes_max_benef = [{
    # option from 'transfer_limit_CEDIL', 'info' columns
    8934907: '',
}]

cash_transfer_variation_amount = [{
    # Variation in cash transfer amount (select all that apply)
    8934910: "None (flat transfer)",
    8934911: "Gender",
    8934912: "Age",
    8934913: "Grade",
    8934914: "Other",
    8934915: "Not reported/Unclear",
}]

cash_transfer_regularity = [{
    # How often do recipients receive the transfer?
    8934917: "Monthly",
    8934918: "Bi-monthly",
    8934919: "Quarterly/Trimesterly",
    8934920: "Biannually",
    8934921: "Annually",
    8939941: "Other",
    8934922: "Not reported/Unclear",
}]

time_limited_program_CEDIL = [{
    # Was the program time limited? (details in info box)
    8934925: "Yes - time limited",
    8934926: "No time limit",
    8934927: "Not reported/Unclear",
}]

primary_condition_CEDIL = [{
    # Primary condition of cash transfer program (select ONE)
    8934929: "School enrolment",
    8934930: "School attendance",
    8934931: "School enrolment and attendance",
    8934932: "School completion",
    8934933: "Academic achievement (details in info box)",
    8934934: "Grade promotion",
    8934935: "Other (details in info box)",
    8934936: "No conditions",
    8934937: "Not reported",
}]

additional_conditions_CEDIL = [{
    # Additional conditions of cash transfer program (select all that apply)
    8934939: "School enrolment",
    8934940: "School attendance",
    8934941: "School enrolment and attendance",
    8934942: "School completion",
    8934943: "Academic achievement (details in info box)",
    8934944: "Grade promotion",
    8934945: "Other",
    8934946: "No additional conditions",
    8934947: "Not reported",
}]

health_conditionality_CEDIL = [{
    # Health conditionality component?
    8934949: "Yes",
    8934950: "No",
    8934951: "Not reported/Unclear",
}]

health_conditions_CEDIL = [{
    # Health conditions of cash transfer program (select all that apply)
    8934953: "Student attendance at health check-ups",
    8934954: "Student immunizations up-to-date",
    8934955: "Health visits for pregnant and breastfeeding women",
    8934956: "Mothers attendance at health education workshops",
    8934957: "Other (details in info box)",
    8934958: "Not reported/Unclear",
}]

monitoring_CEDIL = [{
    # Monitoring of cash transfer program (select all that apply
    8934960: "School enrolment",
    8934961: "School attendance",
    8934962: "School completion",
    8934963: "Academic achievement",
    8934964: "Grade promotion",
    8934965: "Other (detail in info box)",
    8934966: "No monitoring",
    8934967: "Not reported/Unclear",
}]

verification_CEDIL = [{
    # Verification of cash transfer conditions (select all that apply)
    8934969: "School enrolment",
    8934970: "School attendance",
    8934971: "School completion",
    8934972: "Academic achievement",
    8934973: "Grade promotion",
    8934974: "Health attendance",
    8934975: "Other (details in info box)",
    8934976: "No verification",
    8934977: "Not reported/Unclear",
}]

minimum_attend_req_CEDIL = [{
    # Minimum school attendance requirement?
    8934979: "Yes",
    8934980: "No",
    8934981: "Not reported/Unclear",
}]

perc_attend_req_CEDIL = [{
    # % school attendance required (select ONE)
    8934983: "50%",
    8934984: "75%",
    8934985: "80%",
    8934986: "85%",
    8934987: "90%",
    8934988: "95%",
    8934989: "Other (detail in info box)",
    8939946: "Not reported/Unclear",
}]

perc_attend_other_CEDIL = [{
    # option from 'perc_attend_req_CEDIL', 'info' columns
    8934989: '',
}]

enforcement_CEDIL = [{
    # Enforcement (select all that apply)
    8934991: "Attendance at school",
    8934992: "Enrolment at school",
    8934993: "Other (details in info box)",
    8934994: "No enforcement",
    8934995: "Not reported/Unclear",
}]

enforcement_other_CEDIL = [{
    # option from 'enforcement_CEDIL', 'info' columns
    8934993: '',
}]

supply_incentive_CEDIL = [{
    # Supply incentive for education? (select all that apply)
    8934997: "Transfer unaccompanied by supply-side intervention",
    8934998: "Transfer complemented by supply incentive to school (details in info box)",
    8934999: "Transfer complemented by supply incentive to teachers (detail in info box)",
    8935000: "Not reported/Unclear",
}]

savings_component_CEDIL = [{
    # Savings component?
    8935002: "Yes (details in info box)",
    8935003: "No",
    8935004: "Not reported/Unclear",
}]

savings_comp_yes_CEDIL = [{
    # options from 'savings_component_CEDIL', 'info' column
    8935002: '',
}]

economic_outcomes_CEDIL = [{
    # Does the study report economic outcomes for households as a result of the intervention?
    8935006: "Yes (details in info box)",
    8935007: "No",
    8935008: "Not reported/Unclear",
}]

econ_outcomes_yes_CEDIL = [{
    # option from 'economic_outcomes_CEDIL', 'info' columns
    8935006: '',
}]

program_type_CEDIL = [{
    # Based upon the description of the intervention given in the study, which of the following criteria does it most closely align with?
    8935010: "Type 0 - Program is unconditional and not targeted at children e.g. pension transfer",
    8935011: "Type 1 - Unconditional program with the aim to improve educational outcomes",
    8935012: "Type 2 - Labelled transfers where participants are explicitly told that they are for use for education, but without any conditions",
    8935013: "Type 3 - Conditional transfers where conditions are not monitored or enforced",
    8935014: "Type 4 - Conditional transfers where conditions are monitored imperfectly and with little enforcement",
    8935015: "Level 5 - Conditional transfers where school enrolment conditions are monitored and enforced",
    8935016: "Level 6 - Conditional transfers where school attendance conditions are monitored and enforced",
    8935017: "Level 7 - Insufficient information to assign a category",
    8935018: "Level 8 - Program description does not match sufficiently to assign a category",
}]

################################################
# CEDIL MENSTUAL HYGIENE STRAND SPECIFIC CODING
################################################

intervention_type_CEDIL_MH = [{
    9085869: "Hardware",
    9085870: "Software",
    9085935: "Combined Intervention",
    9086198: "Not provided/Unclear",
}]

##########################
# HARDWARE CHARACTERISTICS
##########################

# Material component

commercial_mat_provided_CEDIL_MH = [{
    9087341: "Absorbents",
    9085955: "Underwear",
    9086223: "Other (type in Info Box)",
    9086227: "Provided but detail lacking/unclear",
    9086231: "No commercial materials provided",
}]

homemade_mat_provided_CEDIL_MH = [{
    9086071: "Absorbents",
    9086072: "Underwear",
    9086237: "Other (type in Info Box)",
    9086239: "Provided but detail lacking/unclear",
    9086240: "No commercial materials provided",
}]

use_mat_instruction_CEDIL_MH = [{
    9086181: "Yes, instructions provided",
    9086182: "No instructions provided",
    9086183: "Information not provided/Unclear",
}]

dist_frequency_CEDIL_MH = [{
    9085957: "",
}]

# Wash component

increased_toilets_CEDIL_MH = [{
    9085963: "",
}]

toilet_pupil_ratio_CEDIL_MH = [{
    9085970: "",
}]

improved_facilities_CEDIL_MH = [{
    9085969: "Toilets with menstrual hygiene supplies",
    9085964: "Provision of soap or disinfectant",
    9085965: "Provision of clean water",
    9086191: "Provision of hand washing facilities",
    9086081: "Provision of absorbent washing facilities",
    9086089: "Provision of absorbent disposal facilities",
}]

wash_comp_other_CEDIL_MH = [{
    9086208: "",
}]

wash_comp_provided_unclear_CEDIL_MH = [{
    9086209: "Provided but detail lacking/unclear",
}]

no_wash_comp_CEDIL_MH = [{
    9087425: "No WASH component",
}]

girl_friendly_comp_CEDIL_MH = [{
    9085972: "Single-sex toilets",
    9085967: "Lockable toilets",
    9086078: "Toilets with doors",
    9086184: "Toilets with lighting",
    9087422: "Provided but details lacking/unclear",
    9087427: "No girl-friendly component",
}]

girl_friendly_other_CEDIL_MH = [{
    9087421: "",
}]


calendar_track_cycle_CEDIL_MH = [{
    9086107: "Calendar to track cycle",
}]

hardware_char_other_CEDIL_MH = [{
    9085949: "",
}]

hardware_char_unclear_CEDIL_MH = [{
    9086088: "Information not provided/Unclear ",
}]

hardware_char_NA_software_imp_only_CEDIL_MH = [{
    9085948: "Not applicable, software intervention only",
}]

# SOFTWARE CHARACTERISTICS

software_char_CEDIL_MH = [{
    9086733: "Focus",
    9086262: "Frequency",
    9087273: "Information not provided/Unclear",
    9086256: "Not applicable, hardware intervention only",
}]

software_char_focus_CEDIL_MH = [{
    9085974: "Usage",
    9085976: "Understanding",
    9086734: "Other",
    9086254: "Information not provided/Unclear",
}]

software_char_frequency_CEDIL_MH = [{
    9086048: "One-off session",
    9086049: "Regular sessions",
    9086051: "Overall contact time",
    9086736: "Information not provided/Unclear",
}]

intervention_dur_CEDIL_MH = [{
    9085959: "",
}]

intervention_dur_not_prov = [{
    9086057: "",
}]

intervention_deliv_CEDIL_MH = [{
    9085977: "Teacher",
    9086102: "School nurse",
    9085978: "Midwife",
    9085979: "Parent",
    9085980: "Peer",
    9085982: "Healthcare worker ",
    9085983: "Social worker",
    9085981: "Printed sources",
    9086094: "Electronic sources",
    9085985: "Other (in Info Box)",
    9085986: "Not provided/Unclear",
}]

int_deliv_printed_sources_CEDIL_MH = [{
    9085981: "",
}]

int_deliv_electronic_sources_CEDIL_MH = [{
    9086094: "",
}]

int_deliv_other_CEDIL_MH = [{
    9085985: "",
}]

intervention_recipients_CEDIL_MH = [{
    9085937: "Female students",
    9085938: "Male students",
    9085939: "Mothers",
    9085940: "Other",
    9085987: "Information not provided/unclear",
}]

int_recip_other_CEDIL_MH = [{
    9085940: "",
}]

teacher_training_components_CEDIL_MH = [{
    9085942: "Yes, training provided",
    9085943: "No training provided",
    9085988: "Information not provided/Unclear",
}]

cash_transfer_component_CEDIL_MH = [{
    9085945: "Yes, cash transfer included",
    9085946: "No cash transfer included",
    9086801: "Information not provided/Unclear",
}]

health_outcomes_CEDIL_MH = [{
    9086037: "Menstrual behaviours/health",
    9086038: "Sexual behaviours/health",
    9086040: "Pregnancy",
    9086044: "Reproductive Tract Infection",
    9086803: "Other",
    9086802: "Health outcomes recorded but information not provided/Unclear",
    9087441: "No health outcomes recorded",
}]

health_outcomes_menst_health_CEDIL_MH = [{
    9086037: "",
}]

health_outcomes_sexual_health_CEDIL_MH = [{
    9086038: "",
}]

health_outcomes_pregnancy_CEDIL_MH = [{
    9086040: "",
}]

health_outcomes_other_CEDIL_MH = [{
    9086803: "",
}]

health_outcomes_repro_tract_infection_CEDIL_MH = [{
    9086045: "Bacterial Vaginosis",
    9086046: "Vaginal Candidiasis",
}]

# NEW ADDITIONS

toolkit_versions = [{
    12172938: "MT_Sept_2021",
    12172939: "MT_2023 (in progress)",
    12173011: "EY_January 2023",
}]