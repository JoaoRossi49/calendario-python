import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

# Caminho do arquivo Excel
excel_path = 'modelo.xlsx'

# Carregar o arquivo Excel
workbook = load_workbook(excel_path)
sheet = workbook.active  # Escolhe a primeira planilha, pode mudar para outra se necessário

# Tabela HTML como string
with open('calendario.html', 'r', encoding='utf-8') as file:
    html_table = file.read()

# Converter a tabela HTML para DataFrame
df = pd.read_html(html_table)[0]  # O [0] seleciona o primeiro DataFrame gerado

# Inserir os dados do DataFrame no Excel a partir da linha 24 e coluna B
start_row = 24
start_col = 2  # Coluna B (A=1, B=2, etc.)

for r_idx, row in enumerate(df.itertuples(index=False), start=start_row):
    for c_idx, value in enumerate(row, start=start_col):
        cell = sheet.cell(row=r_idx, column=c_idx)
        cell.value = value

# Salvar as alterações no arquivo Excel
workbook.save(excel_path)
print(f"Dados inseridos com sucesso a partir da linha {start_row} e coluna B!")