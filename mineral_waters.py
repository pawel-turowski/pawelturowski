class MineralWater:


    def __init__(self, sodium, calcium):       #mg/l
        self.sodium = sodium
        self.calcium = calcium


    def __eq__(self, other):
        return (self.sodium == other.sodium and
                self.calcium == other.calcium)


    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return (self.sodium <= other.sodium and
                self.calcium <= other.calcium)

    def __lt__(self, other):
        return (self <= other and
                not self == other)

    def __gt__(self, other):
        return not self <= other


    def __ge__(self, other):
        return not self < other



staropolanka = MineralWater(32.50, 124)
nałęczowianka = MineralWater(10, 115)


print(f'staropolanka == nałęczowianka:{staropolanka == nałęczowianka}')
print(f'staropolanka != nałęczowianka:{staropolanka != nałęczowianka}')
print(f'staropolanka <= nałęczowianka:{staropolanka <= nałęczowianka}')
print(f'staropolanka < nałęczowianka:{staropolanka < nałęczowianka}')
print(f'staropolanka >= nałęczowianka:{staropolanka >= nałęczowianka}')
print(f'staropolanka > nałęczowianka:{staropolanka > nałęczowianka}')