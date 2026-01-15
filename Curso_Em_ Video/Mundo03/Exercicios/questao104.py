def notas(*notas, sit=False):
    """
    deve passar sit= para ativar a situacao de como esta as notas

    """
    dic = dict()
    media = sum(notas) / len(notas)

    dic["Total"] = len(notas)
    dic["Maior nota"] = max(notas)
    dic["Menor nota"] = min(notas)
    if sit:
        if media == 6:
            dic["Situacao"] = "MEDIA"
        elif media >= 7:
            dic["Situacao"] = "BOM"
        else:
            dic["Situacao"] = "RUIM"

    return dic


print(notas(1.5, sit=True))
