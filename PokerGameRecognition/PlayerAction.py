import enum


class ActionType(enum.Enum):
    Fold = 1
    Call = 2
    Raise = 3
    AllIn = 4


class PlayerAction:

    def __init__(self, action_type:ActionType, action_cost:float):
        """

        :param action_type: Գործողության տեսակը, պիտի լինի  ActionType կլասից
        :param action_cost: Գինը գործողության, Fold-ի դեպքում 0, մնացած դեպքում թե ինչքան գումար ա ավելացրել pot-ի մեջ
        """
        self.action_type = action_type
        self.action_cost = action_cost
