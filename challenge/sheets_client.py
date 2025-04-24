import gspread
from auth2client.service_account import ServiceAccountCredentials

def get_sheet_data(sheet_id, sheet_name):
    scope = []
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).worksheet(sheet_name)
    data = sheet.get_all_records()
    return data