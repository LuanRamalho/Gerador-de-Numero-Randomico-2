import tkinter as tk
import random

def gerar_numero():
    numero_aleatorio = random.randint(1, 1000000)
    label_resultado.config(text=f"Número gerado: {numero_aleatorio}")

# Configuração da Janela
root = tk.Tk()
root.title("Gerador de Número Aleatório")
root.configure(bg="#000B75")  # Cor de fundo escuro
root.geometry("300x200")  # Tamanho da janela

# Label para mostrar o número gerado
label_resultado = tk.Label(root, text="", bg="#4E6700", fg="white", font=("Arial", 16, "bold"))
label_resultado.pack(pady=20)

# Botão para gerar o número
botao_gerar = tk.Button(root, text="Gerar Número (1 - 1.000.000)", command=gerar_numero, bg="#00810F", fg="white", font=("Arial", 14, "bold"))
botao_gerar.pack(pady=10)

# Executar a aplicação
root.mainloop()
