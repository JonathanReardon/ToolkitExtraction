import os
import json
import pandas as pd

from DATAFILE import file

exclude = "NA"

script_dir = os.path.dirname(__file__)
datafile = os.path.join(script_dir, file)

with open(datafile) as f:
    data = json.load(f)

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

def get_date():
    global year
    year = []
    for section in range(len(data["References"])):
        if data["References"][section]["Year"]:
            year.append(data["References"][section]["Year"])
        else:
            year.append(exclude)

get_date()

year_df = pd.DataFrame(year)
year_df.columns = ["pub_year"]

""" year_df["decade"] = year_df.apply(decade_row, axis=1) """

year_df.fillna("NA", inplace=True)

print(year_df)

year_df.to_csv("year.csv", index=False)
