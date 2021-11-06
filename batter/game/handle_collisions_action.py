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
        self._handle_bricks(bricks, ball, marquee)
        self._handle_paddle(paddle, ball)
        self._handle_ball_constraints(ball)
        self._handle_paddle_constraints(paddle)


    # Brian
    def _handle_paddle(self, paddle, ball):
        """This function loops through the paddle text's quadrants and the ball's quadrants to see if they are the same. If True the ball velocity is changed.

        Args:
            paddle (Actor): An instance of the Actor class.
            self (Handle_collisions_Action): An instance of Handle_Collisions_Action
            ball (Actor): is an instance of the Actor class
        """

        for i in range(0, len(paddle.get_text())):
            paddle_position = paddle.get_position().add(Point(i, 0))
            # if ball.get_position().equals(paddle_position):
            #     ball.set_velocity(ball.get_velocity().reverse())
            if ball.get_position().equals(paddle_position) and i < 5:
                ball.set_velocity(Point(-1,-1))
            elif ball.get_position().equals(paddle_position) and i > 5:
                ball.set_velocity(Point(1,-1))
            elif ball.get_position().equals(paddle_position) and i == 5:
                ball.set_velocity(Point(0,-1))

    # Vanessa
    def _handle_bricks(self, bricks, ball, marquee):
        """handle_brick first loops through all the bricks and if the ball touches a brick
        the brick is removed.
        Then the ball will get the velocity to a reverse  or reverse_y randomly to change ball  direction.

        Args:
            Self (instance): Is an instance of HandleCollisionsAction class.
            Brick (list):Is an instance of the brick list.
            Ball (instance): Is an instance of Actor.
            marquee (instance): Is an istance of Actor.

        """

        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                random_number = random.randint(1,10)
                bricks.remove(brick)
                self._update_score(brick, marquee)
                if random_number > 5:
                    ball.set_velocity(ball.get_velocity().reverse())
                else:
                    ball.set_velocity(ball.get_velocity().reverse_y())


    # Brian
    def _handle_ball_constraints(self, ball):
        """
        This function determines if the ball hits the walls,ceiling, or floor and reverse the direction of the ball or ends the game.

        Args:
            ball (Actor): is an instance of the Actor class
            self (Handle_collisions_Action): An instance of Handle_Collisions_Action
        """
        position = ball.get_position()
        x = position.get_x()
        y = position.get_y()
        if x ==  0 or x == constants.MAX_X:
            ball.set_velocity(ball.get_velocity().reverse_x())
        if y == 0:
            ball.set_velocity(ball.get_velocity().reverse_y())
        if y == constants.MAX_Y:
            sys.exit()


    # Brian
    def _handle_paddle_constraints(self, paddle):

        """This function keeps the paddle inside the walls of the game.

            Args:
                paddle (Actor): An instance of the Actor class.
                self (Handle_collisions_Action): An instance of Handle_Collisions_Action
        """
        position = paddle.get_position()
        x = position.get_x()

        if x < 0:
            paddle.set_position(Point(0, constants.MAX_Y - 1))
        if x > constants.MAX_X - len(paddle.get_text()):
            paddle.set_position(Point(constants.MAX_X - len(paddle.get_text()), constants.MAX_Y - 1))


    def _update_score(self, brick, marquee):
        """This function gets the point value from the brick and adds it to the score. Then sets value of points
            to the marquee.

            Args:
                marquee (Actor): marquee is an instance of Actor
                brick (Actor): brick is an instance of Actor
                points (integer): point value from Actor
        """
        points = brick.get_points()
        marquee.add_points(points)
        marquee.set_text(marquee.get_points())
