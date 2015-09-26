class Table:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.pixels = [[[0.0, 0.0] for j in range(height)] for i in range(width)]
