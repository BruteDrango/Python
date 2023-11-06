from pathlib import Path
import PySimpleGUI as sg
import pandas as pd

#########-------Adding Colour to Window-----#######
sg.theme('DarkTeal9')

current_dir = Path(_file_).parent if '_file_' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'SZ.xlsx'

#########------Load the data if the file exists, if not, create a new DataFrame------##########

if EXCEL_FILE.exists():
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.DataFrame()

layout = [
    [sg.Text('This is all the Information about SZ DOs:-')],
    [sg.Text('Admin Name', size=(15,1)), sg.InputText( key='Admin Name')],
    [sg.Text('DO Name', size=(15,1)), sg.InputText( key='DO Name')],
    [sg.Text('DO Code', size=(15,1)), sg.InputText( key='DO Code')],
    [sg.Text('Present at DO', size=(15,1)),
     sg.Checkbox('Morning', key='Morning'),
     sg.Checkbox('Afternoon', key='Afternoon'),
     sg.Checkbox('Evening', key='Evening')],
    [sg.Text('Total Office Hours', size=(15,1)), sg.Spin([i for i in range(0,24)],
                                                      initial_value=0, key= 'Total Office Hours')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('SZ DO Details', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False) #-This will create the file if doesn`t exist
        sg.popup('Data saved!!!')
        clear_input()
window.close()