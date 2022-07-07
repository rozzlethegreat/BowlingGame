class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_frame = 1
        self.current_ball = 0

    def finished(self):
        if self.current_frame > 10:
            return True
        return False

    def roll(self, pins):
        # if len(self.rolls) >= 21:
        #     raise IndexError
        if self.finished():
            raise ValueError
        if (pins < 0) or (pins > 10):
            raise ValueError
        self.rolls.append(pins)
        if self.current_frame == 10:
            if self.current_ball == 2:
                self.current_frame += 1
            elif self.current_ball == 0:
                self.current_ball = 1
            else:
                last_pins = self.rolls[len(self.rolls)-1]
                if pins == 10 or last_pins == 10 or last_pins + pins == 10:
                    self.current_ball += 1
                else:
                    self.current_frame += 1
        else:
            if pins == 10 or self.current_ball == 1:
                self.current_frame += 1
                self.current_ball = 0
            else:
                self.current_ball = 1

    def score(self):
        if not self.finished():
            raise ValueError
        result = 0
        roll_index = 0
        for frameIndex in range(10):
            if self.is_strike(roll_index):  # bug; was always true
                result += self.strike_score(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                result += self.spare_score(roll_index)
                roll_index += 2
            else:
                result += self.frame_score(roll_index)
                roll_index += 2  # was indented wrong
        return result  # was indented wrong

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index+1] == 10

    def strike_score(self, roll_index):  # spelling mistake
        return 10 + self.rolls[roll_index+1] + self.rolls[roll_index+2]

    def spare_score(self, roll_index):
        return 10 + self.rolls[roll_index+2]

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index+1]
