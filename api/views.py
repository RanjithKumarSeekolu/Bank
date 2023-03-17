from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Bank import settings
from api.models import Bank, Branches
from api.serializers import BankSerializer, BranchSerializer
import pandas as pd


@api_view(['GET'])
def get_banks(request):
    if request.method == 'GET':
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many = True)
        return Response(serializer.data)



@api_view(['GET'])
def get_details(request, ifsc_code):
    if request.method == 'GET':
        branch = get_object_or_404(Branches.objects.select_related(), ifsc = ifsc_code)
        serializer = BranchSerializer(branch, many = False)
        return Response(serializer.data)

def fillBank():
    bank_data = pd.read_csv(f'{settings.BASE_DIR}/banks.csv', delimiter='\t')
    banks = []
    for i in range(len(bank_data)):
        banks.append(
            Bank(
                name=bank_data.iloc[i][0],
                id=bank_data.iloc[i][1]
            )
        )

    Bank.objects.bulk_create(banks)

def fillBranches():
    branches_data = pd.read_csv(f'{settings.BASE_DIR}/branches.csv', delimiter=',')
    branches = []
    for i in range(len(branches_data)):
        bank = Bank.objects.get(id=(int)(branches_data.iloc[i][1]))

        branches.append(
            Branches(
                ifsc = branches_data.iloc[i][0],
                bank_id = bank,
                branch = branches_data.iloc[i][2],
                address = branches_data.iloc[i][3],
                city = branches_data.iloc[i][4],
                district = branches_data.iloc[i][5],
                state = branches_data.iloc[i][6],
            )
        )
    
    Branches.objects.bulk_create(branches, 1000)

def home(request):
    return render(request,'api/home.html')

def setup(requeset):
    fillBank()
    fillBranches()
    return HttpResponse('database setup successful')