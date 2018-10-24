# Rubrica

Questa semplice applicazione si occupa di gestire una rubrica telefonica tramite linea di comando.
L'applicazione è stata implementata come esercitazione nell'ambito del corso coding4math, facente parte del Programma Operativo Nazionale (PON) 2014-2020. L'intera documentazione del corso è reperibile al seguente link: [docs].

---
## Istruzioni per l'uso
Scaricare l'archivio dal link di [download], e poi estrarlo. Avremo allora il seguente file system relativo al repository scaricato:

```
Download
|__rubrica-master
   |__rubrica-master
      |__src
         |__.DS_Store
         |__crud.py
         |__main.py
         |__rubrica.json
         |__rubrica.py
         |__validazione.py
```

A questo punto, aprire il terminal (su MacOS) o il command prompt (su Windows) e recarsi presso la cartella <code>src</code>. Assicurandosi di avere installato sul dispositivo l'interprete Python 3, potrete stampare la rubrica mediante il comando:

```
src > python main.py stampa
```

Per aggiungere un contatto utilizzare la sintassi

```
src > python main.py aggiungi cognome nome cellulare
```

Per modificare un contatto:

```
src > python main.py modifica cognome nome cellulare nuovo_cognome nuovo_nome nuovo_cellulare
```

Per eliminare un contatto:

```
src > python main.py elimina cognome nome cellulare
```

Per ordinare l'elenco dei contatti:

```
src > python main.py ordina
```

Per eliminare tutti i contatti:

```
src > python main.py resetta
```

[docs]:https://cubocicloide.github.io/coding4math/
[download]:https://github.com/cubocicloide/rubrica/archive/master.zip