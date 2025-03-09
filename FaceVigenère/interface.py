import tkinter as tk
import ttkbootstrap as ttk  # Biblioteca para um visual moderno
from vigenere import tabela_vigenere, tabela_criptografica, descriptografar

# Criar a tabela de Vigenère
criar_tabela = tabela_vigenere()

# Função para criptografar
def criptografar():
    mensagem = entrada_mensagem.get()
    chave = entrada_chave.get()

    if mensagem and chave:
        mensagem_criptografada = tabela_criptografica(mensagem, chave, criar_tabela)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, f"🔒 Criptografado:\n{mensagem_criptografada}")
        resultado_texto.config(state=tk.DISABLED)

# Função para descriptografar
def descriptografar_mensagem():
    mensagem_criptografada = entrada_mensagem.get()
    chave = entrada_chave.get()

    if mensagem_criptografada and chave:
        mensagem_original = descriptografar(mensagem_criptografada, chave, criar_tabela)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, f"🔓 Descriptografado:\n{mensagem_original}")
        resultado_texto.config(state=tk.DISABLED)

# Criar a janela com tema futurista
root = ttk.Window(themename="darkly")  # Escolhe um tema escuro e estiloso
root.title("🔐 Criptografia Vigenère")
root.geometry("400x350")
root.resizable(False, False)

# Estilo futurista
estilo_fonte = ("Consolas", 12, "bold")

# Criar widgets estilizados
ttk.Label(root, text="🔤 Mensagem/Código:", font=estilo_fonte, bootstyle="info").pack(pady=5)
entrada_mensagem = ttk.Entry(root, font=estilo_fonte)
entrada_mensagem.pack(pady=5, fill="x", padx=20)

ttk.Label(root, text="🔑 Chave:", font=estilo_fonte, bootstyle="info").pack(pady=5)
entrada_chave = ttk.Entry(root, font=estilo_fonte)
entrada_chave.pack(pady=5, fill="x", padx=20)

frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=10)

botao_criptografar = ttk.Button(frame_botoes, text="🔒 Criptografar", bootstyle="primary", command=criptografar)
botao_criptografar.pack(side="left", padx=10)

botao_descriptografar = ttk.Button(frame_botoes, text="🔓 Descriptografar", bootstyle="success", command=descriptografar_mensagem)
botao_descriptografar.pack(side="right", padx=10)

# Caixa de resultado estilizada
resultado_texto = tk.Text(root, height=4, width=40, font=estilo_fonte, bg="#222", fg="#0f0", wrap="word")
resultado_texto.pack(pady=10, padx=20, fill="x")
resultado_texto.config(state=tk.DISABLED)

# Rodar a aplicação
root.mainloop()
