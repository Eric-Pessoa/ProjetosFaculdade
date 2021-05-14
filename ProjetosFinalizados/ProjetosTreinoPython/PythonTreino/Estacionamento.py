print("Quantos minutos seu veículo ficou estacionado?")

tempo = int(input(""))

print("É um carro ou uma moto?")

Veiculo = input("")

if Veiculo == "Carro" and tempo <= 15:
    print("Você ficou menos de 15 minutos, não precisa pagar")
elif (tempo>15):
    print("sla")
    