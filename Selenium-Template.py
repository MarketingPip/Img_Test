import os 

import subprocess


counter = 0
print("If you want all the excel file, for example write .xlsx")
inp = ".py"
thisdir = os.getcwd()
for r, d, f in os.walk("/home/runner/work/"): # change the hard drive, if you want
    for file in f:
        filepath = os.path.join(r, file)
        if inp in file:
        	counter += 1
            FilePath = os.path.join(r, file)
            subprocess.run(["optimize-images", FilePath])
        	print(os.path.join(r, file))
print(f"Optimized {counter} files.")
