import pygame
import random

#define variables for game
FPS = 60

#size of our window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

#size of paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#size of ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

#Speed of paddle & ball
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#initialize our screen
screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)

def draw_ball(ballXpos, ballYpos):
    ball = pygame.rect(ballXpos, ballYpos, BALL_WIDTH, BALL_HEIGHT)
    pygame.draw.rect(screen, WHITE, ball)

def drawPaddle1(paddle1Ypos):
    paddle1 = pygame.rect(PADDLE_BUFFER, paddle1Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle1)

def drawPaddle2(paddle2Ypos):
    paddle2 = pygame.rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle2)

def updateBall(paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXdirection, ballYdirection):
    #update x and y position
    ballXpos = ballXpos + ballXdirection * BALL_X_SPEED
    ballYpos = ballYpos + ballYdirection * BALL_Y_SPEED
    score = 0

    #collision - if ball hits left side, then switch direction
    if(ballXpos < PADDLE_BUFFER + PADDLE_WIDTH and ballYpos + BALL_HEIGHT >= paddle1Ypos and ballYpos - BALL_HEIGHT <= paddle1Ypos + PADDLE_HEIGHT):
        ballXdirection = 1
    elif(ballXpos <= 0):
        ballXdirection = 1
        score = -1
        return[score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXdirection, ballYdirection]
    #switch direction if hits on other side
    if(ballXpos >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and ballYpos + BALL_HEIGHT >= paddle2Ypos and ballYpos - BALL_HEIGHT <= paddle2Ypos + PADDLE_HEIGHT):
        ballXdirection = -1
    elif(ballXpos >= WINDOW_WIDTH - BALL_WIDTH):
        ballXdirection = -1
        score = 1
        return[score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXdirection, ballYdirection]
    if(ballYpos <= 0):
        ballYpos = 0
        ballYdirection = 1
    elif(ballYpos >= WINDOW_HEIGHT - BALL_HEIGHT):
        ballYpos = WINDOW_HEIGHT - BALL_HEIGHT
        ballYdirection = -1
    return[score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXdirection, ballYdirection]

def updatePaddle1(action, paddle1Ypos):
    #if move up
    if(action[1] == 1):
        paddle1Ypos = paddle1Ypos - PADDLE_SPEED
    #if move down
    if(action[2] == 2):
        paddle1Ypos = paddle1Ypos + PADDLE_SPEED
    #don't let move off screen
    if(paddle1Ypos < 0):
        paddle1Ypos = 0
    if(paddle1Ypos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle1Ypos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle1Ypos

def updatePaddle2(action, ballYpos):
    #if move up
    if(action[1] == 1):
        paddle2Ypos = paddle2Ypos - PADDLE_SPEED
    #if move down
    if(action[2] == 2):
        paddle2Ypos = paddle1Ypos + PADDLE_SPEED
    #don't let move off screen
    if(paddle2Ypos < 0):
        paddle2Ypos = 0
    if(paddle2Ypos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle2Ypos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle2Ypos

class PongGame:
    def __init__(self):
        #random number for init direction of ball
        num = random.randInt(0, 9)
        #keep score
        self.tally = 0
        #initialize positions of paddle
        self.paddle1Ypos = WINDOW_HEIGHT /2 - PADDLE_HEIGHT/2
        self.paddle2Ypos = WINDOW_HEIGHT /2 - PADDLE_HEIGHT/2
        #ball direction def
        self.ballXdirection = 1
        self.ballYdirection = 1
        #starting point
        self.ballXpos = WINDOW_HEIGHT /2 - BALL_WIDTH /2
    def getPresentFrame(self):
        #for each frame, call the event queue
        pygame.event.pump()
        #make background black
        screen.fill(BLACK)
        #draw paddles
        drawPaddle1(self.paddle1Ypos)
        drawPaddle2(self.paddle2Ypos)
        #draw ball
        drawBall(self.ballXpos, self.ballYpos)
        #get pixels
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        #update window
        pygame.display.flip()
        #return screen data
        return image_data
    def getNextFrame(self, action):
        pygame.event.pump()
        screen.fill(BLACK)
        self.paddle1Ypos = updatePaddle1(action, self.paddle1Ypos)
        drawPaddle1(self.paddle1Ypos)
        self.paddle2Ypos = updatePaddle2(self.paddle2Ypos, self.ballYpos)
        drawBall(self.ballXpos, self.ballYpos)
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.flip()
        self.tally = self.tally + score
        return[score, image_data]
