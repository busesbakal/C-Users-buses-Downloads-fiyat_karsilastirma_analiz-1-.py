
# 1. Gerekli Kütüphaneleri Yükle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, ttest_ind, f_oneway
from sklearn.preprocessing import LabelEncoder

# 2. CSV Dosyasını Oku
df = pd.read_csv("colab_anket_verisi.csv")

# 3. Veriyi Sayısallaştır (Eğer gerekli ise)
likert_map = {
    "1 = Hiç Katılmıyorum": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5 = Kesinlikle Katılıyorum": 5,
    "Hiç Katılmıyorum": 1,
    "Kesinlikle Katılıyorum": 5
}
df.replace(likert_map, inplace=True)

# 4. Normallik Testi (Shapiro-Wilk)
from scipy.stats import shapiro

results = []
for col in df.columns:
    if col.startswith("Soru"):
        stat, p = shapiro(df[col].dropna().astype(float))
        sonuc = "Normal dağılıyor" if p > 0.05 else "Normal dağılmıyor"
        results.append({"Soru": col, "Test istatistiği": stat, "p-değeri": p, "Yorum": sonuc})
normallik_df = pd.DataFrame(results)

# 5. Güvenilirlik Analizi (Cronbach's Alpha)
def cronbach_alpha(df_subset):
    df_corr = df_subset.corr()
    k = df_subset.shape[1]
    item_var_sum = df_subset.var(axis=0, ddof=1).sum()
    total_var = df_subset.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - (item_var_sum / total_var))

likert_cols = [col for col in df.columns if col.startswith("Soru")]
alpha = cronbach_alpha(df[likert_cols].astype(float))

# 6. Histogram (Fiyat karşılaştırma siteleriyle ilgili sorular için)
fiyat_sorular = [col for col in df.columns if "fiyat" in col.lower() or "karşılaştırma" in col.lower()]
for col in fiyat_sorular:
    plt.figure()
    df[col].dropna().astype(float).hist()
    plt.title(f"{col} Histogramı")
    plt.xlabel("Değerler")
    plt.ylabel("Frekans")
    plt.tight_layout()
    plt.savefig(f"{col}_hist.png")

# 7. Cinsiyete Göre T-Testi
t_results = []
for col in likert_cols:
    groups = df.groupby("Cinsiyet")[col].apply(lambda x: x.dropna().astype(float))
    if "Kadın" in groups and "Erkek" in groups:
        stat, p = ttest_ind(groups["Kadın"], groups["Erkek"], equal_var=False)
        yorum = "Anlamlı fark var" if p < 0.05 else "Anlamlı fark yok"
        t_results.append({"Soru": col, "T istatistiği": stat, "p-değeri": p, "Yorum": yorum})
t_test_df = pd.DataFrame(t_results)

# 8. Eğitim Düzeyine Göre ANOVA
anova_results = []
for col in likert_cols:
    gruplar = [gr.dropna().astype(float) for ad, gr in df.groupby("Eğitim")[col]]
    stat, p = f_oneway(*gruplar)
    yorum = "Anlamlı fark var" if p < 0.05 else "Anlamlı fark yok"
    anova_results.append({"Soru": col, "F istatistiği": stat, "p-değeri": p, "Yorum": yorum})
anova_df = pd.DataFrame(anova_results)

# 9. Korelasyon Matrisi
plt.figure(figsize=(10, 8))
sns.heatmap(df[likert_cols].astype(float).corr(), annot=True, cmap="Reds")
plt.title("Likert Soruları Arası Korelasyon Matrisi")
plt.tight_layout()
plt.savefig("korelasyon_matrisi.png")
