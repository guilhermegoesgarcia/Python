import PySimpleGUI as sg

#creating layout
layout = [[sg.Text('Formulario de Inscrição')],
          [sg.Text('Nome:',pad=((5,10),(0,0))), sg.InputText(size=(30,1))],
          [sg.Text('Telefone:',pad=((5,7),(0,0))), sg.InputText(size=(20,1))],
          [sg.Text('Cidade:',pad=((5,15),(0,0))),sg.InputText(size=(20,1))],
          [sg.Button('Enviar',pad=((5,0),(50,0))),sg.Button('Cancelar',pad=((5,0),(50,0)))]
]

# creating window
window = sg.Window('Formulário',layout,size=(500,250))

#event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancelar":
        break
    print('User:', values)
window.close()