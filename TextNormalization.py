import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import openpyxl
nltk.download('punkt')

# Membaca teks dari file
file_path = '/content/artikel.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Mengambil daftar kata kata stopword
nltk.download('stopwords')
stop_words = set(stopwords.words('indonesian'))

# melakukan tokenisasi
words = word_tokenize(input_text)

# Hapus stopword
filtered_words = [word for word in words if word.lower() not in stop_words]

# Menjadikan teks kembali
filtered_text = ' '.join(filtered_words)

# Membuat workbook baru
workbook = openpyxl.Workbook()

#Mengakses worksheet aktif
sheet = workbook.active

# Menyimpan hasil
sheet['A1'] = 'Before'
sheet['A2'] = input_text

sheet['B1'] = 'After'
sheet['B2'] = filtered_text

#Use wrap text
sheet['A2'].alignment = openpyxl.styles.Alignment(wrap_text=True)
sheet['B2'].alignment = openpyxl.styles.Alignment(wrap_text=True)

# Menyimpan workbook ke excel
output_file = 'textNormalization.xlsx'
workbook.save(output_file)

print(f"Hasil : '{output_file}' ")

