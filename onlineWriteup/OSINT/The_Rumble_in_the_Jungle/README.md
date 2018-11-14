## Soru İsmi: The Rumble in the Jungle

## Soru Metni: 

Bir online kod paylaşım sitesinde “welcometothejungle@outlook.com.tr” mail adresine sahip bir hacker’ın gizli bilgiler paylaştığı tespit edilmiştir. Bu hacker’ın paylaştığı gizli bilgiyi bulabilir misin?

Soruda verilen dosya: [phishing.pcap](phishing.pcap)

## Çözüm: 

1. Online kod paylaşım sitesi olarak github incelenmeye başlanır.

2. Burada soruda verilen “welcometothejungle@outlook.com.tr” mail adresi aratılır.

3. Bu mail adresinin “Wiki”de yer aldığı gözlemlenir.

4. Commitlenmiş veriler üzerinde History araştırması yapıldığında daha önceden commitlenmiş veriler içinde ghostbin (https://ghostbin.com/paste/5ktx65mk) linkinin bulunduğu tespit edilir.

5. Github’da yer alan “A game for those who seek to find a way to leave their world behind.” sözü Google üzerinde aratıldığında “jumanji” filmine ait olduğu gözlemlenir.

6. Ghostbin’de linke şifre olarak “jumanji” olarak girilerek flag tespit edilir.

**FLAG = STMCTF{the_first_player_to_reach_the_end_wins}**
