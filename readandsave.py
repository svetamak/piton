def read_addresses(filename, used_addresses_filename):
    with open(used_addresses_filename, "r") as used_addresses_file:
        used_addresses = [line.strip() for line in used_addresses_file.readlines()]

    with open(filename, "r") as file:
        addresses = [line.strip() for line in file.readlines() if line.strip() not in used_addresses and not line.startswith("#")]
    return addresses
  
def save_used_address(used_addresses_filename, addresses_filename, address):
    with open(used_addresses_filename, "a") as file:
        file.write(f"{address}\n")

    with open(addresses_filename, "r") as file:
        addresses = [line.strip() for line in file.readlines()]

    addresses.remove(address)

    with open(addresses_filename, "w") as file:
        for addr in addresses:
            file.write(f"{addr}\n")
