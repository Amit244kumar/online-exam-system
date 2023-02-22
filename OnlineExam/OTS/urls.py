from django.urls import path
from .views import *

urlpatterns=[
   path('new-question/',newQuestion),#html file
   path('save-question/',saveQuestion),#No html file
   path('view-questions/',viewQuestions),#html file
   path('edit-question/',editQuestion),#html file
   path('edit-save-question/',editSaveQuestion),#no html file
   path('delete-question/',deleteQuestion),#no html file
   path('sign-up/',signup),#html file
   path('save-user/',saveUser),#no html file
   path('login/',login),#html file
   path('login-validation/',loginValidation),#no html file
   path('logout/',logout),#no html file
   path('Home/',Home),#html file
   path('start-test/',startTest),#html file
   path('test-result/',testResult),#html file
   path('forgot-password/',forgotPassword),#html file
   path('new-passwrod-save/',newPasswordSave),#no html file
]
