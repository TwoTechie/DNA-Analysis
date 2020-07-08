from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import os
import shutil
from os import path
from .forms import BookForm
from .models import Book


class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        file_path = os.path.join('./media', 'input.txt') # full path to text.
    return render(request, 'upload.html', context)

def fun1(request):
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/inputfun1.txt', './media/fun1.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun1.txt')
        file_path = os.path.join('./media','fun1.txt')
        file1 = open(file_path,"r+")
        Text = file1.readlines()
        PatternCount(Text[0],Text[1],file1)
    return render(request, 'fun1.html', context)

def PatternCount(Textt, Pattern,file1):
            count = 0
            diff = len(Textt)-len(Pattern)+1
            for i in range(0,diff):
                if Textt[i:i+len(Pattern)] == Pattern:
                    count += 1
            cnum = str(count)
            file1.write(cnum)

def fun2(request):
    #pattern matching
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/inputfun2.txt', './media/fun2.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun2.txt')
        file_path = os.path.join('./media','fun2.txt') # full path to text.
        file1 = open(file_path,"r+")
        Text = file1.readlines()
        print ("Output of Read function is ")
        print(Text)
        PatternMatching(Text[0],Text[1],file1)
    return render(request, 'fun2.html', context)

def PatternMatching(Text, Pattern,file1):
    for  i in range(0,len(Text)-len(Pattern)+1):
        flag = 0
        for j in range(i,i+len(Pattern)):
            if Text[j] == Pattern[j-i]:
                flag+=1
        if flag == len(Pattern):
            cnum = str(i)
            file1.write(cnum)
            print(cnum)

def fun3(request):
    #Frequent words
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/inputfun3.txt', './media/fun3.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun3.txt')
        file_path = os.path.join('./media','fun3.txt') # full path to text.
        file1 = open(file_path,"r+")
        Text = file1.readlines()
        FrequentWords(Text[0], Text[1], file1)
    return render(request, 'fun3.html', context)

def FrequentWords(Text, k, file1):
    count = {}
    FrequentPattern_raw = []
    FrequentPattern = []
    z = len(Text)
    z1 = int(z)
    x = int(k)
    for i in range(z1-x+1):
        Pattern = Text[i:i+x]
        count[Pattern] = PCount(Text, Pattern)
    maxCount = max(count.values())
    for i in range(z1-x+1):
        if count[Text[i:i+x]] == maxCount:
            FrequentPattern_raw.append(Text[i:i+x])
            file1.write(Text[i:i+x])
    for i in FrequentPattern_raw:
        if i not in FrequentPattern:
            FrequentPattern.append(i)
            file1.write(i)
            print(i)
    

def PCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

def fun4(request):
    #Reverse
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/inputfun4.txt', './media/fun4.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun4.txt')
        file_path = os.path.join('./media','fun4.txt') # full path to text.
        file1 = open(file_path,"r+")
        Text = file1.readlines()
        ReverseComplement(Text[0], file1)
    return render(request, 'fun4.html', context)

def ReverseComplement(Text, file1):
    c = ''
    for i in Text:
        if i == 'A':
            c+='T'
        if i == 'T':
            c+='A'
        if i == 'G':
            c+='C'
        if i == 'C':
            c+='G'
    Rev_comp = ''
    for i in range(1,len(Text)+1):
        Rev_comp+=c[-i]
    file1.write(Rev_comp)

def fun5(request):
    #clump
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/inputfun5.txt', './media/fun5.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun5.txt')
        file_path = os.path.join('./media','fun5.txt') # full path to text.
        file1 = open(file_path,"r+")
        Text = file1.readlines()
        ClumpFinding(Text[0], Text[1], Text[2], Text[3], file1)
    return render(request, 'fun5.html', context)

def ClumpFinding(Genome, k, L,t, file1):
    j = 0
    L1  = int(L)
    t1  = int(t)
    k1  = int(k)
    clump = set()
    while (j+L1)<=len(Genome):
        substrate = {}
        w = Genome[j:j+L1]
        f = 0
        while (f+k1)<=len(w):
            sub = w[f:f+k1]
            if sub not in substrate:
                substrate[sub] = 1
            else :
                substrate[sub]+=1
            f+=1
        j+=1
        clumpList = [key for key in substrate.keys() if substrate[key]>=t1]
        for l in clumpList:
            clump.add(l)
    file1.write(str(len(clump)))

def fun6(request):
    #skew
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/inputfun6.txt', './media/fun6.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun6.txt')
        file_path = os.path.join('./media','fun6.txt') # full path to text.
        file1 = open(file_path,"r+")
        Text = file1.readlines()
        Skew(Text[0] ,file1)
    return render(request, 'fun6.html', context)

def Skew(Pattern, file1):
    skewArray = []
    for i in range(len(Pattern)+1):
        skewArray.append(0)
    for i in range(len(Pattern)):
        if Pattern[i] == 'C':
            skewArray[i+1] = skewArray[i]-1
            c = skewArray[i+1]
            file1.write(str(c))
        elif  Pattern[i] == 'G':
            skewArray[i+1] = skewArray[i]+1
            c1 = skewArray[i+1]
            file1.write(str(c1))
        else:
            skewArray[i+1] = skewArray[i]
            c2 = skewArray[i+1]
            file1.write(str(c2))

def fun7(request):
    #mismatched
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/inputfun7.txt', './media/fun7.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun7.txt')
        file_path = os.path.join('./media','fun7.txt') # full path to text.
        file1 = open(file_path,"r+")
        Text = file1.readlines()
        MFrequentWords(Text[0], Text[1], Text[2], file1)
    return render(request, 'fun7.html', context)

def MFrequentWords(s,k,d,file1):
    k1 = int(k)
    d1 = int(d)
    counts = {}
    for i in range(len(s)-k1+1):
        for neighbor in neighbors(s[i:i+k1],d1):
            if neighbor not in counts:
                counts[neighbor] = 0
            counts[neighbor] += 1
    m = max(counts.values())
    str1 = ''.join([kmer for kmer in counts if counts[kmer] == m])
    file1.write(str1)

def neighbors( s, d1 ):
    if d1 == 0:
        return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    out = []
    for neighbor in neighbors(s[1:],d1):
        if hamm(s[1:],neighbor) < d1:
            out.extend(['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor])
        else:
            out.append(s[0] + neighbor)
    return out

def hamm( seqA, seqB ):
    hamDistance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            hamDistance+=1
    return hamDistance


def fun8(request):
    #hamming
    context = {}
    if request.method == 'POST':
        shutil.copyfile('./media/inputfun8.txt', './media/fun8.txt')
        fs = FileSystemStorage()
        context['url'] = fs.url('./fun8.txt')
        file_path = os.path.join('./media','fun8.txt') # full path to text.
        file1 = open(file_path,"r+")
        Text = file1.readlines()
        hammingDistance(Text[0], Text[1], file1)
    return render(request, 'fun8.html', context)

def hammingDistance(seqA, seqB, file1):
    hamDistance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            hamDistance+=1
    file1.write(str(hamDistance))