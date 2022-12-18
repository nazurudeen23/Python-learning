class human:

    def __init__(self,n,o):
        self.name = n
        self.occupation = o


    def do_work(self):
        if self.occupation == "Actor":
            print(self.name, "Shoot a flim")

        elif self.occupation == "Tennis player":
            print(self.name, "Play a tennis game")

    def speaks(self):
        print(self.name, " says how are you?")

tom = human("Tom cruise","Actor")
tom.do_work()
tom.speaks()
