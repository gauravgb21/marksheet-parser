from PIL import Image
import pytesseract
import string
import csv


# KMP string search Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0 # index for pat[]
    computeLPSArray(pat, M, lps)
    i = 0 # index for txt[]
    while i<N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            return 1
            j = lps[j-1]
        elif i<N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return 0
 
#calculate lps array 
def computeLPSArray(pat, M, lps):
    len = 0
    lps[0]
    i = 1
    while i<M:
        if pat[i]==pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
 

 
myFile=open('writecsv.csv','w')

boards=[
"AndhraPradeshBoardofSecondaryEducation",
"AndhraPradeshBoardofIntermediateEducation",
"AndhraPradeshOpenSchoolSociety",
"AssamBoardofSecondaryEducation",
"AssamHigherSecondaryEducationCouncil",
"AssamStateOpenSchool",
"BiharBoardofOpenSchooling&Examination",
"BiharSchoolExaminationBoard",
"BoardofHigherSecondaryEducationDelhi",
"CentralBoardofSecondaryEducation",
"CentralBoardofEducationAjmerNewDelhi",
"ChhattisgarhSecondaryBoardofEducation",
"CouncilfortheIndianSchoolCertificateExaminations",
"CouncilOfSecondaryEducationMohali",
"GoaBoardofSecondary&HigherSecondaryEducation",
"GujaratSecondaryEducationBoard",
"GujaratStateOpenSchool",
"HaryanaBoardofSchoolEducation",
"GujaratStateOpenSchool",
"HaryanaStateOpenSchool",
"HimachalPradeshBoardofSchoolEducation",
"HimachalPradeshStateOpenSchool",
"IndianBoardofSchoolEducation",
"JammuandKashmirStateBoardofSchoolEducation",
"JammuandKashmirStateOpenSchool",
"JharkhandAcademicCouncil",
"KarnatakaSecondaryEducationExaminationBoard",
"KeralaHigherSecondaryExaminationBoard",
"KeralaStateOpenSchool",
"MadhyaPradeshBoardofSecondaryEducation",
"MadhyaPradeshStateOpenSchool",
"MaharashtraStateBoardofSecondaryandHigherSecondaryEducation",
"MeghalayaBoardofSchoolEducation",
"MizoramBoardofSchoolEducation",
"NagalandBoardofSchoolEducation",
"NationalInstituteofOpenSchooling",
"OdishaBoardofSecondaryEducation",
"OdishaCouncilofHigherSecondaryEducation",
"PunjabSchoolEducationBoard",
"RajasthanBoardofSecondaryEducation",
"RajasthanStateOpenSchool",
"TamilNaduBoardofSecondaryEducation",
"TelanganaBoardofIntermediateEducation",
"TelanganaBoardofSecondaryEducation",
"TripuraBoardofSecondaryEducation",
"BoardofHighSchoolandIntermediateEducation",
"UttarakhandBoardofSchoolEducation",
"WestBengalBoardofMadrasahEducation",
"WestBengalBoardofPrimaryEducation",
"WestBengalBoardofSecondaryEducation",
"WestBengalCouncilofHigherSecondaryEducation",
"WestBengalCouncilofRabindraOpenSchooling",
"UttarPradeshBoardofSecondaryEducation"]

_len=len(boards)

for i in range(_len):
	boards[i]=boards[i].lower()

# for x in boards:
# 	print(x)
# 	print("\n")

myList=[]

with open('csvtest1.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    writer=csv.writer(myFile)
    for row in reader:
    	newrow=row
    	path="images/"
    	path+=row[3]
    	path+=".jpg"
    	im=Image.open(path)
    	text=pytesseract.image_to_string(im,lang='eng')
    	text=text.lower()
    	text=text.replace(" ","")
    	# print(text)
    	for x in boards:
    		if KMPSearch(x,text)==1:
    			print(x)
    			newrow.append(x)
    			break
    	myList.append(newrow)
    writer.writerows(myList)
print("DONE!")