# Logica_Heranca_de_Classes

Exercitando herança - RPG com Sintaxe de Classe
Crie um arquivo main.py e defina as classes a seguir, com seus respectivos atributos e métodos.

Classe Villager
Um Villager (aldeão) tem alguns atributos:

Um name (nome) (string) que deve ser fornecido como parâmetro para o inicializador.
Um health (vida) com um valor inicial 50.
Um defense (defesa) com um valor inicial 0.
Um attack (ataque) com o valor inicial 0.
Um is_alive (está vivo) com o valor inicial True (verdadeiro)
O principal objetivo do Villager é sobreviver e se defender, caso necessário. Ele deve possuir os seguintes métodos de instância:

check_health
Parâmetro(s):
incoming_attack_value: um inteiro não negativo que representa o valor do ataque recebido.
Procedimento(s):
Crie uma lógica em que o ataque recebido é atenuado pela defesa do aldeão. Se sua defesa for maior ou igual ao ataque recebido, ele não perderá vida. Caso contrário, o valor resultante de ataque menos defesa deve ser tirado da vida do aldeão. Se sua vida for menor ou igual a zero, o atributo is_alive deve ser mudado para False e health deve ser zero.
Retorno:
Se o alvo morrer com o ataque, deve retornar a tupla (False, "Target is dead!").
Se sobreviver, deve ser retornado um inteiro representando seu valor restante de vida.
normal_attack
Parâmetro(s):
target: representa o objeto alvo que receberá o ataque.
Procedimento(s):
Crie uma lógica para atacar o alvo. O valor desse ataque deverá ser o mesmo do atributo attack do atacante. O alvo que recebe o ataque deverá perder vida conforme o valor resultante do ataque do atacante menos a defesa do defensor.
Retorno:
Se o alvo morrer com o ataque, deve retornar a tupla (False, "Target is dead!").
Se o alvo continuar vivo após o ataque, deve retornar o valor de vida restante do alvo.
Dica!

Perceba que o método check_health realiza quase todo o procedimento necessário ao método normal_attack.

Classe Mage
Um Mage (mago) herda de Villager, e tem algumas propriedades:

Um name (nome) (string) que deve ser fornecido como parâmetro para o inicializador.
Um attack (ataque) com o valor inicial 10.
Um mana que tem o valor inicial de 100.
Um mago, além das habilidades normais de um aldeão, possui a seguinte habilidade (método) extra:

fire_ball
Parâmetro(s):
target: representa o objeto alvo que receberá o ataque.
Procedimento(s):
Crie uma lógica idêntica à do método normal_attack. A diferença é que o ataque agora consome 20 de energia. Dessa forma deve ocorrer uma verificação se há mana (energia) suficiente para lançar o ataque. Se houver energia suficiente, o ataque deverá ser lançado e o valor de mana deverá ser reduzido em 20. Além disso, o valor gasto de mana deverá ser adicionado como ataque durante o uso da habilidade.
Retorno:
Se o mago não tiver energia suficiente para lançar o ataque, deve retornar a tupla (False, "Not enough mana!")
Se o alvo morrer com o ataque, deve retornar a tupla (False, "Target is dead!").
Se o alvo continuar vivo após o ataque, deve retornar o valor de vida restante do alvo.
Cole o trecho de código abaixo em seu arquivo main.py logo após ter definido as classes Villager e Mage. Depois rode o comando python main.py no terminal e observe se os retornos dos prints estão adequados aos comentários sobre como eles deveriam ser.

if **name** == "**main**":
villager = Villager("Villager")
mage = Mage("Mage")

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 50, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 100}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        "Esperado: 20",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 20, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.normal_attack(villager)

    print(
        "*"*50,
        "Esperado: 10",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 10, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Target is dead!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 0, 'defense': 0, 'attack': 0, 'is_alive': False}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 60}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Target is dead!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        f"Esperado: 40",
        f"Resultado: {mage.mana}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)
    battle_result = mage.fire_ball(villager)
    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Not enough mana!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )
