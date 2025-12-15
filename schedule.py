import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.courses = {}

    def add_entry(self, item: ScheduleItem):
        self.courses[item.get_key()] = item

    def print_header(self):
        print(f"{'Subject':8} {'Catalog':8} {'Section':8} {'Component':12}"
              f"{'Session':8} {'Units':3} {'TotEnrl':6} {'CapEnrl':8} {'Instructor':<15}")
        print("-" * 80)

    def print(self):
        self.print_header()
        for item in self.courses.values():
            item.print()

    def find_by_subject(self, subject):
        return [item for item in self.courses.values() if item.subject.upper() == subject.upper()]

    def find_by_subject_catalog(self, subject, catalog):
        subject = subject.upper().strip()
        catalog = catalog.upper().strip()
        return [
            item for item in self.courses.values()
            if item.subject.upper().strip() == subject and item.catalog.upper().strip() == catalog
        ]


  
    def find_by_instructor_last_name(self, last_name):
        last_name = last_name.upper().strip()
        results = []

        for item in self.courses.values():
            if last_name in item.instructor.upper():
                results.append(item)

        return results
                                           
                                           
      

       
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
                 