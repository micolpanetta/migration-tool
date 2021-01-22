from parse import parse_files
from excel import make_excel

path_b2b = input("Inserisci il path della cartella B2B : ")
path_b2b = path_b2b if path_b2b != "" else "./B2B"
path_see = input("Inserisci il path della cartella SEE : ")
path_see = path_see if path_see != "" else "./SEE"
segment = input("Inserisci il segmento di controllo : ")
segment = segment if segment != "" else "BGM"

(b2b, see, ids) = parse_files(path_b2b, path_see, segment)

make_excel(b2b, see, ids, segment)

input("Il file excel e' stato salvato con successo nello stesso path in cui e' stato eseguito il programma."
      "\nPremere invio per terminare...")
