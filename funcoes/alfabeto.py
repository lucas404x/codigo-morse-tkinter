from bs4 import BeautifulSoup
import requests, json

site = requests.get('https://pt.wikipedia.org/wiki/C%C3%B3digo_Morse')
soup = BeautifulSoup(site.text, features='html.parser')
soup = soup.find(attrs={'class':'wikitable'})
soup =  soup.find_all('td')

alfabeto = []

for i in soup:
	try:
		caracter = i.b.code.text

	except:
		caracter = i.text[0]

	finally:
		alfabeto.append(caracter)

alfabeto_morse = {}

for i in range(len(alfabeto)):
	try:
		alfabeto_morse[alfabeto[0]] = alfabeto[1]
		alfabeto.pop(0)
		alfabeto.pop(0)
	
	except IndexError:
		break

if __name__ == "__main__":
        
        with open('alfabeto_morse.json', 'w') as file:
                file.write(json.dumps(alfabeto_morse))
