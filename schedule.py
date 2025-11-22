import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.courses = {}

    def add_entry(self, item: ScheduleItem):
        self.courses[item.get_key()] = item

    def print_header(self):
        print(f"{'Subject':6} {'Catalog':6} {'Section':6} {'Component':10}"
              f"{'Session':6} {'Units':5} {'TotEnrl':7} {'CapEnrl':7} {'Instructor'}")
        print("-" * 80)

    def print(self):
        self.print_header()
        for item in self.courses.values():
            item.print()

    def find_by_subject(self, subject):
        return [item for item in self.courses.values() if item.subject.upper() == subject.upper()]

    def find_by_instructor_last_name(self, last_name):
        return [item for item in self.courses.values()
                if item.instructor.split()[-1].upper() == last_name.upper()]

    def load_from_csv(self, filename):
        with open(filename, encoding='utf-8-sig', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                   item = ScheduleItem(
                        subject=row['Subject'],
                        catalog=row['Catalog'],
                        section=row['Section'],
                        component=row['Component'],
                        session=row['Session'],
                        units=int(row['Units']),
                        tot_enrl=int(row['TotEnrl']),
                        cap_enrl=int(row['CapEnrl']),
                        instructor=row['Instructor']
                   )
                   self.add_entry(item)
                except ValueError:
                    continue
                 