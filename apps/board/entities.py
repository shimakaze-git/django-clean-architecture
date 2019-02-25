# class Ticket(TimeStampedModel):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, default='')
#     status = models.SmallIntegerField(choices=TicketStatus.get_choices(), default=TicketStatus.ToDo.value)
#     assignee = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
#     start = models.DateField(null=True, blank=True)
#     end = models.DateField(null=True, blank=True)

# class Product(object):

#     def __init__(self, reference, brand_id):
#         self._reference = reference
#         self._brand_id = brand_id

#     @property
#     def reference(self):
#         return self._reference

#     @property
#     def brand_id(self):
#         return self._brand_id

    # def set_params(self, identify: int):
    #     self.__identify = identify
    #     return self


class Ticket:
    def __init__(self):
        self.__identify = None
        self.__description = None
        self.__status = None
        self.__assignee = None
        self.__start = None
        self.__end = None

    def set_params(
        self,
        identify: int,
        description: str,
        status: str,
        assignee: int
    ):
        self.__identify = identify
        self.__description = description
        self.__status = status
        return self

    @property
    def identify(self):
        return self.__identify
