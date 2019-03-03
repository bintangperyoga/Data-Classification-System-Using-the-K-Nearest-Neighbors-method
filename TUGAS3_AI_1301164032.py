# Nama    : Bintang Peryoga
# NIM     : 13.01.16.4032
# IF-40-04
# TUPRO 3
import csv
from statistics import mode, StatisticsError

def most_common(L):
# source dari https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
    try:
        return mode(L)
    except StatisticsError as e:
        if 'no unique mode' in e.args[0]:
            return L[0]
        raise

# membuat array baru dari data Test
datafile = open("DataTest_Tugas3_AI.csv", "r")
data = csv.reader(datafile)
dataTest = []
for row in data:
    dataTest.append(row)

# membuat array baru dari data Train
datafile = open("DataTrain_Tugas3_AI.csv", "r")
data = csv.reader(datafile)
dataTrain = []
for row in data:
    dataTrain.append(row)

# nilai K = 5
hasil = []
selisih = []
temp = [0, 0, 0, 0, 0]
for j in range(1,len(dataTest)):
    for m in range(1,len(dataTrain)):
        a = 0
        for l in range(1,6):
            a = a + abs(float(dataTrain[m][l]) - float(dataTest[j][l]))
        selisih.append([a,dataTrain[m][6]])

    # data selisih yang sudah terkumpul, disorting secara ascending
    selisih.sort()

    # 5 data teratas diambil.
    # jika data terkecil atau data ke-1 selisihnya tidak ada yang sama, maka data ke-1 diambil
    # jika data terkecil atau data ke-1 selisihnya ada yang sama, maka menggunakan fungsi most_common
    # yang tujuannya mengambil angka terbanyak yang muncul
    adayangsama = False
    for p in range(0,5):
        temp[p] = selisih[p][1]
    for q in range(1,5):
        if selisih[0][0] == selisih[p][0]:
            if selisih[0][1] != selisih[p][1]:
                adayangsama = True
    if adayangsama == False:
        hasil.append(selisih[0][1])
    elif adayangsama == True:
        hasil.append(most_common(temp))
    del selisih[0:800]

# hasil diconvert ke file .csv
datahasil = open('TebakanTugas3.csv', 'w')
datahasill = csv.writer(datahasil, lineterminator='\n')
for d in hasil:
    datahasill.writerow([d])
datahasil.close()