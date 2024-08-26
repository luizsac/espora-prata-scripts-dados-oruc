"""
Praticamente o mesmo módulo uploadImagensPCV, mas duplicado para agilizar o processo

Realiza o upload de imagens para produtos da loja que não contenham variações de modelos.
PSV = Produtos Sem Variação
Ao selecionar um diretório raiz, o módulo varre todas as pastas contidas nele, seleciona
as imagens de cada pasta, converte-as para base64 e realiza o upload das mesmas para seus
respectivos modelos.
As pastas devem ser nomeadas com o código do produto na plataforma
"""

from base64 import b64encode
from os import path, walk, getenv, rename
from requests import post


def encode_image_to_base64(image_path: str) -> str:
    """
    Converte uma imagem para base64.

        :param image_path: O caminho para uma imagem

        :return: String da imagem convertida para base64
    """
    with open(image_path, "rb") as image_file:
        encoded_string = b64encode(image_file.read())
    return encoded_string.decode('utf-8')


def upload_images(code: str, image_list: list[str]) -> bool:
    """
    Realiza o post/upload das imagens convertidas para a loja na plataforma ORUC

        :param code: O código do produto na plataforma
        :param image_list: lista de imagens em base64

        :return: bool
    """

    # caminho para upload de imagens na API
    url = "https://www.meudatacenter.com/api/v1/imagem"

    # pega o id da loja e o token de acesso nas variáveis de ambiente e as atribui a variáveis
    store_id: str = getenv('store_id')
    token: str = getenv('token')

    # headers da requisição
    headers = {
        "x-ID": store_id,
        "x-Token": token,
        "Content-Type": "application/json"
    }

    # dicionário com os dados de upload da imagem - json
    data = {
        "codigo": code,
        "nome_modelo": "",
        "modo": "substituicao_retangular",
        "imagens": image_list
    }

    # faz request e recebe response
    response = post(url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        print(f"Upload de imagens do produto {code} bem-sucedido!")
        print("Resposta do servidor:", response.json())
        return True
    else:
        print(f"Falha no upload de imagens do produto {code}. Status code:", response.status_code)
        print("Resposta do servidor:", response.text)
        return False


# caminho do diretório raiz contendo as pastas dos modelos com suas imagens
root_dir = "../../../Downloads/produto-img"

# percorre todas as pastas do diretório raiz e insere seus caminhos em uma lista
for root, directories, files in walk(root_dir):
    for dir_name in directories:
        if dir_name[-4:] == "done":
            print(f"{dir_name} ignorado")
            continue
        dir_path = path.join(root, dir_name)
        prod_image_list = []
        # print(dir_path)

        # percorre todas as imagens da pasta do modelo e insere seus caminhos em uma lista
        for sub_root, sub_directories, images in walk(dir_path):
            for image in images:
                prod_image_path = path.join(sub_root, image)
                prod_image_list.append(encode_image_to_base64(prod_image_path))
                # print(prod_image_path)

        if upload_images(dir_name, prod_image_list):
            rename(dir_path, f"{dir_path}-done")
