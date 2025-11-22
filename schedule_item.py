from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def get_key(self) -> str: 
        """Return unique key for dictionary storage: Subject_Catalog Section"""
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self):
        """Print formatted course details"""
        print(f"{self.subject:6} {self.catalog:6} {self.section:6} {self.component:10}"
              f"{self.session:6} {self.units:5} {self.tot_enrl:7} {self.cap_enrl:7}"
              f"{self.instructor}")