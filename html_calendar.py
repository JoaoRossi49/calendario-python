import calendar
from datetime import date
from calendar_utils import generate_html_calendar, get_feriados

# Definir os feriados
feriados = get_feriados(2024, 2026)

#Quantos dias de aula teórica
diasTeorico = 0

def pintar_dia(html, dia, mes, feriados):
    global diasTeorico
    diasTreinamentoInicial = 12
    for i in range(1, 32):
        try:
            dia_atual = date(2024, mes, i)
            #Se for feriado, mesmo se tiver aula, será vermelho
            if dia_atual.weekday() == dia and dia_atual in feriados:
                html = html.replace(f'<td class="{dia_atual.strftime("%a").lower()}">{i}</td>', 
                                    f'<td class="highlight-holiday">{i}</td>') 
            #Se for feriado, será vermelho
            elif dia_atual in feriados:
                html = html.replace(f'<td class="{dia_atual.strftime("%a").lower()}">{i}</td>', 
                                    f'<td class="highlight-holiday">{i}</td>')     
            #Se tiver aula, será verde           
            elif dia_atual.weekday() == dia:
                html = html.replace(f'<td class="{dia_atual.strftime("%a").lower()}', 
                                    f'<td class="highlight')
                diasTeorico += 1
               
        except:
            pass
    return html

start_date = "17/01/2024"
end_date = "17/12/2024"

html_calendar = generate_html_calendar(start_date, end_date, locale='pt_BR')

# Aluno terá aulas na segunda-feira (weekday 0 é segunda-feira)
for mes in range(1, 12):
    html_calendar = pintar_dia(html_calendar, 0, mes, feriados)

html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendário Agosto 2024</title>
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
