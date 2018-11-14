# -*- coding: utf-8 -*-

# STMCTF'18
# 8bitKaplumbagaCNC

import turtle as t

t.bgcolor('black')
t.pencolor('white')
t.shape("arrow")
t.resizemode("user")
t.shapesize(0.5, 0.5, 1)
t.screensize(3000, 150)
t.delay(1)
t.showturtle()

with open('8bitKaplumbagaCNC.cmd', "r") as f:
    commands = f.read().splitlines()

for idx, c in enumerate(commands):
    if len(c) < 8:
        continue

    action = c[-2:]
    shift = c[0]
    value = int(c[1:6], 2)
    value_debug = c[1:6]
    degree = 360/value
    
    buyutec = 6 # Buyutec :)
    value *= buyutec 

    hint = "Komut# " + str(idx+1) + ": " + c
    t.title(hint)

    """
    0 00100 11 -> shift, value, action

    action:
    00: NOP
    01: DÖN
    10: GİT
    11: ÇİZ

    value: (1 veya 2 için)
    1. GİT ve ÇİZ için:
    int(value, 2) kadar ilerle veya çiz
    2. DÖN için:
    360/int(value, 2) derece kadar dön

    shift: (1 veya 2 için)
    1. GİT ve ÇİZ için:
    1 ise yönünü değiştirmeden geri git
    2. DÖN için:
    1 ise değeri negatif (-) olarak degerlendir. 0'da 90 derece sağa dönerken 1'de -90 sola döner.

    Derece:
    360/2 = 180 Derece
    360/4 = 90 Derece
    360/5 = 72 Derece
    360/6 = 60 Derece
    360/8 = 45 Derece
    360/12 = 30 Derece
    """

    idx = idx+1
    print idx, c, "DEBUG:", "shift:", shift, "value:", value_debug, "action:", action, "?(value:", value, "degree:", degree, ")",

    if action == "00":  # NOP
        print idx, c, "DEBUG:", "PASS"
	raw_input("Devam icin ENTER!")

    elif action == "01":  # don
        if shift == "0":
            t.right(degree)
            print  "SAGA", degree, "derece don"
        else:
            print  "SOLA", degree, "derece don"
            t.left(degree)
    elif action == "10":  # git
        t.penup()
        if shift == "0":
            print value, "Birim DUZ GiT"
            t.forward(value)
        else:
            print value, "Birim GERi GiT"
            t.backward(value)
    elif action == "11":  # ciz
        t.pendown()
        if shift == "0":
            print  value, "Birim DUZ CiZ"
            t.forward(value)
        else:
            print  value, "Birim GERi CiZ"
            t.backward(value)
    else:
        pass
t.mainloop()
