from rest_framework import serializers
from .models import Solicitation

class CreditSerializerField(serializers.Field):
    def to_representation(self, value):
         return value

    def to_internal_value(self, data):
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


class SolicitationSerializer(serializers.ModelSerializer):
    credit = CreditSerializerField()

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    class Meta : 
        model = Solicitation
        fields = "__all__"

    def create(self, validated_data):
        solicitation = Solicitation(
            credit=validated_data['credit'],
            fk_users=self.context['request'].user
        )
        solicitation.save()
        return solicitation

