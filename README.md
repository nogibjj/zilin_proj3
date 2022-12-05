# IDS706-Zilin Project

## Objective
The high-level overview of this project is to provide a way for people to get inforamtion about car accident / collision happened at New York City using the data retrieved from NYC OpenData, Specifically the "Motor Vehicle Collisions - Crashes" dataset. And the detailed sub-goals of the project are listed as:

1. Use Opendata database and SoQL to query data and perform preliminary data analysis with pandas

2. Find relationship between crash date, location (latitude, longitude) and crashes

3. Use visualization tools (Matplotlib) to provide visualized insight for people

## Dataset
NYC OpenData: https://opendata.cityofnewyork.us/data/

Motor Vehicle Collisions - Crashes: https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

API Docs: https://dev.socrata.com/foundry/data.cityofnewyork.us/h9gi-nx95

## SoQL (Salesforce Object Query Language)
SoQL is a query language similar to SQL. They are different that SQL is used to query data from SQL database while SoQL is not. They are similar because they both support various clauses so as to perform complex data query

For more information about SoQL: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.html

SoQL examples used in the project:
- Get the number of collision after 2014-10-28:00:00:00 where number_of_persons_killed is greater than 0
```
client.get(
    "h9gi-nx95", # dataset_id
    # select_clauses
    select="count(collision_id)",
    # conditional_clauses
    where="crash_date > '2014-10-28T00:00:00.000' AND number_of_persons_killed is not null AND number_of_persons_killed > 0",
)
```

- Get the number of collision after 2014-10-28 where number_of_persons_killed is greater than 0 with location constraint (to omit bad data)
```
client.get(
    "h9gi-nx95", #dataset_id
    # select_clauses
    select="crash_date,crash_time,latitude,longitude,number_of_persons_injured,number_of_persons_killed",
    # conditional_clauses
    where="crash_date > '2014-10-13T00:00:00.000' AND number_of_persons_killed is not null AND latitude > 40 AND longitude > -75",
    order="number_of_persons_killed DESC, number_of_persons_injured DESC, crash_date DESC, crash_time DESC",
)
```

## How to use
step1. make install # to install all dependencies
step2. python / python3 main.py # to run the script

## Results
The generated images are stored in the root directory and are stored in png format. People may use it as a reference to get information about car accident or collision happened in New York City.
