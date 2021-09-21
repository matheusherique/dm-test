from rest_framework import serializers
from .models import Solicitation

class SolicitationSerializer(serializers.ModelSerializer):
    credit = serializers.SerializerMethodField(method_name='calculate_credit')
    
    class Meta : 
        model = Solicitation
        fields = "__all__"

    def calculate_credit(self, instance):
        request = self.context.get('request')
        user = request.user
        income = user.profile.income
        score = user.profile.score
        if(score <= 299):
            return 0
        elif(score >= 300 and score <= 599):
            return 1000.0
        elif(score >= 600 and score <= 799):
            if(income <= 2000.0):
                return 1000.0
            else:
                return income/2
        elif(score >= 800 and score <= 950):
            return income*2
        elif(score >= 951 and score <= 999):
            return 1000000.0

