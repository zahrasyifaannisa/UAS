from view.input_nilai import *
data={}
class daftarNilai():
    def tambah_data(self):
        print('\n\033[95mTambah Data Mahasiswa')
        nambah_nama = nama()
        nambah_nim = nim()
        nambah_tugas = tugas()
        nambah_uts = uts()
        nambah_uas = uas()
        nambah_akhir = akhir()
        data[nambah_nama]=nambah_nim,nambah_tugas,nambah_uts,nambah_uas,nambah_akhir
        print('\n\033[93mData Berhasil Di ditambah!\n')
        
    def ubah_data(self):
        print('\n\033[95mMengubah Data Mahasiswa')
        ubah_nama = nama()
        if ubah_nama in data.keys():
            nambah_nim = nim()
            nambah_tugas = tugas()
            nambah_uts = uts()
            nambah_uas = uas()
            nambah_akhir = akhir()
            data[ubah_nama]=nambah_nim,nambah_tugas,nambah_uts,nambah_uas,nambah_akhir
            print('\n\033[97mData Berhasil Di diubah!\n')
        else:
            print('data tidak ditemukan !!!')  
    def hapus_data(self):
        hapus_nama = nama()
        if hapus_nama in data.keys():
            del data[hapus_nama]
            print('\n\033[94mData Berhasil Di dihapus!\n')
        else:
            print('data tidak ditemukan !!!')  
            
    
    def keluar(self):
        print('thank you')
    