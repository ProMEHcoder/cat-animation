import pygame  #import pygame module
import random

pygame.init()  # initialize pygame

# Variables
# Create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Handles player animation
# TODO 4: Create a new function, playerAnimation(), that will add 0.1 to the playerIndex and set the playerSurface to the playerWalk[playerIndex]
#function - a shortcut for a block of code that we will use often
def playerAnimation():
  global playerSurface, playerindex
  playerindex += 0.1
  if (playerindex >= len(playerWalk)):
    playerindex = 0
  playerSurface =playerWalk[int(playerindex)]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Player 
# Walk Animation 
# TODO 0: Import at least two images for each frame of the walking animation
# TODO 1: Make variables playerWalk1, playerWalk2, ... for each image. Transform the images as needed
playerWalk1 = pygame.image.load('cat1.png').convert_alpha()
playerWalk2 = pygame.image.load('cat2.png').convert_alpha()
playerWalk1 = pygame.transform.scale(playerWalk1,(80,80))
playerWalk2 = pygame.transform.scale(playerWalk2,(80,80))
# TODO 2: Make a list, playerWalk, containing each walk variable. Make a variable, playerIndex set to 0, that will represent which frame we are on
playerWalk =[playerWalk1, playerWalk2]
playerindex = 0
# TODO 3: Make a variable, playerSurface and set it equal to playerWalk[playerIndex]
playersurfis = playerWalk[playerindex]
# Player variables
playerSurface = pygame.image.load('cat1.png').convert_alpha()
playerSurface = pygame.transform.scale(playerSurface,(80,80))
player = playerSurface.get_rect(midbottom=(100, SCREEN_HEIGHT - 80))
isJump = False
jumpSpeed = 8
jumpHeight = 300

# Background
bgSurface = pygame.image.load('background.jpg').convert_alpha()
bgSurface = pygame.transform.scale(bgSurface, (SCREEN_WIDTH + 100, SCREEN_HEIGHT))
background = bgSurface.get_rect()

# Ground
groundSurface = pygame.image.load('ground.png').convert_alpha()
ground = groundSurface.get_rect(midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT))
groundY = 440

# Create the game loop
run = True
while run:
  # Player Jump and Gravity
  # Player controls
  
  # Player animation
  # TODO 4.1: call the playerAnimation function
  playerAnimation()
  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # Display player
  screen.blit(bgSurface, background)
  screen.blit(groundSurface, ground)
  screen.blit(playerSurface, player)

  # Update Display
  pygame.display.update()

  # Determines how many times method should be called per second
  pygame.time.Clock().tick(60)

pygame.quit()