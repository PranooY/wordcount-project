from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def aboutpage(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wcdict = {}
    for word in wordlist:
        if word in wcdict:
            wcdict[word] += 1
        else:
            wcdict[word] = 1

    wcsdict = sorted(wcdict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddict': wcsdict})
