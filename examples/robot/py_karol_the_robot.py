from miniworldmaker import *


class MyBoard(TiledBoard):

    def __init__(self):
        super().__init__(tile_size=30,
                         columns=20,
                         rows=20,
                         tile_margin=0)
        robo1 = self.add_actor(Robot(), position=(1, 1))
        # Draw border
        for i in range(self.rows):
            self.add_actor(Wall(), position=(0, i))
        for i in range(self.rows):
            self.add_actor(Wall(), position=(self.rows - 1, i))
        for i in range(self.columns):
            self.add_actor(Wall(), position=(i, 0))
        for i in range(self.columns - 1):
            self.add_actor(Wall(), position=(i, self.columns - 1))
        self.add_image(path="images/stone.jpg")


class Robot(Actor):

    def __init__(self):
        super().__init__()
        self.add_image(path="images/robo_green.png")

    def act(self):
        actors = self.look_for_actors(direction="forward", distance=1, actor_type=Wall)
        if not actors:
            self.move()
        else:
            self.turn_right(degrees=90)


class Wall(Actor):

    def __init__(self):
        super().__init__()
        self.add_image("images/rock.png")


board = MyBoard()
board.show()
