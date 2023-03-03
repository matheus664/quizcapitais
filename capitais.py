
from asyncore import read
from PySimpleGUI import PySimpleGUI as sg
import sqlite3 as sq

sg.theme('DARKBLUE')   


c=open("banco_cadastro.db","r")
print(len(c))


def janela_login():
    layout = [
        [sg.Text('Usuário')],[sg.Input(key='usuario')],
        [sg.Text('Senha')],[sg.Input(key='senha1',password_char='*')],

        [sg.Button('Continuar')],
        [sg.Checkbox('Esqueceu a senha?',key='esc1')],

    ]

    return sg.Window('QUIZCAPITAIS',layout,finalize=True,no_titlebar=False,keep_on_top=True,transparent_color=True)


def janela_pergunta1():
    layout = [
        [sg.Text('Qual a capital do estado de Roraima?')],

        [sg.Checkbox('Cuiabá',key='cuia1')],
        [sg.Checkbox('João Pessoa',key='joa1')],
        [sg.Checkbox('Boa Vista',key='boa1')],
        [sg.Checkbox('São Luiz',key='luiz1')],

        [sg.Button('Voltar')],
        [sg.Button('Próxima pergunta')],

     ]

    return sg.Window('Pergunta1',layout,finalize=True)


def janela_pergunta2():
    layout = [
        [sg.Text('Qual a capital do estado do Amapá?')],

        [sg.Checkbox('Rio Branco',key='rio1')],
        [sg.Checkbox('Salvador',key='salva1')],
        [sg.Checkbox('São Luiz',key='luiz2')],
        [sg.Checkbox('Macapá',key='maca1')],

        [sg.Button('Anterior')],
        [sg.Button('Próxima pergunta')],
        
    ]

    return sg.Window('Pergunta2',layout,finalize=True)

def janela_pergunta3():
    layout= [
        [sg.Text('Qual a capital do estado do Rio Grande do Norte?')],

        [sg.Checkbox('Curitiba',key='curi1')],
        [sg.Checkbox('Recife',key='reci1')],
        [sg.Checkbox('Vitória',key='vito1')],
        [sg.Checkbox('Natal',key='nata1')],
        
        [sg.Button('Anterior')],
        [sg.Button('Próximo')],
    ]

    return sg.Window('Pergunta3',layout,finalize=True)

def janela_pergunta4():
    layout = [
        [sg.Text('Qual a capital do estado do Acre?')],

        [sg.Checkbox('Curitiba',key='curi2')],
        [sg.Checkbox('Vitoria',key='vito1')],
        [sg.Checkbox('Riobranco',key='rio2')],
        [sg.Checkbox('Florianópolis',key='floripa1')],

        [sg.Button('Anterior')],
        [sg.Button('Próximo')],
    
    ]
    return sg.Window('Pergunta4',layout,finalize=True)




janela1,janela2,janela3,janela4,janela5=janela_login(),None,None,None,None

while True:
    window,event,values=sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break

    if window == janela1 and event == 'Continuar':
        if values ['usuario'] == 'matheus' and values ['senha1'] == '301099':
            sg.popup_notify('Bem Vindo, Vamos testar seus conhecimentos?',display_duration_in_ms=0.5)
            janela2= janela_pergunta1()
            janela1.hide()
        else :
            sg.popup_ok('Digite a senha correta!')

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'Próxima pergunta':
        if values ['boa1'] == True:
            sg.popup_notify('Acertou Mizeravi!',display_duration_in_ms=0.5)
        else:
            sg.popup_ok('Resposta Errada!',auto_close_duration=0.5)
        janela3=janela_pergunta2()
        janela2.hide()

    if window == janela3 and event == 'Anterior':
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Próxima pergunta':
        if values ['maca1'] == True:
            sg.popup_notify('Acertou Mizeravi!',display_duration_in_ms=0.5)
        else:
            sg.popup_ok('Resposta Errada!',auto_close_duration=0.5)
        janela4=janela_pergunta3()
        janela3.hide()

    if window == janela4 and event == 'Anterior':
        janela4.hide()
        janela3.un_hide()

    if window == janela4 and event == 'Próximo':
        if values ['nata1'] == True:
            sg.popup_notify('Acertou Mizeravi!',display_duration_in_ms=0.5)
        else:
            sg.popup_ok('Resposta Errada!',auto_close_duration=0.5)
        janela5=janela_pergunta4()
        janela4.hide()

    if window == janela5 and event == 'Anterior':
        janela5.hide()
        janela4.un_hide()
        
        
    print(event,values)