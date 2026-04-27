def duplicado(lista):

    primeiro_duplicado = []
    
    for i in range(len(lista)):
        underset = set()
        is_duplique = False
        
        for j in range(len(lista[i])):


            if lista[i][j] in underset:
                primeiro_duplicado.append(lista[i][j])
                is_duplique = True
                break
              
            underset.add(lista[i][j])
            
        if not is_duplique:
            primeiro_duplicado.append(-1)
            
    return primeiro_duplicado


lista = [[1, 1, 2], [3, 3, 2], [1, 2, 3]]
print(duplicado(lista))
#