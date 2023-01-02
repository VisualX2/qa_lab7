import paramiko
import subprocess
import pytest

server_ip = "10.0.0.11"
password = "123"
username = "tluna"


@pytest.fixture(scope="function")
def server():
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=server_ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False
    )
    stdin,stdout,stderr = cl.exec_command("iperf -s")
    cl.close()



@pytest.fixture(scope="function")
def client():
    process = subprocess.Popen(["iperf", "-c", server_ip,"-f","m","-i", "0.5", "-t", "10"], encoding = 'utf-8',stdout=subprocess.PIPE)
    result_dict=[]
    while True:
        output = process.stdout.readline()
        result_dict.append(output)
        if output == '':
            rc = process.poll()
            if rc is not None:
                break
        rc = process.poll()
    output, error = process.communicate()
    return result_dict, error


