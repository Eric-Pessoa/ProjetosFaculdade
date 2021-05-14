print("Contagem de 10 minutos a 0.")
TempoMax = 9
MinuMax = 59
print(TempoMax + 1, ":", "00")
print(TempoMax, ":", MinuMax)
while(TempoMax >= 0):
    MinuMax = MinuMax - 1
    if (MinuMax < 0):
        TempoMax = TempoMax - 1
        MinuMax = 59
    if(TempoMax >= 0):
        print(TempoMax, ":", MinuMax)
print("fim")