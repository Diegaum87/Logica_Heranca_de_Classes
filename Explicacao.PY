class Villager:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True
# A linha class Villager: define uma classe chamada "Villager" que representa um personagem do jogo.
# A função __init__(self, name) é um método especial que é executado automaticamente quando um novo objeto da classe é criado. Ele inicializa os atributos do objeto, como nome, saúde, defesa, ataque e estado de vida.
# self.name = name atribui o valor do parâmetro name ao atributo name do objeto.
# self.health = 50 define o atributo health com o valor inicial de 50.
# self.defense = 0 define o atributo defense com o valor inicial de 0.
# self.attack = 0 define o atributo attack com o valor inicial de 0.
# self.is_alive = True define o atributo is_alive como True, indicando que o personagem está vivo.



    def check_health(self, incoming_attack_value):
        damage = incoming_attack_value - self.defense
        self.health -= damage
        self.health = self.health if self.health > 0 else 0
        if not self.health:
            self.is_alive = False
            return (False, "Target is dead!")
        return self.health
# A função check_health(self, incoming_attack_value) verifica a saúde do personagem após um ataque recebido.
# damage = incoming_attack_value - self.defense calcula o dano causado ao personagem subtraindo a defesa do ataque recebido.
# self.health -= damage diminui a saúde do personagem pelo valor do dano.
# self.health = self.health if self.health > 0 else 0 verifica se a saúde é maior que 0 e, se não for, define-a como 0. Isso garante que a saúde não seja um valor negativo.
# O bloco if not self.health: verifica se a saúde é igual a 0. Se for, o personagem é considerado morto.
# self.is_alive = False define o atributo is_alive como False para indicar que o personagem está morto.
# Retorna uma tupla (False, "Target is dead!") indicando que o personagem alvo está morto.
# Se o personagem ainda estiver vivo, retorna o valor atual da saúde.



    def normal_attack(self, target):
        return target.check_health(self.attack)
# A função normal_attack(self, target) realiza um ataque normal ao personagem target.
# Chama o método check_health() do objeto target, passando o valor de self.attack como parâmetro.
# Retorna o resultado da função check_health(), que será a saúde atualizada do personagem target após o ataque.



class Mage(Villager):
    def __init__(self, name):
        super().__init__(name)
        self.attack = 10
        self.mana = 100
# A classe Mage é uma subclasse da classe Villager, herdando seus atributos e métodos.
# O método __init__(self, name) da subclasse é sobrescrito para adicionar novos atributos específicos dos magos.
# A chamada super().__init__(name) chama o método __init__() da superclasse Villager para inicializar os atributos herdados.
# self.attack = 10 define o atributo attack do mago como 10, substituindo o valor padrão da superclasse.
# self.mana = 100 define o atributo mana do mago como 100.



    def fire_ball(self, target):
        mana_spend = 20
        if self.mana < mana_spend:
              return (False, "Not enough mana!")
        self.mana -= mana_spend
        damage = self.attack + mana_spend
        return target.check_health(damage)
# A função fire_ball(self, target) realiza um ataque especial de bola de fogo ao personagem target.
# mana_spend = 20 define o custo de mana para usar o ataque de bola de fogo.
# O bloco if self.mana < mana_spend: verifica se o mago tem mana suficiente para realizar o ataque.
# Se o mago não tiver mana suficiente, retorna a tupla (False, "Not enough mana!") indicando que não há mana suficiente.
# Caso contrário, o ataque é realizado. self.mana -= mana_spend subtrai o custo de mana do mago.
# damage = self.attack + mana_spend calcula o dano do ataque, somando o valor de ataque do mago com o custo de mana gasto.
# Retorna o resultado da função check_health() do objeto target com o dano calculado.
# No bloco if __name__ == "__main__": e nos prints subsequentes, estão sendo realizados testes e exibição dos resultados esperados e obtidos para ilustrar o funcionamento do código.