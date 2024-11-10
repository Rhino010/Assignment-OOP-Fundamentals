"""

Task 2: Event Management System Enhancement

- Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

- Code Example: Basic Event class without participant tracking.

    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
"""
events = {}

class Event:
    # Everything in the __init__ constructor is required in the class.
    def __init__(self, event_name, date):
        self.event_name = event_name
        self.date = date
        # This empty list will take participant names for each instance of the class.
        self.participants = []
    
    def add_participant(self,participant_names):
        # This will append names to self.participants specifically as a value to the dictionary key[event]
        self.participants.append(participant_names)
        

    def get_participant_count(self):
        count = len(self.participants)
        print(f"The total participants in this event are {count}")

def main():


    while True:

        
        choice = input("Please type the number of the option you would like, '1': Enter New Event, '2': Add Participant(s) to an Event, '3': Show Event Particpant Count, '4': Exit Program.\n")
        
        if choice == '1':
            
            new_event = input("Please enter the new event name.\n")
            event_date = input("Please enter the event date.\n")
            event_people = input("Please enter participants attending the event separated by commas (ex. Jane, Donna).\n")
            events[new_event] = Event(new_event, event_date)
    
        
        elif choice == '2':
            event_name = input("Please type the name of the event you wish to add participants for.\n")
            if event_name in events:
                event_people = input("Please type the people you would like to add to the event separated by commas (ex. Jim, John).\n")

            else:
                print("Event not found.")

        elif choice == '3':
            event_name = input("Which event would you like the participant count for?\n")
            if event_name in events:
                events[event_name] = event.get_participant_count()
            else:
                print("Event not found.")
            print(events)


        elif choice == '4':
            print("Exiting now.....")
            break

if __name__ == '__main__':
    main()