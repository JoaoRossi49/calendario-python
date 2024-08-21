from calendar_utils import get_feriados, generate_html_calendar

start_date_str = 2024
end_date_str = 2025

lista = get_feriados(start_date_str, end_date_str)

print(lista)