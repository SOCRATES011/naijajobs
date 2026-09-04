from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Group, Member, Expense, Share
from .serializers import GroupSerializer, ExpenseSerializer
from rest_framework import viewsets, permissions

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required
def index(request):
    groups = Group.objects.filter(members__user=request.user).distinct()
    return render(request, 'expenses/group_list.html', {'groups': groups})

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, 'expenses/group_detail.html', {'group': group})

@login_required
def create_expense(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        paid_by_id = request.POST.get('paid_by')
        paid_by = group.members.filter(id=paid_by_id).first()
        expense = Expense.objects.create(group=group, created_by=request.user, title=title, amount=amount, paid_by=paid_by, date=request.POST.get('date'))
        # naive equal split
        members = list(group.members.all())
        per = float(amount)/len(members)
        for m in members:
            Share.objects.create(expense=expense, member=m, share_amount=per)
        return redirect('group_detail', group_id=group.id)
    return render(request, 'expenses/expense_form.html', {'group': group})
