from guizero import App, Text, TextBox, PushButton, Window
import persistencia


def validar_usuario():
    usuario_valido = persistencia.validar_usuario(nomeUsuario.value, senha.value)

    if usuario_valido:
        mensagemDeAcesso.value = "Acesso Permitido!"
        mensagemDeAcesso.text_color = "green"
        app.hide()
        janela.show()
    else:
        mensagemDeAcesso.value = "Acesso Negado!"
        mensagemDeAcesso.text_color = "red"


def verificar_tecla(tecla_pressionada):
    if tecla_pressionada.keycode == 13:
        validar_usuario()


def fechar_aplicacao():
    app.destroy()


def teste_de_cadastro():
    persistencia.cadastrar_usuario(nomeUsuario.value, senha.value)


def teste_listar_usuarios():
    for usuario in persistencia.listar_usuarios_cadastrados():
        print(f"Código: {usuario.Codigo}")
        print(f"Nome: {usuario.Nome}")
        print(f"Senha: {usuario.Senha}")


def teste_buscar_usuario():
    usuario_pesquisado = persistencia.buscar_usuario(nomeUsuario.value)

    if usuario_pesquisado is not None:
        print(usuario_pesquisado.Codigo)
        print(usuario_pesquisado.Nome)
        print(usuario_pesquisado.Senha)


def teste_excluir_usuario():
    persistencia.excluir_usuario(nomeUsuario.value)


app = App(title="Tela de Login", layout="grid", width=500, height=150)
Text(app, text="Usuário: ", grid=[0, 0])
nomeUsuario = TextBox(app, grid=[1, 0], width=20)
Text(app, text="Senha: ", grid=[0, 1])
senha = TextBox(app, grid=[1, 1], width=20)
Text(app, text="", grid=[0, 2])

nomeUsuario.when_key_pressed = verificar_tecla
senha.when_key_pressed = verificar_tecla
teste_listar_usuarios()
botaoEnviar = PushButton(app, text="Enviar", command=validar_usuario, grid=[0, 3])
botaoCadastrar = PushButton(app, text="Cadastrar usuário", command=teste_de_cadastro, grid=[1, 3])
botaoBuscarUsuario = PushButton(app, text="Buscar usuário", command=teste_buscar_usuario, grid=[2, 3])
botaoExcluirUsuario = PushButton(app, text="Excluir usuário", command=teste_excluir_usuario, grid=[3, 3])

botaoCancelar = PushButton(app, text="Cancelar", command=fechar_aplicacao, grid=[4, 3], align="left")
mensagemDeAcesso = Text(app, text="", grid=[1, 4], align="left")

janela = Window(app, title="Tela Principal", visible=False)
Text(janela, text="Bem vindo a Tela principal")
janela.when_closed = fechar_aplicacao

app.display()
