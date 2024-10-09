#Task 1

class Vehicle:
      def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
      
      def update_owner(self, **kwargs):
           for registration, x in kwargs.items():
                setattr(self, registration, x)

change = Vehicle(99987, "SUV", "Mitch")
change.update_owner(owner = "Micah")
print(change.owner) 
           
           

#Task 2

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.party_list = []
        
        def add_participant(self, new_invitee):
             self.party_list.append(new_invitee)
             new_invitee += 1
             print(self.party_list)
        
        def get_participant_count(self):
             for x in self.party_list:
                  index = 0
                  print(index + 1 + ":" + x)