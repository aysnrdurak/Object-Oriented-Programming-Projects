#Parent Class
class Website:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def loginInfo(self):
        print(self.name + " " + self.surname) 
        
#Minik Uygulama
p1 = Website("Name", "Surname")
p1.loginInfo()

#Child Class
class Idsite(Website):

    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)

        self.ids = ids

    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)

p2 = Idsite("Ayse", "Durak", "3")
p2.login()
p2.loginInfo()

#Second Child Class

class mailSite(Idsite):

    def __init__(self, name, surname, ids, mail):
        Idsite.__init__(self, name, surname, ids)

        self.mail = mail

    def maillogin(self):
        print(self.name + " " + self.surname + " " + self.ids +" " +self.mail)

p3 = mailSite("Nur", "Durak", "5", "ays@mail.com")
p3.maillogin()
p3.loginInfo()
