from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    # /
    path('', views.IndexView.as_view(), name ="index"),

    # /add
    path('add', views.ExpenseCreate.as_view(), name="create_expense"),

    # /update/{id}
    path('update/<int:pk>', views.ExpenseUpdate.as_view(), name="update_expense"),

    # /delete/{id}
    path('delete/<int:pk>', views.ExpenseDelete.as_view(), name="delete_expense"),

    # /analysis
    path('analysis', views.AnalysisView.as_view(), name="analysis")
]