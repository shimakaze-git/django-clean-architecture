from django.urls import path

from . import views
# from .factories import *
from .factories import GetTicketViewFactory, GetAllTicketViewFactory


app_name = 'board'
urlpatterns = [
    # ex: /
    # path('', views.BoardView.as_view(), name='index')
    path('', views.ViewWrapper.as_view(
        view_factory=GetAllTicketViewFactory)
    ),
    path('<int:identify>/', views.ViewWrapper.as_view(
        view_factory=GetTicketViewFactory)
    )

    # path('boards/<int:pk>/', views.board_topics, name='board_topics'),

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:id>', views.index_page, name='index_page'),
]
