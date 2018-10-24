"""
Questo modulo si occupa di validare gli argomenti forniti dall'utente
attraverso la CLI (Command Line Interface).
"""

def controllo(input):
    """
    Questa funzione valida gli argomenti forniti dall'utente da linea di comando.
    """
    if len(input) not in [2, 5, 8]:
        raise ValueError("[ERROR 1] Il numero di argomenti inserito non è valido.")
    if (len(input) == 2) and (input[1] not in ['stampa', 'ordina', 'resetta']):
        raise ValueError("[ERROR 2] L'azione specificata non è valida. " + 
                         "Digitare una tra le azioni seguenti: stampa, ordina, resetta.")
    if (len(input) == 5) and (input[1] not in ['aggiungi', 'elimina']):
        raise ValueError("[ERROR 3] L'azione specificata non è valida. " + 
                         "Digitare una tra le azioni seguenti: aggiungi, elimina.")
    if (len(input) == 8) and (input[1] not in ['modifica']):
        raise ValueError("[ERROR 2] L'azione specificata non è valida. " + 
                         "Digitare una tra le azioni seguenti: modifica.")
        