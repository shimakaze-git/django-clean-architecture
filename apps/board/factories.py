from .datastore import TicketDBRepository
from .repositories import TicketRepo
from .use_case import GetTicketInteractor, GetAllTicketInteractor
from .views import TicketView


""" infrastructure Factory"""

class TicketDataBaseRepoFactory:
    
	@staticmethod
	def get():
		return TicketDBRepository()


class TicketRepoFactory:

    @staticmethod
    def get():
        db_repo = TicketDataBaseRepoFactory.get()
        return TicketRepo(db_repo)










""" GET Request """
class GetAllTicketInteractorFactory(object):

    @staticmethod
    def get():
        ticket_repo = TicketRepoFactory.get()
        return GetAllTicketInteractor(ticket_repo)


class GetAllTicketViewFactory:
    @staticmethod
    def create():
        get_ticket_interactor = GetAllTicketInteractorFactory.get()
        return TicketView(get_ticket_interactor)


class GetTicketInteractorFactory(object):

    @staticmethod
    def get():
        ticket_repo = TicketRepoFactory.get()
        return GetTicketInteractor(ticket_repo)


class GetTicketViewFactory:

    @staticmethod
    def create():
        get_ticket_interactor = GetTicketInteractorFactory.get()
        return TicketView(get_ticket_interactor)
