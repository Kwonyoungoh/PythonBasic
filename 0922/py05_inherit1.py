class Country:

    name = 'country'
    population = 'population'
    capital = 'capital'

    @classmethod
    def show(cls):
        print(f'{cls.name}, {cls.population}, {cls.capital}')

class Korea(Country):

    @classmethod
    def intro_Ctr(cls):
        super().show()

    @classmethod
    def set_name(cls,name):
        cls.name = name


a = Korea()
a.set_name('Korea')
a.intro_Ctr()
a.show()