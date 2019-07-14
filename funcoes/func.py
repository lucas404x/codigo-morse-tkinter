import json

def criptografar(palavra):

    with open('/Users/Lucas/Documents/Python Scripts/codigo morse/funcoes/alfabeto_morse.json') as file:
        alfabeto = json.loads(file.read())
        nova_palavra = []

        for letra in palavra:
            try:
                nova_palavra.append(f'{alfabeto[letra.upper()]} ')
            except:
                if letra == " ":
                    nova_palavra.append(' / ')
        
        return nova_palavra

def descriptografar(palavra):

    with open('/Users/Lucas/Documents/Python Scripts/codigo morse/funcoes/alfabeto_morse.json') as file:
        alfabeto = json.loads(file.read())
        nova_palavra = []

        for letra in palavra:

            for k, v in alfabeto.items():
                
                if v == letra:
                    nova_palavra.append(f'{k}')
                    break

                elif letra == "/":
                	nova_palavra.append(" ")
                	break
        
        return nova_palavra

if __name__ == "__main__":
    print(criptografar("Ola mundo"))
    print(descriptografar(criptografar("Ola mundo")))