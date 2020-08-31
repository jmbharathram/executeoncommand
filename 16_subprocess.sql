subprocess.run("echo 'Hello World'", shell=True)

output = subprocess.run("echo 'Hello World'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

print(output)
print(output.stdout)

output = subprocess.run("echo Hello World", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

print(output)

output = subprocess.run("echo 'Hello World", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

print(output)

from subprocess import Popen

p = Popen(["sleep","5"])
#p.wait()

from subprocess import Popen,PIPE

p1 = Popen(["ls","-1"], stdout=PIPE)
p2 = Popen(["grep", "subprocess"], stdin=p1.stdout, stdout=PIPE, universal_newlines=True)
output = p2.stdout.readline()
print(output)
p1.stdout.close()

output, error = p2.communicate()
print(output)

###

process = subprocess.Popen(['ping', '-c 4', 'python.org'], 
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output)
    
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
         
        for output in process.stdout.readlines():
            print(output)
        break


proc = subprocess.Popen(['ping', '-c 5', 'google.com'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

try:
    outs, _ = proc.communicate(timeout=10)
    print('RETURN CODE', proc.returncode)
    print(outs.decode('utf-8'))
except subprocess.TimeoutExpired:
    print('subprocess did not terminate in time')	
    proc.terminate()	
