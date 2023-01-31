from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import country_CEDIL
import pandas as pd

load_json()

##############################################
# World Bank economy listing by country
# https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups

low_income = ["Afghanistan",  "Guinea-Bissau", "Sierra Leone",
              "Burkina Faso", "Haiti", "Somalia",
              "Burundi", "Korea, Dem. People's Rep.", "South Sudan",
              "Central African Republic", "Liberia", "Sudan",
              "Chad", "Madagascar", "Syrian Arab Republic",
              "Congo, Dem. Rep", "Malawi", "Tajikistan",
              "Eritrea", "Mali", "Togo"
              "Ethiopia", "Mozambique", "Uganda"
              "Gambia, The", "Niger", "Yemen, Rep.",
              "Guinea", "Rwanda"]

##############################################

# get country data
country = get_data(country_CEDIL)
country_df = pd.DataFrame(country)
country_df = country_df.T
country_df.columns = ["loc_country_raw"]

# get country highlighted text
country_HT = highlighted_text(country_CEDIL)
country_HT_df = pd.DataFrame(country_HT)
country_HT_df = country_HT_df.T
country_HT_df.columns = ["loc_country_ht"]

# get country user comments
country_Comments = comments(country_CEDIL)
country_Comments_df = pd.DataFrame(country_Comments)
country_Comments_df = country_Comments_df.T
country_Comments_df.columns = ["loc_country_info"]

# concatenate data frames
""" country_df = pd.concat(
    [country_df, country_HT_df, country_Comments_df], axis=1, sort=False) """

# fill blanks with NA
country_df.fillna("NA", inplace=True)

# save to disk
# country_df.to_csv("Country.csv", index=False)

print(country_df)