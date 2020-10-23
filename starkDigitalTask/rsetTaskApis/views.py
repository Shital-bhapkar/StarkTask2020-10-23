
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
import datetime
# Create your views here.

class home(APIView):
    def get(self, request, format=None):
        content= {"message":"Welcome to my project."}

        return Response(content)

class getDayPrimeInfoByYearDaY(APIView):
    def get(self, request, format=None):
        today = datetime.datetime.now()
        day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
        # prime number is always greater than 1
        if day_of_year > 1:
            for i in range(2, day_of_year):
                if (day_of_year % i) == 0:
                    content = {"date" : "Date is not prime so no date"}
                    break
            else:
                content = {"date": "Date is prime "}

        else:
            content = {"date" : "Date is not prime so no date"}

        return Response(content)

class getDayPrimeInfoByMonthDaY(APIView):
    def get(self, request, format=None):
        today = date.today()
        dayOfMonth = today.day
        # prime number is always greater than 1
        if dayOfMonth > 1:
            for i in range(2, dayOfMonth):
                if (dayOfMonth % i) == 0:
                    content = {"date": "Date is not prime so no date"}
                    break
            else:
                content = {"date": "Date is prime "}

        else:
            content = {"date": "Date is not prime so no date"}

        return Response(content)