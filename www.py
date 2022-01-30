import os
import move
def wwwi():
    os.system ('cd /data/data/com.termux/files/usr/bin')
    #d=("""\n#!/usr/bin/python3\nimport os\nos.system ("cd /data/data/com.termux/files/home/UAP-TEAM;python start.py")""")
    with open("UAP" , 'a') as (file):
        file.write("""#!/usr/bin/python3\nimport os\nos.system ("cd /data/data/com.termux/files/home/UAP-TEAM;python UAP_TEAM.py")""")
    os.system('chmod +x UAP')
    move.m()
