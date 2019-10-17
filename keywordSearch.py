from os import listdir  # lists all files in a directory
from os import makedirs, path
from nltk.stem import WordNetLemmatizer
from tabulate import tabulate
import codecs
import re
from shutil import copyfile

# Categorizer of emails based on keyword-search algorithm
# Results are saved into key-value Map called dictionary
# Input emails are also  into sub-directories based on the result categories
class Categorizer:
    def __init__(self, directory_Inputfiles):
        # list of keywords for every category
        self.listCategories = ["Studiemedel", "Studieresultat", "Inkomst", "Återbetalning", "Väntetid", "Studieförsäkran", "Okategoriserad"]
        self.listKeywordsStudyAids = ["Lån", "Betalning", "Betalningar", "Bidrag", "Pengar", "Studiemedel", "Ansöka", "Villkor", "Lånevillkor"
                               "Ansökning"]
        self.listKeywordsStudyResult = ["Kredit", "Krediter", "Credit", "Universitet", "Kurs", "Course", "hp ", "poäng",
                               "Studieresultat", "Resultat"]
        self.listKeywordsIncome = ["årsinkomst", "Inkomst", "Intyg"]
        self.listKeywordsPayback = ["återbetalning", "Återbetala", "Tillbaka"]
        self.listKeywordsWaitingTime = ["Handledning", "Tid", "Handledningstid", "Vänta", "Beslut", "Väntetid"]
        self.listKeywordsStudyDeclaration = ["Försäkran", "Studieförsäkran", "Insurance", "Assurance"]

        # Key, value map dictionary with categories and files, every key has an array-value
        self.dict_obj = {}
        # key = email.name || value = categoryType
        self.listOfEmails = {}

        # directory that contains txt files
        self.directory_Inputfiles = directory_Inputfiles

    # reads file and searches for keywords and counts their occurrences
    # returns total number of occurrences
    def keywordSearch(self, pathToFile, listKeywords):
        fileContent = openFile(pathToFile)
        totalOccurrences = 0
        for keyword in listKeywords:
            keywordLower = keyword.lower()
            count = 0
            for line in fileContent:
                line = line.split()
                for word in line:
                    wordClear = preprocessWordByTokenizeStemming(word)
                    if keywordLower == wordClear:
                        count += 1
                        totalOccurrences += 1
            # if count > 0:
            #     print("\t", keywordLower, ": ", count)
        return totalOccurrences

    # counts occurrences of keywords in files from a given directory and then categorize them
    # into different sub-directory for every category and save the result in a map
    def categorizeFilesFromDirectoryInMapAndSubDirectory(self):
        directoryCheck(self.directory_Inputfiles)
        for filename in listdir(self.directory_Inputfiles):
            pathToInputFile = pathToFileCreating(self.directory_Inputfiles, filename)
            # print("Occurrences of keywords in the file " + filename + " are: ")
            # search for keywords of the different categories in the file
            totalOccurrencesStudyAids = Categorizer.keywordSearch(self, pathToInputFile, self.listKeywordsStudyAids)
            totalOccurrencesStudyResult = Categorizer.keywordSearch(self, pathToInputFile, self.listKeywordsStudyResult)
            totalOccurrencesIncome = Categorizer.keywordSearch(self, pathToInputFile, self.listKeywordsIncome)
            totalOccurrencesPayback = Categorizer.keywordSearch(self, pathToInputFile, self.listKeywordsPayback)
            totalOccurrencesWaitingTime = Categorizer.keywordSearch(self, pathToInputFile, self.listKeywordsWaitingTime)
            totalOccurrencesStudyDeclaration = Categorizer.keywordSearch(self, pathToInputFile, self.listKeywordsStudyDeclaration)
            # categorizes the file based on which category's keywords appear more often
            categoryMostOccurred = max(totalOccurrencesStudyAids, totalOccurrencesStudyResult, totalOccurrencesIncome, totalOccurrencesPayback, totalOccurrencesWaitingTime, totalOccurrencesStudyDeclaration)
            if (categoryMostOccurred == totalOccurrencesStudyAids):
                Categorizer.appendFileToMapBasedOnMostOccurredCategory(self, filename, self.listCategories[0], self.dict_obj)
                copyFileToUnderdirectory(pathToInputFile, self.listCategories[0], filename)
            elif (categoryMostOccurred == totalOccurrencesStudyResult):
                Categorizer.appendFileToMapBasedOnMostOccurredCategory(self, filename, self.listCategories[1], self.dict_obj)
                copyFileToUnderdirectory(pathToInputFile, self.listCategories[1], filename)
            elif (categoryMostOccurred == totalOccurrencesIncome):
                Categorizer.appendFileToMapBasedOnMostOccurredCategory(self, filename, self.listCategories[2], self.dict_obj)
                copyFileToUnderdirectory(pathToInputFile, self.listCategories[2], filename)
            elif (categoryMostOccurred == totalOccurrencesPayback):
                Categorizer.appendFileToMapBasedOnMostOccurredCategory(self, filename, self.listCategories[3], self.dict_obj)
                copyFileToUnderdirectory(pathToInputFile, self.listCategories[3], filename)
            elif (categoryMostOccurred == totalOccurrencesWaitingTime):
                Categorizer.appendFileToMapBasedOnMostOccurredCategory(self, filename, self.listCategories[4], self.dict_obj)
                copyFileToUnderdirectory(pathToInputFile, self.listCategories[4], filename)
            elif (categoryMostOccurred == totalOccurrencesStudyDeclaration):
                Categorizer.appendFileToMapBasedOnMostOccurredCategory(self, filename, self.listCategories[5], self.dict_obj)
                copyFileToUnderdirectory(pathToInputFile, self.listCategories[5], filename)
            else:
                Categorizer.appendFileToMapBasedOnMostOccurredCategory(self, filename, self.listCategories[6], self.dict_obj)
                copyFileToUnderdirectory(pathToInputFile, self.listCategories[6], filename)
        return self.dict_obj

    # appends the email to the dictionary under the category with most occurred keywords
    def appendFileToMapBasedOnMostOccurredCategory(self, filename, category, dict_obj):
        try:
            dict_obj[category].append(filename)
            #listOfEmails[filename].append(category)
        except KeyError:
            dict_obj[category] = [filename]
        return dict_obj

    # prints the dictionary with the categories and respective files in a table
    def printResultInTable(self):
        headers = ["Category", "File name"]
        print(tabulate(self.dict_obj.items(), headers, tablefmt="grid"))

    # RESULT.Output IN NEW FILE "table.txt": displays the dictionary with the categories and respective files in a new file
    def saveTableResultInFile(self):
        headers = ["Category", "File name"]
        f = open('table.txt', 'w')
        f.write(tabulate(self.dict_obj.items(), headers, tablefmt="grid"))
        f.close()

    def amountOfFiles(self, directory_Inputfiles):
        counterOfEmails = 0
        if not path.exists(directory_Inputfiles):
            print('no folder exists')
        for filename in listdir(directory_Inputfiles):
            counterOfEmails = counterOfEmails + 1
        return counterOfEmails

