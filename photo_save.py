import cv2
import time

# Kamera başlatma
cap = cv2.VideoCapture(0)

photo_count = 0

# İlk fotoğraf çekim zamanını kaydet
last_photo_time = time.time()

while True:
    # Kameradan bir frame yakalama
    ret, frame = cap.read()

    # Frame'i göster
    cv2.imshow('Camera', frame)

    # Klavyeden 'q' tuşuna basılırsa döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Belirli bir süre sonra fotoğraf çek
    current_time = time.time()
    if current_time - last_photo_time >= 2:  # 2 saniyede bir
        photo_count += 1
        photo_filename = f'photo{photo_count}.jpg'
        cv2.imwrite(photo_filename, frame)
        print(f'Photo saved as {photo_filename}')
        last_photo_time = current_time  # Sonraki fotoğraf çekim zamanını güncelle

# Kamera kapatma
cap.release()
cv2.destroyAllWindows()
