# .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
#| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
#| |     ______   | || |  _______     | || |  ____  ____  | || |   ______     | || |     _____    | || |  ___  ____   | |
#| |   .' ___  |  | || | |_   __ \    | || | |_  _||_  _| | || |  |_   _ \    | || |    |_   _|   | || | |_  ||_  _|  | |
#| |  / .'   \_|  | || |   | |__) |   | || |   \ \  / /   | || |    | |_) |   | || |      | |     | || |   | |_/ /    | |
#| |  | |         | || |   |  __ /    | || |    \ \/ /    | || |    |  __'.   | || |      | |     | || |   |  __'.    | |
#| |  \ `.___.'\  | || |  _| |  \ \_  | || |    _|  |_    | || |   _| |__) |  | || |     _| |_    | || |  _| |  \ \_  | |
#| |   `._____.'  | || | |____| |___| | || |   |______|   | || |  |_______/   | || |    |_____|   | || | |____||____| | |
#| |              | || |              | || |              | || |              | || |              | || |              | |
#| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
# WHY YOU ARE LOOKING FOR SOURCE CODE :(
# lmao i'm joking 
# // This script coded by Crybik 
# // Facebook : fb.com/solx20
# // Facebook ( 2 ) : https://www.facebook.com/profile.php?id=100027040380280
# // Github : https://github.com/Crybik
import sys
import os
from ctypes import *
cm = "color c"
cmd = "color a"
returned_value = os.system(cmd)
PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF )
VIRTUAL_MEM = ( 0x1000 | 0x2000 )
kernel32 = windll.kernel32
class injection(object):
    def __init__(self):
	print ("Script Coded by Crybik , \n for more informations See source Code")
        self.pid = raw_input("Procces ID Name [PID]: ")
        self.dll = raw_input("Full path for DLL file : ")
    def open_process(self):
        self.h_process = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, int(self.pid) )
        if not self.h_process:
            print "PID is not Correct : ".format(self.pid)
            sys.exit()
    def get_alloc(self):
        self.open_process()
        self.arg_adress = kernel32.VirtualAllocEx(self.h_process, 0, len(self.dll), VIRTUAL_MEM, PAGE_READWRITE)
    def write_process(self):
        self.get_alloc()
        self.written = c_int(0)
        kernel32.WriteProcessMemory(self.h_process, self.arg_adress, self.dll, len(self.dll), byref(self.written))
        self.h_kernel32 = kernel32.GetModuleHandleA("kernel32.dll")
        self.h_loadlib = kernel32.GetProcAddress(self.h_kernel32,"LoadLibraryA")
        self.thread_id = c_ulong(0)
        if not kernel32.CreateRemoteThread(self.h_process,
                                   None,
                                   0,
                                   self.h_loadlib,
                                   self.arg_adress,
                                   0,
                                   byref(self.thread_id)):
            print "Injection Failed ... "
            sys.exit(0)
        print "[*] Remote thread with ID 0x%08x created." % self.thread_id.value
    def __call__(self):
	os.system('color 4')
        return(self.write_process())
injection = injection()
injection()
# this script coded by Crybik 
