from schedule import  Schedule

def main():
   schedule = Schedule()
   schedule.load_from_csv('courses.csv')

   while True:
       print("\nCourse Schedule System Menu:")
       print("1. Display all courses")
       print("2. Search courses by subject")
       print("3. Search by subject and catalog")
       print("4. Search courses by instructor last name")
       print("5. Quit")

       choice = input("Enter your choice (1-5): ")

       if choice == "1":
           schedule.print()

       elif choice == "2":
           subject = input("Enter the subject: ")
           results = schedule.find_by_subject(subject)
           if results:
               schedule.print_header()
               for item in results:
                   item.print()

           else:
               print("No courses found for the given subject.")

       elif choice == "3":
            subject = input("Enter subject: ")
            catalog = input("Enter catalog: ")
            results = schedule.find_by_subject_catalog(subject, catalog)
            if results:
                schedule.print_header()
                for item in results:
                    item.print()

            else:
                print("No courses found for the given subject and catalog.")

       elif choice == "4":
           last_name = input("Enter instructor's last name: ")
           results = schedule.find_by_instructor_last_name(last_name)
           if results:
               schedule.print_header()
               for item in results:
                   item.print()

           else:
               print("No courses found for the given instructor last name.")

       elif choice == "5":
           print("Exiting program.")
           break
       else: 
           print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
            
           