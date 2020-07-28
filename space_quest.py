"""
Progarm Name: space_quest.py
Written by: Kernard
Date: 23 March 2020
Purpose: This program is a simple game based off of the 'space invaders' game.
A character is able to move up and down left and right until they reach the Star which is the prize.
"""
# Imports
import pygame
import random

# Initializes the game.
pygame.init()

# Initialized values.
width = 1024
height = 768

# Creates the screen size.
screen = pygame.display.set_mode((width, height))

# Screen Background.
background = pygame.image.load("assets/blue-moon.png")

# Images of charcaters.
player_ = pygame.image.load("assets/spaceship.png")
enemy_ = pygame.image.load("assets/enemy.png")
enemy_2 = pygame.image.load("assets/enemy2.png")
enemy_3 = pygame.image.load("assets/enemy3.png")
prize = pygame.image.load("assets/prize.png")


# Title and Icon.
pygame.display.set_caption("Space quest")
icon =pygame.image.load('assets/ico.png')
pygame.display.set_icon(icon)

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).
player_height = player_.get_height()
player_width = player_.get_width()

enemy_height = enemy_.get_height()
enemy_width = enemy_.get_width()

enemy2_height = enemy_2.get_height()
enemy2_width = enemy_2.get_width()

enemy3_height = enemy_3.get_height()
enemy3_width = enemy_3.get_width()

prize_height = enemy_.get_height()
prize_width = enemy_.get_width()

# Player Chracter position.
playerX = 490
playerY = 640
playerX_move = 0
playerY_move = 0


# Make the enemies start off screen and at a random y position.
enemyX = random.randint(0, width)
enemyY = random.randint(50, 468)
enemyX_move = 4
enemyY_move = 40

enemy2X = random.randint(0, width)
enemy2Y = random.randint(50, 468)
enemy2X_move = 4
enemy2Y_move = 40

enemy3X = random.randint(0, width)
enemy3Y = random.randint(50, 468)
enemy3X_move = 4
enemy3Y_move = 40

# Prize position coordinates.
prizeX = random.randint(0, width)
prizeY = random.randint(0, 50)

# Checks that the close button (X) hasn't been pressed to keep the game screen open.
running = True
while running:
# Setting the background color of the game.
    screen.fill((0, 0, 0))
# Background image
    screen.blit(background, (0, 0))
# Player and enemy image being drawn on the screen after the background has been drawn.
    screen.blit(player_, (playerX, playerY))
    screen.blit(enemy_, (enemyX, enemyY))
    screen.blit(enemy_2, (enemy2X, enemy2Y))
    screen.blit(enemy_3, (enemy3X, enemy3Y))
    screen.blit(prize, (prizeX, prizeY))

# This updates the screen.
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Player movement. If keystroke is pressed check whether its right or left.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_move = -5
            if event.key == pygame.K_RIGHT:
                playerX_move = 5

# Player movement. If keystroke is pressed check whether its up or down.
            if event.key == pygame.K_UP:
                playerY_move = -5
            if event.key == pygame.K_DOWN:
                playerY_move = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_move = 0
            else:
                playerY_move = 0

    playerX += playerX_move
    playerY += playerY_move
# Limits the player from moving out of the scren window from left or right.
    if playerX <= 0:
        playerX = 0
    elif playerX >= 960:
        playerX = 960
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 704:
        playerY = 704

# Check for collision of the enemy with the player.
    playerBox = pygame.Rect(player_.get_rect())

# The following updates the playerBox position to the player's position,
# in effect making the box stay around the player image.
    playerBox.top = playerY
    playerBox.left = playerX

# Bounding box for the enemy:
    enemyBox = pygame.Rect(enemy_.get_rect())
    enemyBox.top = enemyY
    enemyBox.left = enemyX
# Enemy 2 Bounding Box
    enemyBox = pygame.Rect(enemy_2.get_rect())
    enemyBox.top = enemy2Y
    enemyBox.left = enemy2X

# Enemy 3 Bounding Box
    enemyBox = pygame.Rect(enemy_3.get_rect())
    enemyBox.top = enemy3Y
    enemyBox.left = enemy3X

# Enemy Movement from Left to right.
    enemyX += enemyX_move
    enemy2X += enemy2X_move
    enemy3X += enemy3X_move

# Bounding box for the prize:
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeY
    prizeBox.left = prizeX


# Limits the enemy from moving out of the scren window from left or right.
    if enemyX <= 0:
        enemyX_move = 4
        enemyY += enemyY_move
    elif enemyX >= 960:
        enemyX_move = -4
        enemyY += enemyY_move
    if enemyY <= 0:
        enemyY_move = 40
        enemyY += enemyY_move
    elif enemyY >= 704:
        enemyY_move = -40
        enemyY += enemyY_move

# Limits enemy 2 from moving out of the scren window from left or right.
    if enemy2X <= 0:
        enemy2X_move = 4
        enemy2Y += enemy2Y_move
    elif enemy2X >= 960:
        enemy2X_move = -4
        enemy2Y += enemy2Y_move
    if enemy2Y <= 0:
        enemy2Y_move = 40
        enemy2Y += enemy2Y_move
    elif enemy2Y >= 704:
        enemy2Y_move = -40
        enemy2Y += enemy2Y_move

# Limits enemy 3 from moving out of the scren window from left or right.
    if enemy3X <= 0:
        enemy3X_move = 4
        enemy3Y += enemy3Y_move
    elif enemy3X >= 960:
        enemy3X_move = -4
        enemy3Y += enemy3Y_move
    if enemy3Y <= 0:
        enemy3Y_move = 40
        enemy3Y += enemy3Y_move
    elif enemy3Y >= 704:
        enemy3Y_move = -40
        enemy3Y += enemy3Y_move


# Test collision of the boxes:
    if playerBox.colliderect(enemyBox):
        # Display losing status to the user:
        print("You lose!")
        # Quite game and exit window:
        running = False

# Test collision of the boxes:
    if playerBox.colliderect(prizeBox):
        # Display losing status to the user:
        print("You Won!!!")
        # Quite game and exit window:
        running = False
