import pickle, Usuario


def serializar_lista_de_usuarios(lista_de_usuarios):
    with open("usuarios.pickle", "wb+", encoding="utf-8") as arquivo:
        pickle.dump(lista_de_usuarios, arquivo)


def listar_usuarios_cadastrados():
    try:
        with open("usuarios.pickle", "rb") as arquivo:
            lista_de_usuarios = pickle.load(arquivo)
            return lista_de_usuarios
    except FileNotFoundError:
        print("Arquivo não foi encontrado")


def gerar_codigo_unico():
    lista_de_usuarios = listar_usuarios_cadastrados()
    ultimo_codigo_cadastrado = lista_de_usuarios[-1].Codigo
    novo_codigo = ultimo_codigo_cadastrado + 1
    return novo_codigo


def cadastrar_usuario(nome, senha):
    lista_de_usuarios = listar_usuarios_cadastrados()
    cadastro_permitido = True
    for usuario in lista_de_usuarios:
        if nome == usuario.Nome or len(nome.split()) > 1:
            cadastro_permitido = False

    if cadastro_permitido:
        novo_usuario = Usuario(nome, senha)
        novo_usuario.Codigo = gerar_codigo_unico()
        lista_de_usuarios.append(novo_usuario)
        serializar_lista_de_usuarios(lista_de_usuarios)
    else:
        print("Nome de usuário já existe ou possui espaços")