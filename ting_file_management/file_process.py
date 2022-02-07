from ting_file_management.file_management import txt_importer
import sys


# https://www.geeksforgeeks.org/sys-stdout-write-in-python/
def process(path_file, instance):
    content = txt_importer(path_file)

    res = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
    }

    for item in instance.data:
        if item["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(res)
    sys.stdout.write(str(res))


def remove(instance):
    if len(instance.data) == 0:
        return sys.stdout.write("Não há elementos\n")

    path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):

    try:
        item = instance.search(position)
        sys.stdout.write(str(item))

    except IndexError:
        sys.stderr.write("Posição inválida")
