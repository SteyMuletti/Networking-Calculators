import ipaddress

def subnet_calc():
    # Prompt the user to input an IP address and subnet mask.
    ip_address_str = input("Enter an IP address: ")
    subnet_mask_str = input("Enter a subnet mask: ")

    # Convert the IP address and subnet mask to IPNetwork objects.
    ip_network = ipaddress.IPv4Network(f"{ip_address_str}/{subnet_mask_str}", strict=False)
    network_address = str(ip_network.network_address)
    broadcast_address = str(ip_network.broadcast_address)
    num_hosts = ip_network.num_addresses - 2
    num_subnets = 2 ** (32 - ip_network.prefixlen)

    # Compute the network range in CIDR notation
    cidr_notation = f"{network_address}/{ip_network.prefixlen}"

    # Create a dictionary to store the results
    results = {
        "Network address": network_address,
        "Broadcast address": broadcast_address,
        "Number of hosts": num_hosts,
        "Number of subnets": num_subnets,
        "CIDR notation": cidr_notation,
    }

    # Print out the results.
    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    subnet_calc()
