## Soru İsmi: Demir Adamın Günlükleri

## Soru Metni: 

Peter'in bilgisayarı ele geçirildi. Bayrağı yakalayıp şifreyi çözebilecek misin?

Soruda verilen dosya: tony_stark_triage_image.ad1

## Çözüm: 

1. tony_stark_triage_image.ad1 dosyası FTK Imager ile açılır. 
Guest makinenin sistem dosyaları incelenerek  NTUSER.DAT registry hive dosyası extract edilir.   

![Preview](s1.png)

2. Registry explorer vasıtasıyla extract edilen dosya, host makinede açılır. 
Yazılımlar sekmesinde STM ve içerisinde CTF kayıtları görülür.  Kayıt isminde flag değerine ulaşılır.   

![Preview](s2.png)

**Flag: STMCTF{gunluk_kayitlarinda_bir_flag_buldum_sanki}**
