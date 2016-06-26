#Author: Mateo Bohorquez
#NickName: MingoDRobin, Milor123

from subprocess import Popen, PIPE, STDOUT
import threading

bootloader = False

def get_code_motorola():
    try:
        igg = 'fastboot oem get_unlock_data'
        p = Popen(igg, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        output = p.stdout.read().splitlines()
        code = []
        for x in output:
            if str(x[1:11]) == 'bootloader': # 1:11 is 'bootloader' > (bootloader) xxxCodexxx
                code.append(x[13:]) # 13: is 'xxxCodexx'
                bootloader = True
        if bootloader:
            alldata= ('').join(code)
            myfile = open('Code_Bootloader.txt','w')
            myfile.write(alldata)
            myfile.close()
        else:
            raise
    except:
        message= 'Error Desconocido, Intenta ejecutar este archivo donde este el fastboot o agregalo a la consola'
        myfile = open('motorola_get_id_Error.log','w')
        myfile.write(message)
        myfile.close()

def killer(): # this is necessary because stdout.read() do a bucle if the phone is not connected
    global code
    import time
    time.sleep(5)
    if code.isAlive(): # if exists the thread
        code._Thread__stop() # kill thread
        message= 'Error Desconocido, Intenta ejecutar este archivo donde este el fastboot o agregalo a la consola'
        myfile = open('motorola_get_id_Error.log','w')
        myfile.write(message)
        myfile.close()

# threads for kill process if its waiting
code = threading.Thread(target=get_code_motorola)
killer = threading.Thread(target=killer)
code.start()
killer.start()


