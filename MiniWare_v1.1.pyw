import pygame
import sys
import time
import random
import os
import sys
from pygame.locals import *

## FOR EXE PURPOSES
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

######################################
#                                    #
#             CONSTANTS              #
#                                    #
######################################

FPS = 30  # frames per second, the general speed of the program
WINDOW_WIDTH = 1280  # size of windows' width in pixels
WINDOW_HEIGHT = 720  # size of windows' height in pixels

# Color constants and their RGB values
#               R    G    B
WHITE =       (255, 255, 255)
BLACK =       (  0,   0,   0)
RED =         (255,   0,   0)
DARK_RED =    (200,   0,   0)
PINK =        (255, 192, 193)
GREEN =       (  0, 255,   0)
DARK_GREEN =  (  0, 200,   0)
ORANGE =      (255, 172,  28)
DARK_ORANGE = (205, 127,  50)
BLUE =        (  0,   0, 255)
LIGHT_BLUE =  (  0, 128, 255)
PURPLE =      (128,   0, 128)
YELLOW =      (255, 255,   0)
GRAY =        (169, 169, 169)
DARK_GRAY =   (128, 128, 128)


BG_COLOR = WHITE
# FONT_FILE = 'freesansbold.ttf' # variable for font-type, change to any other one if necessary.
FONT_FILE = resource_path('Fonts/upheavtt.ttf')
FONT_SIZE = 32  # size of the font, change this number if needed.
SYMBOL_FONT_FILE = resource_path('Fonts/seguisym.ttf')
SYMBOL_FONT_SIZE = 100

# Ensures that there's no problems related to not starting pygame
pygame.init()
pygame.display.set_caption('MiniWare')


# Global constants
# makes the game run a certain speed using the FPS variable above
FPSCLOCK = pygame.time.Clock()
# the display size. Common values: 1920 x 1080, 1280 x 720, etc.
GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Determines how many rounds the player has to get through to win.
WIN_CONDITION = 10 

# Fonts
FONT = pygame.font.Font(FONT_FILE, FONT_SIZE)  # main font style/size
TIMER_FONT = pygame.font.Font(FONT_FILE, 60)
SYMBOL_FONT = pygame.font.Font(SYMBOL_FONT_FILE, SYMBOL_FONT_SIZE)
COUNTER_FONT = pygame.font.Font(FONT_FILE, 50)
BUTTON_FONT = pygame.font.Font(FONT_FILE, 30)

# Main Menu constants
MENUBUTTON_WIDTH = 125
MENUBUTTON_HEIGHT = 62.5

PLAY_STARTINGPOSX = WINDOW_WIDTH // 2.25
PLAY_STARTINGPOSY = (WINDOW_HEIGHT // 4) + 25

FREEPLAY_STARTINGPOSX = WINDOW_WIDTH // 2.25
FREEPLAY_STARTINGPOSY = PLAY_STARTINGPOSY + 95

OPTIONS_STARTINGPOSX = WINDOW_WIDTH // 2.25
OPTIONS_STARTINGPOSY = FREEPLAY_STARTINGPOSY + 95

EXIT_STARTINGPOSX = WINDOW_WIDTH // 2.25
EXIT_STARTINGPOSY = OPTIONS_STARTINGPOSY + 95

# Sounds
MENU_MUSIC = pygame.mixer.Sound(
    resource_path('Free Game Menu Music Pack/2. Bim Bom Bomp.wav'))
BUTTON_CLICK_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Select.wav'))
EXIT_BUTTON_CLICK_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Menu Close.wav'))
FREEPLAY_BUTTON_CLICK_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Menu Open.wav'))
OPTIONS_BUTTON_CLICK_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Equip.wav'))
EXIT_CONFIRMATION_BUTTON_CLICK_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Menu Exit.wav'))
TIME_UP_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Invalid Select.wav'))

WIN_SFX = pygame.mixer.Sound(resource_path('Sound Effects/P4G SLINK SFX/Misc/Win.wav'))
LOSS_SFX = pygame.mixer.Sound(resource_path('Sound Effects/P4G SLINK SFX/Misc/Loss.wav'))

ULTIMATE_WIN_SFX = pygame.mixer.Sound(resource_path('Sound Effects/P4G SLINK SFX/Ultimate Win.wav'))
ULTIMATE_LOSS_SFX = pygame.mixer.Sound(resource_path('Sound Effects/Sad Trombone.wav'))


CORRECT_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4G SLINK SFX/Social Link/Stats Increase 1.wav'))
WRONG_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/Shuffle Time/P4 ST Penalty.wav'))


TYPE_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Hover.wav'))
BACKSPACE_SFX = pygame.mixer.Sound(
    resource_path('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Menu Flip.wav'))

AUDIO_LIST = [BUTTON_CLICK_SFX, EXIT_BUTTON_CLICK_SFX, FREEPLAY_BUTTON_CLICK_SFX, OPTIONS_BUTTON_CLICK_SFX, EXIT_CONFIRMATION_BUTTON_CLICK_SFX,
              WIN_SFX, LOSS_SFX, CORRECT_SFX, WRONG_SFX, TYPE_SFX, BACKSPACE_SFX, TIME_UP_SFX, ULTIMATE_WIN_SFX]
MUSIC_LIST = [MENU_MUSIC]  # If I want to add different music, put it in here
# Images
W_SOUND_BARS = 52  # Actual dimensions of the image
H_SOUND_BARS = 12
SOUND_BARS = pygame.image.load(resource_path('Images/sound_bars.png'))
SOUND_BARS_RESIZED = pygame.transform.scale(
    SOUND_BARS, (W_SOUND_BARS * 5, H_SOUND_BARS * 5))


W_BLACK_BAR = 6  # Actual dimensions of the image
H_BLACK_BAR = 12
BLACK_BAR = pygame.image.load(resource_path('Images/black_bar.png'))
BLACK_BAR_RESIZED = pygame.transform.scale(
    BLACK_BAR, (W_BLACK_BAR * 5, H_SOUND_BARS * 5))

# Dimensions of the heart sprites, just in case
W_HEARTS = 17
H_HEARTS = 17

##############################
# TIC-TAC-TOE GAME CONSTANTS #
##############################

# Thumbnail for Freeplay Mode
# TICTACTOE_IMAGE = pygame.image.load("tictactoe_screenshot.png") Unremark once game is ready
TICTACTOE_IMAGE = pygame.image.load(resource_path("tictactoe_screenshot.png"))
TICTACTOE_IMAGE_THUMBNAIL = pygame.transform.scale(TICTACTOE_IMAGE, (225, 200))

########################
# LOGIC GAME CONSTANTS #
########################

# Thumbnail for Freeplay Mode
LOGIC_IMAGE = pygame.image.load(resource_path("logic_screenshot.png"))
LOGIC_IMAGE_THUMBNAIL = pygame.transform.scale(LOGIC_IMAGE, (225, 200))

# Starting x&y coordinates of the buttons
LOGIC_X_STARTBUTTON = 350
LOGIC_Y_STARTBUTTON = 300
LOGIC_X_EXITBUTTON = 550
LOGIC_Y_EXITBUTTON = 300

# Width and height of the buttons
LOGIC_W_STARTBUTTON = 100
LOGIC_H_STARTBUTTON = 50
LOGIC_W_EXITBUTTON = 100
LOGIC_H_EXITBUTTON = 50

# Width and height of the input box
LOGIC_W_INPUT_BOX = 250
LOGIC_H_INPUT_BOX = 50

# Starting x&y coordinates of the input box
LOGIC_X_INPUT_BOX = (WINDOW_WIDTH // 2) - (LOGIC_W_INPUT_BOX // 2)
LOGIC_Y_INPUT_BOX = WINDOW_HEIGHT // 2

NOFILL = 1  # width value when drawing a circle. 1 = no fill
FILL = 0  # width value when drawing a circle. 0 = fill

THOUSANDS_DIGIT = random.randint(1,9)
THOUSANDS_DIGIT_2 = random.randint(1,9)

HUNDREDS_DIGIT = random.randint(0,9)
HUNDREDS_DIGIT_2 = random.randint(0,9)
HUNDREDS_DIGIT_NOZERO = random.randint(1,9)

TENS_DIGIT = random.randint(0,9)
TENS_DIGIT_2 = random.randint(0,9)
TENS_DIGIT_NOZERO = random.randint(1,9)

SINGLES_DIGIT = random.randint(0,9)
SINGLES_DIGIT_2 = random.randint(0,9)
SINGLES_DIGIT_NOZERO = random.randint(1,9)

EASY_MATH_PROBLEMS = {'Addition': f'{SINGLES_DIGIT}+10 {TENS_DIGIT_NOZERO}0+82 {TENS_DIGIT_NOZERO}5+212 {SINGLES_DIGIT}+8 {TENS_DIGIT_NOZERO}2+186 {TENS_DIGIT_NOZERO}5+37 {TENS_DIGIT_NOZERO}2+29 1{HUNDREDS_DIGIT}{TENS_DIGIT}2+28 '.split(),
                      'Subtraction': f'{SINGLES_DIGIT}-2 1{TENS_DIGIT}8-33 {HUNDREDS_DIGIT_NOZERO}81-342 {TENS_DIGIT_NOZERO}7-62 10{THOUSANDS_DIGIT}{HUNDREDS_DIGIT}34-0 82{TENS_DIGIT}{SINGLES_DIGIT}-{TENS_DIGIT}{SINGLES_DIGIT} {TENS_DIGIT_NOZERO}8-2 2192829-{SINGLES_DIGIT} -5-(-2{TENS_DIGIT}9)'.split(),
                      'Multiplication': f'{SINGLES_DIGIT}*3 {THOUSANDS_DIGIT}{HUNDREDS_DIGIT}{TENS_DIGIT}{SINGLES_DIGIT}*2 33*{SINGLES_DIGIT} {SINGLES_DIGIT}*7 {TENS_DIGIT_NOZERO}0*3 {THOUSANDS_DIGIT}2830*0 {TENS_DIGIT_NOZERO}{SINGLES_DIGIT}*0.5 116*4'.split(),
                      'Division': f'243/3 139{THOUSANDS_DIGIT}{HUNDREDS_DIGIT}{TENS_DIGIT}{SINGLES_DIGIT}/1 {HUNDREDS_DIGIT_NOZERO}40/4 48/6 121/11 388/0 990/9 1111{THOUSANDS_DIGIT}{HUNDREDS_DIGIT_NOZERO}1110/10'.split()}

# Dodging game constants

# Reaction game constants

##############################
# WORD TYPING GAME CONSTANTS #
##############################

# Thumbnail for Freeplay mode
WORDTYPE_IMAGE = pygame.image.load(resource_path('wordtype_screenshot.png'))
WORDTYPE_IMAGE_THUMBNAIL = pygame.transform.scale(WORDTYPE_IMAGE, (225, 200))

# Game constants

# Input box dimensions and x&y coordinate positions
X_CHANGE_INPUTBOX = 125
X_INPUTBOX = ((WINDOW_WIDTH // 2) - X_CHANGE_INPUTBOX)
Y_INPUTBOX = WINDOW_HEIGHT // 2
W_INPUTBOX = X_CHANGE_INPUTBOX * 2
H_INPUTBOX = 50

WORDS = ['banana', 'apple', 'door', 'videogames', 'onomatopeia', 'knowledge', 'pettiness',
         'trigonometry', 'extravaganza', 'melodies', 'ethereal']

################################
#   BUTTONMASH GAME CONSTANTS  #
################################

# Thumbnail for Freeplay mode
BUTTONMASH_IMAGE = pygame.image.load(resource_path('buttonmash_screenshot.png')) #Unremark once it is playable.
BUTTONMASH_IMAGE_THUMBNAIL = pygame.transform.scale(
    BUTTONMASH_IMAGE, (225, 200))

# creates a list variable to hold the home row keys
LETTERS = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
# Starting x&y coordinates of the buttons for the ButtonMashing game
X_STARTBUTTON = 350
Y_STARTBUTTON = 300
X_EXITBUTTON = 550
Y_EXITBUTTON = 300

# Width and height of the buttons for the ButtonMashing game
W_STARTBUTTON = 100
H_STARTBUTTON = 50
W_EXITBUTTON = 100
H_EXITBUTTON = 50


#############################
# DISAPPEARING #S CONSTANTS #
#############################

# Thumbnail for Freeplay mode
#DISAPPEARING_IMAGE = pygame.image.load('disappearing_screenshot.png') Unremark once it is playable.
DISAPPEARING_IMAGE = pygame.image.load(resource_path('disappearing_screenshot.png'))
DISAPPEARING_IMAGE_THUMBNAIL = pygame.transform.scale(
    DISAPPEARING_IMAGE, (225, 200))

# Game constants
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
          '11','12','13','14','15','16','17','18','19', '20']

QUESTIONS = ['Which number was 1st on the left?', 'Which number was in the middle?', 'Which number was 1st on the right?',
'How many numbers were single-digit?', 'How many numbers were double-digit?']

#############################
# COLORED CIRCLES CONSTANTS #
#############################

# Thumbnial for Freeplay mode
COLOREDCIRCLES_IMAGE = pygame.image.load(resource_path('coloredcircles_screenshot.png'))
COLOREDCIRCLES_IMAGE_THUMBNAIL = pygame.transform.scale(
    COLOREDCIRCLES_IMAGE, (225, 200))

# Game constants
CIRCLE_SIZE = 20  # how large the radius of a circle will be
# the outline of the circle is always a half-size larger no-fill circle.
CIRCLE_OUTLINE = CIRCLE_SIZE + 0.5

NOFILL = 1  # width value when drawing a circle. 1 = no fill
FILL = 0  # width value when drawing a circle. 0 = fill

COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, PINK, PURPLE]
COLORS_STRING_LIST = ['red', 'green', 'blue',
                      'yellow', 'orange', 'black', 'pink', 'purple']

######################################
#                                    #
#              CLASSES               #
#                                    #
######################################

soundPlayed = False


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        # Frog images dimensions
        self.sprites_width = 128
        self.sprites_height = 64

        # self.sprites.append(test_scaled)
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_1.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_2.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_3.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_4.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_5.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_6.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_7.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_8.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_9.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Frog/attack_10.png')))

        # Scales the images to be bigger or smaller.
        for i in range(len(self.sprites)):
            image = self.sprites[i]
            self.sprites[i] = pygame.transform.scale(
                image, (self.sprites_width * 2, self.sprites_height * 2))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]


class Hp(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        # Heart images dimensions
        self.sprites_width = 17
        self.sprites_height = 17

        self.sprites.append(pygame.image.load(resource_path('Sprites/Hearts/Empty.png')))
        self.sprites.append(pygame.image.load(
            resource_path('Sprites/Hearts/One-Fourth Full.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Hearts/Half Full.png')))
        self.sprites.append(pygame.image.load(
            resource_path('Sprites/Hearts/Three-Fourths Full.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Hearts/Full.png')))

        # Scales the images to be bigger or smaller.
        for i in range(len(self.sprites)):
            image = self.sprites[i]
            self.sprites[i] = pygame.transform.scale(
                image, (self.sprites_width * 3, self.sprites_height * 3))

        self.current_sprite = 4
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

class SpriteButton(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        # Heart images dimensions
        self.sprites_width = 19
        self.sprites_height = 19

        self.sprites.append(pygame.image.load(resource_path('Sprites/Kenney/Red Button - Unpressed.png')))
        self.sprites.append(pygame.image.load(resource_path('Sprites/Kenney/Red Button - Pressed.png')))

        # Scales the images to be bigger or smaller.
        for i in range(len(self.sprites)):
            image = self.sprites[i]
            self.sprites[i] = pygame.transform.scale(
                image, (self.sprites_width * 3, self.sprites_height * 3))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]


class FullHp(pygame.sprite.Sprite):
    # Sprite animation that shows when a heart is full.
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        # Heart images dimensions
        self.sprites_width = 17
        self.sprites_height = 17

        self.sprites.append(pygame.image.load(
            resource_path('Sprites/Edited Hearts/Full - Frame 1.png')))
        self.sprites.append(pygame.image.load(
            resource_path('Sprites/Edited Hearts/Full - Frame 2.png')))
        self.sprites.append(pygame.image.load(
            resource_path('Sprites/Edited Hearts/Full - Frame 3.png')))
        self.sprites.append(pygame.image.load(
            resource_path('Sprites/Edited Hearts/Full - Frame 4.png')))

        # Scales the images to be bigger or smaller.
        for i in range(len(self.sprites)):
            image = self.sprites[i]
            self.sprites[i] = pygame.transform.scale(
                image, (self.sprites_width * 3, self.sprites_height * 3))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]


class Button:
    # Creates an animated button that also detects if a player has
    # changed their mind about clicking a button (clicked then hovered away registers
    # nothing.)

    # Attributes:
    # self = the class itself (Button)
    # text = string that will be shown on the top button
    # width = length of both top and lower button
    # height = height of both top and lower button
    # pos = [tuple] x & y coordinates of the top button
    # elevation = height of the lower button
    # action = the function that will be called when the player clicks on the button
    def __init__(self, text, width, height, pos, elevation, click_sound, action=None):
        # Core attributes
        self.pressed = False
        self.hovered = False
        self.elevation = elevation  # the lower button's height
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.action = action
        #self.hover_sound = pygame.mixer.Sound('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Hover.wav')

        self.click_sound = click_sound
        # self.click_sound.set_volume(0.8) # Change this value to affect how loud or quiet it is. (0 - 1)

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        # change this to whatever color I want when I use it for TimeWaster
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#354B5E'

        # text
        self.text_surf = BUTTON_FONT.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # Elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(GAME_WINDOW, self.bottom_color,
                         self.bottom_rect, border_radius=12)
        # change to GAME_WINDOW obviously later on
        pygame.draw.rect(GAME_WINDOW, self.top_color,
                         self.top_rect, border_radius=12)
        GAME_WINDOW.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        self.top_color = '#475F77'
        # Checks if the cursor is over the button
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'  # again, change this to a color I want
            if pygame.mouse.get_pressed()[0]:  # If player left clicks
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.click_sound.play()
                    self.call_back()
                    self.pressed = False
        elif not self.top_rect.collidepoint(mouse_pos):
            self.pressed = False
            self.dynamic_elevation = self.elevation

    def call_back(self, *args):
        if self.action:
            return self.action(*args)
        
class HiddenButton:
    # Creates an animated button that also detects if a player has
    # changed their mind about clicking a button (clicked then hovered away registers
    # nothing.)
    # Special feature: it is "hidden" until the player hovers over it.

    # Attributes:
    # self = the class itself (Button)
    # text = string that will be shown on the top button
    # width = length of both top and lower button
    # height = height of both top and lower button
    # pos = [tuple] x & y coordinates of the top button
    # elevation = height of the lower button
    # action = the function that will be called when the player clicks on the button
    def __init__(self, text, width, height, pos, elevation, click_sound, action=None):
        # Core attributes
        self.pressed = False
        self.hovered = False
        self.elevation = elevation  # the lower button's height
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.action = action
        #self.hover_sound = pygame.mixer.Sound('Sound Effects/P4 MENU UI SFX REDUX/UI/P4 Hover.wav')

        self.click_sound = click_sound
        # self.click_sound.set_volume(0.8) # Change this value to affect how loud or quiet it is. (0 - 1)

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        # change this to whatever color I want when I use it for TimeWaster
        self.top_color = WHITE

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = WHITE

        # text
        self.text_surf = BUTTON_FONT.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # Elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(GAME_WINDOW, self.bottom_color,
                         self.bottom_rect, border_radius=12)
        # change to GAME_WINDOW obviously later on
        pygame.draw.rect(GAME_WINDOW, self.top_color,
                         self.top_rect, border_radius=12)
        GAME_WINDOW.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        self.top_color = WHITE
        self.bottom_color = WHITE
        # Checks if the cursor is over the button
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'  # again, change this to a color I want
            self.bottom_color = '#354B5E'
            if pygame.mouse.get_pressed()[0]:  # If player left clicks
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.click_sound.play()
                    self.call_back()
                    self.pressed = False
        elif not self.top_rect.collidepoint(mouse_pos):
            self.pressed = False
            self.dynamic_elevation = self.elevation

    def call_back(self, *args):
        if self.action:
            return self.action(*args)

######################################
#                                    #
#          GLOBAL VARIABLES          #
#                                    #
######################################

# Place all global variables here later

#~~~~~~~~~~~~~~~~~~~~~~#
# LOGIC GAME VARIABLES #
#~~~~~~~~~~~~~~~~~~~~~~#


# boolean values that only change if the player doesn't solve a problem in time.
timeUp_solving_firstProblem = False
# True = didn't solve that problem in time. False = solved in time.
timeUp_solving_secondProblem = False
timeUp_solving_thirdProblem = False
chosenProblems = []

#~~~~~~~~~~~~~~~~~~~~~~#
# BUTTONMASH VARIABLES #
#~~~~~~~~~~~~~~~~~~~~~~#

# Variables to hold the button mashes
a_count = 0
s_count = 0
d_count = 0
f_count = 0
g_count = 0
h_count = 0
j_count = 0
k_count = 0
l_count = 0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# COLORED CIRCLES VARIABLES #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~#

randomColor1 = random.choice(COLORS)
# Ensures that there's no duplicates of colors. Make sure to reset it in the resetValues() function
COLORS.remove(randomColor1)
randomColor2 = random.choice(COLORS)
COLORS.remove(randomColor2)
randomColor3 = random.choice(COLORS)
COLORS.remove(randomColor3)
randomColor4 = random.choice(COLORS)
COLORS.remove(randomColor4)
randomColor5 = random.choice(COLORS)
COLORS.remove(randomColor5)
randomColor6 = random.choice(COLORS)
COLORS.remove(randomColor6)
randomColor7 = random.choice(COLORS)
COLORS.remove(randomColor7)
randomColor8 = random.choice(COLORS)
COLORS.remove(randomColor8)

# Putting the chosen numbers in a new list to be randomized when displayed
chosenColors = [randomColor1, randomColor2, randomColor3,
                randomColor4, randomColor5, randomColor6, randomColor7, randomColor8]
chosenColors_string_list = []
# For loop is called here for the 1st question to work. I might modify this in the future to look cleaner but this is my solution as of now
for x in chosenColors:
    if x == RED:
        chosenColors_string_list.append(COLORS_STRING_LIST[0].upper())
    elif x == GREEN:
        chosenColors_string_list.append(COLORS_STRING_LIST[1].upper())
    elif x == BLUE:
        chosenColors_string_list.append(COLORS_STRING_LIST[2].upper())
    elif x == YELLOW:
        chosenColors_string_list.append(COLORS_STRING_LIST[3].upper())
    elif x == ORANGE:
        chosenColors_string_list.append(COLORS_STRING_LIST[4].upper())
    elif x == BLACK:
        chosenColors_string_list.append(COLORS_STRING_LIST[5].upper())
    elif x == PINK:
        chosenColors_string_list.append(COLORS_STRING_LIST[6].upper())
    elif x == PURPLE:
        chosenColors_string_list.append(COLORS_STRING_LIST[7].upper())

questionColor = random.choice(chosenColors_string_list)

# QUESTIONS is turned into questions since the 1st question doesn't remain constant.
questions = [f'What row did {questionColor} appear on?', 'What color was in the top left?',
             'What color was on the bottom right?', 'What color was second from the top left?', 'What color was second from the top right?']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#   WORD TYPING VARIABLES   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# boolean values that only change if the player doesn't spell a word in time.
timeUp_spellingFirstWord = False
# True = didn't spell that word in time. False = spelled in time.
timeUp_spellingSecondWord = False
timeUp_spellingThirdWord = False
chosenWords = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#  DISAPPEARING # VARIABLES  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Player's input (empty because it will either be A, B, C, or D)
playerAnswer = ''
chosen_number_list = [] # list that will be appended every time the game is ran
single_digits_list = [] # list that will be appended for the single-digit question
double_digits_list = [] # list that will be appended for the double-digit question

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#    ESSENTIAL VARIABLES    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Gamemode variables
# Variable that checks if the player has played the gamemode once or not.
# True = 1st time playing this session. False = played more than once already.
first_play = True

# Variable that checks if the player is in Freeplay mode. 
# True = changes how the minigames function at the end. False = nothing changes.
freeplay_mode = False

# Main game variables
minigame_count = 0
win_count = 0
loss_count = 0
hp = 3  # Starting health of the player
win_has_been_called = False  # Checks if a minigame win has occured
loss_has_been_called = False  # Checks if a minigame loss has occured


game_audio_lvl = 0.6
music_lvl = 0.5

# Setting the volume of every sound to their corresponding levels.
for x in AUDIO_LIST:
    x.set_volume(game_audio_lvl)

for x in MUSIC_LIST:
    x.set_volume(music_lvl)

MENU_MUSIC.set_volume(music_lvl)

######################################
#                                    #
#             FUNCTIONS              #
#                                    #
######################################

# ~~~~~~~~~~~~~~~~~~~~~#
# ESSENTIAL FUNCTIONS #
# ~~~~~~~~~~~~~~~~~~~~~#

def timeUp():
    # Displays "Time's up!" once the countdown timer is finished.
    TIME_UP_SFX.play()
    timeUpFont = pygame.font.Font(FONT_FILE, 100)
    timeUpText = timeUpFont.render('Time\'s up!', True, BLACK, None)
    timeUpTextRect = timeUpText.get_rect()
    timeUpTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    GAME_WINDOW.fill(BG_COLOR)
    GAME_WINDOW.blit(timeUpText, timeUpTextRect)
    transition(1, 1)


def getRandom(list):
    # Picks a random list item from the selected list and returns its value.
    randomChoice = random.choice(list)
    return randomChoice


