
class Membres:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    
    def presentation(self, firstname, lastname):
        print (f"Bonjour, je m'appelle {firstname}{lastname} ")

class Etudiant(Membres):
    def __init__(self, lastname, firstname, reason):
        super().__init__(lastname, firstname)
        print (reason)

class Instructeur(Membres):
    def __init__(self, lastname, firstname,):
        super().__init__(lastname, firstname)

    def biographie():
        pass

    def competences():
        pass



if __name__ == '__main__':
    pass