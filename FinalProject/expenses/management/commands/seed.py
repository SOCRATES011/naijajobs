from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from expenses.models import Group, Member, Expense, Share
from datetime import date

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed demo data'

    def handle(self, *args, **options):
        if User.objects.filter(username='alice').exists():
            self.stdout.write('Seed already applied')
            return
        alice = User.objects.create_user('alice', password='password')
        bob = User.objects.create_user('bob', password='password')
        carol = User.objects.create_user('carol', password='password')
        group = Group.objects.create(name='Apartment', owner=alice, description='Shared apt bills')
        ma = Member.objects.create(group=group, user=alice, display_name='Alice')
        mb = Member.objects.create(group=group, user=bob, display_name='Bob')
        mc = Member.objects.create(group=group, user=carol, display_name='Carol')
        e1 = Expense.objects.create(group=group, created_by=alice, title='Dinner', amount='90.00', paid_by=ma, date=date.today())
        Share.objects.create(expense=e1, member=ma, share_amount='30.00')
        Share.objects.create(expense=e1, member=mb, share_amount='30.00')
        Share.objects.create(expense=e1, member=mc, share_amount='30.00')
        self.stdout.write('Seeded demo data: users alice/bob/carol and one group')
