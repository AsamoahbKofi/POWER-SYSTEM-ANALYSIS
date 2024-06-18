import numpy as np

class Admittance_matrix:
    def __init__(self):
        pass

    def gathering_admittances(self):
        while True:
            try:
                self.number_of_buses = int(input("How many buses are in the system? "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        buses_data = {}
        for x in range(1, self.number_of_buses+1):
            bus_name = f'Bus {x}'
            admittance = input(f'Compute the admittance at {bus_name}: ')
            try:
                admittance=complex(admittance)
            except:
                if "i" in admittance:
                    admittance=complex(admittance.replace("i","j"))
            buses_data[bus_name] = admittance

        line_data = {}
        for i in range(self.number_of_buses):
            for j in range(i+1, self.number_of_buses):
                line_name = f"Line {i+1} to {j+1}"
                try:
                    admittances = input(f"Compute the admittance of {line_name}: ")
                    admittances=complex(admittances)
                except:
                    if "i" in admittances:
                        admittances=complex(admittances.replace("i","j"))
                line_data[line_name] = admittances

        buses_data.update(line_data)
        return buses_data, line_data

    def solve_admittance(self, Admittance_info, line_data):
        total_bus_data = {}

        for i in range(1, self.number_of_buses+1):  # Use the saved number of buses
            total_bus_name = f'Total bus at bus {i}'
            total_bus_value =  0 + 0j
            for bus, admittance in Admittance_info.items():
                if str(i) in bus:
                    total_bus_value += admittance
            total_bus_data[total_bus_name] = total_bus_value

        total_bus_data.update(line_data)
        return total_bus_data
    
    def creating_matrix(self,total_bus_data,line_data):
        matrix=np.zeros((self.number_of_buses,self.number_of_buses),dtype=complex)  # Use the saved number of buses

        for i, (bus_name, admittance) in enumerate(total_bus_data.items()):
            if bus_name.startswith('Total'):
                matrix[i][i] = admittance

        for line_name, admittance in line_data.items():
            bus1, bus2 = line_name.split(" to ")
            i = int(bus1.split(" ")[1]) - 1
            j = int(bus2) - 1
            matrix[i][j] = -admittance
            matrix[j][i] = -admittance  # Since the matrix is symmetric
    
        return matrix

admittance_obj = Admittance_matrix()

# Call the gathering_admittances method to get bus and line data

