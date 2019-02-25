# from common.exceptions import EntityDoesNotExist
# from .models import ORMProduct
# from .entities import Product


# class ProductDatabaseRepo(object):

#     def get_product(self, reference):
#         try:
#             orm_product = ORMProduct.objects \
#                                       .get(reference=reference)
#         except ORMProduct.DoesNotExist:
#             raise EntityDoesNotExist()

#         return self._decode_orm_product(orm_product)

#     def _decode_orm_product(self, orm_product):
#         return Product(reference=orm_product.reference,
#                       brand_id=orm_product.brand_id)


from .models import Ticket
from ..common.exceptions import EntityDoesNotExist


class TicketDBRepository:

    def get_find_by_id(self, identify: int):
        try:
            orm_ticket = Ticket.objects.get(id=identify)
        except Ticket.DoesNotExist as e:
            raise EntityDoesNotExist

        return self.decode_orm_ticket(orm_ticket)

    def decode_orm_ticket(self, orm_ticket):
        return []
        # return Product(reference=orm_product.reference,
        #               brand_id=orm_product.brand_id)

# Ticket