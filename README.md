# Overview

This repo takes the county_State.xlsx file as input and outputs json with the relevant zip codes for the county / state pairs listed.

The county_State file should have two columns, with headers County and State where State uses the two-letter US State abbreviation and is all-caps.

# Steps

1) Reads the county_State file to identify which counties you are after
2) Reads the countyName_to_FIPS file to find the FIPS (state + county unique id) for the relevant counties
3) Reads the FIPS_to_Zip file to find the Zip Codes for the relevant counties
4) Output the zip codes to json file
