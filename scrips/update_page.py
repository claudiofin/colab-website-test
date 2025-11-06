# scripts/update_page.py
from datetime import datetime
import os

def generate_html():
    now = datetime.now().strftime("%A, %d %B %Y ore %H:%M:%S")
    html_content = f"""
    <html>
      <head>
        <title>Sito Aggiornato da GitHub Actions!</title>
        <style>
          body {{ font-family: sans-serif; text-align: center; margin-top: 50px; }}
          h1 {{ color: #24292e; }}
          p {{ font-size: 1.2em; }}
        </style>
      </head>
      <body>
        <h1>Ciao dal Workflow Automatico! 🤖</h1>
        <p>Questa pagina è stata aggiornata automaticamente da GitHub Actions.</p>
        <p><b>Ultimo aggiornamento:</b> {now}</p>
      </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(html_content)
    print("File index.html generato con successo!")

if __name__ == "__main__":
    generate_html()
