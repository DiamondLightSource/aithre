#!/bin/env python3
import subprocess
from subprocess import Popen, PIPE


class ca:
    def __init__(self):
        print("V0.1")

    def cagetstring(pv):
        val = None
        while val is None:
            try:
                a = Popen(["caget", "-S", pv], stdout=PIPE, stderr=PIPE)
                a_stdout, a_stderr = a.communicate()
                val = a_stdout.split()[1]
                val = str(val.decode("ascii"))
            except:
                print("Exception in ca_py3.py cagetstring maybe this PV aint a string")
                pass
        return val

    def caget(pv):
        val = None
        while val is None:
            try:
                a = Popen(["caget", pv], stdout=PIPE, stderr=PIPE)
                a_stdout, a_stderr = a.communicate()
                val = a_stdout.split()[1].decode("ascii")
                # val = evaluate(val)
                # val = val.decode('ascii')
            except:
                print("Exception in ca_py3.py caget, maybe this PV doesnt exist:", pv)
                pass
        return val

    def caput(pv, new_val):
        check = Popen(["cainfo", pv], stdout=PIPE, stderr=PIPE)
        check_stdout, check_stderr = check.communicate()
        if check_stdout.split()[11].decode("ascii") == "DBF_CHAR":
            a = Popen(["caput", "-S", pv, str(new_val)], stdout=PIPE, stderr=PIPE)
            a_stdout, a_stderr = a.communicate()
        else:
            a = Popen(["caput", pv, str(new_val)], stdout=PIPE, stderr=PIPE)
            a_stdout, a_stderr = a.communicate()


class control:
    def __init__(self):
        print("V0.1")

    def get_value(self, pv):
        subprocess.run(("caget", pv))

    def push_value(self, pv):
        subprocess.run(("caput", pv))
