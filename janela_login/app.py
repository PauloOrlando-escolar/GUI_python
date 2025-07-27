import customtkinter as ctk
# https://www.youtube.com/watch?v=Px-DgrQ_wjI

# configuração de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# criação validação de entrada


def validar_login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    # verifica se o usuário e senha estão corretos
    if usuario == "paulo" and senha == "1234":
        resultado_login.configure(
            text="Login bem-sucedido!", text_color="green")
    else:
        resultado_login.configure(
            text="Usuário ou senha incorretos!", text_color="red")


# criação da janela principal
janela = ctk.CTk()
janela.title("Janela de Login")
janela.geometry("400x350")

# criação de um frame para o conteúdo
frame = ctk.CTkFrame(janela)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# criação de um título
titulo = ctk.CTkLabel(frame, text="Bem-vindo ao Sistema", font=("Arial", 24))
titulo.pack(pady=10)

# criação de um campo de entrada para o usuário
usuario_label = ctk.CTkLabel(frame, text="Usuário:")
usuario_label.pack(pady=5)
usuario_entry = ctk.CTkEntry(frame, placeholder_text="Digite seu usuário")
usuario_entry.pack(pady=5, padx=20, fill="x")

# criação de um campo de entrada para a senha
senha_label = ctk.CTkLabel(frame, text="Senha:")
senha_label.pack(pady=5)
senha_entry = ctk.CTkEntry(
    frame, placeholder_text="Digite sua senha", show="*")
senha_entry.pack(pady=5, padx=20, fill="x")

# criação de um botão de login
login_button = ctk.CTkButton(
    frame, text="Login", command=validar_login)
login_button.pack(pady=20)

# campo feedback para do login
resultado_login = ctk.CTkLabel(frame, text="")
resultado_login.pack(pady=10)

# execução da janela
janela.mainloop()
