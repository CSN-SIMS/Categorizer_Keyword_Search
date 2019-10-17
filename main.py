# from keywordSearch import *
#
# # Creates a categorizer for emails from a given directory
# categorizer = Categorizer("./inputFilesSwedish")
#
# # Starts the categorization of the emails
# categorizer.categorizeFilesFromDirectoryInMapAndSubDirectory()
#
# # Prints the results and saves to table.txt
# categorizer.printResultInTable()
# categorizer.saveTableResultInFile()

from GUI_PageResult import *
from GUI_PageOptions import *
from GUI_PageDirectInput import *
# Launch the GUI application for Categorization
PageResult()
PageOptions()
PageDirectInput()