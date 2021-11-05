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
  
     
        ball = cast["ball"][0]
        paddle = cast["paddle"][0]
        bricks = cast["brick"]
        marquee = cast["marquee"][0]
        self._handle_bricks()
        self._handle_paddle()
        self._handle_ball_constraints()
        self._handle_floor()
        self._handle_paddle_constraints()
        self._update_score(ball, bricks, marquee)
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                description = brick.get_description()
                ball.set_text(description)

    # Brian
    def _handle_paddle(self, paddle, ball):
        """This function checks to see if the ball quardanet is equal to the paddle. If it is then the ball velocity is reversed.

        Args:
                paddle and ball are in the cast dictionary with lists as their key.
        """

        for paddles in paddle:
            if ball.get_position().equals(paddles.get_position()):
                ball.set_velocity(Point.reverse)


    # Vanessa
    def _handle_bricks(self, bricks, ball):
        pass
        # Need to loop through each brick in bricks.
        # If the balls position is equal to bricks position, bounce ball and remove brick.

    # Brian
    def _handle_ball_constraints(self, ball):
        """
        This function determens if the ball hits the walls or ceiling and reverse the direction of the ball

        Args:
            ball ([dict]): ball is part of dictionary with a list for its key
        """

        if ball.get_position(Point.get_x()) <=  0 or  ball.get_position(Point.get_x()) >= constants.MAX_X:
            ball.set_velocity(Point.reverse_x())
        elif ball.get_position(Point.get_y())  >= 0 +1:
            ball.set_velocity(Point.reverse_y())



    # Brian
    def _handle_floor(self, ball):
        """This function determins if the ball falls below the paddle and the game is over.

        Args:
            ball ([dict]): ball is part of dictionary with a list for its key
        """
        if ball.get_position(Point.get_y()) >= constants.MAX_Y + 1:
            sys.exit()


    # Brian
    def _handle_paddle_constraints(self, paddle):
        pass
    # Needs to get the position of the paddle.
    # Compare paddle to 0.
    # less then zero set paddle start back to zero
    # If the paddle became more then 69 then reset back to 69

    def _update_score(self, ball, bricks, marquee):
        
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                points = brick.get_points()
                marquee.add_points(points)
                marquee.set_text(marquee.get_points())