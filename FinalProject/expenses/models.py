from django.db import models
from django.conf import settings
from decimal import Decimal

class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_groups')
    currency = models.CharField(max_length=3, default='USD')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField(blank=True)
    display_name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name

class Expense(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='expenses')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_expenses')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    paid_by = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name='paid_expenses')
    date = models.DateField()
    is_settled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.amount} {self.currency}"

    def total_shares(self):
        return sum([s.share_amount for s in self.shares.all()])

class Share(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='shares')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='shares')
    share_amount = models.DecimalField(max_digits=10, decimal_places=2)
    share_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    is_paid_back = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member} owes {self.share_amount}"

class Settlement(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='settlements')
    from_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='settlements_out')
    to_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='settlements_in')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.from_member} -> {self.to_member}: {self.amount}"
