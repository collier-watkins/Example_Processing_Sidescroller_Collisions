
#Making a 2D mario style game

class Player:
    
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.feetX = self.x
        self.feetY = self.y + 35
        self.rightX = self.x + 14
        self.rightY = self.y
        self.leftX = self.x - 14
        self.leftY = self.y
        self.canMoveDown = True
        self.canMoveLeft = True
        self.canMoveRight = True
        
    def draw(self):
        line(self.x - 14, self.y, self.x + 14, self.y) #Arms
        line(self.x, self.y - 20, self.x, self.y + 20) #Body
        line(self.x, self.y + 20, self.x - 7, self.y + 35) #Left Leg
        line(self.x, self.y + 20, self.x + 7, self.y + 35) #Right Leg
        fill(255,255,255) #Head Color
        ellipse(self.x, self.y - 25, 20, 20)
        fill(0,255,0)
        ellipse(self.x, self.y, 5, 5)
        ellipse(self.feetX,self.feetY, 5,5)
        ellipse(self.rightX, self.rightY, 5,5)
        ellipse(self.leftX, self.leftY, 5,5)
        
    def move(self):
        self.feetY = self.y + 35
        self.feetX = self.x
        self.rightX = self.x + 14
        self.rightY = self.y
        self.leftX = self.x - 14
        self.leftY = self.y
        
        if self.canMoveDown :
            self.y = self.y + 5
        if keyPressed and key == "d" and self.canMoveRight:    #If key d is currently pressed
            self.x = self.x + 5
        if keyPressed and key == "a" and self.canMoveLeft :    #If key a is currently pressed
            self.x = self.x - 5
        # TRY TO CALL ME ON YOUR LAPTOP
        if keyPressed and key == " " :
          self.y = self.y - 10
                
                
class Box:
  
  def __init__(self, X, Y, W, H):
    self.x1 = X
    self.x2 = X + W
    self.y1 = Y
    self.y2 = Y + H
    
  def draw(self):
    rectMode(CORNERS)
    fill(255,0,0)
    rect(self.x1,self.y1,self.x2,self.y2)
    
  def isPointInBox(self, x, y):
    if x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2 :
      return True
    else:
      return False
    
##############################

man = Player(100,100)
boxes = []
                

def setup():
  size(800,600)
  boxes.append( Box(50,200,400,50) )
  boxes.append( Box(50,400,400,50) )
  boxes.append( Box(200,300,400,50) )
  boxes.append( Box(550,200,200,100))
  boxes.append( Box(0,200,50,250) )
  
def draw():
  background(150)
    
  for b in boxes:
    b.draw()
      
      # Collision Detection Here
  man.canMoveDown = True
  man.canMoveRight = True
  man.canMoveLeft = True
  for b in boxes:
      if b.isPointInBox(man.feetX,man.feetY) :
        man.canMoveDown = False
      if b.isPointInBox(man.rightX, man.rightY) :
        man.canMoveRight = False
      if b.isPointInBox(man.leftX,man.leftY) :
        man.canMoveLeft = False
      #
  man.move()
  man.draw()