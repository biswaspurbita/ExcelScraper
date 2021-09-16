
from googleapiclient.discovery import build
from google.oauth2 import service_account
from headers import Singleton


class GoogleSheet(metaclass=Singleton):
    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '1KrPYhcIIbYVahqybpoiE4j6nl1vQQ-py5KgeXbmufYQ'

    def __init__(self):
        self.creds = service_account.Credentials.from_service_account_file(
            GoogleSheet.SERVICE_ACCOUNT_FILE,
            scopes=GoogleSheet.SCOPES
        )
        self.service = build('sheets', 'v4', credentials=self.creds)
        self.sheet = self.service.spreadsheets()

    def writeLineToSheet(self, data):
        '''

        :param data:
        {
            "Product Name": "Mars By GHC Green tea, L-carnitine & Gugul With Natural Ingredients For Fitness Management 60 Capsules",
            "Asin": "B097F2MXJ3",
            "Site": "Amazon",
            "Rank": {
                "Global": "No Rank",
                "Sponsored": "No Rank",
                "Non-Sponsored": "No Rank"
            }
        }
        :return:
        '''
        if not data:
            return

        result_data = [[data["timestamp"], data["keyword"], data["Product Name"], data["Asin"], data["Site"], data["Rank"]["Global"], data["Rank"]["Sponsored"], data["Rank"]["Non-Sponsored"], data["Rank"]["Rating"], data["Rank"]["Review"]]]
        resource = {
            "majorDimension": "ROWS",
            "values": result_data
        }
        request = self.sheet.values().append(spreadsheetId=GoogleSheet.SPREADSHEET_ID, range='Amazon!A2', valueInputOption='USER_ENTERED', body=resource).execute()
        return request
