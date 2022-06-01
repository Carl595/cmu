from cmu_graphics import *
from cmu import *

###WINDOWS
app.background = gradient('lightblue', 'royalblue', start = 'bottom-left')

red = Rect(140, 140, 55, 55, fill = gradient('white', 'salmon', 'orangered', start = 'bottom-right'))
green = Rect(205, 140, 55, 55, fill = gradient('white', 'springgreen', 'limegreen', start = 'bottom-left'))
blue = Rect(140, 205, 55, 55, fill = gradient('white', 'skyblue', 'deepskyblue', start = 'top-right')) 
yellow = Rect(205, 205, 55, 55, fill = gradient('white', 'palegoldenrod', 'yellow', start = 'top-left'))

windowslogo = Group(red, green, blue, yellow)

###APPS
#####CHROME
c1 = Arc(200, 200, 30, 30, 300, 120, fill = 'red')
c2 = Arc(200, 200, 30, 30, 60, 120, fill = 'yellow')
c3 = Arc(200, 200, 30, 30, 180, 120, fill = 'green')
c4 = Circle(200, 200, 8, fill = 'white')
c5 = Circle(200, 200, 5, fill = 'dodgerblue')
chrome = Group(c1, c2, c3, c4, c5)

###SETTINGS
obstacles = Group()
app.chromerunning = False
app.dy = 4
app.speed = 0
app.jump = -30
app.stepsPerSecond = 60
app.steps = 0


###START
search1 = Rect(25, 15, 350, 20, fill = rgb(40, 40, 40))
search2 = Rect(80, 180, 240, 40, fill = 'white')
player = Rect(200, 290, 10, 10, fill = 'red', visible = False)
groundmap = Rect(0, 300, 400, 120, visible = False)
noint = Label('You are not connected to the internet.', 200, 80, size = 20, visible = False)
score = Label(0, player.centerX, player.centerY - 20, size = 20, visible = False)
golabel = Label(0, 200, 200, size = 17, visible = False)
gorect = Rect(150, 250, 100, 100, visible = False, fill = 'lime')

closebrowser = Group(
    Rect(385, 0, 15, 15, fill = 'red'),
    Line(387, 2, 398, 13),
    Line(387, 2, 398, 13, rotateAngle = 90)
    )

topchrome = Group(
    Rect(0, 0, 400, 50, fill = rgb(70, 70, 70)),
    search1,
    Circle(25, 25, 10, fill = rgb(40, 40, 40)),
    Circle(375, 25, 10, fill = rgb(40, 40, 40)),
    Label('Search Google or type a URL', 100, 25, fill = rgb(200, 200, 200)),
    Line(0, 50, 400, 50, fill = rgb(200, 200, 200), lineWidth = 1)
    )
    
middlechrome = Group(
    Rect(0, 50, 400, 350, fill = rgb(70, 70, 70)),
    search2,
    Circle(80, 200, 20, fill = 'white'),
    Circle(320, 200, 20, fill = 'white'),
    Label('Search Google or type a URL', 170, 200, size = 15, fill = rgb(70, 70, 70)),
    Label('Google', 200, 130, fill = 'white', size = 60, bold = True),
    closebrowser
    )

closebrowser.visible = False
topchrome.visible = False
middlechrome.visible = False

#SPOTIFY
s1 = Circle(200, 200, 15, fill = rgb(30, 215, 96))
s2 = Oval(200, 193, 20, 5)
s3 = Oval(200, 200, 20, 4.5)
s4 = Oval(200, 207, 20, 4)
s5 = Oval(200, 195, 20, 3, fill = rgb(30, 215, 96))
s6 = Oval(200, 202, 20, 3, fill = rgb(30, 215, 96))
s7 = Oval(200, 209, 20, 3, fill = rgb(30, 215, 96))
spotify = Group(s1, s2, s3, s4, s5, s6, s7)

#STEAM
st1 = Circle(200, 200, 15, fill = gradient('midnightblue', 'darkblue', 'steelblue', start = 'top'))
st2 = Circle(205, 195, 5, fill = 'white')
st3 = Line(202, 198, 196, 205, fill = 'white', lineWidth = 3)
st4 = Circle(205, 195, 4, fill = 'white', border = 'midnightblue', borderWidth = 1)
st5 = Circle(195, 205, 4, fill = 'white')
st6 = Circle(195, 205, 3, fill = 'white', border = 'darkblue', borderWidth = 0.8)
st7 = Line(195, 205, 185, 202, fill = 'white', lineWidth = 3)

steam = Group(st1, st2, st3, st4, st5, st6, st7)

