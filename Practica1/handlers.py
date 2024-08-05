def extraer(path):
    f = open(path, 'r')
    i=0
    for line in f:
        if i==0:   
            cont = line.split(',')
            print(cont)
        i+=1