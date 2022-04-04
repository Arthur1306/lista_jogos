import json

def ler_txt_jogo():
    with open("jogo.txt", "r") as file:
        json_data = file.readlines()[0].replace("'", '"')
        data = json.loads(json_data)
    return data


def adicionar_jogo(jogo, tamanho):
    data = ler_txt_jogo()
    if jogo not in data:
        data[jogo] = tamanho
        with open("jogo.txt", 'w') as file:
            file.write(str(data))
    else:
        raise ValueError("Jogo já existe, não será sobreescrito")

def remover_jogo(jogo, data):
    del data[jogo]
    with open("jogo.txt", 'w') as file:
        file.write(str(data))
    return data

def somar_tamanho_jogo():
    data = ler_txt_jogo()
    valores = list(data.values())
    total = sum(list(map(lambda x: float(x), valores)))
    return total

def listar_jogos():
    data = ler_txt_jogo()
    jogos = list(data.keys())
    print("="*50)
    for i, jogo in enumerate(jogos):
        i+=1
        print(f"{i}. {jogo} \n")
    return jogos

escolha_resposta = input('''O que deseja fazer?: 
[1] Inserir novo jogo
[2] Listar jogos
[3] Excluir jogo
''')

if escolha_resposta == '1':
    resposta_jogo = input("Nome do Jogo: ")
    resposta_tamanho = input("Tamanho Do Jogo em GB: ")
    adicionar_jogo(resposta_jogo, resposta_tamanho)
    somartudo = input("Deseja somar o tamanho total dos jogos?: ")
    somartudo.lower()
    if somartudo[0] == 's': ## aqui quando fazemos somartudo[0] estamos pegando a primeira letra da string, é so verificar se ela é o S de sim
        print(somar_tamanho_jogo())
 ## Não precisa de um else aqui, já que se não foi sim a resposta não vai retornar nada
elif escolha_resposta == '2':
        listar_jogos()
elif escolha_resposta == '3':
    listar_jogos()
    resposta_excluir = input("Qual deseja excluir?: ")
    data = ler_txt_jogo()
    data = remover_jogo(resposta_excluir, data) ## Fiz um funcao de remover o jogo que já atualiza o arquivo txt
    listar_jogos()
else:
    print("Até mais...") ## não existe exit no python em if, só um print de saida já ta otimo, pra sua função pass seria o ideal