def drawProgress(progress, outcome, outcome_2, outcome_3):  # Used by Logic and Word Type
    # Adds 3 blank circles to the bottom right of the screen that represent how many words the
    # player has spelled right or wrong/solved correctly or incorrectly. A blank circle means that the player hasn't spelled the current word/solved the problem.

    # Progress = checks if the player spelt the 1st/2nd/or 3rd word // solved the 1st/2nd/or 3rd problem.
    # Outcome = checks if the player spelt the word correctly/solved the problem correctly or not.
    # Outcome_2 = checks if the player spelt the 2nd word correctly/solved the 2nd problem correctly or not
    # Outcome_3 = checks if the player spelt the 3rd word correctly/solved the 3rd problem correctly or not

    # Values to display the progress of the player
    smallSymbolText = pygame.font.Font(SYMBOL_FONT_FILE, 50)

    displayCheck1 = smallSymbolText.render('✓', True, GREEN, None)
    displayCheck1Rect = displayCheck1.get_rect()
    displayCheck1Rect.center = (WINDOW_WIDTH - 130, WINDOW_HEIGHT - 32)

    displayCheck2 = smallSymbolText.render('✓', True, GREEN, None)
    displayCheck2Rect = displayCheck2.get_rect()
    displayCheck2Rect.center = (WINDOW_WIDTH - 80, WINDOW_HEIGHT - 32)

    displayCheck3 = smallSymbolText.render('✓', True, GREEN, None)
    displayCheck3Rect = displayCheck3.get_rect()
    displayCheck3Rect.center = (WINDOW_WIDTH - 30, WINDOW_HEIGHT - 32)

    displayXMark1 = smallSymbolText.render('❌', True, RED, None)
    displayXMark1Rect = displayXMark1.get_rect()
    displayXMark1Rect.center = (WINDOW_WIDTH - 130, WINDOW_HEIGHT - 32)

    displayXMark2 = smallSymbolText.render('❌', True, RED, None)
    displayXMark2Rect = displayXMark2.get_rect()
    displayXMark2Rect.center = (WINDOW_WIDTH - 80, WINDOW_HEIGHT - 32)

    displayXMark3 = smallSymbolText.render('❌', True, RED, None)
    displayXMark3Rect = displayXMark3.get_rect()
    displayXMark3Rect.center = (WINDOW_WIDTH - 30, WINDOW_HEIGHT - 32)

    radius = 20  # circle radius
    # 1st word is being spelled/problem is being solved (◯◯◯)
    if progress == 1 and outcome == None:
        # radius is subtracted from the dimensions to make the circle appear on screen
        pygame.draw.circle(GAME_WINDOW, BLACK, ((
            WINDOW_WIDTH - radius) - 110, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
        pygame.draw.circle(GAME_WINDOW, BLACK, ((
            WINDOW_WIDTH - radius) - 60, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
        pygame.draw.circle(GAME_WINDOW, BLACK, ((
            WINDOW_WIDTH - radius) - 10, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)

    # All conditions that check if the player types all words/solved all problems correctly and incorrectly
    if progress == 2:  # 2nd word is being spelled/2nd problem is being solved
        if outcome == True:  # ✓◯◯
            GAME_WINDOW.blit(displayCheck1, displayCheck1Rect)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH - radius) - 60, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH - radius) - 10, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
        elif outcome == False:  # ❌◯◯
            GAME_WINDOW.blit(displayXMark1, displayXMark1Rect)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH - radius) - 60, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH - radius) - 10, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
    elif progress == 3:  # 3rd word is being spelled/3rd problem is being solved
        if outcome == True and outcome_2 == True:  # ✓✓◯
            GAME_WINDOW.blit(displayCheck1, displayCheck1Rect)
            GAME_WINDOW.blit(displayCheck2, displayCheck2Rect)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH - radius) - 10, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
        elif outcome == True and outcome_2 == False:  # ✓❌◯
            GAME_WINDOW.blit(displayCheck1, displayCheck1Rect)
            GAME_WINDOW.blit(displayXMark2, displayXMark2Rect)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH - radius) - 10, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
        elif outcome == False and outcome_2 == True:  # ❌✓◯
            GAME_WINDOW.blit(displayXMark1, displayXMark1Rect)
            GAME_WINDOW.blit(displayCheck2, displayCheck2Rect)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH - radius) - 10, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
        elif outcome == False and outcome_2 == False:  # ❌❌◯
            GAME_WINDOW.blit(displayXMark1, displayXMark1Rect)
            GAME_WINDOW.blit(displayXMark2, displayXMark2Rect)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH - radius) - 10, (WINDOW_HEIGHT - radius) - 10), radius, NOFILL)
    elif progress == 4:  # Done spelling/solving
        # if outcome == True and outcome_2 == True and outcome_3 == True:        #✓✓✓
        #     GAME_WINDOW.blit(displayCheck1, displayCheck1Rect)
        #     GAME_WINDOW.blit(displayCheck2, displayCheck2Rect)
        #     GAME_WINDOW.blit(displayCheck3, displayCheck3Rect)
        # elif outcome == True and outcome_2 == True and outcome_3 == False:    #✓✓❌
        #     GAME_WINDOW.blit(displayCheck1, displayCheck1Rect)
        #     GAME_WINDOW.blit(displayCheck2, displayCheck2Rect)
        #     GAME_WINDOW.blit(displayXMark3, displayXMark3Rect)
        if outcome == True and outcome_2 == False and outcome_3 == False:  # ✓❌❌
            GAME_WINDOW.blit(displayCheck1, displayCheck1Rect)
            GAME_WINDOW.blit(displayXMark2, displayXMark2Rect)
            GAME_WINDOW.blit(displayXMark3, displayXMark3Rect)
        # elif outcome == False and outcome_2 == False and outcome_3 == False:  #❌❌❌
        #     GAME_WINDOW.blit(displayXMark1, displayXMark1Rect)
        #     GAME_WINDOW.blit(displayXMark2, displayXMark2Rect)
        #     GAME_WINDOW.blit(displayXMark3, displayXMark3Rect)
        # elif outcome == False and outcome_2 == False and outcome_3 == True:   #❌❌✓
        #     GAME_WINDOW.blit(displayXMark1, displayXMark1Rect)
        #     GAME_WINDOW.blit(displayXMark2, displayXMark2Rect)
        #     GAME_WINDOW.blit(displayCheck3, displayCheck3Rect)
        elif outcome == False and outcome_2 == True and outcome_3 == True:  # ❌✓✓
            GAME_WINDOW.blit(displayXMark1, displayXMark1Rect)
            GAME_WINDOW.blit(displayCheck2, displayCheck2Rect)
            GAME_WINDOW.blit(displayCheck3, displayCheck3Rect)
        elif outcome == True and outcome_2 == False and outcome_3 == True:  # ✓❌✓
            GAME_WINDOW.blit(displayCheck1, displayCheck1Rect)
            GAME_WINDOW.blit(displayXMark2, displayXMark2Rect)
            GAME_WINDOW.blit(displayCheck3, displayCheck3Rect)
        elif outcome == False and outcome_2 == True and outcome_3 == False:  # ❌✓❌
            GAME_WINDOW.blit(displayXMark1, displayXMark1Rect)
            GAME_WINDOW.blit(displayCheck2, displayCheck2Rect)
            GAME_WINDOW.blit(displayXMark3, displayXMark3Rect)

def showRandomQuestion(list):
    # Shows a random question to the player from the selected list.
    global chosenQuestion  # has to be here or the code won't work
    # Picks a random question from the selected list
    chosenQuestion = getRandom(list)
    # chosenQuestion = questions[0] # Picks a random question from the selected list
    # change QUESTIONS[#] to getRandom(QUESTIONS) to return it to its randomized state

    # Values to display the question onto the screen
    QuestionFont = pygame.font.Font(FONT_FILE, 48)
    displayQuestion = QuestionFont.render(chosenQuestion, True, BLACK, None)
    displayQuestionRect = displayQuestion.get_rect()
    displayQuestionRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    GAME_WINDOW.blit(displayQuestion, displayQuestionRect)
    pygame.display.update()
    transition(3, 0)  # 3 seconds first timer, no second timer

# FOCUS ON THIS ANOTHER TIME


## FUTURE PLANS
def selectDifficulty():
    # Lets the player determine how difficult their session will be.
    pass

# ~~~~~~~~~~~~~~~~~~~~~~#
# LOGIC GAME FUNCTIONS #
# ~~~~~~~~~~~~~~~~~~~~~~#


def getRandomProblem(problemDict):
    # Function that will pick a random problem from the dictionary above and return the selected problem.
    # Got from a tutorial on making hangman: https://inventwithpython.com/invent4thed/chapter9.html
    # Randomly select a key from the dictionary
    problemKey = random.choice(list(problemDict.keys()))

    # Randomly select a word from the key's list in the dictionary:
    problemIndex = random.randint(0, len(problemDict[problemKey]) - 1)
    return problemDict[problemKey][problemIndex]
    # return problemDict['Subtraction'][0]


def decide_on_a_problem(numOfCycles):
    # Shows an animation of the program randomly cycling through the problems and then stops at
    # after x amount of cycles.

    while numOfCycles > 0:
        # the chosenLetter variables are meant for drawing the letter on the screen
        cyclingThroughProblemsFont = pygame.font.Font(FONT_FILE, 50)
        cyclingThroughProblems = cyclingThroughProblemsFont.render(getRandomProblem(
            EASY_MATH_PROBLEMS), True, BLACK, WHITE)  # variable for how the text will look
        cyclingThroughProblemsRect = cyclingThroughProblems.get_rect()
        cyclingThroughProblemsRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        # need to make it so that the previous blit will be erased before the next blit occurs
        GAME_WINDOW.blit(cyclingThroughProblems, cyclingThroughProblemsRect)

        pygame.display.update()
        time.sleep(0.02)
        GAME_WINDOW.fill(BG_COLOR)  # "removes" the blit to prevent overlapping
        pygame.display.update()  # second update to show the the "removal"
        FPSCLOCK.tick(FPS)
        # keeps subtracting the parameter and stops the loop when it reaches 0
        numOfCycles = numOfCycles - 1


def LOGIC_resetValues():
    # Resets all the important values to their original states after a win or loss.
    global solving_firstProblem, solving_secondProblem, solving_thirdProblem, doneSolving, timeUp_solving_firstProblem, timeUp_solving_secondProblem, timeUp_solving_thirdProblem, firstAnswer, secondAnswer, thirdAnswer
    # Variables that change depending on which problem the player is solving.
    # Restarting back to solving a new first problem.
    solving_firstProblem = True
    solving_secondProblem = False
    solving_thirdProblem = False
    doneSolving = False

    # Variables that change if the player doesn't solve one of the problems in time.
    timeUp_solving_firstProblem = False
    timeUp_solving_secondProblem = False
    timeUp_solving_thirdProblem = False

    # Variables that store the player's answers.
    firstAnswer = None
    secondAnswer = None
    thirdAnswer = None

    # List that holds the 3 words the player will spell.
    chosenProblems.clear()  # Reverts it back to its blank state.


def LOGIC_win():
    # Shows the player that they won and applies all the win rewards.
    global win_has_been_called
    win_has_been_called = True
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 1)
    pygame.mixer.Channel(4).pause()# Pause the background music as the Win SFX is playing.
    WIN_SFX.play()  # Plays the winning theme.
    transition(0, 0.2)
    winTextFont = pygame.font.Font(FONT_FILE, 100)
    winText = winTextFont.render('You won!', True, BLACK, None)
    winTextRect = winText.get_rect()
    winTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(winText, winTextRect)
    transition(3, 1)
    LOGIC_resetValues()
    winState() # Show the overall stats of the player before the next minigame.
    # startMenu()


def LOGIC_loss():
    # Shows the player that they won and applies all the win rewards.
    global loss_has_been_called
    loss_has_been_called = True
    pygame.mixer.Channel(4).pause()# Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the losing theme.
    transition(0, 0.2)
    lossTextFont = pygame.font.Font(FONT_FILE, 100)
    lossText = lossTextFont.render('You lost!', True, BLACK, None)
    lossTextRect = lossText.get_rect()
    lossTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(lossText, lossTextRect)
    transition(3, 1)
    LOGIC_resetValues()
    lossState()
    # startMenu()

def LOGIC_freeplay_win():
    # Same as the regular win but asks if the player wants to play again.
    global win_has_been_called
    win_has_been_called = True
    winning = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, LOGIC)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    
    WIN_SFX.play() # Plays the winning theme
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    transition(0, 0.2)
    LOGIC_resetValues()
    while winning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        winTextFont = pygame.font.Font(FONT_FILE, 100)
        winText = winTextFont.render('You won!', True, BLACK, None)
        winTextRect = winText.get_rect()
        winTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(winText, winTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def LOGIC_freeplay_loss():
    # Same as the regular loss but asks if the player wants to play again.
    global loss_has_been_called
    loss_has_been_called = True
    losing = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, LOGIC)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the losing theme.
    transition(0, 0.2)
    LOGIC_resetValues()
    while losing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        lossTextFont = pygame.font.Font(FONT_FILE, 100)
        lossText = lossTextFont.render('You lost!', True, BLACK, None)
        lossTextRect = lossText.get_rect()
        lossTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(lossText, lossTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def ready_set_solve():
    # Displays the three words "Ready...", "Set..." "Type!" in quick succession
    readyFont = pygame.font.Font(FONT_FILE, 80)
    readyText = readyFont.render('Ready...', True, BLACK, None)
    readyTextRect = readyText.get_rect()
    readyTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(readyText, readyTextRect)
    transition(1, 0.2)

    setTextFont = pygame.font.Font(FONT_FILE, 140)
    setText = setTextFont.render('Set...', True, BLACK, None)
    setTextRect = setText.get_rect()
    setTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(setText, setTextRect)
    transition(1, 0.2)

    typeTextFont = pygame.font.Font(FONT_FILE, 200)
    typeText = typeTextFont.render('SOLVE!', True, BLACK, None)
    typeTextRect = typeText.get_rect()
    typeTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(typeText, typeTextRect)
    transition(1, 0.2)


def LOGIC_checkUserInput(correctAnswer, userAnswer):
    # Checks the player input after they hit enter on the text box.
    # Values that will display if the player is correct or wrong
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 1)
    displayCorrect = FONT.render('Correct!', True, BLACK, None)
    displayCorrectRect = displayCorrect.get_rect()
    # Exact location as the instructions, as it will replace it once the player answers
    displayCorrectRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    displayCheck = SYMBOL_FONT.render('✓', True, GREEN, None)
    displayCheckRect = displayCheck.get_rect()
    displayCheckRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    displayWrong = FONT.render('Wrong!', True, BLACK, None)
    displayWrongRect = displayWrong.get_rect()
    # Exact location as the instructions, as it will replace it once the player answers
    displayWrongRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    displayXMark = SYMBOL_FONT.render('❌', True, RED, None)
    displayXMarkRect = displayXMark.get_rect()
    displayXMarkRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    global correct, firstAnswer, secondAnswer, thirdAnswer
    correct = None
    # FOCUS ON THIS NEXT TIME
    # Checks if the player typed the word correctly
    if userAnswer == correctAnswer:
        CORRECT_SFX.play()
        correct = True
        if solving_firstProblem:
            firstAnswer = correct
        elif solving_secondProblem:
            secondAnswer = correct
        elif solving_thirdProblem:
            thirdAnswer = correct
        GAME_WINDOW.fill(BG_COLOR)
        GAME_WINDOW.blit(displayCheck, displayCheckRect)
        GAME_WINDOW.blit(displayCorrect, displayCorrectRect)
        pygame.display.update()
        transition(1, 0)

    # Checks if the player typed the word incorrectly
    elif userAnswer != correctAnswer:
        WRONG_SFX.play()
        correct = False
        if solving_firstProblem:
            firstAnswer = correct
        elif solving_secondProblem:
            secondAnswer = correct
        elif solving_thirdProblem:
            thirdAnswer = correct
        GAME_WINDOW.fill(BG_COLOR)
        GAME_WINDOW.blit(displayXMark, displayXMarkRect)
        GAME_WINDOW.blit(displayWrong, displayWrongRect)
        pygame.display.update()
        transition(1, 0)


def calculateAnswer(problem):
    # Calculates the random problem and gives out the result as an integer.
    try:
        # Calculates the problem and turns it into an integer (so no decimals) and then into a string for comparison.
        problem = str(int(eval(problem)))
        print(problem)
    except ZeroDivisionError:
        problem = str(0)
    return problem


def LOGIC_instructions():
    # Shows the player what they need to do to win the Logic minigame
    GAME_WINDOW.fill(BG_COLOR)
    instructing = True
    showingThreeInstructions = True

    # Values to display the 3 instructions
    instruction_font = pygame.font.Font(FONT_FILE, 50)  # Font style
    ready_font = pygame.font.Font(FONT_FILE, 80)
    first_instruction_text = instruction_font.render(
        'Solve the problem that is shown.', True, BLACK, None)
    first_instruction_text_rect = first_instruction_text.get_rect()

    second_instruction_text = instruction_font.render(
        'Solving 2 problems is a win.', True, BLACK, None)
    second_instruction_text_rect = second_instruction_text.get_rect()

    third_instruction_text = instruction_font.render(
        'Failing to solve 2 problems is a loss.', True, BLACK, None)
    third_instruction_text_rect = third_instruction_text.get_rect()

    ready_instruction_text = ready_font.render('Ready?', True, BLACK, None)
    ready_instruction_text_rect = ready_instruction_text.get_rect()

    readyButton = Button('I\'m ready!', 300, 60, ((
        WINDOW_WIDTH // 2) - 450, (WINDOW_HEIGHT // 2) + 200), 6, BUTTON_CLICK_SFX, LOGIC)
    LOGIC_nopeButton = Button('Nope!', 300, 60, ((
        WINDOW_WIDTH // 2) + 150, (WINDOW_HEIGHT // 2) + 200), 6, BUTTON_CLICK_SFX, startMenu)
    while instructing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        if showingThreeInstructions:  # Plays the instruction "animation."
            first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(first_instruction_text,
                             first_instruction_text_rect)
            pygame.display.update()
            transition(1, 0.2)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

            second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(first_instruction_text,
                             first_instruction_text_rect)
            GAME_WINDOW.blit(second_instruction_text,
                             second_instruction_text_rect)
            pygame.display.update()
            transition(1, 0.2)
            # FOCUS HERE NEXT TIME (3 PM, 11/17/22)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.
            second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            third_instruction_text_rect = third_instruction_text.get_rect()
            third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(first_instruction_text,
                             first_instruction_text_rect)
            GAME_WINDOW.blit(second_instruction_text,
                             second_instruction_text_rect)
            GAME_WINDOW.blit(third_instruction_text,
                             third_instruction_text_rect)

            transition(1, 0.2)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.
            second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            third_instruction_text = instruction_font.render(
                'Failing to solve 2 problems is a loss.', True, BLACK, None)
            third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            ready_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
            GAME_WINDOW.blit(first_instruction_text,
                             first_instruction_text_rect)
            GAME_WINDOW.blit(second_instruction_text,
                             second_instruction_text_rect)
            GAME_WINDOW.blit(third_instruction_text,
                             third_instruction_text_rect)
            GAME_WINDOW.blit(ready_instruction_text,
                             ready_instruction_text_rect)

            transition(1, 0.2)
            # Done showing the 3 instructions.
            showingThreeInstructions = False

        # Draws the button alongside the current state of the instructions.
        elif not showingThreeInstructions:
            # Move the 1st instructions a little higher when the 2nd set shows up.
            first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.
            second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            third_instruction_text = instruction_font.render(
                'Failing to solve 2 problems is a loss.', True, BLACK, None)
            third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            ready_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
            GAME_WINDOW.blit(first_instruction_text,
                             first_instruction_text_rect)
            GAME_WINDOW.blit(second_instruction_text,
                             second_instruction_text_rect)
            GAME_WINDOW.blit(third_instruction_text,
                             third_instruction_text_rect)
            GAME_WINDOW.blit(ready_instruction_text,
                             ready_instruction_text_rect)

        readyButton.draw()
        LOGIC_nopeButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    GAME_WINDOW.fill(BG_COLOR)
    return

def LOGIC_freeplay():
    # Screen shown to the player when they want to play Logic in Freeplay mode.
    pygame.mixer.Channel(4).unpause()# Unpause the background music
    GAME_WINDOW.fill(BG_COLOR)
    deciding = True
    # Button values
    playGameButton = Button('Yes', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, LOGIC)
    returnToFreeplayButton = Button('No', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, EXIT_BUTTON_CLICK_SFX, freeplay)

    # Text display values
    titleFont = pygame.font.Font(FONT_FILE, 80)
    subtitleFont = pygame.font.Font(FONT_FILE, 65)
    titleText = titleFont.render('Logic', True, BLACK, None)
    titleText_rect = titleText.get_rect()
    titleText_rect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

    subtitleText = subtitleFont.render('Play?', True, BLACK, None)
    subtitleText_rect = subtitleText.get_rect()
    subtitleText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    while deciding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        GAME_WINDOW.blit(titleText, titleText_rect)
        GAME_WINDOW.blit(subtitleText, subtitleText_rect)
        playGameButton.draw()
        returnToFreeplayButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def LOGIC():
    # Runs the main function of the Logic minigame.
    playing = True  # True = game is not done. False = game is done
    global freeplay_mode, solving_firstProblem, solving_secondProblem, solving_thirdProblem, doneSolving, timeUp_solving_firstProblem, timeUp_solving_secondProblem, timeUp_solving_thirdProblem, chosenProblems, firstAnswer, secondAnswer, thirdAnswer
    # Variables area
    # Values that will display the instructions ('Solve!') beneath the problem
    pygame.display.set_caption('Logic')
    displayInstructions = FONT.render('Solve!', True, BLACK, None)
    displayInstructionsRect = displayInstructions.get_rect()
    displayInstructionsRect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    # Values that will display the selected problem
    if not timeUp_solving_firstProblem and not timeUp_solving_secondProblem and not timeUp_solving_thirdProblem:
        # For loop that loops 3 times. Ensures that the 3 words won't be duplicates/triplicates.
        for i in range(3):
            randomProblem = getRandomProblem(EASY_MATH_PROBLEMS)
            chosenProblems.append(randomProblem)
            # for v in MATH_PROBLEMS.values():
            #     if randomProblem in v:
            #         v.remove(randomProblem)

    firstProblem = chosenProblems[0]
    secondProblem = chosenProblems[1]
    thirdProblem = chosenProblems[2]

    if not timeUp_solving_firstProblem and not timeUp_solving_secondProblem and not timeUp_solving_thirdProblem:
        # boolean values to change the display once the player starts solving
        solving_firstProblem = True
        # False = not solving that problem. True = solving that problem.
        solving_secondProblem = False
        solving_thirdProblem = False
        doneSolving = False

    showProblemText = pygame.font.Font(FONT_FILE, 50)

    showfirstProblem = showProblemText.render(firstProblem, True, BLACK, None)
    showfirstProblemRect = showfirstProblem.get_rect()
    showfirstProblemRect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

    showsecondProblem = showProblemText.render(
        secondProblem, True, BLACK, None)
    showsecondProblemRect = showsecondProblem.get_rect()
    showsecondProblemRect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

    showthirdProblem = showProblemText.render(thirdProblem, True, BLACK, None)
    showthirdProblemRect = showthirdProblem.get_rect()
    showthirdProblemRect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

    # Values that will display the user input text box
    input_box = pygame.Rect(
        LOGIC_X_INPUT_BOX, LOGIC_Y_INPUT_BOX, LOGIC_W_INPUT_BOX, LOGIC_H_INPUT_BOX)
    active_color = pygame.Color(LIGHT_BLUE)
    color = active_color
    active = True
    text = ''

    GAME_WINDOW.fill(BG_COLOR)
    if not timeUp_solving_firstProblem and not timeUp_solving_secondProblem and not timeUp_solving_thirdProblem:
        decide_on_a_problem(30)
        ready_set_solve
    start_ticks = pygame.time.get_ticks()
    while playing:
        # If I were to add "scaling" difficulty, I should probably make the easiest be 5 sec, then 4 sec for medium, then 3 sec for hard.
        seconds = 10 - (int((pygame.time.get_ticks() - start_ticks)/1000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active and seconds > -1:
                    TYPE_SFX.play()
                    if event.key == pygame.K_RETURN:
                        userInput = text
                        if solving_firstProblem:
                            LOGIC_checkUserInput(
                                calculateAnswer(firstProblem), userInput)
                            solving_firstProblem = False
                            solving_secondProblem = True
                            # Resets the timer.
                            start_ticks = pygame.time.get_ticks()
                        elif solving_secondProblem:
                            LOGIC_checkUserInput(
                                calculateAnswer(secondProblem), userInput)
                            solving_secondProblem = False
                            solving_thirdProblem = True
                            # Resets the timer.
                            start_ticks = pygame.time.get_ticks()
                        elif solving_thirdProblem:
                            LOGIC_checkUserInput(
                                calculateAnswer(thirdProblem), userInput)
                            solving_thirdProblem = False
                            doneSolving = True
                            # Resets the timer.
                            start_ticks = pygame.time.get_ticks()
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        TYPE_SFX.stop()
                        BACKSPACE_SFX.play()
                    else:
                        text += event.unicode
            if event.type == pygame.MOUSEBUTTONUP:
                # DEBUGGING
                # print('First problem: ' + str(firstProblem))
                # print('Second problem: ' + str(secondProblem))
                # print('Third problem: ' + str(thirdProblem))
                # If player clicks during any part of the minigame loading, it does nothing (prevents freezing)
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
        GAME_WINDOW.fill(BG_COLOR)
        GAME_WINDOW.blit(displayInstructions, displayInstructionsRect)
        displayCountdown = TIMER_FONT.render(str(seconds), True, BLACK, None)
        displayCountdownRect = displayCountdown.get_rect()
        displayCountdownRect.center = (WINDOW_WIDTH // 2, 100)
        if seconds > -1:  # Countdown timer should come first. Everything else is under it
            GAME_WINDOW.blit(displayCountdown, displayCountdownRect)
            pygame.display.update()
            if solving_firstProblem:
                # Displays the word to be spelled
                GAME_WINDOW.blit(showfirstProblem, showfirstProblemRect)
                drawProgress(1, None, None, None)  # (◯◯◯)
            elif solving_secondProblem:
                GAME_WINDOW.blit(showsecondProblem, showsecondProblemRect)
                # Checks if the player spelt the 1st word in time...
                if timeUp_solving_firstProblem == False:
                    if firstAnswer == True:    # ...AND checks if the player spelt the 1st word correct.
                        drawProgress(2, True, None, None)  # ✓◯◯
                    elif firstAnswer == False:  # ...AND checks if the player spelt the 1st word wrong.
                        drawProgress(2, False, None, None)  # ❌◯◯
                # Checks if the player didn't spell the 1st word in time...
                elif timeUp_solving_firstProblem:
                    firstAnswer = False
                    drawProgress(2, False, None, None)  # ❌◯◯
            elif solving_thirdProblem:
                GAME_WINDOW.blit(showthirdProblem, showthirdProblemRect)
                # Checks if the player spelt the 1st AND 2nd word in time...
                if timeUp_solving_firstProblem == False and timeUp_solving_secondProblem == False:
                    # ...AND checks if the player spelt the 1st & 2nd word correct.
                    if firstAnswer == True and secondAnswer == True:
                        drawProgress(3, True, True, None)  # ✓✓◯
                        if freeplay_mode == False:
                            LOGIC_win()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_win()
                    # ...AND checks if the player spelt the 1st word correct and 2nd wrong.
                    elif firstAnswer == True and secondAnswer == False:
                        drawProgress(3, True, False, None)  # ✓❌◯
                    # ...AND checks if the player spelt both 1st and 2nd word wrong.
                    elif firstAnswer == False and secondAnswer == False:
                        drawProgress(3, False, False, None)  # ❌❌◯
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                    # ...AND checks if the player spelt the 1st word wrong and 2nd correct.
                    elif firstAnswer == False and secondAnswer == True:
                        drawProgress(3, False, True, None)  # ❌✓◯
                # Checks if the player didn't spell the 1st word in time AND did spell the 2nd word in time...
                elif timeUp_solving_firstProblem == True and timeUp_solving_secondProblem == False:
                    # ...AND checks if the player spelt the 1st & 2nd word correct.
                    if firstAnswer == True and secondAnswer == True:
                        drawProgress(3, True, True, None)  # ✓✓◯
                        if freeplay_mode == False:
                            LOGIC_win()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_win()
                    # ...AND checks if the player spelt the 1st word correct and 2nd wrong.
                    elif firstAnswer == True and secondAnswer == False:
                        drawProgress(3, True, False, None)  # ✓❌◯
                    # ...AND checks if the player spelt both 1st and 2nd word wrong.
                    elif firstAnswer == False and secondAnswer == False:
                        drawProgress(3, False, False, None)  # ❌❌◯
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                    # ...AND checks if the player spelt the 1st word wrong and 2nd correct.
                    elif firstAnswer == False and secondAnswer == True:
                        drawProgress(3, False, True, None)  # ❌✓◯
                # Checks if the player spelt the 1st word in time AND didn't spell the 2nd word in time...
                elif timeUp_solving_firstProblem == False and timeUp_solving_secondProblem == True:
                    secondAnswer = False
                    # ...AND checks if the player spelt the 1st & 2nd word correct.
                    if firstAnswer == True and secondAnswer == True:
                        drawProgress(3, True, True, None)  # ✓✓◯
                        if freeplay_mode == False:
                            LOGIC_win()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_win()
                    # ...AND checks if the player spelt the 1st word correct and 2nd wrong.
                    elif firstAnswer == True and secondAnswer == False:
                        drawProgress(3, True, False, None)  # ✓❌◯
                    # ...AND checks if the player spelt both 1st and 2nd word wrong.
                    elif firstAnswer == False and secondAnswer == False:
                        drawProgress(3, False, False, None)  # ❌❌◯
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                    # ...AND checks if the player spelt the 1st word wrong and 2nd correct.
                    elif firstAnswer == False and secondAnswer == True:
                        drawProgress(3, False, True, None)  # ❌✓◯
                # Checks if the player didn't spell the 1st AND 2nd word in time.
                elif timeUp_solving_firstProblem and timeUp_solving_secondProblem:
                    firstAnswer = False
                    secondAnswer = False
                    drawProgress(3, False, False, None)  # ❌❌◯
                    if freeplay_mode == False:
                        LOGIC_loss()
                    elif freeplay_mode == True:
                        LOGIC_freeplay_loss()
            if doneSolving:
                # Checks if the player spelt all 3 words in time...
                if timeUp_solving_firstProblem == False and timeUp_solving_secondProblem == False and timeUp_solving_thirdProblem == False:
                    if firstAnswer == True and secondAnswer == False and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, False)  # ✓❌❌
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                    elif firstAnswer == False and secondAnswer == True and thirdAnswer == True:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, True)  # ❌✓✓
                        if freeplay_mode == False:
                            LOGIC_win()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_win()
                    elif firstAnswer == True and secondAnswer == False and thirdAnswer == True:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, True)  # ✓❌✓
                        if freeplay_mode == False:
                            LOGIC_win()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_win()
                    elif firstAnswer == False and secondAnswer == True and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, False)  # ❌✓❌
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                # Checks if the player spelt the 2nd and 3rd in time but not the 1st...
                elif timeUp_solving_firstProblem == True and timeUp_solving_secondProblem == False and timeUp_solving_thirdProblem == False:
                    if firstAnswer == False and secondAnswer == True and thirdAnswer == True:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, True)  # ❌✓✓
                        if freeplay_mode == False:
                            LOGIC_win()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_win()
                    elif firstAnswer == False and secondAnswer == True and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, False)  # ❌✓❌
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                # Checks if the player spelt the 1st and 2nd in time but not the 3rd...
                elif timeUp_solving_firstProblem == False and timeUp_solving_secondProblem == False and timeUp_solving_thirdProblem == True:
                    # Since the 3rd word wasn't spelt in time, this will be False.
                    thirdAnswer = False
                    if firstAnswer == True and secondAnswer == False and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, False)  # ✓❌❌
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                    elif firstAnswer == False and secondAnswer == True and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, False)  # ❌✓❌
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                # Checks if the player spelt the 1st in time but not the 2nd and 3rd...
                elif timeUp_solving_firstProblem == False and timeUp_solving_secondProblem == True and timeUp_solving_thirdProblem == True:
                    # WORKING AS INTENDEDd
                    if freeplay_mode == False:
                        LOGIC_loss()
                    elif freeplay_mode == True:
                        LOGIC_freeplay_loss()
                # Checks if the player spelt the 2nd word in time but not the 1st and 3rd...
                elif timeUp_solving_firstProblem == True and timeUp_solving_secondProblem == False and timeUp_solving_thirdProblem == True:
                    # Since the 3rd word wasn't spelt in time, this will be False.
                    thirdAnswer = False
                    if firstAnswer == False and secondAnswer == True and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, False)  # ❌✓❌
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                # Checks if the player spelt the 1st and 3rd in time but not the 2nd...
                elif timeUp_solving_firstProblem == False and timeUp_solving_secondProblem == True and timeUp_solving_thirdProblem == False:
                    if firstAnswer == True and secondAnswer == False and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, False)  # ✓❌❌
                        if freeplay_mode == False:
                            LOGIC_loss()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_loss()
                    elif firstAnswer == True and secondAnswer == False and thirdAnswer == True:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, True)  # ✓❌✓
                        if freeplay_mode == False:
                            LOGIC_win()
                        elif freeplay_mode == True:
                            LOGIC_freeplay_win()

        elif seconds == -1:  # If time runs out...
            timeUp()  # ...and "Time's up!" pops up...
            if solving_firstProblem:  # ...and they were solving the first problem...
                # ...this value becomes True and the game moves on to the 2nd problem...
                timeUp_solving_firstProblem = True
                # ...this makes sure that we're not typing the 1st problem...
                solving_firstProblem = False
                # ...and this makes sure that we are typing the 2nd problem.
                solving_secondProblem = True
                LOGIC()
            elif solving_secondProblem:  # ...and they were solving_ the second problem...
                # ...this value becomes True and the game moves on to the 3rd problem...
                timeUp_solving_secondProblem = True
                # ...this makes sure that we're not typing the 2nd problem...
                solving_secondProblem = False
                # ...and this makes sure that we are typing the 3rd problem.
                solving_thirdProblem = True
                LOGIC()
            elif solving_thirdProblem:  # ...and they were solving_ the third problem...
                # ...the game moves onto the final check...
                timeUp_solving_thirdProblem = True
                # ...this makes sure that we're not typing the 3rd problem...
                solving_thirdProblem = False
                # ...and this makes sure that we're done typing.
                doneSolving = True
                LOGIC()
            elif doneSolving:
                LOGIC()
        # Rendering the user input
        txt_surface_font = pygame.font.Font(FONT_FILE, 40)
        txt_surface = txt_surface_font.render(text, True, color)
        txt_surface_rect = txt_surface.get_rect()
        # Makes sure that the text will appear at the center of the box
        txt_surface_rect.center = input_box.center
        GAME_WINDOW.blit(txt_surface, txt_surface_rect)
        # Blitting the input_box rect
        pygame.draw.rect(GAME_WINDOW, color, input_box, 2)
        # Draws the surface object to the screen.
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Dodging game functions

