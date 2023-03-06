import numpy as np
import scipy.stats as st

fb = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hc = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
wl = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

print(st.shapiro(fb), st.shapiro(hc), st.shapiro(wl))

print(st.bartlett(fb, hc, wl))

# Мы обнаружили, что данные у нас подчиняются нормальному распределению и что нет достаточных доказательств,
# чтобы предполагать, что дисперсии не равны.

k = 3
n = len(fb) + len(hc) + len(wl)

fb_mean = np.mean(fb)
hc_mean = np.mean(hc)
wl_mean = np.mean(wl)


total = np.array([173, 175, 180, 178, 177, 185, 183, 182, 177, 179, 180, 188, 177, 172, 171, 184, 180, 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

total_mean = np.mean(total)

s = np.sum((total - total_mean) ** 2)

sf = np.sum((fb_mean - total_mean) ** 2) * len(fb) + np.sum((hc_mean - total_mean) ** 2) * len(hc) + np.sum((wl_mean - total_mean) ** 2) * len(wl)

so = np.sum((fb - fb_mean) ** 2) + np.sum((hc - hc_mean) ** 2) + np.sum((wl - wl_mean) ** 2)

df = sf / (k - 1) 
do = so / (n - k)

F = df / do

print(F)

f = st.f_oneway(fb, hc, wl)
print(f)

# p-value у нас меньше 0.05 и поэтому мы делаем вывод, что есть статистически значимые различия в росте между спортсменами разных категорий