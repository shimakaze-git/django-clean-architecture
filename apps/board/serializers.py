
class TicketSerializer(object):

    @staticmethod
    def serialize(tickets):

        res_tickets = []
        for ticket in tickets:
            res_tickets.append({
                'identify': ticket.identify,
                'description': ticket.description,
                'status': ticket.status,
                'assignee': ticket.assignee,
                'start': ticket.start,
                'end': ticket.end
            })
        print(res_tickets)

        return res_tickets
        # return []
