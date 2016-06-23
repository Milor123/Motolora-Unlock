import os
from subprocess import Popen, PIPE, STDOUT

try:

    igg = 'fastboot oem get_unlock_data'
    p = Popen(igg, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    output = p.stdout.read().splitlines()
    code = []
    for x in output:
        if str(x[1:11]) == 'bootloader': # 1:11 is 'bootloader' > (bootloader) xxxCodexxx
        code.append(x[13:]) # 13: is 'xxxCodexx'
    alldata= ('').join(code)
    print alldata
    myfile = open('Code_Bootloader','w')
    myfile.write(alldata)
    myfile.close()

except:
    message= 'Error Desconocido, Intenta ejecutar este archivo donde este el fastboot o agregalo a la consola'
    myfile = open('motorola_get_id_Error.log','w')
    myfile.write(message)
    myfile.close()
    exit()


