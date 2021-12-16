import socket
 
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
        print("The Jenkins server date when have been pushed code ") 
    except:
        print("Unable to get Hostname and IP")
 
get_Host_name_IP() 
