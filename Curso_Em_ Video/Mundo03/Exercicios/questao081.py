expresao = []


ex = str(input("digite uma expresao: "))
for i in ex:
    if "(" in i:
        expresao.append(i)
    elif ")" in i:
        if len(expresao) > 0:
            expresao.pop()
        else:
            expresao.append(i)
            break
    else:
        continue
if len(expresao) == 0:
    print("valida")
else:
    print("invalida")
