"""Projemizin senaryosu şu şekilde:
İki adet websitesi oluşturacağız. ikisi de isim ve soyisme ihtiyaç duyacak ve ayrıca
ilki id ikincisi e-mail isteyecek"""

class Website:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def LogInInfo(self):
        print("Name: {}, Surname: {}".format(self.name, self.surname))

A = Website("Ays", "Durak")
A.LogInInfo()

class idSite(Website):
    def __init__(self, name, surname, id):
        Website.__init__(self, name, surname) 

        """Burada Website ve super() arasında bir fark var ama 
        anlamadım ikisi birbiri yerine kullanılamadı."""
        #hehe tamam anladım super kullanılırken parantesi unutma
        #ve en önemlisi super self almıyor
        #eğer super kulanmak istersen
        #super().__init__(name, surname) şeklinde kullan
        self.id = id

    def idd(self):
        print("Name: {}, Surname: {}, Id: {}".format(self.name, self.surname, self.id))
        

B = idSite("Aysenur","Durak","12")
B.idd()

class mailSite(Website):
    def __init__(self, name, surname, mail):
        Website.__init__(self, name, surname)
        self.mail = mail

    def email(self):
        print("Name: {}, Surname: {}, e-mail: {}".format(self.name, self.surname, self.mail))

C = mailSite("Aysenur", "Durak", "aysenur@ays.com")
C.LogInInfo()   
C.email()   

