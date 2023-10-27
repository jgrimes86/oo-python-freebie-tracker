from .freebie import Freebie

class Company:

    all = []

    def __init__(self, name, founding_year):
        self.name = name
        self.founding_year = founding_year
        Company.all.append(self)
    
    def __repr__(self):
        return f"<Company name={self.name}, founding={self.founding_year}>"

    @property
    def freebies(self):
        return [freebie for freebie in Freebie.all if freebie.company == self]

    @property
    def devs(self):
        dev_list = []
        for freebie in self.freebies:
            if freebie.dev not in dev_list:
                dev_list.append(freebie.dev)
        return dev_list
    
    def give_freebie(self, dev, item_name, value):
        return Freebie(item_name, value, dev, self)

    @classmethod
    def oldest_company(cls):
        oldest_company = sorted(cls.all, key=lambda company: company.founding_year)
        return oldest_company[0]
        