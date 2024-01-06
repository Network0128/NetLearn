import pexpect  # pexpect 라이브러리 임포트

host = '10.1.1.21'  # 호스트 주소
username = 'ccnp'  # 사용자 이름
password = 'cisco'  # 비밀번호
tn = pexpect.spawn(f'telnet {host}')  # telnet 세션 생성

tn.expect('Username:')  # 사용자 이름 프롬프트 기다림
tn.sendline(username)  # 사용자 이름 전송
tn.expect('Password:')  # 비밀번호 프롬프트 기다림
tn.sendline(password)  # 비밀번호 전송
tn.expect('R1#')  # 커맨드 프롬프트 기다림

tn.sendline('show ip int br')  # 커맨드 전송
tn.expect('R1#')  # 커맨드 프롬프트 기다림
print(tn.before.decode('ascii'))  # 출력 결과 디코딩 후 출력

tn.sendline('exit')  # 종료 커맨드 전송
tn.close()  # 세션 종료


#pexpect 라이브러리를 사용하여 Telnet 세션을 생성하고, 사용자 이름과 비밀번호를 전송하며, 명령 'show ip int br'을 실행하고 그 결과를 출력한 후에 세션을 종료합니다.
