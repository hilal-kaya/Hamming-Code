# Hamming-Code

# Proje Açıklaması

Bu proje, kullanıcıya 8-bit, 16-bit ve 32-bit veri girişi yaparak Hamming SEC-DED algoritması ile:

Kontrol bitlerinin hesaplanması,
Bellek kodunun oluşturulması,
Bellekteki hataların tespiti ve düzeltilmesi
işlemlerini gerçekleştiren bir grafik arayüz (GUI) sunar. Uygulama, PyQt5 kullanılarak geliştirilmiştir.

# Kullanılan Teknolojiler

Python 3
PyQt5
# Dosya Yapısı

BLM230_Proje_HilalKaya_22360859046/
│
├── app_main.py               # Ana arayüz dosyası
├── bit8_logic.py             # 8 bit hata kontrolü ve düzeltmesi
├── bit8_operations.py        # 8 bit GUI arayüzü
├── bit16_logic.py            # 16 bit hata kontrolü ve düzeltmesi
├── bit16_operations.py       # 16 bit GUI arayüzü
├── bit32_logic.py            # 32 bit hata kontrolü ve düzeltmesi
├── bit32_operations.py       # 32 bit GUI arayüzü
├── input_code.py             # Giriş penceresi
├── input_handler.py          # Giriş veri doğrulama işlemleri
└── __pycache__/              # Derlenmiş Python dosyaları
🚀 Nasıl Çalıştırılır?

Python 3 ve PyQt5 kurulu olduğundan emin olun:
pip install PyQt5
Ana arayüzü çalıştırmak için terminalden şu komutu verin:
python app_main.py
Açılan pencerede 8, 16 veya 32 bit seçeneklerinden biri seçilir ve işlem adımları takip edilir.
# Özellikler

Gerçek zamanlı giriş doğrulama
Hamming kontrol bitlerinin hesaplanması
Bellek kodunun oluşturulması
Tek bitlik hatanın tespiti ve düzeltilmesi
Çift bitlik hata durumunun tespiti
Detaylı hata raporu

<img width="1440" alt="Ekran Resmi 2025-06-08 21 36 41" src="https://github.com/user-attachments/assets/460689a7-4745-4fcf-8bd9-d77cc4c38ad1" />

![Uploading Ekran Resmi 2025-06-08 21.36.47.png…]()

<img width="1440" alt="Ekran Resmi 2025-06-08 21 37 07" src="https://github.com/user-attachments/assets/20115bc7-82be-4675-9b5e-46e3d29696f5" />





# Geliştirici
Hilal Kaya
BLM230 Dersi - 2025 Proje Ödevi

# Uygulama Videosu

https://www.youtube.com/watch?v=3Tz5BHAA9YQ
