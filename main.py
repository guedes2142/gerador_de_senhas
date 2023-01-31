import PySimpleGUI as sg
import random
import string

sg.theme('BLACK')
sg.set_options(font='verdana 12')
layout = [
        [sg.Image('max.png')],
        [sg.Text('Uppercase: '), sg.Push(), sg.Input(size=12, key='-UP-')],
        [sg.Text('Lowercase: '), sg.Push(),sg.Input(size=12, key='-LOW-')],
        [sg.Text('Digits: '), sg.Push(),sg.Input(size=12, key='-DIG-')],
        [sg.Text('Symbols: '), sg.Push(),sg.Input(size=12, key='-SYM-')],
        [sg.Button('OK'), sg.Button('Cancel')],
        [sg.Text('Password'),sg.Push(), sg.Multiline(size= 12, no_scrollbar=True, disabled=True, key='-PASS-')]

]

window = sg.Window('Max Password Gen 1.0', icon='maxico.ico').Layout(layout)

while True:

    event, values = window.read()
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
 
    if event == 'OK':

        try:
            u_upper = int(values['-UP-'])
            upper = random.sample(string.ascii_uppercase, u_upper)
            u_lower = int(values['-LOW-'])
            lower = random.sample(string.ascii_lowercase, u_lower)
            u_digits = int(values['-DIG-'])
            digits = random.sample(string.digits, u_digits)
            u_symbos = int(values['-SYM-'])
            symbols = random.sample(string.punctuation, u_symbos)

            total = upper+lower+digits+symbols

            total = random.sample(total, len(total))
            total = ''.join(total)
            window['-PASS-'].update(total)
        except ValueError:
            window['-PASS-'].update('Sem números válidos')

window.close()




