import speedtest

test = speedtest.Speedtest()

# Faz o teste de Download e converte em mb/s
down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e6)
# Faz o teste de Upload e converte em mb/s
upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e6)
# Mostra o resultado
print(f"Sua Velocidade de Download é {fDown} mb/s")
print(f"Sua Velocidade de Upload é {fUp} mb/s")
