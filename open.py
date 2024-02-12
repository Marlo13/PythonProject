FILE_PATH = 'requirements.txt'

f = open(FILE_PATH,'r', encoding='utf-8', newline='')


for line in f:
    print(line.strip(), end='')
    f.close()

f.close()
try: 
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write("Is this the real life?\n")
        f.write("Is this just fantasy?")
except Exception:
    print("Voici l'erreur", Exception)