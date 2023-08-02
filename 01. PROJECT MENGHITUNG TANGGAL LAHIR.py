print("""
==========================
01. PROJECT HITUNG TANGGAL LAHIR 
SOURCE CODE : © MNROMADONI
LIBRARY : DATETIME() => PYTHON
==========================\n\n
"""
)
#IMPORT LIBRARY DATE TIME
import datetime as dt

# INPUT NILAI ( TGL, BLN, THN ) ( NILAI INT )
tanggal = int(input("Masukkan Tanggal Lahir Anda : "))
bulan = int(input("Masukkan Bulan Lahir Anda : "))
tahun = int(input("Masukkan Tahun Lahir Anda : "))

#PROSES INPUT
tanggal_lahir = dt.date(tahun,bulan,tanggal)

# UBAH FORMAT DATE AND TIME DENGAN => strftime()
new_tanggal_lahir = tanggal_lahir.strftime("%A, %d %B %Y")

#PRINT TANGGAL LAHIR 
print("\n",15*"=")
print(f"Tanggal Lahir Anda Adalah : {new_tanggal_lahir}")
print(15*"=","\n")

#TANGGAL HARI INI
hari_ini =dt.date.today()
#CONVERT FORMAT
new_hari_ini=hari_ini.strftime("%A, %d %B %Y")

print(15*"=")
print(f"Hari Ini Adalah : {new_hari_ini}")
print(15*"=","\n")

#HITUNG UMUR DENGAN OPERATION
umur_hari = hari_ini - tanggal_lahir
print("Umur anda dalam hari : ", umur_hari,"\n")

#HITUNG UMUR TAHUN DAN BULAN
umur_tahun = umur_hari.days // 365
umur_bulan = ( umur_hari.days % 365 ) // 30
umur_hari = ( umur_tahun % 30 )


print("Jadi Umur Anda adalah ", umur_tahun, " Tahun ", umur_bulan, " Bulan ",umur_hari," Hari")
