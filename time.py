# TYPE WAKTU
# DEFINISI TYPE
# Type trigonomety: <J: jam, M: menit, D: detik>
# DEFINISI DAN SPESIFIKASI SELEKTOR (FUNGSI)
# jam: waktu --> integer [0...23]

def jam(w):
    return w[0]
#   {jam(w) untuk memasukan input berupa jam agar nilai nilai tertentu memiliki jam}

# menit: waktu --> integer [0...59]
def menit(w):
    return w[1]
#   {menit(w) untuk memasukan input berupa waktu agar suatu nilai tertentu dapat memiliki menit}

# detik: waktu --> integer [0...59]
def detik(w):
    return w[2]
#   {detik(t) untuk memasukan input berupa detik agar waktu dari suatu nilai memiliki detik}

# DEFINISI DAN SPESIFIKASI KONSTRUKSI 
# CreateWaktu: Integer [0...23], integer [0...59], integer [0...59] --> waktu
def CreateWaktu(j,m,d):
    return[j,m,d]
#   {Create(j,m,d) waktu pada jam, menit, dan detik yang bersangkutan}

# DEFINISI DAN SPESIFIKASI OPERATOR (WAKTU)
# After1Sec : w
#   {After1Sec(w) adalah fungsi untuk memajukan waktu 1 detik}
# Before1Sec : time --> time:
#   {Before1Sec(w) adalah fungsi untuk mundurkan waktu selama 1 detik}

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEq: 2 waktu --> boolean
#   {IsEq(w1, w2) adalah untuk membandingkan apakah kedua waktu tersebut adalah sama}
# IsBefore: 2 waktu --> boolean
#   {IsBefore(w1,w2) akan true jika w1 < w2 untuk membandingkan kedua buah waktu apakah w1 sebelum w2}
# IsAfter: 2 waktu --> boolean
#   {IsAfter(w1,w2) akan true jika w1 < w2 untuk membandingkan kedua buah waktu apakah w1 sesudah w2}

# REALISASI
def After1Sec(w):
    if detik(w) and menit(w) == 59:
        if jam(w)== 23:
            return CreateWaktu(0,menit(w)-59, detik(w)-59)
        else:
            return CreateWaktu(jam(w)+1, menit(w)-59, detik(w)-59)
    elif detik(w) == 59:
        return CreateWaktu(jam(w), menit(w)+1, detik(w)-59)
    else:
        return CreateWaktu(jam(w),menit(w),detik(w)+1)

def Before1Sec(w):
    if detik(w) and menit(w) == 0:
        if jam(w)== 0:
            return CreateWaktu(23, 59, 59)
        else:
            return CreateWaktu(jam(w)-1, 59, 59)
    elif detik(w) == 59:
        return CreateWaktu(jam(w), menit(w)+1, 59)
    else:
        return CreateWaktu(jam(w),menit(w),detik(w)-1)

def IsEq(w1,w2):
    return jam(w1) == jam(w2) and menit(w1) == menit(w2) and detik(w1) == detik(w2)

def IsBefore(w1,w2):
    if jam(w1) != jam(w2):
        return jam(w1) < jam(w2)
    elif menit(w1) != menit(w2):
        return menit(w1) < menit(w2)
    else:
        return detik(w1) < detik(w2)

def IsAfter(w1,w2):
    if jam(w1) != jam(w2):
        return jam(w1) > jam(w2)
    elif menit(w1) != menit(w2):
        return menit(w1) > menit(w2)
    else:
        return detik(w1) > detik(w2)

# APLIKASI
print(After1Sec(CreateWaktu(11,5,59)))
print(Before1Sec(CreateWaktu(10,0,19)))

print(IsEq(CreateWaktu(3,4,7),(CreateWaktu(3,4,7))))
print(IsBefore(CreateWaktu(2,3,4),CreateWaktu(2,3,2)))
print(IsAfter(CreateWaktu(3,3,4),CreateWaktu(3,3,4)))
