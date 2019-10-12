nama = 'meta riani ananda'
program = 'gerak lurus'

print(f'Program {program} oleh {nama}')

def hitung_tegangan(arus , hambatan):
    tegangan = arus * hambatan
    print(f'arus = {arus * 30}A dengan hambatan = {hambatan * 8}ohm')
    print(f'sehingga tegangan = {tegangan} volt')
    return arus * hambatan

#arus = 30
#hambatan = 8
tegangan = hitung_tegangan(30, 8)
tegangan = hitung_tegangan(45, 6)

