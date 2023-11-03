class GridWorld():
    def __init__(self):
        self.x=0
        self.y=0
    
    def step(self, a):
        if a==0:
            self.move_left()
        elif a==1:
            self.move_up()
        elif a==2:
            self.move_right()
        elif a==3:
            self.move_down()
        reward = -1 
        done = self.is_done()
        return (self.x, self.y), reward, done

    def move_right(self):
        self.y += 1  
        if self.y > 3:
            self.y = 3
    def move_left(self):
        self.y -= 1
        if self.y < 0:
            self.y = 0
    def move_up(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0
    def move_down(self):
        self.x += 1
        if self.x > 3:
            self.x = 3

    def is_done(self):
        if self.x == 3 and self.y == 3:
            return True
        else :
            return False

    def get_state(self):
        return (self.x, self.y)
    
    def reset(self):
        self.x = 0
        self.y = 0
        return (self.x, self.y)
