class ScheduleItem:
    def __init__(self, subject, catalog, section, component, session, units, tot_enrl, cap_enrl, instructor):
        self.subject = subject.strip()
        self.catalog = catalog.strip()
        self.section = section.strip()
        self.component = component.strip()
        self.session = session.strip()
        self.units = units
        self.tot_enrl = tot_enrl
        self.cap_enrl = cap_enrl
        self.instructor = instructor.strip()
        
   
    def get_key(self):
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self):
        print(f"{self.subject:8} {self.catalog:8} {self.section:8}  {self.component:12}{self.session:8} {self.units:3} {self.tot_enrl:6} {self.cap_enrl:8}     {self.instructor:<15}")