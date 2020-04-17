# Show a grid of images.
# For now, this only works if each image has the same number of pages as all the others.
# The number of pages is taken from the first file we encounter and assumed for the rest.

import rhksm4
from matplotlib import pyplot
import glob

files = glob.glob('./inputs/*.[Ss][Mm]4')

number_of_files = len(files)

# We will define the figure once we get the number of pages from the first file
figure = None

plot_number = 1
for file_name in files:
    # Add each file's pages to the plot

    file = rhksm4.load(file_name)
    number_of_pages = len(file._pages)

    if figure is None:
        # Assume the number of pages in the first file is the number of pages for all files.
        # Create a figure
        figure = pyplot.figure(figsize=(number_of_files, number_of_pages))

    for page in file:
        # Add each page as a subplot
        figure.add_subplot(number_of_files, number_of_pages, plot_number).axis('off')
        pyplot.imshow(page.data)
        plot_number += 1

pyplot.show()
