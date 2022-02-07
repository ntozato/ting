def exists_word(word, instance):
    line = 0
    ocurrencies = []
    result = []

    for item in instance.data:
        for row in item["linhas_do_arquivo"]:
            line += 1
            if word.lower() in row.lower():
                ocurrencies.append({"linha": line})
                result.append(
                    {
                        "palavra": word,
                        "arquivo": item["nome_do_arquivo"],
                        "ocorrencias": ocurrencies
                    }
                )

    return result


def search_by_word(word, instance):
    line = 0
    ocurrencies = []
    result = []

    for item in instance.data:
        for row in item["linhas_do_arquivo"]:
            line += 1
            if word.lower() in row.lower():
                ocurrencies.append(
                    {
                        "linha": line,
                        "conteudo": row
                    }
                )
                result.append(
                    {
                        "palavra": word,
                        "arquivo": item["nome_do_arquivo"],
                        "ocorrencias": ocurrencies
                    }
                )

    return result
