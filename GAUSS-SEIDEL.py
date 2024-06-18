from Admittancematrix import Admittance_matrix
class GAUSS_SEIDEL:
    def __innit():
        pass
    def initializers(self):
        while True:
            try:
                no_of_iter = int(input("How many iterations do you want to perform? "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        while True:
            slack_bus_voltage = input("Compute the slack bus voltage (in the form a±bi): ")
            try:
                slack_bus_voltage = complex(slack_bus_voltage)
                break
            except ValueError:
                if "i" in slack_bus_voltage:
                    try:
                        slack_bus_voltage = complex(slack_bus_voltage.replace("i", "j"))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid complex number.")
                else:
                    print("Invalid input. Please enter a valid complex number.")
        
        return no_of_iter, slack_bus_voltage
    

        
    def power_values(self,n):
        power_values={}
        for iters in range(2,n+1):
            Power_buses_name=f'Bus {iters}'
            Power_bus_values=input(f'Compute the power at {Power_buses_name} (Should be in the form 0±0j): ')
            try:
                Power_bus_values=complex(Power_bus_values)
            except:
                if "i" in Power_bus_values:
                    Power_bus_values=complex(Power_bus_values.replace("i","j"))
            power_values[Power_buses_name]=Power_bus_values
        return power_values
    
    def Voltage_values(self,n):
        voltage_values={}
        for iters in range(2,n+1):
            voltage_buses_name=f'Bus {iters}'
            voltage_bus_values=input(f'Compute the Voltage at {voltage_buses_name} (Should be in the form 0±0j): ')
            try:
                voltage_bus_values=complex(voltage_bus_values)
            except:
                if "i" in voltage_bus_values:
                    Power_bus_values=complex(Power_bus_values.replace("i","j"))
            voltage_values[voltage_buses_name]=voltage_bus_values
        return voltage_values
    
    def iterations(self, number_of_buses, matrix, slack_bus_voltage, power_values,no_of_iter,voltage_values):
        Voltage_data = {}
        power_value=list(power_values.values())
        voltage_value=list(voltage_values.values())
    
        # Assuming necessary data structures and variables are already defined:
# no_of_iter, number_of_buses, voltage_value, matrix, power_value, slack_bus_voltage, voltage_data, Voltage_data

        for iteration in range(1, no_of_iter + 1):
            for bus_name in range(2, number_of_buses + 1):
                remaining = 0
                
                for iter in range(1,number_of_buses):
                    for voltage in voltage_value:
                        matrix[1][iter] *= voltage  # Assuming an operation with voltage here
                        remaining -= remaining  # This line doesn't make sense and seems to reset remaining to 0 every time
                
                # Calculate the voltage values
                real_voltage_value = voltage_value[iter-1]  # This should be defined outside the nested loops
                ax = 1 / matrix[1][iter]  # Matrix inversion or a similar operation
                ay = power_value[iter-1] / real_voltage_value  # Power value calculation
                az = matrix[1][iter-1] * slack_bus_voltage  # Some operation with slack bus voltage
                
                main_voltage = ax * (ay - az - remaining)  # Final voltage calculation
                Voltage_data[main_voltage] = main_voltage  # Storing the calculated voltage
        
                Voltage_data[f'Voltage at bus {bus_name} at iteration {iteration}'] = main_voltage  # Store the result with a descriptive key

                        
                    
                            

                        
                            
                            
                            
                        

        return Voltage_data

    


    

            
# Create an instance of the Admittance_matrix class
admittance_obj = Admittance_matrix()

# Call the gathering_admittances method to get bus and line data
bus_data, line_data = admittance_obj.gathering_admittances()

# Call the solve_admittance method to get total bus data
total_bus_data = admittance_obj.solve_admittance(bus_data, line_data)

# Call the creating_matrix method to get the admittance matrix
admittance_matrix = admittance_obj.creating_matrix(total_bus_data, line_data)

# Create an instance of the GAUSS_SEIDEL class
gauss_seidel_obj = GAUSS_SEIDEL()

# Call the initializers method to get the number of iterations and slack bus voltage
no_of_iter, slack_bus_voltage = gauss_seidel_obj.initializers()

# Call the power_values method to get the power values
power_values = gauss_seidel_obj.power_values(admittance_obj.number_of_buses)
voltage_values = gauss_seidel_obj.Voltage_values(admittance_obj.number_of_buses)

# Call the iterations method to get the voltage data
voltage_data = gauss_seidel_obj.iterations(admittance_obj.number_of_buses, admittance_matrix,
                                            slack_bus_voltage, power_values,no_of_iter,voltage_values)

# Print the voltage data
print(voltage_data)