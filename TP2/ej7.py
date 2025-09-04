lista1 = [8, 1, 3]
lista2= [5, 9, 7]

def main():
   lista1[1::2] = lista2
   lista1[1::2].extend(lista2)
   
   print (lista1)   

if __name__ == "__main__":
    main()