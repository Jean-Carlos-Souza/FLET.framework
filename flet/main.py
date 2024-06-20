import flet as ft



#sempre recomendado fazer esse def
def main(pag: ft.Page):

#modularização da pagina/app

    #titulo do app
    pag.title = 'Contador'

    #alinhamendo vertical do centro
    pag.vertical_alignment = ft.MainAxisAlignment.CENTER


    def diminuir(evento):
        caixa_de_texto.value = str(int(caixa_de_texto.value) - 1)
        pag.update()

    def somar(evento):
        caixa_de_texto.value = str(int(caixa_de_texto.value) + 1)
        pag.update()


    
#criação de funções/itens ex: botão
    botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=diminuir)
    caixa_de_texto = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER)
    botao_mais = ft.IconButton(ft.icons.ADD, on_click=somar)



#adicionar os itens na pagina
    pag.add(
        ft.Row(
            [botao_menos,
             caixa_de_texto,
             botao_mais], alignment=ft.MainAxisAlignment.CENTER
        )
    )



#target = = = definir qual a pagina a ser exibida
#view = = = modo de exibição que deseja
#ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main, view=ft.WEB_BROWSER)

