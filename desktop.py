from cmu_graphics import *

###windows
app.background = gradient('lightblue', 'royalblue', start = 'bottom-left')
app.stepsPerSecond = 2

red = Rect(140, 140, 55, 55, fill = gradient('white', 'salmon', 'orangered', start = 'bottom-right'))
green = Rect(205, 140, 55, 55, fill = gradient('white', 'springgreen', 'limegreen', start = 'bottom-left'))
blue = Rect(140, 205, 55, 55, fill = gradient('white', 'skyblue', 'deepskyblue', start = 'top-right')) 
yellow = Rect(205, 205, 55, 55, fill = gradient('white', 'palegoldenrod', 'yellow', start = 'top-left'))

windowslogo = Group(red, green, blue, yellow)
app.gamestart = False


###apps
#chrome
c1 = Arc(200, 200, 30, 30, 300, 120, fill = 'red')
c2 = Arc(200, 200, 30, 30, 60, 120, fill = 'yellow')
c3 = Arc(200, 200, 30, 30, 180, 120, fill = 'green')
c4 = Circle(200, 200, 8, fill = 'white')
c5 = Circle(200, 200, 5, fill = 'dodgerblue')
chrome = Group(c1, c2, c3, c4, c5)

#spotify
s1 = Circle(200, 200, 15, fill = rgb(30, 215, 96))
s2 = Oval(200, 193, 20, 5)
s3 = Oval(200, 200, 20, 4.5)
s4 = Oval(200, 207, 20, 4)
s5 = Oval(200, 195, 20, 3, fill = rgb(30, 215, 96))
s6 = Oval(200, 202, 20, 3, fill = rgb(30, 215, 96))
s7 = Oval(200, 209, 20, 3, fill = rgb(30, 215, 96))
spotify = Group(s1, s2, s3, s4, s5, s6, s7)

#steam
st1 = Circle(200, 200, 15, fill = gradient('midnightblue', 'darkblue', 'steelblue', start = 'top'))
st2 = Circle(205, 195, 5, fill = 'white')
st3 = Line(202, 198, 196, 205, fill = 'white', lineWidth = 3)
st4 = Circle(205, 195, 4, fill = 'white', border = 'midnightblue', borderWidth = 1)
st5 = Circle(195, 205, 4, fill = 'white')
st6 = Circle(195, 205, 3, fill = 'white', border = 'darkblue', borderWidth = 0.8)
st7 = Line(195, 205, 185, 202, fill = 'white', lineWidth = 3)

steam = Group(st1, st2, st3, st4, st5, st6, st7)

#notepad
n1 = Rect(200, 200, 25, 30, fill = 'white')
n1.centerX = 200
n1.centerY = 200
n2 = Polygon(n1.centerX - 13, n1.top, n1.centerX - 18, n1.bottom - 5, n1.centerX + 9, n1. bottom - 5, n1.centerX + 12, n1.top, fill = 'lightblue')
n3 = Line(187, 185, 212, 185, dashes = True, fill = 'darkgray')
notepad = Group(n1, n2, n3)

i1 = Rect(50, 100, 300, 200, fill = 'white', border = 'black', borderWidth = 0.5)
i2 = Label('Instructions - Notepad', i1.left + 62, i1.top + 8)
i3 = Label('Open up the terminal.', i1.left + 55, i1.top + 30, size = 10)
i4 = Label('Type the following: "run game.exe"', i1.left + 84, i1.top + 45, size = 10)

info = Group(i1, i2, i3, i4)

closebox = Rect(i1.right - 30, i1.top + 1, 29, 20, fill = 'white')
cross1 = Line(closebox.left + 9, closebox.top + 5, closebox.right - 9, closebox.bottom - 5, lineWidth = 1)
cross2 = Line(closebox.right - 9, closebox.top + 5, closebox.left + 9, closebox.bottom - 5, lineWidth = 1)

cross = Group(cross1, cross2)
closenp = Group(closebox, cross)

np = Group(info, closenp)
np.visible = False


###desktop
chrome.centerX = 30
chrome.centerY = 30
spotify.centerX = 75
spotify.centerY = 30
steam.centerX = 120
steam.centerY = 30
notepad.centerX = 165
notepad.centerY = 28


###error
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


###opening apps function
def onMousePress(mouseX, mouseY):
    if chrome.hits(mouseX, mouseY):
        errtitle.value = 'Chrome'
        errmsg.value = 'Chrome has stopped working'
        error.visible = True
        error.toFront()

    if spotify.hits(mouseX, mouseY):
        errtitle.value = 'Spotify'
        errmsg.value = 'Spotify has stopped working'
        error.visible = True
        error.toFront()

    if steam.hits(mouseX, mouseY):
        errtitle.value = 'Steam'
        errmsg.value = 'Steam has stopped working'
        error.visible = True
        error.toFront()
    
    if notepad.hits(mouseX, mouseY):
        np.visible = True
    
    if info.hits(mouseX, mouseY) and error.hits(mouseX, mouseY) == False:
        np.toFront()
    
    if closenp.contains(mouseX, mouseY):
        np.visible = False
    
    if errescbox.contains(mouseX, mouseY):
        error.visible = False

###close function
def onMouseMove(mouseX, mouseY):
    if closenp.contains(mouseX, mouseY):
        closebox.fill = 'red'
        cross.fill = 'white'
    else:
        closebox.fill = 'white'
        cross.fill = 'black'

#####test
def onKeyPress(key):
    if key == 'w':
        app.gamestart = True
        windowslogo.clear()
        chrome.clear()
        spotify.clear()
        steam.clear()
        notepad.clear()
        np.clear()
        app.background = 'black'
        
cmu_graphics.run() 