"""
Questo modulo è il punto di ingresso all'applicazione che gestisce la rubrica.
"""

# importiamo i moduli necessari
import crud
import rubrica
import sys
import validazione

# definiamo la funzione da eseguire in ingresso al programma
def main():
    # preleviamo l'elenco di contatti in rubrica
    elenco = rubrica.leggi()

    try:
        # validiamo gli argomenti forniti dall'utente
        validazione.controllo(sys.argv)
    except ValueError as error:
        # in caso di errore, stampiamo il relativo messaggio
        print(error)
    else:
        # sulla base dell'azione specificata dall'utente, eseguiamo alcune funzioni
        azione = sys.argv[1]
        
        if azione == "stampa":
            crud.stampa(elenco)
        elif azione == "ordina":
            crud.ordina(elenco)
        elif azione == "resetta":
            crud.resetta(elenco)
        elif azione == "aggiungi":
            contatto = {
                "cognome": sys.argv[2],
                "nome": sys.argv[3],
                "cellulare": sys.argv[4]
            }
            crud.aggiungi(contatto, elenco)
        elif azione == "elimina":
            contatto = {
                "cognome": sys.argv[2],
                "nome": sys.argv[3],
                "cellulare": sys.argv[4]
            }
            crud.elimina(contatto, elenco)
        else:
            contatto = {
                "cognome": sys.argv[2],
                "nome": sys.argv[3],
                "cellulare": sys.argv[4]
            }
            modifica_contatto = {
                "cognome": sys.argv[5],
                "nome": sys.argv[6],
                "cellulare": sys.argv[7]
            }
            crud.modifica(contatto, modifica_contatto, elenco)    
    finally:
        # terminiamo il programma trascrivendo il nuovo elenco in rubrica
        rubrica.scrivi(elenco)        

# eseguiamo l'applicazione
if __name__ == "__main__":
    main()
