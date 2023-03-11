import pygame
from pygame.locals import *

from userlogin_sqlite import *

#define frames per second
FPS = 32

#define some colors
BLACK = (160,160,160)
PURPLE = (102, 0, 102)
BLUE = (0,102,204)
RED = (204,0,102)

#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
# GUI objects

#########################################################
#########################################################
class Image(pygame.sprite.Sprite):

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,screen):

        win.blit(self.image, self.rect.topleft)
        
#########################################################
#########################################################
class TitleText():
    def __init__(self, x, y, width, height, text, textColour):

        self.text = text
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(text, 1, textColour)
        self.x = x
        self.y = y
        self.width = max(width,text.get_width())+10
        self.height = max(height,text.get_height())      
        self.textColour = textColour
        self.rect = pygame.Rect(x,y,self.width,self.height)
    
    def draw(self,win):

        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(self.text, 1, self.textColour)
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

#########################################################
#########################################################
class Button():
    def __init__(self, x, y, width, height, text, textColour, lineColour, lineWidth, fillColour, activeColour):

        self.text = text
        font = pygame.font.SysFont('comicsansms', 40)
        text = font.render(text, 1, textColour)
        self.x = x
        self.y = y
        self.width = max(width,text.get_width())+10
        self.height = max(height,text.get_height())      
        self.textColour = textColour
        self.lineColour = lineColour
        self.lineWidth = lineWidth
        self.fillColour = fillColour
        self.activeColour = activeColour
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.active = False
        
    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = True
                return True
            else:
                self.active = False
                
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return True  
        return False
                
    def draw(self,win):

        if self.active:
            pygame.draw.rect(win, self.activeColour, (self.x,self.y,self.width,self.height),0)
        else:
            pygame.draw.rect(win, self.fillColour, (self.x,self.y,self.width,self.height),0)

        if self.lineWidth != None:
            pygame.draw.rect(win, self.lineColour, (self.x,self.y,self.width,self.height),self.lineWidth)
                    
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, self.textColour)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

#########################################################
#########################################################
class TextInput():
    def __init__(self, x, y, width, height, text, textColour, lineColour, lineWidth, fillColour, activeColour):

        self.text = text
        font = pygame.font.SysFont('comicsans', 40)
        text = font.render(text, 1, textColour)
        self.x = x
        self.y = y
        self.width = max(width,text.get_width())+10
        self.height = max(height,text.get_height())      
        self.textColour = textColour
        self.lineColour = lineColour
        self.lineWidth = lineWidth
        self.fillColour = fillColour
        self.activeColour = activeColour
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.active = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key != pygame.K_RETURN and event.key != pygame.K_TAB:
                self.text += event.unicode
                
        return self.text
    
    def draw(self,win):

        # Resize the box if the text is too long.
        font = pygame.font.SysFont('comicsans', 40)
        text = font.render(self.text, 1, self.textColour)
        self.width = max(200,text.get_width())+10
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        
        if self.active:
            pygame.draw.rect(win, self.activeColour, (self.x,self.y,self.width,self.height),0)
        else:
            pygame.draw.rect(win, self.fillColour, (self.x,self.y,self.width,self.height),0)

        if self.lineWidth != None:
            pygame.draw.rect(win, self.lineColour, (self.x,self.y,self.width,self.height),self.lineWidth)
                    
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, self.textColour)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


