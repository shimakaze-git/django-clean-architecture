# class ProductRepo(object):

#     def __init__(self, db_repo, cache_repo):
#         self.db_repo = db_repo
#         self.cache_repo = cache_repo

#     def get_product(self, reference):
#         product = self.cache_repo.get_product(reference)

#         if product is None:
#             product = self.db_repo.get_product(reference)
#             self.cache_repo.save_product(product)

#         return product


class TicketRepo:

    def __init__(self, db_repo):
        self.__db_repo = db_repo

    def get_ticket(self, identify: int):
        # return self.__db_repo
        ticket = self.__db_repo.get_find_by_id(identify=identify)
        return ticket

    def get_tickets(self):
        tickets = self.__db_repo.get_find()
        return tickets
