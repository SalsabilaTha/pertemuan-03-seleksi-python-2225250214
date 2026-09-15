# Pertemuan 03 - Seleksi Python 
## Identitas

- Nama: [Salsabila Thahira]
- NIM: 2225250214
- Kelas: [3B]

## Tujuan

Pada pertemuan ini dibuat beberapa program Python Menulis program seleksi menggunakan if, if-else, kondisi majemuk, dan nested if. menggunakan percabangan:

1. Genap atau Ganjil
2. Membandingkan Dua Bilangan
3. Kelulusan Bersyarat
4. Menentukan Jenis Segitiga
5. Analisis Persamaan Kuadrat

## Cara Menjalankan

Program dijalankan melalui terminal pada VS Code.

Untuk menjalankan latihan, gunakan perintah sesuai nama file, contohnya:

python latihan/01_genap_ganjil.py
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py

Untuk menjalankan Tugas 2:

python tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
1. Latihan 1 - Genap atau Ganjil
    1. Memasukkan satu bilangan bulat.
    2. Mengecek sisa pembagian bilangan dengan 2 menggunakan operator %.
    3. Jika sisanya 0, bilangan dinyatakan genap.
    4. Jika sisanya bukan 0, bilangan dinyatakan ganjil.

2. Latihan 2 - Membandingkan Dua Bilangan
    1. Memasukkan dua bilangan.
    2. Membandingkan bilangan pertama dengan bilangan kedua.
    3. Jika bilangan pertama lebih besar, tampilkan bahwa bilangan pertama lebih besar.
    4. Jika kedua bilangan sama, tampilkan bahwa keduanya sama.
    5. Jika tidak, tampilkan bahwa bilangan pertama lebih kecil.

3. Latihan 3 - Kelulusan Bersyarat
    1. Memasukkan nilai akhir dan persentase kehadiran.
    2. Mengecek apakah nilai minimal 60.
    3. Mengecek apakah kehadiran minimal 80%.
    4. Kedua syarat harus terpenuhi menggunakan operator and.
    5. Jika keduanya terpenuhi, mahasiswa dinyatakan lulus.
    6. Jika salah satu syarat tidak terpenuhi, mahasiswa dinyatakan belum lulus.

4. Latihan 4 - Jenis Segitiga
    1. Memasukkan tiga panjang sisi.
    2. Mengecek terlebih dahulu apakah ketiga sisi dapat membentuk segitiga.
    3. Jika bisa membentuk segitiga, mengecek apakah ketiga sisinya sama.
    4. Jika semua sama, hasilnya segitiga sama sisi.
    5. Jika ada dua sisi yang sama, hasilnya segitiga sama kaki.
    6. Jika semua sisi berbeda, hasilnya segitiga sembarang.
    7. Jika tidak memenuhi syarat segitiga, program menyatakan bahwa ketiga sisi tidak membentuk segitiga.

5. Tugas 2 - Analisis Persamaan Kuadrat
    1. Memasukkan nilai koefisien a, b, dan c.
    2. Mengecek apakah a = 0.
    3. Jika a = 0, berarti bukan persamaan kuadrat.
    4. Jika a tidak sama dengan 0, menghitung diskriminan dengan rumus D = b² - 4ac.
    5. Jika D > 0, terdapat dua akar real yang berbeda.
    6. Jika D = 0, terdapat satu akar real kembar.
    7. Jika D < 0, tidak terdapat akar real.
    8. Untuk D > 0, menghitung nilai x1 dan x2.
    9. Untuk D = 0, menghitung nilai akar kembar.
## Hasil Pengujian

### Latihan 1 - Genap atau Ganjil

<table>
<tr><th>Input</th><th>Keluaran yang Diharapkan</th><th>Keluaran Aktual</th><th>Status</th></tr>
<tr><td>8</td><td>8 adalah bilangan genap</td><td>8 adalah bilangan genap</td><td>Berhasil</td></tr>
<tr><td>13</td><td>13 adalah bilangan ganjil</td><td>13 adalah bilangan ganjil</td><td>Berhasil</td></tr>
<tr><td>0</td><td>0 adalah bilangan genap</td><td>0 adalah bilangan genap</td><td>Berhasil</td></tr>
<tr><td>-7</td><td>-7 adalah bilangan ganjil</td><td>-7 adalah bilangan ganjil</td><td>Berhasil</td></tr>
</table>

