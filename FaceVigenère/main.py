from vigenere import tabela_vigenere, tabela_criptografica
import tkinter as tk
from tkinter import Label, Button, Entry, Text,ttk

# Criar a tabela de Vigenère
criar_tabela = tabela_vigenere()

# Função para criptografar usando Tkinter
def criptografar():
    mensagem = entrada_mensagem.get()
    chave = entrada_chave.get()

    if mensagem and chave:
        mensagem_criptografada = tabela_criptografica(mensagem, chave, criar_tabela)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, f"Mensagem Criptografada:\n{mensagem_criptografada}")
        resultado_texto.config(state=tk.DISABLED)



# Criando a janela principal
janela = tk.Tk()
janela.title("Criptografia Vigenère")
janela.geometry("400x300")
janela.config(bg="#121212")

#Estilo
estilo = ttk.Style()
estilo.configure("TLabel", foreground="white", background="#121212", font=("Arial", 12))
estilo.configure("TButton", foreground="black", background="#00aaff", font=("Arial", 12, "bold"))
estilo.map("TButton", background=[("active", "#0088cc")])

# Criando os widgets estilizados
ttk.Label(janela, text="Mensagem:").pack(pady=5)
entrada_mensagem = ttk.Entry(janela, width=50)
entrada_mensagem.pack(pady=5)

ttk.Label(janela, text="Chave:").pack(pady=5)
entrada_chave = ttk.Entry(janela, width=50)
entrada_chave.pack(pady=5)

botao = ttk.Button(janela, text="Criptografar", command=criptografar)
botao.pack(pady=15)

resultado_texto = Text(janela, height=3, width=50, font=("Arial", 12), bg="#1e1e1e", fg="white")
resultado_texto.pack(pady=5)
resultado_texto.config(state=tk.DISABLED)


# Entrada de texto
website_entry = Entry(janela, width=35)
website_entry.pack(pady=5)
website_entry.focus()

# Botão para sair
botao = Button(janela, text="Sair", command=janela.quit)
botao.pack(pady=10)
ttk.Button(janela, text="Limpar", command=lambda: [entrada_mensagem.delete(0, tk.END),
                                                   entrada_chave.delete(0, tk.END),
                                                   resultado_texto.config(state=tk.NORMAL),
                                                   resultado_texto.delete("1.0", tk.END),
                                                   resultado_texto.config(state=tk.DISABLED)]).pack(pady=5)



janela.mainloop()
