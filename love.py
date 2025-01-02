import pygame
import sys
import math

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel-Art Animasyon")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)
BLUE = (0, 0, 255)

# FPS ve saat
clock = pygame.time.Clock()
fps = 30

# Kalp çizimi
def draw_heart(x, y):
    """Kalp çizer."""
    pygame.draw.circle(screen, RED, (x - 10, y), 10)  # Sol üst yuvarlak
    pygame.draw.circle(screen, RED, (x + 10, y), 10)  # Sağ üst yuvarlak
    pygame.draw.polygon(screen, RED, [(x - 20, y), (x + 20, y), (x, y + 30)])  # Alt kısım

# Çöp adam karakterleri
def draw_man(x, y, is_girl=False):
    """Çöp adam çizer. Erkek veya kız belirlenebilir."""
    # Kafa
    pygame.draw.circle(screen, BLACK, (x, y - 50), 20, 2)  # Kafa çemberi
    # Yüz detayları
    pygame.draw.circle(screen, BLACK, (x - 7, y - 55), 3)  # Sol göz
    pygame.draw.circle(screen, BLACK, (x + 7, y - 55), 3)  # Sağ göz
    pygame.draw.arc(screen, BLACK, (x - 10, y - 45, 20, 10), 3.14, 6.28, 2)  # Tebessüm
    # Saçlar
    if is_girl:
        for i in range(-20, 21, 10):  # Kıvırcık saç
            pygame.draw.circle(screen, BLACK, (x + i, y - 70), 10, 2)
    # Gövde
    pygame.draw.line(screen, BLACK, (x, y - 30), (x, y + 20), 2)
    # Kollar
    pygame.draw.line(screen, BLACK, (x, y - 20), (x - 30, y), 2)
    pygame.draw.line(screen, BLACK, (x, y - 20), (x + 30, y), 2)
    # Bacaklar
    pygame.draw.line(screen, BLACK, (x, y + 20), (x - 20, y + 60), 2)  # Sol bacak
    pygame.draw.line(screen, BLACK, (x, y + 20), (x + 20, y + 60), 2)  # Sağ bacak
    # Ayakkabılar
    pygame.draw.rect(screen, BLACK, (x - 25, y + 55, 10, 5))  # Sol ayakkabı
    pygame.draw.rect(screen, BLACK, (x + 15, y + 55, 10, 5))  # Sağ ayakkabı
    # Elbise (sadece kız için)
    if is_girl:
        pygame.draw.polygon(screen, PINK, [(x, y - 20), (x - 20, y + 20), (x + 20, y + 20)])

# Ana döngü
man_x, man_y = 200, 400  # Erkek çöp adam pozisyonu
girl_x, girl_y = 600, 400  # Kız çöp adam pozisyonu
heart_x, heart_y = 400, 300  # Kalbin pozisyonu
heart_direction = 1  # Kalbin yukarı-aşağı hareket yönü

# Hareket parametreleri
speed = 1  # Hız
max_distance = 120  # Kalpten maksimum mesafe
approaching = True  # Çöp adamların yaklaşma durumu

while True:
    screen.fill(WHITE)

    # Çöp adamlar arasındaki mesafeyi hesapla
    def move_towards(x, y, target_x, target_y):
        """Verilen x, y noktasına doğru hareket et."""
        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        # Mesafe 0'dan küçükse, hedefe ulaşmış demektir
        if distance < 1:
            return target_x, target_y
        
        # Yön hesaplaması
        dx /= distance
        dy /= distance

        # Hedefe doğru hareket et
        new_x = x + dx * speed
        new_y = y + dy * speed
        return new_x, new_y

    # Çöp adamları hareket ettir
    if approaching:
        man_x, man_y = move_towards(man_x, man_y, heart_x, heart_y)
        girl_x, girl_y = move_towards(girl_x, girl_y, heart_x, heart_y)
        
        # Eğer çöp adamlar kalbe çok yakınsa, uzaklaşmaya başla
        if math.sqrt((man_x - heart_x) ** 2 + (man_y - heart_y) ** 2) < max_distance:
            approaching = False
    else:
        man_x, man_y = move_towards(man_x, man_y, man_x - (heart_x - man_x), man_y - (heart_y - man_y))
        girl_x, girl_y = move_towards(girl_x, girl_y, girl_x - (heart_x - girl_x), girl_y - (heart_y - girl_y))
        
        # Eğer çöp adamlar kalpten uzaklaştıysa, tekrar yaklaşmaya başla
        if math.sqrt((man_x - heart_x) ** 2 + (man_y - heart_y) ** 2) > max_distance:
            approaching = True

    # Çöp adamları çiz
    draw_man(man_x, man_y, is_girl=False)  # Erkek
    draw_man(girl_x, girl_y, is_girl=True)  # Kız

    # Kalbi çiz ve hareket ettir
    draw_heart(heart_x, heart_y)
    heart_y += heart_direction
    if heart_y > 310 or heart_y < 290:
        heart_direction *= -1

    # Olayları dinle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Görüntüyü güncelle
    pygame.display.flip()
    clock.tick(fps)

