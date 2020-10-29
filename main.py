from parse import get_diffs
from excel import save_excel

path_b2b = input("Inserisci il path della cartella B2B : ")
path_b2b = path_b2b if path_b2b != "" else "./B2B"
path_see = input("Inserisci il path della cartella SEE : ")
path_see = path_see if path_see != "" else "./SEE"

(b2b, see, diff) = get_diffs(path_b2b, path_see)

save_excel(b2b, see, diff)

input("Il file excel e' stato salvato con successo nello stesso path in cui e' stato eseguito il programma.\nPremere invio per terminare...")
