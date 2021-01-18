"""Description:
    * author: Magdy Abdelkader
    * company: Fresh Futures/Seeka Technology
    * position: IT Intern
    * date: 12-01-21
    * description:This script fetch the lat and long nominatim open street API using the Addresses in the Address.csv
"""
import pandas as pd # pip install pandas
from geopandas.tools import geocode  # follow https://geopandas.org/install.html
import geopy # pip install geopy
import time

# changing the default user_agent name
geopy.geocoders.options.default_user_agent = "magdy"

# Reading the addresses csv file into dataframe
addresses = pd.read_csv('address.csv', usecols=["Address"])

# looping through the addresses and fitch the long and lat
for index, row in addresses.iterrows():
    try:
        print(row['Address'])
        # fetching each row (Address) from geopandas and using the open street map "nominatim" read 'https://nominatim.openstreetmap.org/ui/search.html'
        info = geocode(str(row['Address']), provider='nominatim')
        # Adding Lat and lon columns to the dataframe
        addresses.loc[int(index), 'Lon'] = info['geometry'].loc[0].x
        addresses.loc[int(index), 'Lat'] = info['geometry'].loc[0].y
    except TypeError:
        print("\nGeocoding information for "+row['Address']+" is not found!\n")
    time.sleep(1)

    # Saving the dataframe to a csv file
    addresses.to_csv('addresses_with_lon_and_lat.csv')



