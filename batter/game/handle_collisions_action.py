import random
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    # Vanessa
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # Need to create the ball
        # Need to create the paddle
        # need to create a list of the bricks
        # Call handle bricks function
        # Call handle paddel function
        # Call handle ball constraints
        # Call handle floor function
        # Call handle paddle function

    # Brian
    def _handle_paddle(self, paddle, ball):
        pass
        # Needs to loop through the length of the paddle and compare its position with the position of the ball.
        # If the ball postition is equal to any portion of the paddle, bounce.

    # Vanessa
    def _handle_bricks(self, bricks, ball):
        pass
        # Need to loop through each brick in bricks.
        # If the balls position is equal to bricks position, bounce ball and remove brick.

    # Brian
    def _handle_ball_constraints(self, ball):
        pass
        # Needs to find the position of the ball.
        # Then grab the y value of the ball.
        # The check to see if y equals 0 + 1
        # if yes, bounce the ball.
        # Find the x value of ball.
        # if x equal 0 or Max_X bounce.

    # Brian
    def _handle_floor(self, ball):
        pass
        # Needs to find the position of the ball.
        # Then grab the y value of the ball.
        # The check to see if y equals of MAX_Y
        # Exit the system

    # Brian
    def _handle_paddle_constraints(self, paddle):
        pass
    # Needs to get the position of the paddle.
    # Compare paddle to 0.
    # less then zero set paddle start back to zero
    # If the paddle became more then 69 then reset back to 69