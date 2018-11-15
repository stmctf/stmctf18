## Soru İsmi: CIPHER201
Hazırlayan: [mertcan](https://twitter.com/mertcancoskuner)
## Soru Metni: 

Lisede derste sıkıldığın için arkadaşlarına kaynatmak için kağıda yazarak attığın mesajları hocanın okumasını istemiyorsun. 
Hoca da basit kripto algoritmalarından haberi olan birisi. Arkadaşlarınla mesajlaşabilmek için bir şifreleme algoritması 
programlamanız gerekiyor.

Programlayacağın şifreleme algoritması bir Transposition Cipher* türü olan Route Cipher**. 

*Transposition Cipher: Açık metin bir sisteme göre kaydırılarak oluşturulur. Sonucunda ortaya çıkan şifrelenmiş metin açık metinin permutasyon hali olur.

**Route Cipher: Açık metin matris şekline getirildikten sonra anahtar olarak verilen kalıba (pattern) göre ayarlanır.

**Algoritma ile ilgili detaylar**

- Route Cipher için kullanılacak anahtar kalıp ise saat yönü ya da saat yönünün tersi şeklinde döndürme olacak. 
- Açık metin içerisinde noktalama işaretleri olsa da, şifrelenmiş metinde olmayacak. 
- Açık metin içerisinde yer alan harflerin büyüklüğü ya da küçüklüğü ne olursa olsun, şifrelenmiş metindeki tüm harfler büyük harf olacak.
- Input parametresi olarak matris boyutu ve rotasyonun yönü verilecek.
- Matrise koyulan açık metin soldan başlayarak sağa doğru koyulacak.
- Eğer açık metin matrise yerleştirilirken boşluklar kalırsa, bu boşluklar türkçe kelimelerde en az geçen harflerden biri olan N ile doldurulacak.
- Şifreleme sağ üstten başlayarak spiral şeklinde dışarıdan içeri doğru saat yönü ya da saat yönünün tersi şeklinde şifreleme yapacak.

**Algoritma ile ilgili örnek**

- Örnek açık metin: BU BIR ORNEKTIR. PANIK YAPMAYIN.
- Örnek boyut: (9, 3)
- Örnek döndürme: saat yönü
- Verilecek girdi: ("BU BIR ORNEKTIR. PANIK YAPMAYIN.", (9, 3), 'saatyonu')
- (9x3) Matrisinde örnek açık metin aşağıdaki gibi görünmektedir

    ```
    B 	U 	B 	I 	R 	O 	R 	N 	E

    K 	T 	I 	R 	P 	A 	N 	I 	K

    Y 	A 	P 	M 	A 	Y 	I 	N 	N
    ```

- Matrise sağ üstten başlayarak dışarıdan içeriye doğru saat yönünde döndürme işlemi yapıldığında şifreli metin aşağıdaki gibi görünmektedir
    ```
    EKNNIYAMPAYKBUBIRORNINAPRIT
    ```
- Bayrağın bulunması için aşağıdaki metinler anlatılan algoritma ile işlenerek uç uca ekleme ile birleştirilmelidir. 

**Bayrağın bulunması ile ilgili örnek**

- Yukarıdaki şifreleme sonucu çıkan şifreli metin: EKNNIYAMPAYKBUBIRORNINAPRIT
- ("iki ornek bir bayrak.", (6,3), 'terssaatyonu') girdisinin sonucunda çıkan şifreli metin: NROIKIEAYRAKNBRIBK
- Bayrak: STMCTF{EKNNIYAMPAYKBUBIRORNINAPRITNROIKIEAYRAKNBRIBK} (EKNNIYAMPAYKBUBIRORNINAPRIT + NROIKIEAYRAKNBRIBK)

**Aşağıdaki girdiyi algoritmaya vererek deşifre edip çıktıyı STMCTF{} içerisine yerleştirerek bayrağa ulaşabilirsin.**

**""SAMIRELKEBNASRABENIMADIMERYAKIRENUKN"", (12, 3), 'saatyonu'**

Online CTF'teki Cipher101 isimli sorunun aynısı gibi değil mi? evet aynı algoritma. Sadece bu sefer tam tersini yapacaksın. :)


## Çözüm: 

```python
def desifrele(_input):
    def tersine_spiral(bayrak, n, m):
        if bayrak:
            return tersine_spiral(bayrak[n:], m-1, n) + [bayrak[:n]]
        return []
    bayrak, x, y, yon = _input.rsplit(" ", 3)
    bayrak, x, y = bayrak[1:-1], int(x[1:-1]), int(y[:-1])
    matris = []
    if yon == "saatyonu":
        for i in tersine_spiral(bayrak, y, x):
            matris = list(zip(*(matris + [i])))[::-1]
        print("".join("".join(n) for n in matris[::-1]))
    elif yon == "terssaatyonu":
        for i in tersine_spiral(bayrak, x, y):
            matris = list(zip(*([i] + matris)[::-1]))
        print("".join("".join(n) for n in zip(*matris))[::-1])
        
desifrele('''"SAMIRELKEBNASRABENIMADIMERYAKIRENUKN" (12, 3) saatyonu''')
```

**Flag  = STMCTF{BENIMADIMERSANKUNERIKAYARSANBEKLERIM}**
