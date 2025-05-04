# 1.soru : 1 ile 100 arasındaki tam sayılardan oluşan vektörü oluşturunnuz

sayii <- 1:100
print(sayii)

# 2.soru : Bir vektör x <- c(25,43,21,12,55,67,89,59,67,83) biçiminde yaratıldığına göre x[3] ve x[9] değerlerini bulan R kodunu yazınız.

x <- c(25,43,21,12,55,67,89,59,67,83)
ucuncu_eleman <- x[3]
dokuzuncu_eleman <- x[9]
print(ucuncu_eleman)
print(dokuzuncu_eleman)

length(x)
# 3. soru: Yukarıdaki vektörün eleman sayısını bulan R kodunu yazınız

boy <- c(175, 166, 180, 185, 160)
toplam_boy <- sum(boy)
print(toplam_boy)

# 4.soru: Tablonun Boy sütununda yer alan veriyi bir vektöre yerleştirerek toplamını hesaplayan R kodlarını yazınız.

ortalama_boy <- mean(boy)
print(ortalama_boy)

# 5.soru: Tablonun Boy sütununda yer alan verilerin ortalamasını hesaplayan R kodlarını yazınız

print(mean(boy))

# 6.soru: Bir x <- c(11,15,9,7,12,13) vektörünü göz önüne alalım. Bu vektörün içerdiği veriler arasından 10’dan büyük olanları seçerek bulan R kodlarını yazınız

x <- c(11,15,9,7,12,13)
buyuk_olanlar <- x[x > 10]
print(buyuk_olanlar)

# 7.soru: İsimlerden oluşan birinci sütundaki veriyi bir vektör içinde tanımlayarak vektörün yaratılmasını sağlayan R kodlar
isimler <- c("Halit", "Mehmet", "Ersin", "Suat", "Tuncer")

# 8.soru:
x <- c(3, 22, 11, 19, 16, 25)
x[4] <- 11
print(x)

# 9.soru:
x <- x[-3]
print(x)

# 10.soru:
x <- c(12, 2, 4, 17, 13, 19, 6, 24, 15, 23)
x <- x[-c(3:5)]
print(x)

# 11.aoru:
x <- NULL
print(x)
show(x)
# 12.soru:
x <- sort(x)
x
# 13.soru:
iller <- c("ANKARA", "ANKARA", "İSTANBUL", "İZMİR", "ANKARA", "İZMİR")
iller_faktor <- as.factor(iller)
show(iller_faktor)
# 14.soru:
levels(iller_faktor)[levels(iller_faktor) == "İSTANBUL"] <- "ANTALYA"
show(iller_faktor)
# 15.soru:

iller_faktor <- factor(c(as.character(iller_faktor), "SİNOP"))
show(iller_faktor)
