import flet as ft

def main(pag: ft.Page):
    pag.title = 'LoginPage'

    pag.vertical_alignment = ft.MainAxisAlignment.CENTER

    caixa_login = ft.TextField(value='login', text_align=ft.TextAlign.CENTER)
    caixa_senha = ft.TextField(value='senha',  text_align=ft.TextAlign.CENTER)


    pag.add(
        ft.Row(
            caixa_login, alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            caixa_senha,alignment=ft.MainAxisAlignment.CENTER
        )
    )


    
    
    
    
    
ft.app(target=main)
