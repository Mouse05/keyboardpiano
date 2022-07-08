import pygame as pg
import keyboard
import time

pg.mixer.init()
pg.init()

var = "C:/Users/User/Downloads/mlh_init/keyboard-piano/"

a1Note = pg.mixer.Sound(var + "key01.wav")
a2Note = pg.mixer.Sound(var + "key02.wav")
a3Note = pg.mixer.Sound(var + "key03.wav")
a4Note = pg.mixer.Sound(var + "key04.wav")
a5Note = pg.mixer.Sound(var + "key05.wav")
a6Note = pg.mixer.Sound(var + "key06.wav")
a7Note = pg.mixer.Sound(var + "key07.wav")
a8Note = pg.mixer.Sound(var + "key08.wav")
a9Note = pg.mixer.Sound(var + "key09.wav")
a10Note = pg.mixer.Sound(var + "key10.wav")
a11Note = pg.mixer.Sound(var + "key11.wav")
a12Note = pg.mixer.Sound(var + "key12.wav")
a13Note = pg.mixer.Sound(var + "key13.wav")
a14Note = pg.mixer.Sound(var + "key14.wav")
a15Note = pg.mixer.Sound(var + "key15.wav")
a16Note = pg.mixer.Sound(var + "key16.wav")



pg.mixer.set_num_channels(50)

while True:
    try:
        if keyboard.is_pressed('a'):
            a1Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('w'):
            a2Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('s'):
            a3Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('e'):
            a4Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('d'):
            a5Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('f'):
            a6Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('g'):
            a7Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('y'):
            a8Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('h'):
            a9Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('u'):
            a10Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('j'):
            a11Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('k'):
            a12Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('o'):
            a13Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('l'):
            a14Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed('p'):
            a15Note.play()
            time.sleep(0.3)
        if keyboard.is_pressed(';'):
            a16Note.play()
            time.sleep(0.3)
    except:
        break