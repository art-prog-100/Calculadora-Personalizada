import tkinter
import math

valor_botoes = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "=", "√"]
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
                      foreground=cor_branca, anchor="e", width = contador_coluna)
label.grid(row=0, column=0, columnspan=contador_coluna, sticky="we")


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

def clear_all():
    global A, B, operador
    A = "0"
    operador = None
    B = None
    
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def botao_clicado(value):
    global right_symbols, top_symbols, label, A, B, operador
    digitos = "0123456789"
    
    if value in right_symbols:
        if value == "=":
           if A is not None and operador is not None:
               B = label["text"]
               numA = float(A)
               numB = float(B)
               
               if operador == "+":
                   label["text"] = remove_zero_decimal(numA + numB)
                   
               elif operador == "-":
                   label["text"] = remove_zero_decimal(numA - numB)
                
               elif operador == "×":
                   label["text"] = remove_zero_decimal(numA * numB)
                   
               elif operador == "÷":
                   label["text"] = remove_zero_decimal(numA / numB)
                   
                   
               clear_all()       
               
        if value == "√":
            if A is not None and B is None:
               A  = label["text"] 
               numA = float(A)
               
               label["text"] = str(math.sqrt(numA)) 
        
        
        
        
        
        elif value in "+-×÷":
           if operador is None:
               A = label["text"]
               label["text"] = "0"
               B = 0
           operador = value
           
        elif value in "√":
            if operador is None:
               A = label["text"]
               operador = value
    
               
           
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
            
        elif value == "+/-":
            if "." in label["text"]:
             resultado = float(label["text"])*-1
             label["text"] = str(resultado)
            else:
             resultado = int(label["text"])*-1
             label["text"] = str(resultado)
             
        elif value == "%":
            resultado = float(label["text"])/100
            label["text"] = remove_zero_decimal(resultado)
    
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
            
        elif value in digitos:
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value
                
        

#A+B, A-B, A*B, A/B
A = "0"
operador = None
B = None




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