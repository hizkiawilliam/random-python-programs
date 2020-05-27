from vpython import*
from vpython.text import *
import random
import winsound


scene.title="Python Hero"
scene.width=600
scene.height=700
scene.center=(0,10,4)
scene.autoscale=0
scene.userzoom=0
scene.userspin=0

#Shapes

f=frame()
f2=frame()
f3=frame()

title=text(pos=(0,20.5,0), string='PYTHON HERO', color=color.white, depth=0.5, height=1, justify='center')

background=box(frame=f, pos=(0,10,0,), length=10, width=.01, height=20)

greenkey=box(frame=f, pos=(-4,0,0), length=2, width=.5, height=1)
greenkey.color=color.green
redkey=box(frame=f, pos=(-2,0,0), length=2, width=.5, height=1)
redkey.color=color.red
yellowkey=box(frame=f, pos=(0,0,0), length=2, width=.5, height=1)
yellowkey.color=color.yellow
bluekey=box(frame=f, pos=(2,0,0), length=2, width=.5, height=1)
bluekey.color=color.blue
orangekey=box(frame=f, pos=(4,0,0), length=2, width=.5, height=1)
orangekey.color=color.orange

divider1=cylinder(frame=f, pos=(-3,0,0), radius=.1, axis=(0,20,0))
divider2=cylinder(frame=f, pos=(-1,0,0), radius=.1, axis=(0,20,0))
divider3=cylinder(frame=f, pos=(1,0,0), radius=.1, axis=(0,20,0))
divider4=cylinder(frame=f, pos=(3,0,0), radius=.1, axis=(0,20,0))

sidebar1=cylinder(frame=f, pos=(-5,0,0), radius=.15, axis=(0,20,0))
sidebar2=cylinder(frame=f, pos=(5,0,0), radius=.15, axis=(0,20,0))

streak1=cylinder(frame=f2, pos=(5.25,6.25,0), radius=.4, axis=(1,.5,0))
streak2=cylinder(frame=f2, pos=(5.25,7,0), radius=.4, axis=(1,.5,0))
streak3=cylinder(frame=f2, pos=(5.25,7.75,0), radius=.4, axis=(1,.5,0))
streak4=cylinder(frame=f2, pos=(5.25,8.5,0), radius=.4, axis=(1,.5,0))
streak5=cylinder(frame=f2, pos=(5.25,9.25,0), radius=.4, axis=(1,.5,0))

rockmeter=box(frame=f, pos=(-7,14,.25), length=2, width=.01, height=.5)
rockmeterhi=box(frame=f, pos=(-8,14,0), length=.5, width=.01, height=4)
rockmeterhi.color=color.green
rockmetermed=box(frame=f, pos=(-8,10,0), length=.5, width=.01, height=4)
rockmetermed.color=color.yellow
rockmeterlow=box(frame=f, pos=(-8,6,0), length=.5, width=.01, height=4)
rockmeterlow.color=color.red

def white(x,y,z):
    wkey=box(frame=f3, pos=(x,y,z), length=.475, width=.25, height=1.75)
    return wkey

C1=white(-3.5,10,-1)
D1=white(-3,10,-1)
E1=white(-2.5,10,-1)
F1=white(-2,10,-1)
G1=white(-1.5,10,-1)
A1=white(-1,10,-1)
B1=white(-.5,10,-1)
C2=white(0,10,-1)
D2=white(.5,10,-1)
E2=white(1,10,-1)
F2=white(1.5,10,-1)
G2=white(2,10,-1)
A2=white(2.5,10,-1)
B2=white(3,10,-1)
C3=white(3.5,10,-1)

def black(x,y,z):
    bkey=box(frame=f3, pos=(x,y,z), length=.3, width=.1, height=.9)
    bkey.color=color.black
    return bkey

