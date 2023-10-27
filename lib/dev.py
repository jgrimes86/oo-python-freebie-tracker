from .freebie import Freebie

class Dev:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Dev name={self.name}>"

    @property
    def freebies(self):
        return [freebie for freebie in Freebie.all if freebie.dev == self]

    @property
    def companies(self):
        company_list = []
        for freebie in self.freebies:
            if freebie.company not in company_list:
                company_list.append(freebie.company)
        return company_list
    
    def received_one(self, item_name):
        dev_items = [freebie.item_name for freebie in self.freebies]
        if item_name in dev_items:
            return True
        else:
            return False

    def give_away(self, new_dev, freebie_string):
        if freebie_string in [freebie.item_name for freebie in self.freebies]:
            gift = [freebie for freebie in self.freebies if freebie.item_name == freebie_string]
            gift[0].dev = new_dev
        else:
            return "That freebie doesn't belong to you."
