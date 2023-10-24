class Game:
    def __init__(self):
        self.scene = "start"
        self.inventory = []
        self.scenes = {
            "start": {
                "describtion": "You wake up in a dark, cold and moist room. You can't even see your own hands and you do not remember how you got here. You slowly starting to scan the room by touching your surrounding. You find a candle and a lighter, now you finally can see the room better",
                "items": [],
                "directions": {"north": "hallway", "south": "exit"},
            },
            "candle_room": {
                "describtion": "There's a key under the candle. There are two doors, one to your left and one to your right.",
                "items": [],
                "directions": {},
            },
        }

        self.actions = {"go": self.go_direction}

    def go_direction(self, direction):
        return

    def play(self):
        print(self.scenes[self.room])
        while True:
            action = input("> ")

            print(self.scenes[self.room])


game = Game()
game.play()
