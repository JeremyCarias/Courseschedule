from schedule import Schedule
from schedule_item import ScheduleItem
from schedule import print_header
import csv

def main():
    schedule = Schedule()
    filename = "attached_assets/couces.csv"

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
                    units=int(row['Units']) if row['Units'] else 0,
                    tot_enrl=int(row['TotEnrl']) if row['TotEnrl'] else 0,
                    cap_enrl=int(row['CapEnrl']) if row['CapEnrl'] else 0,
                    instructor=row['Instructor']
                )
                schedule.add_entry(item)
            except Exception as e:
                continue


    while True:
        print("\nMenu:")
        print("1. Display all courses (BST)")
        print("2. Display all courses (AVL)")
        print("3. Search by subject")
        print("4. Search by subject and catalog")
        print("5. Search courses by instructor last name")
        print("6. Display tree heights")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            schedule.print(tree='bst')
        elif choice == '2':
            schedule.print(tree='avl')
        elif choice == '3':
            subject = input("Enter subject: ")
            result = schedule.find_by_subject(subject)
            print_header()
            for item in result:
                item.print()
        elif choice  == '4':
            subject = input("Enter subject: ")
            catalog = input("Enter catalog: ")
            result = schedule.find_by_subject_catalog(subject, catalog)
            print_header()
            for item in result:
                item.print()
        elif choice == '5':
            last_name = input("Enter instructor last name: ")
            result = schedule.find_by_instructor_last_name(last_name)
            print_header()
            for item in result:
                item.print()
        elif choice == '6':
            print(f"BST height: {schedule.bst.height()}")
            print(f"AVL height: {schedule.avl.height()}")
        elif choice == '7':
             break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()