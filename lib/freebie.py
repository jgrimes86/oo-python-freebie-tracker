
class Freebie:

    all = []

    def __init__(self, item_name, value, dev, company):
        self.item_name = item_name
        self.value = value
        self.dev = dev
        self.company = company
        Freebie.all.append(self)

    def __repr__(self):
        return f"<Freebie name={self.item_name}, value={self.value}>"

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"