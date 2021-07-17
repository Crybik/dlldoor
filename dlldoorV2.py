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
# // Instagram : Crybik.x
# // Github : https://github.com/Crybik
import sys
import os
from ctypes import *
os.system('color c')
output = os.popen('wmic process get description, processid').read()
print(output)
os.system('dir/s/b *.dll')
returned_value = 0
PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF )
VIRTUAL_MEM = ( 0x1000 | 0x2000 )
kernel32 = windll.kernel32
class injection(object):
    def __init__(self):
	print ("Script Coded by Crybik , \n for more information See source Code")
        self.pid = raw_input("Procces ID Name [PID]: ")
        self.dll = raw_input("Full path for DLL file : ")
    def open_process(self):
        self.h_process = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, int(self.pid) )
        if not self.h_process:
            print "PID isn't Correct : ".format(self.pid)
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

            
            if sys.exit(0) : os.system('color c')
        print "[*] Remote thread with ID 0x%08x created." % self.thread_id.value
    def __call__(self):
        return(self.write_process())
injection = injection()
injection()
# this script coded by Crybik 
