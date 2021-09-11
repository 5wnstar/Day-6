import socket
def print_target_ip():
    target_url =str(input("Enter your target Url:"))
    ip_address = socket.gethostbyname(target_url)
    print ("Host name: ",  traget_url)
    print ("IP address: ",  ip_address)
 
if __name__ == '__main__':
    print_target_ip()
