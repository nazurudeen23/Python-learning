class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    def me(self):
        Youtuber.youtubers_action(self)
      


coder = Person()
# coder.teachers_action()
# coder.Engineers_action()
# coder.youtubers_action()
coder.me()