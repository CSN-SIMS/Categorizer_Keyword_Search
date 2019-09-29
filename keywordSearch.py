from os import listdir # lists all files in a directory
from nltk.stem import WordNetLemmatizer
from tabulate import tabulate
import codecs

# lemmatization of words like payment and payments
stemmer = WordNetLemmatizer()

# reads file and searches for keywords and counts their occurrences
# returns total number of occurrences
def keywordSearch(filename, listKeywords):
    try:
        file = codecs.open(filename, "r", encoding='utf-8') # reads non-ASCII characters from a text file
        document = file.readlines()
        file.close()
        totalOccurrences = 0
        for keyword in listKeywords:
            keywordLower = keyword.lower()
            count = 0
            for line in document:
                line = line.split()
                for word in line:
                    wordLower = word.lower()
                    wordLower = wordLower.strip('@#$%&*+./!,"')
                    wordLower = stemmer.lemmatize(wordLower) # lemmatization of words like payment and payments
                    if keywordLower == wordLower:
                        count += 1
                        totalOccurrences += 1
            if count > 0:
                print("\t", keywordLower, ": ", count)
        return totalOccurrences
    except FileNotFoundError:
        print("The file is not found.")

# list of keywords for every category
#listCategories = ["Betalning", "Krediter", "Återbetalning", "Handledningstid", "Studieförskring"]
listKeywordsPayment = ["Lån","Betalning","Bidrag","Pengar"]
listKeywordsCredits = ["Kredit", "Credit", "Universitet", "Kurs", "Course", "hp "]
listKeywordsRepayment = ["återbetalning","Återbetala","Tillbaka"]
listKeywordsProcessingTime = ["Handledning","Tid","Handledningstid","Vänta","Beslut"]
listKeywordsStudyAssurance = ["Försäkran","Studieförsäkran","Insurance","Assurance"]

# directory that contains txt files
directory = "inputFiles"

# dictionary with categories and files
dict_obj = {}

for filename in listdir(directory):
    # create the full path of the file to open
    pathToFile = directory + '/' + filename
    print("Occurrences of keywords in the file " + filename + " are: ")
    # search for keywords of the different categories in the file
    totalOccurrencesPayment = keywordSearch(pathToFile, listKeywordsPayment)
    totalOccurrencesCredits = keywordSearch(pathToFile, listKeywordsCredits)
    totalOccurrencesRepayment = keywordSearch(pathToFile, listKeywordsRepayment)
    totalOccurrencesProcessingTime = keywordSearch(pathToFile, listKeywordsProcessingTime)
    totalOccurrencesStudyAssurance = keywordSearch(pathToFile, listKeywordsStudyAssurance)
    # categorizes the file based on which category's keywords appear more often
    if (totalOccurrencesPayment>totalOccurrencesCredits)and(totalOccurrencesPayment>totalOccurrencesRepayment)and(totalOccurrencesPayment>totalOccurrencesProcessingTime)and(totalOccurrencesPayment>totalOccurrencesStudyAssurance):
        try:
            dict_obj["Payment"].append(filename)
        except KeyError:
            dict_obj["Payment"] = [filename]
    elif (totalOccurrencesCredits>totalOccurrencesPayment)and(totalOccurrencesCredits>totalOccurrencesRepayment)and(totalOccurrencesCredits>totalOccurrencesProcessingTime)and(totalOccurrencesCredits>totalOccurrencesStudyAssurance):
        try:
            dict_obj["Credits"].append(filename)
        except KeyError:
            dict_obj["Credits"] = [filename]
    elif (totalOccurrencesRepayment>totalOccurrencesCredits)and(totalOccurrencesRepayment>totalOccurrencesPayment)and(totalOccurrencesRepayment>totalOccurrencesProcessingTime)and(totalOccurrencesRepayment>totalOccurrencesStudyAssurance):
        try:
            dict_obj["Repayment"].append(filename)
        except KeyError:
            dict_obj["Repayment"] = [filename]
    elif (totalOccurrencesProcessingTime>totalOccurrencesCredits)and(totalOccurrencesProcessingTime>totalOccurrencesRepayment)and(totalOccurrencesProcessingTime>totalOccurrencesPayment)and(totalOccurrencesProcessingTime>totalOccurrencesStudyAssurance):
        try:
            dict_obj["Processing time"].append(filename)
        except KeyError:
            dict_obj["Processing time"] = [filename]
    elif (totalOccurrencesStudyAssurance>totalOccurrencesCredits)and(totalOccurrencesStudyAssurance>totalOccurrencesRepayment)and(totalOccurrencesStudyAssurance>totalOccurrencesProcessingTime)and(totalOccurrencesStudyAssurance>totalOccurrencesPayment):
        try:
            dict_obj["Study Assurance"].append(filename)
        except KeyError:
            dict_obj["Study Assurance"] = [filename]
    else:
        try:
            dict_obj["Uncategorized"].append(filename)
        except KeyError:
            dict_obj["Uncategorized"] = [filename]

print("\n")
# displays the dictionary with categories and respective files
headers = ["Category", "File name"]
# for key, val in dict_obj.items():
#     print(key, "|", val)
print(tabulate(dict_obj.items(), headers, tablefmt="grid"))