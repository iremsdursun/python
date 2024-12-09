#1.soru :Girilen bir sayının 0-100 arsaında olup olmadığını bulun

number = int(input("Lutfen bir sayi giriniz:"))
print(number)

if number > 0 and number <100 :
    print("number sayisi 0-100 arasindadir.")
else :
    print("number sayisi 0-100 araliginda degildir.")

#2.soru :Girilen sayinin pozitif çift sayi olup olmadığını bulun

num = int(input("Lutfen bir sayi giriniz:"))
print(num)

if num > 0 and num % 2 == 0 :
    print("Girdiginiz deger hem bir cift sayidir hemde pozitiftir")
if num > 0 and num % 2 != 0 :
    print("Girdiginiz deger pozitif bir sayidie ama cift degildir")
else :
    print("Girdiginiz deger ne pozitiftir ne de cift sayidir.")

