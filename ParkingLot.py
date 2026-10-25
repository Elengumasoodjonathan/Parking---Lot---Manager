class ParkingLot:
    def __init__(self):
        self.parking_spaces = {
            'space 1': None,
            'space 2': 'CA 567 890',
            'space 3': None,
            'space 4': 'CC 123 456'
        }

    def find_empty_space(self):
        for spaces, cars in self.parking_spaces.items():
            if cars is None:
                return spaces

    def find_car_space(self, registration):
        for space, car in self.parking_spaces.items():
            self.registration = registration
            if registration == car:
                return space

    def remove_car(self):
        #while True:

            user = input('Registration of the car to remove: ')

            if user in self.parking_spaces.values():
                finder = self.find_car_space(user)
                self.parking_spaces[finder] = None
                print(f'{user} has been removed from the {finder}')
            else:
                print(f'{user} has not been parked here')

    def show_parked_car(self):
        for spaces, cars in self.parking_spaces.items():
            print('-', spaces, cars)

    def availible_parking_spot(self):
        availible = False

        for space, car in self.parking_spaces.items():
            if car is None:
                print(f'{space} is availible')
                availible = True
        if availible == False:
            print('There are no available space, the parking lot is unfortunately full')
            


    def park_car(self):

        #while True:

            user = input('Registration number here: ')

            empty_space = self.find_empty_space()

            
            if user in self.parking_spaces.values():
                    key = self.find_car_space(user)
                    print(f'{user} has already been parked here and you can find it by {key}.')
            else:
                
                if empty_space is None:
                    print('The parking lot is full')
                else:
                    self.parking_spaces[empty_space] = user
                    print(f'Your {user} has been parked at {empty_space}')




def main():
        parking = ParkingLot()
        while True:

            print('===========================')
            print('    PARKING LOT SYSTEM')
            print('===========================')
            print('')
            print('1. Park a car')
            print('2. Remove a car')
            print('3. Show parked cars')
            print('4. Show available spaces')
            print('5. Exit')

            my_user = input('Enter your choice here: ')

            if my_user == '1':
                parking.park_car()
            elif my_user == '2':
                parking.remove_car()
            elif my_user == '3':
                parking.show_parked_car()
            elif my_user == '4':
                parking.availible_parking_spot()
            elif my_user == '5':
                print('SYSTEM SHUTTING DOWN ...')
                break
            else:
                print('Invalid choice. Please choose 1-5.')
                
            



main()

# Display the menu - update        


        
