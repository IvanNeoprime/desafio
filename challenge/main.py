from sheets_client import get_sheet_data
from auto.py import enviar_email, iniciar_fila
import os
import time
from dotenv import load_dotenv

load_dotenv()
TPS = float(os.getenv("TPS", 1))
SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
SHEET_NAME = os.getenv("SHEET_NAME")

def main():
    iniciar_fila()
    data = get_sheet_data(SHEET_ID, SHEET_NAME)
    for item in data:
        nome = item.get("Nome") or item.get("Name")
        email = item.get("Email")
        if nome and email:
            enviar_email(nome, email)
            time.sleep(1 / TPS)

if __name__=="__main__":
    main()
    