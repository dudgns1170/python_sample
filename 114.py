class Car:


    def __init__(self,wheel,price,name):
        self.wheel = wheel
        self.price =price
        self.name = name

    def Info(self):
        #super().Info()
        print("총 정보는\n","바퀴수:",self.wheel, "\n가격:",self.price,"\n정보:",self.name)


class Bicyle(Car):

    def __init__(self,wheel,price,name):
        super().__init__(wheel,price,name)
        #self.name = name

    def Info(self):
        #super().Info()
        super(Bicyle, self).Info()






'''class InFo(Car):
    def __init__(self,wheel,price):
        super().__init__(wheel,price)


    def Info(self):''
        super().Info()'''
       



# car =Car(4,8855,"dsd")
# bicycle = Bicyle(2,1000,"사노이")
#
# bicycle.Info()
# car.Info()

