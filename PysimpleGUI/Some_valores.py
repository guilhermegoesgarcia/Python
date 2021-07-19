import PySimpleGUI as sg

#creating layout
layout = [
    [sg.Text('Entre com os numeros:')],
    [sg.InputText(key='valor1'),sg.Text('+'),sg.InputText(key='valor2')],
    [],
    [sg.Text('.. Calculando ..', key='resp0')],
    [sg.Button('Calcular')]
]

#creating window
window = sg.Window('Calculadora',layout)

#loop
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    resp = int(values['valor1']) + int(values['valor2'])
    window['resp0'].update(resp)
window.close()