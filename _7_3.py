import json
import requests
from email.message import EmailMessage
import ssl
andmed = {"nimi": "Anna", "vanus": 25, "abielus": False}
json_string = json.dumps(andmed, indent=2, sort_keys=True)
print(json_string)

with open("andmed.json", "w") as f:
    json.dump(andmed, f)

with open("andmed.json", "r") as f:
    faillist = json.load(f)
print(faillist)

klass = {
"opetaja": "Tamm",
"opilased": [
{"nimi": "Mari", "hinne": 5},
{"nimi": "Juri", "hinne": 4}
] }
with open("andmed.json", "w") as f:
    json.dump(klass, f, indent=2)

linn = input("Город:")
api_voti = "406dcc9420d668aef8f87731cc13779d"
url = f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_voti}&units=metric&lang=et)"

vastus = requests.get(url)
andmed = andmed.json()
if andmed.get("cod") != "404" and "main" in andmed and "wheather" in andmed:
     peamine = andmed["main"]
     temperatuur = peamine["temp"]
     niiskus = peamine["humidity"]
     kirjeldus = andmed["weather"][0]["description"]
     tuul = andmed["wind"]["speed"]
     print(f"Ilm linnas {linn}:")
     print(f"Temperatuur: {temperatuur}C")
     print(f"Kirjeldus: {kirjeldus.capitalize()}")
     print(f"Niiskus: {niiskus}%")
     print(f"Tuule kiirus: {tuul} m/s")
else:
     print("Linna ei leitud. Palun kontrolli nime õigekirja.")
with open("andmed.json", "w", encoding = "utf-8") as f:
    json.dump(andmed, f, indent=4, ensure_ascii= False)

andmed = andmed.json()
with open("andmed.json", "w") as f:
    andmed.json.load(f)
print(andmed)

sisestatud_nimi = input("Sisesta kasutajanimi: ")

if andmed.get("nimi", "Viga") == sisestatud_nimi:
    print(f"\nAutod kasutajal {sisestatud_nimi}")
    for auto in andmed.get("autod", []):
        print(f' - {auto['mark']} {auto['varv']}", {auto["joud"]} hj), number: {auto["number"]}')
else:
    print("Viga")

def load_questions(file_path):
    list = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    question, answer = line.split(":")
                    list[question] = answer
    except FileNotFoundError:
        print(f"Файл {file_path} не найден!")
    return list
    
a = load_questions("C:\Users\opilane.TTHK\source\repos\EldarTARpv24\7,3\questions_answers.txt")
print(a)

def send_mail(email, subject, body):
    """Отправка уведомления на e-mail."""
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465 
    sender_email = "eldar040503@gmail.com"
    sender_password = "wqwp zjly akcd rwyp"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email
    msg.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Teavitus saadetud!")
    except Exception as e:
        print(f"Teavituse saatmine nurjus: {e}")


def loe_kusimused():
    kys_vas = {}
    with open("kusimused_vastused.txt", "r", encoding="utf-8") as f:
        for rida in f:
            if ":" in rida:
                osad = rida.strip().split(":", 1)
                kysimus = osad[0].strip()
                vastus = osad[1].strip()
                kys_vas[kysimus] = vastus
    return kys_vas


def alusta_testi():
    kysimused = loe_kusimused()
    kasutajad = []
    M = 3  
    N = 5  

    for i in range(M):
        print(f"\nTestija {i+1}")
        nimi = input("Sisesta oma nimi (Eesnimi Perenimi): ")
        email = input("Sisesta oma e-posti aadress: ")

        if nimi in kasutajad:
            print("Selle nimega on juba test tehtud.")
            continue
        kasutajad.append(nimi)

        kysimused_list = list(kysimused.items())
        random.shuffle(kysimused_list)
        valitud = kysimused_list[:N]

        oiged = 0
        for kysimus, oige in valitud:
            vastus = input(kysimus + " ")
            if vastus.strip().lower() == oige.lower():
                oiged += 1

        tulemus_rida = nimi + " – " + str(oiged) + " õigesti"

        if oiged >= (N // 2 + 1):
            with open("oiged.txt", "a", encoding="utf-8") as f:
                f.write(tulemus_rida + "\n")
            seis = "Sa sooritasid testi edukalt."
        else:
            with open("valed.txt", "a", encoding="utf-8") as f:
                f.write(nimi + "\n")
            seis = "Kahjuks testi ei sooritatud edukalt."

        with open("koik.txt", "a", encoding="utf-8") as f:
            f.write(nimi + " – " + str(oiged) + " – " + email + "\n")

        subject = "Küsimustiku tulemus"
        body = f"Tere {nimi}!\nSinu õigete vastuste arv: {oiged}.\n{seis}"
        send_email_notification(email, subject, body)

    print("\nKõik testid on tehtud.")
    print("Tulemused saadetud e-posti aadressidele.")


def lisa_kysimus():
    uus = input("Sisesta uus küsimus: ")
    vastus = input("Sisesta õige vastus: ")
    with open("kusimused_vastused.txt", "a", encoding="utf-8") as f:
        f.write(uus + ":" + vastus + "\n")
    print("Küsimus lisatud!")


def menuu():
    while True:
        print("\n1. Alusta küsimustikku")
        print("2. Lisa uus küsimus")
        print("3. Välju")

        valik = input("Vali tegevus (1-3): ")
        if valik == "1":
            alusta_testi()
        elif valik == "2":
            lisa_kysimus()
        elif valik == "3":
            print("Programmist väljutakse.")
            break
        else:
            print("Vale valik. Proovi uuesti.")

menuu()