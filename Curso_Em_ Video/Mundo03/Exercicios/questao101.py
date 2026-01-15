import datetime


def voto(ano):
    ano = datetime.date.today().year - ano

    if ano >= 18 and ano <= 65:
        return f"vc tem {ano} e ainda e obrigado a votar"
    elif ano < 16:
        return f"vc tem {ano} e ainda n pode votar"
    else:
        return f"vc tem {ano} e e opcional votar"


ano = int(input("Digite sua idade: "))
print(voto(ano))
