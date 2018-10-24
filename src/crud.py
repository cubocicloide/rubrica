"""
Questo modulo implementa le funzionalità CRUD (Create Read Update Delete) della rubrica.
"""

def aggiungi(contatto, elenco):
    """
    Questa funzione si occupa di aggiungere un contatto in rubrica.
    """
    elenco["contatti"].append(contatto)

def modifica(contatto, modifica_contatto, elenco):
    """
    Questa funzione si occupa di modificare un contatto della rubrica.
    """
    for i in range(len(elenco["contatti"])):
        if elenco["contatti"][i] == contatto:
            elenco["contatti"][i] = modifica_contatto
            break

def elimina(contatto, elenco):
    """
    Questa funzione si occupa di eliminare un contatto dalla rubrica.
    """
    for utente in elenco["contatti"]:
        if utente == contatto:
            elenco["contatti"].remove(utente)
            break

def ordina(elenco):
    """
    Questa funzione si occupa di ordinare alfabeticamente i contatti della rubrica.
    """
    nominativi = []
    for i in range(len(elenco["contatti"])):
        _i = elenco["contatti"][i]["cognome"] + ' ' + \
             elenco["contatti"][i]["nome"] + ' ' + \
             str(elenco["contatti"][i]["cellulare"])
        nominativi.append(_i)
    nominativi.sort()
    _ = []
    for i in range(len(nominativi)):
        for j in range(len(elenco["contatti"])):
            _j = elenco["contatti"][j]["cognome"] + ' ' + \
                 elenco["contatti"][j]["nome"] + ' ' + \
                 str(elenco["contatti"][j]["cellulare"])
            if _j == nominativi[i]:
                _.append(elenco["contatti"][j])
    elenco["contatti"] = _

def stampa(elenco):
    """
    Questa funzione si occupa di stampare i contatti della rubrica.
    """
    print('-'*50)
    print('COGNOME | NOME | CELLULARE')
    print('-'*50)
    for utente in elenco["contatti"]:
        print(utente["cognome"] + ' | ' + 
              utente["nome"] + ' | ' + 
              str(utente["cellulare"]))
    print('-'*50)

def resetta(elenco):
    """
    Questa funzione si occupa di eliminare tutti i contatti dalla rubrica.
    """
    elenco["contatti"].clear()

# testiamo il modulo
if __name__=="__main__":
    # importiamo i moduli di cui abbiamo bisogno
    import rubrica

    # preleviamo l'elenco dalla rubrica
    elenco = rubrica.leggi()

    # lo resettiamo a fini di verifica
    resetta(elenco)

    # aggiungiamo un nuovo contatto nell'elenco
    contatto = { 
        "cognome": "Faleni",
        "nome": "Biagio",
        "cellulare": 0000000000 
    }
    aggiungi(contatto, elenco)

    # lo modifichiamo
    modifica_contatto = { "cognome": "Faleni",
                          "nome": "Biagio",
                          "cellulare": 3381485594 }
    modifica(contatto, modifica_contatto, elenco)

    # aggiungiamo nuovi contatti
    contatto_1 = { 
        "cognome": "Zaniolo",
        "nome": "Marco",
        "cellulare": 3312630594 
    }
    contatto_2 = {
        "cognome": "Zaniolo",
        "nome": "Aldo",
        "cellulare": 3387984725 
    }
    contatto_3 = { 
        "cognome": "Baracca",
        "nome": "Angela",
        "cellulare": 3321649594 
    }
    contatto_4 = { 
        "cognome": "Verde",
        "nome": "Daniela",
        "cellulare": 3339540594 
    }
    aggiungi(contatto_1, elenco)
    aggiungi(contatto_2, elenco)
    aggiungi(contatto_3, elenco)
    aggiungi(contatto_4, elenco)

    # eliminiamo un contatto
    elimina(contatto_3, elenco)

    # ordiniamo i contatti inseriti
    ordina(elenco)

    # stampiamo l'elenco di contatti ottenuto
    stampa(elenco)

    # scriviamo il nuovo elenco nella rubrica
    rubrica.scrivi(elenco)
