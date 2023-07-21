from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from urllib.request import urlopen
from PIL import Image, ImageTk

# importando a função principal

from main import *

# cores -----------

co0 = "#000000"  # preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  #
co6 = "#03091f"  # azul

# Criando janela -------------------

janela = Tk()
janela.title("")
janela.geometry('460x560')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = Style(janela)
style.theme_use("clam")

# Fremes ------------

frameCima = Frame(janela, width=450, height=50, bg=co6, relief="flat", )
frameCima.grid(row=0, column=0)

frameAsk = Frame(janela, width=450, height=60, bg=co1, relief="solid", )
frameAsk.grid(row=1, column=0, padx=5, sticky=NSEW)

frameMeio = Frame(janela, width=450, height=90, bg=co1, relief="solid", )
frameMeio.grid(row=2, column=0, padx=5, sticky=NSEW)

frameBaixo = Frame(janela, width=300, height=460, bg=co1, relief="raised", )
frameBaixo.grid(row=3, column=0, sticky=NSEW)

# Logo -----------------------------------------------

# abrindo imagem
url = "https://cdn-icons-png.flaticon.com/512/6134/6134346.png"

response = urlopen(url)

app_img = Image.open(response)
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_nome = Label(frameCima, text='O chatbot de recommendation de filmes', compound=LEFT, padx=5, relief=FLAT, anchor=NW,
                 font='Verdana, 15', bg=co6, fg=co1)
app_nome.place(x=50, y=7)

l_linha = Label(frameCima, width=450, height=1, anchor=NW, font='Verdana 15', bg=co3, fg=co1)
l_linha.place(x=0, y=47)

# Pergunta ----------------------------------------------

app_pergunta = Label(frameAsk, text='Olá! Sou um chatbot de sugestões de filmes. Como você está se sentindo hoje?',
                     width=45, height=2, wraplength=320, justify='center', compound=CENTER, padx=5, relief=FLAT,
                     anchor=NW, font=('Verdana', 11), bg=co1, fg=co0)
app_pergunta.grid(row=0, column=0, padx=10, pady=10)

l_linha = Label(frameAsk, width=450, height=1, anchor=NW, font='Verdana 15', bg=co3, fg=co1)
l_linha.place(x=0, y=57)


# função resultado

def resultado(i):
    global capa_1, capa_2, capa_3

    # filmes sugeridos
    sugeridos = suggest_movies(i)

    titlos = sugeridos[0]
    poster = sugeridos[1]
    data = sugeridos[2]
    votos = sugeridos[3]

    # limpando o frame baixo
    for widget in frameBaixo.winfo_children():
        widget.destroy()

        # ------------------- Criando frame para cada filme

        # filme 1
        frame_1 = Frame(frameBaixo, width=150, height=400, bg=co1, )
        frame_1.grid(row=0, column=0, sticky=NSEW, pady=5)

        # nome
        nome = Label(frame_1, text=f'{titlos[0]}', height=2, padx=10, wraplength=100, justify='left', pady=5, relief=SOLID, anchor=NW,
                     font='Ivy, 9 bold', bg=co1, fg=co0, bd=1, highlightbackground='white')
        nome.place(x=7, y=260)


# Frame Meio --------------------------------------------

b_1 = Button(frameMeio, command=lambda: resultado('OK'), compound=LEFT, width=17, text='OK', bg=co1, fg=co0,
             font='Ivy, 10', overrelief=RIDGE)
b_1.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)

b_2 = Button(frameMeio, command=lambda: resultado('Anger'), compound=LEFT, width=17, text='Anger', bg=co1, fg=co0,
             font='Ivy, 10', overrelief=RIDGE)
b_2.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)

b_3 = Button(frameMeio, command=lambda: resultado('heppy'), compound=LEFT, width=17, text='heppy', bg=co1, fg=co0,
             font='Ivy, 10', overrelief=RIDGE)
b_3.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2)

b_4 = Button(frameMeio, command=lambda: resultado('gratitude'), compound=LEFT, text='gratitude', bg=co1, fg=co0,
             font='Ivy, 10', overrelief=RIDGE)
b_4.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2)

b_5 = Button(frameMeio, command=lambda: resultado('sad'), compound=LEFT, text='sad', bg=co1, fg=co0, font='Ivy, 10',
             overrelief=RIDGE)
b_5.grid(row=1, column=1, sticky=NSEW, pady=2, padx=2)

b_6 = Button(frameMeio, command=lambda: resultado('good'), compound=LEFT, width=17, text='good', bg=co1, fg=co0,
             font='Ivy,10', overrelief=RIDGE)
b_6.grid(row=1, column=2, sticky=NSEW, pady=2, padx=2)

janela.mainloop()
