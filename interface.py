from tkinter import *

class Main:
	"""Janela principal"""
	def __init__(self):
		window = Tk()

		#Frames
		cabecalho = Frame(window)

		#informacoes da janela
		window.title("Janela principal")
		window.geometry("450x500")
		window.resizable(False, False)

		#Labels e buttons
		titulo = Label(cabecalho, text = "Conversor de código Morse", 
			font = ("Arial", 14, "bold"))
		imagem_samuel = PhotoImage(file = 'c:/Users/Lucas/Documents/Python Scripts/codigo morse/imagens/samuel_morse.png')
		bem_vindo_img = Label(cabecalho, image = imagem_samuel)
		#empacotamento
		cabecalho.pack()
		bem_vindo_img.pack()
		titulo.pack()

		window.mainloop()