###CALCULATOR
calc1 = Rect(200, 14, 25, 30, fill = 'white')
calc2 = Rect(201, 15, 23, 6, fill = 'orange')
calc3 = Line(203.4, 24, 223, 24, lineWidth = 1, dashes = (4, 3))
calc4 = Line(203.4, 29, 223, 29, lineWidth = 1, dashes = (4, 3))
calc5 = Line(203.4, 34, 223, 34, lineWidth = 1, dashes = (4, 3))
calc6 = Line(203.4, 39, 223, 39, lineWidth = 1, dashes = (4, 3))
calculatoricon = Group(calc1, calc2, calc3, calc4, calc5, calc6)

#NOTEPAD
n1 = Rect(200, 200, 25, 30, fill = 'white')
n1.centerX = 200
n1.centerY = 200
n2 = Polygon(n1.centerX - 13, n1.top, n1.centerX - 18, n1.bottom - 5, n1.centerX + 9, n1. bottom - 5, n1.centerX + 12, n1.top, fill = 'lightblue')
n3 = Line(187, 185, 212, 185, dashes = True, fill = 'darkgray')
notepad = Group(n1, n2, n3)

i1 = Rect(50, 100, 300, 200, fill = 'white', border = 'black', borderWidth = 0.5)
i2 = Label('Instructions - Notepad', 0, i1.top + 8)
i3 = Label('Open the apps and try them out', 0, i1.top + 25, size = 10)
i4 = Label('Have fun!', 0, i1.top + 40, size = 10)

i2.left, i3.left, i4.left = i1.left + 5, i1.left + 6, i1.left + 6

info = Group(i1, i2, i3, i4)

closebox = Rect(i1.right - 30, i1.top + 1, 29, 20, fill = 'white')
cross1 = Line(closebox.left + 9, closebox.top + 5, closebox.right - 9, closebox.bottom - 5, lineWidth = 1)
cross2 = Line(closebox.right - 9, closebox.top + 5, closebox.left + 9, closebox.bottom - 5, lineWidth = 1)

cross = Group(cross1, cross2)
closenp = Group(closebox, cross)

np = Group(info, closenp)
np.visible = False


###DESKTOP
chrome.centerX = 30
chrome.centerY = 30
spotify.centerX = 75
spotify.centerY = 30
steam.centerX = 120
steam.centerY = 30
notepad.centerX = 165
notepad.centerY = 28


###ERROR
err = Rect(100, 150, 200, 100, fill = 'whitesmoke', border = 'lightgray')

errtitle = Label('', err.left + 18, err.top + 7, opacity = 60, size = 8)
errmsg = Label('', err.left + 70, err.centerY - 28, size = 10, fill = 'midnightblue')

errinf1 = Label('A problem caused the program to stop working correctly.', err.centerX, err.centerY, size = 7.5)
errinf2 = Label('Windows will close the program and notify you if', err.centerX - 13, err.centerY+10, size = 7.5)
errinf3 = Label('a solution is available', err.centerX - 57, err.centerY+20, size = 7.5)

errescbox = Rect(232, 230, 63, 15, fill = None, border = 'dodgerblue')
erresc = Label('Close program', errescbox.centerX, errescbox.centerY, size = 8)

error = Group(err, errtitle, errmsg, errinf1, errinf2, errinf3, errescbox, erresc)
error.visible = False

error2 = Group(
    Rect(0, 0, 400, 400, fill = gradient('lightblue', 'royalblue', start = 'bottom-left')),
    Rect(50, 150, 300, 100, fill = 'white'),
    Label('Application Error', 102, 160, size = 13),
    Label('The application was unable to start correctly (0xc000007b).', 200, 190, size = 11),
    Label('Run again to close the application and restart.', 169, 210, size = 11))
error2.visible = False
app.game1playing = False
app.game2playing = False
app.game3playing = False


#####FUNCTIONS
def appsetting(boolean):
    calculatoricon.visible = boolean
    spotify.visible = boolean
    steam.visible = boolean
    notepad.visible = boolean
    chrome.visible = boolean
    
def getRandomHeight():
    heightindex = randrange(0, 3)
    heights = [290, 280, 270]
    height = heights[heightindex]
    return height

for x in range(1000, 10000, 200):
    height = getRandomHeight()
    obstacles.add(Rect(x, height, 25, 30))
app.obstaclestart = obstacles.centerX


