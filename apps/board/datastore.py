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


from .models import Ticket as TicketORM
from .entities import Ticket
from ..common.exceptions import EntityDoesNotExist


class TicketDBRepository:

    def get_find_by_id(self, identify: int):
        try:
            orm_ticket = TicketORM.objects.get(id=identify)
        except TicketORM.DoesNotExist as e:
            raise EntityDoesNotExist
        return self.decode_orm_ticket(orm_ticket)

    def get_find(self):
        try:
            orm_tickets = TicketORM.objects.all()
        except TicketORM.DoesNotExist as e:
            raise EntityDoesNotExist
        return self.decode_orm_tickets(orm_tickets)

    def decode_orm_ticket(self, orm_ticket_queryset):

        ticket = Ticket()
        ticket_entity = ticket.set_params(
            orm_ticket_queryset.id,
            orm_ticket_queryset.description,
            orm_ticket_queryset.status,
            str(orm_ticket_queryset.assignee) if orm_ticket_queryset.assignee else "null",
            str(orm_ticket_queryset.start.strftime('%Y/%m/%d')),
            str(orm_ticket_queryset.end.strftime('%Y/%m/%d'))
        )

        return [ticket_entity]

    def decode_orm_tickets(self, orm_ticket_queryset):
        tickets_list = []

        for orm_ticket in orm_ticket_queryset:
            ticket = Ticket()
            ticket_entity = ticket.set_params(
                orm_ticket.id,
                orm_ticket.description,
                orm_ticket.status,
                str(orm_ticket.assignee) if orm_ticket.assignee else "null",
                str(orm_ticket.start),
                str(orm_ticket.end)
            )
            tickets_list.append(ticket_entity)
        return tickets_list
