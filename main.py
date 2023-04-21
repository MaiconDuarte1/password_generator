import customtkinter as ct
import secrets
import string

ct.set_appearance_mode("System")
ct.set_default_color_theme("dark-blue")
janela = ct.CTk()
janela.title("PASSOWORD GENERATOR")
janela.resizable(False, False)
janela.geometry("315x350")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)
janela.iconbitmap("padlock.ico")

tabview = ct.CTkTabview(janela, width=307, height=310)
tabview.grid()
tabview.add("GERADOR DE SENHAS")
tabview.tab("GERADOR DE SENHAS").grid_columnconfigure([0, 1], weight=1)


def gerarsenha():
    itens = (string.ascii_letters + string.digits)
    senha = [secrets.choice(itens) for i in range(int(menu_opcoes.get()))]
    senha = ''.join(senha)
    textbox_senhanova.delete(index1="1.0", index2="end")
    textbox_senhanova.insert(index="1.0", text=senha)


valores = ["1", "2", "3", "4", "5", "6", "7" ,"8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]

label_texto1 = ct.CTkLabel(tabview.tab("GERADOR DE SENHAS"), text="ESCOLHA A QUANTIDADE DE CARACTERES")
label_texto1.grid(row=0, column=1, padx=10, pady=10, columnspan=3)

menu_opcoes = ct.CTkOptionMenu(tabview.tab("GERADOR DE SENHAS"), values=valores)
menu_opcoes.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

botao_gerarsenha = ct.CTkButton(tabview.tab("GERADOR DE SENHAS"), text="GERAR SENHA", command=gerarsenha)
botao_gerarsenha.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

label_senhagerada = ct.CTkLabel(tabview.tab("GERADOR DE SENHAS"), text="SENHA GERADA:")
label_senhagerada.grid(row=3, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

textbox_senhanova = ct.CTkTextbox(tabview.tab("GERADOR DE SENHAS"), width=10, height=10)
textbox_senhanova.grid(row=4, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)



janela.mainloop()