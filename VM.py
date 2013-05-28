#!/usr/bin/python

import subprocess



class ansicolours:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

vms = {}

i=0
for name in subprocess.check_output(['VBoxManage', 'list', 'vms']).split('\n'):
    if name != '':
        vm = name[name.find('{'):name.find('}')+1]

        info = subprocess.check_output(['VBoxManage','showvminfo',vm,'--machinereadable'])
        for line in info.split('\n'):
            if 'VMState' in line:
                if 'running' in line:
                    vms[i] = [vm,1]
                    print str(i) + ') ' + name + ' Power:' + ansicolours.GREEN + 'ON' + ansicolours.ENDC
                else:
                    vms[i] = [vm,0]
                    print str(i) + ') ' + name + ' Power:' + ansicolours.RED + 'OFF' + ansicolours.ENDC
                i+=1
                break


print "Start or Stop VM? or (q)uit?"
vm_no = int(raw_input())
if vm_no in vms.keys():
    if vms[vm_no][1] == 1:
        subprocess.check_output(['VBoxManage','controlvm',vms[vm_no][0],'acpipowerbutton'])
        print ansicolours.RED + "Shutting Down " + ansicolours.ENDC + vms[vm_no][0] + ' Please wait...'
    else:
        subprocess.check_output(['VBoxManage','startvm',vms[vm_no][0],'--type','headless'])
        print ansicolours.GREEN + "Starting Up " + ansicolours.ENDC + vms[vm_no][0] + ' Please wait...'
else:
    print 'Bye'
