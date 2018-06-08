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
 

def stringSearch(pat, txt):
    tlen=len(txt)
    plen=len(pat)
    for i in range(tlen):
        if txt[i]==pat[0]:
            j=0
            while j<plen and i+j<tlen and pat[j]==txt[i+j]:
                j=j+1
            if j==plen:
                return 1
    return 0


 
myFile=open('outputcsv.csv','w')

boards=[
"Andhra Pradesh Board of Secondary Education",
"Andhra Pradesh Board of Intermediate Education",
"Andhra Pradesh Open School Society",
"Assam Board of Secondary Education",
"Assam Higher Secondary Education Council",
"Assam State Open School",
"Bihar Board of Open Schooling & Examination",
"Bihar School Examination Board",
"Board of Higher Secondary Education",
"Central Board of Secondary Education",
"Central Board of Education",
"Chhattisgarh Secondary Board of Education",
"Council for the Indian School Certificate Examinations",
"Council Of Secondary Education Mohali",
"Goa Board of Secondary & Higher Secondary Education",
"Gujarat Secondary Education Board",
"Gujarat State Open School",
"Haryana Board of School Education",
"Gujarat State Open School",
"Haryana State Open School",
"Himachal Pradesh Board of School Education",
"Himachal Pradesh State Open School",
"Indian Board of School Education",
"Jammu and Kashmir State Board of School Education",
"Jammu and Kashmir State Open School",
"Jharkhand Academic Council",
"Karnataka Secondary Education Examination Board",
"Kerala Higher Secondary Examination Board",
"Kerala State Open School",
"Madhya Pradesh Board of Secondary Education",
"Madhya Pradesh State Open School",
"Maharashtra State Board of Secondary and Higher Secondary Education",
"Meghalaya Board of School Education",
"Mizoram Board of School Education",
"Nagaland Board of School Education",
"National Institute of Open Schooling",
"Odisha Board of Secondary Education",
"Odisha Council of Higher Secondary Education",
"Punjab School Education Board",
"Rajasthan Board of Secondary Education",
"Rajasthan State Open School",
"Tamil Nadu BoardofSecondary Education",
"Telangana Board of Intermediate Education",
"Telangana Board of Secondary Education",
"Tripura Board of Secondary Education",
"Board of High School and Intermediate Education",
"Uttarakhand Board of School Education",
"West Bengal Board of Madrasah Education",
"West Bengal Board of Primary Education",
"West Bengal Board of Secondary Education",
"West Bengal Council of Higher Secondary Education",
"West Bengal Council of Rabindra Open Schooling",
"Uttar Pradesh Board of Secondary Education"]


_len=len(boards)

myList=[]

with open('inputcsv.csv') as File:
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
    	for i in range(_len):
            x=boards[i]
            x=x.lower()
            x=x.replace(" ","")
            if KMPSearch(x,text)==1:
                newrow.append(boards[i])
                break
    	myList.append(newrow)
    writer.writerows(myList)
print("DONE!")