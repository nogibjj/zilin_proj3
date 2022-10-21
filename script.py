import pandas as pd
from sodapy import Socrata
import os  # also need os
from dotenv import load_dotenv

load_dotenv()  # blank if .env file in same directory as script
# load_dotenv('<path to file>.env') to point to another location
APPTOKEN = os.getenv('APPTOKEN')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# # Unauthenticated client only works with public data sets. Note 'None'
# # in place of application token, and no username or password:
# client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
                 APPTOKEN,
                 username=USERNAME,
                 password=PASSWORD)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ic3t-wcy2", limit=10, select="*")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df)