### Latihan 2 - Membandingkan Dua Bilangan

<table>
<tr><th>Input</th><th>Keluaran yang Diharapkan</th><th>Keluaran Aktual</th><th>Status</th></tr>
<tr><td>7, 4</td><td>Bilangan pertama lebih besar</td><td>Bilangan pertama lebih besar</td><td>Berhasil</td></tr>
<tr><td>2, 9</td><td>Bilangan pertama lebih kecil</td><td>Bilangan pertama lebih kecil</td><td>Berhasil</td></tr>
<tr><td>5, 5</td><td>Kedua bilangan sama</td><td>Kedua bilangan sama</td><td>Berhasil</td></tr>
<tr><td>-3, -8</td><td>Bilangan pertama lebih besar</td><td>Bilangan pertama lebih besar</td><td>Berhasil</td></tr>
</table>

### Latihan 3 - Kelulusan Bersyarat

<table>
<tr><th>Nilai</th><th>Kehadiran</th><th>Keluaran yang Diharapkan</th><th>Keluaran Aktual</th><th>Status</th></tr>
<tr><td>75</td><td>90</td><td>Lulus</td><td>Lulus</td><td>Berhasil</td></tr>
<tr><td>59</td><td>90</td><td>Belum lulus</td><td>Belum lulus</td><td>Berhasil</td></tr>
<tr><td>75</td><td>79</td><td>Belum lulus</td><td>Belum lulus</td><td>Berhasil</td></tr>
<tr><td>60</td><td>80</td><td>Lulus</td><td>Lulus</td><td>Berhasil</td></tr>
</table>

### Latihan 4 - Jenis Segitiga

<table>
<tr><th>Sisi</th><th>Keluaran yang Diharapkan</th><th>Keluaran Aktual</th><th>Status</th></tr>
<tr><td>3, 3, 3</td><td>Segitiga sama sisi</td><td>Segitiga sama sisi</td><td>Berhasil</td></tr>
<tr><td>5, 5, 8</td><td>Segitiga sama kaki</td><td>Segitiga sama kaki</td><td>Berhasil</td></tr>
<tr><td>3, 4, 5</td><td>Segitiga sembarang</td><td>Segitiga sembarang</td><td>Berhasil</td></tr>
<tr><td>1, 2, 3</td><td>Tidak membentuk segitiga</td><td>Ketiga sisi tidak membentuk segitiga</td><td>Berhasil</td></tr>
</table>

### Tugas 2 - Analisis Persamaan Kuadrat

<table>
<tr><th>a</th><th>b</th><th>c</th><th>Keluaran yang Diharapkan</th><th>Keluaran Aktual</th><th>Status</th></tr>
<tr><td>1</td><td>-5</td><td>6</td><td>Dua akar real</td><td>Dua akar real: x1 = 3.00, x2 = 2.00</td><td>Berhasil</td></tr>
<tr><td>1</td><td>-4</td><td>4</td><td>Satu akar real kembar</td><td>Akar real kembar: x = 2.00</td><td>Berhasil</td></tr>
<tr><td>1</td><td>2</td><td>5</td><td>Tidak ada akar real</td><td>Tidak ada akar real</td><td>Berhasil</td></tr>
<tr><td>0</td><td>2</td><td>1</td><td>Bukan persamaan kuadrat</td><td>Bukan persamaan kuadrat.</td><td>Berhasil</td></tr>
</table>

## Refleksi
Setelah mengerjakan latihan dan Tugas 2, saya jadi lebih memahami penggunaan percabangan dalam Python. Kesalahan logika yang cukup mudah saya lakukan adalah salah menggunakan operator perbandingan, terutama membedakan > dengan >=. Saya mengatasinya dengan mencoba nilai batas seperti 59, 60, dan 61 sehingga bisa memastikan kondisi yang dibuat sudah sesuai. Saya juga belajar bahwa setiap cabang program perlu diuji, bukan hanya mencoba satu contoh saja