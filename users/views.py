from django.shortcuts import render
from django.http import HttpResponse


class Users:
    users = ["Antonio", 'Pepe', 'Juan', 'Vicente', 'Victor', 'Pedro']

    def index(request):
        users = ""
        for user in Users.users:
            users += user+", "
        users = users[0: len(users)-2]
        return HttpResponse(users)

    def user(request):
        id = request.GET['id']
        return HttpResponse(Users.users[int(id)])