# make lowercase of a word, remove special characters and digits, lemmatization of words like payment and payments
def preprocessWordByTokenizeStemming(word):
    wordLower = word.lower()
    wordLowerNoSymbols = re.sub("(\\d|\\W)+", " ", wordLower)
    wordClear = WordNetLemmatizer().lemmatize(wordLowerNoSymbols)
    return wordClear

# checks if a directory exists, if not creates it
def directoryCheck(directory_Inputfiles):
    if not path.exists(directory_Inputfiles):
        makedirs(directory_Inputfiles)

# create the full path of file in a folder
def pathToFileCreating(directory_Inputfiles, filename):
    pathToFile = directory_Inputfiles + '/' + filename
    return pathToFile

# open a file for reading, including unicode for Swedish
def openFile(pathToFile):
    try:
        file = codecs.open(pathToFile, "r", encoding='utf-8')  # reads non-ASCII characters from a text file
        fileContent = file.readlines()
        file.close()
    except FileNotFoundError:
        print('The file is not found.')
    return fileContent

# copy a file from given input path to an output path
def copyFileToUnderdirectory(pathToInputFile, category, filename):
    directory_Outputfiles = "./outputEmails/" + category
    pathToOutputFile = pathToFileCreating(directory_Outputfiles, filename)
    directoryCheck(directory_Outputfiles)
    try:
        copyfile(pathToInputFile, pathToOutputFile)
    except FileNotFoundError:
        print("Error categorizing the file:" + filename)