Cs1=black(-3.25,10.4,-.9)
Ds1=black(-2.75,10.4,-.9) 
Fs1=black(-1.75,10.4,-.9)
Gs1=black(-1.25,10.4,-.91)
As1=black(-.75,10.4,-.9)
Cs2=black(.25,10.4,-.9)
Ds2=black(.75,10.4,-.9)
Fs2=black(1.75,10.4,-.9)
Gs2=black(2.25,10.4,-.9)
As2=black(2.75,10.4,-.9)

start=sphere(frame=f3, pos=(0,12,-1), radius=.5)
start.color=color.red
custombackground=box(frame=f3, pos=(0,10,-1), length=8, width=.2, height=2.5)
custombackground.color=color.blue
f3.axis=(1,0,0)

#Functions

def menu():
    option=int(raw_input("Python Hero\n\n\n1. Play Game\n\n2. Create Song\n\n3. Exit Game\n\n"))
    if option==1:
        return 1
    elif option==2:
        return 2
    elif option==3:
        return 3

def difficultySelect():
    difficulty=int(raw_input("\n\nPlease select difficulty.\n\n1.  Easy\n\n2.  Medium\n\n3.  Hard\n\n"))
    if difficulty==1:
        return 3
    elif difficulty==2:
        return 4
    elif difficulty==3:
        return 5

def noteGenerator(pitches):
    noteList=[]
    for i in range(50):
        noteNum=random.randrange(pitches)
        noteList.append(noteNum)
    return noteList

def noteAnimation(note, noteNum):
    notes=[65.4,69.3,73.4,77.8,82.4,87.3,92.5,98,103.8,110,116.5,123.5,130.8,138.6,146.8,155.6,164.8,174.6,185,196,207.6,220,233,247,261.6]
    while True:
        rate(180)
        if scene.kb.keys:
            key=scene.kb.getkey()
            if key=="1" and note.x==-4 and note.y>-4 and note.y<4:
                greenkey.z=greenkey.z+.5
                greenkey.color=color.white
                note.visible=0
                if noteNum==0:
                    winsound.Beep(notes[0],200)
                elif noteNum==5:
                    winsound.Beep(notes[9],200)
                elif noteNum==10:
                    winsound.Beep(notes[17],200)
                elif noteNum==15:
                    winsound.Beep(notes[1],200)
                elif noteNum==20:
                    winsound.Beep(notes[13],200)
                greenkey.z=greenkey.z-.5
                greenkey.color=color.green
                return 1
            elif key=="2" and note.x==-2 and note.y>-4 and note.y<4:
                redkey.z=redkey.z+.5
                redkey.color=color.white
                note.visible=0
                if noteNum==1:
                    winsound.Beep(notes[2],200)
                elif noteNum==6:
                    winsound.Beep(notes[11],200)
                elif noteNum==11:
                    winsound.Beep(notes[19],200)
                elif noteNum==16:
                    winsound.Beep(notes[3],200)
                elif noteNum==21:
                    winsound.Beep(notes[15],200)
                redkey.z=redkey.z-.5
                redkey.color=color.red
                return 1
            elif key=="3" and note.x==0 and note.y>-4 and note.y<4:
                yellowkey.z=yellowkey.z+.5
                yellowkey.color=color.white
                note.visible=0
                if noteNum==2:
                    winsound.Beep(notes[4],200)
                elif noteNum==7:
                    winsound.Beep(notes[12],200)
                elif noteNum==12:
                    winsound.Beep(notes[21],200)
                elif noteNum==17:
                    winsound.Beep(notes[6],200)
                elif noteNum==22:
                    winsound.Beep(notes[18],200)
                yellowkey.z=yellowkey.z-.5
                yellowkey.color=color.yellow
                return 1
            elif key=="4" and note.x==2 and note.y>-4 and note.y<4:
                bluekey.z=bluekey.z+.5
                bluekey.color=color.white
                note.visible=0
                if noteNum==3:
                    winsound.Beep(notes[5],200)
                elif noteNum==8:
                    winsound.Beep(notes[14],200)
                elif noteNum==13:
                    winsound.Beep(notes[23],200)
                elif noteNum==18:
                    winsound.Beep(notes[8],200)
                elif noteNum==23:
                    winsound.Beep(notes[20],200)
                bluekey.z=bluekey.z-.5
                bluekey.color=color.blue
                return 1
            elif key=="5" and note.x==4 and note.y>-4 and note.y<4:
                orangekey.z=orangekey.z+.5
                orangekey.color=color.white
                note.visible=0
                if noteNum==4:
                    winsound.Beep(notes[7],200)
                elif noteNum==9:
                    winsound.Beep(notes[16],200)
                elif noteNum==14:
                    winsound.Beep(notes[24],200)
                elif noteNum==19:
                    winsound.Beep(notes[10],200)
                elif noteNum==24:
                    winsound.Beep(notes[22],200)
                orangekey.z=orangekey.z-.5
                orangekey.color=color.orange
                return 1
        elif note.y>-4:
            note.y=note.y-.1
        elif note.y<-4:      
            note.visible=0
            return 0