# Reaction game functions

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# WORD TYPING GAME FUNCTIONS #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def WORD_TYPE_checkUserInput(correctAnswer, userAnswer):
    # Checks the player input after they hit enter on the text box.

    # Values that will display if the player is correct or wrong
    displayCorrect = FONT.render('Correct!', True, BLACK, None)
    displayCorrectRect = displayCorrect.get_rect()
    # Exact location as the instructions, as it will replace it once the player answers
    displayCorrectRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    displayCheck = SYMBOL_FONT.render('✓', True, GREEN, None)
    displayCheckRect = displayCheck.get_rect()
    displayCheckRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    displayWrong = FONT.render('Wrong!', True, BLACK, None)
    displayWrongRect = displayWrong.get_rect()
    # Exact location as the instructions, as it will replace it once the player answers
    displayWrongRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    displayXMark = SYMBOL_FONT.render('❌', True, RED, None)
    displayXMarkRect = displayXMark.get_rect()
    displayXMarkRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    global correct, firstAnswer, secondAnswer, thirdAnswer
    correct = None
    # Checks if the player typed the word correctly
    # .casefold() ensures that the string comparison is case-insensitive (the player can type in uppercase or lowercase, it would still be the same.)
    if userAnswer.casefold() == correctAnswer.casefold():
        transition(0, 1)
        CORRECT_SFX.play()
        correct = True
        if spellingFirstWord:
            firstAnswer = correct
        elif spellingSecondWord:
            secondAnswer = correct
        elif spellingThirdWord:
            thirdAnswer = correct
        GAME_WINDOW.fill(BG_COLOR)
        GAME_WINDOW.blit(displayCheck, displayCheckRect)
        GAME_WINDOW.blit(displayCorrect, displayCorrectRect)
        # Remove the chosen word from the list so that it can't be spelled twice.
        for x in WORDS:
            if correctAnswer == x:
                WORDS.remove(x)
        pygame.display.update()
        transition(1, 0)

    # Checks if the player typed the word incorrectly
    elif userAnswer.casefold() != correctAnswer.casefold():
        transition(0, 1)
        WRONG_SFX.play()
        correct = False
        if spellingFirstWord:
            firstAnswer = correct
        elif spellingSecondWord:
            secondAnswer = correct
        elif spellingThirdWord:
            thirdAnswer = correct
        GAME_WINDOW.fill(BG_COLOR)
        GAME_WINDOW.blit(displayXMark, displayXMarkRect)
        GAME_WINDOW.blit(displayWrong, displayWrongRect)
        # Remove the chosen word from the list so that it can't be spelled twice.
        for x in WORDS:
            if correctAnswer == x:
                WORDS.remove(x)
        pygame.display.update()
        transition(1, 0)


def decide_on_a_word(numOfCycles):
    # Shows an animation of the program randomly cycling through the problems and then stops at
    # after x amount of cycles.

    while numOfCycles > 0:
        # the chosenLetter variables are meant for drawing the letter on the screen
        cycleFont = pygame.font.Font(FONT_FILE, 80)
        cycleText = cycleFont.render('Choosing a word...', True, BLACK, None)
        cycleTextRect = cycleText.get_rect()
        cycleTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

        pygame.display.update()
        time.sleep(0.02)
        GAME_WINDOW.fill(BG_COLOR)  # "removes" the blit to prevent overlapping
        GAME_WINDOW.blit(cycleText, cycleTextRect)
        pygame.display.update()  # second update to show the the "removal"
        FPSCLOCK.tick(FPS)
        # keeps subtracting the parameter and stops the loop when it reaches 0
        numOfCycles = numOfCycles - 1
    transition(0, 2)


def ready_set_type():
    # Displays the three words "Ready...", "Set..." "Type!" in quick succession
    readyFont = pygame.font.Font(FONT_FILE, 80)
    readyText = readyFont.render('Ready...', True, BLACK, None)
    readyTextRect = readyText.get_rect()
    readyTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(readyText, readyTextRect)
    transition(1, 0.2)

    setTextFont = pygame.font.Font(FONT_FILE, 140)
    setText = setTextFont.render('Set...', True, BLACK, None)
    setTextRect = setText.get_rect()
    setTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(setText, setTextRect)
    transition(1, 0.2)

    typeTextFont = pygame.font.Font(FONT_FILE, 200)
    typeText = typeTextFont.render('TYPE!', True, BLACK, None)
    typeTextRect = typeText.get_rect()
    typeTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(typeText, typeTextRect)
    transition(1, 0.2)


def WORD_TYPE_resetValues():
    # Resets all the important values to their original states after a win or loss.
    global spellingFirstWord, spellingSecondWord, spellingThirdWord, doneSpelling, timeUp_spellingFirstWord, timeUp_spellingSecondWord, timeUp_spellingThirdWord, firstAnswer, secondAnswer, thirdAnswer
    # Variables that change depending on which word the player is spelling.
    spellingFirstWord = True  # Restarting back to spelling a new first word.
    spellingSecondWord = False
    spellingThirdWord = False
    doneSpelling = False

    # Variables that change if the player doesn't spell one of the words in time.
    timeUp_spellingFirstWord = False
    timeUp_spellingSecondWord = False
    timeUp_spellingThirdWord = False

    # Variables that store the player's answers.
    firstAnswer = None
    secondAnswer = None
    thirdAnswer = None

    # List that holds the 3 words the player will spell.
    # Puts the 3 words that were chosen back into the constant list.
    WORDS.extend(chosenWords)
    chosenWords.clear()       # Reverts it back to its blank state.


## I think I'll go ahead and make this one. ##
def WORD_TYPE_instructions():
    # Shows the player what they need to do to win the Word Type minigame
    GAME_WINDOW.fill(BG_COLOR)
    WORD_TYPE_instructing = True
    WORD_TYPE_showingThreeInstructions = True

    # Values to display the 3 instructions
    WORD_TYPE_instruction_font = pygame.font.Font(FONT_FILE, 50)  # Font style
    WORD_TYPE_ready_font = pygame.font.Font(FONT_FILE, 80)
    WORD_TYPE_first_instruction_text = WORD_TYPE_instruction_font.render(
        'Type the word that is shown.', True, BLACK, None)
    WORD_TYPE_first_instruction_text_rect = WORD_TYPE_first_instruction_text.get_rect()

    WORD_TYPE_second_instruction_text = WORD_TYPE_instruction_font.render(
        'Spelling it 2X is a win.', True, BLACK, None)
    WORD_TYPE_second_instruction_text_rect = WORD_TYPE_second_instruction_text.get_rect()

    WORD_TYPE_third_instruction_text = WORD_TYPE_instruction_font.render(
        'Failing to spell it 2X is a loss.', True, BLACK, None)
    WORD_TYPE_third_instruction_text_rect = WORD_TYPE_third_instruction_text.get_rect()

    WORD_TYPE_ready_instruction_text = WORD_TYPE_ready_font.render(
        'Ready?', True, BLACK, None)
    WORD_TYPE_ready_instruction_text_rect = WORD_TYPE_ready_instruction_text.get_rect()

    WORD_TYPE_readyButton = Button('I\'m ready!', 300, 60, ((
        WINDOW_WIDTH // 2) - 450, (WINDOW_HEIGHT // 2) + 200), 6, BUTTON_CLICK_SFX, WORD_TYPE)
    WORD_TYPE_nopeButton = Button('Nope!', 300, 60, ((
        WINDOW_WIDTH // 2) + 150, (WINDOW_HEIGHT // 2) + 200), 6, BUTTON_CLICK_SFX, startMenu)
    while WORD_TYPE_instructing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                WORD_TYPE_instructing = False
                pygame.quit()
                sys.exit()
        if WORD_TYPE_showingThreeInstructions:  # Plays the instruction "animation."
            WORD_TYPE_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(WORD_TYPE_first_instruction_text,
                             WORD_TYPE_first_instruction_text_rect)
            pygame.display.update()
            transition(1, 0.2)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            WORD_TYPE_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

            WORD_TYPE_second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(WORD_TYPE_first_instruction_text,
                             WORD_TYPE_first_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_second_instruction_text,
                             WORD_TYPE_second_instruction_text_rect)
            pygame.display.update()
            transition(1, 0.2)
            # FOCUS HERE NEXT TIME (3 PM, 11/17/22)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            WORD_TYPE_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.
            WORD_TYPE_second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            WORD_TYPE_third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(WORD_TYPE_first_instruction_text,
                             WORD_TYPE_first_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_second_instruction_text,
                             WORD_TYPE_second_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_third_instruction_text,
                             WORD_TYPE_third_instruction_text_rect)

            transition(1, 0.2)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            WORD_TYPE_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.
            WORD_TYPE_second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            WORD_TYPE_third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            WORD_TYPE_ready_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
            GAME_WINDOW.blit(WORD_TYPE_first_instruction_text,
                             WORD_TYPE_first_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_second_instruction_text,
                             WORD_TYPE_second_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_third_instruction_text,
                             WORD_TYPE_third_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_ready_instruction_text,
                             WORD_TYPE_ready_instruction_text_rect)

            transition(1, 0.2)
            # Done showing the 3 instructions.
            WORD_TYPE_showingThreeInstructions = False

        # Draws the button alongside the current state of the instructions.
        elif not WORD_TYPE_showingThreeInstructions:
            # Move the 1st instructions a little higher when the 2nd set shows up.
            WORD_TYPE_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.5
            WORD_TYPE_second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            WORD_TYPE_third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            WORD_TYPE_ready_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
            GAME_WINDOW.blit(WORD_TYPE_first_instruction_text,
                             WORD_TYPE_first_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_second_instruction_text,
                             WORD_TYPE_second_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_third_instruction_text,
                             WORD_TYPE_third_instruction_text_rect)
            GAME_WINDOW.blit(WORD_TYPE_ready_instruction_text,
                             WORD_TYPE_ready_instruction_text_rect)

        WORD_TYPE_readyButton.draw()
        WORD_TYPE_nopeButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    GAME_WINDOW.fill(BG_COLOR)
    return

    # FOCUS HERE NEXT TIME (3 PM, 11/17/22)


def WORD_TYPE_win():
    # Shows the player that they won and applies all the win rewards.
    global win_has_been_called
    win_has_been_called = True
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 1)
    pygame.mixer.Channel(4).pause()# Pause the background music as the Win SFX is playing.
    WIN_SFX.play()  # Plays the winning theme.
    transition(0, 0.2)
    winTextFont = pygame.font.Font(FONT_FILE, 100)
    winText = winTextFont.render('You won!', True, BLACK, None)
    winTextRect = winText.get_rect()
    winTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(winText, winTextRect)
    transition(3, 1)
    WORD_TYPE_resetValues()
    winState() # Show the overall stats of the player before the next minigame.
    # startMenu()


def WORD_TYPE_loss():
    # Show the player that they lost and applise all the loss rewards.
    global loss_has_been_called
    loss_has_been_called = True
    pygame.mixer.Channel(4).pause()# Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()
    transition(0, 0.2)
    lossTextFont = pygame.font.Font(FONT_FILE, 100)
    lossText = lossTextFont.render('You lost!', True, BLACK, None)
    lossTextRect = lossText.get_rect()
    lossTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(lossText, lossTextRect)
    transition(3, 1)
    WORD_TYPE_resetValues()
    lossState()
    # startMenu()

def WORD_TYPE_freeplay_win():
    # Same as the regular win but asks if the player wants to play again.
    global win_has_been_called
    win_has_been_called = True
    winning = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, WORD_TYPE)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    
    WIN_SFX.play() # Plays the winning theme
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    transition(0, 0.2)
    while winning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        winTextFont = pygame.font.Font(FONT_FILE, 100)
        winText = winTextFont.render('You won!', True, BLACK, None)
        winTextRect = winText.get_rect()
        winTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(winText, winTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def WORD_TYPE_freeplay_loss():
    # Same as the regular loss but asks if the player wants to play again.
    global loss_has_been_called
    loss_has_been_called = True
    losing = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, WORD_TYPE)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the losing theme.
    transition(0, 0.2)
    while losing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        lossTextFont = pygame.font.Font(FONT_FILE, 100)
        lossText = lossTextFont.render('You lost!', True, BLACK, None)
        lossTextRect = lossText.get_rect()
        lossTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(lossText, lossTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def WORD_TYPE_freeplay():
    # Screen shown to the player when they're in Freeplay mode.
    pygame.mixer.Channel(4).unpause()# Unpause the background music
    GAME_WINDOW.fill(BG_COLOR)
    deciding = True
    # Button values
    playGameButton = Button('Yes', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, WORD_TYPE)
    returnToFreeplayButton = Button('No', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, EXIT_BUTTON_CLICK_SFX, freeplay)

    # Text display values
    titleFont = pygame.font.Font(FONT_FILE, 80)
    subtitleFont = pygame.font.Font(FONT_FILE, 65)
    titleText = titleFont.render('WORD TYPE', True, BLACK, None)
    titleText_rect = titleText.get_rect()
    titleText_rect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

    subtitleText = subtitleFont.render('Play?', True, BLACK, None)
    subtitleText_rect = subtitleText.get_rect()
    subtitleText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    while deciding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        GAME_WINDOW.blit(titleText, titleText_rect)
        GAME_WINDOW.blit(subtitleText, subtitleText_rect)
        playGameButton.draw()
        returnToFreeplayButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def WORD_TYPE():
    playing = True  # True = game is not done. False = game is done.
    global spellingFirstWord, spellingSecondWord, spellingThirdWord, doneSpelling, timeUp_spellingFirstWord, timeUp_spellingSecondWord, timeUp_spellingThirdWord, chosenWords, firstAnswer, secondAnswer, thirdAnswer

    pygame.display.set_caption('Word Type')
    # Variables area
    # Values that will display the selected word
    if not timeUp_spellingFirstWord and not timeUp_spellingSecondWord and not timeUp_spellingThirdWord:
        # For loop that loops 3 times. Ensures that the 3 words won't be duplicates/triplicates.
        for i in range(3):
            # Takes words from the WORDS list if the player keeps playing without closing the game. Ensures that they can play forever.
            if len(WORDS) != 0:
                randomWord = random.choice(WORDS)
                chosenWords.append(randomWord)
                WORDS.remove(randomWord)
            # Takes words from the chosenWords list if the player keeps playing without closing the game. Ensures that they can play forever.
            elif len(WORDS) == 0:
                randomWord = random.choice(chosenWords)
                WORDS.append(randomWord)
                chosenWords.remove(randomWord)

    firstWord = chosenWords[0]
    secondWord = chosenWords[1]
    thirdWord = chosenWords[2]

    if not timeUp_spellingFirstWord and not timeUp_spellingSecondWord and not timeUp_spellingThirdWord:
        # boolean values to change the display once the player starts spelling
        spellingFirstWord = True
        # False = not spelling that word. True = spelling that word.
        spellingSecondWord = False
        spellingThirdWord = False
        doneSpelling = False

    # chosenWord = getRandom(WORDS) # variable that holds the random word
    showWordText = pygame.font.Font(FONT_FILE, 50)
    typeTextFont = pygame.font.Font(FONT_FILE, 40)

    showFirstWord = showWordText.render(firstWord, True, BLACK, None)
    showFirstWordRect = showFirstWord.get_rect()
    showFirstWordRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

    showSecondWord = showWordText.render(secondWord, True, BLACK, None)
    showSecondWordRect = showSecondWord.get_rect()
    showSecondWordRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

    showThirdWord = showWordText.render(thirdWord, True, BLACK, None)
    showThirdWordRect = showThirdWord.get_rect()
    showThirdWordRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

    typeText = typeTextFont.render('Type!', True, BLACK, None)
    typeTextRect = typeText.get_rect()
    typeTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    # Values that will display the user input text box
    input_box = pygame.Rect(X_INPUTBOX, Y_INPUTBOX, W_INPUTBOX, H_INPUTBOX)
    active_color = pygame.Color(BLUE)
    color = active_color
    active = True
    text = ''

    if not timeUp_spellingFirstWord and not timeUp_spellingSecondWord and not timeUp_spellingThirdWord:
        decide_on_a_word(30)
        ready_set_type()
    start_ticks = pygame.time.get_ticks()
    while playing:
        # If I were to add "scaling" difficulty, I should probably make the easiest be 5 sec, then 4 sec for medium, then 3 sec for hard.
        seconds = 3 - (int((pygame.time.get_ticks() - start_ticks)/1000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if active and seconds > -1:
                    TYPE_SFX.play()
                    if event.key == pygame.K_RETURN:
                        userInput = text
                        if spellingFirstWord:
                            WORD_TYPE_checkUserInput(firstWord, userInput)
                            spellingFirstWord = False
                            spellingSecondWord = True
                            # Resets the timer.
                            start_ticks = pygame.time.get_ticks()
                        elif spellingSecondWord:
                            WORD_TYPE_checkUserInput(secondWord, userInput)
                            spellingSecondWord = False
                            spellingThirdWord = True
                            # Resets the timer.
                            start_ticks = pygame.time.get_ticks()
                        elif spellingThirdWord:
                            WORD_TYPE_checkUserInput(thirdWord, userInput)
                            spellingThirdWord = False
                            doneSpelling = True
                            # Resets the timer.
                            start_ticks = pygame.time.get_ticks()
                            # special condition should happen here where the game checks
                            # if the player got 2 out of 3 correct/2 out of 3 wrong
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        TYPE_SFX.stop()
                        BACKSPACE_SFX.play()
                        text = text[:-1]
                    else:
                        text += event.unicode
        GAME_WINDOW.fill(BG_COLOR)
        displayCountdown = TIMER_FONT.render(str(seconds), True, BLACK, None)
        displayCountdownRect = displayCountdown.get_rect()
        displayCountdownRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 5)
        if seconds > -1:  # Countdown timer should come first. Everything else is under it
            GAME_WINDOW.blit(displayCountdown, displayCountdownRect)
            pygame.display.update()
            if spellingFirstWord:
                # Displays the word to be spelled
                GAME_WINDOW.blit(showFirstWord, showFirstWordRect)
                drawProgress(1, None, None, None)  # (◯◯◯)
            elif spellingSecondWord:
                GAME_WINDOW.blit(showSecondWord, showSecondWordRect)
                # Checks if the player spelt the 1st word in time...
                if timeUp_spellingFirstWord == False:
                    if firstAnswer == True:    # ...AND checks if the player spelt the 1st word correct.
                        drawProgress(2, True, None, None)  # ✓◯◯
                    elif firstAnswer == False:  # ...AND checks if the player spelt the 1st word wrong.
                        drawProgress(2, False, None, None)  # ❌◯◯
                # Checks if the player didn't spell the 1st word in time...
                elif timeUp_spellingFirstWord:
                    firstAnswer = False
                    drawProgress(2, False, None, None)  # ❌◯◯
            elif spellingThirdWord:
                GAME_WINDOW.blit(showThirdWord, showThirdWordRect)
                # Checks if the player spelt the 1st AND 2nd word in time...
                if timeUp_spellingFirstWord == False and timeUp_spellingSecondWord == False:
                    # ...AND checks if the player spelt the 1st & 2nd word correct.
                    if firstAnswer == True and secondAnswer == True:
                        drawProgress(3, True, True, None)  # ✓✓◯
                        WORD_TYPE_win()
                    # ...AND checks if the player spelt the 1st word correct and 2nd wrong.
                    elif firstAnswer == True and secondAnswer == False:
                        drawProgress(3, True, False, None)  # ✓❌◯
                    # ...AND checks if the player spelt both 1st and 2nd word wrong.
                    elif firstAnswer == False and secondAnswer == False:
                        drawProgress(3, False, False, None)  # ❌❌◯
                        WORD_TYPE_loss()
                    # ...AND checks if the player spelt the 1st word wrong and 2nd correct.
                    elif firstAnswer == False and secondAnswer == True:
                        drawProgress(3, False, True, None)  # ❌✓◯
                # Checks if the player didn't spell the 1st word in time AND did spell the 2nd word in time...
                elif timeUp_spellingFirstWord == True and timeUp_spellingSecondWord == False:
                    # ...AND checks if the player spelt the 1st & 2nd word correct.
                    if firstAnswer == True and secondAnswer == True:
                        drawProgress(3, True, True, None)  # ✓✓◯
                        WORD_TYPE_win()
                    # ...AND checks if the player spelt the 1st word correct and 2nd wrong.
                    elif firstAnswer == True and secondAnswer == False:
                        drawProgress(3, True, False, None)  # ✓❌◯
                    # ...AND checks if the player spelt both 1st and 2nd word wrong.
                    elif firstAnswer == False and secondAnswer == False:
                        drawProgress(3, False, False, None)  # ❌❌◯
                        WORD_TYPE_loss()
                    # ...AND checks if the player spelt the 1st word wrong and 2nd correct.
                    elif firstAnswer == False and secondAnswer == True:
                        drawProgress(3, False, True, None)  # ❌✓◯
                # Checks if the player spelt the 1st word in time AND didn't spell the 2nd word in time...
                elif timeUp_spellingFirstWord == False and timeUp_spellingSecondWord == True:
                    secondAnswer = False
                    # ...AND checks if the player spelt the 1st & 2nd word correct.
                    if firstAnswer == True and secondAnswer == True:
                        drawProgress(3, True, True, None)  # ✓✓◯
                        WORD_TYPE_win()
                    # ...AND checks if the player spelt the 1st word correct and 2nd wrong.
                    elif firstAnswer == True and secondAnswer == False:
                        drawProgress(3, True, False, None)  # ✓❌◯
                    # ...AND checks if the player spelt both 1st and 2nd word wrong.
                    elif firstAnswer == False and secondAnswer == False:
                        drawProgress(3, False, False, None)  # ❌❌◯
                        WORD_TYPE_loss()
                    # ...AND checks if the player spelt the 1st word wrong and 2nd correct.
                    elif firstAnswer == False and secondAnswer == True:
                        drawProgress(3, False, True, None)  # ❌✓◯
                # Checks if the player didn't spell the 1st AND 2nd word in time.
                elif timeUp_spellingFirstWord and timeUp_spellingSecondWord:
                    firstAnswer = False
                    secondAnswer = False
                    drawProgress(3, False, False, None)  # ❌❌◯
                    WORD_TYPE_loss()
            if doneSpelling:
                # Checks if the player spelt all 3 words in time...
                if timeUp_spellingFirstWord == False and timeUp_spellingSecondWord == False and timeUp_spellingThirdWord == False:
                    if firstAnswer == True and secondAnswer == False and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, False)  # ✓❌❌
                        WORD_TYPE_loss()
                    elif firstAnswer == False and secondAnswer == True and thirdAnswer == True:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, True)  # ❌✓✓
                        WORD_TYPE_win()
                    elif firstAnswer == True and secondAnswer == False and thirdAnswer == True:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, True)  # ✓❌✓
                        WORD_TYPE_win()
                    elif firstAnswer == False and secondAnswer == True and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, False)  # ❌✓❌
                        WORD_TYPE_loss()
                # Checks if the player spelt the 2nd and 3rd in time but not the 1st...
                elif timeUp_spellingFirstWord == True and timeUp_spellingSecondWord == False and timeUp_spellingThirdWord == False:
                    if firstAnswer == False and secondAnswer == True and thirdAnswer == True:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, True)  # ❌✓✓
                        WORD_TYPE_win()
                    elif firstAnswer == False and secondAnswer == True and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, False)  # ❌✓❌
                        WORD_TYPE_loss()
                # Checks if the player spelt the 1st and 2nd in time but not the 3rd...
                elif timeUp_spellingFirstWord == False and timeUp_spellingSecondWord == False and timeUp_spellingThirdWord == True:
                    # Since the 3rd word wasn't spelt in time, this will be False.
                    thirdAnswer = False
                    if firstAnswer == True and secondAnswer == False and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, False)  # ✓❌❌
                        WORD_TYPE_loss()
                    elif firstAnswer == False and secondAnswer == True and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, False)  # ❌✓❌
                        WORD_TYPE_loss()
                # Checks if the player spelt the 1st in time but not the 2nd and 3rd...
                elif timeUp_spellingFirstWord == False and timeUp_spellingSecondWord == True and timeUp_spellingThirdWord == True:
                    # WORKING AS INTENDEDd
                    WORD_TYPE_loss()
                # Checks if the player spelt the 2nd word in time but not the 1st and 3rd...
                elif timeUp_spellingFirstWord == True and timeUp_spellingSecondWord == False and timeUp_spellingThirdWord == True:
                    # Since the 3rd word wasn't spelt in time, this will be False.
                    thirdAnswer = False
                    if firstAnswer == False and secondAnswer == True and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, False, True, False)  # ❌✓❌
                        WORD_TYPE_loss()
                # Checks if the player spelt the 1st and 3rd in time but not the 2nd...
                elif timeUp_spellingFirstWord == False and timeUp_spellingSecondWord == True and timeUp_spellingThirdWord == False:
                    if firstAnswer == True and secondAnswer == False and thirdAnswer == False:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, False)  # ✓❌❌
                        WORD_TYPE_loss()
                    elif firstAnswer == True and secondAnswer == False and thirdAnswer == True:
                        # WORKING AS INTENDEDd
                        drawProgress(4, True, False, True)  # ✓❌✓
                        WORD_TYPE_win()

                # Ones that are remarked can be brought back if I feel like adding more words to spell and check.
                # if firstAnswer == True and secondAnswer == True and thirdAnswer == True:
                #     drawProgress(4, True, True, True)
                # if firstAnswer == True and secondAnswer == True and thirdAnswer == False:
                #     drawProgress(4, True, True, False)
                # elif firstAnswer == False and secondAnswer == False and thirdAnswer == False:
                #     drawProgress(4, False, False, False)
                # elif firstAnswer == False and secondAnswer == False and thirdAnswer == True:
                #     drawProgress(4, False, False, True)

        elif seconds == -1:  # If time runs out...
            timeUp()  # ...and "Time's up!" pops up...
            if spellingFirstWord:  # ...and they were spelling the first word...
                # ...this value becomes True and the game moves on to the 2nd word...
                timeUp_spellingFirstWord = True
                # ...this makes sure that we're not typing the 1st word...
                spellingFirstWord = False
                # ...and this makes sure that we are typing the 2nd word.
                spellingSecondWord = True
                WORD_TYPE()
            elif spellingSecondWord:  # ...and they were spelling the second word...
                # ...this value becomes True and the game moves on to the 3rd word...
                timeUp_spellingSecondWord = True
                # ...this makes sure that we're not typing the 2nd word...
                spellingSecondWord = False
                # ...and this makes sure that we are typing the 3rd word.
                spellingThirdWord = True
                WORD_TYPE()
            elif spellingThirdWord:  # ...and they were spelling the third word...
                # ...the game moves onto the final check...
                timeUp_spellingThirdWord = True
                # ...this makes sure that we're not typing the 3rd word...
                spellingThirdWord = False
                # ...and this makes sure that we're done typing.
                doneSpelling = True
                WORD_TYPE()
            elif doneSpelling:
                WORD_TYPE()

        # Rendering the user input
        txt_surface = FONT.render(text, True, color)
        txt_surface_rect = txt_surface.get_rect()
        # Makes sure that the text will appear at the center of the box
        txt_surface_rect.center = input_box.center
        GAME_WINDOW.blit(txt_surface, txt_surface_rect)
        GAME_WINDOW.blit(typeText, typeTextRect)
        # Blitting the input_box rect
        pygame.draw.rect(GAME_WINDOW, color, input_box, 2)
        # Draws the surface object to the screen
        pygame.display.update()  # DO NOT ERASE
        FPSCLOCK.tick(FPS)  # DO NOT ERASE

