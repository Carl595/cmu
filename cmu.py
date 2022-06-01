from cmu_graphics import *

app.rows = 5
app.cols = 4
app.dots = makeList(app.rows, app.cols)
app.button = makeList(app.rows, app.cols)
app.stuff = ['C','+/-','%','/','7','8','9','x','4','5','6','-','1','2','3','+','0','','.','=']
app.index = 0
app.val1 = ''
app.action = ''

app.screen = Label('',280,105) 

app.screen.right = 290

app.his = Label('',280,90)

close = Rect(280,25,20,20,fill='red')

calculator = Group(
Rect(100,25,200,345,fill='darkgray'),
Rect(105,50,190,70,border='black',fill='white'),
Label('Calculator',130,35),
)
calculator.add(app.screen,app.his,close,Line(285,30,295,40),
Line(285,40,295,30))
calculator.visible = False


for row in range(app.rows):
    for col in range(app.cols):
        centerX = 125 + col * 50
        centerY = 145 + row * 50
        if app.index < 3:
            color='lightgray'
        elif col == 3:
            color = 'darkcyan'
        else:
            color='white'
        app.dots[row][col] = Circle(centerX, centerY, 20,fill=color)
        app.button[row][col] = Label(app.stuff[app.index],centerX,centerY)
        calculator.add(app.dots[row][col],app.button[row][col])
        app.index += 1

    
         
