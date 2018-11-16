## Soru İsmi: Kaçak

## Soru Metni: 

Şirketin finans müdürü Ege Deniz önemli bilgileri şirketten kaçırdı. Hangi otelde kaldığını bulup bilgi kopyladığı usbleri almak gerekiyor. Hakkındaki bilgi dosyasını ekte bulabilirsin. Bayrak formatı STMCTF{HOTEL_*_*}

Soruda verilen dosya: [db_hr.sql](db_hr.sql)

## Çözüm: 

1. Soruda bize Ege Deniz isimli kişinin kaçtığı bilgisi ve insan kaynakları veritabanı dosyası verilmektedir. Veritabanı dosyasını açmak için mysql’de veritabanı oluşturulur.

![Preview](s1.png)
 
2. Dosya veritabanına aktarılır. Bilgi tablosu tespit edilir.
 
![Preview](s2.png)

3. Soruda Ege Deniz adlı kişinin kaldığı otelin bulunması isteniyor. Bunun için sosyal medya hesaplarından paylaşım yapabileceği düşünülerek ilgili kişinin sosyal medya üzerindeki hesabı araştırılır. Sosyal Medya Hesabı: halikarnasli48
 
![Preview](s3.png)

4. Instagram üzerinde bu kullanıcı adında bir hesap tespit edilir.

![Preview](s4.png)

5. Resimler incelendiğinde, bir gönderi dikkati çeker. Verilen sayılar koordinat bilgilerini tespit etmektedir. 

![Preview](s5.png) 

6. Bulunan koordinatlar haritalar üzerinden araştırılır. 
 
![Preview](s6.png)

7. Bulunan koordinatlara sokak görünümünden bakıldığında ilgili kişinin kaldığı otelin adı bulunur. 

![Preview](s7.png) 

8. Hotel Marina Vista tespit edilir.

![Preview](s8.png)

**Flag  = STMCTF{HOTEL_MARINA_VISTA}**
