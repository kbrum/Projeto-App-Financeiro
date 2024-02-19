import customtkinter as ctk
from tkinter import *
from tkinter import PhotoImage
import webbrowser
import time
class LoginApp:
    
    #janela principal    
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("900x600")
        self.janela.title("nubanco.com.br")
        self.janela.resizable(False, False)
        self.janela.iconbitmap("nubanco.ico")
        self.mais_visivel = True
        self.mais_visivel = False
        self.tela_login()
        
    #tela de login
    def tela_login(self):
        self.login_frame = ctk.CTkFrame(master=self.janela, width=450, height=600, fg_color="white", corner_radius=0)
        self.login_frame.pack(side=RIGHT)

        self.logo_frame = ctk.CTkFrame(master=self.janela, width=450, height=600, fg_color="#6b3fa0", corner_radius=0)
        self.logo_frame.pack(side=LEFT)    

        img1 = PhotoImage(file="nubanco.png")
        lbl_img1 = ctk.CTkLabel(master=self.logo_frame, text=None, image=img1, width=225)
        lbl_img1.place(x=110, y=175)

        tamanho_fonte_nubanco = 60
        fonte_nubanco = ("Microsoft Himalaya", tamanho_fonte_nubanco)
        Nubanco_label = ctk.CTkLabel(master=self.login_frame, text="Nubanco", font=fonte_nubanco, fg_color="white")
        Nubanco_label.place(x=155, y=40)

        username_entry = ctk.CTkEntry(master=self.login_frame, placeholder_text="Telefone, nome de usuário ou email",placeholder_text_color="#333333", width=300, height=35, corner_radius=4,border_width=1,border_color="#CCCCCC")
        username_entry.place(x=75, y=135)

        password_entry = ctk.CTkEntry(master=self.login_frame, placeholder_text="senha",placeholder_text_color="#333333", width=300, height=35, corner_radius=4,border_width=1,border_color="#CCCCCC", show="*")
        password_entry.place(x=75, y=175)

        checkbox = ctk.CTkCheckBox(master=self.login_frame, text="Lembra-se de mim sempre", width=5,height=5, corner_radius=50)
        checkbox.place(x=75, y=235)

        login_button = ctk.CTkButton(master=self.login_frame, text="Entrar", width=300, height=32, fg_color="#00a8ff", hover_color="#00a8ff", corner_radius=9, command=self.menu)
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
        cadastre_button = ctk.CTkButton(master=self.login_frame, text="Cadastre-se", font=fonte_cadastre, width=10, fg_color="white", text_color="#0d84ff", hover_color="white", command=self.tela_register)
        cadastre_button.place(x=239, y=500)
        
    #facebook link
    def login_with_facebook(self):

        self.facebook_login_url = "https://www.facebook.com/login.php"

        webbrowser.open(self.facebook_login_url)
        
    #tela de menu do app
    def menu(self):
        self.login_frame.pack_forget()
        self.logo_frame.pack_forget()

        self.funções_frame = ctk.CTkFrame(master=self.janela, width=170, height=600, fg_color="white", corner_radius=0, border_width=1, border_color="#E0E0E0")
        self.funções_frame.place(x=0, y=0)
        self.app_frame = ctk.CTkFrame(master=self.janela, width=730, height=600, fg_color="white", corner_radius=0)
        self.app_frame.place(x=170,y=0)

        fonte_nubanco_menu = 35
        fonte_nubanco_menu = ctk.CTkFont("Microsoft Himalaya", size=fonte_nubanco_menu)

        nubanco_menu = ctk.CTkButton(self.funções_frame, text="Nubanco", width=50, fg_color="white", text_color="#333333", hover_color="white", font=fonte_nubanco_menu, command=self.inicial)
        nubanco_menu.place(x=10, y=35)

        fonte_botoes_menu = 14
        fonte_botoes_menu = ctk.CTkFont(size=fonte_botoes_menu)

        inicial_botao = ctk.CTkButton(self.funções_frame, text="Página Inicial", width=50, fg_color="white", text_color="#333333", hover_color="white", font=fonte_botoes_menu, command=self.inicial)
        inicial_botao.place(x=40, y=110)

        img4 = PhotoImage(file="casa.png")
        lbl_img4 = ctk.CTkLabel(self.funções_frame, image=img4 , text= None, width=0, height=0)
        lbl_img4.place(x=8, y=105)

        pesquisa_botao = ctk.CTkButton(self.funções_frame, text="Pesquisa", width=50, fg_color="white", text_color="#333333", hover_color="white", font=fonte_botoes_menu)
        pesquisa_botao.place(x=40, y=165)

        img5 = PhotoImage(file="lupa.png")
        lbl_img5 = ctk.CTkLabel(self.funções_frame, image=img5 , text= None, width=0, height=0)
        lbl_img5.place(x=8, y=160)

        despesas_botao = ctk.CTkButton(self.funções_frame, text="Despesas", width=50, fg_color="white", text_color="#333333", hover_color="white", font=fonte_botoes_menu, command=self.despesas)
        despesas_botao.place(x=40, y=220)

        img6 = PhotoImage(file="despesas.png")
        lbl_img6 = ctk.CTkLabel(self.funções_frame, image=img6 , text= None, width=0, height=0)
        lbl_img6.place(x=8, y=220)

        dividas_botao = ctk.CTkButton(self.funções_frame, text="Dívidas", width=50, fg_color="white", text_color="#333333", hover_color="white", font=fonte_botoes_menu, command=self.dividas)
        dividas_botao.place(x=40, y=275)

        img7 = PhotoImage(file="dividas.png")
        lbl_img7 = ctk.CTkLabel(self.funções_frame, image=img7 , text= None, width=0, height=0)
        lbl_img7.place(x=8, y=275)

        mais_botao = ctk.CTkButton(self.funções_frame, text="Mais", width=50, fg_color="white", text_color="#333333", hover_color="white", font=fonte_botoes_menu, command=self.mais)
        mais_botao.place(x=40, y=550)

        img8 = PhotoImage(file="mais.png")
        lbl_img8 = ctk.CTkLabel(self.funções_frame, image=img8 , text= None, width=0, height=0)
        lbl_img8.place(x=8, y=548)

        perfil_botao = ctk.CTkButton(self.funções_frame, text="Perfil", width=50, fg_color="white", text_color="#333333", hover_color="white", font=fonte_botoes_menu, command=self.perfil)
        perfil_botao.place(x=40, y=330)

        img9 = PhotoImage(file="perfil.png")
        lbl_img9 = ctk.CTkLabel(self.funções_frame, image=img9 , text= None, width=0, height=0)
        lbl_img9.place(x=8, y=330)

    #Pagina inicial do app
    def inicial(self):
        if hasattr(self, 'despesas_frame') and self.despesas_frame:
            self.despesas_frame.destroy()
        if hasattr(self, 'dividas_frame') and self.dividas_frame:
            self.dividas_frame.destroy()
        if hasattr(self, 'perfil_frame') and self.perfil_frame:
            self.perfil_frame.destroy()

        self.app_frame.place(x=170,y=0)
        
    #Pagina de despesas do app
    def despesas(self):
        if hasattr(self, 'app_frame') and self.app_frame:
            self.app_frame.pack_forget()    
        if hasattr(self, 'dividas_frame') and self.dividas_frame:
            self.dividas_frame.destroy()
        if hasattr(self, 'perfil_frame') and self.perfil_frame:
            self.perfil_frame.destroy()

        self.despesas_frame = ctk.CTkFrame(master=self.janela, width=730, height=600, fg_color="white", corner_radius=0)
        self.despesas_frame.place(x=170,y=0)
        
    #Pagina de dividas do app
    def dividas(self):
        if hasattr(self, 'app_frame') and self.app_frame:
            self.app_frame.pack_forget()    
        if hasattr(self, 'despesas_frame') and self.despesas_frame:
            self.despesas_frame.destroy()
        if hasattr(self, 'perfil_frame') and self.perfil_frame:
            self.perfil_frame.destroy()

        self.dividas_frame = ctk.CTkFrame(master=self.janela, width=730, height=600, fg_color="white", corner_radius=0)
        self.dividas_frame.place(x=170,y=0)
            
    #Pagina de perfil do app
    def perfil(self):
        if hasattr(self, 'app_frame') and self.app_frame:
            self.app_frame.pack_forget()    
        if hasattr(self, 'despesas_frame') and self.despesas_frame:
            self.despesas_frame.destroy()
        if hasattr(self, 'dividas_frame') and self.dividas_frame:
            self.dividas_frame.destroy()

        self.perfil_frame = ctk.CTkFrame(master=self.janela, width=730, height=600, fg_color="white", corner_radius=0)
        self.perfil_frame.place(x=170,y=0) 

    #botao 'mais' do menu do app
    def mais(self):

        if self.mais_visivel:
            self.mais_frame.destroy()
            self.mais_visivel = False

        else:
            self.mais_frame = ctk.CTkFrame(master=self.janela, width=185, height=50, fg_color="white", corner_radius=13, bg_color="white", border_width=1, border_color="#E0E0E0")
            self.mais_frame.place(x=10, y=485)   
            self.mais_visivel = True

            fonte_logout = 15
            fonte_logout = ctk.CTkFont("bold", size=fonte_logout)

            logout_button = ctk.CTkButton(master=self.mais_frame, text="logout                           ", width=168, height=35, fg_color="white", text_color="#333333", hover_color="#F0F0F0", font=fonte_logout, command=self.logout)
            logout_button.place(x=8, y=8)
    
    #botao 'logout' do menu do app
    def logout(self):
        if hasattr(self, 'despesas_frame') and self.despesas_frame:
            self.despesas_frame.destroy()
        if hasattr(self, 'dividas_frame') and self.dividas_frame:
            self.dividas_frame.destroy()
        if hasattr(self, 'perfil_frame') and self.perfil_frame:
            self.perfil_frame.destroy()
        if hasattr(self, 'mais_frame') and self.mais_frame:
            self.mais_frame.destroy()
        if hasattr(self, 'funções_frame') and self.funções_frame:
            self.funções_frame.destroy()
        if hasattr(self, 'app_frame') and self.app_frame:
            self.app_frame.destroy()
        self.login_frame.pack(side=RIGHT)
        self.logo_frame.pack(side=LEFT)
        
    #tela de registro
    def tela_register(self):
        self.login_frame.pack_forget()
        self.rg_frame = ctk.CTkFrame(master=self.janela, width=450, height=600, fg_color="white", corner_radius=0)
        self.rg_frame.pack(side=RIGHT)

        tamanho_fonte_nubanco = 30
        fonte_nubanco = ("Georgia", tamanho_fonte_nubanco)
        Nubanco_label = ctk.CTkLabel(self.rg_frame, text="Nubanco", font=fonte_nubanco, fg_color="white")
        Nubanco_label.place(x=165, y=40)

        tamanho_fonte_ou = 13
        fonte_ou = ctk.CTkFont(size=tamanho_fonte_ou)
        OU2_label = ctk.CTkLabel(self.rg_frame, text="-------------------------------      OU      -------------------------------", font=fonte_ou, fg_color="white")
        OU2_label.place(x=75, y=130)

        email_entry = ctk.CTkEntry(self.rg_frame, placeholder_text="email",placeholder_text_color="#333333", width=300, height=35, corner_radius=4,border_width=1,border_color="#CCCCCC")
        email_entry.place(x=76, y=175)

        nome_entry = ctk.CTkEntry(self.rg_frame, placeholder_text="Nome completo",placeholder_text_color="#333333", width=300, height=35, corner_radius=4,border_width=1,border_color="#CCCCCC")
        nome_entry.place(x=76, y=215)

        nome_usuario_entry = ctk.CTkEntry(self.rg_frame, placeholder_text="Nome de usuário",placeholder_text_color="#333333", width=300, height=35, corner_radius=4,border_width=1,border_color="#CCCCCC")
        nome_usuario_entry.place(x=76, y=255)

        senha_entry = ctk.CTkEntry(self.rg_frame, placeholder_text="senha", width=300, height=35,placeholder_text_color="#333333", corner_radius=4,border_width=1,border_color="#CCCCCC", show="*")
        senha_entry.place(x=76, y=295)

        fonte_descriçao = 12
        fonte_descriçao = ctk.CTkFont(size=fonte_descriçao)
        descriçao_label = ctk.CTkLabel(self.rg_frame, text="Ao se cadastrar, você concorda com nossos",text_color="#333333", font=fonte_descriçao)
        descriçao_label.place(x=100, y=340)

        cadastro_button = ctk.CTkButton(self.rg_frame, text="Cadastre-se", width=300, height=32, fg_color="#00a8ff", hover_color="#00a8ff", corner_radius=9, command=self.cadastre_se)
        cadastro_button.place(x=76, y=415)

        facebook_button2 = ctk.CTkButton(self.rg_frame, text="Entrar com o Facebook", width=300, height=32, fg_color="#0d94eb", text_color="white", hover_color="#397edf", corner_radius=9, command=self.rg_with_facebook)
        facebook_button2.place(x=76, y=90)

        img3 = PhotoImage(file="facebook.rg1.png")
        lbl_img3 = ctk.CTkLabel(self.rg_frame, text=None, image=img3, width=0, height=0)
        lbl_img3.place(x=137, y=95)

        tem_conta_fonte = 14
        tem_conta = ctk.CTkFont(size=tem_conta_fonte)
        tem_conta_label = ctk.CTkLabel(self.rg_frame, text="Tem uma conta?", font=tem_conta, fg_color="white")
        tem_conta_label.place(x=120, y=500)

        fonte_conecte = 14
        fonte_conecte = ctk.CTkFont(size=fonte_conecte)
        conecte_button = ctk.CTkButton(self.rg_frame, text="Conecte-se", font=fonte_conecte, width=50, fg_color="white", text_color="#0d84ff", hover_color="white", command=self.conecte)
        conecte_button.place(x=225, y=500)

        links_fonte = 12
        links_fonte = ctk.CTkFont(size=links_fonte)

        termos_button = ctk.CTkButton(self.rg_frame, text="  Termos,", width=0, text_color="#211a60", fg_color="transparent", font= links_fonte, hover_color="white", command=self.termos)
        termos_button.place(x=112, y=360)

        privacidade_button = ctk.CTkButton(self.rg_frame, text="Política de Privacidade e       ", width=0, text_color="#211a60", fg_color="transparent", font= links_fonte, hover_color="white", command=self.privacidade)
        privacidade_button.place(x=168, y=360)

        cookies_button = ctk.CTkButton(self.rg_frame, text="Política de Cookies.", width=0, text_color="#211a60", fg_color="transparent", font= links_fonte, hover_color="white", command=self.cookies)
        cookies_button.place(x=160, y=380)
        
    #link dos termos 
    def termos(self):
        self.termos_janela = ctk.CTkToplevel(self.janela)
        self.termos_janela.geometry("600x600")
        self.termos_janela.grab_set()
        self.termos_janela.iconbitmap("nubanco_privacidade.ico")   
        self.termos_janela.title("Central de Privacidade")

        self.termos_frame = ctk.CTkFrame(master=self.termos_janela, width=600, height=600, fg_color="#E0F5FF", corner_radius=0)
        self.termos_frame.place(x=0 , y=0)

    #link de privacidade
    def privacidade(self):
        self.privacidade_janela = ctk.CTkToplevel(self.janela)
        self.privacidade_janela.geometry("600x600")
        self.privacidade_janela.grab_set()
        self.privacidade_janela.iconbitmap("nubanco_privacidade.ico")   
        self.privacidade_janela.title("Central de Privacidade")

        self.privacidade_frame = ctk.CTkFrame(master=self.privacidade_janela, width=600, height=600, fg_color="#E0F5FF", corner_radius=0)
        self.privacidade_frame.place(x=0 , y=0)

        fonte_privacidade_titulo = 22
        fonte_privacidade_titulo = ctk.CTkFont("bold Segoe UI Historic",fonte_privacidade_titulo)

        self.privacidade_titulo_label = ctk.CTkLabel(self.privacidade_frame, font=fonte_privacidade_titulo, text="Política de Privacidade")
        self.privacidade_titulo_label.place(x=30 ,y=50)  
        self.privacidade_titulo_label = ctk.CTkLabel(self.privacidade_frame, font=fonte_privacidade_titulo, text="O que é a Política de Privacidade e o que ela aborda?")
        self.privacidade_titulo_label.place(x=30 ,y=90)                                   

        fonte_privacidade_texto = 15
        fonte_privacidade_texto = ctk.CTkFont(size=fonte_privacidade_texto)

        self.privacidade_texto_label = ctk.CTkLabel(self.privacidade_frame, font=fonte_privacidade_texto, text="Nós, da Nubanco, queremos que você saiba quais informações coletamos \ne como as usamos e compartilhamos. É por essa razão que recomendamos \na leitura da nossa Política de Privacidade. Isso facilita o uso das ferramentas \nde maneira certa para você.", justify="left")
        self.privacidade_texto_label.place(x=30,y=150)
        self.privacidade_texto_label = ctk.CTkLabel(self.privacidade_frame, font=fonte_privacidade_texto, text="Na Política de Privacidade, explicamos como coletamos, usamos, compartilhamos, \nretemos e transferimos informações. Explicamos também quais são seus direitos. \nCada seção da Política apresenta exemplos úteis em uma linguagem simples para \nque nossas práticas sejam fáceis de entender. Além disso, adicionamos links para \nrecursos em que você pode saber mais sobre tópicos de privacidade do seu \ninteresse.", justify="left")
        self.privacidade_texto_label.place(x=30,y=230)
        self.privacidade_texto_label = ctk.CTkLabel(self.privacidade_frame, font=fonte_privacidade_texto, text="Para nós, é importante que você saiba como controlar sua privacidade. Por isso, \ntambém mostramos onde gerenciar suas informações nas configurações das \nferramentas da Nubanco que você usa.", justify="left")
        self.privacidade_texto_label.place(x=30,y=340)
        
    #link de cookies
    def cookies(self):
        self.cookies_janela = ctk.CTkToplevel(self.janela)
        self.cookies_janela.geometry("600x600")
        self.cookies_janela.grab_set()
        self.cookies_janela.iconbitmap("nubanco_privacidade.ico")   
        self.cookies_janela.title("Central de Privacidade")


        self.cookies_frame = ctk.CTkFrame(master=self.cookies_janela, width=600, height=600, fg_color="#E0F5FF", corner_radius=0)
        self.cookies_frame.place(x=0 , y=0)

        fonte_cookies_titulo = 22
        fonte_cookies_titulo = ctk.CTkFont("bold Segoe UI Historic",fonte_cookies_titulo)

        self.titulo_cookies_label = ctk.CTkLabel(self.cookies_frame, font=fonte_cookies_titulo, text="Política de Cookies")
        self.titulo_cookies_label.place(x=30 ,y=50)  
        self.titulo_cookies_label = ctk.CTkLabel(self.cookies_frame, font=fonte_cookies_titulo, text="O que são cookies e o que esta política aborda?")
        self.titulo_cookies_label.place(x=30 ,y=90)                                   

        fonte_cookies_texto = 15
        fonte_cookies_texto = ctk.CTkFont(size=fonte_cookies_texto)

        self.cookies_texto_label = ctk.CTkLabel(self.cookies_frame, font=fonte_cookies_texto, text="Cookies são pequenos fragmentos de texto usados para armazenar informações \nem navegadores da web. Os cookies são usados para armazenar e receber \nidentificadores e outras informações em computadores, smartphones e outros \ndispositivos. Outras tecnologias, inclusive os dados que armazenamos no seu \nnavegador ou dispositivo, identificadores associados ao seu dispositivo e outros \nsoftwares, são usadas com finalidades semelhantes. Nesta política, nós nos \nreferimos a todas essas tecnologias como “cookies.", justify="left")
        self.cookies_texto_label.place(x=30,y=150)
        self.cookies_texto_label = ctk.CTkLabel(self.cookies_frame, font=fonte_cookies_texto, text="Esta política explica como usamos os cookies e as opções que você tem. Salvo \ndisposições em contrário indicadas nesta política, a\nserá aplicada ao nosso tratamento de dados que coletamos por meio de cookies.", justify="left")
        self.cookies_texto_label.place(x=30,y=288)
        cookies_button = ctk.CTkButton(master=self.cookies_frame, text="Política de Privacidade", width=0, height=0, text_color="#211a60", fg_color="transparent", font= fonte_cookies_texto, hover_color="#E0F5FF", command=self.privacidade)
        cookies_button.place(x=381, y=304)
        
    #link do facebook 
    def rg_with_facebook(self):
        self.facebook_rg_url ="https://www.facebook.com/login.php"
        webbrowser.open(self.facebook_rg_url)   
        
    #botao 'conecte' da tela de registro
    def conecte(self):
        self.rg_frame.pack_forget()

        self.login_frame.pack(side=RIGHT)
        
    #botao 'casdastre-se' da tela de resgistro
    def cadastre_se(self):

        self.rg_frame.pack_forget()    

        self.login_frame.pack(side=RIGHT)
        
def main():
    janela = ctk.CTk()
    app = LoginApp(janela)
    janela.mainloop()

main()