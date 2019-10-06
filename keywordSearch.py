from os import listdir # lists all files in a directory
from os import makedirs, path
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
                    #wordLower = stemmer.lemmatize(wordLower) # lemmatization of words like payment and payments
                    if keywordLower == wordLower:
                        count += 1
                        totalOccurrences += 1
            # if count > 0:
            #     print("\t", keywordLower, ": ", count)
        return totalOccurrences
    except FileNotFoundError:
        print("The file is not found.")

# list of keywords for every category
#listCategories = ["Betalning", "Krediter", "Återbetalning", "Handledningstid", "Studieförskring"]
listKeywordsPayment = ["Lån","Betalning","Betalningar","Bidrag","Pengar", "Studiemedel", "Ansöka", "Ansökning"]
listKeywordsCredits = ["Kredit", "Krediter", "Credit", "Universitet", "Kurs", "Course", "hp ", "poäng", "Studieresultat", "Resultat"]
listKeywordsRepayment = ["återbetalning","Återbetala","Tillbaka"]
listKeywordsProcessingTime = ["Handledning","Tid","Handledningstid","Vänta","Beslut", "Väntetid"]
listKeywordsStudyAssurance = ["Försäkran","Studieförsäkran","Insurance","Assurance"]

# dictionary with categories and files
dict_obj = {}

# directory that contains txt files
directory_Inputfiles = "./inputFiles"

def fileCategorizedInMap(directory_Inputfiles):
    if not path.exists(directory_Inputfiles):
        makedirs(directory_Inputfiles)

    for filename in listdir(directory_Inputfiles):
        # create the full path of the file to open
        pathToFile = directory_Inputfiles + '/' + filename
        # print("Occurrences of keywords in the file " + filename + " are: ")
        # search for keywords of the different categories in the file
        totalOccurrencesPayment = keywordSearch(pathToFile, listKeywordsPayment)
        totalOccurrencesCredits = keywordSearch(pathToFile, listKeywordsCredits)
        totalOccurrencesRepayment = keywordSearch(pathToFile, listKeywordsRepayment)
        totalOccurrencesProcessingTime = keywordSearch(pathToFile, listKeywordsProcessingTime)
        totalOccurrencesStudyAssurance = keywordSearch(pathToFile, listKeywordsStudyAssurance)
        # categorizes the file based on which category's keywords appear more often
        if (totalOccurrencesPayment>totalOccurrencesCredits)and(totalOccurrencesPayment>totalOccurrencesRepayment)and(totalOccurrencesPayment>totalOccurrencesProcessingTime)and(totalOccurrencesPayment>totalOccurrencesStudyAssurance):
            try:
                dict_obj["Studiemedel"].append(filename)
            except KeyError:
                dict_obj["Studiemedel"] = [filename]
        elif (totalOccurrencesCredits>totalOccurrencesPayment)and(totalOccurrencesCredits>totalOccurrencesRepayment)and(totalOccurrencesCredits>totalOccurrencesProcessingTime)and(totalOccurrencesCredits>totalOccurrencesStudyAssurance):
            try:
                dict_obj["Studieresultat"].append(filename)
            except KeyError:
                dict_obj["Studieresultat"] = [filename]
        elif (totalOccurrencesRepayment>totalOccurrencesCredits)and(totalOccurrencesRepayment>totalOccurrencesPayment)and(totalOccurrencesRepayment>totalOccurrencesProcessingTime)and(totalOccurrencesRepayment>totalOccurrencesStudyAssurance):
            try:
                dict_obj["Återbetalning"].append(filename)
            except KeyError:
                dict_obj["Återbetalning"] = [filename]
        elif (totalOccurrencesProcessingTime>totalOccurrencesCredits)and(totalOccurrencesProcessingTime>totalOccurrencesRepayment)and(totalOccurrencesProcessingTime>totalOccurrencesPayment)and(totalOccurrencesProcessingTime>totalOccurrencesStudyAssurance):
            try:
                dict_obj["Väntetid"].append(filename)
            except KeyError:
                dict_obj["Väntetid"] = [filename]
        elif (totalOccurrencesStudyAssurance>totalOccurrencesCredits)and(totalOccurrencesStudyAssurance>totalOccurrencesRepayment)and(totalOccurrencesStudyAssurance>totalOccurrencesProcessingTime)and(totalOccurrencesStudyAssurance>totalOccurrencesPayment):
            try:
                dict_obj["Studieförsäkran"].append(filename)
            except KeyError:
                dict_obj["Studieförsäkran"] = [filename]
        else:
            try:
                dict_obj["Okategoriserad"].append(filename)
            except KeyError:
                dict_obj["Okategoriserad"] = [filename]
    return dict_obj

#dict_obj = fileCategorizedInMap(directory_Inputfiles)
print("\n")
# displays the dictionary with categories and respective files
headers = ["Category", "File name"]
# for key, val in dict_obj.items():
#     print(key, "|", val)

f = open('table.txt', 'w')
f.write(tabulate(dict_obj.items(), headers, tablefmt="grid"))
f.close()

#input("Press enter to exit ;)")