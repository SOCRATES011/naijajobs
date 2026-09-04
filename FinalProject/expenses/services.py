from decimal import Decimal

def recalculate_group_balances(group):
    # returns dict {member_id: balance} where positive means others owe this member
    balances = {}
    for m in group.members.all():
        balances[m.id] = Decimal('0.00')
    for expense in group.expenses.all():
        payer = expense.paid_by
        if payer:
            balances[payer.id] += expense.amount
        for share in expense.shares.all():
            balances[share.member.id] -= share.share_amount
    return balances
