class Machine():
    def __init__(self):
        self.line = [0] # initializion empty machine line
        self.current = 0 # current cell on the line

    def execute (self, program, get_details = 0):
        """
        Executes the program written on Brainfuck language
        """
        loop = ""
        loop_level = 0
        for symbol in program:
            if get_details == 1:
                print(self.line)
                print("Current:" , self.current)
            if symbol == "[":
                loop_level += 1
                if loop_level == 1:
                    continue
            if symbol == "]":
                loop_level -= 1
                if loop_level == 0:
                    self.do_loop(loop)
                    loop = ""
            if loop_level > 0:
                loop += symbol
                continue
            if symbol == "+":
                self.increment()
            if symbol == "-":
                self.decrement()
            if symbol == ">":
                self.go_right()
            if symbol == "<":
                self.go_left()
            if symbol == ".":
                self.output()
            if symbol == ",":
                self.input_stream()

    def executeMoo(self, program, get_details=0):
        """
        Executes the program written on Moo dialect
        """
        instruction = {1 : "+", 2: "-", 3: ">", 4: "<", 5: "[", 6 : "]", 7 : ".", 0 : ","}
        fuck_prog = ""
        parsed = ""   
        moo_dict = {"MoO":"+","MOo":"-","moO":">","mOo":"<","moo":"[","MOO":"]","OOM":".","oom":","}
        for symbol in program:
            if symbol != " ":
                parsed += symbol
            for key in moo_dict.keys():
                if parsed == key:
                    fuck_prog += moo_dict[key]
                    parsed = ""
            if parsed == "mOO":
                fuck_prog += instruction[self.current]
                parsed = ""
        self.current = 0
        self.line = [0]
        if get_details == 1:
            self.execute(fuck_prog, 1)
        else: 
            self.execute(fuck_prog)

    def input_stream(self):
        """
        Takes input as an integer. Corresponds to "." in Brainfuck, "OOM" in Moo
        """
        raw = input()
        self.line[self.current] = int(raw)

    def convertToMOO (self, program):
        """
        Converts the program written on Brainfuck to Moo dialect and returns string containing it
        """
        moo_prog = ""
        moo_dict = {"MoO":"+","MOo":"-","moO":">","mOo":"<","moo":"[","MOO":"]","OOM":".","oom":","}
        for symbol in program:
            for key, val in moo_dict.items():
                if symbol == val:
                    moo_prog += key + " "
        return moo_prog

    def do_loop(self, code):
        """ 
        Used by execute() function to handle loops
        """
        while self.line[self.current] != 0:
            self.execute(code)

    def increment (self):
        """
        Does an increment for value in the current Turing machine's cell. Corresponds to "+" in Brainfuck, "MoO" in Moo
        """
        self.line[self.current] += 1

    def decrement (self):
        """
        Does an decrement for value in the current Turing machine's cell. Corresponds to "-" in Brainfuck, "MOo" in Moo
        """
        self.line[self.current] -= 1

    def go_right (self):
        """
        Moves cursor in the Turing machine's line one cell to the right. Corresponds to ">" in Brainfuck, "moO" in Moo
        """
        self.current += 1
        try: 
            temp = self.line[self.current] 
        except:
            self.line.append(0)

    def go_left (self):
        """
        Moves cursor in the Turing machine's line one cell to the left. Corresponds to "<" in Brainfuck, "mOo" in Moo
        """
        self.current -= 1

    def output (self):
        """
        Prints the value in the current cell into the console. Corresponds to "," in Brainfuck, "oom" in Moo
        """
        symbol = self.line[self.current]
        print(symbol, end="")

# some code samples
# evaluates expression given in a lab task: 
program_expression = """
, [->+>+<<] >        [ ->  [->+>+<<] > [-<+>] << ]          >>>       [->+>+<<] > [ ->  [->+>+<<] > [-<+>] << ] <<< [->>> >>> > + > + >>> + <<<   <<<< <<<<]     >>> >>> >         [ ->  [->+>+<<] > [-<+>] << ] 
>>>     [ ->  [->+>+<<] > [-<+>] << ]  >> ++  [ ->  [->+>+<<] > [-<+>] << ]  >>> 
> +++ ++ < [->+<]    <<< <<< <<< [- >>>>> >>>>> + <<<<< <<<<< ]  >>>>> >>>>> .
 """

# returns square of number
program_square = """
, [ >+ >+ >+ <<<- ]    > [ >> [ >>+ <<- ] < [ >+ >+ <<- ] >> [ <<+ >>- ] <<<- ]    >>>>.
"""

# returns product of 2 numbers
program_mult = """
, >, < [ >>+ >+ <<<- ]    > [ >> [ >>+ <<- ] < [ >+ >+ <<- ] >> [ <<+ >>- ] <<<- ]    >>>>.
"""

# returns num1 raised to the power of num2
program_power = """
, >, < [ >>+ >+ <<<- ] >>>>+ >+    <<<< [ >> [ >> [ >>+ <<- ] < [ >+ >+ <<- ] >> [ <<+ >>- ] <<<- ] > [ >-  <- ] >>> [ <<<+ >+ >>- ]  <<<<< [ >+ >>>+ <<<<- ] >>>> [ <<<<+ >>>>- ] <<<<<- ]    >>>.
"""

# Moo program for evaluating task expression: 
moo_expression = """ oom moo MOo moO MoO moO MoO mOo mOo MOO moO moo MOo moO moo MOo moO MoO moO MoO mOo mOo MOO moO moo MOo mOo MoO moO MOO mOo mOo MOO moO moO moO moo MOo moO MoO moO MoO mOo mOo MOO moO moo MOo moO moo MOo moO MoO moO MoO mOo mOo MOO moO moo MOo mOo MoO moO MOO mOo mOo MOO mOo mOo mOo moo MOo moO moO moO moO moO moO moO MoO moO MoO moO moO moO MoO mOo mOo mOo mOo mOo mOo mOo mOo mOo mOo mOo MOO moO moO moO moO moO moO moO moo MOo moO moo MOo moO MoO moO MoO mOo mOo MOO moO moo MOo mOo MoO moO MOO mOo mOo MOO moO moO moO moo MOo moO moo MOo moO MoO moO MoO mOo mOo MOO moO moo MOo mOo MoO moO MOO mOo mOo MOO moO moO MoO MoO moo MOo moO moo MOo moO MoO moO MoO mOo mOo MOO moO moo MOo mOo MoO moO MOO mOo mOo MOO moO moO moO moO MoO MoO MoO MoO MoO mOo moo MOo moO MoO mOo MOO mOo mOo mOo mOo mOo mOo mOo mOo mOo moo MOo moO moO moO moO moO moO moO moO moO moO MoO mOo mOo mOo mOo mOo mOo mOo mOo mOo mOo MOO moO moO moO moO moO moO moO moO moO moO OOM 
"""

b = Machine()
b.executeMoo(moo_expression)

print("\nDone")
b.execute(program_power)
print("\nDone")
b.execute(program_mult)
print("\nDone")
b.execute(program_square)
print("\nDone")
b.execute(program_expression)
print("\nDone")