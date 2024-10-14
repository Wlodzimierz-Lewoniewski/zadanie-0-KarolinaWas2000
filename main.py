import re

# Pobranie liczby zdań
liczba_zdan = int(input("Podaj liczbę zdań: "))

# Pobranie zdań
zdania = []
for _ in range(liczba_zdan):
    zdanie = input("Podaj zdanie: ")
    zdania.append(zdanie)

# Pobranie liczby słów do sprawdzenia
liczba_slow = int(input("Podaj liczbę słów: "))

# Pobranie słów do sprawdzenia
slowa_do_policzenia = []
for _ in range(liczba_slow):
    slowo = input("Podaj słowo do policzenia: ")
    slowa_do_policzenia.append(slowo)

# Funkcja do liczenia i sortowania zdań według wystąpień słowa
def sortuj_zdania(slowo, zdania):
    licznik_slow = []
    for i, zdanie in enumerate(zdania):
        # Dzielimy zdanie na słowa, ignorując interpunkcję
        slowa_w_zdaniu = re.findall(r'\b\w+\b', zdanie.lower())
        licznik = slowa_w_zdaniu.count(slowo.lower())
        if licznik > 0:
            licznik_slow.append((i, licznik))

    def sortowanie(pary):
        return (-pary[1], pary[0])  # Sortowanie według liczby wystąpień malejąco, a potem według indeksu rosnąco

    licznik_slow.sort(key=sortowanie)

    # Zwracanie indeksów zdań, tylko jeżeli słowo wystąpiło w zdaniu
    return [indeks for indeks, _ in licznik_slow]

for slowo in slowa_do_policzenia:
    wynik = sortuj_zdania(slowo, zdania)
    print(wynik)