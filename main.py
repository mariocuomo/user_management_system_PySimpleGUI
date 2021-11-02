import PySimpleGUI as sg
import re
import datetime
import csv
from csv import writer
import os
import numpy as np
import pandas as pd
from pandas import DataFrame

utenti=[]
sg.theme('Reddit')


#funzione per tornare alla homepage
#nasconde tutto e mostra i bottoni VEDI UTENTI e INSERISCI UTENTE
def tornaAHomepage():
    window.Element('vedi_utenti').Update(disabled = False)
    window.Element('inserisci_utenti').Update(disabled = False)

    window.Element('nome_input').Update('')
    window.Element('cognome_input').Update('')
    window.Element('email_input').Update('')
    window.Element('data_input').Update('')
    window.Element('errore').Update(value='')



    window.Element('nome_input').Update(disabled = False)
    window.Element('cognome_input').Update(disabled = False)
    window.Element('email_input').Update(disabled = False)
    window.Element('data_input').Update(disabled = False)
    window.Element('AVANTI').Update(disabled = True)


    window.Element('inserisci_dati').Update(visible = False)
    window.Element('nome_text').Update(visible = False)
    window.Element('nome_input').Update(visible = False)
    window.Element('cognome_text').Update(visible = False)
    window.Element('cognome_input').Update(visible = False)
    window.Element('email_text').Update(visible = False)
    window.Element('email_input').Update(visible = False)
    window.Element('data_text').Update(visible = False)
    window.Element('data_input').Update(visible = False)

#funzione per stampare l'errore di formato sbagliato nei campi TEXT
def errore(campo):
    stringa = "campo " + campo + " non valido"
    window.Element('errore').Update(value=stringa)

#funzione per pulire la schermata dopo aver insierito un utente
def pulisciSchermata():
    window.Element('nome_input').Update('')
    window.Element('cognome_input').Update('')
    window.Element('email_input').Update('')
    window.Element('data_input').Update('')

    window.Element('nome_input').Update(disabled = False)
    window.Element('cognome_input').Update(disabled = False)
    window.Element('email_input').Update(disabled = False)
    window.Element('data_input').Update(disabled = False)

    window.Element('cognome_text').Update(visible = False)
    window.Element('cognome_input').Update(visible = False)
    window.Element('email_text').Update(visible = False)
    window.Element('email_input').Update(visible = False)
    window.Element('data_text').Update(visible = False)
    window.Element('data_input').Update(visible = False)

    window.Element('NUOVO').Update(visible = False)
    window.Element('AVANTI').Update(text='AVANTI')

#funzione per nascondere il menu e mostrare la schermata di inserimento utenti
def inserisciUtenti():
    window.Element('vedi_utenti').Update(disabled = True)
    window.Element('inserisci_utenti').Update(disabled = True)
    window.Element('inserisci_dati').Update(visible = True)
    window.Element('AVANTI').Update(disabled = False)

#funzione per nascondere il menu e mostrare la schermata di visualizzazione utenti
def vediUtenti(utenti):
    window.Element('vedi_utenti').Update(disabled = True)
    window.Element('inserisci_utenti').Update(disabled = True)
    window.Element('AVANTI').Update(disabled = False)
    window['-Column-'].expand(True,True,True)
    window.Element('-Column-').Update(visible = True)
    window.Element('-INPUT-').Update(visible = True)
    window.Element('CERCA').Update(visible = True)
    window.Element('-TABLE-').Update(values=utenti)

#funzione per salvare il nuovo utente nel CSV
def salvaInCSV():
    if not os.path.exists('utenti.csv'):
        np.savetxt("utenti.csv", [], delimiter=",", fmt='%s', header="nome,cognome,email, data di nascita")
    with open('utenti.csv', 'a', newline='') as file:
                writer_object = writer(file)
                writer_object.writerow(utente)  
                file.close()


headings = ['      NOME      ','      COGNOME      ','      EMAIL      ','      DATA DI NASCITA      ']
utenti = [['1','1','1','1']]


layout = [
            [sg.Text("BENVENUTO!", key='benvenuto', expand_y=True)],
            [sg.Button("VEDI UTENTI", key='vedi_utenti'),sg.Button("INSERISCI UTENTE", key='inserisci_utenti',expand_y=True)],
            [sg.Text("Inserisci i dati dell'utente", key='inserisci_dati', visible = False,expand_y=True)],
            [sg.Text('Nome', size =(15, 1), key='nome_text', visible = False,expand_y=True)],
            [sg.InputText(key='nome_input',visible = False,expand_y=True)],
            [sg.Text('Cognome', size =(15, 1), visible = False, key='cognome_text',expand_y=True)],
            [sg.InputText(key='cognome_input', visible = False,expand_y=True)],
            [sg.Text('Email', size =(15, 1), visible = False, key='email_text',expand_y=True)],
            [sg.InputText(key='email_input', visible = False,expand_y=True)],
            [sg.Text('Data di nascita (gg/mm/aa)', size =(30, 1), visible = False, key='data_text',expand_y=True)],
            [sg.InputText(key='data_input', visible = False,expand_y=True)],
            [sg.Input(size=(33, 1), key='-INPUT-',  visible=False,expand_y=True)],
            [sg.Button('CERCA',visible=False,expand_y=True)],
            [sg.pin(sg.Column([[sg.Table(utenti, headings=headings, justification='left', key='-TABLE-',expand_y=True)]], key='-Column-',  visible=False,expand_y=True))],
            [sg.Button("AVANTI", key='AVANTI', visible = True, disabled=True, expand_y=True),sg.Button("ANNULLA", key='ANNULLA', visible = True, disabled=True,expand_y=True), sg.Text('',text_color='red', key='errore',expand_y=True)],
            [sg.Button("INSERISCI NUOVO", key='NUOVO', visible=False,expand_y=True)]
        ]