#~~~~~~~~~~~~~~~~~~~~~~#
# BUTTONMASH FUNCTIONS #
#~~~~~~~~~~~~~~~~~~~~~~#

def shuffleLetters():
    # Picks from a random value from the "LETTERS" list and returns the value
    shuffle = random.randint(0,8)
    RANDOM_LETTERS = LETTERS[shuffle]
    return RANDOM_LETTERS

def selectingLetter(numOfCycles):
    # Shows an animation of the program randomly cycling through the home row keys and then stops at
    # after x amount of cycles.

    while numOfCycles > 0:
        # the chosenLetter variables are meant for drawing the letter on the screen
        cyclingThroughLetters = FONT.render(shuffleLetters(), True, RED, BLACK) # variable for how the text will look
        cyclingThroughLettersRect = cyclingThroughLetters.get_rect()
        cyclingThroughLettersRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        # Values that display "Cycling..." underneath the letter cycle
        cycleFont = pygame.font.Font(FONT_FILE, 80)
        cycleText = cycleFont.render('Choosing a letter...', True, BLACK, None)
        cycleTextRect = cycleText.get_rect()
        cycleTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

        GAME_WINDOW.blit(cyclingThroughLetters, cyclingThroughLettersRect) # need to make it so that the previous blit will be erased before the next blit occurs
        
        pygame.display.update()
        time.sleep(0.02)
        GAME_WINDOW.fill(BG_COLOR) # "removes" the blit to prevent overlapping
        GAME_WINDOW.blit(cycleText, cycleTextRect)
        pygame.display.update() # second update to show the the "removal"
        FPSCLOCK.tick(FPS)
        numOfCycles = numOfCycles - 1 # keeps subtracting the parameter and stops the loop when it reaches 0
    transition(0,2)

def ready_set_mash():
    # Displays the three words "Ready...", "Set..." "Type!" in quick succession.
    # The text gets bigger and bigger after "Ready..." until "Mash!" is shown.
    readyFont = pygame.font.Font(FONT_FILE, 80)
    readyText = readyFont.render('Ready...', True, BLACK, None)
    readyTextRect = readyText.get_rect()
    readyTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(readyText, readyTextRect)
    transition(1, 0.2)

    setTextFont = pygame.font.Font(FONT_FILE, 140) # A little bigger than "Ready..."
    setText = setTextFont.render('Set...', True, BLACK, None)
    setTextRect = setText.get_rect()
    setTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(setText, setTextRect)
    transition(1, 0.2)

    mashTextFont = pygame.font.Font(FONT_FILE, 200) # A lot bigger than "Set..."
    mashText = mashTextFont.render('MASH!', True, BLACK, None)
    mashTextRect = mashText.get_rect()
    mashTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(mashText, mashTextRect)
    transition(1, 0.2)

def BUTTON_MASH_win():
    # Shows the player that they won and applies all the win rewards.
    global win_has_been_called
    win_has_been_called = True
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 1)
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    WIN_SFX.play() # Plays the winning theme
    transition(0, 0.2)
    winTextFont = pygame.font.Font(FONT_FILE, 100)
    winText = winTextFont.render('You won!', True, BLACK, None)
    winTextRect = winText.get_rect()
    winTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    GAME_WINDOW.blit(winText, winTextRect)
    transition(3, 1)
    BUTTON_MASH_resetValues()
    winState() # Show the overall stats of the player before the next minigame.

def BUTTON_MASH_loss():
    # Show the player that they lost and applise all the loss rewards.
    global loss_has_been_called
    loss_has_been_called = True
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the losing theme.
    transition(0, 0.2)
    lossTextFont = pygame.font.Font(FONT_FILE, 100)
    lossText = lossTextFont.render('You lost!', True, BLACK, None)
    lossTextRect = lossText.get_rect()
    lossTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    GAME_WINDOW.blit(lossText, lossTextRect)
    transition(3, 1)
    BUTTON_MASH_resetValues()
    lossState()

def BUTTON_MASH_freeplay_win():
    # Same as the regular win but asks if the player wants to play again.
    global win_has_been_called
    win_has_been_called = True
    winning = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, BUTTON_MASH)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    
    WIN_SFX.play() # Plays the winning theme
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    transition(0, 0.2)
    while winning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        winTextFont = pygame.font.Font(FONT_FILE, 100)
        winText = winTextFont.render('You won!', True, BLACK, None)
        winTextRect = winText.get_rect()
        winTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(winText, winTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def BUTTON_MASH_freeplay_loss():
    # Same as the regular loss but asks if the player wants to play again.
    global loss_has_been_called
    loss_has_been_called = True
    losing = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, BUTTON_MASH)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the losing theme.
    transition(0, 0.2)
    while losing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        lossTextFont = pygame.font.Font(FONT_FILE, 100)
        lossText = lossTextFont.render('You lost!', True, BLACK, None)
        lossTextRect = lossText.get_rect()
        lossTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(lossText, lossTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def BUTTON_MASH_resetValues():
    # Resets every game variable back to its starting state.
    global a_count, s_count, d_count, f_count, g_count, h_count, j_count, k_count, l_count, chosenletter
    a_count = 0
    s_count = 0
    d_count = 0
    f_count = 0
    g_count = 0
    h_count = 0
    j_count = 0
    k_count = 0
    l_count = 0

    chosenletter = ''

def buttonMashCounter():
    # Displays a counter to the player of how many times they have mashed the selected letter.
    # Values to display the button mash counters for each letter
    global chosenletter
    display_a_count = COUNTER_FONT.render(str(a_count), True, BLACK, None)
    display_a_count_Rect = display_a_count.get_rect()
    display_a_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    display_s_count = COUNTER_FONT.render(str(s_count), True, BLACK, None)
    display_s_count_Rect = display_s_count.get_rect()
    display_s_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    display_d_count = COUNTER_FONT.render(str(d_count), True, BLACK, None)
    display_d_count_Rect = display_d_count.get_rect()
    display_d_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    display_f_count = COUNTER_FONT.render(str(f_count), True, BLACK, None)
    display_f_count_Rect = display_f_count.get_rect()
    display_f_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    display_g_count = COUNTER_FONT.render(str(g_count), True, BLACK, None)
    display_g_count_Rect = display_g_count.get_rect()
    display_g_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    display_h_count = COUNTER_FONT.render(str(h_count), True, BLACK, None)
    display_h_count_Rect = display_h_count.get_rect()
    display_h_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    display_j_count = COUNTER_FONT.render(str(j_count), True, BLACK, None)
    display_j_count_Rect = display_j_count.get_rect()
    display_j_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    display_k_count = COUNTER_FONT.render(str(k_count), True, BLACK, None)
    display_k_count_Rect = display_k_count.get_rect()
    display_k_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    display_l_count = COUNTER_FONT.render(str(l_count), True, BLACK, None)
    display_l_count_Rect = display_l_count.get_rect()
    display_l_count_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    # Values to display "Finished!" once the player has button mashed the letter enough.
    Finished = COUNTER_FONT.render('Finished!', True, BLACK, None)
    FinishedRect = Finished.get_rect()
    FinishedRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    
    if chosenletter == 'a':
        if a_count < 20:
            GAME_WINDOW.blit(display_a_count, display_a_count_Rect)  # Button mash counter for A
        elif a_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.
    elif chosenletter == 's':
        if s_count < 20:
            GAME_WINDOW.blit(display_s_count, display_s_count_Rect)  # Button mash counter for S  
        elif s_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.
    elif chosenletter == 'd':
        if d_count < 20:
            GAME_WINDOW.blit(display_d_count, display_d_count_Rect)  # Button mash counter for D
        elif d_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.
    elif chosenletter == 'f':
        if f_count < 20:
            GAME_WINDOW.blit(display_f_count, display_f_count_Rect)  # Button mash counter for F
        elif f_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.
        
    elif chosenletter == 'g':
        if g_count < 20:
            GAME_WINDOW.blit(display_g_count, display_g_count_Rect)  # Button mash counter for G
        elif g_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.
        
    elif chosenletter == 'h':
        if h_count < 20:
            GAME_WINDOW.blit(display_h_count, display_h_count_Rect)  # Button mash counter for H
        elif h_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.
        
    elif chosenletter == 'j':
        if j_count < 20:
            GAME_WINDOW.blit(display_j_count, display_j_count_Rect)  # Button mash counter for J
        elif j_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.
        
    elif chosenletter == 'k':
        if k_count < 20:
            GAME_WINDOW.blit(display_k_count, display_k_count_Rect)  # Button mash counter for K
        elif k_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.
        
    elif chosenletter == 'l':
        if l_count < 20:
            GAME_WINDOW.blit(display_l_count, display_l_count_Rect)  # Button mash counter for L
        elif l_count == 20:
            GAME_WINDOW.blit(Finished, FinishedRect) # Displays "Finished!" once player reaches the amount needed to mash.

def BUTTON_MASH_freeplay():
    # Screen shown to the player when they want to play Logic in Freeplay mode.
    pygame.mixer.Channel(4).unpause()# Unpause the background music
    GAME_WINDOW.fill(BG_COLOR)
    deciding = True
    # Button values
    playGameButton = Button('Yes', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, BUTTON_MASH)
    returnToFreeplayButton = Button('No', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, EXIT_BUTTON_CLICK_SFX, freeplay)

    # Text display values
    titleFont = pygame.font.Font(FONT_FILE, 80)
    subtitleFont = pygame.font.Font(FONT_FILE, 65)
    titleText = titleFont.render('Button Mash', True, BLACK, None)
    titleText_rect = titleText.get_rect()
    titleText_rect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

    subtitleText = subtitleFont.render('Play?', True, BLACK, None)
    subtitleText_rect = subtitleText.get_rect()
    subtitleText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    while deciding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        GAME_WINDOW.blit(titleText, titleText_rect)
        GAME_WINDOW.blit(subtitleText, subtitleText_rect)
        playGameButton.draw()
        returnToFreeplayButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def BUTTON_MASH():
    playing = True # boolean variable for the game loop. If it becomes False, the game has stopped executing.

    # Variables area
    global a_count, s_count, d_count, f_count, g_count, h_count, j_count, k_count, l_count, chosenletter, freeplay
    
    # Values that will display the shuffling of the letters
    chosenletter = random.choice(LETTERS)

    chosenletterFont = pygame.font.Font(FONT_FILE, 80)
    displaySelectedLetter = chosenletterFont.render(str(chosenletter), True, RED, BLACK) # variable for the selected letter and how it will look
    displaySelectedLetterRect = displaySelectedLetter.get_rect()
    displaySelectedLetterRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

    goMashFont = pygame.font.Font(FONT_FILE, 65)
    goMash = goMashFont.render('Mash it!', True, BLACK, None)
    goMashRect = goMash.get_rect()
    goMashRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 150)

    # Button sprite
    BUTTON_MASH_spritesGroup = pygame.sprite.Group()
    redButton = SpriteButton(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
    BUTTON_MASH_spritesGroup.add(redButton)
    
    pygame.display.set_caption('Button Mash!')
    GAME_WINDOW.fill(BG_COLOR)
    selectingLetter(50)
    ready_set_mash()
    start_ticks = pygame.time.get_ticks()
    while playing:
        seconds = 3 - (int((pygame.time.get_ticks() - start_ticks)/1000)) # If I were to add "scaling" difficulty, I should probably make the easiest be 5 sec, then 4 sec for medium, then 3 sec for hard.
        for event in pygame.event.get():
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if seconds > -1:
                if event.type == pygame.QUIT:               
                    pygame.quit() # deactivates the pygame library
                    playing = False              
                    sys.exit() # quit the program.  
                    
                if event.type == pygame.KEYDOWN:
                    # checking if key "A" was pressed and iterating a_count until it is mashed 20 times
                    if chosenletter == 'a' and event.key == pygame.K_a and a_count < 20:
                        a_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if a_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()
                    # checking if key "S" was pressed
                    elif chosenletter == 's' and event.key == pygame.K_s and s_count < 20:
                        s_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if s_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()                      
                    # checking if key "D" was pressed
                    elif chosenletter == 'd' and event.key == pygame.K_d and d_count < 20:
                        d_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if d_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()                                    
                    # checking if key "F" was pressed
                    elif chosenletter == 'f' and event.key == pygame.K_f and f_count < 20:
                        f_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if f_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()                                    
                    # checking if key "G" was pressed
                    if chosenletter == 'g' and event.key == pygame.K_g and g_count < 20:
                        g_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if g_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()                                   
                    # checking if key "H" was pressed
                    elif chosenletter == 'h' and event.key == pygame.K_h and h_count < 20:
                        h_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if h_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()                                    
                    # checking if key "J" was pressed
                    elif chosenletter == 'j' and event.key == pygame.K_j and j_count < 20:
                        j_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if j_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()                                    
                    # checking if key "K" was pressed
                    elif chosenletter == 'k' and event.key == pygame.K_k and k_count < 20:
                        k_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if k_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()                                         
                    # checking if key "L" was pressed
                    elif chosenletter == 'l' and event.key == pygame.K_l and l_count < 20:
                        l_count +=1
                        redButton.animate()
                        BUTTON_MASH_spritesGroup.update(1)
                        if l_count == 20:
                            if freeplay_mode == False: 
                                BUTTON_MASH_win()
                            elif freeplay_mode == True:
                                BUTTON_MASH_freeplay_win()                                    
        GAME_WINDOW.fill(BG_COLOR)
        GAME_WINDOW.blit(displaySelectedLetter, displaySelectedLetterRect) # Displays the "selected" letter after the shuffling
        buttonMashCounter() # Displays a button mash counter for the player
        
        displayCountdown = TIMER_FONT.render(str(seconds), True, BLACK, None)
        displayCountdownRect = displayCountdown.get_rect()
        displayCountdownRect.center = (WINDOW_WIDTH // 2, 100)
        if seconds > -1:
            GAME_WINDOW.blit(displayCountdown, displayCountdownRect)
            GAME_WINDOW.blit(goMash, goMashRect)
            BUTTON_MASH_spritesGroup.draw(GAME_WINDOW)
        elif seconds == -1:
            break      
        # Draws the surface object to the screen.                    
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    timeUp() # Once time is up, this function is run...
    #...and also the BUTTON_MASH_loss() functions after it.
    if freeplay_mode == False:
        BUTTON_MASH_loss() 
    elif freeplay_mode == True:
        BUTTON_MASH_freeplay_loss()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# COLORED CIRCLES GAME FUNCTIONS #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def decide_on_colors(numOfCycles):
    # Shows an animation of the program randomly cycling through the problems and then stops at
    # after x amount of cycles.

    while numOfCycles > 0:
        # the chosenLetter variables are meant for drawing the letter on the screen
        cycleFont = pygame.font.Font(FONT_FILE, 80)
        cycleText = cycleFont.render('Choosing colors...', True, BLACK, None)
        cycleTextRect = cycleText.get_rect()
        cycleTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

        pygame.display.update()
        time.sleep(0.02)
        GAME_WINDOW.fill(BG_COLOR)  # "removes" the blit to prevent overlapping
        GAME_WINDOW.blit(cycleText, cycleTextRect)
        pygame.display.update()  # second update to show the the "removal"
        FPSCLOCK.tick(FPS)
        # keeps subtracting the parameter and stops the loop when it reaches 0
        numOfCycles = numOfCycles - 1
    transition(0, 2)


def COLORED_CIRCLES_resetValues(list):
    # Resets all the important values to their original states after a win or loss.
    # list = the list where all the no.s are in.
    # Return all chosen colors into the original COLORS list.
    global randomColor1, randomColor2, randomColor3, randomColor4, randomColor5, randomColor6, randomColor7, randomColor8, chosenColors, chosenColors_string_list, questionColor
    for x in list:
        COLORS.append(x)

    list.clear()  # Clears the selected list, ready to get new values.

    # Restarts the code that was ran at the beginning to ensure there's a "new" order of colors
    randomColor1 = random.choice(COLORS)
    COLORS.remove(randomColor1)  # Ensures that there's no duplicates of colors
    randomColor2 = random.choice(COLORS)
    COLORS.remove(randomColor2)
    randomColor3 = random.choice(COLORS)
    COLORS.remove(randomColor3)
    randomColor4 = random.choice(COLORS)
    COLORS.remove(randomColor4)
    randomColor5 = random.choice(COLORS)
    COLORS.remove(randomColor5)
    randomColor6 = random.choice(COLORS)
    COLORS.remove(randomColor6)
    randomColor7 = random.choice(COLORS)
    COLORS.remove(randomColor7)
    randomColor8 = random.choice(COLORS)
    COLORS.remove(randomColor8)

    chosenColors = [randomColor1, randomColor2, randomColor3,
                    randomColor4, randomColor5, randomColor6, randomColor7, randomColor8]
    chosenColors_string_list = []
    for x in chosenColors:
        if x == RED:
            chosenColors_string_list.append(COLORS_STRING_LIST[0].upper())
        elif x == GREEN:
            chosenColors_string_list.append(COLORS_STRING_LIST[1].upper())
        elif x == BLUE:
            chosenColors_string_list.append(COLORS_STRING_LIST[2].upper())
        elif x == YELLOW:
            chosenColors_string_list.append(COLORS_STRING_LIST[3].upper())
        elif x == ORANGE:
            chosenColors_string_list.append(COLORS_STRING_LIST[4].upper())
        elif x == BLACK:
            chosenColors_string_list.append(COLORS_STRING_LIST[5].upper())
        elif x == PINK:
            chosenColors_string_list.append(COLORS_STRING_LIST[6].upper())
        elif x == PURPLE:
            chosenColors_string_list.append(COLORS_STRING_LIST[7].upper())

    questionColor = random.choice(chosenColors_string_list)

    # Removes the first question from the questions list and creates a new one to ensure it asks a random color.
    del questions[0]
    questions.insert(0, f'What row did {questionColor} appear on?')


def COLORED_CIRCLES_correct():
    # Shows the player that they were correct. Also plays a special sound.
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 2)
    CORRECT_SFX.play()
    correctFont = pygame.font.Font(FONT_FILE, 100)
    displayCorrect = correctFont.render('Correct!', True, GREEN, None)
    displayCorrectRect = displayCorrect.get_rect()
    displayCorrectRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    GAME_WINDOW.fill(BG_COLOR)
    GAME_WINDOW.blit(displayCorrect, displayCorrectRect)
    transition(1, 0)


def COLORED_CIRCLES_wrong():
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 2)
    WRONG_SFX.play()
    # Shows the player that they were wrong.
    wrongFont = pygame.font.Font(FONT_FILE, 100)
    displayWrong = wrongFont.render('Wrong!', True, RED, None)
    displayWrongRect = displayWrong.get_rect()
    displayWrongRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    GAME_WINDOW.fill(BG_COLOR)
    GAME_WINDOW.blit(displayWrong, displayWrongRect)
    transition(1, 0)


def COLORED_CIRCLES_win():
    global win_has_been_called
    win_has_been_called = True
    # Shows the player that they won and applies all the win rewards.
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 1)
    pygame.mixer.Channel(4).pause()# Pause the background music as the Win SFX is playing.
    WIN_SFX.play()  # Plays the winning theme.
    transition(0, 0.2)
    winTextFont = pygame.font.Font(FONT_FILE, 100)
    winText = winTextFont.render('You won!', True, BLACK, None)
    winTextRect = winText.get_rect()
    winTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(winText, winTextRect)
    transition(3, 1)
    COLORED_CIRCLES_resetValues(chosenColors)
    winState() # Show the overall stats of the player before the next minigame.
    # startMenu()


def COLORED_CIRCLES_loss():
    global loss_has_been_called
    loss_has_been_called = True
    # Show the player that they lost and applise all the loss rewards.
    pygame.mixer.Channel(4).pause()# Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the losing theme.
    transition(0, 0.2)
    lossTextFont = pygame.font.Font(FONT_FILE, 100)
    lossText = lossTextFont.render('You lost!', True, BLACK, None)
    lossTextRect = lossText.get_rect()
    lossTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(lossText, lossTextRect)
    transition(3, 1)
    COLORED_CIRCLES_resetValues(chosenColors)
    lossState()
    # startMenu()

