import pandas as pd
import json

# Read the county_State Excel file
county_state_df = pd.read_excel('county_State.xlsx')

# Extract county and state columns
counties = county_state_df['County'].tolist()
states = county_state_df['State'].tolist()
counties_states = list(zip(counties, states))

# Read the countyName_to_FIPS Excel file
county_fips_df = pd.read_excel('countyName_to_FIPS.xls', dtype={'FIPS': str})

# Read the FIPS to ZIP Excel file
fips_zip_df = pd.read_excel('FIPS_to_Zip.xlsx', dtype={'FIPS': str, 'ZipCode': str})

# Dictionary to store the ZIP codes for each county
county_zip_codes = {}

# Iterate over each county and state
for county, state in counties_states:
    # Search for the county and state in the countyName_to_FIPS DataFrame
    filtered_df = county_fips_df[(county_fips_df['County'] == county) & (county_fips_df['State'] == state)]

    if not filtered_df.empty:
        # Extract FIPS code if a match is found
        fips_code = filtered_df['FIPS'].values[0]

        # Filter the FIPS to ZIP DataFrame to get ZIP codes for this FIPS
        zip_codes_df = fips_zip_df[fips_zip_df['FIPS'] == fips_code]
        if not zip_codes_df.empty:
            zip_codes = zip_codes_df['ZipCode'].dropna().unique().tolist()
            county_zip_codes[county] = zip_codes

# Prepare the JSON output
options = [
    {
        "label": county,
        "value": county,
        "zipcodes": zip_codes,
        "membershipGroup": {
            "id": county[:4].upper(),  # Example ID: first 4 letters of county
            "description": county
        }
    }
    for county, zip_codes in county_zip_codes.items()
]

# Save the output to a JSON file
with open('zips.json', 'w') as json_file:
    json.dump({"options": options}, json_file, indent=4)

print("JSON output saved to zips.json")
