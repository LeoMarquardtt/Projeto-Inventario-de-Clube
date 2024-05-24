from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from view import *
from tkinter import filedialog as fd

#Cores
cor0 = '#2e2d2b' # Cinza Escuro
cor1 = '#feffff' # Branco
cor2 = '#4fa882' # Verde Agua
cor3 = '#38576b' # Azul
cor4 = '#403d3d' # Preto
cor5 = '#e06636' # Laranja
cor6 = '#038cfc' # Azul Claro
cor7 = '#3fbfb9' # Verde Claro
cor8 = '#263238' # Azul Escuro
cor9 = '#e9edf5' # Cinza Claro


#Janela
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=cor9)
janela.resizable(width=False, height=False)
style = ttk.Style(janela)
style.theme_use('clam')


#Cabecario

frameCabecario = Frame(janela, width=1040, height=60, bg=cor1, relief=FLAT)
frameCabecario.grid(row=0, column=0)

#Corpo

frameCorpo = Frame(janela, width=1040, height=300, bg=cor1, pady=20, relief=FLAT)
frameCorpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#Tabela
frametabela = Frame(janela, width=1040, height=300, bg=cor1, relief=FLAT)
frametabela.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#Funcoes

global tree

#Função Inserir

def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    posicao = e_posicao.get()
    numero = e_num.get()
    lugar_nasc = e_nasc.get()
    data = e_data.get()
    fim_ctt = e_fim_ctt.get()
    valor = e_valor.get()
    imagem = imagem_string

    lista_inserir = [nome, posicao, numero, lugar_nasc, data, fim_ctt, valor, imagem]
    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_posicao.delete(0, 'end')
    e_num.delete(0, 'end')
    e_nasc.delete(0, 'end')
    e_data.delete(0, 'end')
    e_fim_ctt.delete(0, 'end')
    e_valor.delete(0, 'end')

    mostrar()

#Função Atualizar

def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_posicao.delete(0, 'end')
        e_num.delete(0, 'end')
        e_nasc.delete(0, 'end')
        e_data.delete(0, 'end')
        e_fim_ctt.delete(0, 'end')
        e_valor.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_posicao.insert(0, treev_lista[2])
        e_num.insert(0, treev_lista[3])
        e_nasc.insert(0, treev_lista[4])
        e_data.insert(0, treev_lista[5])
        e_fim_ctt.insert(0, treev_lista[6])
        e_valor.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]

        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            posicao = e_posicao.get()
            numero = e_num.get()
            lugar_nasc = e_nasc.get()
            data = e_data.get()
            fim_ctt = e_fim_ctt.get()
            valor = e_valor.get()
            imagem = imagem_string

            if imagem == '':
                imagem = e_fim_ctt.insert(0, treev_lista[7])

            lista_atualizar = [nome, posicao, numero, lugar_nasc, data, fim_ctt, valor, imagem,id]

            for i in lista_atualizar:
                if i =='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
            atualizar_(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_posicao.delete(0, 'end')
            e_num.delete(0, 'end')
            e_nasc.delete(0, 'end')
            e_data.delete(0, 'end')
            e_fim_ctt.delete(0, 'end')
            e_valor.delete(0, 'end')

            b_confirmar.destroy

            mostrar()

        
        b_confirmar = Button(frameCorpo,command=update, width=13, text='CONFIRMAR', overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor2, fg=cor1)
        b_confirmar.place(x=330, y=190)
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')



#Função Deletar

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados deletados com sucesso')

        mostrar()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')


#Função Escolher Imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem
    #Abrindo Imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((160,160))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameCorpo, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=700, y=0)

#Função Ver Imagem

def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]
    
    item = ver_item(valor)
    imagem = item[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((160,160))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameCorpo, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=700, y=10)



#Cabecario

