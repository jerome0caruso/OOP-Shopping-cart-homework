class StringStuff():

    def __init__(self):
        pass



    def get_String(self, u_str = ""):
        u_input = input("Please enter a sentance!")
        return self.print_String(u_input)

    def print_String(self, u_input):
        print(u_input.upper())

string_1 = StringStuff()

string_1.get_String()

