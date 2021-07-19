import PySimpleGUI as sg

#creating layout
layout = [[sg.Text('texto primeira linha')],
          [sg.Text('texto segunda linha'), sg.InputText()],
          [sg.Button('OK', pad=((0,0),(0,0))), sg.Button('Cancel')]
]

#creating a window
window = sg.Window('Hello', layout, size=(500, 200))

#Event loop to precess 'events' and get the 'values' of inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =='Cancel':
        break
    print('USER_TEXTO: ',values[0])
window.close()