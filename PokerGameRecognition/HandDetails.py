import Card
import PlayerAction

# Հիմնական կլասը, որի մեջ պահելու ենք Hand Details-ը։ Պիտի կարողանա նկարի path-ով Construct լինի
class HandDetails:

    def __init__(self, path_to_png_file):
        # Ստեղ կպահենք խաղացողների անունները։ եթե ամբողջ անունը նկարի մեջ չի երևում, երևացով մասը մենակ
        self.player_names = []

        # ամեն խաղացողի համար թե ինչքան փող ունի խաղի սկզբին
        self.player_initial_funds = []

        # ընդհանուր քարտերը
        self.public_cards = []

        # list-երի list, ամեն խաղացողի համար իրա քարտերը, եթե գիտենք իրանը։ Եթե չգիտենք, դատարկ լիսթ
        self.player_cards = []

        # Էս լիսթը կունենա ուղիղ 4 էլեմենտ (preflop, flop, turn, river-ի համար), ամեն մեկը իրա հերթին էլի լիսթ ա։
        # Էտ 4 լիսթից ամեն մեկի մեջ կպահենք թե ինչ գործողություններ են եղել տվյալ round-ին, PlayerAction class-ից։
        self.player_actions = []

