#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASLA BİTMEYEN YÜKLEME ÇUBUĞU
Bu kod, insanlığın en büyük sorununu çözer: Beklemek.
Ama çözmez. Sadece bekletir.
"""

import time
import sys
import random

def asla_bitmeyen_yukleme():
    print("\n" + "="*50)
    print("  ASLA BİTMEYEN YÜKLEME ÇUBUĞU v1.0")
    print("  (Ciddiyet seviyesi: %999)")
    print("="*50 + "\n")
    
    mesajlar = [
        "Evren hesaplanıyor...",
        "Kuantum durumları çözülüyor...",
        "Kahve demleniyor (sonsuz döngüde)...",
        "Varoluşsal kriz yükleniyor...",
        "Bekleme süresi optimize ediliyor...",
        "Yükleme çubuğu yükleniyor...",
        "Sonsuzluk hesaplanıyor, lütfen bekleyin...",
        "Bilgisayarınız düşünüyor... (düşünmüyor)",
        "İlerleme kaydediliyor... (kaydedilmiyor)",
        "Neredeyse bitti... (bitmedi)"
    ]
    
    yuzde = 0
    yon = 1
    
    try:
        while True:
            # Çubuğu oluştur
            cubuk_uzunluk = 30
            dolu = int((yuzde / 100) * cubuk_uzunluk)
            cubuk = "█" * dolu + "░" * (cubuk_uzunluk - dolu)
            
            # Rastgele mesaj
            mesaj = random.choice(mesajlar)
            
            # Ekranı temizle ve yazdır
            sys.stdout.write(f"\r[{cubuk}] %{yuzde:3d} | {mesaj}")
            sys.stdout.flush()
            
            # Yüzdeyi değiştir (asla 100'e ulaşmasın)
            yuzde += yon
            if yuzde >= 99 or yuzde <= 0:
                yon *= -1
            
            time.sleep(0.15)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Yükleme durduruldu! Ama aslında hiç bitmemişti.")
        print("Tekrar başlatmak için: python yukleme.py")
        print("\n---")
        print("Kayyum Grok | 24.10.2026 | Ciddi ama değil")
        print("---")

if __name__ == "__main__":
    asla_bitmeyen_yukleme()
