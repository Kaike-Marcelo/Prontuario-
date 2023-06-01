import requests
import json


def lo() -> dict:
    dados = {
        "login": {
            "name": "Breno",
            "last_name": "Breno",
            "password": "padrao",
            "email": "breno@gmail.com",
            "doctor": 1,
            "admin": 1
        },

        "informacao": {
            "data_nascimento": "2018-12-10",
            "telefone": "12345678",
            "foto": "3fdkfjsdldgdsg",
            "cns": "374885995",
            "rg": "488599604",
            "sexo": "masculino",
            "endereco": "uma rua qualquer",
            "numero": "234",
            "cidade": "Eunapolis",
            "bairro": "nao sei",
            "estado": "bahia"
        },
        "doctor":{

        }

    }

    con = requests.post('http://127.0.0.1:8000/api/user/create',
                        data=json.dumps(dados), headers={'Content-type': 'application/json'})
    print(con)
 
#lo()


def lo_return():
        
    con = requests.get('http://127.0.0.1:8000/api/user/1')

    try:
        dados = json.loads(con.text)
        #print(dados)
        print(dados)

    except json.decoder.JSONDecodeError as err:
        # Tratar a exceção e exibir uma mensagem de erro personalizada
        print("Erro ao decodificar JSON:", err)


    # print(con.text)
    '''
    for usuario in dados:
        print(usuario)
        
        if usuario.get('id') == '1':
            print(f"ID: {usuario.get('id')} -> CPF: {usuario.get('cns')} -> Nome: {usuario.get('name')}")
            
        else:
            print("Lista de usuários não encontrada nos dados retornados.")
        
        # return json.loads(dados)
    '''


#lo_return()



def imprimir_um():
    response = requests.get('http://127.0.0.1:8000/api/user')

    # Verificar se a resposta foi bem-sucedida (código 200 indica sucesso)
    # Converter a resposta em um objeto JSON

     
    data = json.loads(response.text)

    # Iterar sobre os usuários e imprimir todos os dados
    for user in data:
        for key, value in user.items():
            print(key + ':', value)
        for key, value in user['information'].items():
            print(key + ':', value)
        print('---')



#imprimir_um()


def imprimir_tudo():

    #con = requests.get('http://127.0.0.1:8000/api/user/')
    #dados = json.loads(con.text)

    url = 'http://127.0.0.1:8000/api/user/'

    response = requests.get(url)
    #print(dados)
    #print(con.text)

    if response.status_code == 200:
        usuarios = response.json()  # Decodifica o JSON recebido em um objeto Python
        
        # Itera sobre os usuários e imprime suas informações
        for usuario in usuarios:
            print("ID:", usuario['id'])
            print("Nome:", usuario['nome'])
            print("Email:", usuario['email'])
            print()
    else:
        print("Erro ao obter os usuários do banco de dados.")
            print(response.status_code)

        
    '''
    for usuario in dados:
        print(usuario.get('id'))
    '''
imprimir_tudo()



def atualizar_dados():

    # Dados a serem atualizados
    dados = {
        
        "email": "aelson@email.com",

    }

    # Enviar solicitação PUT ou PATCH
    response = requests.post('http://127.0.0.1:8000/api/user/update/1', json=dados, headers={'Content-type': 'application/json'})
    print(response.status_code)

    if response.status_code == 200:
        print('Dados atualizados com sucesso!')
        lo_return()
    else:
        print('Falha ao atualizar os dados.')
        print('Resposta do servidor:', response.text)

    #return response.json()

#dados_atualizados = atualizar_dados()