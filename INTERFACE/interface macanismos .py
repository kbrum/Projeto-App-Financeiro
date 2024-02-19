import customtkinter as ctk

janela = ctk.CTk()

janela.title("APP")
janela.geometry("800x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)
janela._set_appearance_mode("dark")

frame1 = ctk.CTkFrame(master= janela, width=150, height=380, fg_color = "grey", bg_color="grey").place(x=10, y=10)

frame2 = ctk.CTkFrame(janela, width=525, height=380, fg_color = "grey", bg_color="grey").place(x=165, y=10)

def nova_janela(): 
    nova_janela = ctk.CTkToplevel(janela)
    nova_janela.geometry("200x200")


btn_novajanela = ctk.CTkButton(master=janela, text="abrir nova janela", command=nova_janela).place(x=350, y=100)

tabview = ctk.CTkTabview(janela, width=0, height=370, corner_radius=15)
tabview.place(x=15,y=15)
tabview.add(" > Configurações").grid(column=0, row=0)
tabview.add(" > Segurança").grid(column=0, row=0)
tabview.add(" > Documentos").grid(column=0, row=0)
tabview.add(" > Open Finance").grid(column=0, row=0)
tabview.tab(" > Configurações").grid_columnconfigure(0, weight=1)
tabview.tab(" > Segurança").grid_columnconfigure(0, weight=1)
tabview.tab(" > Documentos").grid_columnconfigure(0, weight=1)
tabview.tab(" > Open Finance").grid_columnconfigure(0, weight=1)

text = ctk.CTkLabel(tabview.tab(" > Configurações"), text="CONFIGRAR CARTÃO\nCONFIGURAR CONTA\nEDITAR DADOS DO PERFIL").place(x=10, y=10)
text = ctk.CTkLabel(tabview.tab(" > Segurança"), text="ALTERAR SENHA DE ACESSO").place(x=10, y=10)
text = ctk.CTkLabel(tabview.tab(" > Documentos"), text="EXTRATO DA CONTA").place(x=10, y=10)
text = ctk.CTkLabel(tabview.tab(" > Open Finance"), text="TRANSFERÊNCIAS").place(x=10, y=10)


janela.mainloop()
