from abc import ABC, abstractmethod

class User(ABC):
     
     var_test = 100

     @abstractmethod
     def login():
          pass
     
     def non_abstract():
          pass
     
     def non_abstract_implemented():
          return 0
     
     @staticmethod
     def abstract_static_test():
          return 1

class Player(User):
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


        self.email_ = first_name.lower()+"."+last_name.lower()+"@gmail.com"

        

        Player.players +=1

    @property
    def email(self):
        return self.email_
    
    @email.setter
    def email(self,email):
         if self.is_valid_email(email):
              self.email_ = email
         else:
              print("Given email was not valid")     

    def login():
         print("Logging in...")

    def full_name(self) -> str:
        return self.first_name+" "+self.last_name
    
    def get_free_game(self):
        return Player.week_free_game
    
    def player_info(self):
         print("First name:",self.first_name)
         print("Second name",self.last_name)
         print("Games colledction:")
         print("-------------------")
         for game in self.games:
              print(game)
         print("-------------------")     
         
    @classmethod
    def add_free_game(cls,game):
        if isinstance(cls.week_free_game,str):
            cls.week_free_game = [cls.week_free_game,game]
        else:
            cls.week_free_game.append(game) 

    @classmethod
    def parse_instance_string(cls,instance_string):

        games_index = instance_string.index("[")

        first_name, last_name = instance_string[:games_index-1].split(",")

        games = instance_string[games_index+1:-1]

        return cls(first_name,last_name,games.split(",")) 

    @staticmethod 
    def is_valid_email(email):

        if all([element in email for element in ["@","."]]):
            if email.count("@") == 1 and email.count(".") == 2:
                if any([email[-start:] in ["com","pl","de"] for start in [len(element) for element in ["com","pl","de"]] ]):
                             return True

        return False

    def __len__(self):
         return self.players                



class VipPlayer(Player):
     vips = 0
     def __init__(self, first_name, last_name, games,diamonds):
          super().__init__(first_name, last_name, games)
          self.diamonds = diamonds
          VipPlayer.vips += 1

     def apply_premium_game_account(self,game):
          if self.diamonds >= 10:
               self.games[self.games.index(game)] = game+": Premium Version"
               self.diamonds -= 10

     def player_info(self):
        super().player_info()
        print("Diamonds:",self.diamonds)

                  


class AdminPlayer(VipPlayer):
     admins = 0
     def __init__(self, first_name, last_name, games,diamonds,respect_points):
          super().__init__(first_name, last_name, games,diamonds)
          self.respect_points = respect_points
          AdminPlayer.admins += 1

     def get_respect(self):
          return self.respect_points
     
     def player_info(self):
          super().player_info()
          print("Respect points:",self.respect_points)
     


admin1 = AdminPlayer("Damianek","Malboras",["tf2","batman","witcher 3"],22,12032)

print(help(admin1))
        