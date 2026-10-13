"""
ap, semangat! Belajar dari kesalahan itu cara paling efektif buat paham perulangan.

Yuk, kita coba satu soal latihan lagi dengan struktur serupa. Soal ini dirancang khusus untuk melatih kembali poin-poin yang tadi sempat keliru:

---

### **Soal Latihan: Filter Suhu (** **process_temperatures** **)**

Buatlah fungsi Python bernama **process_temperatures(temps)** yang menerima parameter berupa list angka `temps` (suhu dalam Celsius).

#### **Langkah 1: Filter Data (Gunakan** **while** **loop)**

* Iterasi list `temps` dari kiri ke kanan menggunakan **while** **loop**.
* Berhenti (**break**) jika menemukan suhu ekstrem, yaitu suhu **&lt; 0** atau **gt; 100**.
* Masukkan semua suhu valid (antara `0` sampai `100` inklusif) sebelum pemberhentian tersebut ke dalam list baru `valid_temps`.

#### **Langkah 2: Hitung Nilai (Gunakan** **for** **loop)**

* Hitung dua hal berikut dari `valid_temps` menggunakan **for** **loop**:
  1. **sum_odd_index**: Jumlah suhu yang berada pada **indeks ganjil** (`1, 3, 5, ...`).
  2. **count_above_30**: Banyaknya suhu yang nilainya **gt; 30**.
* Kembalikan nilai berupa **tuple**: `(sum_odd_index, count_above_30)`.
"""

def process_temperatures(temps):
    valid_temps = []
    i = 0

    while i < len(temps):
        suhu = temps[i]
        if suhu < 0 or suhu > 100:
            break

        valid_temps.append(suhu)

        i += 1

    sum_odd_index = 0
    count_above_30 = 0

    for idx in range(len(valid_temps)):
        num = valid_temps[idx]

        if idx % 2 == 1:
            sum_odd_index += num
            if num > 30:
                count_above_30 += 1
        elif num > 30:
            count_above_30 += 1

    return (sum_odd_index, count_above_30)

print(process_temperatures([25, 32, 28, 35, 40, -5, 50]))