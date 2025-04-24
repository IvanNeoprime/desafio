import sqlite3
from redmail import gmail
from jinja2 import template
from pathlib import path
from dotenv import load_dotenv
import os

load_dotenv()
gmail.username = os.getenv('ivandromaoze138@gmail.com')
gmail.password = os.getenv('achas que te vou dar a senha?')
DB_fila = "fila_reenvio.db"
TEMPLATE = "template.html"

def iniciar_fila():
    with sqlite3.connect(DB_fila) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS file(
                     nome TEXT,
                     email TEXT,
                     tentativas INTEGER DEFAULT 0)""")
        
def utilizar_template(nome):
    Template=path(TEMPLATE).read_text(encoding="utf-8")
    return template(Template).render(bome = nome)

def add_na_fila(nome,email):
    with sqlite3.connect(DB_fila) as conn:
        conn.execute("INSERT INTO fila(nome,email) VALUES(?,?)",(nome,email))
        conn.commit()

def enviar_email(nome, email):
    html = utilizar_template(nome)
    try:
        gmail.send(
             subject="Confirmação de Inscrição no Evento",
            receivers=[email],
            html=html
        )
        print(f"Enviado co sucesso: {nome} <{email}>")
        return True
        
    except Exception as e: 
        print(f'Falha de envio:{nome}<{email}> - {e}')
        add_na_fila(nome, email)
        return False
    
    
print('obrigado')