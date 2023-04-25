import socket
import ipaddress

def main():
    while True:
        # Get the IP address and port range from the user.
        target = input("Enter an IP address, 'localhost' to scan your own machine, a network address (e.g. 192.168.1.0/24), or 'quit' to exit: ")
        
        # Check if the user wants to quit.
        if target.lower() == "quit":
            break
        
        # Check if the target is a network address.
        try:
            network = ipaddress.ip_network(target)
            print(f"Scanning network {network}")
        except ValueError:
            # Check if the target is the local machine.
            if target.lower() == "localhost":
                target = "127.0.0.1"
                print("Scanning local machine...")
            else:
                # Check if the target is a valid IP address.
                try:
                    socket.gethostbyaddr(target)
                except socket.herror:
                    print(f"The IP address {target} is not online. Please enter a valid IP address or network address.")
                    continue

                print(f"Scanning IP address {target}...")
                
            # Scan the specified ports.
            open_ports = []
            port_range = input("Enter a port range (e.g. 1-100) or 'all' to scan all ports: ")
            if port_range.lower() == "all":
                start_port = 1
                end_port = 65535
            else:
                # Split the port range into a start and end value.
                start_port, end_port = port_range.split("-")
                start_port = int(start_port)
                end_port = int(end_port)

            # Create a socket object.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set the socket to non-blocking mode.
            sock.setblocking(False)

            # Scan the specified ports.
            for port in range(start_port, end_port + 1):
                try:
                    sock.connect((target, port))
                    open_ports.append(port)
                    sock.close()
                except:
                    pass

            # Print the results.
            if len(open_ports) > 0:
                print(f"The following ports are open on {target}:")
                for port in open_ports:
                    print(port)
            else:
                print(f"No open ports were found on {target}.")
        else:
            # Scan the network for online hosts.
            online_hosts = []
            for host in network.hosts():
                try:
                    socket.gethostbyaddr(str(host))
                    online_hosts.append(str(host))
                except socket.herror:
                    pass

            # Print the results.
            if len(online_hosts) > 0:
                print(f"The following hosts are online on {network}:")
                for host in online_hosts:
                    print(host)
            else:
                print(f"No hosts were found on {network}.")

        # Ask the user if they want to scan another IP address.
        choice = input("Would you like to scan another IP address? (Y/N) ").lower()
        if choice != "y":
            break

if __name__ == "__main__":
    main()
