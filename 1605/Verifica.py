import flet as ft

#SUPERVISED USED CIRCLE

def main (page: ft.Page):


    #Dati

    listanomi = []

    #Controlli

    def Inizia_premuto(e):
        nome = Inserimento1.value
        nome = nome.lower()
        nome = nome.replace(" ","")
        if nome not in listanomi:
            if len(nome) > 3:
                if nome.isnumeric() == False:
                    print("Done!")
                    listanomi.append(nome)
                    print(listanomi)
                    return
                else:
                    print("Il nome contiene numeri.")
            else:
                print("Nome troppo corto")
        else:
            print("Nome già presente")
        page.update()
    
    #Preliminari

    page.title = "Sondaggio"
    page.theme_mode = "LIGHT"
    page.scroll = "AUTO"

    #Testo

    Titolo1 = ft.Text("Prima parte", size = 30, weight=ft.FontWeight.BOLD)
    Testo1 = ft.Text("Verifica che il nome dell'intervistato non sia già utilizzato.", size=20 ,italic= True)

    Inserimento1 = ft.TextField(label="Nome Intervistato",)
    

    Titolo2 = ft.Text("Seconda parte", size = 30, weight=ft.FontWeight.BOLD)
    Titolo2.padding = ft.padding.all(10)
    Testo2 = ft.Text("Accoda le preferenze nel file sondaggio.txt", size = 20, italic=True)
    Sottotitolo1 = ft.Text("Sistemi di gioco a disposizione", size= 15)
    Sottotitolo2 = ft.Text("Tipologia di gioco preferita", size = 15)

    #Checkbox 

    Check1 = ft.Checkbox(label="Xbox", label_position=ft.LabelPosition.RIGHT)
    Check2 = ft.Checkbox(label="Psx", label_position=ft.LabelPosition.RIGHT)
    Check3 = ft.Checkbox(label="Switch", label_position=ft.LabelPosition.RIGHT)
    Check4 = ft.Checkbox(label="Pc", label_position=ft.LabelPosition.RIGHT)
    Check5 = ft.Checkbox(label="Android/Ios", label_position=ft.LabelPosition.RIGHT)

    #Radio

    InsiemeRadio = ft.RadioGroup(content=ft.Column([
    
                       ft.Radio(value="Nessuna", label="Nessuna"),
                       ft.Radio(value="Sport", label="Sport"),
                       ft.Radio(value="Platform", label="Platform"),
                       ft.Radio(value="Rpg", label="Rpg"),
                       ft.Radio(value="Fps", label="Fps"),
                                                    ])
    )

    #Dropdown


    InsiemeAnni = ft.DropdownM2(label= "Quale anno frequenti?", options = [
        ft.dropdownm2.Option("Prima"), 
        ft.dropdownm2.Option("Seconda"),
        ft.dropdownm2.Option("Terza"),
        ft.dropdownm2.Option("Quarta"),
        ft.dropdownm2.Option("Quinta"),
    ])
    
    #Bottoni

    Inizia = ft.FilledButton(text="Inizia", icon=ft.icons.SEARCH, on_click=Inizia_premuto)

    Conferma = ft.FilledButton(text="Conferma", icon=ft.icons.CHECK)

    #Switch

    Switch1 = ft.Switch(label="Acconsento all'invio delle promozioni pubblicitarie")

    #Icon

    Icona = ft.Icon(name=ft.icons.SUPERVISED_USER_CIRCLE)

    #Funzionamento programma


    #Aggiunta alla pagina
    
    page.add(

        #Prima Parte

        Titolo1,
        Testo1,
        Icona,
        Inserimento1,
        Inizia,
        ft.Divider(),
        #Seconda Parte

        Titolo2,
        Testo2,
        #Sezione Checkbox

        Sottotitolo1,
        Check1,
        Check2,
        Check3,
        Check4,
        Check5,

        #Sezione radiobuttom

        Sottotitolo2,
        InsiemeRadio,
        ft.Divider(),

        #Sezione dropdown

        InsiemeAnni,

        #Sezione Switch

        Switch1,

        #Sezione Bottone finale

        Conferma

    )
    print(Inserimento1)


ft.app(main)