###MOUSEPRESS
def onMouseRelease(mouseX, mouseY):
    if search1.contains(mouseX, mouseY) and topchrome.visible == True or search2.contains(mouseX, mouseY) and topchrome.visible == True:
        middlechrome.visible = False
        topchrome.visible = False
        app.chromerunning = True
        app.background = 'white'
        obstacles.visible = True

        
    if chrome.hits(mouseX, mouseY) and chrome.visible == True:
        appsetting(False)
        topchrome.visible = True
        middlechrome.visible = True
        windowslogo.visible = False
        closebrowser.visible = True
    
    if closebrowser.contains(mouseX, mouseY) and topchrome.visible == True:
        topchrome.visible = False
        middlechrome.visible = False
        closebrowser.visible = False
        windowslogo.visible = True
        app.background = gradient('lightblue', 'royalblue', start = 'bottom-left')
        appsetting(True)

    if spotify.hits(mouseX, mouseY) and spotify.visible == True:
        errtitle.value = 'Spotify'
        errmsg.value = 'Spotify has stopped working'
        error.visible = True
        error.toFront()
        
    if calculatoricon.hits(mouseX, mouseY) and calculatoricon.visible == True:
        calculator.visible = True
        calculator.toFront()
        
    if steam.hits(mouseX, mouseY) and steam.visible == True:
        cleardesktop()
        showsteam(True)
        steammenu.visible = True
    
    if notepad.hits(mouseX, mouseY) and notepad.visible == True:
        np.visible = True
    
    if info.hits(mouseX, mouseY) and error.hits(mouseX, mouseY) == False:
        np.toFront()
    
    if closenp.contains(mouseX, mouseY):
        np.visible = False
    
    if errescbox.contains(mouseX, mouseY):
        error.visible = False
    
    if steammenu.visible == True and steamlist[0].hits(mouseX, mouseY) and app.load1.visible == False and error2.visible == False:
        steamlist[0] = Rect(20, 130, 100, 40, fill = 'white')
        
    if steammenu.visible == True and steamlist[2].hits(mouseX, mouseY) and app.load2.visible == False and error2.visible == False:
        steamlist[2] = Rect(150, 130, 100, 40, fill = 'white')
        
    if steammenu.visible == True and steamlist[4].hits(mouseX, mouseY) and app.load3.visible == False and error2.visible == False:
        steamlist[4] = Rect(280, 130, 100, 40, fill = 'white')
        
    if app.game1downloaded == True and app.load1.hits(mouseX, mouseY):
        steammenu.clear()
        showsteam(False)
        options.clear()
        error2.visible = True
        error2.toFront()
        app.game1playing = True
    if app.game2downloaded == True and app.load2.hits(mouseX, mouseY):
        steammenu.clear()
        showsteam(False)
        options.clear()
        error2.visible = True
        error2.toFront()
        app.game2playing = True
    if app.game3downloaded == True and app.load3.hits(mouseX, mouseY):
        steammenu.clear()
        showsteam(False)
        options.clear()
        error2.visible = True
        error2.toFront()
        app.game3playing = True
        
    if gorect.hits(mouseX, mouseY) and gorect.visible == True:
        gorect.visible = False
        golabel.visible = False
        topchrome.visible = True
        middlechrome.visible = True
        player.centerX = 200
        obstacles.centerX = app.obstaclestart
        score.value = 0
        player.bottom = 300
        
     
        
###KEYPRESS
def onKeyPress(key):
    if key == 'space' and player.bottom == 300:
        app.speed = app.jump


###MOUSEMOVE
def onMouseMove(mouseX, mouseY):
    if closenp.contains(mouseX, mouseY):
        closebox.fill = 'red'
        cross.fill = 'white'
    else:
        closebox.fill = 'white'
        cross.fill = 'black'
    
    if steammenu.visible == True and steamlist[0].contains(mouseX, mouseY):
        steamlist[1].opacity = 100
    elif steammenu.visible == True and steamlist[0].contains(mouseX, mouseY) == False:
        steamlist[1].opacity = 80
        
    if steammenu.visible == True and steamlist[2].contains(mouseX, mouseY):
        steamlist[3].opacity = 100
    elif steammenu.visible == True and steamlist[2].contains(mouseX, mouseY) == False:
        steamlist[3].opacity = 80   
        
    if steammenu.visible == True and steamlist[4].contains(mouseX, mouseY):
        steamlist[5].opacity = 100
    elif steammenu.visible == True and steamlist[4].contains(mouseX, mouseY) == False:
        steamlist[5].opacity = 80

#####TEST
def cleardesktop():
    windowslogo.clear()
    chrome.clear()
    spotify.clear()
    steam.clear()
    notepad.clear()
    np.clear()
    error.clear()
    