def COLORED_CIRCLES_freeplay_win():
    # Same as the regular win but asks if the player wants to play again.
    global win_has_been_called
    win_has_been_called = True
    winning = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, COLORED_CIRCLES)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    
    WIN_SFX.play() # Plays the winning theme
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    transition(0, 0.2)
    COLORED_CIRCLES_resetValues(chosenColors)
    while winning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        winTextFont = pygame.font.Font(FONT_FILE, 100)
        winText = winTextFont.render('You won!', True, BLACK, None)
        winTextRect = winText.get_rect()
        winTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(winText, winTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def COLORED_CIRCLES_freeplay_loss():
    # Same as the regular loss but asks if the player wants to play again.
    global loss_has_been_called
    loss_has_been_called = True
    losing = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, COLORED_CIRCLES)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the losing theme.
    transition(0, 0.2)
    COLORED_CIRCLES_resetValues(chosenColors)
    while losing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        lossTextFont = pygame.font.Font(FONT_FILE, 100)
        lossText = lossTextFont.render('You lost!', True, BLACK, None)
        lossTextRect = lossText.get_rect()
        lossTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(lossText, lossTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawNoFillCircles():
    # Draws the first row of circles
    pygame.draw.circle(GAME_WINDOW, BLACK, ((
        WINDOW_WIDTH // 2) - 95, (WINDOW_HEIGHT // 2) - 50), CIRCLE_SIZE, NOFILL)
    pygame.draw.circle(GAME_WINDOW, BLACK, ((
        WINDOW_WIDTH // 2) - 35, (WINDOW_HEIGHT // 2) - 50), CIRCLE_SIZE, NOFILL)
    pygame.draw.circle(GAME_WINDOW, BLACK, ((
        WINDOW_WIDTH // 2) + 35, (WINDOW_HEIGHT // 2) - 50), CIRCLE_SIZE, NOFILL)
    pygame.draw.circle(GAME_WINDOW, BLACK, ((
        WINDOW_WIDTH // 2) + 95, (WINDOW_HEIGHT // 2) - 50), CIRCLE_SIZE, NOFILL)
    # Draws the second row of circles
    pygame.draw.circle(GAME_WINDOW, BLACK, ((
        WINDOW_WIDTH // 2) - 95, (WINDOW_HEIGHT // 2)), CIRCLE_SIZE, NOFILL)
    pygame.draw.circle(GAME_WINDOW, BLACK, ((
        WINDOW_WIDTH // 2) - 35, (WINDOW_HEIGHT // 2)), CIRCLE_SIZE, NOFILL)
    pygame.draw.circle(GAME_WINDOW, BLACK, ((
        WINDOW_WIDTH // 2) + 35, (WINDOW_HEIGHT // 2)), CIRCLE_SIZE, NOFILL)
    pygame.draw.circle(GAME_WINDOW, BLACK, ((
        WINDOW_WIDTH // 2) + 95, (WINDOW_HEIGHT // 2)), CIRCLE_SIZE, NOFILL)
    pygame.display.update()
    transition(2, 0.5)


def drawFillCircles():
    # Fills the circles with random colors.
    memorizing = True  # True = player is still memorizing. False = move on to the questions
    # Picks a random color from the colors
    # I think there's an easier way to do this. Fix this when you can
    memorize_ticks = pygame.time.get_ticks()
    seconds_amt = 10
    while memorizing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                memorizing = False
                pygame.exit()
                sys.exit()
            # If player clicks during any part of the minigame loading, it does nothing (prevents freezing)
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        GAME_WINDOW.fill(BG_COLOR)
        memorize_seconds = seconds_amt - \
            (int((pygame.time.get_ticks() - memorize_ticks)/1000))
        displayMemorizeCountdown = TIMER_FONT.render(
            str(memorize_seconds), True, BLACK, None)
        displayMemorizeCountdownRect = displayMemorizeCountdown.get_rect()
        displayMemorizeCountdownRect.center = (WINDOW_WIDTH // 2, 75)

        if memorize_seconds > -1:
            GAME_WINDOW.blit(displayMemorizeCountdown,
                             displayMemorizeCountdownRect)
            # Draws the first row of filled circles
            pygame.draw.circle(GAME_WINDOW, randomColor1, ((
                WINDOW_WIDTH // 2) - 95, (WINDOW_HEIGHT // 2) - 50), CIRCLE_SIZE, FILL)
            pygame.draw.circle(GAME_WINDOW, randomColor2, ((
                WINDOW_WIDTH // 2) - 35, (WINDOW_HEIGHT // 2) - 50), CIRCLE_SIZE, FILL)
            pygame.draw.circle(GAME_WINDOW, randomColor3, ((
                WINDOW_WIDTH // 2) + 35, (WINDOW_HEIGHT // 2) - 50), CIRCLE_SIZE, FILL)
            pygame.draw.circle(GAME_WINDOW, randomColor4, ((
                WINDOW_WIDTH // 2) + 95, (WINDOW_HEIGHT // 2) - 50), CIRCLE_SIZE, FILL)
            # Draws the second row of filled circles
            pygame.draw.circle(GAME_WINDOW, randomColor5, ((
                WINDOW_WIDTH // 2) - 95, (WINDOW_HEIGHT // 2)), CIRCLE_SIZE, FILL)
            pygame.draw.circle(GAME_WINDOW, randomColor6, ((
                WINDOW_WIDTH // 2) - 35, (WINDOW_HEIGHT // 2)), CIRCLE_SIZE, FILL)
            pygame.draw.circle(GAME_WINDOW, randomColor7, ((
                WINDOW_WIDTH // 2) + 35, (WINDOW_HEIGHT // 2)), CIRCLE_SIZE, FILL)
            pygame.draw.circle(GAME_WINDOW, randomColor8, ((
                WINDOW_WIDTH // 2) + 95, (WINDOW_HEIGHT // 2)), CIRCLE_SIZE, FILL)

            # Draws a black "outline" on all circles
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH // 2) - 95, (WINDOW_HEIGHT // 2) - 50), CIRCLE_OUTLINE, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH // 2) - 35, (WINDOW_HEIGHT // 2) - 50), CIRCLE_OUTLINE, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH // 2) + 35, (WINDOW_HEIGHT // 2) - 50), CIRCLE_OUTLINE, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH // 2) + 95, (WINDOW_HEIGHT // 2) - 50), CIRCLE_OUTLINE, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH // 2) - 95, (WINDOW_HEIGHT // 2)), CIRCLE_OUTLINE, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH // 2) - 35, (WINDOW_HEIGHT // 2)), CIRCLE_OUTLINE, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH // 2) + 35, (WINDOW_HEIGHT // 2)), CIRCLE_OUTLINE, NOFILL)
            pygame.draw.circle(GAME_WINDOW, BLACK, ((
                WINDOW_WIDTH // 2) + 95, (WINDOW_HEIGHT // 2)), CIRCLE_OUTLINE, NOFILL)

            # Values that will display the instructions ('Solve!') beneath the problem
            instructionsFont = pygame.font.Font(FONT_FILE, 80)
            displayInstructions = instructionsFont.render(
                'Memorize!', True, BLACK, None)
            # I think I should also add a countdown timer during this part. Show the player they have 5 seconds to memorize
            displayInstructionsRect = displayInstructions.get_rect()
            displayInstructionsRect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 60)

            GAME_WINDOW.blit(displayInstructions, displayInstructionsRect)
            pygame.display.update()
        elif memorize_seconds == -1:
            break
    transition(1, 1)


def COLORED_CIRCLES_showAnswers():
    # Shows the answers to the player in multiple choice format (A B C D)

    # Values to display the answers (which are 4 of the chosen numbers)
    # What row did [random color] appear on?'
    if chosenQuestion == questions[0]:
        displayAnswerA = FONT.render('TOP', True, BLACK, None)
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 25)

        displayAnswerB = FONT.render('BOTTOM', True, BLACK, None)
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 25)

        GAME_WINDOW.blit(displayAnswerA, displayAnswerARect)
        GAME_WINDOW.blit(displayAnswerB, displayAnswerBRect)

    # 'What color was on the top left?'
    if chosenQuestion == questions[1]:
        displayAnswerA = FONT.render(
            chosenColors_string_list[3], True, BLACK, None)
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

        # The first color to be appended is always the top-left color.
        displayAnswerB = FONT.render(
            chosenColors_string_list[0], True, BLACK, None)
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        displayAnswerC = FONT.render(
            chosenColors_string_list[2], True, BLACK, None)
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

        displayAnswerD = FONT.render(
            chosenColors_string_list[1], True, BLACK, None)
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)

        GAME_WINDOW.blit(displayAnswerA, displayAnswerARect)
        GAME_WINDOW.blit(displayAnswerB, displayAnswerBRect)
        GAME_WINDOW.blit(displayAnswerC, displayAnswerCRect)
        GAME_WINDOW.blit(displayAnswerD, displayAnswerDRect)

    # 'What color was on the bottom right?'
    if chosenQuestion == questions[2]:
        displayAnswerA = FONT.render(
            chosenColors_string_list[6], True, BLACK, None)
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

        displayAnswerB = FONT.render(
            chosenColors_string_list[5], True, BLACK, None)
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        # The last to be appended is always the bot-right color.
        displayAnswerC = FONT.render(
            chosenColors_string_list[7], True, BLACK, None)
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

        displayAnswerD = FONT.render(
            chosenColors_string_list[4], True, BLACK, None)
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
        GAME_WINDOW.blit(displayAnswerA, displayAnswerARect)
        GAME_WINDOW.blit(displayAnswerB, displayAnswerBRect)
        GAME_WINDOW.blit(displayAnswerC, displayAnswerCRect)
        GAME_WINDOW.blit(displayAnswerD, displayAnswerDRect)

    # 'What color was second from the top left?'
    if chosenQuestion == questions[3]:
        displayAnswerA = FONT.render(
            chosenColors_string_list[3], True, BLACK, None)
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

        displayAnswerB = FONT.render(
            chosenColors_string_list[5], True, BLACK, None)
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        displayAnswerC = FONT.render(
            chosenColors_string_list[7], True, BLACK, None)
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

        # The 2nd to be appended is always the second from the top-left.
        displayAnswerD = FONT.render(
            chosenColors_string_list[1], True, BLACK, None)
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
        GAME_WINDOW.blit(displayAnswerA, displayAnswerARect)
        GAME_WINDOW.blit(displayAnswerB, displayAnswerBRect)
        GAME_WINDOW.blit(displayAnswerC, displayAnswerCRect)
        GAME_WINDOW.blit(displayAnswerD, displayAnswerDRect)

    # 'What color was second from the top right?'
    if chosenQuestion == questions[4]:
        # The third to be appended is always the second from the top-left color.
        displayAnswerA = FONT.render(
            chosenColors_string_list[2], True, BLACK, None)
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

        displayAnswerB = FONT.render(
            chosenColors_string_list[7], True, BLACK, None)
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        displayAnswerC = FONT.render(
            chosenColors_string_list[3], True, BLACK, None)
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

        displayAnswerD = FONT.render(
            chosenColors_string_list[5], True, BLACK, None)
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (
            WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
        GAME_WINDOW.blit(displayAnswerA, displayAnswerARect)
        GAME_WINDOW.blit(displayAnswerB, displayAnswerBRect)
        GAME_WINDOW.blit(displayAnswerC, displayAnswerCRect)
        GAME_WINDOW.blit(displayAnswerD, displayAnswerDRect)


def COLORED_CIRCLES_checkAnswersA():
    # Checks the players answer for choice A if they were right or wrong

    # If player answered A for 'What row did [random color] appear on?'
    if chosenQuestion == questions[0]:
        # WORKING AS INTENDED
        # Any of the first 4 colors are in the top row.
        if questionColor == chosenColors_string_list[0] or questionColor == chosenColors_string_list[1] or questionColor == chosenColors_string_list[2] or questionColor == chosenColors_string_list[3]:
            COLORED_CIRCLES_correct()
            if freeplay_mode == False:
                COLORED_CIRCLES_win()
            elif freeplay_mode == True:
                COLORED_CIRCLES_freeplay_win()
        # Any of the last 4 colors are in the bot row.
        elif questionColor == chosenColors_string_list[4] or questionColor == chosenColors_string_list[5] or questionColor == chosenColors_string_list[6] or questionColor == chosenColors_string_list[7]:
            COLORED_CIRCLES_wrong()
            if freeplay_mode == False:
                COLORED_CIRCLES_loss()
            elif freeplay_mode == True:
                COLORED_CIRCLES_freeplay_loss()

    # If player answered A for 'What color was on the top left?'
    elif chosenQuestion == questions[1]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered A for 'What color was on the bottom right?'
    elif chosenQuestion == questions[2]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered A for 'What color was second from the top left?'
    elif chosenQuestion == questions[3]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered A for 'What color was second from the top right?'
    elif chosenQuestion == questions[4]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_correct()
        if freeplay_mode == False:
                COLORED_CIRCLES_win()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_win()


def COLORED_CIRCLES_checkAnswersB():
    # Checks the players answer for choice B if they were right or wrong

    # If player answered B for 'Which number was 1st on the left?'
    if chosenQuestion == questions[0]:
        # WORKING AS INTENDED
        # Any of the first 4 colors are in the top row.
        if questionColor == chosenColors_string_list[0] or questionColor == chosenColors_string_list[1] or questionColor == chosenColors_string_list[2] or questionColor == chosenColors_string_list[3]:
            COLORED_CIRCLES_wrong()
            if freeplay_mode == False:
                COLORED_CIRCLES_loss()
            elif freeplay_mode == True:
                COLORED_CIRCLES_freeplay_loss()
        # Any of the last 4 colors are in the bot row.
        elif questionColor == chosenColors_string_list[4] or questionColor == chosenColors_string_list[5] or questionColor == chosenColors_string_list[6] or questionColor == chosenColors_string_list[7]:
            # If the questionColor was one of the last 4, then the player is correct
            COLORED_CIRCLES_correct()
            if freeplay_mode == False:
                COLORED_CIRCLES_win()
            elif freeplay_mode == True:
                COLORED_CIRCLES_freeplay_win()

    # If player answered B for 'What color was on the top left?'
    elif chosenQuestion == questions[1]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_correct()
        if freeplay_mode == False:
            COLORED_CIRCLES_win()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_win()

    # If player answered B for 'Which number was 1st on the right?'
    elif chosenQuestion == questions[2]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered B for 'What color was second from the top left?'
    elif chosenQuestion == questions[3]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered B for 'What color was second from the top right?'
    elif chosenQuestion == questions[4]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()


def COLORED_CIRCLES_checkAnswersC():
    # Checks the players answer for choice C if they were right or wrong

    # If player answered C for 'What color was on the top left?'
    if chosenQuestion == questions[1]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered C for 'What color was on the bottom right?'
    elif chosenQuestion == questions[2]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_correct()
        if freeplay_mode == False:
            COLORED_CIRCLES_win()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_win()

    # If player answered C for 'What color was second from the top left?'
    elif chosenQuestion == questions[3]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered C for 'What color was second from the top right?'
    elif chosenQuestion == questions[4]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()


def COLORED_CIRCLES_checkAnswersD():
    # Checks the players answer for choice B if they were right or wrong

    # If player answered D for 'What color was on the top left?'
    if chosenQuestion == questions[1]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered D for 'What color was on the bottom right?'
    elif chosenQuestion == questions[2]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()

    # If player answered D for 'What color was second from the top left?'
    elif chosenQuestion == questions[3]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_correct()
        if freeplay_mode == False:
            COLORED_CIRCLES_win()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_win()

    # If player answered D for 'What color was second from the top right?'
    elif chosenQuestion == questions[4]:
        # WORKING AS INTENDED
        COLORED_CIRCLES_wrong()
        if freeplay_mode == False:
            COLORED_CIRCLES_loss()
        elif freeplay_mode == True:
            COLORED_CIRCLES_freeplay_loss()


def COLORED_CIRCLES_instructions():
    # Shows the player what they need to do to win the Logic minigame
    GAME_WINDOW.fill(BG_COLOR)
    COLORED_CIRCLES_instructing = True
    COLORED_CIRCLES_showingThreeInstructions = True

    # Values to display the 3 instructions
    COLORED_CIRCLES_instruction_font = pygame.font.Font(
        FONT_FILE, 50)  # Font style
    COLORED_CIRCLES_ready_font = pygame.font.Font(FONT_FILE, 80)
    COLORED_CIRCLES_first_instruction_text = COLORED_CIRCLES_instruction_font.render(
        '2 rows of 4 circles are shown.', True, BLACK, None)
    COLORED_CIRCLES_first_instruction_text_rect = COLORED_CIRCLES_first_instruction_text.get_rect()

    COLORED_CIRCLES_second_instruction_text = COLORED_CIRCLES_instruction_font.render(
        'Memorize their positions.', True, BLACK, None)
    COLORED_CIRCLES_second_instruction_text_rect = COLORED_CIRCLES_second_instruction_text.get_rect()

    COLORED_CIRCLES_third_instruction_text = COLORED_CIRCLES_instruction_font.render(
        '...then answer the question.', True, BLACK, None)
    COLORED_CIRCLES_third_instruction_text_rect = COLORED_CIRCLES_third_instruction_text.get_rect()

    COLORED_CIRCLES_ready_instruction_text = COLORED_CIRCLES_ready_font.render(
        'Ready?', True, BLACK, None)
    COLORED_CIRCLES_ready_instruction_text_rect = COLORED_CIRCLES_ready_instruction_text.get_rect()

    COLORED_CIRCLES_readyButton = Button('I\'m ready!', 300, 60, ((
        WINDOW_WIDTH // 2) - 450, (WINDOW_HEIGHT // 2) + 200), 6, BUTTON_CLICK_SFX, COLORED_CIRCLES)
    COLORED_CIRCLES_nopeButton = Button('Nope!', 300, 60, ((
        WINDOW_WIDTH // 2) + 150, (WINDOW_HEIGHT // 2) + 200), 6, BUTTON_CLICK_SFX, startMenu)
    while COLORED_CIRCLES_instructing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                COLORED_CIRCLES_instructing = False
                pygame.quit()
                sys.exit()
        if COLORED_CIRCLES_showingThreeInstructions:  # Plays the instruction "animation."
            COLORED_CIRCLES_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            # Show the first instruction at the middle.
            GAME_WINDOW.blit(COLORED_CIRCLES_first_instruction_text,
                             COLORED_CIRCLES_first_instruction_text_rect)
            pygame.display.update()
            transition(1, 0.2)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            COLORED_CIRCLES_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

            COLORED_CIRCLES_second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            # Show the first instruction at the top of the 2nd instruction.
            GAME_WINDOW.blit(COLORED_CIRCLES_first_instruction_text,
                             COLORED_CIRCLES_first_instruction_text_rect)
            # Show the second instruction at the middle.
            GAME_WINDOW.blit(COLORED_CIRCLES_second_instruction_text,
                             COLORED_CIRCLES_second_instruction_text_rect)
            pygame.display.update()
            transition(1, 0.2)
            # FOCUS HERE NEXT TIME (3 PM, 11/17/22)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            COLORED_CIRCLES_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.
            COLORED_CIRCLES_second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            COLORED_CIRCLES_third_instruction_text_rect = COLORED_CIRCLES_third_instruction_text.get_rect()
            COLORED_CIRCLES_third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            # Show the first instruction at the top of the 2nd & 3rd instruction.
            GAME_WINDOW.blit(COLORED_CIRCLES_first_instruction_text,
                             COLORED_CIRCLES_first_instruction_text_rect)
            # Show the second instruction at the top of the 3rd instruction.
            GAME_WINDOW.blit(COLORED_CIRCLES_second_instruction_text,
                             COLORED_CIRCLES_second_instruction_text_rect)
            # Show the 3rd instruction at the middle.
            GAME_WINDOW.blit(COLORED_CIRCLES_third_instruction_text,
                             COLORED_CIRCLES_third_instruction_text_rect)

            transition(1, 0.2)

            # Move the 1st instructions a little higher when the 2nd set shows up.
            COLORED_CIRCLES_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.
            COLORED_CIRCLES_second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            COLORED_CIRCLES_third_instruction_text = COLORED_CIRCLES_instruction_font.render(
                '...then answer the question.', True, BLACK, None)
            COLORED_CIRCLES_third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            COLORED_CIRCLES_ready_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
            GAME_WINDOW.blit(COLORED_CIRCLES_first_instruction_text,
                             COLORED_CIRCLES_first_instruction_text_rect)  # Same as before
            GAME_WINDOW.blit(COLORED_CIRCLES_second_instruction_text,
                             COLORED_CIRCLES_second_instruction_text_rect)  # Same as before
            GAME_WINDOW.blit(COLORED_CIRCLES_third_instruction_text,
                             COLORED_CIRCLES_third_instruction_text_rect)  # Same as before
            # Show 'Ready!' below the 3rd instruction
            GAME_WINDOW.blit(COLORED_CIRCLES_ready_instruction_text,
                             COLORED_CIRCLES_ready_instruction_text_rect)

            transition(1, 0.2)
            # Done showing the 3 instructions.
            COLORED_CIRCLES_showingThreeInstructions = False

        # Permanently shows the 3 instructions along with the Ready at the bottom.
        elif not COLORED_CIRCLES_showingThreeInstructions:
            # Move the 1st instructions a little higher when the 2nd set shows up.
            COLORED_CIRCLES_first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200)
            # Move the 2nd instructions a little higher when the 3rd set shows up.
            COLORED_CIRCLES_second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)
            COLORED_CIRCLES_third_instruction_text = COLORED_CIRCLES_instruction_font.render(
                '...then answer the question.', True, BLACK, None)
            COLORED_CIRCLES_third_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            COLORED_CIRCLES_ready_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
            GAME_WINDOW.blit(COLORED_CIRCLES_first_instruction_text,
                             COLORED_CIRCLES_first_instruction_text_rect)
            GAME_WINDOW.blit(COLORED_CIRCLES_second_instruction_text,
                             COLORED_CIRCLES_second_instruction_text_rect)
            GAME_WINDOW.blit(COLORED_CIRCLES_third_instruction_text,
                             COLORED_CIRCLES_third_instruction_text_rect)
            GAME_WINDOW.blit(COLORED_CIRCLES_ready_instruction_text,
                             COLORED_CIRCLES_ready_instruction_text_rect)

        COLORED_CIRCLES_readyButton.draw()
        COLORED_CIRCLES_nopeButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    GAME_WINDOW.fill(BG_COLOR)
    return

def COLORED_CIRCLES_freeplay():
    # Screen shown to the player when they want to play Colored Circles in Freeplay mode.
    pygame.mixer.Channel(4).unpause()# Unpause the background music
    GAME_WINDOW.fill(BG_COLOR)
    deciding = True
    # Button values
    playGameButton = Button('Yes', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, COLORED_CIRCLES)
    returnToFreeplayButton = Button('No', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, EXIT_BUTTON_CLICK_SFX, freeplay)

    # Text display values
    titleFont = pygame.font.Font(FONT_FILE, 80)
    subtitleFont = pygame.font.Font(FONT_FILE, 65)
    titleText = titleFont.render('Colored Circles', True, BLACK, None)
    titleText_rect = titleText.get_rect()
    titleText_rect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

    subtitleText = subtitleFont.render('Play?', True, BLACK, None)
    subtitleText_rect = subtitleText.get_rect()
    subtitleText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    while deciding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        GAME_WINDOW.blit(titleText, titleText_rect)
        GAME_WINDOW.blit(subtitleText, subtitleText_rect)
        playGameButton.draw()
        returnToFreeplayButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def COLORED_CIRCLES():
    global playing
    playing = True  # True = game is not done. False = game is done

    # Variables area

    pygame.display.set_caption('Colored Circles') # I think I'll eventually change this to also show which no. minigame the player is on
    GAME_WINDOW.fill(BG_COLOR)

    QuestionFont = pygame.font.Font(FONT_FILE, 48)

    # drawNoFillCircles() # Draws circles with no color first. Ensures that it will be random each time, no "true" cycle
    decide_on_colors(30)
    drawFillCircles()  # Fills the circles with colors in random order
    showRandomQuestion(questions)
    if chosenQuestion == questions[0]:
        aButton = Button('A', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                         2) - 35), 6, BUTTON_CLICK_SFX, COLORED_CIRCLES_checkAnswersA)
        bButton = Button('B', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                         2) + 15), 6, BUTTON_CLICK_SFX, COLORED_CIRCLES_checkAnswersB)
    else:
        aButton = Button('A', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                         2) - 105), 4, BUTTON_CLICK_SFX, COLORED_CIRCLES_checkAnswersA)
        bButton = Button('B', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                         2) - 55), 4, BUTTON_CLICK_SFX, COLORED_CIRCLES_checkAnswersB)
        cButton = Button('C', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                         2) - 5), 4, BUTTON_CLICK_SFX, COLORED_CIRCLES_checkAnswersC)
        dButton = Button('D', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                         2) + 45), 4, BUTTON_CLICK_SFX, COLORED_CIRCLES_checkAnswersD)
    start_ticks = pygame.time.get_ticks()
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                # If player clicks during any part of the minigame loading, it does nothing (prevents freezing)
                pass
        GAME_WINDOW.fill(BG_COLOR)
        # If I were to add "scaling" difficulty, I should probably make the easiest be 5 sec, then 4 sec for medium, then 3 sec for hard.
        seconds = 5 - (int((pygame.time.get_ticks() - start_ticks)/1000))
        displayCountdown = TIMER_FONT.render(str(seconds), True, BLACK, None)
        displayCountdownRect = displayCountdown.get_rect()
        displayCountdownRect.center = (WINDOW_WIDTH // 2, 75)

        displayQuestion = QuestionFont.render(
            chosenQuestion, True, BLACK, None)
        displayQuestionRect = displayQuestion.get_rect()
        if chosenQuestion == questions[0]:
            # This question will be positioned lower than the others.
            displayQuestionRect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 75)
        else:
            displayQuestionRect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 175)
        if seconds > -1:  # Countdown timer should come first. Everything else is under it
            GAME_WINDOW.blit(displayCountdown, displayCountdownRect)
            GAME_WINDOW.blit(displayQuestion, displayQuestionRect)
            COLORED_CIRCLES_showAnswers()

            # print(pygame.mouse.get_focused())
            if chosenQuestion == questions[0]:
                aButton.draw()
                bButton.draw()
            else:
                aButton.draw()
                bButton.draw()
                cButton.draw()
                dButton.draw()
        elif seconds == -1:
            timeUp()
            if freeplay_mode == False:
                COLORED_CIRCLES_loss()
            elif freeplay_mode == True:
                COLORED_CIRCLES_freeplay_loss()

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  DISAPPEARING # FUNCTIONS  #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def cycle_through_numbers(numOfCycles):
    # Shows an animation of the program randomly cycling through the problems and then stops at
    # after x amount of cycles.

    while numOfCycles > 0:

        cycleText = FONT.render('Cycling...', True, BLACK, None)
        cycleTextRect = cycleText.get_rect()
        cycleTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

        # Font style for the numbers
        cyclingThroughNumbersFont = pygame.font.Font(FONT_FILE, 50)
        
        # 1st Number
        cyclingThroughNumbers_1 = cyclingThroughNumbersFont.render(str(getRandom(NUMBERS)), True, BLACK, WHITE) # variable for how the text will look
        cyclingThroughNumbers_1_Rect = cyclingThroughNumbers_1.get_rect()
        cyclingThroughNumbers_1_Rect.center = ((WINDOW_WIDTH // 2) - 200, (WINDOW_HEIGHT // 2) - 50)

        # 2nd Number
        cyclingThroughNumbers_2 = cyclingThroughNumbersFont.render(str(getRandom(NUMBERS)), True, BLACK, WHITE) # variable for how the text will look
        cyclingThroughNumbers_2_Rect = cyclingThroughNumbers_2.get_rect()
        cyclingThroughNumbers_2_Rect.center = ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT // 2) - 50)

        # 3rd Number
        cyclingThroughNumbers_3 = cyclingThroughNumbersFont.render(str(getRandom(NUMBERS)), True, BLACK, WHITE) # variable for how the text will look
        cyclingThroughNumbers_3_Rect = cyclingThroughNumbers_3.get_rect()
        cyclingThroughNumbers_3_Rect.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2) - 50)

        # 4th Number
        cyclingThroughNumbers_4 = cyclingThroughNumbersFont.render(str(getRandom(NUMBERS)), True, BLACK, WHITE) # variable for how the text will look
        cyclingThroughNumbers_4_Rect = cyclingThroughNumbers_4.get_rect()
        cyclingThroughNumbers_4_Rect.center = ((WINDOW_WIDTH // 2) + 100, (WINDOW_HEIGHT // 2) - 50)

        # 5th Number
        cyclingThroughNumbers_5 = cyclingThroughNumbersFont.render(str(getRandom(NUMBERS)), True, BLACK, WHITE) # variable for how the text will look
        cyclingThroughNumbers_5_Rect = cyclingThroughNumbers_5.get_rect()
        cyclingThroughNumbers_5_Rect.center = ((WINDOW_WIDTH // 2) + 200, (WINDOW_HEIGHT // 2) - 50)

        GAME_WINDOW.blit(cyclingThroughNumbers_1, cyclingThroughNumbers_1_Rect)
        GAME_WINDOW.blit(cyclingThroughNumbers_2, cyclingThroughNumbers_2_Rect)
        GAME_WINDOW.blit(cyclingThroughNumbers_3, cyclingThroughNumbers_3_Rect)
        GAME_WINDOW.blit(cyclingThroughNumbers_4, cyclingThroughNumbers_4_Rect)
        GAME_WINDOW.blit(cyclingThroughNumbers_5, cyclingThroughNumbers_5_Rect)

        pygame.display.update()
        time.sleep(0.02)
        GAME_WINDOW.fill(BG_COLOR) # "removes" the blit to prevent overlapping
        GAME_WINDOW.blit(cycleText, cycleTextRect) 
        pygame.display.update() # second update to show the the "removal"
        FPSCLOCK.tick(FPS)
        numOfCycles -= 1 # keeps subtracting the parameter and stops the loop when it reaches 0

def show_chosen_numbers():
    # Shows the player the chosen numbers and tells them to memorize it. Disappears after 3 seconds, after which the second set of instructions
    # is shown (in the main() loop)

    # Values that hold the 6 randomly chosen numbers. Global because they will be used in the questions function
    global chosen_number_1, chosen_number_2, chosen_number_3, chosen_number_4, chosen_number_5, chosen_number_list
    chosen_number_1 = str(getRandom(NUMBERS))
    NUMBERS.remove(chosen_number_1) # Ensures the next no. is not a duplicate
    chosen_number_2 = str(getRandom(NUMBERS))
    NUMBERS.remove(chosen_number_2)
    chosen_number_3 = str(getRandom(NUMBERS))
    NUMBERS.remove(chosen_number_3)
    chosen_number_4 = str(getRandom(NUMBERS))
    NUMBERS.remove(chosen_number_4)
    chosen_number_5 = str(getRandom(NUMBERS))
    NUMBERS.remove(chosen_number_5)

    # For testing purposes, put any number inside str()
    # chosen_number_1 = str(1)
    # chosen_number_2 = str(1)
    # chosen_number_3 = str(3)
    # chosen_number_4 = str(4)
    # chosen_number_5 = str(2)

    # Appending the chosen_numbers to a list. Used for checking the player's answers later
    chosen_number_list.append(int(chosen_number_1))
    chosen_number_list.append(int(chosen_number_2))
    chosen_number_list.append(int(chosen_number_3))
    chosen_number_list.append(int(chosen_number_4))
    chosen_number_list.append(int(chosen_number_5))

    # Values that will display the selected numbers
    showNumberText = pygame.font.Font(FONT_FILE, 70)

    # Values that will display the first set of instructions ('Memorize!') beneath the chosen numbers
    instructionsFont = pygame.font.Font(FONT_FILE, 80)
    displayInstructions1 = instructionsFont.render('Memorize!', True, BLACK, None)
    displayInstructions1_Rect = displayInstructions1.get_rect()
    displayInstructions1_Rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    # 1st Number
    showNumber1 = showNumberText.render(chosen_number_1, True, BLACK, None)
    showNumber1_Rect = showNumber1.get_rect()
    showNumber1_Rect.center = ((WINDOW_WIDTH // 2) - 200, (WINDOW_HEIGHT // 2) - 50 )

    # 2nd Number
    showNumber2 = showNumberText.render(chosen_number_2, True, BLACK, WHITE) # variable for how the text will look
    showNumber2_Rect = showNumber2.get_rect()
    showNumber2_Rect.center = ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT // 2) - 50)

    # 3rd Number
    showNumber3 = showNumberText.render(chosen_number_3, True, BLACK, WHITE) # variable for how the text will look
    showNumber3_Rect = showNumber3.get_rect()
    showNumber3_Rect.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2) - 50)

    # 4th Number
    showNumber4 = showNumberText.render(chosen_number_4, True, BLACK, WHITE) # variable for how the text will look
    showNumber4_Rect = showNumber4.get_rect()
    showNumber4_Rect.center = ((WINDOW_WIDTH // 2) + 100, (WINDOW_HEIGHT // 2) - 50)

    # 5th Number
    showNumber5 = showNumberText.render(chosen_number_5, True, BLACK, WHITE) # variable for how the text will look
    showNumber5_Rect = showNumber5.get_rect()
    showNumber5_Rect.center = ((WINDOW_WIDTH // 2) + 200, (WINDOW_HEIGHT // 2) - 50)

    GAME_WINDOW.blit(showNumber1, showNumber1_Rect)
    GAME_WINDOW.blit(showNumber2, showNumber2_Rect)
    GAME_WINDOW.blit(showNumber3, showNumber3_Rect)
    GAME_WINDOW.blit(showNumber4, showNumber4_Rect)
    GAME_WINDOW.blit(showNumber5, showNumber5_Rect)
    GAME_WINDOW.blit(displayInstructions1, displayInstructions1_Rect) # Displays "Memorize!" underneath the problem

    pygame.display.update()
    time.sleep(0.02)
    FPSCLOCK.tick(FPS)
    pygame.time.delay(3000) # Shows the player the numbers for 3 seconds before disappearing
    GAME_WINDOW.fill(BG_COLOR)
    pygame.display.update()
    pygame.time.delay(2000) # Waits 1.5 seconds before the questions pop up

def DISAPPEARING_NUMBERS_resetValues(list):
    # Resets all the important values to their original states after a win or loss.
    # list = the list where all the no.s are in.
    # Return all chosen numbers into the original NUMBERS list.
    for x in list:
        NUMBERS.append(str(x))
        
    list.clear() # Clears the selected list, ready to get new values.

def DISAPPEARING_NUMBERS_correct():
    # Shows the player that they were correct. Also plays a special sound.
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 2)
    CORRECT_SFX.play()
    correctFont = pygame.font.Font(FONT_FILE, 100)
    displayCorrect = correctFont.render('Correct!', True, GREEN, None)
    displayCorrectRect = displayCorrect.get_rect()
    displayCorrectRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    GAME_WINDOW.fill(BG_COLOR)
    GAME_WINDOW.blit(displayCorrect, displayCorrectRect)
    transition(1, 0)


def DISAPPEARING_NUMBERS_wrong():
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 2)
    WRONG_SFX.play()
    # Shows the player that they were wrong.
    wrongFont = pygame.font.Font(FONT_FILE, 100)
    displayWrong = wrongFont.render('Wrong!', True, RED, None)
    displayWrongRect = displayWrong.get_rect()
    displayWrongRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    GAME_WINDOW.fill(BG_COLOR)
    GAME_WINDOW.blit(displayWrong, displayWrongRect)
    transition(1, 0)

def DISAPPEARING_NUMBERS_win():
    # Shows the player that they won and applies all the win rewards.
    global win_has_been_called
    win_has_been_called = True
    # Adds a little delay so that the sounds are evenly spaced out due to their lengths.
    transition(0, 1)
    pygame.mixer.Channel(4).pause()# Pause the background music as the Win SFX is playing.
    WIN_SFX.play()  # Plays the winning theme.
    transition(0, 0.2)
    winTextFont = pygame.font.Font(FONT_FILE, 100)
    winText = winTextFont.render('You won!', True, BLACK, None)
    winTextRect = winText.get_rect()
    winTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(winText, winTextRect)
    transition(3, 1)
    DISAPPEARING_NUMBERS_resetValues(chosen_number_list)
    winState() # Show the overall stats of the player before the next minigame.

def DISAPPEARING_NUMBERS_loss():
    # Show the player that they lost and applise all the loss rewards.
    global loss_has_been_called
    loss_has_been_called = True
    pygame.mixer.Channel(4).pause()# Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the winning theme.
    transition(0, 0.2)
    lossTextFont = pygame.font.Font(FONT_FILE, 100)
    lossText = lossTextFont.render('You lost!', True, BLACK, None)
    lossTextRect = lossText.get_rect()
    lossTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))
    GAME_WINDOW.blit(lossText, lossTextRect)
    transition(3, 1)
    DISAPPEARING_NUMBERS_resetValues(chosen_number_list)
    lossState()

def DISAPPEARING_NUMBERS_freeplay_win():
    # Same as the regular win but asks if the player wants to play again.
    global win_has_been_called
    win_has_been_called = True
    winning = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    
    WIN_SFX.play() # Plays the winning theme
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    transition(0, 0.2)
    COLORED_CIRCLES_resetValues(chosenColors)
    while winning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        winTextFont = pygame.font.Font(FONT_FILE, 100)
        winText = winTextFont.render('You won!', True, BLACK, None)
        winTextRect = winText.get_rect()
        winTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(winText, winTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def DISAPPEARING_NUMBERS_freeplay_loss():
    # Same as the regular loss but asks if the player wants to play again.
    global loss_has_been_called
    loss_has_been_called = True
    losing = True

    # Buttons
    retryButton = Button('Retry', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS)
    exitToMenuButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, freeplay)
    pygame.mixer.Channel(4).pause() # Pause the background music as the Win SFX is playing.
    LOSS_SFX.play()  # Plays the losing theme.
    transition(0, 0.2)
    COLORED_CIRCLES_resetValues(chosenColors)
    while losing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        lossTextFont = pygame.font.Font(FONT_FILE, 100)
        lossText = lossTextFont.render('You lost!', True, BLACK, None)
        lossTextRect = lossText.get_rect()
        lossTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        GAME_WINDOW.blit(lossText, lossTextRect)

        retryButton.draw()
        exitToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def DISAPPEARING_NUMBERS_showAnswers():
    # Shows the answers to the player in multiple choice format (A B C D)
    
    # Putting the chosen numbers in a new list to be randomized when displayed
    # Values to display the answers (which are 4 of the chosen numbers)
    # 'Which number was 1st on the left?'
    global eButton
    if chosenQuestion == QUESTIONS[0]:
        displayAnswerA = FONT.render(chosen_number_2, True, BLACK, None) 
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

        displayAnswerB = FONT.render(chosen_number_3, True, BLACK, None) 
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        displayAnswerC = FONT.render(chosen_number_1, True, BLACK, None) 
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        displayAnswerD = FONT.render(chosen_number_4, True, BLACK, None) 
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)

    # 'Which number was in the middle?'
    if chosenQuestion == QUESTIONS[1]:
        displayAnswerA = FONT.render(chosen_number_3, True, BLACK, None) 
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)


        displayAnswerB = FONT.render(chosen_number_1, True, BLACK, None) 
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        displayAnswerC = FONT.render(chosen_number_5, True, BLACK, None) 
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        displayAnswerD = FONT.render(chosen_number_2, True, BLACK, None) 
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
    
    # 'Which number was 1st on the right?'
    if chosenQuestion == QUESTIONS[2]:
        displayAnswerA = FONT.render(chosen_number_1, True, BLACK, None) 
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)


        displayAnswerB = FONT.render(chosen_number_5, True, BLACK, None) 
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        displayAnswerC = FONT.render(chosen_number_2, True, BLACK, None) 
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        displayAnswerD = FONT.render(chosen_number_4, True, BLACK, None) 
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
    
    # 'How many numbers were single-digit?'
    if chosenQuestion == QUESTIONS[3]:
        # Button is only created if this is the question. Otherwise, it doesn't exist
        #createButtons('E', (WINDOW_WIDTH // 2) - 100, 325, 25, 25, GREEN, DARK_GREEN, checkAnswersE)
        
        # Displaying the answers
        # Checking each chosen_number if they are single-digits
        displayAnswerA = FONT.render('1', True, BLACK, None) 
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)


        displayAnswerB = FONT.render('2', True, BLACK, None) 
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        displayAnswerC = FONT.render('3', True, BLACK, None) 
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        displayAnswerD = FONT.render('4', True, BLACK, None) 
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)

        displayAnswerE = FONT.render('5', True, BLACK, None) 
        displayAnswerERect = displayAnswerE.get_rect()
        displayAnswerERect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

        GAME_WINDOW.blit(displayAnswerE, displayAnswerERect) # only blitted if this question is asked
        # Calculating the answer
        for n in chosen_number_list:
            if n >= 10:
                chosen_number_list.remove(n)
    
    # 'How many numbers were double-digit?'
    if chosenQuestion == QUESTIONS[4]:
        # Button is only created if this is the question. Otherwise, it doesn't exist

        displayAnswerA = FONT.render('1', True, BLACK, None) 
        displayAnswerARect = displayAnswerA.get_rect()
        displayAnswerARect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)


        displayAnswerB = FONT.render('2', True, BLACK, None) 
        displayAnswerBRect = displayAnswerB.get_rect()
        displayAnswerBRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

        displayAnswerC = FONT.render('3', True, BLACK, None) 
        displayAnswerCRect = displayAnswerC.get_rect()
        displayAnswerCRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        displayAnswerD = FONT.render('4', True, BLACK, None) 
        displayAnswerDRect = displayAnswerD.get_rect()
        displayAnswerDRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)

        displayAnswerE = FONT.render('5', True, BLACK, None) 
        displayAnswerERect = displayAnswerE.get_rect()
        displayAnswerERect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
        
        GAME_WINDOW.blit(displayAnswerE, displayAnswerERect) # only blitted if this question is asked

        # Calculating the answer
        for n in chosen_number_list:
            if n < 10:
                chosen_number_list.remove(n)

    GAME_WINDOW.blit(displayAnswerA, displayAnswerARect)
    GAME_WINDOW.blit(displayAnswerB, displayAnswerBRect)
    GAME_WINDOW.blit(displayAnswerC, displayAnswerCRect)
    GAME_WINDOW.blit(displayAnswerD, displayAnswerDRect)

def DISAPPEARING_NUMBERS_checkAnswersA():
    # Checks the players answer for choice A if they were right or wrong
    # For duplicate/triplicate questions
    
    # If player answered A for 'Which number was 1st on the left?'
    if chosenQuestion == QUESTIONS[0]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered A for 'Which number was in the middle?'
    elif chosenQuestion == QUESTIONS[1]:
        DISAPPEARING_NUMBERS_correct()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_win()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_win()
    # If player answered A for 'Which number was 1st on the right?'
    elif chosenQuestion == QUESTIONS[2]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered A for 'How many numbers were single-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[3]: 
        if len(chosen_number_list) == 1:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered A for 'How many numbers were double-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[4]: 
        if len(chosen_number_list) == 1:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()

def DISAPPEARING_NUMBERS_checkAnswersB():
    # Checks the players answer for choice B if they were right or wrong
    # For duplicate/triplicate questions

    # If player answered B for 'Which number was 1st on the left?'
    if chosenQuestion == QUESTIONS[0]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered B for 'Which number was in the middle?'
    elif chosenQuestion == QUESTIONS[1]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered B for 'Which number was 1st on the right?'
    elif chosenQuestion == QUESTIONS[2]:
        DISAPPEARING_NUMBERS_correct()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_win()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_win()
    # If player answered B for 'How many numbers were single-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[3]: 
        if len(chosen_number_list) == 2:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered B for 'How many numbers were double-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[4]: 
        if len(chosen_number_list) == 2:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()


def DISAPPEARING_NUMBERS_checkAnswersC():
    # Checks the players answer for choice C if they were right or wrong
    # For duplicate/triplicate questions
    # If player answered C for 'Which number was 1st on the left?'
    if chosenQuestion == QUESTIONS[0]:
        DISAPPEARING_NUMBERS_correct()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_win()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_win()
    # If player answered C for 'Which number was in the middle?'
    elif chosenQuestion == QUESTIONS[1]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered C for 'Which number was 1st on the right?'
    elif chosenQuestion == QUESTIONS[2]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered C for 'How many numbers were single-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[3]: 
        if len(chosen_number_list) == 3:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered C for 'How many numbers were double-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[4]: 
        if len(chosen_number_list) == 3:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()


def DISAPPEARING_NUMBERS_checkAnswersD():
    # Checks the players answer for choice B if they were right or wrong
    # For duplicate/triplicate questions
    # If player answered D for 'Which number was 1st on the left?'
    if chosenQuestion == QUESTIONS[0]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered D for 'Which number was in the middle?'
    elif chosenQuestion == QUESTIONS[1]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered D for 'Which number was 1st on the right?'
    elif chosenQuestion == QUESTIONS[2]:
        DISAPPEARING_NUMBERS_wrong()
        if freeplay_mode == False:
            DISAPPEARING_NUMBERS_loss()
        elif freeplay_mode == True:
            DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered D for 'How many numbers were single-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[3]: 
        if len(chosen_number_list) == 4:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered D for 'How many numbers were double-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[4]: 
        if len(chosen_number_list) == 4:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()


def DISAPPEARING_NUMBERS_checkAnswersE():
    # Checks the players answer for choice E if they were right or wrong.
    # For duplicate/triplicate questions

    # If player answered E for 'How many numbers were single-digit?'
    ## WORKS AS INTENDED ##
    if chosenQuestion == QUESTIONS[3]: 
        if len(chosen_number_list) == 5:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()
    # If player answered E for 'How many numbers were double-digit?'
    ## WORKS AS INTENDED ##
    elif chosenQuestion == QUESTIONS[4]: 
        if len(chosen_number_list) == 5:
            DISAPPEARING_NUMBERS_correct()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_win()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_win()
        else:
            DISAPPEARING_NUMBERS_wrong()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()

def DISAPPEARING_NUMBERS_freeplay():
    # Screen shown to the player when they want to play Logic in Freeplay mode.
    pygame.mixer.Channel(4).unpause()# Unpause the background music
    GAME_WINDOW.fill(BG_COLOR)
    deciding = True
    # Button values
    playGameButton = Button('Yes', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS)
    returnToFreeplayButton = Button('No', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, EXIT_BUTTON_CLICK_SFX, freeplay)

    # Text display values
    titleFont = pygame.font.Font(FONT_FILE, 80)
    subtitleFont = pygame.font.Font(FONT_FILE, 65)
    titleText = titleFont.render('DISAPPEARING NUMBERS', True, BLACK, None)
    titleText_rect = titleText.get_rect()
    titleText_rect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

    subtitleText = subtitleFont.render('Play?', True, BLACK, None)
    subtitleText_rect = subtitleText.get_rect()
    subtitleText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2))

    while deciding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        GAME_WINDOW.blit(titleText, titleText_rect)
        GAME_WINDOW.blit(subtitleText, subtitleText_rect)
        playGameButton.draw()
        returnToFreeplayButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def DISAPPEARING_NUMBERS():
    playing = True # True = game is not done. False = game is done.
    # Variables area

    
    cycle_through_numbers(30)
    GAME_WINDOW.fill(BG_COLOR)
    QuestionFont = pygame.font.Font(FONT_FILE, 48)
    show_chosen_numbers()
    showRandomQuestion(QUESTIONS)
    aButton = Button('A', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                         2) - 105), 4, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS_checkAnswersA)
    bButton = Button('B', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                        2) - 55), 4, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS_checkAnswersB)
    cButton = Button('C', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                        2) - 5), 4, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS_checkAnswersC)
    dButton = Button('D', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT //
                        2) + 45), 4, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS_checkAnswersD)
    eButton = Button('E', 30, 30, ((WINDOW_WIDTH // 2) - 100, (WINDOW_HEIGHT // 
                        2) + 95), 6, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS_checkAnswersE)
    start_ticks = pygame.time.get_ticks()

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()
        GAME_WINDOW.fill(BG_COLOR)
        seconds = 3 - (int((pygame.time.get_ticks() - start_ticks)/1000)) # If I were to add "scaling" difficulty, I should probably make the easiest be 5 sec, then 4 sec for medium, then 3 sec for hard.
        displayCountdown = TIMER_FONT.render(str(seconds), True, BLACK, None)
        displayCountdownRect = displayCountdown.get_rect()
        displayCountdownRect.center = (WINDOW_WIDTH // 2, 100)

        displayQuestion = QuestionFont.render(
            chosenQuestion, True, BLACK, None)
        displayQuestionRect = displayQuestion.get_rect()

        displayQuestionRect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 175)
        #GAME_WINDOW.blit(displayInstructions2, displayInstructions2_Rect)
        if seconds > -1:
            GAME_WINDOW.blit(displayCountdown, displayCountdownRect)
            GAME_WINDOW.blit(displayQuestion, displayQuestionRect)
            DISAPPEARING_NUMBERS_showAnswers()

            if chosenQuestion == QUESTIONS[3] or chosenQuestion == QUESTIONS[4]:
                aButton.draw()
                bButton.draw()
                cButton.draw()
                dButton.draw()
                eButton.draw()
            else:
                aButton.draw()
                bButton.draw()
                cButton.draw()
                dButton.draw()
        # Draws the surface object to the screen
        elif seconds == -1:
            timeUp()
            if freeplay_mode == False:
                DISAPPEARING_NUMBERS_loss()
            elif freeplay_mode == True:
                DISAPPEARING_NUMBERS_freeplay_loss()

        pygame.display.update() ## DO NOT ERASE
        FPSCLOCK.tick(FPS) ## DO NOT ERASE

# ~~~~~~~~~~~~~~~~~~~~~ #
#  ESSENTIAL FUNCTIONS  #
# ~~~~~~~~~~~~~~~~~~~~~ #


# Timer lengths are milliseconds, hence the multiplication by 1000
def transition(first_timer_length, second_timer_length):
    # Transitions to the next part of the program
    pygame.display.update()  # Updates the current display to what was last blitted
    # How long the current display will last
    pygame.time.delay(int(first_timer_length) * 1000)
    GAME_WINDOW.fill(BG_COLOR)
    # Updates the current display to a blank display (because of the previous line)
    pygame.display.update()
    # How long the blank display will last
    pygame.time.delay(int(second_timer_length) * 1000)

# This function serves as a "base" for the instructions for future games.
# def instructions():
#     # Shows the player what they need to do to win the Logic minigame
#     GAME_WINDOW.fill(BG_COLOR)
#     instructing = True
#     showingThreeInstructions = True

#     # Values to display the 3 instructions
#     instruction_font = pygame.font.Font(FONT_FILE, 50) # Font style
#     ready_font = pygame.font.Font(FONT_FILE, 80)
#     first_instruction_text = instruction_font.render('Solve the problem that is shown.', True, BLACK, None)
#     first_instruction_text_rect = first_instruction_text.get_rect()

#     second_instruction_text = instruction_font.render('Solving 2 problems is a win.', True, BLACK, None)
#     second_instruction_text_rect = second_instruction_text.get_rect()

#     third_instruction_text = instruction_font.render('Failing to solve 2 problems is a loss.', True, BLACK, None)
#     third_instruction_text_rect = third_instruction_text.get_rect()

#     ready_instruction_text = ready_font.render('Ready?', True, BLACK, None)
#     ready_instruction_text_rect = ready_instruction_text.get_rect()

#     readyButton = Button('I\'m ready!', 300, 60, ((WINDOW_WIDTH // 2) - 150, (WINDOW_HEIGHT // 2) + 200), 6, BUTTON_CLICK_SFX, LOGIC)
#     while instructing:

#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     playing = False
#                     pygame.quit()
#                     sys.exit()
#         if showingThreeInstructions: # Plays the instruction "animation."
#             first_instruction_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
#             GAME_WINDOW.blit(first_instruction_text, first_instruction_text_rect)
#             pygame.display.update()
#             transition (1, 0.2)

#             first_instruction_text_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100) # Move the 1st instructions a little higher when the 2nd set shows up.

#             second_instruction_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
#             GAME_WINDOW.blit(first_instruction_text, first_instruction_text_rect)
#             GAME_WINDOW.blit(second_instruction_text, second_instruction_text_rect)
#             pygame.display.update()
#             transition (1, 0.2)
#             ## FOCUS HERE NEXT TIME (3 PM, 11/17/22)

#             first_instruction_text_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200) # Move the 1st instructions a little higher when the 2nd set shows up.
#             second_instruction_text_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100) # Move the 2nd instructions a little higher when the 3rd set shows up.
#             third_instruction_text_rect = third_instruction_text.get_rect()
#             third_instruction_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
#             GAME_WINDOW.blit(first_instruction_text, first_instruction_text_rect)
#             GAME_WINDOW.blit(second_instruction_text, second_instruction_text_rect)
#             GAME_WINDOW.blit(third_instruction_text, third_instruction_text_rect)

#             transition (1, 0.2)
#             showingThreeInstructions = False # Done showing the 3 instructions.

#         elif not showingThreeInstructions: # Draws the button alongside the current state of the instructions.
#             first_instruction_text_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 200) # Move the 1st instructions a little higher when the 2nd set shows up.
#             second_instruction_text_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100) # Move the 2nd instructions a little higher when the 3rd set shows up.
#             third_instruction_text = instruction_font.render('Failing to solve 2 problems is a loss.', True, BLACK, None)
#             third_instruction_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
#             ready_instruction_text_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
#             GAME_WINDOW.blit(first_instruction_text, first_instruction_text_rect)
#             GAME_WINDOW.blit(second_instruction_text, second_instruction_text_rect)
#             GAME_WINDOW.blit(third_instruction_text, third_instruction_text_rect)
#             GAME_WINDOW.blit(ready_instruction_text, ready_instruction_text_rect)

#         readyButton.draw()
#         pygame.display.update()
#         FPSCLOCK.tick(FPS)
#     GAME_WINDOW.fill(BG_COLOR)
#     return


def audio_volumeDown():
    # Decreases the volume of in-game audio by 0.1 and also displays it to the player.
    global game_audio_lvl
    for x in AUDIO_LIST:
        # print(str(x.get_volume()))
        if x.get_volume() > 0:
            x.set_volume(round(x.get_volume() - 0.1, 1))
        print(str(x.get_volume()))

    if game_audio_lvl > 0:
        game_audio_lvl = round(game_audio_lvl - 0.1, 1)
    elif game_audio_lvl == 0:
        game_audio_lvl = 0
    print(game_audio_lvl)


def audio_volumeUp():
    # Increases the volume of in-game audio by 0.1.
    global game_audio_lvl
    for x in AUDIO_LIST:
        x.set_volume(round(x.get_volume() + 0.1, 1))
        print(str(x.get_volume()))

    if game_audio_lvl < 1:
        game_audio_lvl = round(game_audio_lvl + 0.1, 1)
    elif game_audio_lvl == 1:
        game_audio_lvl = 1
    print(game_audio_lvl)


def music_volumeDown():
    # Decreases the volume of music by 0.1 until it is mute.
    global music_lvl
    for x in MUSIC_LIST:
        if x.get_volume() > 0:
            x.set_volume(round(x.get_volume() - 0.1, 1))
        print(str(x.get_volume()))

    if music_lvl > 0:
        music_lvl = round(music_lvl - 0.1, 1)
    elif music_lvl == 0:
        music_lvl = 0
    print(music_lvl)


def music_volumeUp():
    # Increases the volume of a music by 0.1.
    global music_lvl
    for x in MUSIC_LIST:
        print(str(x.get_volume()))
        x.set_volume(round(x.get_volume() + 0.1, 1))

    if music_lvl < 1:
        music_lvl = round(music_lvl + 0.1, 1)
    elif music_lvl == 1:
        music_lvl = 1
    print(music_lvl)


def exitGame():
    GAME_WINDOW.fill(BG_COLOR)
    goodbye = 'See ya!'  # change this to the name of the game itself later on
    goodbyeFont = pygame.font.Font(FONT_FILE, 65)
    goodbyeTextSurf, goodbyeTextRect = createTextBoxes(goodbye, goodbyeFont)
    goodbyeTextRect.center = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2))
    GAME_WINDOW.blit(goodbyeTextSurf, goodbyeTextRect)
    transition(1, 0)
    pygame.quit()
    sys.exit()


def createTextBoxes(text, font):
    # Creates a text box using two parameters: text (the string of text) and font (font style and
    # font size based on pygame.font.Font())
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def play_showInstructions():
    # Shows the player what to do in the gamemode before they start playing.
    # Instructions:
    # -- You will play a random set of 3 minigames.
    # -- You have 3 lives. (maybe show as animated hearts?)
    # -- Win: you keep a life. Lose: you lose a life.
    # -- Difficulty increases as you get closer to the end.
    # -- Win by staying alive for 10 rounds!
    GAME_WINDOW.fill(BG_COLOR)
    instructing = True
    showingInstructions = True

    # Instantiating the HP class for the Hearts
    sprites = pygame.sprite.Group()
    hearts_1 = Hp(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
    hearts_2 = Hp((WINDOW_WIDTH // 2) - 60, (WINDOW_HEIGHT // 2) + 50)
    hearts_3 = Hp((WINDOW_WIDTH // 2) + 60, (WINDOW_HEIGHT // 2) + 50)

    moving_hearts_1 = FullHp(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50)
    moving_hearts_2 = FullHp((WINDOW_WIDTH // 2) - 60, (WINDOW_HEIGHT // 2) + 50)
    moving_hearts_3 = FullHp((WINDOW_WIDTH // 2) + 60, (WINDOW_HEIGHT // 2) + 50)

    sprites.add(moving_hearts_1)
    sprites.add(moving_hearts_2)
    sprites.add(moving_hearts_3)

    

    # Values to display "How to Play" on the top-left
    title = 'How to Play'
    titleFont = pygame.font.Font(FONT_FILE, 80)
    titleTextSurf, titleTextRect = createTextBoxes(title, titleFont)
    titleTextRect.center = (275, 50)  # Positioned at the top-left for now

    # Values to display the 3 instructions
    instruction_font = pygame.font.Font(FONT_FILE, 50)  # Font style
    ready_font = pygame.font.Font(FONT_FILE, 80)
    first_instruction_text = instruction_font.render(
        'You will play a random set of 3 minigames.', True, BLACK, None)
    first_instruction_text_rect = first_instruction_text.get_rect()

    # Thinking of adding a sprite animation of hearts below this to show what the HP looks like.
    second_instruction_text = instruction_font.render(
        'You have 3 lives.', True, BLACK, None)
    second_instruction_text_rect = second_instruction_text.get_rect()

    third_instruction_text = instruction_font.render(
        'Win: you keep a life.', True, BLACK, None)
    third_instruction_text_rect = third_instruction_text.get_rect()

    fourth_instruction_text = instruction_font.render(
        'Lose: you lose a life.', True, BLACK, None)
    fourth_instruction_text_rect = fourth_instruction_text.get_rect()

    fifth_instruction_text = instruction_font.render(
        'Win by staying alive for 10 rounds!', True, BLACK, None)
    fifth_instruction_text_rect = fifth_instruction_text.get_rect()

    ready_instruction_text = ready_font.render('Ready?', True, BLACK, None)
    ready_instruction_text_rect = ready_instruction_text.get_rect()

    readyButton = Button('I\'m ready!', 200, 60, ((WINDOW_WIDTH // 2) - 225,
                         (WINDOW_HEIGHT // 2) + 50), 6, BUTTON_CLICK_SFX, check_first_play)
    play_nopeButton = Button('Nope!', 200, 60, ((
        WINDOW_WIDTH // 2) + 25, (WINDOW_HEIGHT // 2) + 50), 6, BUTTON_CLICK_SFX, startMenu)
    repeat_Button = Button('Come again?', 220, 60, ((WINDOW_WIDTH // 2) - 110,
                           (WINDOW_HEIGHT // 2) + 150), 6, BUTTON_CLICK_SFX, play_showInstructions)

    instructing_ticks = pygame.time.get_ticks()
    while instructing and first_play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        if showingInstructions:  # Plays the instruction "animation."
            # "How to Play" is displayed on the top-left.
            GAME_WINDOW.blit(titleTextSurf, titleTextRect)
            first_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(first_instruction_text,
                             first_instruction_text_rect)
            transition(2, 0)

            # Ensures that only the next instruction will be shown.
            GAME_WINDOW.fill(BG_COLOR)
            # "How to Play" is displayed on the top-left.
            GAME_WINDOW.blit(titleTextSurf, titleTextRect)
            second_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 20)
            sprites.draw(GAME_WINDOW)
            GAME_WINDOW.blit(second_instruction_text,
                             second_instruction_text_rect)

            transition(2, 0)
            showing3rd = True
            instructing_ticks = pygame.time.get_ticks()
            while showing3rd:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        showing3rd = False
                        instructing = False
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pass
                countdown = 2 - \
                    (int((pygame.time.get_ticks() - instructing_ticks)/1000))
                if countdown == -1:
                    showing3rd = False  # break out of loop
                elif countdown > -1:
                    # Ensures that only the next instruction will be shown.
                    GAME_WINDOW.fill(BG_COLOR)
                    # "How to Play" is displayed on the top-left.
                    GAME_WINDOW.blit(titleTextSurf, titleTextRect)
                    third_instruction_text_rect.center = (
                        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 20)
                    GAME_WINDOW.blit(third_instruction_text,
                                    third_instruction_text_rect)
                    sprites.draw(GAME_WINDOW)
                    sprites.update(0.2)  # How fast the sprites animation is

                    moving_hearts_1.animate()
                    moving_hearts_2.animate()
                    moving_hearts_3.animate()
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

            showing4th = True
            instructing_ticks = pygame.time.get_ticks()
            while showing4th:
                # Amount of seconds for the countdown is 2 * the # of the instruction being shown (ex. 2 * 4 for the 4th instruction)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        showing4th = False
                        instructing = False
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pass
                countdown = 2 - \
                    (int((pygame.time.get_ticks() - instructing_ticks)/1000))
                if countdown == -1:
                    showing4th = False  # break out of loop
                elif countdown > -1:
                    # Ensures that only the next instruction will be shown.
                    GAME_WINDOW.fill(BG_COLOR)
                    # "How to Play" is displayed on the top-left.
                    GAME_WINDOW.blit(titleTextSurf, titleTextRect)
                    fourth_instruction_text_rect.center = (
                        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 20)
                    GAME_WINDOW.blit(fourth_instruction_text,
                                     fourth_instruction_text_rect)
                    # Replace the current sprites with different ones.
                    sprites.remove(moving_hearts_1)
                    sprites.remove(moving_hearts_2)
                    sprites.remove(moving_hearts_3)

                    sprites.add(hearts_1)
                    sprites.add(hearts_2)
                    sprites.add(hearts_3)
                    sprites.draw(GAME_WINDOW)

                    sprites.update(0.2)  # How fast the sprites animation is

                    hearts_3.animate()
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

            # Ensures that only the next instruction will be shown.
            GAME_WINDOW.fill(BG_COLOR)
            # "How to Play" is displayed on the top-left.
            GAME_WINDOW.blit(titleTextSurf, titleTextRect)
            fifth_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 20)
            GAME_WINDOW.blit(fifth_instruction_text,
                             fifth_instruction_text_rect)

            transition(2, 0)
            # Ensures that only the next instruction will be shown.
            GAME_WINDOW.fill(BG_COLOR)
            # "How to Play" is displayed on the top-left.
            GAME_WINDOW.blit(titleTextSurf, titleTextRect)
            ready_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(ready_instruction_text,
                             ready_instruction_text_rect)
            transition(1, 0)

            showingInstructions = False  # Done showing the 3 instructions.

        # Draws the button alongside the current state of the instructions.
        elif not showingInstructions:
            # "How to Play" is displayed on the top-left.
            GAME_WINDOW.blit(titleTextSurf, titleTextRect)
            ready_instruction_text_rect.center = (
                WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(ready_instruction_text,
                             ready_instruction_text_rect)

        # Show the buttons
        readyButton.draw()
        play_nopeButton.draw()
        repeat_Button.draw()
        # Animate the hearts
        hearts_1.animate()
        hearts_2.animate()
        hearts_3.animate()

        sprites.update(0.2)  # How fast the sprites animation is
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    GAME_WINDOW.fill(BG_COLOR)
    play()


def pickMinigame():
    # Puts all the available minigames into a list, picks a random one, and plays it.
    global minigame_count
    minigame_count = minigame_count + 1
    playing = True
    # Took out WORD_TYPE() until I fix the 'Time's up' at the beginning of each play after the 1st
    MINIGAMES = [COLORED_CIRCLES, LOGIC, BUTTON_MASH, DISAPPEARING_NUMBERS, WORD_TYPE]
    while playing:
        selected_minigame = getRandom(MINIGAMES)
        selected_minigame()


def winState():
    # After winning a minigame, the player's HP doesn't go down. ## (EVENTUALLY) If they win 3 in a row, their life is added by 1.
    global hp, minigame_count, win_has_been_called, loss_has_been_called
    # Resets the check for win variable. Ensures that the next outcome is always different
    pygame.mixer.Channel(4).unpause()# Unpause the background music
    win_has_been_called = False
    titleFont = pygame.font.Font(FONT_FILE, 80)
    subtitleFont = pygame.font.Font(FONT_FILE, 50)
    congratulateText = titleFont.render('Keep it up!', True, BLACK, None)
    congratulateText_rect = congratulateText.get_rect()
    congratulateText_rect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

    fulllifeText = subtitleFont.render('HP is at max!', True, BLACK, None)
    fulllifeText_rect = fulllifeText.get_rect()
    fulllifeText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 60)

    twolifeText = subtitleFont.render('HP is at 2/3!', True, BLACK, None)
    twolifeText_rect = twolifeText.get_rect()
    twolifeText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 60)

    onelifeText = subtitleFont.render('Danger! HP is at 1!', True, BLACK, None)
    onelifeText_rect = onelifeText.get_rect()
    onelifeText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 60)

    winState_sprites = pygame.sprite.Group()

    # Sprites for full hearts
    full_life_middle = FullHp(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    full_life_left = FullHp((WINDOW_WIDTH // 2) - 60, WINDOW_HEIGHT // 2)
    full_life_right = FullHp((WINDOW_WIDTH // 2) + 60, WINDOW_HEIGHT // 2)

    # Static images for empty hearts (since it won't be animated here)
    # All display values for the middle empty heart
    empty_life_middle = pygame.image.load(resource_path('Sprites/Hearts/Empty.png'))
    empty_life_middle = pygame.transform.scale(empty_life_middle, (W_HEARTS * 3, H_HEARTS * 3))
    empty_life_middle_rect = empty_life_middle.get_rect()
    empty_life_middle_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    # All display values for the left empty heart
    empty_life_left = pygame.image.load(resource_path('Sprites/Hearts/Empty.png'))
    empty_life_left = pygame.transform.scale(empty_life_left, (W_HEARTS * 3, H_HEARTS * 3))
    empty_life_left_rect = empty_life_left.get_rect()
    empty_life_left_rect.center = ((WINDOW_WIDTH // 2) - 60, WINDOW_HEIGHT // 2)


    # All display values for the right empty heart
    empty_life_right = pygame.image.load(resource_path('Sprites/Hearts/Empty.png'))
    empty_life_right = pygame.transform.scale(empty_life_right, (W_HEARTS * 3, H_HEARTS * 3))
    empty_life_right_rect = empty_life_right.get_rect()
    empty_life_right_rect.center = ((WINDOW_WIDTH // 2) + 60, WINDOW_HEIGHT // 2)

    winState_sprites.add(full_life_middle)
    winState_sprites.add(full_life_left)
    winState_sprites.add(full_life_right)

    showingResults = True
    results_ticks = pygame.time.get_ticks()
    while showingResults:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        if minigame_count < WIN_CONDITION:
            countdown = 2 - (int((pygame.time.get_ticks() - results_ticks)/1000))
            if countdown > 0:
                GAME_WINDOW.fill(BG_COLOR)
                GAME_WINDOW.blit(congratulateText, congratulateText_rect)
                
            elif countdown == 0:
                break
        elif minigame_count == WIN_CONDITION:
            ultimate_win()

        if hp == 3: # HP is full, draw full hearts & message.
            GAME_WINDOW.blit(fulllifeText, fulllifeText_rect)
            full_life_middle.animate()
            full_life_left.animate()
            full_life_right.animate()
        elif hp == 2: # HP is 2 full, 1 empty, draw 2 full hearts & 1 empty heart & the message.
            # Remove the right heart from the sprites list.
            GAME_WINDOW.blit(twolifeText, twolifeText_rect)
            
            winState_sprites.remove(full_life_right)
            
            full_life_middle.animate()
            full_life_left.animate()
            GAME_WINDOW.blit(empty_life_right, empty_life_right_rect)
        elif hp == 1: # HP is 1 full, 2 empty. Draw 1 full heart & 2 empty hearts & the message.
            GAME_WINDOW.blit(onelifeText, onelifeText_rect)
            # Remove the right and left heart from the sprites list.
            winState_sprites.remove(full_life_right)
            winState_sprites.remove(full_life_middle)
            
            GAME_WINDOW.blit(empty_life_middle, empty_life_middle_rect)
            full_life_left.animate()
            GAME_WINDOW.blit(empty_life_right, empty_life_right_rect)

        winState_sprites.draw(GAME_WINDOW)
        winState_sprites.update(0.2)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    play()


def lossState():
    # After losing a minigame, the player's HP is decreased by 1. If they lose all their lives, it is game over.
    # After winning a minigame, the player's HP doesn't go down. If they win 3 in a row, their life is added by 1.
    global hp, minigame_count, loss_has_been_called
    # Resets the check for loss variable. Ensures that the next outcome is always different
    hp -= 1 # Iterate the hp change here.
    pygame.mixer.Channel(4).unpause()# Unpause the background music
    loss_has_been_called = False
    titleFont = pygame.font.Font(FONT_FILE, 80)
    subtitleFont = pygame.font.Font(FONT_FILE, 50)
    congratulateText = titleFont.render('Get the next one!', True, BLACK, None)
    congratulateText_rect = congratulateText.get_rect()
    congratulateText_rect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

    decreaseText = subtitleFont.render('HP decreased by 1', True, BLACK, None)
    decreaseText_rect = decreaseText.get_rect()
    decreaseText_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 60)

    

    # Sprites for full hearts
    full_life_middle = FullHp(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    full_life_left = FullHp((WINDOW_WIDTH // 2) - 60, WINDOW_HEIGHT // 2)

    # Sprites for losing hearts
    losing_life_middle = Hp(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    losing_life_left = Hp((WINDOW_WIDTH // 2) - 60, WINDOW_HEIGHT // 2)
    losing_life_right = Hp((WINDOW_WIDTH // 2) + 60, WINDOW_HEIGHT // 2)

    # Creating the sprite group and adding the hearts to be shown
    lossState_sprites = pygame.sprite.Group()
    lossState_sprites.add(full_life_left)  # Left heart
    lossState_sprites.add(full_life_middle)  # Middle heart
    lossState_sprites.add(losing_life_right)  # Right heart

    # Static images for empty hearts (since it won't be animated here)
    # All display values for the middle empty heart
    empty_life_middle = pygame.image.load(resource_path('Sprites/Hearts/Empty.png'))
    empty_life_middle = pygame.transform.scale(empty_life_middle, (W_HEARTS * 3, H_HEARTS * 3))
    empty_life_middle_rect = empty_life_middle.get_rect()
    empty_life_middle_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    # All display values for the left empty heart
    empty_life_left = pygame.image.load(resource_path('Sprites/Hearts/Empty.png'))
    empty_life_left = pygame.transform.scale(empty_life_left, (W_HEARTS * 3, H_HEARTS * 3))
    empty_life_left_rect = empty_life_left.get_rect()
    empty_life_left_rect.center = ((WINDOW_WIDTH // 2) - 60, WINDOW_HEIGHT // 2)

    # All display values for the right empty heart
    empty_life_right = pygame.image.load(resource_path('Sprites/Hearts/Empty.png'))
    empty_life_right = pygame.transform.scale(empty_life_right, (W_HEARTS * 3, H_HEARTS * 3))
    empty_life_right_rect = empty_life_right.get_rect()
    empty_life_right_rect.center = ((WINDOW_WIDTH // 2) + 60, WINDOW_HEIGHT // 2)

    showingResults = True
    results_ticks = pygame.time.get_ticks()
    while showingResults:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        if minigame_count < WIN_CONDITION:
            countdown = 2 - (int((pygame.time.get_ticks() - results_ticks)/1000))
            if countdown > 0:
                GAME_WINDOW.fill(BG_COLOR)
                GAME_WINDOW.blit(congratulateText, congratulateText_rect)
                GAME_WINDOW.blit(decreaseText, decreaseText_rect)
            elif countdown == 0:
                break
        elif minigame_count == WIN_CONDITION:
            startMenu()
        if hp == 2: # Lost 1 HP, draw 2 full hearts and 1 empty heart & message.
            full_life_middle.animate()
            full_life_left.animate()
            losing_life_right.animate()
        elif hp == 1: # Lost 1 HP, draw 1 full heart and 2 empty hearts & message.
            # Remove the right heart from the sprites list.
            lossState_sprites.remove(losing_life_right)
            lossState_sprites.remove(full_life_middle)
            
            # Add the middle heart being emptied.
            lossState_sprites.add(losing_life_middle)

            losing_life_middle.animate()
            full_life_left.animate()
            GAME_WINDOW.blit(empty_life_right, empty_life_right_rect)
        elif hp == 0: # Lost all 3 hp, draw 2 empty hearts and the left one being emptied.
            lossState_sprites.remove(losing_life_right)
            lossState_sprites.remove(full_life_middle)

            lossState_sprites.add(losing_life_left)

            losing_life_left.animate()
            
            GAME_WINDOW.blit(empty_life_middle, empty_life_middle_rect)
            GAME_WINDOW.blit(empty_life_right, empty_life_right_rect)
        lossState_sprites.draw(GAME_WINDOW)
        lossState_sprites.update(0.2)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    play()


def ultimate_win():
    # Shows the player that they won the main gamemode and asks them if they want to play again or not.
    # Maybe show how many games they won/lost?
    ultimate_resetValues()
    pygame.mixer.Channel(4).pause()# Pause the background music as the Ultimate Win SFX is playing.
    ULTIMATE_WIN_SFX.play()
    GAME_WINDOW.fill(BG_COLOR)
    congratulating = True 
    doing_short_animation = True
    # Button values
    retryButton = Button('Yes', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, play)
    returnToMenuButton = Button('No', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, startMenu)
    # Text display values
    
    ultimate_titleFont = pygame.font.Font(FONT_FILE, 80)
    ultimate_subtitleFont = pygame.font.Font(FONT_FILE, 50)
    askPlayFont = pygame.font.Font(FONT_FILE, 100)

    ultimate_congratulateText = ultimate_titleFont.render('CONGRATS!', True, BLACK, None)
    ultimate_congratulateText_rect = ultimate_congratulateText.get_rect()
    

    youWon = ultimate_subtitleFont.render('You won the game!', True, BLACK, None)
    youWon_rect = youWon.get_rect()
    

    askPlay = askPlayFont.render('Play again?', True, BLACK, None)
    askPlay_rect = askPlay.get_rect()
    askPlay_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    while congratulating:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        if doing_short_animation: # Plays a small animation for congratulating the player.
            ultimate_congratulateText_rect.center = ( # Positions the 'Congrats!' on the middle
        WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(ultimate_congratulateText, ultimate_congratulateText_rect)
            transition(2,0)

            GAME_WINDOW.fill(BG_COLOR)
            youWon_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(youWon, youWon_rect)
            transition(2,0)

            GAME_WINDOW.fill(BG_COLOR)
            askPlay_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(askPlay,askPlay_rect)
            transition(1,0)

            doing_short_animation = False
        elif not doing_short_animation:
            GAME_WINDOW.blit(askPlay,askPlay_rect)

        retryButton.draw()
        returnToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS) # Resets all the values throughout the game that were used.
    

def ultimate_loss():
    # Shows the player that they lost the main gamemode and asks them if they want to play again or not.
    # Maybe show how many games they won/lost?
    ultimate_resetValues()
    pygame.mixer.Channel(4).pause()# Pause the background music as the Ultimate Loss SFX is playing.
    ULTIMATE_LOSS_SFX.play()
    GAME_WINDOW.fill(BG_COLOR)
    congratulating = True 
    doing_short_animation = True
    # Button values
    retryButton = Button('Yes', 300, 60, ((WINDOW_WIDTH // 2) - 350, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, play)
    returnToMenuButton = Button('No', 300, 60, ((WINDOW_WIDTH // 2) + 50, (WINDOW_HEIGHT // 2) + 100), 6, BUTTON_CLICK_SFX, startMenu)
    # Text display values
    
    ultimate_titleFont = pygame.font.Font(FONT_FILE, 80)
    ultimate_subtitleFont = pygame.font.Font(FONT_FILE, 50)
    askPlayFont = pygame.font.Font(FONT_FILE, 100)

    ultimate_uDeadText = ultimate_titleFont.render('You died!', True, BLACK, None)
    ultimate_uDeadText_rect = ultimate_uDeadText.get_rect()
    

    youWon = ultimate_subtitleFont.render('Better luck next time!', True, BLACK, None)
    youWon_rect = youWon.get_rect()
    

    askPlay = askPlayFont.render('Play again?', True, BLACK, None)
    askPlay_rect = askPlay.get_rect()
    askPlay_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)

    while congratulating:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        if doing_short_animation: # Plays a small animation for congratulating the player.
            ultimate_uDeadText_rect.center = ( # Positions the 'Congrats!' on the middle
        WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(ultimate_uDeadText, ultimate_uDeadText_rect)
            transition(2,0)

            GAME_WINDOW.fill(BG_COLOR)
            youWon_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(youWon, youWon_rect)
            transition(2,0)

            GAME_WINDOW.fill(BG_COLOR)
            askPlay_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            GAME_WINDOW.blit(askPlay,askPlay_rect)
            transition(1,0)

            doing_short_animation = False
        elif not doing_short_animation:
            GAME_WINDOW.blit(askPlay,askPlay_rect)

        retryButton.draw()
        returnToMenuButton.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS) # Resets all the values throughout the game that were used.

def ultimate_resetValues():
    global win_count, minigame_count, loss_count, hp
    # Calls all the reset functions from the games and also resets essential variables in the game.
    LOGIC_resetValues()
    WORD_TYPE_resetValues()
    COLORED_CIRCLES_resetValues(chosenColors)
    BUTTON_MASH_resetValues()
    DISAPPEARING_NUMBERS_resetValues(chosen_number_list)
    
    win_count = 0
    minigame_count = 0
    loss_count = 0
    hp = 3

    print('Values were all reset!')

def startMenu():
    # Displays a menu where the player selects from 4 Options: Play, Freeplay, Options, and Exit.
    # (should be called before the main() function)
    # READY
    
    # Reset the freeplay_mode value to its original state.
    global freeplay_mode
    freeplay_mode = False

    pygame.display.set_caption('MiniWare')
    # Starts the backgroun music if it hasn't yet.
    global sound_effectButton, returnButton
    if pygame.mixer.Channel(4).get_busy() == False:
        # Plays the background music on a separate channel from the other sounds.
        pygame.mixer.Channel(4).play(MENU_MUSIC, -1)
    # Unpauses the background music if it's been paused.
    elif pygame.mixer.Channel(4).get_busy() == True:
        pygame.mixer.Channel(4).unpause()
    inMenu = True  # boolean variable for the while loop.
    # Eventually make the coordinate/box values constants
    playButton = Button('Play', 300, 60, ((WINDOW_WIDTH // 2) -
                        150, (WINDOW_HEIGHT // 5) + 100), 6, BUTTON_CLICK_SFX, play)
    freeplayButton = Button('Freeplay', 300, 60, ((WINDOW_WIDTH // 2) - 150,
                            (WINDOW_HEIGHT // 5) + 200), 6, FREEPLAY_BUTTON_CLICK_SFX, freeplay)
    optionsButton = Button('Options', 300, 60, ((WINDOW_WIDTH // 2) - 150,
                           (WINDOW_HEIGHT // 5) + 300), 6, OPTIONS_BUTTON_CLICK_SFX, options)
    exitButton = Button('Exit', 300, 60, ((WINDOW_WIDTH // 2) - 150,
                        (WINDOW_HEIGHT // 5) + 400), 6, EXIT_BUTTON_CLICK_SFX, exit)
    returnButton = Button('Back', 200, 40, (50, 650), 6,
                          EXIT_BUTTON_CLICK_SFX, startMenu)
    sound_effectButton = HiddenButton('?', 100, 50, (
        (WINDOW_WIDTH) - 120, (WINDOW_HEIGHT // 5) + 500), 6, BUTTON_CLICK_SFX, playRandomSound)

    while inMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONUP:
            #     gameRandomizer()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        GAME_WINDOW.fill(WHITE)
        title = 'MiniWare'  # change this to the name of the game itself later on
        subtitle = 'a WarioWare inspired Game'

        titleFont = pygame.font.Font(FONT_FILE, 65)
        subtitleFont = pygame.font.Font(FONT_FILE, 35)
        subtitleTextSurf = subtitleFont.render(subtitle, True, RED, None)
        subtitleTextRect = subtitleTextSurf.get_rect()
        titleTextSurf, titleTextRect = createTextBoxes(title, titleFont)
        titleTextRect.center = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/5))
        subtitleTextRect.center = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/4))

        GAME_WINDOW.blit(subtitleTextSurf, subtitleTextRect)
        GAME_WINDOW.blit(titleTextSurf, titleTextRect)

        # Creates the 4 Main Menu options: Play, Freeplay, Options, and Exit.
        # createButtons("PLAY", PLAY_STARTINGPOSX, PLAY_STARTINGPOSY, MENUBUTTON_WIDTH, MENUBUTTON_HEIGHT, GREEN, DARK_GREEN, main) # starts the game by picking random minigames and giving the player a life of 3.
        # createButtons("FREEPLAY", FREEPLAY_STARTINGPOSX, FREEPLAY_STARTINGPOSY, MENUBUTTON_WIDTH, MENUBUTTON_HEIGHT, ORANGE, DARK_ORANGE, freeplay)
        # createButtons("OPTIONS", OPTIONS_STARTINGPOSX, OPTIONS_STARTINGPOSY, MENUBUTTON_WIDTH, MENUBUTTON_HEIGHT, GRAY, DARK_GRAY, options)
        # createButtons("EXIT", EXIT_STARTINGPOSX, EXIT_STARTINGPOSY, MENUBUTTON_WIDTH, MENUBUTTON_HEIGHT, RED, DARK_RED, exitGame)

        playButton.draw()
        freeplayButton.draw()
        optionsButton.draw()
        exitButton.draw()
        sound_effectButton.draw()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def intro():
    # Plays an intro animation before the start menu shows up.

    inIntro = True  # for readability purposes, same as while True
    # Number of seconds of how long the intro will last
    intro_ticks = pygame.time.get_ticks()

    # Display "A game made by andy" in the middle of the GAME_WINDOW
    # change this to the name of the game itself later on
    introText = 'A Game Made By andy'
    introFont = pygame.font.Font(FONT_FILE, 65)
    introTextSurf, introTextRect = createTextBoxes(introText, introFont)
    introTextRect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

    # Creating the sprites and groups
    moving_sprites = pygame.sprite.Group()
    player = Player(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 100)
    life = Hp((WINDOW_WIDTH // 2) + 100, (WINDOW_HEIGHT // 2) + 50)
    moving_sprites.add(player)
    moving_sprites.add(life)

    while inIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        countdown = 3 - (int((pygame.time.get_ticks() - intro_ticks)/1000))
        if countdown > 0:
            player.animate()
            life.animate()
            countdown -= 1
        elif countdown == 0:
            break

        GAME_WINDOW.fill(BG_COLOR)
        GAME_WINDOW.blit(introTextSurf, introTextRect)
        moving_sprites.draw(GAME_WINDOW)
        moving_sprites.update(0.2)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    # transition(0, 2) Remove the remark once I'm done testing with the intro() screen


def check_first_play():
    # Returns the value of first_play to False.
    global first_play
    first_play = False
    return first_play


def play():
    # The main gamemode. Games are randomized and are played 10 times.
    # Player has 3 HP: if they win, they keep their current life. Lose, they lose a life.
    # Lose all their lives: loss. Survive until after the 10th minigame: they win!
    global first_play, minigame_count, win_count, loss_count, win_has_been_called, loss_has_been_called, hp
    if first_play == True:  # The player hasn't played this gamemode once during this session.
        play_showInstructions()
    elif first_play == False:  # The player has played this gamemode once or more during this session
        if minigame_count < WIN_CONDITION and hp > 0:  # Minigame count = how many times I want them to play
            pygame.mixer.Channel(4).unpause()
            pickMinigame()
            if win_has_been_called == True:  # If a win has occured
                win_count += 1
                # print("Minigames played: " + str(minigame_count))
                # print("Player wins: " + str(win_count))
                winState()         
            elif loss_has_been_called == True:  # If a loss has occured
                loss_count += 1
                hp -= 1
                # print("Player losses: " + str(loss_count))
                # print("HP: " + str(hp))
            # elif win_count == 3:  # For testing purposes. Remove this condition eventually
            #     print('Player has won!')
            
            #else:
                # DEBUGGING, unremark if I need to test a game
                # LOGIC() 
                # COLORED_CIRCLES()
                # WORD_TYPE()
                # BUTTON_MASH()
                # TIC_TAC_TOE()
                # DISAPPEARING_NUMBERS()    
                
        elif minigame_count == WIN_CONDITION:  # Player has reached the end. Ultimate win.
            winState()
            ultimate_win()
            # print('The amt of minigames played: ' + str(minigame_count))
        elif hp == 0:  # All hp is depleted. Ultimate loss.
            ultimate_loss()
            


def comingSoon():
    # Tells the player the minigame is not available yet and is in the works!
    GAME_WINDOW.fill(BG_COLOR)

    comingSoonFont = pygame.font.Font(FONT_FILE, 100)
    comingSoon = comingSoonFont.render('Coming Soon!', True, BLACK, None)
    comingSoonRect = comingSoon.get_rect()
    comingSoonRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    GAME_WINDOW.blit(comingSoon, comingSoonRect)
    pygame.display.update()
    transition(3, 0)
    FPSCLOCK.tick(FPS)


def playRandomSound():
    # Plays a random sound! Also tells the player they found the button.
    # Function for the ? mark button if the player finds it.
    randomSound = getRandom(AUDIO_LIST)
    sound_effectButton.click_sound = randomSound

def freeplay():
    # Mode that lets the player play any of the minigames by themselves and not in a group.
    pygame.display.set_caption('Freeplay')
    pygame.mixer.Channel(4).unpause()# Unpause the background music
    # Change freeplay_mode to ensure that the minigames end appropriate to the gamemode.
    global freeplay_mode
    freeplay_mode = True
    # Values that display the thumbnails for the minigames
    # I think I make a function that eventually condenses all these
    wordTypeImageRect = WORDTYPE_IMAGE_THUMBNAIL.get_rect()
    wordTypeImageRect.center = (
        (WINDOW_WIDTH // 2) - 300, (WINDOW_HEIGHT // 2) - 150)
    logicImageRect = LOGIC_IMAGE_THUMBNAIL.get_rect()
    logicImageRect.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2) - 150)
    buttonMashImageRect = BUTTONMASH_IMAGE_THUMBNAIL.get_rect()
    buttonMashImageRect.center = (
        (WINDOW_WIDTH // 2) + 300, (WINDOW_HEIGHT // 2) - 150)

    disappearingImageRect = DISAPPEARING_IMAGE_THUMBNAIL.get_rect()
    disappearingImageRect.center = (
        (WINDOW_WIDTH // 2) - 150, (WINDOW_HEIGHT // 2) + 125)
    coloredCirclesImageRect = COLOREDCIRCLES_IMAGE_THUMBNAIL.get_rect()
    coloredCirclesImageRect.center = (
        ((WINDOW_WIDTH // 2) + 150), (WINDOW_HEIGHT // 2) + 125)

    pygame.draw.rect(LOGIC_IMAGE_THUMBNAIL, BLACK,
                     LOGIC_IMAGE_THUMBNAIL.get_rect(), 2)
    pygame.draw.rect(WORDTYPE_IMAGE_THUMBNAIL, BLACK,
                     WORDTYPE_IMAGE_THUMBNAIL.get_rect(), 2)
    pygame.draw.rect(BUTTONMASH_IMAGE_THUMBNAIL, BLACK,
                     BUTTONMASH_IMAGE_THUMBNAIL.get_rect(), 2)
    pygame.draw.rect(TICTACTOE_IMAGE_THUMBNAIL, BLACK,
                     TICTACTOE_IMAGE_THUMBNAIL.get_rect(), 2)
    pygame.draw.rect(DISAPPEARING_IMAGE_THUMBNAIL, BLACK,
                     DISAPPEARING_IMAGE_THUMBNAIL.get_rect(), 2)
    pygame.draw.rect(COLOREDCIRCLES_IMAGE_THUMBNAIL, BLACK,
                     COLOREDCIRCLES_IMAGE_THUMBNAIL.get_rect(), 2)

    # Buttons that will be under the images. If a player clicks on 1, it will bring them to the
    # introduction screen of the minigame shown above it.
    start_wordType_Button = Button(
        '>', 50, 50, (wordTypeImageRect.center[0] - 25, wordTypeImageRect.center[1] + 115), 6, BUTTON_CLICK_SFX, WORD_TYPE_freeplay)
    start_logic_Button = Button(
        '>', 50, 50, (logicImageRect.center[0] - 25, logicImageRect.center[1] + 115), 6, BUTTON_CLICK_SFX, LOGIC_freeplay)
    start_buttonMash_Button = Button(
        '>', 50, 50, (buttonMashImageRect.center[0] - 25, buttonMashImageRect.center[1] + 115), 6, BUTTON_CLICK_SFX, BUTTON_MASH_freeplay)
    start_disappearing_Button = Button(
        '>', 50, 50, (disappearingImageRect.center[0] - 25, disappearingImageRect.center[1] + 115), 6, BUTTON_CLICK_SFX, DISAPPEARING_NUMBERS_freeplay)
    start_coloredCircles_Button = Button(
        '>', 50, 50, (coloredCirclesImageRect.center[0] - 25, coloredCirclesImageRect.center[1] + 115), 6, BUTTON_CLICK_SFX, COLORED_CIRCLES_freeplay)
    returnButton = Button('Back', 200, 40, (50, 650), 6,
                          EXIT_BUTTON_CLICK_SFX, startMenu)
    inFreeplay = True  # boolean variable for the while loop.
    while inFreeplay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        GAME_WINDOW.fill(BG_COLOR)
        returnButton.draw()

        title = 'Freeplay'  # change this to the name of the game itself later on
        titleFont = pygame.font.Font(FONT_FILE, 80)
        titleTextSurf, titleTextRect = createTextBoxes(title, titleFont)
        titleTextRect.center = (225, 50)  # Positioned at the top-left for now
        GAME_WINDOW.blit(titleTextSurf, titleTextRect)
        # Displays the Logic Game image
        GAME_WINDOW.blit(LOGIC_IMAGE_THUMBNAIL, logicImageRect)
        GAME_WINDOW.blit(WORDTYPE_IMAGE_THUMBNAIL, wordTypeImageRect)
        GAME_WINDOW.blit(BUTTONMASH_IMAGE_THUMBNAIL, buttonMashImageRect)
        GAME_WINDOW.blit(DISAPPEARING_IMAGE_THUMBNAIL, disappearingImageRect)
        GAME_WINDOW.blit(COLOREDCIRCLES_IMAGE_THUMBNAIL,
                         coloredCirclesImageRect)

        start_wordType_Button.draw()
        start_logic_Button.draw()
        start_buttonMash_Button.draw()
        start_disappearing_Button.draw()
        start_coloredCircles_Button.draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def options():
    # READY
    # Mode that lets the player change certain settings in the game.
    # Potential options:
    # 1) Speed of the game (changing the FPS)
    # 2) Turning off in-game audio
    # 3) Turning off music
    # 4) Changing the "brightness" (don't know how yet)
    # (should be called before the main() function)
    pygame.display.set_caption('Options')

    inOptions = True  # boolean variable for the while loop.

    # Buttons
    audio_decreaseButton = Button('-', 100, 50, ((WINDOW_WIDTH // 2) - 250,
                                  (WINDOW_HEIGHT // 5) + 95), 6, BUTTON_CLICK_SFX, audio_volumeDown)
    audio_increaseButton = Button('+', 100, 50, ((WINDOW_WIDTH // 2) + 150,
                                  (WINDOW_HEIGHT // 5) + 95), 6, BUTTON_CLICK_SFX, audio_volumeUp)
    music_decreaseButton = Button('-', 100, 50, ((WINDOW_WIDTH // 2) - 250,
                                  (WINDOW_HEIGHT // 5) + 195), 6, BUTTON_CLICK_SFX, music_volumeDown)
    music_increaseButton = Button('+', 100, 50, ((WINDOW_WIDTH // 2) + 150,
                                  (WINDOW_HEIGHT // 5) + 195), 6, BUTTON_CLICK_SFX, music_volumeUp)

    # Icons
    iconFont = pygame.font.Font(SYMBOL_FONT_FILE, 80)
    speakerIconText = iconFont.render('🔊', True, BLACK, None)
    speakerIconText_rect = speakerIconText.get_rect()
    speakerIconText_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4)

    musicNoteIconText = iconFont.render('🎵', True, BLACK, None)
    musicNoteIconText_rect = musicNoteIconText.get_rect()
    musicNoteIconText_rect.center = (
        WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 75)

    # Rects for images
    # For the audio/music sound bars
    audio_sound_bars_rect = SOUND_BARS_RESIZED.get_rect()
    audio_sound_bars_rect.center = (
        (WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2) - 100)
    music_sound_bars_rect = SOUND_BARS_RESIZED.get_rect()
    music_sound_bars_rect.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))

    # For the black bars

    # In-game audio
    audio_black_bar_10_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_10_rect.center = (
        (WINDOW_WIDTH // 2) + 115, (WINDOW_HEIGHT // 2) - 100)  # On the 10th sound bar

    audio_black_bar_9_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_9_rect.center = (
        (WINDOW_WIDTH // 2) + 90, (WINDOW_HEIGHT // 2) - 100)  # On the 9th sound bar

    audio_black_bar_8_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_8_rect.center = (
        (WINDOW_WIDTH // 2) + 65, (WINDOW_HEIGHT // 2) - 100)  # On the 8th sound bar

    audio_black_bar_7_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_7_rect.center = (
        (WINDOW_WIDTH // 2) + 40, (WINDOW_HEIGHT // 2) - 100)  # On the 7th sound bar

    audio_black_bar_6_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_6_rect.center = (
        (WINDOW_WIDTH // 2) + 15, (WINDOW_HEIGHT // 2) - 100)  # On the 6th sound bar

    audio_black_bar_5_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_5_rect.center = (
        (WINDOW_WIDTH // 2) - 10, (WINDOW_HEIGHT // 2) - 100)  # On the 5th sound bar

    audio_black_bar_4_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_4_rect.center = (
        (WINDOW_WIDTH // 2) - 35, (WINDOW_HEIGHT // 2) - 100)  # On the 4th sound bar

    audio_black_bar_3_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_3_rect.center = (
        (WINDOW_WIDTH // 2) - 60, (WINDOW_HEIGHT // 2) - 100)  # On the 3rd sound bar

    audio_black_bar_2_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_2_rect.center = (
        (WINDOW_WIDTH // 2) - 85, (WINDOW_HEIGHT // 2) - 100)  # On the 2nd sound bar

    audio_black_bar_1_rect = BLACK_BAR_RESIZED.get_rect()
    audio_black_bar_1_rect.center = (
        (WINDOW_WIDTH // 2) - 110, (WINDOW_HEIGHT // 2) - 100)  # On the 1st sound bar

    # Music
    music_black_bar_10_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_10_rect.center = (
        (WINDOW_WIDTH // 2) + 115, (WINDOW_HEIGHT // 2))  # On the 10th sound bar

    music_black_bar_9_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_9_rect.center = (
        (WINDOW_WIDTH // 2) + 90, (WINDOW_HEIGHT // 2))  # On the 9th sound bar

    music_black_bar_8_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_8_rect.center = (
        (WINDOW_WIDTH // 2) + 65, (WINDOW_HEIGHT // 2))  # On the 8th sound bar

    music_black_bar_7_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_7_rect.center = (
        (WINDOW_WIDTH // 2) + 40, (WINDOW_HEIGHT // 2))  # On the 7th sound bar

    music_black_bar_6_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_6_rect.center = (
        (WINDOW_WIDTH // 2) + 15, (WINDOW_HEIGHT // 2))  # On the 6th sound bar

    music_black_bar_5_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_5_rect.center = (
        (WINDOW_WIDTH // 2) - 10, (WINDOW_HEIGHT // 2))  # On the 5th sound bar

    music_black_bar_4_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_4_rect.center = (
        (WINDOW_WIDTH // 2) - 35, (WINDOW_HEIGHT // 2))  # On the 4th sound bar

    music_black_bar_3_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_3_rect.center = (
        (WINDOW_WIDTH // 2) - 60, (WINDOW_HEIGHT // 2))  # On the 3rd sound bar

    music_black_bar_2_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_2_rect.center = (
        (WINDOW_WIDTH // 2) - 85, (WINDOW_HEIGHT // 2))  # On the 2nd sound bar

    music_black_bar_1_rect = BLACK_BAR_RESIZED.get_rect()
    music_black_bar_1_rect.center = (
        (WINDOW_WIDTH // 2) - 110, (WINDOW_HEIGHT // 2))  # On the 1st sound bar
    while inOptions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        GAME_WINDOW.fill(WHITE)
        returnButton.draw()

        audio_decreaseButton.draw()
        audio_increaseButton.draw()
        music_decreaseButton.draw()
        music_increaseButton.draw()

        title = 'Options'  # change this to the name of the game itself later on
        titleFont = pygame.font.Font(FONT_FILE, 80)
        titleTextSurf, titleTextRect = createTextBoxes(title, titleFont)
        titleTextRect.center = (225, 50)
        GAME_WINDOW.blit(titleTextSurf, titleTextRect)
        GAME_WINDOW.blit(speakerIconText, speakerIconText_rect)
        GAME_WINDOW.blit(musicNoteIconText, musicNoteIconText_rect)

        # The sound bars for the in-game audio
        GAME_WINDOW.blit(SOUND_BARS_RESIZED, audio_sound_bars_rect)
        # The sound bars for the music
        GAME_WINDOW.blit(SOUND_BARS_RESIZED, music_sound_bars_rect)

        # Displaying the in-game audio level change
        # Maybe show this off for the presentation. Talk about how simple the design look on the outside but the complex code (all of this) is what makes it happen

        # If both in-game audio and music are being changed:
        # In-game audio: 0.9 / Music: 0.9
        if game_audio_lvl == 0.9 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            # The black bar will be on the 10th sound bar, indicating that the volume is at 0.9
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)

        # In-game audio: 0.9 / Music: 0.8
        elif game_audio_lvl == 0.9 and music_lvl == 0.8:
            # The black bar will be on the 10th sound bar, indicating that the volume is at 0.9
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            # The black bar will be on the 9th sound bar, indicating that the volume is at 0.8
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
        # In-game audio: 0.9 / Music: 0.7
        elif game_audio_lvl == 0.9 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
        # In-game audio: 0.9 / Music: 0.6
        elif game_audio_lvl == 0.9 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
        # In-game audio: 0.9 / Music: 0.5
        elif game_audio_lvl == 0.9 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
        # In-game audio: 0.9 / Music: 0.4
        elif game_audio_lvl == 0.9 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
        # In-game audio: 0.9 / Music: 0.3
        elif game_audio_lvl == 0.9 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
        # In-game audio: 0.9 / Music: 0.2
        elif game_audio_lvl == 0.9 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
        # In-game audio: 0.9 / Music: 0.1
        elif game_audio_lvl == 0.9 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
        # In-game audio: 0.9 / Music: 0
        elif game_audio_lvl == 0.9 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0.8 / Music: 0.9
        elif game_audio_lvl == 0.8 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
        # In-game audio: 0.8 / Music: 0.8
        elif game_audio_lvl == 0.8 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            # The black bars will be on the 9th sound bar, indicating that the volume is at 0.8 for both
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)

        # In-game audio: 0.8 / Music: 0.7
        elif game_audio_lvl == 0.8 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)

        # In-game audio: 0.8 / Music: 0.6
        elif game_audio_lvl == 0.8 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0.8 / Music: 0.5
        elif game_audio_lvl == 0.8 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)

        # In-game audio: 0.8 / Music: 0.4
        elif game_audio_lvl == 0.8 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)

        # In-game audio: 0.8 / Music: 0.3
        elif game_audio_lvl == 0.8 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)

        # In-game audio: 0.8 / Music: 0.2
        elif game_audio_lvl == 0.8 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)

        # In-game audio: 0.8 / Music: 0.1
        elif game_audio_lvl == 0.8 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)

        # In-game audio: 0.8 / Music: 0
        elif game_audio_lvl == 0.8 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0.7 / Music: 0.9
        elif game_audio_lvl == 0.7 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
        # In-game audio: 0.7 / Music: 0.8
        elif game_audio_lvl == 0.7 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
        # In-game audio: 0.7 / Music: 0.7
        elif game_audio_lvl == 0.7 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            # The black bar will be on the 8th sound bar, indicating that the volume is at 0.7
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)

        # In-game audio: 0.7 / Music: 0.6
        elif game_audio_lvl == 0.7 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0.7 / Music: 0.5
        elif game_audio_lvl == 0.7 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
        # In-game audio: 0.7 / Music: 0.4
        elif game_audio_lvl == 0.7 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
        # In-game audio: 0.7 / Music: 0.3
        elif game_audio_lvl == 0.7 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
        # In-game audio: 0.7 / Music: 0.2
        elif game_audio_lvl == 0.7 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
        # In-game audio: 0.7 / Music: 0.1
        elif game_audio_lvl == 0.7 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
        # In-game audio: 0.7 / Music: 0
        elif game_audio_lvl == 0.7 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0.6 / Music: 0.9
        elif game_audio_lvl == 0.6 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
        # In-game audio: 0.6 / Music: 0.8
        elif game_audio_lvl == 0.6 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
        # In-game audio: 0.6 / Music: 0.7
        elif game_audio_lvl == 0.6 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
        # In-game audio: 0.6 / Music: 0.6
        elif game_audio_lvl == 0.6 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            # The black bar will be on the 7th sound bar, indicating that the volume is at 0.6
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0.6 / Music: 0.5
        elif game_audio_lvl == 0.6 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)

        # In-game audio: 0.6 / Music: 0.4
        elif game_audio_lvl == 0.6 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
        # In-game audio: 0.6 / Music: 0.3
        elif game_audio_lvl == 0.6 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
        # In-game audio: 0.6 / Music: 0.2
        elif game_audio_lvl == 0.6 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)

        # In-game audio: 0.6 / Music: 0.1
        elif game_audio_lvl == 0.6 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)

        # In-game audio: 0.6 / Music: 0
        elif game_audio_lvl == 0.6 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0.5 / Music: 0.9
        elif game_audio_lvl == 0.5 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)

        # In-game audio: 0.5 / Music: 0.8
        elif game_audio_lvl == 0.5 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
        # In-game audio: 0.5 / Music: 0.7
        elif game_audio_lvl == 0.5 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)

        # In-game audio: 0.5 / Music: 0.6
        elif game_audio_lvl == 0.5 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0.5 / Music: 0.5
        elif game_audio_lvl == 0.5 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            # The black bar will be on the 6th sound bar, indicating that the volume is at 0.5
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)

        # In-game audio: 0.5 / Music: 0.4
        elif game_audio_lvl == 0.5 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)

        # In-game audio: 0.5 / Music: 0.3
        elif game_audio_lvl == 0.5 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)

        # In-game audio: 0.5 / Music: 0.2
        elif game_audio_lvl == 0.5 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)

        # In-game audio: 0.5 / Music: 0.1
        elif game_audio_lvl == 0.5 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)

        # In-game audio: 0.5 / Music: 0
        elif game_audio_lvl == 0.5 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0.4 / Music: 0.9
        elif game_audio_lvl == 0.4 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)

        # In-game audio: 0.4 / Music: 0.8
        elif game_audio_lvl == 0.4 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)

        # In-game audio: 0.4 / Music: 0.7
        elif game_audio_lvl == 0.4 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)

        # In-game audio: 0.4 / Music: 0.6
        elif game_audio_lvl == 0.4 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0.4 / Music: 0.5
        elif game_audio_lvl == 0.4 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)

        # In-game audio: 0.4 / Music: 0.4
        elif game_audio_lvl == 0.4 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            # The black bar will be on the 5th sound bar, indicating that the volume is at 0.4
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)

        # In-game audio: 0.4 / Music: 0.3
        elif game_audio_lvl == 0.4 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)

        # In-game audio: 0.4 / Music: 0.2
        elif game_audio_lvl == 0.4 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)

        # In-game audio: 0.4 / Music: 0.1
        elif game_audio_lvl == 0.4 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)

        # In-game audio: 0.4 / Music: 0
        elif game_audio_lvl == 0.4 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0.3 / Music: 0.9
        elif game_audio_lvl == 0.3 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)

        # In-game audio: 0.3 / Music: 0.8
        elif game_audio_lvl == 0.3 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)

        # In-game audio: 0.3 / Music: 0.7
        elif game_audio_lvl == 0.3 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)

        # In-game audio: 0.3 / Music: 0.6
        elif game_audio_lvl == 0.3 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0.3 / Music: 0.5
        elif game_audio_lvl == 0.3 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)

        # In-game audio: 0.3 / Music: 0.4
        elif game_audio_lvl == 0.3 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)

        # In-game audio: 0.3 / Music: 0.3
        elif game_audio_lvl == 0.3 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            # The black bar will be on the 4th sound bar, indicating that the volume is at 0.3
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)

        # In-game audio: 0.3 / Music: 0.2
        elif game_audio_lvl == 0.3 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)

        # In-game audio: 0.3 / Music: 0.1
        elif game_audio_lvl == 0.3 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)

        # In-game audio: 0.3 / Music: 0
        elif game_audio_lvl == 0.3 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0.2 / Music: 0.9
        elif game_audio_lvl == 0.2 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)

        # In-game audio: 0.2 / Music: 0.8
        elif game_audio_lvl == 0.2 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)

        # In-game audio: 0.2 / Music: 0.7
        elif game_audio_lvl == 0.2 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)

        # In-game audio: 0.2 / Music: 0.6
        elif game_audio_lvl == 0.2 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0.2 / Music: 0.5
        elif game_audio_lvl == 0.2 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)

        # In-game audio: 0.2 / Music: 0.4
        elif game_audio_lvl == 0.2 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)

        # In-game audio: 0.2 / Music: 0.3
        elif game_audio_lvl == 0.2 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)

        # In-game audio: 0.2 / Music: 0.2
        elif game_audio_lvl == 0.2 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            # The black bar will be on the 3rd sound bar, indicating that the volume is at 0.2
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)

        # In-game audio: 0.2 / Music: 0.1
        elif game_audio_lvl == 0.2 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)

        # In-game audio: 0.2 / Music: 0
        elif game_audio_lvl == 0.2 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0.1 / Music: 0.9
        elif game_audio_lvl == 0.1 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)

        # In-game audio: 0.1 / Music: 0.8
        elif game_audio_lvl == 0.1 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)

        # In-game audio: 0.1 / Music: 0.7
        elif game_audio_lvl == 0.1 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)

        # In-game audio: 0.1 / Music: 0.6
        elif game_audio_lvl == 0.1 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0.1 / Music: 0.5
        elif game_audio_lvl == 0.1 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)

        # In-game audio: 0.1 / Music: 0.4
        elif game_audio_lvl == 0.1 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)

        # In-game audio: 0.1 / Music: 0.3
        elif game_audio_lvl == 0.1 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)

        # In-game audio: 0.1 / Music: 0.2
        elif game_audio_lvl == 0.1 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)

        # In-game audio: 0.1 / Music: 0.1
        elif game_audio_lvl == 0.1 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            # The black bar will be on the 2nd sound bar, indicating that the volume is at 0.1
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)

        # In-game audio: 0.1 / Music: 0
        elif game_audio_lvl == 0.1 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # In-game audio: 0 / Music: 0.9
        elif game_audio_lvl == 0 and music_lvl == 0.9:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)

        # In-game audio: 0 / Music: 0.8
        elif game_audio_lvl == 0 and music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)

        # In-game audio: 0 / Music: 0.7
        elif game_audio_lvl == 0 and music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)

        # In-game audio: 0 / Music: 0.6
        elif game_audio_lvl == 0 and music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)

        # In-game audio: 0 / Music: 0.5
        elif game_audio_lvl == 0 and music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)

        # In-game audio: 0 / Music: 0.4
        elif game_audio_lvl == 0 and music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)

        # In-game audio: 0 / Music: 0.3
        elif game_audio_lvl == 0 and music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)

        # In-game audio: 0 / Music: 0.2
        elif game_audio_lvl == 0 and music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)

        # In-game audio: 0 / Music: 0.1
        elif game_audio_lvl == 0 and music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)

        # In-game audio: 0 / Music: 0
        elif game_audio_lvl == 0 and music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)
            # The black bar will be on the 1st sound bar, indicating that the volume is at 0 (mute)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        # Changing in-game audio ONLY
        elif game_audio_lvl == 0.9:
            # The black bar will be on the 1st sound bar for game_audio, indicating that the volume is at 0.9
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
        elif game_audio_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            # The black bar will be on the 9th sound bar, indicating that the volume is at 0.8
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
        elif game_audio_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            # The black bar will be on the 8th sound bar, indicating that the volume is at 0.7
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
        elif game_audio_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            # The black bar will be on the 7th sound bar, indicating that the volume is at 0.6
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
        elif game_audio_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            # The black bar will be on the 6th sound bar, indicating that the volume is at 0.5
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
        elif game_audio_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            # The black bar will be on the 5th sound bar, indicating that the volume is at 0.4
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
        elif game_audio_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            # The black bar will be on the 4th sound bar, indicating that the volume is at 0.3
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
        elif game_audio_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            # The black bar will be on the 3rd sound bar, indicating that the volume is at 0.2
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
        elif game_audio_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            # The black bar will be on the 2nd sound bar, indicating that the volume is at 0.1
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
        elif game_audio_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_2_rect)
            # The black bar will be on the 1st sound bar, indicating that the volume is at 0 (mute)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, audio_black_bar_1_rect)

        # Changing music level ONLY
        elif music_lvl == 0.9:
            # The black bar will be on the 1st sound bar for music, indicating that the volume is at 0.9
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
        elif music_lvl == 0.8:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            # The black bar will be on the 9th sound bar, indicating that the volume is at 0.8
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
        elif music_lvl == 0.7:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            # The black bar will be on the 8th sound bar, indicating that the volume is at 0.7
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
        elif music_lvl == 0.6:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            # The black bar will be on the 7th sound bar, indicating that the volume is at 0.6
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
        elif music_lvl == 0.5:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            # The black bar will be on the 6th sound bar, indicating that the volume is at 0.5
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
        elif music_lvl == 0.4:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            # The black bar will be on the 5th sound bar, indicating that the volume is at 0.4
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
        elif music_lvl == 0.3:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            # The black bar will be on the 4th sound bar, indicating that the volume is at 0.3
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
        elif music_lvl == 0.2:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            # The black bar will be on the 3rd sound bar, indicating that the volume is at 0.2
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
        elif music_lvl == 0.1:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            # The black bar will be on the 2nd sound bar, indicating that the volume is at 0.1
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
        elif music_lvl == 0:
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_10_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_9_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_8_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_7_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_6_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_5_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_4_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_3_rect)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_2_rect)
            # The black bar will be on the 1st sound bar, indicating that the volume is at 0 (mute)
            GAME_WINDOW.blit(BLACK_BAR_RESIZED, music_black_bar_1_rect)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def exit():
    # Mode that asks a 2nd confirmation from the player if they want to exit the game.
    # READY
    pygame.display.set_caption('Exiting...')
    if pygame.mixer.Channel(4).get_busy():
        pygame.mixer.Channel(4).pause()

    exiting = True  # boolean variable for the while loop
    yesButton = Button('Yes', 200, 60, ((WINDOW_WIDTH // 2) - 250,
                       WINDOW_HEIGHT // 2), 6, EXIT_CONFIRMATION_BUTTON_CLICK_SFX, exitGame)
    noButton = Button('No', 200, 60, ((WINDOW_WIDTH // 2) +
                      50, WINDOW_HEIGHT // 2), 6, BUTTON_CLICK_SFX, startMenu)

    while exiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        GAME_WINDOW.fill(WHITE)

        title = 'Are you sure?'
        titleFont = pygame.font.Font(FONT_FILE, 65)
        titleTextSurf, titleTextRect = createTextBoxes(title, titleFont)
        titleTextRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

        yesButton.draw()
        noButton.draw()
        GAME_WINDOW.blit(titleTextSurf, titleTextRect)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def testScreen():
    # Screen I will use for debugging/testing purposes. I plan to do anything with this
    GAME_WINDOW.fill(BG_COLOR)

    testSpritesGroup = pygame.sprite.Group()
    redButton = SpriteButton(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    testSpritesGroup.add(redButton)

    testing = True
    while testing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.KEYDOWN:
                redButton.animate()
        testSpritesGroup.draw(GAME_WINDOW)
        
        testSpritesGroup.update(1)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        

if __name__ == '__main__':
    #testing = True
    # while testing:
    #     intro()
    #startMenu()
    #testScreen()
    #lossState()
    #BUTTON_MASH()
    #DISAPPEARING_NUMBERS()
    startMenu()

# This is the main program of the game TimeWaster. It will call all the functions I've created
# in different files. Once the games' code is done, copy and paste them here (I'll figure out how to make them work
# eventually).

# To-Do List:
# 1) When the game loads up, a starting animation should play before loading the Main Menu.
# 2) Code the Main Menu. Should have 4 options: Play, Freeplay, Options, Exit
# 3) Add the main() function from buttonmashing_prototype_v3 and use it as the main function that will call the
# other games using event flags.
# 4) Change font to a "16-bit/pixel" font to make it seem more retro.
# 5) Create different intro animations for every menu option except Exit(3 in total: Play, Freeplay, Options)


# Logs:
# 10/28/22
# (9:56 PM) Finished a 30 min session creating the 4 Main Menu buttons. All that's left is adding the functions for the games.
# Next time, focus on making the ButtonMashing game and Logic Game
# 11/16/22
# (10:30 PM) Decided to stop working on the prototype, was watching the video posted below about sprites.
# Plan is to have an Intro animation using the sprites before getting the game loaded up. Work on that tomorrow
# 11/17/22
# (11 AM) Finished a 3 hr session working on the main game file. Gave functionality to the Freeplay, Options, and Exit buttons.
# Created an intro animation that loads when the game starts up. Created button sound effects that use files from the Persona 4 game.
# Next time, focus on fixing the button hover sound bug. A bug occurs with one of the buttons where it continuously plays the sound whenever it's being hovered.
# Make it so that when a button is hovered, the sound is only played once per hover.
# (10:25 PM) Finished a 4 hr session working on this. Deleted the old createButtons function and created a Button class instead that also gives the buttons
# an "animated" look. Also gave the buttons a sound when being clicked, though the sound when they're being hovered is a mess to code so I left it out.
# Next time, focus on finishing up the minigames

# 11/18/22
# (8:38 PM) Finished a 10 min session. Modified the font to look more "retro." Was also looking into "transition screens" where
# the scene looks like it'll fade into the next one
# Look into those next time, I saved a bookmark in Firefox from a StackOverflow question.

# 11/25/22
# (1:41 PM) Finished an hour sess. Added the Logic minigame functions and named them as such to not be confused with similar ones that I will add later on.
# Was imagining how the freeplay area would look but I think I'll need to draw it in Notability first.
# Next time, apply what I will draw in Notability to this file. Also start adding the other games' code.
# (5:02 PM) Finished an hour sess. Started on adding what I drew in Notability to the Freeplay function, just gotta work out some coordinate positions.
# Next time, start on Line 947
# (8:40 PM) Finished an hour sess. Finished what I had drawn into Notability.
# Next time, focus on the Colored Circles game, as it is not close to being done.

# 11/27/22
# Added instructions for the 3 minigames that are in here so far. Added background music for the player to listen to (make sure to cite them in presentation).
# Working on Options menu. Finished Options menu.
# Next time, work on the main function of the game: counting how many minigames a player has won/lost out of 5 then determining if they won/lost. Also, work on presentation!

# 11/28/22
# Added instructions for the Play gamemode. Working on adding the win/loss states.
# Working on the HP sprite. The empty heart image is turning yellow for some reason, look into fixing that next time.
# Don't forget to unremark the lines of code for the music!
# (10:35 PM) Added Hearts sprites to the play_showInstructions() function. Just got to position right.
# Next time, position them correctly under the 2nd instructions and animate the hearts I want moving.
# Read Line 2405!

# 11/29/22
# Instructions for the play_showInstructions() is complete.
# Bugs with minigames:
# -- Word Type: showing Time's up! after 1st iteration each iteration
# Next time, work on bugs and configure winState and lossState. Also PRESENTATION!

# 11/29/22 Session 2
# Created the winState and lossStates. Confirmed working with LOGIC so far, need to test with COLORED_CIRCLES and WORD_TYPE next.
# Next time, work on setting the conditions for displaying how much HP the player has and determining a loss based on their HP.
# ALSO PRESENTATION

# 11/29/22 Session 3
# Arranged some code around to look better and perform efficiently. Still creating the conditions for displaying how much HP the player has and determining losses based on that.
# Next time, same thing. Also, make a separate win() and loss() functions for the Freeplay mode (probably two for each game).
# ALSO PRESENTATION

# 11/30/22 Session 1
# Added a hidden button in the start menu. If a player finds it, they can click on it to play a random sound effect each time.
#

# 12/1/22 Session 1
# Added the BUTTON_MASH() game into the main game. Currently debugging and adding a "button sprite" that is "pressed" everytime
# the player hits the selected letter.
# Next time, focus on fixing that

# 12/2/22 Session 1
# Added freeplay_mode variable that is always set to True whenever the player enters Freeplay.
# Changes the ending functions of each minigame when played. Once the player returns to startMenu(), it is set back to False.
# Created the BUTTON_MASH_freeplay_win() and loss() functions. Make sure to copy and paste those for the 3 other minigames.
# Next time, create the _freeplay_win() and loss() for COLORED_CIRCLES, LOGIC_, and WORD_TYPE.
# Once done, add DISAPPEARING_NUMBERS and ensure it's good to go.

# 12/2/22 Session 2
# Added the functions for DISAPPEARING_NUMBERS and it is working. Also gave every other minigame the _freeplay version
# to work with the freeplay_mode variable.
# Next, gotta convert it to exe to be able to upload it on itch.io!

# Useful sources:
# https://www.youtube.com/watch?v=MYaxPa_eZS0 Intro to Sprites in PyGame
