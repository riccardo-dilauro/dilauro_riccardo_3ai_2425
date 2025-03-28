"""
Realizzare un'applicazione grafica per l'iscrizione al campionato di
fine anno.
L'app richiede: 
 NOME E COGNOME
 CLASSE DI APPARTENENZA
 MASCHIO / FEMMINA / Non dichiarato
 ANNO DI NASCITA

 PREFERENZE:
    CALCIO
    BASKET
    PING-PONG
    ATLETICA
 CONSOLE PREFERITA:
    PSX
    SWITCH
    XBOX
    (wii)
    
EFFETTUA GLI EVENTUALI CONTROLLI SUI DATI INSERITI 
E VISUALIZZA UN RIEPILOGO DELLE INFORMAZIONI COLLEZIONATE.

"""






import flet as ft

def main(page: ft.Page):
    page.title = "😊Counter😊"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    c1 = ft.Checkbox(label="XBOX", value=False)
    c2 = ft.Checkbox(label="PLAYSTATION", value=False)
    c3 = ft.Checkbox(label="WII", value=False)
    label1 = ft.Text("Scegli le tue console",size=30,color="indigo500",italic=False,bgcolor="black",)

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def b1_clicked(e):
        txt_number.value = "ciao!!!"
        page.update()
    def console_clicked(e):
        msg = F"Hai scelto: {c1.value}"
        if c1.value():
            msg += "Playstation"
        label1.value = msg
        page.update()
        
    page.add(
        ft.Row(
            [
                ft.TextButton(text="Premi qui"),
                ft.IconButton(ft.Icons.REMOVE, on_click=b1_clicked),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
                c1
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        ft.Row(
            [
                c1,c2,c3
                

            ]
        ),
        ft.Row(
            [
                ft.TextButton(
                    "Button with colorful icon",
                    icon="ADD_ALARM_ROUNDED",
                    icon_color="green400",
                ),
                label1
            ]
        )


    )

ft.app(main)