###STEAMMENU
menu1 = Rect(0, 140, 400, 260, fill = 'gray')
menu2 = Rect(0, 0, 410, 195, fill = 'dimgray')
game1 = Group(
    Rect(20, 20, 100, 100, fill = 'white'),
    Label('Small', 70, 70, size = 20, fill = 'lime')
    )
    
game2 = Group(
    Rect(150, 20, 100, 100, fill = 'white'),
    Label('Big', 200, 70, size = 20, fill = 'red')
    )

game3 = Group(
    Rect(280, 20, 100, 100, fill = 'white'),
    Label('Medium', 330, 70, size = 20, fill = 'yellow')
    )

steammenu = Group(menu1, menu2, game1, game2, game3)
steammenu.visible = False

steamlist = []

def showsteam(boolean):
    for x in range(20, 380, 130):
        steamlist.append(Rect(x, 130, 100, 40, fill = gradient('darkslateblue', 'royalblue', start = 'right-top')))
        steamlist.append(Label('INSTALL', x + 50, 150, fill = 'white', size = 22, opacity = 80))
    for i in range(len(steamlist)):
        steamlist[i].visible = boolean
  
  
###STEAMOPTIONS
app.load1 = Line(20, 150, 20, 150, fill = 'lime', lineWidth = 40)
app.play1 = Label('PLAY', 70, 150, fill = 'white', size = 25)

app.load2 = Line(150, 150, 150, 150, fill = 'lime', lineWidth = 40)
app.play2 = Label('PLAY', 200, 150, fill = 'white', size = 25)

app.load3 = Line(280, 150, 280, 150, fill = 'lime', lineWidth = 40)
app.play3 = Label('PLAY', 330, 150, fill = 'white', size = 25)

app.game1downloaded = False
app.game2downloaded = False
app.game3downloaded = False

options = Group(app.load1, app.play1, app.load2, app.play2, app.load3, app.play3)
options.visible = False
    
def onStep():
    if steammenu.visible == True and steamlist[0].fill == 'white' and app.load1.x2 < 120:
        app.load1.toFront()
        app.load1.visible = True
        app.load1.x2 += 1

    if app.load1.x2 == 120:
        app.play1.visible = True
        app.game1downloaded = True
        
    if steammenu.visible == True and steamlist[2].fill == 'white' and app.load2.x2 < 250:
        app.load2.toFront()
        app.load2.visible = True
        app.load2.x2 += 0.25

    if app.load2.x2 == 250:
        app.play2.visible = True
        app.game2downloaded = True
        
    if steammenu.visible == True and steamlist[4].fill == 'white' and app.load3.x2 < 380:
        app.load3.toFront()
        app.load3.visible = True
        app.load3.x2 += 0.5

    if app.load3.x2 == 380:
        app.play3.visible = True
        app.game3downloaded = True
        
    if app.game1downloaded == True and app.game1playing == True:
        app.load1.visible = False
        app.play1.visible = False
        app.load2.visible = False
        app.play2.visible = False
        app.load3.visible = False
        app.play3.visible = False
    
    if app.game2downloaded == True and app.game2playing == True:
        app.load1.visible = False
        app.play1.visible = False
        app.load2.visible = False
        app.play2.visible = False
        app.load3.visible = False
        app.play3.visible = False
    
    if app.game3downloaded == True and app.game3playing == True:
        app.load1.visible = False
        app.play1.visible = False
        app.load2.visible = False
        app.play2.visible = False
        app.load3.visible = False
        app.play3.visible = False
    
    if app.chromerunning == True:
        player.visible = True
        score.visible = True
        groundmap.visible = True
        noint.visible = True
        app.steps += 1
        obstacles.centerX -= 10
        app.speed += app.dy
        player.centerY += app.speed
        score.centerY += app.speed
        score.centerX = player.centerX
        
        if score.value == 100:
            app.chromerunning = False
            player.visible = False
            score.visible = False
            groundmap.visible = False
            noint.visible = False
            obstacles.visible = False
            golabel.visible = True
            golabel.value = 'You won! Click the box to restart'
            gorect.visible = True
        
        if player.bottom >= 300:
                player.bottom = 300
                score.bottom = player.bottom - 60
        
        if player.hitsShape(obstacles):
            golabel.value = f'You died with the score {score.value}. Click the box to restart.'
            app.chromerunning = False
            player.visible = False
            score.visible = False
            groundmap.visible = False
            noint.visible = False
            obstacles.visible = False
            golabel.visible = True
            gorect.visible = True
            
        if app.steps % 10 == 0:
            score.value += 1
cmu_graphics.run() 