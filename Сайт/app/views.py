"""
Definition of views.
"""

from datetime import datetime
from pickle import GET
from django.shortcuts import render
from django.http import HttpRequest
from .forms import ExamScoresForm

russian: int = 0


def chance_of_admission(p1: int, p2: int, s: int):
    p: float = ((s - p1) / (300 - p1) + (s - p2) / (300 - p2) + 0.2) / 2 * 100
    if p > 0 and p < 100:
        return p
    elif p > 100:
        return 100
    elif p < 0:
        return 0


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

score: int = 0 

# def exams (request):
#     return render(request, 'exams.html', )

def exams(request):
    """Renders the exams page."""
    assert isinstance(request, HttpRequest)
    # d: int =0
    global score
    score = 0
    if request.method == 'POST':
        form = ExamScoresForm(request.POST)
        # print(form)
        russian = request.POST['russian']
        physics = request.POST['physics']
        literature = request.POST['literature']
        history = request.POST['history']
        math = request.POST['math']
        chemistry = request.POST['chemistry']
        geography = request.POST['geography']
        socialstudies = request.POST['socialstudies']
        informatics = request.POST['informatics']
        biology = request.POST['biology']
        english = request.POST['english']
        
        forms = [russian, physics, literature, history, math, chemistry, geography, socialstudies, informatics, biology, english]
        # for i in range(len(forms)):
        #     if forms[i] == 'None':
        #         forms[i] = 0
                
        # for exam in forms:
        #     score+= int(exam)

        score = int(russian) + int(physics) + int(literature) + int(history) + int(math) + int(chemistry) + int(geography) + int(socialstudies) + int(informatics) + int(biology) + int(english)
            
        # for i in range (len(forms)):
        #     if type(forms[i]) == type(d):
        #         score+=forms[i]

        if score > 300 or score < 0:
            form = ExamScoresForm()
            return render(
                    request,
                    'app/exams.html',
                    {
                        'form': form,
                    }
                )
        else:
            form = ExamScoresForm()
            return render(
                    request,
                    'app/universities.html',
                    {
                        'form': form,
                    }
                )




    else:
        form = ExamScoresForm()
        return render(
            request,
            'app/exams.html',
            {
                'form': form,
                'message': 'Your application description page.',
                'year': datetime.now().year,
            }
        )


def universities(request):
    """Renders the universities page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/universities.html',
        {
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def calendar(request):
    """Renders the calendar page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/calendar.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def specialties(request):
    """Renders the specialties page."""
    assert isinstance(request, HttpRequest)
    posts = [
    {"number": "09.03.03",
    "name": "i",
    "probability": chance_of_admission(234, 243, score),
    "chance": "m",
    "min_score_1": 234,
    "min_score_2": 243,
    "exams": "m",
    }
]
    
    return render(
        request,
        'app/specialties.html',
        {"specs": posts
        }
    )