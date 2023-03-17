from rest_framework import serializers
from api.models import Bank, Branches


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank 
        fields = ['id', 'name']

class BranchSerializer(serializers.ModelSerializer):
    # bank_id = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    bank_id = BankSerializer()



    class Meta:
        model = Branches
        fields = ['ifsc', 'bank_id','branch','address','city','district','state',] 

