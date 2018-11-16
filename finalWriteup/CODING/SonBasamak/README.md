## Soru İsmi: Son Basamak

## Soru Metni: 

Metin dosyası içindeki her 14 basamaklı sayının aşağıdaki yönteme göre 15.basamağı hesaplanacaktır. Sıralı biçimde olan 15.basamaklar 700 basamaklı bir sayıyı oluşturacaktır. Bu 700 basamaklı sayı içinde flag değeri saklıdır. Soruda verilen aralıkta bulunan 15 basamaklı sayı değeri flag değeridir.

2556000762172588-SAYI-364042733192523

Bulunan SAYI flag formatı içerisine yerleştirilmelidir.

STMCTF{SAYI}

**Yöntem:**
- 1,3,5,7,9,11,13 basamakları toplanır.
- 2,4,6,8,10,12,14 basamakları iki ile çarpılır eğer sonuç iki basamaklı ise basamakların sayı değerleri toplanır.
- Tek ve Çift basamakları sonuçları toplanır.
- Toplam sonucu 10'a bölünen sonuçtan büyük sonuca en yakın sayıdan çıkartılır.
- Bulunan değer 15.basamaktır.

**Örnek:**

**58186778266652**

Tek basamaklar:

    5+1+6+7+2+6+5=32

Çift basamaklar:

    2*8=16 1+6=7

    2*8=16 1+6=7

    2*7=14 1+4=5

    2*8=16 1+6=7

    2*6=12 1+2=3

    2*6=12 1+2=3

    2*2=4

    7+7+5+7+3+3+4=36

    32+36=68

    70-68=2

15.basamak = 2

Soruda verilen dosya: [sonbasamak.txt](sonbasamak.txt)

## Çözüm: 

1. [solution.py](solution.py) scripti yazılarak flag elde edilir.

**Flag  = STMCTF{469575577405784}**
