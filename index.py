class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]


class Company:  # but install
    total_bus = 5
    total_bus_lst = []  # dummy database

    def install(self):
        bus_no = int(input("Enter Bus No: "))
        flag = 1
        for bus in self.total_bus_lst:  # checking any bus already installed or not
            if bus_no == bus['coach']:
                print("Bus already installed!")
                flag = 0
                break
        if flag:
            bus_driver = input("Enter Bus Driver Name: ")
            bus_arrival = input("Enter Bus Arrival Time: ")
            bus_departure = input("Enter Bus Departure Time: ")
            bus_from = input("Enter Bus Start From: ")
            bus_to = input("Enter Bus Destination To: ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival,
                               bus_departure, bus_from, bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print("\nBus installed successfully!\n")


class BusCounter(Company):  # for user or counter officer
    user_lst = []  # user database
    bus_seat = 20

    def reservation(self):
        bus_no = int(input("Enter Bus Number: "))
        flag = 0
        for bus in self.total_bus_lst:
            if bus_no == bus['coach']:
                passenger = input("Enter Your Name: ")
                seat_no = int(input("Enter Your Wanted Seat Number: "))
                if seat_no-1 > self.bus_seat:
                    print("Only 20 seats are available!")
                elif bus['seat'][seat_no-1] != "Empty":
                    print("Seat already booked!")
                else:
                    bus['seat'][seat_no-1] = passenger
                flag = 1
        if flag == 0:
            print("This bus is not available in our company!")

    def showBusInfo(self):
        bus_no = int(input("Enter Bus No: "))
        for bus in self.total_bus_lst:
            if bus['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} Bus Info {'#'*10}")
                print(f"Bus Number: {bus_no} \t\t Driver: {bus['driver']}")
                print(
                    f"Arrival: {bus['arrival']} \t\t Departure: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\t To: {bus['to']}")
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()

    def get_users(self):
        return self.user_lst

    def get_users_info(self):
        print('*'*50)
        print()
        print(f"{' '*10} {'#'*10} User Info {'#'*10}")
        for user in self.user_lst:
            print(f"User: {user.username} \t Password: {user.password}")

    def create_account(self):
        name = input("Enter your name: ")
        flag = 0
        for user in self.get_users():
            if user['username'] == name:
                print("Username already exists!")
                flag = 1
                break
        if flag == 0:
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Account Created Successfully!")

    def available_buses(self):
        if len(self.total_bus_lst) == 0:
            print("No Bus Available!")
        else:
            for bus in self.total_bus_lst:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} Bus Info {'#'*10}")
                print()
                print(
                    f"Bus Number: {bus['coach']} \t\t Driver: {bus['driver']}")
                print(
                    f"Arrival: {bus['arrival']} \t\t Departure: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\t To: {bus['to']}")
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()
                print()


""" 
1. create an account -> create_new_account()
2. login to your account -> authentic user
                            -> 1. Available buses
                            -> 2. Reservation 
                            -> 3. Show bus info
                         -> administrator (admin, 123)
                            -> 1. Install Buses
                            -> 2. See available buses
                            -> 3. See total user list
3. exit 
"""

while True:
    counter = BusCounter()
    print("1. Create an account \n2. Login to your account \n3. Exit")
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        isAdmin = False
        flag = 0
        if name == "admin" and password == "123":
            isAdmin = True
        if isAdmin == False:    # normal user/customer
            for user in counter.get_users():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(
                        f"1. Available busses \n2. Show bus info \n3. Reservation \n4. Exit")
                    a = int(input("Enter your choice: "))
                    if a == 1:
                        counter.available_buses()
                    elif a == 2:
                        counter.showBusInfo()
                    elif a == 3:
                        counter.reservation()
                    else:
                        break
            else:
                print("This user is not exists!")
        else:
            while True:
                print("Hello Admin, welcome back!")
                print(
                    "1. Install bus \n2. Available buses \n3. Show bus \n4. Show user list \n5. Exit")
                a = int(input("Enter your choice: "))
                if a == 1:
                    counter.install()
                elif a == 2:
                    counter.available_buses()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    counter.get_users_info()

                else:
                    break
    elif user_input == 3:
        break
