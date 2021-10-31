import PySimpleGUI as sg
import re
import datetime


def errore(campo):
    stringa = "campo " + campo + " non valido"
    window.Element('errore').Update(value=stringa)


sg.theme('Reddit')

layout = [
            [sg.Text("Inserisci i tuoi dati")],
            [sg.Text('Nome', size =(15, 1), key='nome_text', visible = False)],
            [sg.InputText(key='nome_input',visible = False)],
            [sg.Text('Cognome', size =(15, 1), visible = False, key='cognome_text')],
            [sg.InputText(key='cognome_input', visible = False)],
            [sg.Text('Email', size =(15, 1), visible = False, key='email_text')],
            [sg.InputText(key='email_input', visible = False)],
            [sg.Text('Data di nascita (gg/mm/aa)', size =(30, 1), visible = False, key='data_text')],
            [sg.InputText(key='data_input', visible = False)],
            [sg.Button("AVANTI", key='AVANTI'), sg.Text('',text_color='red', key='errore')],
            [sg.Button("INSERISCI NUOVO", key='NUOVO', visible=False)]
        ]

# Create the window
window = sg.Window("Form di contatto", layout)
pattern_email="[a-zA-Z0-9_.-]*@[a-zA-Z0-9]*[.][a-z]+"
pattern_dataNascita="^(0[1-9]|[12][0-9]|3[01])[-/.](0[1-9]|1[012])[-/.][0-9]{4}$"


# Create an event loop
while True:
    event, values = window.read()


    if event == "AVANTI":
        if window['nome_text'].visible==False:
            window.Element('nome_text').Update(visible = True)
            window.Element('nome_input').Update(visible = True)
            continue


        if window['cognome_text'].visible==False:
            nome = values['nome_input']
            if not nome or not nome.strip():
                errore("nome");
                continue

            window.Element('errore').Update(value='')
            window.Element('nome_input').Update(disabled = True)
            window.Element('cognome_text').Update(visible = True)
            window.Element('cognome_input').Update(visible = True)
            continue
            


        if window['email_text'].visible==False:   
            cognome = values['cognome_input']
            if not cognome or not cognome.strip():
                errore("cognome");
                continue

            window.Element('errore').Update(value='')
            window.Element('cognome_input').Update(disabled = True)
            window.Element('email_text').Update(visible = True)
            window.Element('email_input').Update(visible = True)
            continue



        if window['data_text'].visible==False:   
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
            window.Element('AVANTI').Update(text='RIEPILOGO UTENTI')
            window.Element('NUOVO').Update(visible = True)

            continue
            

    if event == "AVANTI" and window.Element('AVANTI').get_text()=="RIEPILOGO UTENTI":
        print ("da qui andrai su schermata riepilogativa")


    if event == "NUOVO":
        print ("da qui inserirai nuovi utenti")




    if event == sg.WIN_CLOSED:
        break





window.close()

