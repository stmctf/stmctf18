## Soru İsmi: STM128

## Soru Metni: 

Bu soruda flag'in stm128 algoritmasıyla hashlenmiş hali sorulacaktı lakin flag'i malesef kaybetmiş bulunmaktayız.
Flag'i kaybetme durumuna karşı hash'i saklanmıştı ama hash'i hesaplamak için Enter tuşuna basarken yanlışlıkla ',' 
tuşuna basıp sonra Enter tuşuna basılmış. Hatırlananlara göre flag'in uzunluğu 16'nın katıydı. 
Bu bilgilere göre orjinal flag'in stm128 algorithmasıyla hesaplanmış hash'ini bulabilir misiniz? 

hash = c87cced0b2430495ea3900129da1f2aa

Gireceğiniz flag değeri aşağıdaki şekilde flag in STM128 hashi olmalıdır. 

Flag = 89***************************9d

Soruda verilen dosya: [stm128.py](stm128.py)

## Çözüm: 

1. Kaynak kod incelendiğinde aslında her işlemin roundkey'i bilindiğinde tersine alınabileceği farkedilir.

2. Flag'in uzunluğu 16'ın katı olduğu için en son round'daki roundkey'in padding ile 
',\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f' olduğu bilinmektedir.

3. Son round tersine çevrildiğinde ise orjinal flag'in hash bulunmuş olacaktır.

4. [solution.py](solution.py) scripti yazılarak flag elde edilir.

**Flag  = 89f7622efdb88720bd9c00f9413139d**
