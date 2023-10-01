import re
import Levenshtein
import nltk
from nltk.tokenize import word_tokenize
import openpyxl

# Melakukan download kamus bahasa inggris dengan library nltk
nltk.download('words')
from nltk.corpus import words

# Mengambil kata kata nya
english_words = set(words.words())

# Membaca teks dari file
file_path = '/content/artikel_english_wrong.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Penghapusan tanda baca, agar lebih mudah
teks_tanda = re.sub(r'[^\w\s]', '', input_text)

# Penghapusan angka, agar lebih mudah
normalized_text = re.sub(r'\d', '', teks_tanda)

# Melakukan tokenisasi
words = word_tokenize(normalized_text)

# Variabel teks yang benar
kata_benar = ""

# Perulangan untuk setiap kata
for word in words:
  # Penghapusan char non-alfaber
  word = ''.join(filter(str.isalpha, word))

  # Variabel untuk menyimpan kata terbaik
  best_word = None
  # Nilai tak terhingga
  min_distance = float('inf')

  # Perulangan dengan kamus
  for dict_word in english_words:
    distance = Levenshtein.distance(word.lower(), dict_word.lower())
    if distance < min_distance:
      min_distance = distance
      best_word = dict_word

  # Penambahan kata yang terkoreksi ke hasil koreksi
  if min_distance <= 1:
    kata_benar += best_word + " "
  else:
    kata_benar += word + " "

# Membuat workbook baru
workbook = openpyxl.Workbook()

#Mengakses worksheet aktif
sheet = workbook.active

# Menyimpan hasil
sheet['A1'] = 'Before'
sheet['A2'] = input_text

sheet['B1'] = 'After'
sheet['B2'] = kata_benar

#Use wrap text
sheet['A2'].alignment = openpyxl.styles.Alignment(wrap_text=True)
sheet['B2'].alignment = openpyxl.styles.Alignment(wrap_text=True)

# Menyimpan workbook ke excel
output_file = 'minimumEditDistance.xlsx'
workbook.save(output_file)

print(f"Hasil : '{output_file}' ")



