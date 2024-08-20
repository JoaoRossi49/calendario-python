from calendar import LocaleHTMLCalendar
from datetime import datetime, date
import itertools
import holidays

def generate_html_calendar(start_date, end_date, locale='pt_BR.UTF-8'):
    # Inicializa o calendário com a localidade especificada
    cal = LocaleHTMLCalendar(locale=locale)

    # Converte as datas de string para datetime se necessário
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%d/%m/%Y")

    # Gera uma sequência de meses entre a data de início e de fim
    current_year = start_date.year
    current_month = start_date.month
    end_year = end_date.year
    end_month = end_date.month

    # Lista para armazenar os meses
    months = []

    for year, month in itertools.product(range(current_year, end_year + 1), range(1, 13)):
        if (year == current_year and month >= current_month) or (year == end_year and month <= end_month) or (year != current_year and year != end_year):
            months.append((year, month))

    # Gera o HTML para cada mês
    html_output = ""
    for year, month in months:
        html_output += cal.formatmonth(year, month)
        html_output += "<br><br>"

    return html_output


def get_feriados(ano_inicial, ano_final):
    br_holidays = holidays.Brazil(years=[ano_inicial, ano_final], subdiv='SP')
    feriados = sorted(list(br_holidays.keys()))
    feriados_list = [date(feriado.year, feriado.month, feriado.day) for feriado in feriados]
    return feriados_list