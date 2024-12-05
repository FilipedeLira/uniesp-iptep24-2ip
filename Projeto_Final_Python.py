import requests
from deep_translator import GoogleTranslator


def obter_conselho():
    response = requests.get("https://api.adviceslip.com/advice")
    if response.status_code == 200:
        advice = response.json()["slip"]
        return advice["id"], advice["advice"]
    else:
        return None, "Erro ao acessar a API."


def salvar_conselho_em_arquivo(lista_conselhos, nome_arquivo="conselhos.txt"):
    with open(nome_arquivo, "a", encoding="utf-8") as file:
        for id_conselho, conselho in lista_conselhos:
            file.write(f"{id_conselho} | {conselho}\n")


def ler_conselhos_salvos(nome_arquivo="conselhos.txt"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def traduzir_texto(texto, idioma_destino="pt"):
    tradutor = GoogleTranslator(source="auto", target=idioma_destino)
    return tradutor.translate(texto)


def salvar_conselhos_traduzidos(conselho, nome_arquivo="conselhos_traduzidos.txt"):
    with open(nome_arquivo, "a", encoding="utf-8") as file:
        file.write(conselho + "\n")


def ler_conselhos_traduzidos(nome_arquivo="conselhos_traduzidos.txt"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def menu_principal():
    while True:
        print("\nMenu do Seu Zé:")
        print("1. Ouvir o Seu Zé (Receber conselhos traduzidos)")
        print("2. Mostrar os Conselhos (em português)")
        print("3. Guardar a Sabedoria (Salvar conselhos)")
        print("4. Traduzir conselhos salvos para outro idioma")
        print("5. Mostrar conselhos traduzidos")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            quantidade = int(input("Quantos conselhos deseja receber? "))
            conselhos = [obter_conselho() for _ in range(quantidade)]
            conselhos_traduzidos = []
            for i, (id_conselho, conselho) in enumerate(conselhos, 1):
                if id_conselho is not None:  # Verifica se o conselho foi obtido com sucesso
                    conselho_traduzido = traduzir_texto(conselho, idioma_destino="pt")
                    print(f"\nConselho {i} (ID: {id_conselho}): {conselho_traduzido}")
                    conselhos_traduzidos.append((id_conselho, conselho_traduzido))
                else:
                    print(f"\nConselho {i}: Erro ao buscar o conselho.")
            salvar_conselho_em_arquivo(conselhos_traduzidos)
        
        elif escolha == "2":
            conselhos = ler_conselhos_salvos()
            if conselhos:
                print("\nConselhos em português:")
                for conselho in conselhos:
                    print(conselho.strip().split("|")[1])  # Exibe apenas a parte traduzida
            else:
                print("Nenhum conselho salvo ainda!")
        
        elif escolha == "3":
            quantidade = int(input("Quantos conselhos deseja salvar? "))
            conselhos = [obter_conselho() for _ in range(quantidade)]
            conselhos_traduzidos = [(id_conselho, traduzir_texto(conselho, idioma_destino="pt")) for id_conselho, conselho in conselhos if id_conselho is not None]
            salvar_conselho_em_arquivo(conselhos_traduzidos)
            print("Conselhos traduzidos e salvos com sucesso!")
        
        elif escolha == "4":
            conselhos = ler_conselhos_salvos()
            if conselhos:
                print("\nConselhos salvos:")
                for i, conselho in enumerate(conselhos, 1):
                    print(f"{i}. {conselho.strip()}")
                idx = int(input("Escolha o número do conselho para traduzir: ")) - 1
                if 0 <= idx < len(conselhos):
                    original = conselhos[idx].split("|")[1].strip()
                    idioma_destino = input("Para qual idioma deseja traduzir? (Ex: en, es, fr): ")
                    traduzido = traduzir_texto(original, idioma_destino=idioma_destino)
                    print(f"\nConselho original: {original}")
                    print(f"Conselho traduzido ({idioma_destino}): {traduzido}")
                    salvar_conselhos_traduzidos(f"{original} -> {traduzido} ({idioma_destino})")
                else:
                    print("Opção inválida!")
            else:
                print("Nenhum conselho salvo ainda!")
        
        elif escolha == "5":
            traducoes = ler_conselhos_traduzidos()
            if traducoes:
                print("\nConselhos traduzidos na opção 4:")
                for traducao in traducoes:
                    print(traducao.strip())
            else:
                print("Nenhuma tradução realizada ainda!")
        
        elif escolha == "0":
            print("Até logo, Seu Zé!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
