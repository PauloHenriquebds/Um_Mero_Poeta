import os
import shutil

def organizar_arquivos():
    pasta_nova = "./arquivos"
    if not os.path.exists(pasta_nova):
        os.makedirs

    arquivos = os.listdir(".")
    extensoes_ignoradas = ["py", "ipynb"]

    for arquivo in arquivos:
        if os.path.isfile(arquivo):
            nome_base, extensao = os.path.splitext(arquivo)
            extensao = extensao.lstrip(".")

        if extensao in extensoes_ignoradas:
            continue

        pasta_extensao = os.path.join(pasta_nova, extensao)
        if not os.path.exists(pasta_extensao):
            os.makedirs(pasta_extensao)

        caminho_antigo = os.path.join(".", arquivo)
        caminho_novo = os.path.join(pasta_extensao, arquivo)

        shutil.move(caminho_antigo, caminho_novo)

    print("Organização concluida")
