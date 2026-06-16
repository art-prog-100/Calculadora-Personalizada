import tkinter

valor_botoes = [
["AC", "+/-", "%", "÷"], 
["7", "8", "9", "×"], 
["4", "5", "6", "-"],
["1", "2", "3", "+"],
["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

contador_linha = len(valor_botoes)#5
contador_coluna = len(valor_botoes[0])#4

cor_cinza = "#4F4F4F"
cor_preta = "#000000"
cor_laranja = "#FF9500"
cor_branca = "#ffffff"

#montagem da janela

janela = tkinter.Tk() #criando janela
janela.title("Calculadora")
janela.resizable(False,False)

frame = tkinter.Frame(janela)
label = tkinter.Label(frame,text = "0", font = ("Arial", 45), background = cor_preta,
                      foreground= cor_branca)
label.pack()


frame.pack()





janela.mainloop()