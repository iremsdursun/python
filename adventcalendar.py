import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

# Advent Calendar içerikleri
advent_calendar = {
    1: "Kodlama İpucu: 'Zen of Python'u okumak için Python terminaline 'import this' yazın. 😊",
    2: "Görev: Bir Python fonksiyonunda *args ve **kwargs kullanmayı deneyin!",
    3: "Eğlence: Bugün sadece karanlık temada kod yazın. ☕",
    4: "Kodlama İpucu: Kodunuzu daha temiz tutmak için 'PEP 8' kurallarına göz atın.",
    5: "Görev: Bir 'FizzBuzz' uygulaması yazın. Ancak bir 'lambda' kullanmayı deneyin.",
    6: "Eğlence: IDE'nizde hiç denemediğiniz bir kısa yol tuşunu öğrenin.",
    7: "Kodlama İpucu: 'list comprehension' ile kodunuzu kısaltabilirsiniz.",
    8: "Görev: Bir JSON dosyasını okuyup yazan bir program oluşturun.",
    9: "Eğlence: Kendi yazı tipinizi seçerek terminalinize kişisel dokunuş katın.",
    10: "Kodlama İpucu: Daha hızlı debug için 'pdb' modülünü öğrenin.",
    11: "Görev: Bir API'den veri çekmek için 'requests' modülünü kullanın.",
    12: "Eğlence: Sadece bir satırda bir Python programı yazın.",
    13: "Kodlama İpucu: Daha hızlı kod yazmak için bir 'snippet' aracı kullanın.",
    14: "Görev: Bir dosyayı zip formatında sıkıştıran bir program yazın.",
    15: "Eğlence: Şaka moduna girin ve her değişkene eğlenceli isimler verin. 😄",
    16: "Kodlama İpucu: Hataları daha iyi yönetmek için 'try-except' bloklarını kullanın.",
    17: "Görev: Python ile rastgele bir şifre oluşturucu yazın.",
    18: "Eğlence: Kendi 'ASCII sanatı' eserinizi yapın.",
    19: "Kodlama İpucu: Kodunuzu modüler hale getirmek için sınıfları deneyin.",
    20: "Görev: Bir 'Todo List' uygulaması yazın ve terminalde kullanın.",
    21: "Eğlence: Kod yazarken lo-fi müzik dinleyin. 🎵",
    22: "Kodlama İpucu: Performansı artırmak için 'generator'ları inceleyin.",
    23: "Görev: Python'da bir zamanlayıcı programı yazın.",
    24: "Mutlu Noeller! 🎄 Bugün açık kaynaklı bir projeye katkıda bulunun."
}

# Bugünün tarihini alalım
today = datetime.now()
current_day = today.day
current_month = today.month

# Yılbaşı renkleri paleti
christmas_colors = ["#FF0000", "#008000", "#FFFFFF", "#FFD700"]  # Kırmızı, Yeşil, Beyaz, Altın Sarısı

# GUI uygulaması
root = tk.Tk()
root.title("Advent Calendar - Yazılımcılar için")
root.geometry("600x400")
root.configure(bg="white")

# Bir kutuya tıklanınca açılma işlemi
def open_box(day):
    if day > current_day:  # Gelecek günler kilitli
        messagebox.showinfo("Kilitli", "Bu kutu henüz açılmadı!")
    else:  # Geçmiş ve bugünkü kutular açılabilir
        content = advent_calendar.get(day, "İçerik bulunamadı!")
        messagebox.showinfo(f"Gün {day}", content)

# Uyarı mesajları için başlık ekleme
header = tk.Label(
    root,
    text="🎄 Advent Calendar - Yazılımcılar için 🎄",
    bg="white",
    fg="black",
    font=("Arial", 16)
)
header.grid(row=0, column=0, columnspan=6, pady=10)  # Başlığı 6 sütuna yay

# Kutuları yerleştirelim (4x6 ızgara düzeni)
for day in range(1, 25):
    color = random.choice(christmas_colors)  # Yılbaşı renklerinden birini seç
    btn = tk.Button(
        root,
        text=str(day),
        width=8,
        height=3,
        bg=color,
        fg="black",
        command=lambda d=day: open_box(d),
    )
    btn.grid(row=(day - 1) // 6 + 1, column=(day - 1) % 6, padx=5, pady=5)  # +1 ile başlığı hesaba kat

# Tkinter modülü için ana döngüyü başlat
root.mainloop()

