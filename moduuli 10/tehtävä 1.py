class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):

        if self.current_floor < self.top_floor:
            self.current_floor +=1
            print(f"You are now on {self.current_floor} floor!")
        else:
            print("Already at top floor!")

    def floor_down(self):

        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor -1
            print(f"You are now on {self.current_floor} floor!")
        else:
            print("Already at bottom floor")

    def go_to_floor(self, final_d):
        if final_d < self.current_floor:
            while final_d < self.current_floor:
                self.floor_down()
        elif final_d > self.current_floor:
            while final_d > self.current_floor:
                self.floor_up()



