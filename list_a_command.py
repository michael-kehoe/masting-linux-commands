import os
import random

stream = os.popen('compgen -c')
output = stream.readlines()
print(random.choice(output))
