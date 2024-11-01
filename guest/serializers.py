from rest_framework import serializers
from guest.models import   affiliates, annualreport, boardmembers, bylawtable, district, events, eventtype, institution, membershipsubscription, membershiptype, payment, signup, states

class stateSerializer(serializers.ModelSerializer):
    class Meta:
        model = states
        fields = '__all__'
class districtSerializer(serializers.ModelSerializer):
    state=stateSerializer()
    class Meta:
        model = district
        fields = '__all__'
class LawSerializer(serializers.ModelSerializer):
    class Meta:
        model = bylawtable
        fields = '__all__'
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = boardmembers
        fields = '__all__'
class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = institution
        fields = '__all__'
class AffiliatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = affiliates
        fields = '__all__'

class AnnualreportSerializer(serializers.ModelSerializer):
    class Meta:
        model = annualreport
        fields = '__all__'
class SignupSerializer(serializers.ModelSerializer):
    state=stateSerializer()
    district=districtSerializer()
    affiliation=AffiliatesSerializer()
    class Meta:
        model = signup
        fields = '__all__'
class MembershiptypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = membershiptype
        fields = '__all__'
class MembershipsubscriptionSerializer(serializers.ModelSerializer):
    membershiptype=MembershiptypeSerializer()
    class Meta:
        model = membershipsubscription
        fields = '__all__'
class EventtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = eventtype
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    state=stateSerializer()
    district=districtSerializer()
    eventtype=EventtypeSerializer()
    
    class Meta:
        model = events
        fields = '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    member=SignupSerializer()
    membershiptype=MembershiptypeSerializer()
    class Meta:
        model = payment
        fields = '__all__'