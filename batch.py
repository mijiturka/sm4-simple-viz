import rhksm4
from matplotlib import pyplot
import glob
import os

for file_path in glob.iglob('./inputs/*.SM4'):
    file = rhksm4.load(file_path)

    for page in file:
        pyplot.imsave('outputs/kenlee_{}_{}.png'.format(os.path.basename(file_path), page.name),
                      page.data)
