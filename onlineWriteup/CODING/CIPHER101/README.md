## Soru İsmi: CIPHER101
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
    ``
- Bayrağın bulunması için aşağıdaki metinler anlatılan algoritma ile işlenerek uç uca ekleme ile birleştirilmelidir. 

**Bayrağın bulunması ile ilgili örnek**

- Yukarıdaki şifreleme sonucu çıkan şifreli metin: EKNNIYAMPAYKBUBIRORNINAPRIT
- ("iki ornek bir bayrak.", (6,3), 'terssaatyonu') girdisinin sonucunda çıkan şifreli metin: NROIKIEAYRAKNBRIBK
- Bayrak: STMCTF{EKNNIYAMPAYKBUBIRORNINAPRITNROIKIEAYRAKNBRIBK} (EKNNIYAMPAYKBUBIRORNINAPRIT + NROIKIEAYRAKNBRIBK)

**Aşağıdaki girdileri algoritmaya vererek çıktılarını STMCTF{} içerisine yerleştirip bayrağı elde ediniz**

- **("ARADIGIN GUC ICINDE", (6, 3), 'saatyonu')**
- **("BIRAZ EKSINA NE DERSIN", (10, 2), 'terssaatyonu')**
- **("kusura bakmayin ben korum", (5, 5), 'saatyonu')**
- **("daha once kafa binbesyuz kullandin mi", (7, 5), 'terssaatyonu')**
- **("su brosurleri goruyor musun", (6, 4), 'saatyonu')**
- **("BEN GORMUYORUM ISTE", (7, 3), 'terssaatyonu')**


## Çözüm: 



**STMCTF{GINEDNICIARADICUGNNISKEZARIBANEDERSINNRMBRNNNMUEAAKUSUKNOKNYBAICNOAHADENKINMINNNDZIBAFAKBULLANUYSESIONUSUMRGUSUBRORYURORLEMROGNEBUSTENNNNIMUROY}**