def noteStreakCounter(notestreak):
    notestreak=notestreak+1
    notestreakbox=label(frame=f, pos=(8,15,0), text=str(notestreak))
    if notestreak==1:
        streak1.color=color.yellow
    elif notestreak==2:
        streak2.color=color.yellow
    elif notestreak==3:
        streak3.color=color.yellow
    elif notestreak==4:
        streak4.color=color.yellow
    elif notestreak==5:
        streak5.color=color.yellow
    elif notestreak==6:
        for obj in f2.objects:
            obj.color = color.white
        streak1.color=color.yellow
    elif notestreak==7:
        streak2.color=color.yellow
    elif notestreak==8:
        streak3.color=color.yellow
    elif notestreak==9:
        streak4.color=color.yellow
    elif notestreak==10:
        streak5.color=color.yellow
    elif notestreak==11:
        for obj in f2.objects:
            obj.color = color.white
        streak1.color=color.green
    elif notestreak==12:
        streak2.color=color.green
    elif notestreak==13:
        streak3.color=color.green
    elif notestreak==14:
        streak4.color=color.green
    elif notestreak==15:
        streak5.color=color.green
    elif notestreak==16:
        for obj in f2.objects:
            obj.color = color.white
        streak1.color=(.9,0,1)
    elif notestreak==17:
        streak2.color=(.9,0,1)
    elif notestreak==18:
        streak3.color=(.9,0,1)
    elif notestreak==19:
        streak4.color=(.9,0,1)
    elif notestreak==20:
        streak5.color=(.9,0,1)
    return notestreak

def rockMeter(result):
    if result==1 and rockmeter.y==16:
        rockmeter.y=16
    elif result==0 and rockmeter.y==4:
        rockmeter.y=4
        return "fail"
    elif result==1:
        rockmeter.y=rockmeter.y+1
    elif result==0:
        rockmeter.y=rockmeter.y-1
    return

def scoreMultiplier(notestreak):
    if notestreak<6:
        multiplier=1
        multiplierbox=label(frame=f, pos=(8,8,0), text="1X", height=50)
    elif notestreak>=6 and notestreak<11:
        multiplier=2
        multiplierbox=label(frame=f, pos=(8,8,0), text="2X", height=50)
    elif notestreak>=11 and notestreak<16:
        multiplier=3
        multiplierbox=label(frame=f, pos=(8,8,0), text="3X", height=50)
    elif notestreak>=16:
        multiplier=4
        multiplierbox=label(frame=f, pos=(8,8,0), text="4X", height=50)        
    return multiplier

def scoreCounter(score, multiplier):
    score=score+50*multiplier
    scorebox=label(frame=f, pos=(8,17,0), text=str(score))
    return score
 
