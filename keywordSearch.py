from os import listdir # lists all files in a directory
from nltk.stem import WordNetLemmatizer

stemmer = WordNetLemmatizer()

# reads file and searches for keywords and counts their occurrences
# returns total number of occurrences
def keywordSearch(filename, listKeywords):
    try:
        file = open(filename, "r")
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
listKeywordsPayment = ["Loan", "payment", "grant", "money"]
listKeywordsCredits = ["credit", "university", "course"]
# directory that contains txt files
directory = "inputFiles"

for filename in listdir(directory):
    # create the full path of the file to open
    pathToFile = directory + '/' + filename
    print("Occurrences of the keywords in the file " + filename + " are: ")
    # search for keywords of the different categories in the file
    totalOccurrencesPayment = keywordSearch(pathToFile, listKeywordsPayment)
    totalOccurrencesCredits = keywordSearch(pathToFile, listKeywordsCredits)
    # categorizes the file based on which category's keywords appear more often
    if totalOccurrencesPayment > totalOccurrencesCredits:
        print("The file", filename, "then might belong to category Payment")
    elif totalOccurrencesCredits > totalOccurrencesPayment:
        print("The file", filename, "then might belong to category Credits")
    else:
        print("The file cannot be categorized.")
    print("\n")