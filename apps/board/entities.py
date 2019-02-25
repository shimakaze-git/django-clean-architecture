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

from datetime import date


class Ticket:
    def __init__(self):
        self._identify = None
        self._description = None
        self._status = None
        self._assignee = None
        self._start = None
        self._end = None

    def set_params(
        self,
        identify: int,
        description: str,
        status: str,
        assignee: int,
        start,
        end
    ):
        self._identify = identify
        self._description = description
        self._status = status
        self._assignee = assignee
        self._start = start
        self._end = end

        return self

    @property
    def identify(self):
        return self._identify

    @property
    def description(self):
        return self._description

    @property
    def status(self):
        return self._status

    @property
    def assignee(self):
        return self._assignee

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end
