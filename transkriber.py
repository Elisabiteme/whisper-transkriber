import whisper

# Last inn Whisper-modellen
print("Laster inn modell...")
model = whisper.load_model("small")  # eller "small" hvis du vil ha raskere hastighet

# Sett riktig filsti til lydfilen og transkriber

lydfil = "whisper/MøteAlfred.m4a"
print("Transkriberer lydfilen...")
resultat = model.transcribe(lydfil)

print("Ferdig transkribert!")

# Skriv ut transkripsjon
print(resultat["text"])

# Lagre til fil
with open("transkripsjon.txt", "w", encoding="utf-8") as f:
    f.write(resultat["text"])

print("Ferdig transkribert!")

