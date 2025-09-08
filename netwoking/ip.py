
import socket as a 
# following you get the your hostname
my_hostname = a.gethostname()
print("Hostname:", my_hostname)
# following you get the your ip address
my_ip = a.gethostbyname(my_hostname)
print("IP Address:", my_ip)

# following you get the ip address of any website
host = "www.yahoo.com"
ip = a.gethostbyname(host)

print('this is the ip address of', host, ip)

# Get port number of HTTP & HTTPS
print("HTTP Port:", a.getservbyname("http"))
print("HTTPS Port:", a.getservbyname("https"))

# Ask the port number and get where they belong to 
port = int(input("Enter a port number: "))
if port <= 1203:
    try:
        service = a.getservbyport(port)
        print(f"Port {port} belongs to: {service}")
    except OSError:
        print(f"Port {port} is not assigned to a standard service.")
else:
    print("Please enter a port number between 0 and 1203.") 