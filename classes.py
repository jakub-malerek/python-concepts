class Player:
    week_free_game = "Spiderman"
    players = 0
    def __init__(self,first_name,last_name,games):
        self.last_name = last_name
        self.first_name = first_name

        try:
            games.__iter__()  
        except AttributeError:
            print("Iterable is expected as argument for \"games\" parameter")
            self.games = None
        else:
            self.games = list(games)

        self.email = first_name+"."+last_name+"@gmail.com"

        Player.players +=1

    def full_name(self) -> str:
        return self.first_name+" "+self.last_name
    
    def get_free_game(self):
        return Player.week_free_game
    
    def class_method():
        print("Class method --------------")


p1 = Player("Ziomek","Karczix",{"CS:GO":5,"LoL":10})

p2 = Player("Diego","Maradona",10)

print(p2.get_free_game())

p2.week_free_game = "Helldivers 2"

print(p2.get_free_game())
print(p1.get_free_game())

Player.week_free_game = "Team Fortress 2"

print(p1.get_free_game())
print(p2.get_free_game())

p1.class_method()






        