# importing pyglet module
import pyglet
import pyglet.window.key

class test:
    def __init__(self):
        self.window2 = pyglet.window.Window(500, 500, "Geeksforgeeks")
        self.text = "GeeksforGeeks"
        
        self.label = pyglet.text.Label(self.text,
                            font_name ='Times New Roman',
                            font_size = 36,
                            x = window2.width//2, y = window2.height//2,
                            anchor_x ='center', anchor_y ='center')
        
        self.new_label = pyglet.text.Label(self.text,
                            font_name ='Times New Roman',
                            font_size = 10,
                            x = 25, y = 25)
    
    # on draw event
    def on_draw(self):   
        
        # clearing the window
        self.window2.clear()
        # drawing the label on the window
        self.label.draw()
    
        
    # key press event   
    def on_key_press(self,symbol, modifier):
    
        # key "C" get press
        if symbol == pyglet.window.key.C:
            
            # closing the window
            #self.window.close()
                # getting window display
            value = self.window2.display
    
            # printing the value
            print(value)
        
    
    # image for icon

    
    # setting image as icon

    
    # getting window display
    #value = window.display
    
    # printing the value
    #print("Window Display : ")
    #print(value)