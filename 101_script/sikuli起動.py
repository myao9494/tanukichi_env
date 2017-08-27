# -*- coding: utf-8 -*-
import os,subprocess
hp=os.environ['USERPROFILE']
path = os.path.join(hp, 'OneDrive\\sikuli\\runsikulix.cmd')
print(path)
args = [path]
subprocess.Popen(args, shell=True)
