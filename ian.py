from PySimpleGUI import PySimpleGUI as sg


#layout
sg.theme ('Reddit')
layout = [
            [sg.text('Usuario'), sg.Input(key='usuario')],
            [sg.tex('Senha'), sg.Input(key='senha', password_char='*')],
            [sg.Checkbox('Savar o login')],
            [sg.Button('Entrar')],      
             
    ]
    #janela
janela = sg.Window('Tela de Login', layout),
    
    #ler os eventos 
while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Entar':
            if valores ['usuarios'] == 'ian' and valores ['senha'] == '12345':
                print ('Bem vindo ao login Ian!')
             