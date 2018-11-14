## Soru İsmi: H4ckl3nd1k

## Soru Metni: 

Şirketin ağına saldırganlar girdi, ağ kaydımızı analiz ederek hangi bilgileri tespit ettiklerini bulmak gerekiyor.

Soruda verilen dosya: [kayit.pcap](kayit.pcap)

## Çözüm: 

1. Verilen pcap kaydı açılır. Kayıtlarda bulunan tcp paketleri incelenir ve bir yazışma tespit edilir.
 
![Preview](s1.png)

2. Yazışmada bir dosyanın indirilebileceğinden söz etmektedir. 

![Preview](s2.png) 

3. liste.ods dosyası wireshark’tan export edilerek indirilir.

![Preview](s3.png)

4. liste.ods dosyasını açmak için şifre gerekmektedir. Ağ kayıtları incelenmeye devam ettiğinde şifrenin *hack1!* olduğu bulunmaktadır.

![Preview](s4.png) 

5. Dosya bu şifre ile açılınca  ctf satırı açıklamalarında bayrak bulunur.

![Preview](s5.png)

**FLAG = STMCTF{Hackledim_Cok_da_Guzel_Oldu}**

