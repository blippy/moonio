import pexpect # sudo pip3 install pexpect

def create(app):
    return pexpect.spawn(app)

def send(p, msg, eot):
    p.sendline(msg + "\n")
    p.expect(eot)
    return p.after

def main():
    p = create("gforth")
    while True:
        inp = input()
        resp = send(p, inp, ".*ok\r\n")
        print(resp)

if __name__ == "__main__":
    main()
        
