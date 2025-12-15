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
        print(f"{self.subject:8} {self.catalog:8} {self.section:8} {self.component:12}"
              f"{self.session:8} {self.units:3} {self.tot_enrl:6} {self.cap_enrl:8}    {self.instructor:<15}")