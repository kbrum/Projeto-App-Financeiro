import customtkinter as ctk
from tkinter import *
from tkinter import PhotoImage
from tkinter import font
import _mysql_connector

ctk.set_appearance_mode("light")

def tela_register():    
    login_frame.pack_forget()
            
    rg_frame = ctk.CTkFrame(master=janela, width=450, height=596,fg_color="white")
    rg_frame.pack(side=RIGHT)
                
    tamanho_fonte_nubanco = 30
    fonte_nubanco = ("Georgia",tamanho_fonte_nubanco)
    Nubanco_label = ctk.CTkLabel(master=rg_frame, text="Nubanco", font = fonte_nubanco, fg_color="white")
    Nubanco_label.place(x=165, y=40)
                
    tamanho_fonte_ou = 10
    fonte_ou = ctk.CTkFont(size = tamanho_fonte_ou)
    OU2_label = ctk.CTkLabel(rg_frame, text="---------------------------------------------      OU      ---------------------------------------------", font = fonte_ou, fg_color="white")
    OU2_label.place(x=73, y=130)

    email_entry = ctk.CTkEntry(rg_frame, placeholder_text="email", width=300)
    email_entry.place(x=76, y=175)
                
    nome_entry = ctk.CTkEntry(rg_frame, placeholder_text="Nome completo", width=300)
    nome_entry.place(x=76, y=215)
                
    nome_usuario_entry = ctk.CTkEntry(rg_frame, placeholder_text="Nome de usuário", width=300)
    nome_usuario_entry.place(x=76, y=255)
                
    senha_entry = ctk.CTkEntry(rg_frame, placeholder_text="senha", width=300, show="*")
    senha_entry.place(x=76, y=295)

    fonte_descriçao = 12
    fonte_descriçao = ctk.CTkFont(size = fonte_descriçao)
    descriçao_label = ctk.CTkLabel(master=rg_frame, text="Ao se cadastrar, você concorda com nossos\nTermos,Política de Privacidade e Política de\n Cookies.", font = fonte_descriçao)
    descriçao_label.place(x=100, y=340)            

    cadastro_button = ctk.CTkButton(rg_frame, text="Cadastre-se", width=300, fg_color="#00a8ff",hover_color= "#00a8ff",)
    cadastro_button.place(x=76, y=400)
                
    facebook_button2 = ctk.CTkButton(master=rg_frame,text="Entrar com o Facebook", width=300,fg_color="#0d94eb",text_color="white", hover_color="#397ebf")
    facebook_button2.place(x=76, y=90)
    
    #Inserir "tem uma conta?"
    tem_conta_fonte = 14
    tem_conta = ctk.CTkFont(size = tem_conta_fonte)
    tem_conta_label = ctk.CTkLabel(master=rg_frame, text="Tem uma conta?", font = tem_conta, fg_color="white")
    tem_conta_label.place(x=120, y=500)

    
    
    
    #Inserir botao conecte-se para voltar na janela de login
    def conecte():
        rg_frame.pack_forget()

        login_frame.pack(side=RIGHT)
        pass
    
    fonte_conecte = 14
    fonte_conecte = ctk.CTkFont(size = fonte_conecte)
    conecte_button = ctk.CTkButton(master=rg_frame, text="Conecte-se", font= fonte_conecte, width=50, fg_color="white", text_color="#4169e1", hover_color="white", command=conecte)
    conecte_button.place(x=225, y=500)
    

#Janela principal de login
janela = ctk.CTk()
janela.geometry("900x600")
janela.title("NUBANCO")
janela.resizable(False,False)
janela.iconbitmap("nubanco.ico")
        
      
#Frame direito
login_frame = ctk.CTkFrame(master=janela, width=450, height=596,fg_color="white")
login_frame.pack(side=RIGHT)
        
#Frame esquerdo
logo_frame = ctk.CTkFrame(master=janela, width=450, height=596, fg_color="#6b3fa0")
logo_frame.pack(side=LEFT)

#imagem nubanco
img1 = PhotoImage(file="nubanco.png")
lbl_img1 = ctk.CTkLabel(master=logo_frame, text= None,image=img1, width=225)
lbl_img1.place(x=110, y=175)

#Nubanco 
tamanho_fonte_nubanco = 60
fonte_nubanco = ("Microsoft Himalaya",tamanho_fonte_nubanco)
Nubanco_label = ctk.CTkLabel(master=login_frame, text="Nubanco", font = fonte_nubanco, fg_color="white")
Nubanco_label.place(x=155, y=40)

#inserir "nome de usuario"
username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Telefone, nome de usuário ou email", width=300).place(x=75, y=105)

username_label = ctk.CTkLabel(master=login_frame, text="*o campo acima é de carater obrigatorio.", text_color="green").place(x=75, y=135)

#inserir "senha de usuario""
password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="senha", width=300, show="*").place(x=75, y=175)

password_label = ctk.CTkLabel(master=login_frame, text="*o campo acima é de carater obrigatorio.", text_color="green").place(x=75, y=205)

#inserir Check box
chekbox = ctk.CTkCheckBox(master=login_frame, text="Lembra-se de mim sempre").place(x=75, y=235)

#botão login
login_button = ctk.CTkButton(master=login_frame, text="Entrar", width=300, fg_color="#00a8ff", hover_color= "#00a8ff").place(x=75, y=285)

#inserir o "OU"
tamanho_fonte_ou = 10
fonte_ou = ctk.CTkFont(size = tamanho_fonte_ou)
OU_label = ctk.CTkLabel(master=login_frame, text="----------------------------------------------  OU  -----------------------------------------------", font = fonte_ou)
OU_label.place(x=75, y=320)

#Imagem facebook
img2 = PhotoImage(file="facebook.png")
lbl_img2 = Label(image=img2, width=20, height=20)
lbl_img2.place(x=590, y=375)

#Botao entrar com o facebook
fonte_entrar = 13
fonte_entrar = ctk.CTkFont("bold", size = fonte_entrar)
facebook_button = ctk.CTkButton(master=login_frame, text="Entrar com o Facebook", width=50,fg_color="white",text_color="black", hover_color="white", font= fonte_entrar).place(x=165, y=370)

#Botao Esqueceu a senha
forgotpassword_button = ctk.CTkButton(master=login_frame, text="Esqueceu a senha?", width=50, fg_color="white", text_color="black", hover_color="white").place(x=165, y=420)


#Inserir "nao tem uma conta"
tamanho_fonte_cadastro = 14
fonte_cadastro = ctk.CTkFont(size = tamanho_fonte_cadastro)
nao_tem_conta_label = ctk.CTkLabel(master=login_frame, text="Não tem uma conta?", font = fonte_cadastro)
nao_tem_conta_label.place(x=110, y=500)

#Inserir bota casdastre-se na tela de login
fonte_cadastre = 14
fonte_cadastre = ctk.CTkFont("bold", size = fonte_cadastre)
cadastre_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", font= fonte_cadastre, width=10, fg_color="white", text_color="#4169e1", hover_color="white", command=tela_register)
cadastre_button.place(x=239, y=500)

janela.mainloop()  
