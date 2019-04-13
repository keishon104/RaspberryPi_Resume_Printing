import os
import tempfile
LAST = 'SMITH'
FIRST = 'KEISHON'
UPLOAD_FOLDER = '/Users/darpa/Documents/Development/raspberrypi-flask-server/docs'
filename = '/Users/darpa/Downloads/Keishon\ Smith\ September\ Resume'
# Detects the current working directory
path = os.getcwd()
# os.mkdir(str(path+"/"+LAST+"_"+FIRST))
print(path + "/apple")

# Create a temporary directory
with tempfile.TemporaryFile("w+t") as directory:
    print('The created temporary directory is %s' % directory)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
