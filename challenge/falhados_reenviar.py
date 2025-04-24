import sqlite3
from auto import enviar_email
import time
from dotenv import load_dotenv

load_dotenv
TPS = float(os.getenv("TPS",1))
MAX_TENTATIVAS = 3
def reenviar():
    with sqlite3.connect("fila_reenvio") as conn:
        cursor =conn.cursor()
        cursor.execute("select rowid, nome, email, tentativas FROM fila")
        falhados = cursor.fetchall()

            
        for rowid, nome, email, tentativas in falhados:
            if tentativas >= MAX_TENTATIVAS:
                print(f"[⚠️] Ignorado (muitas tentativas): {email}")
                continue

            if enviar_email(nome, email):
                cursor.execute("DELETE FROM fila WHERE rowid=?", (rowid,))
            else:
                cursor.execute("UPDATE fila SET tentativas=tentativas+1 WHERE rowid=?", (rowid,))
            conn.commit()
            time.sleep(1 / TPS)

if __name__ == "__main__":
    reenviar()

