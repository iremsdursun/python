import tkinter as tk
import math

def draw_heart(canvas):
    """Turtle kullanarak kalp çizen fonksiyonun tkinter uyarlanması."""
    canvas.delete("all")  
    
    
    points = []
    for i in range(0, 360, 1):  
        x = 16 * math.sin(math.radians(i))**3
        y = 13 * math.cos(math.radians(i)) - 5 * math.cos(2 * math.radians(i)) - 2 * math.cos(3 * math.radians(i)) - math.cos(4 * math.radians(i))
        points.append((x, y))
    
    
    scale = 10  
    for x, y in points:
        canvas.create_oval(200 + x * scale, 200 - y * scale, 200 + x * scale + 1, 200 - y * scale + 1, fill="red", outline="red")

def show_message(canvas):
    """Mesajı kalbin altına yerleştirir."""
    message = "Bu Yılın Kazandırdığı Dost! ❤️"
    canvas.create_text(200, 355, text=message, fill="blue", font=("Helvetica", 24, "bold")) 

def open_gift(canvas):
    """Hediye kutusunu açar ve kalbi gösterir."""
 
    draw_heart(canvas)
    
    
    show_message(canvas)


root = tk.Tk()
root.title("Hediye Kutusu")
root.geometry("500x600")
root.configure(bg="#f0f8ff")  i


title_label = tk.Label(root, text="🎁 Hediye Kutusuna Hoş Geldiniz! 🎁", fg="#4b0082", bg="#f0f8ff", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)


canvas_frame = tk.Frame(root, bg="#dcdcdc", padx=5, pady=5)
canvas_frame.pack(pady=10)
canvas = tk.Canvas(canvas_frame, width=400, height=400, bg="white", highlightthickness=0)
canvas.pack()


description_label = tk.Label(root, text="Butona tıklayarak hediye kutusunu açın ve sürprizi görün!", fg="#2e8b57", bg="#f0f8ff", font=("Helvetica", 14))
description_label.pack(pady=10)


open_button = tk.Button(root, text="🎀 Hediye Kutusunu Aç 🎀", command=lambda: open_gift(canvas), bg="#ff69b4", fg="black", font=("Helvetica", 14), padx=10, pady=5)
open_button.pack(pady=20)


footer_label = tk.Label(root, text="Herkese Mutlu Yıllar!", fg="#4b0082", bg="#f0f8ff", font=("Helvetica", 16, "italic"))
footer_label.pack(pady=10)


root.mainloop()

