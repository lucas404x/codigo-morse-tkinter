from tkinter import *

class Main:
	"""Janela principal"""
	def __init__(self):
		window = Tk()

		#Frames
		cabecalho = Frame(window, highlightbackground="black", highlightthickness=7)
		conteudo = Frame(window, highlightbackground="black", highlightthickness=7)

		#informacoes da janela
		window.title("Janela principal")
		window.geometry("450x500")
		window.resizable(False, False)

		#Labels e buttons

		imagem_samuel = PhotoImage(file = 'c:/Users/Lucas/Documents/Python Scripts/codigo morse/imagens/samuel_morse.png')
		img_home = Label(cabecalho, image = imagem_samuel)
		titulo = Label(cabecalho, text = "Conversor de código Morse", 
			font = ("Arial", 14, "bold"), foreground = '#7E9BA4')
		
		texto = Label(conteudo, text = "Insira o seu texto", 
			font = ("Arial", 9))
		entrada_texto = Entry(conteudo, font = ("Arial", 12, "bold"), foreground = '#466943')
		criptografar = Button(conteudo, text = "Criptografar")
		descriptografar = Button(conteudo, text = "Descriptografar")

		#empacotamento
		cabecalho.pack()
		img_home.pack()
		titulo.pack()
		conteudo.pack()
		texto.pack()
		entrada_texto.pack()
		criptografar.pack(side = LEFT)
		descriptografar.pack(side = RIGHT)

		window.mainloop()