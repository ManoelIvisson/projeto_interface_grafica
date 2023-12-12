from guizero import App, Text, TextBox, PushButton, Window
import persistencia


def validar_usuario():
    try:
        with open("usuarios.txt", 'r', encoding="utf-8") as arquivo:
            for linha in arquivo.readlines():
                usuario_do_arquivo = linha.split()[0]
                senha_do_arquivo = linha.split()[1]

                if nomeUsuario.value == usuario_do_arquivo and senha.value == senha_do_arquivo:
                    mensagemDeAcesso.value = "Acesso Permitido!"
                    mensagemDeAcesso.text_color = "green"
                    app.hide()
                    janela.show()
                else:
                    mensagemDeAcesso.value = "Acesso Negado!"
                    mensagemDeAcesso.text_color = "red"
    except FileNotFoundError:
        print("Arquivo não encontrado")


def verificar_tecla(tecla_pressionada):
    if tecla_pressionada.keycode == 13:
        validar_usuario()


def fechar_aplicacao():
    app.destroy()


def teste_de_cadastro():
    persistencia.cadastrar_usuario("Robert", 321)


app = App(title="Tela de Login", layout="grid", width=220, height=150)
Text(app, text="Usuário: ", grid=[0, 0])
nomeUsuario = TextBox(app, grid=[1, 0], width=20)
Text(app, text="Senha: ", grid=[0, 1])
senha = TextBox(app, grid=[1, 1], width=20)
Text(app, text="", grid=[0, 2])

nomeUsuario.when_key_pressed = verificar_tecla
senha.when_key_pressed = verificar_tecla

botaoEnviar = PushButton(app, text="Enviar", command=validar_usuario, grid=[0, 3])
botaoCadastrar = PushButton(app, text="Cadastrar usuário", command=teste_de_cadastro, grid=[1, 3])
botaoCancelar = PushButton(app, text="Cancelar", command=fechar_aplicacao, grid=[2, 3], align="left")
mensagemDeAcesso = Text(app, text="", grid=[1, 4], align="left")

janela = Window(app, title="Tela Principal", visible=False)
Text(janela, text="Bem vindo a Tela principal")
janela.when_closed = fechar_aplicacao

app.display()