def onMousePress(mouseX, mouseY):
    if close.hits(mouseX, mouseY):
        calculator.visible = False
    if calculator.visible == True:
        for row in range(app.rows):
            for col in range(app.cols):
                dot = app.dots[row][col]
                if (dot.contains(mouseX, mouseY) == True): 
                    
                    try:
                        if float(app.button[row][col].value) >=0 and len(app.screen.value) <= 24:
                            app.screen.value = str(app.screen.value) + str(app.button[row][col].value)
                    except:
                        if app.button[row][col].value == '.' and app.screen.value !='':
                            app.screen.value += (app.button[row][col].value)
                        if app.button[row][col].value == '+/-' and app.screen.value !='':
                            if str(app.screen.value).find('.') > 0:
                                app.screen.value = -float(app.screen.value)
                            elif str(app.screen.value).find('.') < 0:
                                app.screen.value = -int(app.screen.value)
                        if app.button[row][col].value == '+' and app.val1 != '' and app.action != '' and app.screen.value !='':
                            if str(app.screen.value).find('.') > 0:
                                app.screen.value = float(app.screen.value)
                            elif str(app.screen.value).find('.') < 0:
                                app.screen.value = int(app.screen.value)
                            if str(app.val1).find('.') > 0:
                                app.val1 = float(app.val1)
                            elif str(app.val1).find('.') < 0:
                                app.val1 = int(app.val1)
                            if app.action == '+':
                                app.val1 = app.val1 + app.screen.value
                            if app.action == '-':
                                app.val1 = app.val1 - app.screen.value
                            if app.action == '/':
                                app.val1 = app.val1 / app.screen.value
                            if app.action == 'x':
                                app.val1 =  app.val1 * app.screen.value
                        
                            app.screen.value = ''
                            app.action = '+'
                        elif app.button[row][col].value == '+' and app.val1 != '' and app.screen.value !='':
                            if str(app.screen.value).find('.') > 0:
                                app.screen.value = float(app.screen.value)
                            elif str(app.screen.value).find('.') < 0:
                                app.screen.value = int(app.screen.value)
                            if str(app.val1).find('.') > 0:
                                app.val1 = float(app.val1)
                            elif str(app.val1).find('.') < 0:
                                app.val1 = int(app.val1)
                            app.val1 = app.val1 + app.screen.value
                            app.screen.value = ''
                            app.action = '+'
                        elif app.button[row][col].value == '+' and app.screen.value !='':
                            app.val1 = app.screen.value
                            app.screen.value = ''
                            app.action = '+'
                        elif app.button[row][col].value == '+' and app.screen.value == '':
                            app.action = '+'
                        if app.button[row][col].value == '-' and app.val1 != '' and app.action != '' and app.screen.value !='':
                            if str(app.screen.value).find('.') > 0:
                                app.screen.value = float(app.screen.value)
                            elif str(app.screen.value).find('.') < 0:
                                app.screen.value = int(app.screen.value)
                            if str(app.val1).find('.') > 0:
                                app.val1 = float(app.val1)
                            elif str(app.val1).find('.') < 0:
                                app.val1 = int(app.val1)
                            if app.action == '+':
                                app.val1 = app.val1 + app.screen.value
                            if app.action == '-':
                                app.val1 = app.val1 - app.screen.value
                            if app.action == '/':
                                app.val1 = app.val1 / app.screen.value
                            if app.action == 'x':
                                app.val1 =  app.val1 * app.screen.value
                        
                            app.screen.value = ''
                            app.action = '-'
                        elif app.button[row][col].value == '-' and app.val1 != '' and app.screen.value !='':
                            if str(app.screen.value).find('.') > 0:
                                app.screen.value = float(app.screen.value)
                            elif str(app.screen.value).find('.') < 0:
                                app.screen.value = int(app.screen.value)
                            if str(app.val1).find('.') > 0:
                                app.val1 = float(app.val1)
                            elif str(app.val1).find('.') < 0:
                                app.val1 = int(app.val1)
                            app.val1 = app.val1 - app.screen.value
                            app.screen.value = ''
                            app.action = '-'
                        elif app.button[row][col].value == '-' and app.screen.value !='':
                            app.val1 = app.screen.value
                            app.screen.value = ''
                            app.action = '-'
                        elif app.button[row][col].value == '-' and app.screen.value == '':
                            app.action = '-'
                        if app.button[row][col].value == 'x' and app.val1 != '' and app.action != '' and app.screen.value !='':
                            if str(app.screen.value).find('.') > 0:
                                app.screen.value = float(app.screen.value)
                            elif str(app.screen.value).find('.') < 0:
                                app.screen.value = int(app.screen.value)
                            if str(app.val1).find('.') > 0:
                                app.val1 = float(app.val1)
                            elif str(app.val1).find('.') < 0:
                                app.val1 = int(app.val1)
                            if app.action == '+':
                                app.val1 = app.val1 + app.screen.value
                            if app.action == '-':
                                app.val1 = app.val1 - app.screen.value
                            if app.action == '/':
                                app.val1 = app.val1 / app.screen.value
                            if app.action == 'x':
                                app.val1 =  app.val1 * app.screen.value
                        
                            app.screen.value = ''
                            app.action = 'x'
                        elif app.button[row][col].value == 'x' and app.val1 != '' and app.screen.value !='':
                            if str(app.screen.value).find('.') > 0:
                                app.screen.value = float(app.screen.value)
                            elif str(app.screen.value).find('.') < 0:
                                app.screen.value = int(app.screen.value)
                            if str(app.val1).find('.') > 0:
                                app.val1 = float(app.val1)
                            elif str(app.val1).find('.') < 0:
                                app.val1 = int(app.val1)
                            app.val1 = app.val1 * app.screen.value
                            app.screen.value = ''
                            app.action = 'x'
                        elif app.button[row][col].value == 'x' and app.screen.value !='':
                            app.val1 = app.screen.value
                            app.screen.value = ''
                            app.action = 'x'
                        elif app.button[row][col].value == 'x' and app.screen.value == '':
                            app.action = 'x'

                        try:    
                            if app.button[row][col].value == '/' and app.val1 != '' and app.action != '' and app.screen.value !='':
                                if str(app.screen.value).find('.') > 0:
                                    app.screen.value = float(app.screen.value)
                                elif str(app.screen.value).find('.') < 0:
                                    app.screen.value = int(app.screen.value)
                                if str(app.val1).find('.') > 0:
                                    app.val1 = float(app.val1)
                                elif str(app.val1).find('.') < 0:
                                    app.val1 = int(app.val1)
                                if app.action == '+':
                                    app.val1 = app.val1 + app.screen.value
                                if app.action == '-':
                                    app.val1 = app.val1 - app.screen.value
                                if app.action == '/':
                                    app.val1 = app.val1 / app.screen.value
                                if app.action == 'x':
                                    app.val1 =  app.val1 * app.screen.value
                            
                                app.screen.value = ''
                                app.action = '/'
                            elif app.button[row][col].value == '/' and app.val1 != '' and app.screen.value !='':
                                if str(app.screen.value).find('.') > 0:
                                    app.screen.value = float(app.screen.value)
                                elif str(app.screen.value).find('.') < 0:
                                    app.screen.value = int(app.screen.value)
                                if str(app.val1).find('.') > 0:
                                    app.val1 = float(app.val1)
                                elif str(app.val1).find('.') < 0:
                                    app.val1 = int(app.val1)
                                app.val1 = app.val1 / app.screen.value
                                app.screen.value = ''
                                app.action = '/'
                            elif app.button[row][col].value == '/' and app.screen.value !='':
                                app.val1 = app.screen.value
                                app.screen.value = ''
                                app.action = '/'
                            elif app.button[row][col].value == '/' and app.screen.value == '':
                                app.action = '/'
                            if app.button[row][col].value == '%' and app.screen.value !='':
                                if str(app.screen.value).find('.') > 0:
                                    app.screen.value = float(app.screen.value)
                                elif str(app.screen.value).find('.') < 0:
                                    app.screen.value = int(app.screen.value)
                                app.screen.value = app.screen.value / 100
                        except:
                            app.screen.value = 'error'
                            app.val1 = ''
                            
                            
                        
                        if app.button[row][col].value == 'C':
                            app.val1 = ''
                            app.screen.value = ''
                            app.action = ''
                        

                        if app.button[row][col].value == '=' and app.screen.value !='' and app.val1 !='':
                            if str(app.screen.value).find('.') > 0:
                                app.screen.value = float(app.screen.value)
                            elif str(app.screen.value).find('.') < 0:
                                app.screen.value = int(app.screen.value)
                            
                            if str(app.val1).find('.') > 0:
                                app.val1 = float(app.val1)
                            elif str(app.val1).find('.') < 0:
                                app.val1 = int(app.val1)

                            
                            if app.action == '+':
                                app.screen.value = app.val1 + app.screen.value
                                app.val1 = ''
                            if app.action == '-':
                                app.screen.value = app.val1 - app.screen.value
                                app.val1 = ''
                            try:
                                if app.action == '/':
                                    app.screen.value = app.val1 / app.screen.value
                                    app.val1 = ''
                            except:
                                app.screen.value = 'error'
                                app.val1 = ''
                            if app.action == 'x':
                                app.screen.value = app.val1 * app.screen.value
                                app.val1 = ''
                    app.screen.right = 290   
                    app.his.value = app.val1   
                    app.his.right = 290   