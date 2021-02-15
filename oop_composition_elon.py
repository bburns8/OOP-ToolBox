class Elon:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def revenue(self):
        return f'My name is {self.name} and I am {self.age} years old.'


class Tesla:
    def __init__(self, model_s, model_x, model_3, roadster, cybertruck):
        self.model_s = model_s
        self.model_x = model_x
        self.model_3 = model_3
        self.roadster = roadster
        self.cybertruck = cybertruck

    def manufactured(self):
        return f'Tesla has now manufactured the {self.model_s},' \
               f' {self.model_x},' \
               f' {self.model_3},' \
               f' {self.roadster},' \
               f' and the {self.cybertruck}.'
    def


class SpaceX:
    def __init__(self, falcon_9, falcon_heavy, falcon_heavy_block, dragon):
        self.falcon_9 = falcon_9
        self.falcon_heavy = falcon_heavy
        self.falcon_heavy_block = falcon_heavy_block
        self.dragon = dragon

    def launched(self):
        return f'SpaceX has successfully launched and re-landed four different rockets including the ' \
               f'{self.falcon_9}, ' \
               f'{self.falcon_heavy}, ' \
               f'{self.falcon_heavy_block}, ' \
               f'and the {self.dragon}.'


class BoringCompany:
    def __init__(self, hyperloop, flamethrower):
        self.hyperloop = hyperloop
        self.flamethrower = flamethrower

    def travel(self):
        return f'The Boring Company has sold 20,000 of their Not-A-{self.flamethrower}' \
               f' as well as digging tunnels for their {self.hyperloop} project.'


elon = Elon('Elon Musk', 49)
tesla = Tesla('Model-S', 'Model-X', 'Model-3', 'Roadster', 'Cybertruck')
spacex = SpaceX('Falcon-9', 'Falcon-Heavy', 'Falcon-Heavy-Block', 'Dragon')
boring = BoringCompany('Hyperloop', 'Flamethrower')
print(elon.revenue())
print(tesla.manufactured())
print(spacex.launched())
print(boring.travel())
