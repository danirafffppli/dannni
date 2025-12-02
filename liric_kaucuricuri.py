import sys
import time

lirik = [
    ("Kau curi-curi pandangan...", 2.70),
    ("Kutau kau suka tantangan...", 3.18),
    ("Oh jangan di tahan-tahan...", 3.30),
    ("Aku tau tipemu yang berandalannnn", 3.0),
    ("Tapi jangan komplain soal keadaan...", 3.0),
    ("Bintang 5 tapi ku bukan ancaman", 3.0),
    ("Aku bukan polisi ku buatmu angkat tangan", 3.50),
    ("Jangan buru-buru kita pelan-pelan...", 3.51)
]

def efek(teks, delay_karakter=0.03):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay_karakter)
    print()

for baris, delay_baris in lirik:
    efek(baris)             
    time.sleep(delay_baris)