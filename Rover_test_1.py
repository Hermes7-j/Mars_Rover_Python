class NASA_Rover:  
    def __init__(self, x, y, orientation):  
        self.x = x  
        self.y = y  
        self.orientation = orientation  
        self.directions = ['N', 'E', 'S', 'W']  
    
    def turn_left(self):  
        self.orientation = self.directions[(self.directions.index(self.orientation) - 1) % 4]  
    
    def turn_right(self):  
        self.orientation = self.directions[(self.directions.index(self.orientation) + 1) % 4]  
    
    def move(self):  
        if self.orientation == 'N':  
            self.y += 1  
        elif self.orientation == 'E':  
            self.x += 1  
        elif self.orientation == 'S':  
            self.y -= 1  
        elif self.orientation == 'W':  
            self.x -= 1  

def process_rovers_commands(upper_right, rovers_info):  
    plateau_x, plateau_y = map(int, upper_right.split())  
    rovers = []  
    
    for i in range(0, len(rovers_info), 2):  
        position = rovers_info[i].split()  
        instructions = rovers_info[i + 1]  

        rover = NASA_Rover(int(position[0]), int(position[1]), position[2])  
         
        for command in instructions:  
            if command == 'L':  
                rover.turn_left()  
            elif command == 'R':  
                rover.turn_right()  
            elif command == 'M':   
                if rover.orientation == 'N' and rover.y + 1 <= plateau_y:  
                    rover.move()  
                elif rover.orientation == 'E' and rover.x + 1 <= plateau_x:  
                    rover.move()  
                elif rover.orientation == 'S' and rover.y - 1 >= 0:  
                    rover.move()  
                elif rover.orientation == 'W' and rover.x - 1 >= 0:  
                    rover.move()    
        rovers.append(f"{rover.x} {rover.y} {rover.orientation}")  
    return rovers  
 
upper_right = "5 5"  
rovers_info = [  
    "1 2 N",  
    "LMLMLMLMM",  
    "3 3 E",  
    "MMRMMRMRRM"  
]   
results = process_rovers_commands(upper_right, rovers_info)  
for result in results:  
    print(result)