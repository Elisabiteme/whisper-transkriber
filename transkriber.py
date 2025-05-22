
import whisper

print("Laster inn modell...")
model = whisper.load_model("small")

lydfil = "mitt_møte.m4a"  # Endre til din faktiske fil

print("Transkriberer lydfilen...")
resultat = model.transcribe(lydfil)

print("Ferdig transkribert!")

with open("transkripsjon.txt", "w", encoding="utf-8") as f:
    f.write(resultat["text"])

print("Transkripsjon lagret i transkripsjon.txt")
