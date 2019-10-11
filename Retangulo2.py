
class Retangulo:

    def __init__(self,largura,altura):
        self.largura = 0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self,num):
        if(not((isinstance(num,int)and(num>0)))):
            raise ValueError("Altura é invalida: {} ".format(num))
        self.altura = num
    def set_largura(self,num):
        if(not(isinstance(num,int)and(num>0))):
            raise ValueError("Largura é invalida: {} ".format(num))
        self.largura = num
    def get_area(self):
        return self.altura * self.largura

# r = Retangulo(largura=10,altura=5)
r = Retangulo(largura=1,altura=6)
print(r.get_area())
