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

contador_linha = len(valor_botoes)
contador_coluna = len(valor_botoes[0])

cor_cinza = "#4F4F4F"
cor_cinza_claro ="#D3D3D3"
cor_preta = "#000000"
cor_laranja = "#FF9500"
cor_branca = "#ffffff"

# montagem da janela
janela = tkinter.Tk()
janela.title("Calculadora")
janela.resizable(False, False)

frame = tkinter.Frame(janela)

label = tkinter.Label(frame, text="0", font=("Arial", 45), background=cor_preta,
                      foreground=cor_branca, anchor="e")
label.grid(row=0, column=0, columnspan=contador_coluna, sticky="we")

def botao_clicado(value):
    pass

for linha in range(contador_linha):
    for coluna in range(contador_coluna):
        valor = valor_botoes[linha][coluna]
        botao = tkinter.Button(frame, text=valor, font=("Arial", 30),
                               width=3, height=1,
                               command=lambda valor=valor: botao_clicado(valor))
        if valor in top_symbols:
            botao.config(foreground=cor_preta, background= cor_cinza)
        elif valor in right_symbols:
            botao.config(foreground=cor_branca, background= cor_laranja)
        else:
            botao.config(foreground=cor_branca, background= cor_cinza_claro)    
        
        botao.grid(row=linha + 1, column=coluna)

frame.pack()

#centralizar a janela
janela.update()
janela_width = janela.winfo_width()
janela_height = janela.winfo_height()
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

janela_x = int((screen_width/2) - (janela_width/2))
janela_y = int((screen_height/2) - (janela_height/2))

#formato
janela.geometry(f"{janela_width}x{janela_height}+{janela_x}+{janela_y}")
janela.mainloop()