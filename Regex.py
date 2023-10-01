import openpyxl
import re

# Membaca teks dari file
file_path = '/content/artikel.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Tokenisasi teks menjadi kata - kata
tokens = re.findall(r'\b\w+\b', input_text)

# Membuat workbook baru
workbook = openpyxl.Workbook()

#Mengakses worksheet aktif
sheet = workbook.active

# Menyimpan hasil
sheet['A1'] = 'Kata - kata tertokenisasi'

for i, token in enumerate(tokens, start = 2):
  sheet[f'A{i}'] = token

# Menyimpan workbook ke excel
output_file = 'contoh_regex.xlsx'
workbook.save(output_file)

print(f"Hasil Tokenisasi : '{output_file}' ")

# Sekarang, variabel 'tokens' berisi array paragraf yang telah ditokenisasi
# print("Tokens: ", tokens)
