'''
House and thief problem. Assume circular colony
TBD: Fix accessible value which set for -1 index, to consider as a sigle line colony

Author: Milton S
'''

class Colony(object):

    def __init__(self, position, money, looted=False, accessible=True):
        self.position : int = position
        self.money : int =  money
        self.looted : bool = looted
        self.accessible : bool = accessible

    def __str__(self):
        return f'house{self.position} with {self.money}dollar'

h1 = Colony(0, 26)
h2 = Colony(1, 7)
h3 = Colony(2, 11)
h4 = Colony(3, 25)
# h5 = Colony(4, 10)
# h6 = Colony(5, 100)

colony = [h1, h2, h3, h4]
# colony = [h1, h2, h3, h4, h5, h6]

def find_max(colony):
    max = 0
    for n in colony:
        # print(n.money)
        try:
            if n.money > max and not n.looted and n.accessible:
                max = n
        except TypeError:
            if n.money > max.money and not n.looted and n.accessible:
                max = n
    return max

def loot(colony):
    max = find_max(colony)
    if max != 0:
        max.looted = True
        try:
            colony[max.position - 1].accessible = False
            colony[max.position + 1].accessible = False
        except IndexError:
            pass
        return max


if __name__ == '__main__':
    loots = []
    for i in range(0,3):
        loots.append(loot(colony))
    print([n.money for n in loots if isinstance(n, Colony)])
