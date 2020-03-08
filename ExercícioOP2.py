EntradaSeg = input('Por favor, entre com o número de segundos que deseja converter: ')
EntradaSegInt = int(EntradaSeg)
saidaDias = int(EntradaSegInt/86400)
saidaHoras = int((EntradaSegInt%86400)/3600)
saidaMinutos = int(((EntradaSegInt%86400)%3600)/60)
saidaSegundos = EntradaSegInt-(saidaDias*86400)-(saidaHoras*3600)-(saidaMinutos*60)
print(str(saidaDias)+' dias, '+str(saidaHoras)+' horas, '+str(saidaMinutos)+' minutos e '+str(saidaSegundos)+' segundos.')

