import pandas as pd
from sodapy import Socrata
import os  # also need os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

load_dotenv()  # blank if .env file in same directory as script
# load_dotenv('<path to file>.env') to point to another location
APPTOKEN = os.getenv("APPTOKEN")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# authenticated client (needed for non-public datasets):
client = Socrata(
    "data.cityofnewyork.us", APPTOKEN, username=USERNAME, password=PASSWORD
)

# Motor Vehicle Collisions - Crashes DB from NYC open data 
# returned as JSON from API / converted to Python list of dictionaries by sodapy.
count = client.get( # Get the number of collision after 2014-10-28 where number_of_persons_killed is greater than 0
    "h9gi-nx95", # dataset_id
    # select clauses
    select="count(collision_id)",
    # conditional clauses
    where="crash_date > '2014-10-28T00:00:00.000' AND number_of_persons_killed is not null AND number_of_persons_killed > 0",
)
print(count) # Number of collision in total
print(int(count[0]["count_collision_id"]) / (8 * 365)) # Number of collision average per day

# Get the number of collision after 2014-10-28 where number_of_persons_killed is greater than 0
# plus location constraint (to omit bad data)
records = client.get(
    "h9gi-nx95", #dataset_id
    # select clauses
    select="crash_date,crash_time,latitude,longitude,number_of_persons_injured,number_of_persons_killed",
    # conditional clauses
    where="crash_date > '2014-10-13T00:00:00.000' AND number_of_persons_killed is not null AND latitude > 40 AND longitude > -75",
    order="number_of_persons_killed DESC, number_of_persons_injured DESC, crash_date DESC, crash_time DESC",
)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(records)
print(df.head)
print(df.dtypes)
df["crash_date"] = pd.to_datetime(df["crash_date"])
df["crash_time"] = pd.to_datetime(df["crash_time"], format="%H:%M")
df["latitude"] = df["latitude"].astype(float)
df["longitude"] = df["longitude"].astype(float)
df["number_of_persons_injured"] = df["number_of_persons_injured"].astype(int)
df["number_of_persons_killed"] = df["number_of_persons_killed"].astype(int)
print(df.dtypes)

# find the relationship between crash_date and crashes
x = df["crash_date"]
y = df["number_of_persons_killed"]
# plotting number_of_persons_killed vs. crash_date
plt.plot(x, y, "bo")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("results/date_crashes.png")
plt.close()

# plotting number_of_persons_killed vs. (latitude, longitude)
nx = df["latitude"]
ny = df["longitude"]
nc = df["number_of_persons_killed"]
plt.scatter(nx, ny, s=10, c=nc, cmap="gray")
plt.savefig("results/location_crashes.png")
