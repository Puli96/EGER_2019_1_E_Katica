##########################################
#                                        #
#            NE HASZNÁLD!!!!             #
#                                        #
##########################################

##########################################
#               Használata:              #
#                                        #
# a packages-be írd be az összes         #
# szükséges import-ot                    #
# majd futtad le a setap.py-t:           #
# python3 setup.py build                 #
##########################################

from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "time", "turtle"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="EGER_2019_1_E_Katica",
    options=options,
    version="Beta 0.41",
    description='EGER_2019_1_E_Katica',
    executables=executables
)
