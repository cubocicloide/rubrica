"""
Questo modulo si occupa di leggere e scrivere dati sul file rubrica.json
"""

# importo il modulo json necessario caricare i dati contenuti in rubrica.json
import json

# path dove è ubicato il file di rubrica (i.e., rubrica.json)
RUBRICA = './rubrica.json'

def leggi():
    """
    Questa funzione si occupa di leggere il contenuto della RUBRICA
    """
    with open(RUBRICA) as json_data:
        elenco = json.load(json_data)
    return elenco

def scrivi(elenco):
    """
    Questa funzione si occupa di scrivere sulla RUBRICA
    """
    with open(RUBRICA, 'w') as outfile:  
        json.dump(elenco, outfile)

# testiamo il modulo
if __name__=="__main__":

    # preleviamo l'elenco dei contatti dalla RUBRICA
    elenco = leggi()

    # aggiungiamo un nuovo contatto nell'elenco
    contatto = { "nome": "Biagio",
                 "cognome": "Faleni",
                 "cellulare": 3387985594 }
    elenco["contatti"].append(contatto)

    # stampiamo il nuovo elenco di contatti
    print(elenco["contatti"])

    # scriviamo il nuovo elenco nella RUBRICA
    scrivi(elenco)
