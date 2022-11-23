class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None
    
    def set_cell_value(self, value):
        self.value = value
    
    def set_sketched_value(self, value):
        if self.sketched_value == None:
            self.sketched_value = value
    
