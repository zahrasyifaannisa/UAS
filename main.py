from model.daftar_nilai import daftarNilai
from view.view_nilai import melihat 
while True:
    data = daftarNilai()
    em = melihat()
    print('tambah\t(1)\nubah\t(2)\nhapus\t(3)\nlihat\t(4)')
    a = input('masukan pilihan > ')
    if (a=="1"):
        data.tambah_data()
    elif (a=="2"):
        data.ubah_data()
    elif (a=="3"):
        data.hapus_data()
    elif (a=="4"):
        em.cetak_daftar_nilai()
    else :
        data.keluar()
        break
