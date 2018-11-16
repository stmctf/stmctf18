#!/usr/bin/python

f=open("sonbasamak.txt","r")

sonbas=[]
for line in f:
	print "line: "+str(line)
	tek=0
	cift=0
	for i in range (1,len(line)):
		print "i: "+str(i)
		if i%2==0:
			print "rakam: "+str(line[i-1])
			carp=2*int(line[i-1])
			if carp>9:
				top=int((str(carp))[0])+int((str(carp))[1])
				cift=cift+top
			else:
				cift=cift+carp
			print "cift: "+str(cift)
		else:
			print "rakam: "+str(line[i-1])
			tek=tek+int(line[i-1])
			print "tek: "+str(tek)

	print "tek+cift: "+str(tek+cift)
	if (tek+cift)%10==0:
		sonbas.append(0)
	else:
		sonbas.append(10-((tek+cift)%10))

print "".join(map(str,sonbas))
f.close()
