from django.http import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_view(request):
    visit_count = request.session.get("visit_count", 0)
    visit_count += 1
    response = HttpResponse(f"This is just an Hello!. view count={visit_count}")
    request.session["visit_count"] = visit_count
    response.set_cookie('dj4e_cookie', '561e7e7d', max_age=1000)
    return response