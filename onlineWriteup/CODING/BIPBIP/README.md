## Soru İsmi: BIPBIP

## Soru Metni: 

dat diri dat dat dat diri dat dat dat diri dat dat

Soruda verilen dosya: [bipbip.mp4](bipbip.mp4)

## Çözüm: 

1. Verilen dosya incelendiğinde her karede farklı noktalar çıktığı görülür.

2. `exiftool bipbip.mp4` komutuyla videonun FPS değeri 4 olarak bulunur.

3. `ffmpeg -i bipbip.mp4 -vf fps=4 images/flag%02d.jpg` komutuyla her kare images altında bir resim dosyasına yazılır.

4. Aşağıdaki script ile her resim dosyasındaki noktalar binary olarak okunur. Bulunan binary string daha sonrasında flag i oluşturur.


```python
#!/usr/bin/python

#ffmpeg -i bipbip.mp4 -vf fps=4 flag%02d.jpg
#200x100

from PIL import Image
import os
import binascii

path = "images/"
filelist = os.listdir(path)
number_files = len(filelist)

flag = ""

for i in range(1,number_files+1):
	file = path+"flag%02d.jpg" % (i)

	binlist=[]
	bcode = ""

	im = Image.open(file)
	pix = im.load()
	for x in range(0,4):
		binlist.append(pix[(50*x)+25,25])
	for y in range(0,4):
		binlist.append(pix[(50*y)+25,75])

	for i in range(0,8):
		if binlist[i] == (0,0,0):
			bcode=bcode+"1"
		else:
			bcode=bcode+"0"

	n = int(bcode, 2)
	flag += binascii.unhexlify('%x' % n)


print "".join(flag)
```

**Flag  = STMCTF{bLip_BL!P_81ip_blip!_!1!}**
