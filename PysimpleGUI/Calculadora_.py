import PySimpleGUI as sg

#Default settings - Layout
'''bw > button white ; bt > button than ; bo > button orange'''
bw = {'size':(3,1), 'font':('Franklin Gothic Book', 24), 'button_color':('black','#F8F8F8'),'mouseover_colors':'#D4CFFF'}
bt = {'size':(3,1), 'font':('Franklin Gothic Book',24), 'button_color':('black','#F1EABC'),'mouseover_colors':'#F5D294'}
bo = {'size':(7,1), 'font':('Franklin Gothic Book', 24), 'button_color':('black','#ECA527'),'mouseover_colors':'#B8801F', 'focus':True}

#Creating Layout
layout =[
    [sg.Text('Calculadora GGG',size=(41,1), justification='right', background_color='#272533',text_color='white', font=('Franklin Gothic Book',12,'bold'))],
    [sg.Text('0.00', size=(15,1), justification='right',background_color='black',text_color='red', font=('Digital-7',42), relief='sunken', key='_DISPLAY_')],
    [sg.Text('', background_color='#272533')],
    [sg.Button('%',**bt), sg.Button('CE',**bt),sg.Button('C',**bt),sg.Button('←',**bt)],
    [sg.Button('¹/x',**bt), sg.Button('x²',**bt),sg.Button('²√x',**bt),sg.Button('/',**bt)],
    [sg.Button('7',**bw),sg.Button('8',**bw),sg.Button('9',**bw),sg.Button('*',**bt)],
    [sg.Button('4',**bw),sg.Button('5',**bw),sg.Button('6',**bw),sg.Button('-',**bt)],
    [sg.Button('1',**bw), sg.Button('2',**bw),sg.Button('3',**bw),sg.Button('+',**bt)],
    [sg.Button('0',**bw),sg.Button('.',**bw),sg.Button('=',**bo,bind_return_key=True)]

]


#Creating Window
window: object = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(297, 570), return_keyboard_events=True)

#Calculation functions
var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

#Helper Functions
def format_number() -> float:
    '''Create a consolidate String of numbers from front and back list..'''
    return float(''.join(var['front']).replace(',','') + '.' + ''.join(var['back']))

def update_display(display_value):
    ''' Update the calculator display after an event click '''
    try:
        window['_DISPLAY_'].update(value='{:,.2f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)

#Clic event
def number_click(event: str):
    '''Number of button click event'''
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())

def clear_click():
    '''CE or C button click event'''

    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False

def operator_click():
    ''' '+', '-', '/' or '*'  button click'''
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']

    clear_click()

def calculate_click():
    '''Equal button click event'''
    global var
    try:
        var['y_val'] = format_number()
    except ValueError: #When equal is pressed without any input
        var['x_val'] = var['result']

    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val'] ))
        update_display(var['result'])
        clear_click()
    except:
        update_display('  Error !!! ')
        clear_click()
    print(var['result'])

def back_click():
    ''' '←' delete one digit'''
    global var

    a = str(var['result'])
    a = a[:-1]
    var['result'] = a
    update_display(var['result'])

def fraction_click():
    ''' '¹/x' do fraction'''
    global var
    try:
        var['result'] = 1/(format_number())

    except:
        update_display('  Error !!! ')
        clear_click()

    update_display(var['result'])

def square_click():
    ''' 'x²' square operation '''
    try:
        var['result'] = format_number()*format_number()
        clear_click()

    except:
        update_display('  Error !!! ')
        clear_click()
    update_display(var['result'])

def square_root_click():
    ''' '²√x' '''
    global var
    try:

        var['result'] = format_number()**(1/2)
    except:
        update_display('  Error !!! ')
        clear_click()
    update_display(var['result'])


#Loop
while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    elif event in['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    elif event in ['Escape:27','C','CE']:
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    elif event in ['+','-','*','/']:
        operator_click()
    elif event == '=':
        calculate_click()
    elif event == '.':
        var['decimal'] = True
    elif event == '%':
        update_display(var['result']/100.0)
    elif event == '←':
        back_click()
    elif event == '¹/x':
        fraction_click()
    elif event == 'x²':
        square_click()
    elif event == '²√x':
        square_root_click()