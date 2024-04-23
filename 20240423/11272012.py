# https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/

import requests
import os

for date in range( 16, 23, 1 ):

    date_str = str(date).zfill(2)

    for hour in range(24):  # Loop through each hour

        hour_str = str(hour).zfill(2)

        for minute in range(0, 60, 5):  # Loop through each minute in the hour

            minute_str = str(minute).zfill(2)
            time_str = hour_str + minute_str + "00"
            url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/202404{date_str}/{hour_str}/TDCS_M04A_202404{date_str}_{time_str}.csv"
            response = requests.get(url)

            if response.status_code == 200:

                with open( f"TDCS_M04A_202404{date_str}_{time_str}.csv", 'wb') as f:
                    f.write(response.content)

            else:
                print(f"Failed to download file: TDCS_M04A_202404{date_str}_{time_str}.csv")


# import pandas as pd
# import glob

# # Get a list of all CSV files

# for date in range( 16, 23, 1 ):
    
#     date_str = str(date).zfill(2)

#     csv_files = glob.glob('TDCS_M04A_202404{date_str}_*.csv')

# # Create a list to store the dataframes
# dfs = []

# # Read each CSV file and append it to the list of dataframes
# for csv_file in csv_files:
#     df = pd.read_csv(csv_file)
#     dfs.append(df)

# # Concatenate all dataframes into one
# result = pd.concat(dfs)

# # Write the result to a new CSV file
# result.to_csv("output.csv", index=False)