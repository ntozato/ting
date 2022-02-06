import sys


# referências
# https://www.hashtagtreinamentos.com/trabalhar-com-arquivos-de-texto-python
# https://codare.aurelio.net/2007/01/30/python-imprimir-mensagens-de-erro-stderr/

def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, "r", encoding="utf-8") as file:
            text = file.readlines()

            data = [row.strip('\n') for row in text]
            return data
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

# teste = txt_importer("statics/arquivo_teste.txt")
# print(teste)
