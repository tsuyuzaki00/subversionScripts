import sys
import autoSvn

_path = "D:/Shotgun_work/new_angle_test/assets/01-Character/asset_test000/MDL/work/maya"

autoSvn.usdAdd(_path)
autoSvn.svnDCCtoUSD(_path)

"""
    import os
    import glob
    
    _path = "D:/Shotgun_work/new_angle_test"
    
    os.chdir(_path)
    files = glob.glob("./**.usd", recursive=True)
    print(files)
    for file in files:
        print(file)
    
"""