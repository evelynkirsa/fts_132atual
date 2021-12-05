# bibliotecas
import pytest
import requests

# Endereço de API
url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # No .asmr seria 'text/xml


# O teste
def testar_criar_usuario():
    # Configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '4689'

    # Executa
    resposta = requests.post(  # Faz a requisição, passando:
        url=url,  # O endpoint da API
        data=open('C:/Users/User/PycharmProjects/FTS132/test/db/user1.json', 'rb'),  # O body JSON
        headers=headers  # O header com o Content-Type
    )

    # formatação
    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # status code
    print(corpo_da_resposta)  # respostas formatada

    # valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_consultar_usuario():
    #configura
    status_code = 200
    id = 4689
    username = 'mer'
    firstName = 'meredith'
    lastName = 'grey'
    email = 'meredith.grey@teste.com.br'
    password = 'lalala'
    phone = '11999999999'
    userStatus = 0

    #Executa
    resposta = requests.get(
        url=f'{url}/{username}',
        headers=headers
    )
    # formatação
    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # status code
    print(corpo_da_resposta)  # respostas formatada

    #valida
    assert  resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone

def testar_alterar_usuario():
    username = 'mer'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '4689'

    #executa
    resposta = requests.put(
        url=f'{url}/{username}',
        data=open('C:/Users/User/PycharmProjects/FTS132/test/db/user2.json', 'rb'),
        headers=headers
    )
    #formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    #Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_excluir_usuario():
    #configura
    username = 'mer'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'mer'

    #executa
    resposta = requests.delete(
        url=f'{url}/{username}',
        headers=headers

    )
    # formatação
    match resposta.status_code:
        case 200:                       #Apagar um usuario que foi encontrado
            corpo_da_resposta = resposta.json()
            print(resposta)
            print(resposta.status_code)
            print(corpo_da_resposta)

            # Valida
            assert resposta.status_code == status_code_esperado
            assert corpo_da_resposta['code'] == codigo_esperado
            assert corpo_da_resposta['type'] == tipo_esperado
            assert corpo_da_resposta['message'] == mensagem_esperada
        case 400:
            print('Username fornecido incorretamente')
        case 404:
            print('usuario não encontrado')

def testar_login_do_usuario():
    username = 'mer'
    password = 'lelele'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    inicio_mensagem_esperada = 'logged in user session:'

    #executa
    resposta = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers
    )
    #formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    #Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'].find(inicio_mensagem_esperada) != -1

    frase = 'Neste fim de ano planeje seu sucesso'
    assert frase.find('sucesso') != -1

    #Extrair
    # Na mensagem "logged in user session:1638120238950" queremos pegar os numeros
    mensagem_recebida = token_usuario = corpo_da_resposta['message']
    print(f' A mensagem recebida é:{mensagem_recebida}')
    token_usuario = mensagem_recebida[23:37]
    print(f'O token do usuario é: {token_usuario}')

    #exemplo
    frase = 'Saldo: R$1.987,65'
    valor = frase[8:17]
    print(f' O valor é: {valor}')

def testar_sequencia_de_testes():
    testar_criar_usuario()
    testar_login_do_usuario()
    testar_alterar_usuario()
    testar_consultar_usuario()
    testar_excluir_usuario()

