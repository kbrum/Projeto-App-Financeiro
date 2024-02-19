import customtkinter as ctk
from tkinter import *
from tkinter import PhotoImage
import webbrowser

class LoginApp:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("900x600")
        self.janela.title("NUBANCO")
        self.janela.resizable(False, False)
        self.janela.iconbitmap("nubanco.ico")
        self.tela_login()
    
    def tela_login(self):
        self.login_frame = ctk.CTkFrame(master=self.janela, width=450, height=596, fg_color="white")
        self.login_frame.pack(side=RIGHT)
        
        self.logo_frame = ctk.CTkFrame(master=self.janela, width=450, height=596, fg_color="#6b3fa0")
        self.logo_frame.pack(side=LEFT)
        
        
        img1 = PhotoImage(file="nubanco.png")
        lbl_img1 = ctk.CTkLabel(master=self.logo_frame, text=None, image=img1, width=225)
        lbl_img1.place(x=110, y=175)
        
        tamanho_fonte_nubanco = 60
        fonte_nubanco = ("Microsoft Himalaya", tamanho_fonte_nubanco)
        Nubanco_label = ctk.CTkLabel(master=self.login_frame, text="Nubanco", font=fonte_nubanco, fg_color="white")
        Nubanco_label.place(x=155, y=40)
        
        username_entry = ctk.CTkEntry(master=self.login_frame, placeholder_text="Telefone, nome de usuário ou email", width=300)
        username_entry.place(x=75, y=105)
        
        username_label = ctk.CTkLabel(master=self.login_frame, text="*o campo acima é de carater obrigatorio.", text_color="green")
        username_label.place(x=75, y=135)
        
        password_entry = ctk.CTkEntry(master=self.login_frame, placeholder_text="senha", width=300, show="*")
        password_entry.place(x=75, y=175)
        
        password_label = ctk.CTkLabel(master=self.login_frame, text="*o campo acima é de carater obrigatorio.", text_color="green")
        password_label.place(x=75, y=205)
        
        checkbox = ctk.CTkCheckBox(master=self.login_frame, text="Lembra-se de mim sempre")
        checkbox.place(x=75, y=235)
        
        login_button = ctk.CTkButton(master=self.login_frame, text="Entrar", width=300, fg_color="#00a8ff", hover_color="#00a8ff")
        login_button.place(x=75, y=285)
        
        tamanho_fonte_ou = 13
        fonte_ou = ctk.CTkFont(size=tamanho_fonte_ou)
        OU_label = ctk.CTkLabel(master=self.login_frame, text="-------------------------------      OU      -------------------------------", font=fonte_ou)
        OU_label.place(x=75, y=325)
        
        img2 = PhotoImage(file="facebook.png")
        lbl_img2 = ctk.CTkLabel(self.login_frame, image=img2 , text= None, width=0, height=0)
        lbl_img2.place(x=130, y=368)
        
        fonte_entrar = 13
        fonte_entrar = ctk.CTkFont("bold", size=fonte_entrar)
        facebook_button = ctk.CTkButton(self.login_frame, text="Entrar com o Facebook", width=50, fg_color="white", text_color="black", hover_color="white", font=fonte_entrar, command=self.login_with_facebook)
        facebook_button.place(x=165, y=370)

        forgotpassword_button = ctk.CTkButton(master=self.login_frame, text="Esqueceu a senha?", width=50, fg_color="white", text_color="black", hover_color="white")
        forgotpassword_button.place(x=165, y=420)
        
        tamanho_fonte_cadastro = 14
        fonte_cadastro = ctk.CTkFont(size=tamanho_fonte_cadastro)
        nao_tem_conta_label = ctk.CTkLabel(master=self.login_frame, text="Não tem uma conta?", font=fonte_cadastro)
        nao_tem_conta_label.place(x=110, y=500)
        
        fonte_cadastre = 14
        fonte_cadastre = ctk.CTkFont("bold", size=fonte_cadastre)
        cadastre_button = ctk.CTkButton(master=self.login_frame, text="Cadastre-se", font=fonte_cadastre, width=10, fg_color="white", text_color="#4169e1", hover_color="white", command=self.tela_register)
        cadastre_button.place(x=239, y=500)
    
    def login_with_facebook(self):
        # URL de login do Facebook
        self.facebook_login_url = "https://www.facebook.com/login.php"

        # Abrir a página de login do Facebook no navegador padrão
        webbrowser.open(self.facebook_login_url)

    
    def tela_register(self):
        self.login_frame.pack_forget()
        
        self.rg_frame = ctk.CTkFrame(master=self.janela, width=450, height=596, fg_color="white")
        self.rg_frame.pack(side=RIGHT)
        
        tamanho_fonte_nubanco = 30
        fonte_nubanco = ("Georgia", tamanho_fonte_nubanco)
        Nubanco_label = ctk.CTkLabel(master=self.rg_frame, text="Nubanco", font=fonte_nubanco, fg_color="white")
        Nubanco_label.place(x=165, y=40)
        
        tamanho_fonte_ou = 13
        fonte_ou = ctk.CTkFont(size=tamanho_fonte_ou)
        OU2_label = ctk.CTkLabel(self.rg_frame, text="-------------------------------      OU      -------------------------------", font=fonte_ou, fg_color="white")
        OU2_label.place(x=75, y=130)
        
        email_entry = ctk.CTkEntry(self.rg_frame, placeholder_text="email", width=300)
        email_entry.place(x=76, y=175)
        
        nome_entry = ctk.CTkEntry(self.rg_frame, placeholder_text="Nome completo", width=300)
        nome_entry.place(x=76, y=215)
        
        nome_usuario_entry = ctk.CTkEntry(self.rg_frame, placeholder_text="Nome de usuário", width=300)
        nome_usuario_entry.place(x=76, y=255)
        
        senha_entry = ctk.CTkEntry(self.rg_frame, placeholder_text="senha", width=300, show="*")
        senha_entry.place(x=76, y=295)
        
        fonte_descriçao = 12
        fonte_descriçao = ctk.CTkFont(size=fonte_descriçao)
        descriçao_label = ctk.CTkLabel(master=self.rg_frame, text="Ao se cadastrar, você concorda com nossos\nTermos,Política de Privacidade e Política de\n Cookies.", font=fonte_descriçao)
        descriçao_label.place(x=100, y=340)
        
        cadastro_button = ctk.CTkButton(self.rg_frame, text="Cadastre-se", width=300, fg_color="#00a8ff", hover_color="#00a8ff")
        cadastro_button.place(x=76, y=400)
        
        facebook_button2 = ctk.CTkButton(master=self.rg_frame, text="Entrar com o Facebook", width=300, fg_color="#0d94eb", text_color="white", hover_color="#397ebf", command=self.rg_with_facebook)
        facebook_button2.place(x=76, y=90)
        
        tem_conta_fonte = 14
        tem_conta = ctk.CTkFont(size=tem_conta_fonte)
        tem_conta_label = ctk.CTkLabel(master=self.rg_frame, text="Tem uma conta?", font=tem_conta, fg_color="white")
        tem_conta_label.place(x=120, y=500)

        # Adicionando o botão "Conecte-se" ao frame de registro (rg_frame)
        fonte_conecte = 14
        fonte_conecte = ctk.CTkFont(size=fonte_conecte)
        conecte_button = ctk.CTkButton(master=self.rg_frame, text="Conecte-se", font=fonte_conecte, width=50, fg_color="white", text_color="#4169e1", hover_color="white", command=self.conecte)
        conecte_button.place(x=225, y=500)

    def rg_with_facebook(self):
        self.facebook_rg_url ="https://www.facebook.com/login.php"
        webbrowser.open(self.facebook_rg_url)   
        
    def conecte(self):
        self.rg_frame.pack_forget()
        
        self.login_frame.pack(side=RIGHT)
        
        
def main():
    janela = ctk.CTk()
    app = LoginApp(janela)
    janela.mainloop()

main()
