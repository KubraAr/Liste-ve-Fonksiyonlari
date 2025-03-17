#Liste Fonksiyonları
import random 

# Soru1: Listedeki Tekrarlanan Elemanları ve Kaç Kez Tekrar Ettiklerini Bulma

elemanlar = input("Liste elemanlarini girin: ").split()

tekrarlar = {}

for eleman in elemanlar:
    tekrarlar[eleman] = elemanlar.count(eleman)

print("Elemanlarin tekrar sayilari:")
for eleman, sayi in tekrarlar.items():
    print(f"{eleman}: {sayi} kez")



#Soru 2: Listedeki En Büyük İkinci Sayıyı Bulma

elemanlar = list(map(int, input("Liste elemanlarinigirin: ").split()))

if len(set(elemanlar)) < 2:
    print("Liste en az iki farkli sayi icermelidir.")
else:
    
    en_buyuk = max(elemanlar)

    elemanlar = [x for x in elemanlar if x != en_buyuk]
    ikinci_en_buyuk = max(elemanlar)

    print("En buyuk ikinci sayi:", ikinci_en_buyuk)



#Soru 3:  Listedeki Sayıları Küçükten Büyüğe ve Büyükten Küçüğe Sıralama

elemanlar = list(map(int, input("Liste elemanlarini girin: ").split()))

artan_sira = sorted(elemanlar)
azalan_sira = sorted(elemanlar, reverse=True)

print("Kucukten Buyuge sirali liste:", artan_sira)
print("Buyukten Kucuge sirali liste:", azalan_sira)


#Soru4: Liste Elemanlarını 2 ile Çarpma ve Yeni Liste Oluşturma

elemanlar = list(map(int, input("Liste elemanlarini girin: ").split()))

# Her elemanı 2 ile çarp ve yeni bir liste oluştur
yeni_liste = [x * 2 for x in elemanlar]

print("Yeni Liste:", yeni_liste)



#Soru5:  Listedeki Elemanları Rastgele Karıştırma

elemanlar = input("Liste elemanlarini girin: ").split()
random.shuffle(elemanlar)

print("Karistirilmis Liste:", elemanlar)





