import time
import sys

lirik = [
    ("tante...", 1.9),
    ("sudah terbiasa terjadi tante", 2.0),
    ("teman datang ketika lagi butuh saja", 2.0),
    ("coba kalo lagi susah", 2.0),
    ("mereka semua menghilaaaaaaaaaaaaaaaaaanggggggggg", 3.5)
]

def tulis_per_huruf(teks, jeda=0.05):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(jeda)
    print() 

for baris, jeda in lirik:
    tulis_per_huruf(baris)
    time.sleep(jeda)