#########################################################
#########################################################
class PasswordInput():
    def __init__(self, x, y, width, height, text, textColour, lineColour, lineWidth, fillColour, activeColour):

        self.text = text
        font = pygame.font.SysFont('comicsans', 40)
        text = font.render(text, 1, textColour)
        self.x = x
        self.y = y
        self.width = max(width,text.get_width())+10
        self.height = max(height,text.get_height())      
        self.textColour = textColour
        self.lineColour = lineColour
        self.lineWidth = lineWidth
        self.fillColour = fillColour
        self.activeColour = activeColour
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.active = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key != pygame.K_RETURN and event.key != pygame.K_TAB:
                self.text += event.unicode

        return self.text
    
    def draw(self,win):

        # Resize the box if the text is too long.
        font = pygame.font.SysFont('comicsans', 40)
        text = font.render(self.text, 1, self.textColour)
        self.width = max(200,text.get_width())+10
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        
        if self.active:
            pygame.draw.rect(win, self.activeColour, (self.x,self.y,self.width,self.height),0)
        else:
            pygame.draw.rect(win, self.fillColour, (self.x,self.y,self.width,self.height),0)

        if self.lineWidth != None:
            pygame.draw.rect(win, self.lineColour, (self.x,self.y,self.width,self.height),self.lineWidth)
                    
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(len(self.text)*"*", 1, self.textColour)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
#########################################################
#########################################################
class MultiLineText():
    def __init__(self, x, y, width, height, text, textColour, lineColour, lineWidth, fillColour):

        self.text = text
        font = pygame.font.SysFont('couriernew', 20)
        text = font.render(text, 1, textColour)
        self.x = x
        self.y = y
        self.width = max(width,text.get_width())+10
        self.height = max(height,text.get_height())      
        self.textColour = textColour
        self.lineColour = lineColour
        self.lineWidth = lineWidth
        self.fillColour = fillColour
        self.rect = pygame.Rect(x,y,self.width,self.height)
    
    def draw(self,win):
      
        pygame.draw.rect(win, self.lineColour, (self.x,self.y,self.width,self.height),self.lineWidth)

        font = pygame.font.SysFont('couriernew', 20)

        words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.x + self.width, self.y + self.height
        x, y = self.x + 5, self.y
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, self.textColour)
                word_width, word_height = word_surface.get_size()
                if x + word_width + space >= max_width:
                    x = self.x + 5 # Reset the x.
                    y += word_height  # Start on new row.
                win.blit(word_surface, (x, y))
                x += word_width + space
            x = self.x + 5 # Reset the x.
            y += word_height  # Start on new row.

#########################################################
#########################################################
class TableText():
    def __init__(self, x, y, width, height, text, textColour, lineColour, lineWidth, fillColour, cols):

        self.text = text
        font = pygame.font.SysFont('couriernew', 20)
        text = font.render(text, 1, textColour)
        self.x = x
        self.y = y
        self.width = max(width,text.get_width())+10
        self.height = max(height,text.get_height())      
        self.textColour = textColour
        self.lineColour = lineColour
        self.lineWidth = lineWidth
        self.fillColour = fillColour
        self.cols = cols
        self.rect = pygame.Rect(x,y,self.width,self.height)
    
    def draw(self,win):
      
        pygame.draw.rect(win, self.lineColour, (self.x,self.y,self.width,self.height),self.lineWidth)

        font = pygame.font.SysFont('couriernew', 20)

        max_width, max_height = self.x + self.width, self.y + self.height
        myx, myy = self.x, self.y
        for line in self.text:
            for i in range(len(line)):
                word_surface = font.render(line[i], 0, self.textColour)
                word_width, word_height = word_surface.get_size()
                myx = self.x + self.cols[i]
                win.blit(word_surface, (myx, myy))
            myx = self.x  # Reset the x.
            myy += word_height  # Start on new row.    

#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
# GUI functions

