## Soru İsmi: Rubik
Hazırlayan: [mertcan](https://twitter.com/mertcancoskuner)
## Soru Metni: 

Bayrağı bulmak için WCA standartlarında bir rubik küp programlanması (https://www.worldcubeassociation.org/regulations/#article-12-notation) ve verilen sekans girdisinden o sekans sonucunda gelinen küp durumundan orjinal duruma aynı sekans ile kaç adımda dönüleceğinin hesaplanması gerekiyor. Problem çözme yeteneklerini görelim bakalım!

Sekans aşağıdaki gibidir:

```
  F2 L2 R2 B2
  D L D' L'
  F D F' D'
  R F2 L' U D B2
  R' D' R 
  F' D' F D
  R' F2 B F B F2 L' U F2 D R2 L R' B L B2 R U
  L D L'
  B U L U' L' B'
  U R U' L' U R' U' L
  U F R
  U R U' L' U R' U' L
  F D F' D' F D F' D' 
  D F D' F' D F D' F'
```

Sekans sonucunda çıkan numaralar yukarıda verilen sekans sırasına göre STMCTF{} içerisine yazılmalıdır.

## Çözüm: 

1. Pycuber ile:
```python
# -*- coding: utf-8 -*-
import pycuber as pc

for sekans in ["F2 L2 R2 B2", "D L D' L'", "F D F' D'", "R F2 L' U D B2", "R' D' R", "F' D' F D", "R' F2 B F B F2 L' U F2 D R2 L R' B L B2 R U", "L D L'", "B U L U' L' B'", "U R U' L' U R' U' L", "U F R", "U R U' L' U R' U' L", "F D F' D' F D F' D'", "D F D' F' D F D' F'"]:
    rubik, i = pc.Cube(), 0
    while rubik != pc.Cube() or i == 0:
        i+=1
        rubik(sekans)
    print("Sekans %s toplam %d adımda orjinal yerine geri dönüyor" % (sekans,i))
```

2. Custom script ile:
```python
import re
from string import ascii_uppercase, ascii_lowercase, maketrans
from itertools import chain, count

_YENI_KUP = ''.join(chain(ascii_uppercase, ascii_lowercase))[:8*6]

def rot_cw(s):
    kenarlar, kup_yuzu = s[:12], s[12:]
    rotated = ''.join(chain(kenarlar[-3:], kenarlar[:-3], *map(reversed, zip(*zip(*[iter(kup_yuzu)]*3)))))
    return _YENI_KUP.translate(maketrans(s, rotated)).translate
_YUZ_DONUSUMLERI = {name: rot_cw(kup_yuzleri) for name, kup_yuzleri
        in zip('LRUDFB', (
            'ADFgjlNLItroSRQU_TXWV',
            'HECqsvKMPnkiYZab_cdef',
            'opqaZYihgQRSABCD_EFGH',
            'lmndefvutXWVNOPL_MIJK',
            'FGHYbdPONVTQghij_klmn',
            'CBASUXIJKfcaqpos_rvut'))}
def cevir(durum, kup_yuzu):
    return _YUZ_DONUSUMLERI[kup_yuzu](maketrans(_YENI_KUP, durum))
def normalize(sekans):
    return reduce(lambda a, u: re.sub(u[0], u[1], a),
                  ((r' ', r''), (r'(.)\'', r'\1\1\1'), (r'(.)2', r'\1\1'), (r'(.)\1{3}', r'')),
                  sekans)
def coz(sekans):
    combined = durum = reduce(cevir, normalize(sekans), _YENI_KUP)
    for i in count(1):
        if durum == _YENI_KUP:
            return i
        durum = combined.translate(maketrans(_YENI_KUP, durum))
def challenge(sekans):
    for line in sekans.splitlines():
        print coz(line)

sekans = """F2 L2 R2 B2 
D L D' L'
F D F' D'
R F2 L' U D B2
R' D' R 
F' D' F D
R' F2 B F B F2 L' U F2 D R2 L R' B L B2 R U
L D L'
B U L U' L' B'
U R U' L' U R' U' L
U F R
U R U' L' U R' U' L
F D F' D' F D F' D' 
D F D' F' D F D' F'"""

challenge(sekans)
```

**Flag  = STMCTF{26618463646380333}**
