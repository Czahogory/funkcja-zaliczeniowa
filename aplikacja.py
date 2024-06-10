
print("wprowadz liczby odzielone spacja")
wej = input() 
try :
    tab = list(map(int, wej.split(' ')))
except ValueError : 
    print("liczby powinny byc rozdielone jedna spacja")
tab = list(map(int, wej.split(' ')))# pobiera dane i robi  z ich liste 
sortab = sorted(tab)                   # sortuje
n = len(tab)                           # dlugosc listy
i = 0
x = 0
while i < n:                           # sumuje elementy listy
    x += tab[i]
    i += 1
y = x/n                                # średnia
m = n/2
if n%2 == 0 :                          #mediana jeżeli długość listy jest pparzysta sumuje dwa elementy
    j = int(m)
    z1 = sortab[j] + sortab[j-1]
    z2 = z1/2
    print("funkcja")
else: j = round(m)
z2 =sortab[j-1]
print("sort ",sortab)
print("suma ",x)
print("średnia  ",round(y))
print("max ",max(tab))
print("min ",min(tab))
print("mediana",z2)