import json

import pexpect # sudo pip3 install pexpect

p = None # the executable process
expect = None # the regex that finds end of input

def create(app):
    global p
    print(app)
    p = pexpect.spawn(app)
    assert(p is not None)


def read_config():
    global p, expect
    #cfg = configparser.ConfigParser()
    #cfg.read('moonio.ini')
    j = json.loads(open("moonio.json").read())
    command = j['command']
    expect = j['expect']
    create(command)
    print("hello", command, expect)


def send(msg):
    global p, expect
    p.sendline(msg + "\n")
    p.expect(expect)
    return p.after

def main():
    p = create("gforth")
    while True:
        inp = input()
        resp = send(p, inp, ".*ok\r\n")
        print(resp)

if __name__ == "__main__":
    #global p
    read_config()
    #print(p)
        
