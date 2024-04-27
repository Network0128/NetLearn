# Ubuntu To multiple switch
#접속 대상 장비들을 파일로 만들어서 반복문과 함께 실행하는 파이썬 자동화 코드를 완성하시오.
import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass("Enter your telnet password: ")

f = open('myswitches') #relative Path : 파일을 못찾는 경우 해당 파일이 있는 디렉터리로 이동 후 실행
#Absolute Path : f = open('/home/ubuntu/PythonHome/1.telnet/myswitches')

for IP in f:
    IP = IP.strip()
    print('Configuring Switch ' + IP)
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name Python_VLAN_4\n")
    tn.write(b"vlan 5\n")
    tn.write(b"name Python_VLAN_5\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
