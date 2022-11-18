# Nama: Rini Ariza
# Nim: 312210337
# Kelas: TI.22.A3

## Tugas praktikum 5
### Soal

<img width="579" alt="Screenshot 180" src="https://user-images.githubusercontent.com/115542704/202370020-187d2651-fd02-4dbf-b415-670ad56cbbbf.png">

- Pertama buat dulu list kosong untuk menampung data-data yang ingin diinputkan

  `data = []`

- Pada program ini gunakan perulangan While

  **While** pada python, secara umum akan menjalankan sebuah perintah atau statement selama kondisi tersebut terpenuhi atau kondisi tersebut bernilai TRUE.

    Jadi pada saat argument tersebut terpenuhi (TRUE) maka statement tersebut akan terus di proses atau dilaksanakan, dan sebaliknya jika argumentnya tidak terpenuhi   (FALSE) maka statement tersebut akan berhenti atau tidak dilaksanakan.

- Kemudian gunakan fungsi input() untuk memasukkan data

```
while True:
    nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
```
    
- Untuk menambahkan daftar list gunakan perintah `.append()`

```
 data.append([nama, nim, tugas, uts, uas, int(akhir)])
```

- While disini digunakan untuk melakukan perulangan input ingin menambah data atau tidak (y/t)

```
    more = ""
    while more != "y" and more != "t":
        more = input("Tambah Data(y/t)?")
```

- Perintah if disini digunakan jika data tidak ingin ditambahkan lagi (t) kemudian tambahkan perintah break untuk menghentikan proses perulangan pada kondisi tertentu

```
    if more == "t":
        break
```
