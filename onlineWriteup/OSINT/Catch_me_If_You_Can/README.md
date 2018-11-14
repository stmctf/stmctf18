## Soru İsmi: Catch me If You Can

## Soru Metni: 

Gotham’daki bir bilişim şirketinin CEO’su olan Bruce Wayne’e yönelik hedef odaklı bir oltalama saldırısı gerçekleştirilmiştir. Bu saldırıyı gerçekleştiren saldırganın Twitter adresini tespit edebilir misin?

Soruda verilen dosya: [phishing.pcap](phishing.pcap)

## Çözüm: 

1. Pcap dosyası Wireshark ile açılır.

2. File -> Export Objects -> HTTP seçilerek “attachment.pdf” dosyası elde edilir.

3. Elde edilen “attachment.pdf” dosyası exiftool ile incelenerek hackerjohndoe007@gmail.com mail adresi elde edilir.

4. https://www.wikihow.com/Add-Contacts-in-Gmail adresinde olduğu gibi yeni bir gmail hesabı açılarak “hackerjohndoe007@gmail.com” mail adresi Contact listesine eklenir

5. Daha sonra bu mail adresi ile yeni bir twitter adresi açılarak “Tanıdığın kişileri bul” ile Contact listesindeki “hackerjohndoe007@gmail.com” aranarak bulunur.

6. Tespit edilen “The Extreme One (@XtremerHacker)” adlı twitter kullanıcısının bio kısmında yer alan flag tespit edilir.

**FLAG = STMCTF{B0ND_J4M35_B0ND}**
