import random # pythonda random modülünü kullanmamiz için gerekli

randomNum = random.randint(1,10) #1-100 arasında rasegle bir sayi üretir
can = int(input("Lütfen kaç adet hak istediginizi giriniz:"))
hak = can
sayac = 0

while hak > 0 :
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))

    if randomNum == tahmin :
        print(f'Tebriklerr, {sayac}.tahminde bildiniz.Toplam puaniniz:{100 - (100 / can) * (sayac - 1)}')
        break
    elif randomNum > tahmin :
        print("yukari")
    else :
        print("aşagi")

    if hak == 0 :
        print(f'hakkiniz bitmisitir.Tutulan sayi:{randomNum}')