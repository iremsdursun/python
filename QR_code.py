import qrcode
import qrcode.constants # QR kod oluşturmak için gerekli kütüphaneyi dahil ediyoruz

konumBaglanti = "https://g.co/kgs/SUo4hi1" # Google haritaalrdan konum kopyalaıyoruz

qr = qrcode.QRCode(
    version = 1, # QR kodun boyutunu bwlirler. 1-40 değeri arasında seçilir.dğer arttıkça veri boyutu ve saklma alanı artar
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 15,
    border = 7,
)

qr.add_data(konumBaglanti) # konum bağlantısını QR koda ekler
qr.make(fit = True)  # QR kodun en uygun boyutta olmasını sağlar

qr_resim = qr.make_image(dolgu="siyah", arka_plan="beyaz") #QR kodu oluşturup renklendirme aşamaası

qr_resim.save =("konum_qr.png") # Qr kodu adıyla kaydedip görsel oluşturuyor.

qr_resim.show() # QR kodu göstermek için 