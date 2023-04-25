import time

def bandwidth_calc():
    bandwidth = float(input("Enter bandwidth in Mbps: "))
    latency = float(input("Enter latency in ms: "))
    data_size = float(input("Enter data size in MB: "))

    # Calculate maximum data transfer rate
    max_data_rate = bandwidth * 1000 / 8   # Convert Mbps to Kbps

    # Calculate time taken to transfer data
    transfer_time = (data_size * 1024 * 1024 * 8) / (max_data_rate * 1000)   # Convert MB to bits

    # Add latency to transfer time
    total_transfer_time = transfer_time + latency / 1000

    # Convert transfer time to minutes and seconds
    minutes, seconds = divmod(total_transfer_time, 60)

    # Print out the results
    print("Maximum data transfer rate: {:.2f} Kbps".format(max_data_rate))
    print("Time taken to transfer {:.2f} MB of data: {:.0f} minutes {:.0f} seconds".format(data_size, minutes, seconds))

if __name__ == "__main__":
    bandwidth_calc()
