# Fiyat Karşılaştırma Siteleri Üzerine Anket Analizi

Bu proje, fiyat karşılaştırma siteleriyle ilgili yürütülen bir anket çalışmasının analizlerini içermektedir. Çalışma kapsamında, 122 katılımcıdan toplanan veriler üzerinde istatistiksel testler ve görsel analizler uygulanmıştır.

## Hazırlayan
**Buse Sudenaz Bakal**, **Sümeyye Şahin**  
Yönetim Bilişim Sistemleri

## Projenin Amacı
Bu projenin temel amacı, fiyat karşılaştırma sitelerinin kullanıcı algıları, davranışları ve eğilimleri üzerindeki etkisini anlamaktır. Anket, 5’li Likert ölçeği kullanılarak hazırlanmış 16 sorudan oluşmaktadır.

## Veri Seti
- `colab_anket_verisi.csv`: Anket katılımcılarının yanıtlarını içerir.

## Kullanılan Yöntemler ve Analizler
- **Normallik Testi (Shapiro-Wilk):** Verilerin normal dağılıp dağılmadığı test edilmiştir.
- **Güvenilirlik Analizi (Cronbach's Alpha):** Anketin tutarlılığı ölçülmüştür.
- **ANOVA Testi:** Eğitim, yaş ve harcama düzeylerine göre farklılık analizi yapılmıştır.
- **T-Testi:** Cinsiyete göre yanıt farklılıkları test edilmiştir.
- **Korelasyon Matrisi:** Likert soruları arasındaki ilişkiler görselleştirilmiştir.

## Üretilen Grafikler
- Cinsiyete Göre Isı Haritası
- Eğitim Düzeyine Göre Ortalama Yanıtlar
- Harcama Düzeyine Göre Soru Bazlı Ortalama Tablosu
- Cinsiyet, Eğitim, Harcama ve Yaş'a Göre P-Değeri Karşılaştırma Grafikleri
- Histogramlar ve Dağılım Grafikleri

## Kütüphaneler
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`

## Kullanım
Google Colab üzerinde çalıştırılmak üzere hazırlanmıştır. `.csv` dosyası yüklenerek aşağıdaki adımlarla analizler tekrarlanabilir:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, shapiro, levene, kruskal
```

## Lisans
Bu proje akademik kullanım içindir. Kaynak gösterilerek kullanılabilir.
