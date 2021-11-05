from game.action import Action

class DrawActorsAction(Action):
    """The role of this class is to draw the games various actors.

    Args:
        Action ([type]): The Action class

    Attributes: 
        output_service (Output_Service): An instance of Output_Service()
    """

    def __init__(self, output_service):
        """The class constructor

        Args:
            output_service (Output_Service): An instance of Output_Service
        """

        self._output_service = output_service

    def execute(self, cast):
        """The purpose of this function is to draw the various actors on the screen.

        Args:
            cast (list): The list of actors.
        """

        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()