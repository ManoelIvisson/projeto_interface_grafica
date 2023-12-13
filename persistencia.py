from Usuario import Usuario
import pickle


def serializar_lista_de_usuarios(lista_de_usuarios):
    with open("usuarios.pickle", "rb+") as arquivo:
        pickle.dump(lista_de_usuarios, arquivo)


def listar_usuarios_cadastrados():
    try:
        lista_de_usuarios = []
        with open("usuarios.pickle", "rb") as arquivo:
            if len(arquivo.readlines()) > 0:
                arquivo.seek(0)
                lista_de_usuarios = pickle.load(arquivo)
        return lista_de_usuarios
    except FileNotFoundError:
        print("Arquivo não foi encontrado")


def gerar_codigo_unico(lista_de_usuarios):
    try:
        ultimo_codigo_cadastrado = lista_de_usuarios[-1].Codigo
    except IndexError:
        ultimo_codigo_cadastrado = 0
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
        novo_usuario.Codigo = gerar_codigo_unico(lista_de_usuarios)
        lista_de_usuarios.append(novo_usuario)
        serializar_lista_de_usuarios(lista_de_usuarios)
        return True
    else:
        return False


def buscar_usuario(pesquisa):
    lista_de_usuarios = listar_usuarios_cadastrados()
    for usuario in lista_de_usuarios:
        if pesquisa == usuario.Nome or pesquisa == str(usuario.Codigo):
            return usuario
    return None


def excluir_usuario(codigo):
    try:
        codigo = int(codigo)
        lista_de_usuarios = listar_usuarios_cadastrados()
        for usuario in lista_de_usuarios:
            if codigo == usuario.Codigo:
                lista_de_usuarios.remove(usuario)
                serializar_lista_de_usuarios(lista_de_usuarios)
                return True
    except ValueError:
        print("Valor do código inválido")
    return False


def validar_usuario(nome, senha):
    lista_de_usuarios = listar_usuarios_cadastrados()
    for usuario in lista_de_usuarios:
        if nome == usuario.Nome and senha == usuario.Senha:
            return True
    return False
