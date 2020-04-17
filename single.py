import rhksm4
from matplotlib import pyplot

file = rhksm4.load('inputs/filename.SM4')

for page in file:
    pyplot.imsave('outputs/kenlee_{}.png'.format(page.name),
                  page.data)