def gameplay(noteList):
    
    notestreak=0
    notestreaktitle=label(frame=f, pos=(8,16,0), text="Note Streak")
    notestreakbox=label(frame=f, pos=(8,15,0), text=str(notestreak))
    score=0
    scoretitle=label(frame=f, pos=(8,18,0), text="Score")
    scorebox=label(frame=f, pos=(8,17,0), text=str(score))
    multiplier=1
    multipliertitle=label(frame=f, pos=(8,10,0), text="Multiplier")
    multiplierbox=label(frame=f, pos=(8,8,0), text="1X", height=50)
    
    for i in range(len(noteList)):
        noteNum=noteList[i]
        if noteNum==0 or noteNum==5 or noteNum==10 or noteNum==15 or noteNum==20:
            greennote=ellipsoid(frame=f, pos=(-4,20,0), length=2, height=.5, width=1)
            greennote.color=color.green
            result=noteAnimation(greennote, noteNum)
            if result==1:
                notestreak=noteStreakCounter(notestreak)
                multiplier=scoreMultiplier(notestreak)
                score=scoreCounter(score, multiplier)
            elif result==0:
                notestreak=0
                notestreakbox=label(frame=f, pos=(8,15,0), text=str(notestreak))
                multiplier=1
                multiplierbox=label(frame=f, pos=(8,8,0), text="1X", height=50)
                for obj in f2.objects:
                    obj.color = color.white
            fail=rockMeter(result)
            if fail=="fail":
                text(pos=(0,10,0), string='YOU FAIL', color=color.red, depth=0.3, justify='center')
                return 
        elif noteNum==1 or noteNum==6 or noteNum==11 or noteNum==16 or noteNum==21:
            rednote=ellipsoid(frame=f, pos=(-2,20,0), length=2, height=.5, width=1)
            rednote.color=color.red
            result=noteAnimation(rednote, noteNum)
            rockMeter(result)
            if result==1:
                notestreak=noteStreakCounter(notestreak)
                multiplier=scoreMultiplier(notestreak)
                score=scoreCounter(score, multiplier)
            elif result==0:
                notestreak=0
                notestreakbox=label(frame=f, pos=(8,15,0), text=str(notestreak))
                multiplier=1
                multiplierbox=label(frame=f, pos=(8,8,0), text="1X", height=50)
                for obj in f2.objects:
                    obj.color = color.white
            fail=rockMeter(result)
            if fail=="fail":
                text(pos=(0,10,0), string='YOU FAIL', color=color.red, depth=0.3, justify='center') 
                return 
        elif noteNum==2 or noteNum==7 or noteNum==12 or noteNum==17 or noteNum==22:
            yellownote=ellipsoid(frame=f, pos=(0,20,0), length=2, height=.5, width=1)
            yellownote.color=color.yellow
            result=noteAnimation(yellownote, noteNum)
            if result==1:
                notestreak=noteStreakCounter(notestreak)
                multiplier=scoreMultiplier(notestreak)
                score=scoreCounter(score, multiplier)
            elif result==0:
                notestreak=0
                notestreakbox=label(frame=f, pos=(8,15,0), text=str(notestreak))
                multiplier=1
                multiplierbox=label(frame=f, pos=(8,8,0), text="1X", height=50)
                for obj in f2.objects:
                    obj.color = color.white
            fail=rockMeter(result)
            if fail=="fail":
                text(pos=(0,10,0), string='YOU FAIL', color=color.red, depth=0.3, justify='center')
                return 
        elif noteNum==3 or noteNum==8 or noteNum==13 or noteNum==18 or noteNum==23:
            bluenote=ellipsoid(frame=f, pos=(2,20,0), length=2, height=.5, width=1)
            bluenote.color=color.blue
            result=noteAnimation(bluenote, noteNum)
            if result==1:
                notestreak=noteStreakCounter(notestreak)
                multiplier=scoreMultiplier(notestreak)
                score=scoreCounter(score, multiplier)
            elif result==0:
                notestreak=0
                notestreakbox=label(frame=f, pos=(8,15,0), text=str(notestreak))
                multiplier=1
                multiplierbox=label(frame=f, pos=(8,8,0), text="1X", height=50)
                for obj in f2.objects:
                    obj.color = color.white
            fail=rockMeter(result)
            if fail=="fail":
                text(pos=(0,10,0), string='YOU FAIL', color=color.red, depth=0.3, justify='center')
                return 
        elif noteNum==4 or noteNum==9 or noteNum==14 or noteNum==19 or noteNum==24:
            orangenote=ellipsoid(frame=f, pos=(4,20,0), length=2, height=.5, width=1)
            orangenote.color=color.orange
            result=noteAnimation(orangenote, noteNum)
            rockMeter(result)
            if result==1:
                notestreak=noteStreakCounter(notestreak)
                multiplier=scoreMultiplier(notestreak)
                score=scoreCounter(score, multiplier)
            elif result==0:
                notestreak=0
                notestreakbox=label(frame=f, pos=(8,15,0), text=str(notestreak))
                multiplier=1
                multiplierbox=label(frame=f, pos=(8,8,0), text="1X", height=50)
                for obj in f2.objects:
                    obj.color = color.white
            fail=rockMeter(result)
            if fail=="fail":
                text(pos=(0,10,0), string='YOU FAIL', color=color.red, depth=0.3, justify='center')
                return
    text(pos=(0,10,0), string='YOU ROCK', color=color.green, depth=0.3, justify='center')
    return

