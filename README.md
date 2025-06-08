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
# Geliştirici

Hilal Kaya
BLM230 Dersi - 2025 Proje Ödevi

# Uygulama Videosu

https://www.youtube.com/watch?v=3Tz5BHAA9YQ
