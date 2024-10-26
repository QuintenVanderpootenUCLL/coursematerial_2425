# write your code here
def thanos(queue_size, target_size):
    amount_snaps = 0
    while queue_size > target_size:
        queue_size = queue_size // 2
        amount_snaps += 1
    return amount_snaps