def customSongMaker():
    notes=[65.4,69.3,73.4,77.8,82.4,87.3,92.5,98,103.8,110,116.5,123.5,130.8,138.6,146.8,155.6,164.8,174.6,185,196,207.6,220,233,247,261.6]
    customnotes=[]
    while True:
        rate(100)
        if scene.mouse.clicked:
            m=scene.mouse.getclick()
            if m.pick==C1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[0],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(0)
            elif m.pick==Cs1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[1],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(15)
            elif m.pick==D1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[2],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(1)
            elif m.pick==Ds1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[3],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(16)
            elif m.pick==E1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[4],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(2)
            elif m.pick==F1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[5],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(3)
            elif m.pick==Fs1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[6],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(17)
            elif m.pick==G1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[7],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(4)
            elif m.pick==Gs1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[8],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(18)
            elif m.pick==A1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[9],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(5)
            elif m.pick==As1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[10],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(19)
            elif m.pick==B1:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[11],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(6)
            elif m.pick==C2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[12],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(7)
            elif m.pick==Cs2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[13],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(20)
            elif m.pick==D2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[14],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(8)
            elif m.pick==Ds2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[15],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(21)
            elif m.pick==E2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[16],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(9)
            elif m.pick==F2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[17],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(10)
            elif m.pick==Fs2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[18],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(22)
            elif m.pick==G2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[19],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(11)
            elif m.pick==Gs2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[20],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(23)
            elif m.pick==A2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[21],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(12)
            elif m.pick==As2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[22],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(24)
            elif m.pick==B2:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[23],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(13)
            elif m.pick==C3:
                m.pick.y=m.pick.y-.1
                winsound.Beep(notes[24],200)
                m.pick.y=m.pick.y+.1
                customnotes.append(14)
            elif m.pick==start:
                return customnotes

#Run Functions

def runGame():
    while True:
        option=menu()
        if option==1:
            for obj in f3.objects:
                obj.visible = 0
            difficulty=difficultySelect()
            notes=noteGenerator(difficulty)
            gameplay(notes)
            return
        elif option==2:
            for obj in f3.objects:
                obj.z=obj.z+12
            customnotes=customSongMaker()
            for obj in f3.objects:
                obj.z=obj.z-12
            gameplay(customnotes)
            return
        elif option==3:
            return

runGame()
raw_input("Thanks for playing!")
