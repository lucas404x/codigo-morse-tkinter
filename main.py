from tkinter import *
from tkinter import messagebox
from funcoes import func

class Main:
	"""Janela principal"""
	def __init__(self):
		window = Tk()

		#Frames
		cabecalho = Frame(window)
		conteudo = Frame(window)

		#informacoes da janela
		window.title("Conversor de código Morse")
		window.geometry("450x500")
		window.resizable(False, False)

		global entrada_texto
		
		#Labels e buttons

		imagem_samuel = PhotoImage(file = 'c:/Users/Lucas/Documents/Python Scripts/codigo morse/imagens/samuel_morse.png')
		img_home = Label(cabecalho, image = imagem_samuel)
		titulo = Label(cabecalho, text = "Conversor de código Morse", 
			font = ("Arial", 14, "bold"), foreground = '#7E9BA4')
		
		texto = Label(conteudo, text = "Insira o seu texto", 
			font = ("Arial", 9))
		entrada_texto = Entry(conteudo, font = ("Arial", 12, "bold"), foreground = '#466943')
		criptografar = Button(conteudo, text = "Criptografar", command = self.criptografia)
		descriptografar = Button(conteudo, text = "Descriptografar", command = self.descriptografia)

		#empacotamento
		cabecalho.pack()
		img_home.pack()
		titulo.pack()
		conteudo.pack()
		texto.pack()
		entrada_texto.pack()
		criptografar.pack(side = LEFT, pady = 8)
		descriptografar.pack(side = RIGHT, pady = 8)

		window.mainloop()

	def criptografia(self):
		msg = func.criptografar(entrada_texto.get())
		messagebox.showinfo('Resultado', "".join(msg))

	def descriptografia(self):
		msg = func.descriptografar(entrada_texto.get().split('/'))
		print(msg)
		messagebox.showinfo('Resultado', "".join(msg))
