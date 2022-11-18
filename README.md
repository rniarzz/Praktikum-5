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

- Selanjutnya tampilkan daftar datanya

```
print("==================================================================")
print("| No |    Nama      |  NIM  | Tugas |  UTS  |  UAS  |  Akhir |")
print("==================================================================")

i = 0

for nilai in data:
    i += 1
    print("| {no}  | {nama:12s} | {nim:5s} | {tugas:5d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |".format(no=i, nama=nilai[0], nim=nilai[1], tugas=nilai[2],uts=nilai[3],uas=nilai[4],akhir=nilai[5]))

print("==================================================================")
```

### OUTPUT

<img width="441" alt="screenshot 181" src="https://user-images.githubusercontent.com/115542704/202617912-3db0b820-e688-4218-a57e-b3f941e276f7.png">
