# For telegram automation
import asyncio
from pyrogram import Client
# For google_sheet
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials



# google_sheet connection
sheetconn = gspread.service_account(filename="service.json")
filename = sheetconn.open("test")

working_sheet = filename.worksheet("s1")

# print('Rows:',wks.row_count)
# print('Rows:',wks.col_count)
# worksheet=wks.get_all_records()

# get all the records of the data
records_data = working_sheet.get_all_records()
# convert the json to dataframe
records_df =pd.DataFrame.from_dict(records_data)

ids = [val['id'] for val in records_data]
print(ids)


# ------------------------------------------------------------------
# Add Telegram Members

api_id =16661874
api_hash = "3fbd8b39162b5d9b0d12a3501b63b5ee"
list = ["@Teamblack1415",'@nelsondurairaj']

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.add_chat_members(chat_id=-641830690, user_ids= list)

asyncio.run(main())