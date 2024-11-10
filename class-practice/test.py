events = {}


class Events:
    def __init__(self, name, location, date):
        self.name = name
        self.location = location
        self.date = date
        self.participants = []
    
    def add_participants(self, participant_names):
        separated = participant_names.split(',')
        for person in separated:
            self.participants.append(person)

def main():

    people = input("Please enter the names of the participants separated by commas (ex. janey, johnny, jimmy).")
    for person in people:
        Events.add_participants(person)
    
    print(Events.participant_names)


if __name__ == "__main__":
    main()