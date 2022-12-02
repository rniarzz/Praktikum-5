data = []

print('| Nama\t: rini ariza\t|\n| NIM\t: 312110337\t    |\n| Kelas\t: TI.22.A3\t    |')
print(25*'=','\n')
print('progam menambah data mahasiswa\n')
while True:
    nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
    data.append([nama, nim, tugas, uts, uas, int(akhir)])

    more = ""
    while more != "y" and more != "t":
        more = input("Tambah Data(y/t)?")
    if more == "t":
       break

print("==================================================================")
print("| No |    Nama      |  NIM  | Tugas |  UTS  |  UAS  |  Akhir |")
print("==================================================================")

i = 0

for nilai in data:
    i += 1
    print("| {no}  | {nama:12s} | {nim:5s} | {tugas:5d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |".format(no=i, nama=nilai[0], nim=nilai[1], tugas=nilai[2],uts=nilai[3],uas=nilai[4],akhir=nilai[5]))

print("==================================================================")