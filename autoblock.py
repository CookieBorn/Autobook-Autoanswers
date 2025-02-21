class Autoblock():
    def __init__(self, symbol, numbers):
        self.symbol=symbol
        self.numbers=numbers
        self.columns=numbers[0:10]
        self.rows=numbers[10:20]
        self.answers=numbers[0:10]
        self.text=None

        self.text_block()
        print(self.answers)

    def answers_fill(self):
        if self.symbol=="+ ":
            inx=0
            for inx in range(len(self.rows)):
                self.answers.append(self.rows[inx])
                x=0
                for x in range(len(self.columns)):
                    self.answers.append(f"{int(self.columns[x])+int(self.rows[inx])} ")
                    x+=1
                inx+=1

    def text_block(self):
        self.text="\n".join(self.answers)
