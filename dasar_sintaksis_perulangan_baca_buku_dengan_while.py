"""
Program perulangan baca buku dengan while
"""

jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_dibaca}')

while jumlah_buku_dibaca < jumlah_buku:
    jumlah_buku_dibaca = jumlah_buku_dibaca + 1
    print(f"Baca buku ke {jumlah_buku_dibaca} yang belum dibaca")

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_dibaca}')