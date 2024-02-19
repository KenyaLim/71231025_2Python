#melamar pekerjaan untuk liburan selama 5 minggu
#gaji perjam
#pajak penghasilan 14%
#budi menghabiskan 10% dari pendapatan bersih - untuk sem baru
# 1% untuk alat tulis
#25% untuk disedekahkan
#setiap 1000 bdui sedekahkan 30%, sisa untuk kaum duafa

gajiperjam = float(input("Gaji perjam = "))
jam = int(input("Jam kerja selama 1 minggu = "))

gajisblmpajak = gajiperjam * jam * 5
gajistlhpajak = gajisblmpajak - gajisblmpajak *(14/100)
uangstlhsembaru = gajistlhpajak * 10/1008
uangstlhsembaru2 = gajistlhpajak * 1/100

sedekah = 0.25  * (gajistlhpajak - uangstlhsembaru - uangstlhsembaru2)
y = 0
d = 0
while sedekah > 1000:
    sedekah-=1000
    y+=(1000 * (30/100))
    d+=(1000 * (70/100))

print(f"Gaji selama liburan musim panas sebelum pajak = {gajisblmpajak}")
print(f"Gaji selama liburan musim panas setelah pajak = {gajistlhpajak}")
print(f"Jumlah uang yang dihabiskan untuk pakaian dan aksesoris = {uangstlhsembaru}")
print(f"Jumlah uang yang dihabiskan untuk alat tulis = {uangstlhsembaru2}")
print(f"Sedekah = {sedekah}")
print(f"Jumlah yang diterima oleh yatim = {y}")
print(f"Jumlah yang diterima oleh duafa = {d}")