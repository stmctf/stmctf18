## Soru İsmi: Rastgele

## Soru Metni: 

Bu sorunun flag'i ekte verilen program ile şifrelenmiştir. Programın çıktısı şu şekildedir: 

n = 6372770546496319102179620437307638173638450624706994013150556737556325599703330944379292690861019317896179238639531103215452528829844474367267311641005420236669484549925277976322608347329839738367472716421549441841809205650965622561195036563462678859216423865852610719120951177139295537080439411028696345435214848494163374918999689909835436773514063023408641642730779603935834213337924666184669534359324246716927163328942404372033668897126060617824416978557501665796292712890480413460846730640731379072921121900697734892519479348366220299821848153550069772424968362100343986833830629806781246764199433828997536664737

c = 0x312a9507b4e1d48cf52c31e9eaf5a044d99b5c14298245ec61c27a0d5e8cfda840e397ab46cc9196a65258debb26c5c96bb23443c94e6bcfd55154f3f14453994e230c2ab106025d7916c9f00a0542bbe1e9c29c0b9620c34f71064f6741a2a7369355fc7bac7dbf1a17142a65855be33076a98e9defd4a48305883abf2d26c424f3b376d6bb8a46112e6a5503b9f787cc2e6eb9746afd083772f7dc5e547efbf1290c3a95dca18d9bb2f0a0d60ce3fc82b4d4e635e2a6b7308d46c09976123c3a1f89823275a945345aa4c311fde2133e8ffbed57ff7ecb9d9415609fb946420e639e95c2fb104810a087d67f2a496ee368b5c929c9ce6998ba581504cc4e25

Sorudaki şifreyi çözüp flag'i bulunuz.

Soruda verilen dosya: [rastgele.py](rastgele.py)

## Çözüm: 

1. Soruyu ilk incelediğimizde görüyoruz ki log(n,2) > 2048 ve e != 3. Bu demek oluyor ki RSA'in implemente edilişinde bariz bir problem yok.
Bu yüzden sorunun çözülebilmesi için problemin, sorunun isminin de gösterdiği gibi, asal sayıların üretiminde olması gerek. 

2. Kodu incelediğimizde p ve q'un aslında r'nin bir fonksiyonu olduğunu fark ediyoruz.

3. n = p * q olduğundan her bir n için eşsiz bir p ve q ikilisi vardır.

4. f(r) -> (p,q) -> n fonksiyonu bir müddet daha incelendiğinde farkedilir ki f sürekli artan bir fonksiyondur.

5. log(r,2) <= 1024 olduğu için f(r) üzerinde [1, 2**1024] aralığında binary search yapılabilir.

6. Bu aramanın sonucunda bulunan r_, f(r_) == n koşulunu sağlıyor ise r_ = r ve r_ üzerinden p ve q rahatlıkla hesaplanabilir.

7. [solution.py](solution.py) scripti yazılarak flag elde edilir.

**Flag  = STMCTF{Balikcilar_Elleri_Dolu_Dondu}**
