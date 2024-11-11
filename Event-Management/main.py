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


class Event:
    # Everything in the __init__ constructor is required in the class.
    def __init__(self, event_name, date):
        self.event_name = event_name
        self.date = date
        # This empty list will take participant names for each instance of the class.
        self.participants = []
    
    def add_participant(self,participant_name):
        # This will append names to self.participants specifically as a value to the dictionary key[event]
        self.participants.append(participant_name)
        

    def get_participant_count(self):
        count = len(self.participants)
        return count

def main():
    events = {}

    while True:

        
        choice = input("Please type the number of the option you would like, '1': Enter New Event, '2': Add Participant(s) to an Event, '3': Show Event Particpant Count, '4': Exit Program.\n")
        
        if choice == '1':
            
            new_event_name = input("Please enter the new event name.\n")
            event_date = input("Please enter the event date.\n")
            events[new_event_name] = Event(new_event_name, event_date)
            print(events[new_event_name].event_name)
        
        elif choice == '2':
            event_name = input("Please type the name of the event you wish to add participants for.\n")
            if event_name in events:
                participant_name = input("Please type the name you would like to add.\n")
                events[event_name].add_participant(participant_name)
                print(f"Participant {participant_name} has been added.")
            else:
                print("Event not found.")

        elif choice == '3':
            event_name = input("Which event would you like the participant count for?\n")
            if event_name in events:
                print(f"The total people registered to attend this event is: {events[event_name].get_participant_count()}")
            else:
                print("Event not found.")


        elif choice == '4':
            print("Exiting now.....")
            break

if __name__ == '__main__':
    main()