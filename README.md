# Oblig2 Develop and test a web server

Oppgave 2

2.1 Testing with a webserver 
Filen navn:simple-webserver
I denne oppgaven lagde er http server ved hjelp av socket. Den tar imot en klient om gangen. Den leser en forespørsel og retunere index.filen. hvis den ikke finnes retuneren den 404 Not found. har lagt inn bilde av begge

Hvordan jeg kjørte koden:
  - py simple-webserver.py: starter serverren
  - py client.py -i 127.0.0.1 -p 8000 -f index.html


2.2
fil jeg brukte: client.py
i denne oppgaen lagde jeg HTTP cleint som tester serveren. den kobler til webserveren over TCP. den bruker argparse til å ta inn IP og port. la inn bilde 

Hvordan jeg kjørte koden:
  - python3 client.py -i 127.0.0.1 -p 8000 -f index.html


Oppgave 3 Making a multi-threaded web server

i denne oppgaven lagde jeg en webserver som støtter flere samtidige klienter ved bruk av threading. det blir lagd en ny thread hver gang en ny klient kobler seg til. la til bilde av flere thread som kjører

Hvordan jeg kjørte koden:
  - py multithreaded-webserver.py


 Oppgave 4: Testing i mininet

 filene jeg brukte:

i denne oppgaven kjører jeg en server og web klient ved hjlep av Mininet. la til bilde 


Hvordan jeg kjørte koden:

  -sudo python3 simpletopo.py: åpner minni
  - xterm h1 h3 r2: åpner terminal for hestene
  - sudo python3 webserver.py
    




  









