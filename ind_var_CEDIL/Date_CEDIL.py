from Main import load_json, get_metadata
import pandas as pd

load_json()

# add decade column
def decade_row(row):
    if int(row["pub_year"]) >= 1960 and int(row["pub_year"]) <= 1969:
        decade = "1960-1969"
    elif int(row["pub_year"]) >= 1970 and int(row["pub_year"]) <= 1979:
        decade = "1970-1979"
    elif int(row["pub_year"]) >= 1980 and int(row["pub_year"]) <= 1989:
        decade = "1980-1989"
    elif int(row["pub_year"]) >= 1990 and int(row["pub_year"]) <= 1999:
        decade = "1990-1999"
    elif int(row["pub_year"]) >= 2000 and int(row["pub_year"]) <= 2009:
        decade = "2000-2010"
    elif int(row["pub_year"]) >= 2010 and int(row["pub_year"]) <= 2019:
        decade = "2010-2019"
    elif int(row["pub_year"]) >= 2019 and int(row["pub_year"]) <= 2029:
        decade = "2020-2029"
    return decade

# get year data
year = get_metadata("Year")
year_df = pd.DataFrame(year)
year_df.columns = ["pub_year"]

# add decade column
""" year_df["decade"] = year_df.apply(decade_row, axis=1) """

# fill blanks with NA
year_df.fillna("NA", inplace=True)

# save to disk
#year_df.to_csv("year.csv", index=False)

print(year_df)