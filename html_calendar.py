import calendar
from datetime import date, datetime
from calendar_utils import generate_html_calendar, get_feriados, pintar_dia

def gerar_calendario():
    # Ajustar as datas de início e fim
    start_date_str = "17/01/2024"
    end_date_str = "17/12/2025"
    
    diasTeorico = 0

    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()

    # Definir os feriados
    feriados = get_feriados(start_date.year, end_date.year)

    html_months_list = generate_html_calendar(start_date_str, end_date_str, locale='pt_BR')

    # Loop sobre anos e meses
    html_calendar = ''
    
    for index, (data, html) in enumerate(html_months_list):
        mes = data.month
        ano = data.year
        isPrimeiroAno = False
        if index == 0:
            isPrimeiroAno = True
            
        html = pintar_dia(html, 0, mes, ano, feriados, start_date, end_date, isPrimeiroAno)
        
        if index == 0 or index % 2 != 0:
            html_calendar += '<tr class="mes">'
            html_calendar += f'<td class="mes">{html}</td>'
            html_calendar += '<td></td>'
        else:
            html_calendar += f'<td class="mes" >{html}</td>'
            html_calendar += '<td></td>'
            html_calendar += '</tr class="mes">'  
    
    with open('head.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
        
    html_content += f"""
    <table border="0" cellpadding="0" cellspacing="0">
        {html_calendar}
            </table>
    </body>
    </html>
    """

    filename = "calendario.html"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)

