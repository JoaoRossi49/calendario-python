import calendar
from datetime import date, datetime
from calendar_utils import generate_html_calendar, get_feriados

# Quantos dias de aula teórica
diasTeorico = 0

def pintar_dia(html, dia, mes, ano, feriados, start_date, end_date):
    global diasTeorico
    nome_dia = ""
    for i in range(1, 32):
        try:
            dia_atual = date(ano, mes, i)
            amanha = date(ano, mes, i+1)
            nome_dia = dia_atual.strftime("%a").lower()     

            if not (start_date <= dia_atual <= end_date):
                continue
            nome_dia = dia_atual.strftime("%a").lower()

            #Se o dia da próxima iteração for feriado e hoje for segunda ou sexta, será vermelho
            if ((nome_dia == 'mon' or nome_dia == 'fri') and amanha in feriados):
                html = html.replace(f'<td class="{nome_dia}">{i}</td>', 
                                    f'<td class="highlight-near-holiday">{i}</td>') 
                

            # Se for feriado, será vermelho
            if dia_atual in feriados:
                html = html.replace(f'<td class="{nome_dia}">{i}</td>', 
                                    f'<td class="highlight-holiday">{i}</td>') 
                
            # Se tiver aula, será verde           
            elif dia_atual.weekday() == dia:
                html = html.replace(f'<td class="{nome_dia}">{i}</td>', 
                                    f'<td class="highlight">{i}</td>')
                diasTeorico += 1

        except Exception as e:
            continue
    return html

# Ajustar as datas de início e fim
start_date_str = "10/02/2024"
end_date_str = "17/12/2025"

start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()

# Definir os feriados
feriados = get_feriados(start_date.year, end_date.year)

html_months_list = generate_html_calendar(start_date_str, end_date_str, locale='pt_BR')

# Loop sobre anos e meses
html_calendar = ""
for data, html in html_months_list:
    mes = data.month
    ano = data.year
    html_calendar += pintar_dia(html, 0, mes, ano, feriados, start_date, end_date) 

html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendário 2024-2025</title>
    <style>
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #000;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        .highlight {{
            background-color: green;
            color: white;
            font-weight: bold;
        }}
        .highlight-holiday {{
            background-color: red;
            color: white;
            font-weight: bold;
        }}
        .highlight-near-holiday {{
            background-color: yellow;
            color: white;
            font-weight: bold;
        }}        
    </style>
</head>
<body>
    {html_calendar}
    <h1>Total de encontros: {diasTeorico}</h1>
</body>
</html>
"""

filename = "calendario.html"

with open(filename, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Calendário salvo em {filename}")
