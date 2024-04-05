def slice_simple():
    texto = "Awesome"
    print(texto[:3:1].lower())
    print(texto[2:5:1].lower())
    print(texto[:4].lower()+texto[-3:].lower())
