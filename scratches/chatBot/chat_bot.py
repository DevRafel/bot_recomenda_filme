import nltk
from nltk.chat.util import Chat, reflections

pares = [
    [
        r"oi|Ola|hey|hello!|blz",
        ["Ola", "oi", "Hey!"]
    ],

    [
        r"Qual e o seu nome?",
        ["Meu nome é Chatbot", "Eu sou o Chatbot"]
    ],

    [
        r"Como posso ajudalo?|Como esta?|Como voce esta?",
        ["Estou bem, obrigado! E voce?", "Estou otimo", "Vou bem"]
    ],

    [
        r"Adeus|tchau|bay|falou|bay bay",
        ["tchau", "Ate mais!", "Ate a proxima"]
    ],
]


def chatbot(keyboardInterrupt=None):
    print("Ola! sou o chatbot. Como posso ajudalo?")
    chat = Chat(pares, reflections)

    while True:
        try:
            resposta = chat.respond(input())
            print(resposta)
            if resposta.lower() == "tchau":
                print("Até logo!")
        except keyboardInterrupt:
            break


chatbot()
