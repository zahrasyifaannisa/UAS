def nama():
    global nm
    nm = input('\033[92mmasukan nama\t\t: ')
    return nm

def nim():
    global n
    n = input('masukan NIM\t\t: ')
    return n

def tugas():
    global tg
    tg = int(input('masukan nilai tugas\t: '))
    return tg

def uts():
    global ut
    ut = int(input('masukan nilai UTS\t: '))
    return ut

def uas():
    global ua
    ua = int(input('masukan nilai UAS\t: '))
    return ua

def akhir():
    global ak
    ak = (0.30*tg)+(0.35*ut)+(0.35*ua)
    return ak