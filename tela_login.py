from guizero import App, Text, TextBox, PushButton, Window, Picture, Box, info, warn, error
import persistencia


def validar_usuario():
    usuario_valido = persistencia.validar_usuario(nomeUsuario.value, senha.value)

    if usuario_valido:
        app.hide()
        janela.show()
    else:
        error("Atenção", "Acesso Negado, verifique o nome de usuario e a senha")


def verificar_tecla(tecla_pressionada):
    if tecla_pressionada.keycode == 13:
        validar_usuario()


def fechar_aplicacao():
    app.destroy()


def cadastro_de_usuario():
    cadastro_permitido = persistencia.cadastrar_usuario(nomeUsuario.value, senha.value)

    if cadastro_permitido:
        info("Sucesso", "Usuário cadastrado com sucesso")
    else:
        warn("Atenção", "Nome de usuário já existe ou possui espaços")


def listar_usuarios():
    for usuario in persistencia.listar_usuarios_cadastrados():
        print(f"Código: {usuario.Codigo}")
        print(f"Nome: {usuario.Nome}")
        print(f"Senha: {usuario.Senha}")


def buscar_usuario():
    usuario_pesquisado = persistencia.buscar_usuario(codigoBuscar.value)

    if usuario_pesquisado is not None:
        info("Informações do usuário", f"Código: {usuario_pesquisado.Codigo} | Login: {usuario_pesquisado.Nome}"
            f" | Senha: {usuario_pesquisado.Senha}")
    else:
        error("Aviso", "Este usuário não existe")


def excluir_usuario():
    remocao_permitida = persistencia.excluir_usuario(codigoExcluir.value)

    if remocao_permitida:
        info("Sucesso", "Usuário deletado com sucesso")
    else:
        warn("Atenção", "Usuário não encontrado")


app = App(title="Usuário lunático", layout="grid", width=1100, height=619)
app.tk.resizable(False, False)
picture = Picture(app, image="source/fundo login.png", grid=[0,0,4,4])

Login = Box (app, grid=[0,0], layout="")

Text(Login, text="Usuário 👦: ", font="Century Gothic", size=24)
nomeUsuario = TextBox(Login, width=30)

loginBotaoBox = Box(Login, layout="grid")

Text(Login, text="Senha 🔑: ", font="Century Gothic", size=24)
# senha = TextBox(app, grid=[1, 1], width=35)
senha = TextBox(Login, width=30, hide_text=True)
Text(Login, text="")

nomeUsuario.when_key_pressed = verificar_tecla
senha.when_key_pressed = verificar_tecla
listar_usuarios()

loginBotaoBox = Box(Login, layout="grid")

botaoEnviar = PushButton(loginBotaoBox, text="Enviar", command=validar_usuario, grid=[0, 0], width=10)
botaoEnviar.bg = "blue"
botaoEnviar.text_color = "white"
botaoEnviar.text_size = 10
Invisivel = Box(loginBotaoBox, grid=[1,0], height=15, width=15)
botaoCadastrar = PushButton(loginBotaoBox, text="Cadastrar usuário", command=cadastro_de_usuario, grid=[2,0], width=15)
botaoCadastrar.bg = "white"
botaoCadastrar.text_size = 10
#InvisivelCancelar = Box(loginBotaoBox, grid=[2,0], height=60)
botaoCancelar = PushButton(loginBotaoBox, text="Fechar", command=fechar_aplicacao, grid=[0, 3], align="left")
botaoCancelar.bg = "red"

ferramenta = Box(app, layout="grid", grid=[0,3])

ferramentaBusca = Box(ferramenta, grid=[0,0])
Text(ferramentaBusca, text="Busca por ID/Nome 👾: ", font="Century Gothic", size=20)
Text(ferramentaBusca, text="", font="Century Gothic", size=1)
codigoBuscar = TextBox(ferramentaBusca, width=30)
Text(ferramentaBusca, text="", font="Century Gothic", size=3)
botaoBuscarUsuario = PushButton(ferramentaBusca, text="🔍", command=buscar_usuario)
botaoBuscarUsuario.bg = "green"

ferramentaExcluir = Box(ferramenta, grid=[1,0])
Text(ferramentaExcluir, text="Excluir por ID 🗑: ", font="Century Gothic", size=20)
Text(ferramentaExcluir, text="", font="Century Gothic", size=1)
codigoExcluir = TextBox(ferramentaExcluir, width=30)
Text(ferramentaExcluir, text="", font="Century Gothic", size=3)
botaoExcluirUsuario = PushButton(ferramentaExcluir, text="❌", command=excluir_usuario)
botaoExcluirUsuario.text_color = "red"

mensagemDeAcesso = Text(app, text="", grid=[1, 4], align="left")

janela = Window(app, title="Tela Principal", visible=False)
Text(janela, text="Bem vindo a Tela principal")
janela.when_closed = fechar_aplicacao

app.display()