#########################################################
#########################################################
def pygame_userlogin():
    
    #initialise GUI objects
    logo = Image(50,10,"logo.png")
    TitleBox = TitleText(100, 200, 50, 50, "User login...", RED)
    usernameTextbox = TextInput(100, 300, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    passwordTextbox = PasswordInput(100, 400, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    submitButton = Button(100, 500, 50, 50, "Submit", PURPLE, RED, 3, BLACK, BLUE)

    #make the username textbox active
    usernameTextbox.active = True

    #loop until the user presses ESC key
    run = True

    #initialise keyboard input
    key = None

    username=""
    password=""

    while run == True:
        
        for event in pygame.event.get():
          
            #close nicely if the user closes the window
            if event.type == pygame.QUIT:
                run = False
                username=""
            #close nicely if the user presses the escape key
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
                username=""
            elif event.type == pygame.KEYDOWN:
                #tabbing between textboxes
                if usernameTextbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    usernameTextbox.active = False
                    passwordTextbox.active = True
                elif passwordTextbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    passwordTextbox.active = False
                    submitButton.active = True
                elif submitButton.active and (event.key == pygame.K_TAB):
                    submitButton.active = False
                    usernameTextbox.active = True          

            username = usernameTextbox.handle_event(event)
            password = passwordTextbox.handle_event(event)

            if submitButton.handle_event(event):
                run = False
                
        #draw the white background
        win.fill((255,255,255))

        logo.draw(win)
        
        #draw textbox
        TitleBox.draw(win)  
        usernameTextbox.draw(win)  
        passwordTextbox.draw(win)  

        #draw button
        submitButton.draw(win)  

        #update the screen
        pygame.display.update()
        clock.tick(FPS)
 
    return username,password

#########################################################
#########################################################
def pygame_menu():
    
    #initialise GUI objects
    TitleBox = TitleText(100, 10, 50, 50, "User login - Menu...", RED)
    showButton = Button(100, 100, 50, 50, "Show users", PURPLE, RED, 3, BLACK, BLUE)
    addButton = Button(100, 200, 50, 50, "Add user", PURPLE, RED, 3, BLACK, BLUE)
    updateButton = Button(100, 300, 50, 50, "Update user", PURPLE, RED, 3, BLACK, BLUE)
    deleteButton = Button(100, 400, 50, 50, "Delete user", PURPLE, RED, 3, BLACK, BLUE)
    quitButton = Button(100, 500, 50, 50, "Log out", PURPLE, RED, 3, BLACK, BLUE)

    #loop until the user presses ESC key
    run = "Error"

    #initialise keyboard input
    key = None

    while run == "Error":
        
        for event in pygame.event.get():
          
            #close nicely if the user closes the window
            if event.type == pygame.QUIT:
                run = "Log out"
            #close nicely if the user presses the escape key
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = "Log out"

            elif showButton.handle_event(event):
                run = "Show users"
            elif addButton.handle_event(event):
                run = "Add user"
            elif updateButton.handle_event(event):
                run = "Update user"
            elif deleteButton.handle_event(event):
                run = "Delete user"
            elif quitButton.handle_event(event):
                run = "Log out"

        #draw the white background
        win.fill((255,255,255))

        TitleBox.draw(win)

        #draw button
        showButton.draw(win)  
        addButton.draw(win)  
        updateButton.draw(win)  
        deleteButton.draw(win)  
        quitButton.draw(win)  

        #update the screen
        pygame.display.update()
        clock.tick(FPS)
    
    return run

#########################################################
#########################################################
def pygame_showusers():
    
    #initialise GUI objects
    TitleBox = TitleText(100, 10, 50, 50, "User login - Show users...", RED)
    usersTableText = TableText(100, 100, 400, 400, "", BLACK, RED, 3, PURPLE, [5, 155])
    backtomenuButton = Button(100, 500, 50, 50, "Back", PURPLE, RED, 3, BLACK, BLUE)

    # fetch the data
    mytext = [["Username","Password"]]
    results = showmeall()
    
    for i in range (len(results)):
        mytext.append( [str(results[i][1]), str(results[i][2])] )

    usersTableText.text = mytext


    #loop until the user presses ESC key
    run = True
    
    while run == True:
        
        for event in pygame.event.get():
          
            #close nicely if the user closes the window
            if event.type == pygame.QUIT:
                run = False
            #close nicely if the user presses the escape key
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            elif backtomenuButton.handle_event(event):
                run = False

        #draw the white background
        win.fill((255,255,255))

        #draw textbox
        TitleBox.draw(win)
        usersTableText.draw(win)
        
        #draw button
        backtomenuButton.draw(win)
        
        #update the screen
        pygame.display.update()
        clock.tick(FPS)

#########################################################
#########################################################
def pygame_adduser():
    
    #initialise GUI objects
    TitleBox = TitleText(100, 10, 50, 50, "User login - Add user...", RED)
    usernameTitleBox = TitleText(100, 100, 50, 50, "Username", RED)
    usernameTextbox = TextInput(200, 100, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    password1TitleBox = TitleText(100, 200, 50, 50, "Password:", RED)
    password1Textbox = PasswordInput(200, 200, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    password2TitleBox = TitleText(100, 300, 50, 50, "Password:", RED)
    password2Textbox = PasswordInput(200, 300, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    submitButton = Button(100, 400, 50, 50, "Add", PURPLE, RED, 3, BLACK, BLUE)
    backtomenuButton = Button(100, 500, 50, 50, "Back", PURPLE, RED, 3, BLACK, BLUE)

    #make the username textbox active
    usernameTextbox.active = True

    #loop until the user presses ESC key
    run = True

    #initialise keyboard input
    key = None

    username = ""
    password1 = ""
    password2 = ""
    
    while run == True:
        
        for event in pygame.event.get():
          
            #close nicely if the user closes the window
            if event.type == pygame.QUIT:
                run = False
                username = ""
            #close nicely if the user presses the escape key
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
                username = ""
            elif backtomenuButton.handle_event(event):
                run = False
                username = ""
            elif event.type == pygame.KEYDOWN:
                #tabbing between textboxes
                if usernameTextbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    usernameTextbox.active = False
                    password1Textbox.active = True
                elif password1Textbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    password1Textbox.active = False
                    password2Textbox.active = True
                elif password2Textbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    password2Textbox.active = False
                    submitButton.active = True
                elif submitButton.active and (event.key == pygame.K_TAB):
                    submitButton.active = False
                    usernameTextbox.active = True          

            username = usernameTextbox.handle_event(event)
            password1 = password1Textbox.handle_event(event)
            password2 = password2Textbox.handle_event(event)

            if submitButton.handle_event(event):
                run = False

        #draw the white background
        win.fill((255,255,255))

        #draw textbox
        TitleBox.draw(win)
        usernameTitleBox.draw(win)
        usernameTextbox.draw(win)
        password1TitleBox.draw(win)
        password1Textbox.draw(win)
        password2TitleBox.draw(win)
        password2Textbox.draw(win)  

        #draw button
        submitButton.draw(win)  
        backtomenuButton.draw(win)

        #update the screen
        pygame.display.update()
        clock.tick(FPS)
    
    return username,password1,password2

#########################################################
#########################################################
def pygame_updateuser():
    
    #initialise GUI objects
    TitleBox = TitleText(100, 10, 50, 50, "User login - Update user...", RED)
    usernameTitleBox = TitleText(100, 100, 50, 50, "Username", RED)
    usernameTextbox = TextInput(200, 100, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    password1TitleBox = TitleText(100, 200, 50, 50, "Password:", RED)
    password1Textbox = PasswordInput(200, 200, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    password2TitleBox = TitleText(100, 300, 50, 50, "Password:", RED)
    password2Textbox = PasswordInput(200, 300, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    submitButton = Button(100, 400, 50, 50, "Update", PURPLE, RED, 3, BLACK, BLUE)
    backtomenuButton = Button(100, 500, 50, 50, "Back", PURPLE, RED, 3, BLACK, BLUE)

    #make the username textbox active
    usernameTextbox.active = True

    #loop until the user presses ESC key
    run = True

    #initialise keyboard input
    key = None

    username = ""
    password1 = ""
    password2 = ""
    
    while run == True:
        
        for event in pygame.event.get():
          
            #close nicely if the user closes the window
            if event.type == pygame.QUIT:
                run = False
                username = ""
            #close nicely if the user presses the escape key
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
                username = ""
            elif backtomenuButton.handle_event(event):
                run = False
                username = ""
            elif event.type == pygame.KEYDOWN:
                #tabbing between textboxes
                if usernameTextbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    usernameTextbox.active = False
                    password1Textbox.active = True
                elif password1Textbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    password1Textbox.active = False
                    password2Textbox.active = True
                elif password2Textbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    password2Textbox.active = False
                    submitButton.active = True
                elif submitButton.active and (event.key == pygame.K_TAB):
                    submitButton.active = False
                    usernameTextbox.active = True

            username = usernameTextbox.handle_event(event)
            password1 = password1Textbox.handle_event(event)
            password2 = password2Textbox.handle_event(event)

            if submitButton.handle_event(event):
                run = False

        #draw the white background
        win.fill((255,255,255))

        #draw textbox

        TitleBox.draw(win)
        usernameTitleBox.draw(win)
        usernameTextbox.draw(win)
        password1TitleBox.draw(win)
        password1Textbox.draw(win)
        password2TitleBox.draw(win)
        password2Textbox.draw(win)

        #draw button
        submitButton.draw(win)  
        backtomenuButton.draw(win)

        #update the screen
        pygame.display.update()
        clock.tick(FPS)
    
    return username,password1,password2

#########################################################
#########################################################
def pygame_deleteuser():
    
    #initialise GUI objects
    TitleBox = TitleText(100, 10, 50, 50, "User login - Delete user...", RED)
    usernameTitleBox = TitleText(100, 100, 50, 50, "Username", RED)
    usernameTextbox = TextInput(200, 100, 50, 50, "", PURPLE, RED, 3, BLACK, BLUE)
    submitButton = Button(100, 400, 50, 50, "Delete", PURPLE, RED, 3, BLACK, BLUE)
    backtomenuButton = Button(100, 500, 50, 50, "Back", PURPLE, RED, 3, BLACK, BLUE)

    #make the username textbox active
    usernameTextbox.active = True

    #loop until the user presses ESC key
    run = True

    #initialise keyboard input
    key = None

    username = ""
    
    while run == True:
        
        for event in pygame.event.get():
          
            #close nicely if the user closes the window
            if event.type == pygame.QUIT:
                run = False
                username = ""
            #close nicely if the user presses the escape key
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
                username = ""
            elif backtomenuButton.handle_event(event):
                run = False
                username = ""
            elif event.type == pygame.KEYDOWN:
                #tabbing between textboxes
                if usernameTextbox.active and (event.key == pygame.K_TAB or event.key == pygame.K_RETURN):
                    usernameTextbox.active = False

            username = usernameTextbox.handle_event(event)
            
            if submitButton.handle_event(event):
                run = False

        #draw the white background
        win.fill((255,255,255))

        #draw textbox
        TitleBox.draw(win)
        usernameTitleBox.draw(win)
        usernameTextbox.draw(win)

        #draw button
        submitButton.draw(win)  
        backtomenuButton.draw(win)

        #update the screen
        pygame.display.update()
        clock.tick(FPS)
    
    return username

#########################################################
#########################################################
def pygame_message(msg):
    
    #initialise GUI objects
    TitleBox = TitleText(100, 10, 50, 50, "User login - Message...", RED)
    MessageBox = MultiLineText(100, 100, 400, 400, msg, BLACK, RED, 3, BLACK)    
    submitButton = Button(100, 500, 50, 50, "Continue", PURPLE, RED, 3, BLACK, BLUE)

    #make the username textbox active
    submitButton.active = True

    #loop until the user presses ESC key
    run = True

    #initialise keyboard input
    key = None
    
    while run == True:
        
        for event in pygame.event.get():
          
            #close nicely if the user closes the window
            if event.type == pygame.QUIT:
                run = False
            #close nicely if the user presses the escape key
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

            if submitButton.handle_event(event):
                run = False

        #draw the white background
        win.fill((255,255,255))

        #draw textbox
        TitleBox.draw(win)
        MessageBox.draw(win)  

        #draw button
        submitButton.draw(win)  

        #update the screen
        pygame.display.update()
        clock.tick(FPS)

#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
# MAIN PROGRAM

if __name__ == "__main__":

    width = 550
    height = 600

    #initialise the pygame font
    pygame.font.init()

    #initialise the window
    win = pygame.display.set_mode((width, height),RESIZABLE)

    #Title and Icon
    pygame.display.set_caption("WGS User Login")

    #initilise the font for text
    myFront = pygame.font.SysFont('comicsans', 40)

    #initialise the clock (how fast the screen updates)
    clock = pygame.time.Clock()


    userid = [""]
    while userid != ["close"]:
           
        ###Get user login
        userid = ["Error",""]
        while userid[0] == "Error":
            username, password = pygame_userlogin()
            if username != "":
                userid = userlogin(username,password)
                pygame_message(userid[0]+"\n\n"+userid[1])
            else:
                userid = ["close"]

        if userid != ["close"]:

            ###Show main menu
            option = ""
            while option != "Log out":
                option = pygame_menu()
                if option == "Show users":
                    pygame_showusers()
                elif option == "Add user":
                    userid = ["Error",""]
                    while userid[0] == "Error":
                        username, password1, password2 = pygame_adduser()
                        if username != "":
                            userid = adduser(username,password1,password2)
                            pygame_message(userid[0]+"\n\n"+userid[1])
                        else:
                            userid = ["back"]

                elif option == "Update user":
                    userid = ["Error",""]
                    while userid[0] == "Error":
                        username, password1, password2 = pygame_updateuser()
                        if username != "":
                            userid = adminupdateuser(username,password1,password2)
                            pygame_message(userid[0]+"\n\n"+userid[1])
                        else:
                            userid = ["back"]
                elif option == "Delete user":
                    userid = ["Error",""]
                    while userid[0] == "Error":
                        username = pygame_deleteuser()
                        if username != "":
                            userid = deleteuser(username)
                            pygame_message(userid[0]+"\n\n"+userid[1])
                        else:
                            userid = ["back"]
                elif option == "Log out":
                    print("Log out")
                else:
                    print("Error")

    ###End of program
    print("Goodbye")
    pygame.quit()
