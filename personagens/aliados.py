from funções.functions import CalculoDanoFisico, CalculoDanoMagico


class Mago:
    def __init__(self, nome, vida, manaVariavel, manaMaxima, danoFisico, danoMagico, defesaFisica, defesaMagica, agilidade):
        self.nome = nome
        self.vida = vida
        self.manaV = manaVariavel
        self.manaM = manaMaxima
        self.danoF = danoFisico
        self.danoM = danoMagico
        self.defesaF = defesaFisica
        self.defesaM = defesaMagica
        self.agilidade = agilidade
        self.ataqueEspecial = "Bola de Fogo"
        
    def __str__(self):
        return f''
    
    def ataque1(self, inimigo):
        print(f"{self.nome} bateu no inimigo com seu cajado causando {CalculoDanoFisico(self.danoF, inimigo.defesaF)} de dano") 
        if self.manaV < self.manaM:
            self.manaV += 2
            if self.manaV > self.manaM:
                self.manaV = self.manaM

    def defesa(self):
        print(f"{self.nome} se defendeu com magia de proteção")
        self.defesaF = self.defesaF * 2
        self.defesaM = self.defesaM * 2
        if self.manaV < self.manaM:
            self.manaV += 2
            if self.manaV > self.manaM:
                self.manaV = self.manaM

    def ataque2(self, inimigo):
        if self.manaV >= 6:
            print(f"{self.nome} jogou uma bola de fogo no inimigo causando {CalculoDanoMagico(self.danoM, inimigo.defesaM)}") 
            self.manaV -= 6

class Ladino:
    def __init__(self, nome, vida, manaVariavel, manaMaxima, danoFisico, danoMagico, defesaFisica, defesaMagica, agilidade):
        self.nome = nome
        self.vida = vida
        self.manaV = manaVariavel
        self.manaM = manaMaxima
        self.danoF = danoFisico
        self.danoM = danoMagico
        self.defesaF = defesaFisica
        self.defesaM = defesaMagica
        self.agilidade = agilidade
        self.ataqueEspecial = "Ataque das Sombras"       

    def __str__(self):
        return f''

    def ataque1(self, inimigo):
        print(f'{self.nome} atacou o inimigo com sua adaga, assim causando {CalculoDanoFisico(self.danoF, inimigo.defesaF)}') 
        if self.manaV < self.manaM:
            self.manaV += 1

    def defesa(self):
        print(f"{self.nome} ficou em posicao defensiva")
        self.defesaF = self.defesaF * 2
        self.defesaM = self.defesaM * 2
        if self.manaV < self.manaM:
            self.manaV += 2
            if self.manaV > self.manaM:
                self.manaV = self.manaM

    def ataque2(self, inimigo):
        if self.manaV >= 4:
         print(f"{self.nome} atacou o inimigo pelas costas, causando {CalculoDanoFisico(self.danoF + 10, inimigo.defesaM)} de dano") 

class Paladino:
    def __init__(self, nome, vida, manaVariavel, manaMaxima, danoFisico, danoMagico, defesaFisica, defesaMagica, agilidade):
        self.nome = nome
        self.vida = vida
        self.manaV = manaVariavel
        self.manaM = manaMaxima
        self.danoF = danoFisico
        self.danoM = danoMagico
        self.defesaF = defesaFisica
        self.defesaM = defesaMagica
        self.agilidade = agilidade
        self.ataqueEspecial = "Benção Divina"

    def ataque1(self, inimigo):
        print(f"{self.nome} atacou o inimigo com seu martelo, causando {CalculoDanoFisico(self.danoF, inimigo.defesaF)}")
        if self.manaV < self.manaM:
            self.manaV += 2
            if self.manaV > self.manaM:
                self.manaV = self.manaM


    def defesa(self):
        print(f"{self.nome} posicionou seu escudo a frente")
        self.defesaF = self.defesaF * 2
        self.defesaM = self.defesaM * 2
        if self.manaV < self.manaM:
            self.manaV += 2
            if self.manaV > self.manaM:
                self.manaV = self.manaM

    def ataque2(self, inimigo = None):
        if self.manaV >= 4:
            print(f"{self.nome} rezou para os deuses o ajudarem")
            print(f"Seus status de defesa fisica e magica aumentaram")
            self.defesaF += 5
            self.defesaM += 5
            self.manaV -= 4

class Sacerdote:
    def __init__(self, nome, vida, manaVariavel, manaMaxima, danoFisico, danoMagico, defesaFisica, defesaMagica, agilidade):
        self.nome = nome
        self.vida = vida
        self.manaV = manaVariavel
        self.manaM = manaMaxima
        self.danoF = danoFisico
        self.danoM = danoMagico
        self.defesaF = defesaFisica
        self.defesaM = defesaMagica
        self.agilidade = agilidade
        self.ataqueEspecial = "Cura Superior"

    def ataque1(self, inimigo):
        print(f"{self.nome} invocou a luz divina para queimar seus inimigos")
        print(f"Luz divina causou {CalculoDanoMagico(self.danoM, inimigo.defesaM)}") 
        if self.manaV < self.manaM:
            self.manaV += 3
            if self.manaV > self.manaM:
                self.manaV = self.manaM

    def defesa(self):
        print(f"{self.nome} foi agraciado com a proteção dos deuses")
        self.defesaF = self.defesaF * 2
        self.defesaM = self.defesaM * 2
        if self.manaV < self.manaM:
            self.manaV += 3
            if self.manaV > self.manaM:
                self.manaV = self.manaM

    def ataque2(self, inimigo = None):
        if self.manaV >= 5:
            print(f"{self.nome} utiliza sua fé para fortalecer seus aliados e a si")
            self.vida += 5
            self.manaV -= 5

class Caçador:
    def __init__(self, nome, vida, manaVariavel, manaMaxima, danoFisico, danoMagico, defesaFisica, defesaMagica, agilidade):
        self.nome = nome
        self.vida = vida
        self.manaV = manaVariavel
        self.manaM = manaMaxima
        self.danoF = danoFisico
        self.danoM = danoMagico
        self.defesaF = defesaFisica
        self.defesaM = defesaMagica
        self.agilidade = agilidade
        self.ataqueEspecial = "Caçar"

    def ataque(self, inimigo):
        print(f"{self.nome} usa sua besta para atirar no inimigo, a flecha causa {CalculoDanoFisico(self.danoF, inimigo.defesaF)}")
        if self.manaV < self.manaM:
            self.manaV += 2
            if self.manaV > self.manaM:
                self.manaV = self.manaM


    def defesa(self):
        print(f"{self.nome} utiliza o ambiente para se proteger")
        self.defesaF = self.defesaF * 2
        self.defesaM = self.defesaM * 2
        if self.manaV < self.manaM:
            self.manaV += 2
            if self.manaV > self.manaM:
                self.manaV = self.manaM

    def ataque2(self, inimigo):
        if self.manaV >= 6:
            print(f"{self.nome} usa sua besta para caçar todos os inimigos")
            print(f"Caçar causa {CalculoDanoFisico(self.danoF + 4, inimigo.defesaF)}")
            self.manaV -= 6


JMago = Mago("BigodinhoA", 50, 15, 15, 6, 15, 2, 3, 5)

JLadino = Ladino("VitorA", 45, 10, 10, 10, 0, 2, 2, 20)

JPaladino = Paladino("MikaA", 80, 16, 16, 6, 6, 5, 5, 7)

JSacerdote = Sacerdote("DalilaA", 50, 18, 18, 2, 7, 3, 3, 4)

JCaçador = Caçador("DanielA", 60, 9, 9, 7, 0, 4, 1, 15)