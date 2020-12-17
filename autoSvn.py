import os
import subprocess
import svn.local

def kameSvnAdd(_path):
    commit_command = [
        "TortoiseProc",
        "/command:add",
        "/path:" + _path,
        "/closeforlocal:0"
    ]
    subprocess.call(commit_command)

def kameSvnCommit(_path):
    message = "testUpdate_to_USD"
    commit_command = [
        "TortoiseProc",
        "/command:commit",
        "/logmsg:" + message,
        "/path:" + _path,
        "/command:update"
        "/closeOnend:0"
    ]
    subprocess.call(commit_command)

def svnUpdate(_path):
    _path = "D:/Shotgun_work/new_angle_test"
    os.chdir(_path)
    subprocess.call('svn up')

def usdAdd(_path):
    svlocal = svn.local.LocalClient(_path)

    path = _path
    result = svlocal.run_command("status", [path, "--non-recursive"])
    while(True):
        result = svlocal.run_command("status", [path, "--non-recursive"])
        if(result[0] == "" or result[0][0] == "A"):
            break
        
        path, d = os.path.split(path)

    os.chdir(_path)
    files = os.listdir(_path)
    usdfiles = [file for file in files if '.usd' in file]
    for usd in usdfiles:
        subprocess.call('svn add ' + usd)

def svnDCCtoUSD(_path):
    svlocal = svn.local.LocalClient(_path)

    path = _path
    result = svlocal.run_command("status", [path, "--non-recursive"])
    while(True):
        result = svlocal.run_command("status", [path, "--non-recursive"])
        if(result[0] == "" or result[0][0] == "A"):
            break
        
        path, d = os.path.split(path)

    os.chdir(_path)
    message = "Update_to_USD"
    subprocess.call("svn ci -m " + message)

"""
#Run scripts
_path = "D:/Shotgun_work/new_angle_test/assets/01-Character/asset_test000/MDL/work/maya"
kameSvnAdd(_path)
kameSvnCommit(_path)

svnUpdate(_path)

usdAdd(_path)
svnDCCtoUSD(_path)
"""