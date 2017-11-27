import subprocess

spaces_count = 4

dirStr = '''K1
    K2
    K3
        K4
K5
    K6'''

lv0 = None
lv1 = None
for catalog in dirStr.split("\n"):
    if catalog.split(" ")[0] != '':
        lv0 = catalog.split(" ")[0]
        subprocess.call('mkdir ' + lv0, shell = True)
    else:
        if catalog.split(" ")[4:][0] != '':
            lv1 = catalog.split(" ")[4:][0]
            subprocess.call('mkdir ' + lv0 + "/" + catalog.split(" ")[4:][0] , shell = True)
        else:
            subprocess.call('mkdir ' + lv0 + "/" + lv1 + "/" + catalog.split(" ")[8:][0] , shell = True)
