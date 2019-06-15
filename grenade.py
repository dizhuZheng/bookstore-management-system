from rain import Rain

class Grenade(Rain):

    def __init__(self, screen, rect_x, rect_bottom):
        super().__init__(screen, rect_x, rect_bottom)
        self.color = (190,207,140)
        self.speed_factor = 1
