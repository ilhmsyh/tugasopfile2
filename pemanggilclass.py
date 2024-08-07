from fileclass import HandleFile


file = HandleFile()
     
file.baca_file('hasil.txt')

file.tulis_file('hasil.txt', 'a') # Bisa Ganti Mode Sesuka Hati "tulis_file("nama_file", "mode")"