
class GetTicketInteractor:

    def __init__(self, board_repository):
        self.__identify = None

        self.board_repository = board_repository

    def set_params(self, identify: int):
        self.__identify = identify
        return self

    def execute(self):
        return self.board_repository.get_ticket(
            identify=self.__identify
        )


class GetAllTicketInteractor:

    def __init__(self, board_repository):
        # self.__identify = None

        self.board_repository = board_repository

    def set_params(self):
        # self.__identify = identify
        return self

    def execute(self):
        return self.board_repository.get_tickets()
