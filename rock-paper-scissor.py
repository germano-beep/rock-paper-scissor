class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, Choose between rock, scissor and paper: ".format(name=self.name))
        print("{name} selected {choice}".format(name=self.name, choice=self.choice))

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]

    def incrementPoints(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, 1, -1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("Round result in a {result}".format(result=self.getResultAsString(result)))

        if result > 0:
            p1.incrementPoints()

        elif result < 0:
            p2.incrementPoints()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def awardPoints(self):
        print("implement")

    def getResultAsString(self, result):
        res = {
            1: "Win",
            0: "Draw",
            -1: "loss"
        }
        return res[result]

class Game:
    def __init__(self):
        self.end_game = False
        self.firstParticipant = Participant("Arthur")
        self.secondParticipant = Participant("Jucimara")

    def start(self):
        while not self.end_game:
            gameRound = GameRound(self.firstParticipant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == "y":
            GameRound(self.firstParticipant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended. {p1name} has {p1points} and {p2name} has {p2points}".format(p1name=self.firstParticipant.name,p1points=self.firstParticipant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.end_game = True

    def determineWinner(self):
        resultString = "It's a draw"
        if self.firstParticipant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.firstParticipant.name)
        elif self.firstParticipant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)

        print(resultString)

if __name__ == '__main__':
    game = Game()
    game.start()
