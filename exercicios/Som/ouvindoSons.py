import pyaudio as pa
import speech_recognition as sr

notas = {
    0: {
        "Data",
        "Nome da Nota",

    },
}

def ouvirAudio():
    #Habilita o Microfone para ser utilizado
    microfone = sr.Recognizer()

    #Usando microfone
    with sr.Microphone() as source:
        #Reduz os ruidos recebidos no audio
        #microfone.adjust_for_ambient_noise(source)

        #Armazena o que foi recebido
        audio = microfone.listen(source)
    try:
        notas["nota"] = ["Dó", audio]
        continuar = True
    except sr.UnknownValueError:
        print("Desculpa, mas você tem que afinar esse som")
        continuar = False
    return continuar
def falarNota():
    nome="Tentando identificar"

    #Habilita o Microfone para ser utilizado
    microfone = sr.Recognizer()

    #Usando microfone
    with sr.Microphone() as source:
        #Reduz os ruidos recebidos no audio
        #microfone.adjust_for_ambient_noise(source)

        #Armazena o que foi recebido
        audio = microfone.listen(source)
    try:
        for a in notas["nota"]:
            if(notas[a] == audio):
                nome = "Dó"
            else:
                nome = "Afine essa nota ai"
    except sr.UnknownValueError:
        print("Desculpa, mas você tem que afinar esse som")
    return nome;
def menu():
    menu = int(input(" _______ MENU ________ "
                 "\n1 - Ouvir som"
                 "\n2 - Falar som/"
                 "\n3 - Sair"
                 "\n -> "
    ))
    respostaMenu(menu)
def respostaMenu(menu):
    if (menu == 1):
        print("Ouvindo o som . . . \n")
        continuar = ouvirAudio()
        if(continuar == True):
            menu()
        else:
            print("Não conseguimos identificar a nota!")
    elif(menu == 2):
        print("Acho que você falou . . .\n")
        print(falarNota())
    else:
        print("Tchau, até a próxima. . . ")

#menu()

notas[1] = ("Dó", 1123)
notas[2] = ("Ré", 1234)
print(notas)

for n in notas:
    print(notas[n])

p = pa.PyAudio()

