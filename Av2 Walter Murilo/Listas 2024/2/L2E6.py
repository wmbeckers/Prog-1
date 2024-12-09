capacidade_tanque = float(input("Informe a capacidade total do tanque de combustível (em litros): "))
consumo_veiculo = float(input("Informe o consumo do veículo (em km/l): "))
distancia_viagem = float(input("Informe a distância da viagem (em km): "))

autonomia_veiculo = capacidade_tanque * consumo_veiculo

if distancia_viagem <= autonomia_veiculo:
    print("É possível realizar a viagem sem a necessidade de abastecer.")
else:
    print("Não é possível realizar a viagem sem a necessidade de abastecer.")
