import calendar


class DVD:

    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int):
        creation_day, creation_month, creation_year = [int(x) for x in date.split('.')]
        creation_month = calendar.month_name[creation_month]

        return cls(name=name, _id=_id,
                   creation_year=creation_year, creation_month=creation_month,
                   age_restriction=age_restriction)

    def __repr__(self):
        text = (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
                f"has age restriction {self.age_restriction}. "
                f"Status: {('rented' if self.is_rented is True else 'not rented')}")

        return text
