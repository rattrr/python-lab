import subprocess
import sys



def try_compile():
    err_code = None
    try:
        err_code = subprocess.check_call('g++ ' + sys.argv[1], shell = True)
    except:
        print "Blad kompilacji"
    return err_code

def try_run():
    try:
        subprocess.check_call("./a.out", shell = True)
    except:
        print "Blad w programie"


if try_compile() == 0:
    try_run()
