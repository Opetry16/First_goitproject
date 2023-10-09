def game(terra, power):
    total_energy = power  # Initialize total_energy with power

    # Iterate through each list in the outer list
    for energy_list in terra:
        # Iterate through each energy value in the current list
        for energy_value in energy_list:
            # If the energy_value can be absorbed, add it to total_energy and update total_energy
            if energy_value <= total_energy:
                total_energy += energy_value
            else:
                break  # If energy_value is greater than total_energy, stop and move to the next list

    return total_energy