#Abrindo imagem
app_img = Image.open('prancheta.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameCabecario, image=app_img, text=' Inventário de Clube', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=cor1, fg=cor4)
app_logo.place(x=0, y=0)


#Corpo

#Entradas
l_nome = Label(frameCorpo, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameCorpo, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=12)

l_posicao = Label(frameCorpo, text='Posição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_posicao.place(x=10, y=40)
e_posicao = Entry(frameCorpo, width=30, justify='left', relief=SOLID)
e_posicao.place(x=130, y=42)

l_num = Label(frameCorpo, text='Numero', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_num.place(x=10, y=70)
e_num = Entry(frameCorpo, width=30, justify='left', relief=SOLID)
e_num.place(x=130, y=72)

l_nasc = Label(frameCorpo, text='Nacionalidade', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_nasc.place(x=10, y=100)
e_nasc = Entry(frameCorpo, width=30, justify='left', relief=SOLID)
e_nasc.place(x=130, y=102)

l_data = Label(frameCorpo, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_data.place(x=10, y=130)
e_data = DateEntry(frameCorpo, width=12, bordewidth=2, year=2024)
e_data.place(x=130, y=132)

l_fim_ctt = Label(frameCorpo, text='Fim do contrato', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_fim_ctt.place(x=10, y=160)
e_fim_ctt = DateEntry(frameCorpo, width=12, bordewidth=2, year=2024)
e_fim_ctt.place(x=130, y=162)

l_valor = Label(frameCorpo, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_valor.place(x=10, y=190)
e_valor = Entry(frameCorpo, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=192)

#Botões

#Botão Imagem
l_img = Label(frameCorpo, text='Foto do Jogador', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
l_img.place(x=10, y=222)
b_img = Button(frameCorpo,command=escolher_imagem , width=29, text='CARREGAR', compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_img.place(x=130, y=222)

#Botão Inserir
img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
b_add = Button(frameCorpo,command=inserir, image=img_add, width=95, text='  ADICIONAR', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_add.place(x=330, y=10)

#Botão Atualizar
img_att = Image.open('att.png')
img_att = img_att.resize((20,20))
img_att = ImageTk.PhotoImage(img_att)
b_att = Button(frameCorpo,command=atualizar, image=img_att, width=95, text='  ATUALIZAR', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_att.place(x=330, y=50)

#Botão Deletar
img_del = Image.open('del.png')
img_del = img_del.resize((20,20))
img_del = ImageTk.PhotoImage(img_del)
b_del = Button(frameCorpo,command=deletar , image=img_del, width=95, text='  DELETAR', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_del.place(x=330, y=90)

#Botão Ver Item
img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)
b_item = Button(frameCorpo,command=ver_imagem, image=img_item, width=95, text='  VER JOGADOR', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=cor1, fg=cor0)
b_item.place(x=330, y=222)

#Labels Qtd e Valores
l_total = Label(frameCorpo, text='', width=14, height=2, anchor=CENTER, font=('Ivy 18 bold'), bg=cor7, fg=cor1)
l_total.place(x=450, y=17)
l_total_ = Label(frameCorpo, text='      VALOR TOTAL DO CLUBE      ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor7, fg=cor1)
l_total_.place(x=450, y=12)

l_qtd = Label(frameCorpo, text='', width=14, height=2,pady=5, anchor=CENTER, font=('Ivy 18 bold'), bg=cor7, fg=cor1)
l_qtd.place(x=450, y=90)
l_qtd_ = Label(frameCorpo, text='   QUANTIDADE DE JOGADORES  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor7, fg=cor1)
l_qtd_.place(x=450, y=92)

#Tabela de itens

def mostrar():
    global tree

    #Cabecario da Tabela
    tabela_head = ['#Item','Nome',  'Posição','Número', 'Nacionalidade', 'Data da compra', 'Fim do Contrato','Valor da compra']

    lista_itens = ver_form()

    tree = ttk.Treeview(frametabela, selectmode="extended",columns=tabela_head, show="headings")

    #Barra Vertical
    vsb = ttk.Scrollbar(frametabela, orient="vertical", command=tree.yview)
    #Barra Horizontal
    hsb = ttk.Scrollbar(frametabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frametabela.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,120,120,120,120,120,120,120]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    #Inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []
    for iten in lista_itens:
        quantidade.append(float(iten[7]))

    Total_valor = float(0)
    for item in quantidade:
        Total_valor += item
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()


janela.mainloop()