#crea la finestra dell'applicazione
window = sg.Window("GESTIONALE", layout,finalize=True)

pattern_email="[a-zA-Z0-9_.-]*@[a-zA-Z0-9]*[.][a-z]+"
pattern_dataNascita="^(0[1-9]|[12][0-9]|3[01])[-/.](0[1-9]|1[012])[-/.][0-9]{4}$"

entry = window['-INPUT-']
table = window['-TABLE-']



#in loop aspetta di ricevere un input
while True:
    event, values = window.read()

    if event in ('CERCA', '-INPUT-RETURN-'):
        text = values['-INPUT-']
        if text:
            index = None
            for i, item in enumerate(utenti):
                if text.lower() in item[0].lower() or text.lower() in item[1].lower() or text.lower() in item[2].lower():
                    index = i-1
                    break
            if index is not None:
                table.set_vscroll_position(index/len(utenti))
                table.update(select_rows=[index])

    if event == "vedi_utenti":
        with open('utenti.csv', 'r') as read_obj: # read csv file as a list of lists            
            csv_reader = csv.reader(read_obj)
            utenti = list(csv_reader)
            vediUtenti(utenti[1:])
            window.Element('AVANTI').Update(text= 'HOME')

    if event == "inserisci_utenti":
        window.Element('ANNULLA').Update(disabled= False)
        inserisciUtenti()

    if event == "AVANTI":

        if window['nome_text'].visible==False and window.Element('AVANTI').get_text()=="AVANTI":
            window.Element('nome_text').Update(visible = True)
            window.Element('nome_input').Update(visible = True)
            continue


        if window['cognome_text'].visible==False and window.Element('AVANTI').get_text()=="AVANTI":
            nome = values['nome_input']
            if not nome or not nome.strip():
                errore("nome");
                continue

            window.Element('errore').Update(value='')
            window.Element('nome_input').Update(disabled = True)
            window.Element('cognome_text').Update(visible = True)
            window.Element('cognome_input').Update(visible = True)
            continue
            

        if window['email_text'].visible==False and window.Element('AVANTI').get_text()=="AVANTI":   
            cognome = values['cognome_input']
            if not cognome or not cognome.strip():
                errore("cognome");
                continue

            window.Element('errore').Update(value='')
            window.Element('cognome_input').Update(disabled = True)
            window.Element('email_text').Update(visible = True)
            window.Element('email_input').Update(visible = True)
            continue


        if window['data_text'].visible==False and window.Element('AVANTI').get_text()=="AVANTI":   
            email = values['email_input']
            if not email or not email.strip() or not (bool(re.match(pattern_email, email))):
                errore("email");
                continue

            window.Element('errore').Update(value='')
            window.Element('email_input').Update(disabled = True)
            window.Element('data_text').Update(visible = True)
            window.Element('data_input').Update(visible = True)
            continue


        if window['data_text'].visible==True and window.Element('AVANTI').get_text()=="AVANTI":   
            data = values['data_input']
            if not data or not data.strip() or not (bool(re.match(pattern_dataNascita, data))):
                errore("data");
                continue

            formato = "%d/%m/%Y"
            dt_object = datetime.datetime.strptime(data, formato)
            if(dt_object.date() > datetime.datetime.now().date()):
                continue

            window.Element('errore').Update(value='')
            window.Element('data_input').Update(disabled = True)
            window.Element('AVANTI').Update(text='INSERISCI')
            window.Element('ANNULLA').Update(visible = True)

            continue

        
        if window.Element('AVANTI').get_text()=="HOME":
            window.Element('AVANTI').Update(text= 'AVANTI')
            window.Element('ANNULLA').Update(visible = True)
            window.Element('-Column-').Update(visible = False)
            window.Element('-INPUT-').Update(visible = False)
            window.Element('CERCA').Update(visible = False)
            tornaAHomepage()
            continue
            

        if window.Element('AVANTI').get_text()=="INSERISCI":
            utente=[values['nome_input'], values['cognome_input'], values['email_input'], values['data_input']]

            salvaInCSV()

            window.Element('errore').Update(value='utente salvato!')
            window.Element('ANNULLA').Update(disabled= True)
            window.Element('AVANTI').Update(text= 'HOME')

    if event == "ANNULLA":
        window.Element('AVANTI').Update(text='AVANTI')
        window.Element('AVANTI').Update(disabled= True)
        window.Element('ANNULLA').Update(disabled= True)
        tornaAHomepage();

    if event == "NUOVO":
        utente=[values['nome_input'], values['cognome_input'], values['email_input'], values['data_input']]
        utenti.append(utente)

    if event == sg.WIN_CLOSED:
        break




window.close()

