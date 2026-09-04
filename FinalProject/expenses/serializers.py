from rest_framework import serializers
from .models import Group, Member, Expense, Share, Settlement
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name']

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Member
        fields = ['id','display_name','email','role','user']

class ShareSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    class Meta:
        model = Share
        fields = ['id','member','share_amount','share_percent','is_paid_back']

class ExpenseSerializer(serializers.ModelSerializer):
    shares = ShareSerializer(many=True, read_only=True)
    class Meta:
        model = Expense
        fields = ['id','title','description','amount','currency','paid_by','date','shares']

class GroupSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['id','name','description','currency','owner','members']

class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = ['id','group','from_member','to_member','amount','date','method']
