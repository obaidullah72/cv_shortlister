from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from .models import CV
from .utils import extract_text_from_file

class UploadCVView(View):
    def get(self, request: HttpRequest):
        return render(request, 'cv_processor/upload.html')

    def post(self, request: HttpRequest):
        cv_file = request.FILES.get('cv_file')
        if cv_file:
            cv = CV.objects.create(file=cv_file)
            cv.save()
        return render(request, 'cv_processor/upload.html')


class FilterCVsView(View):
    def get(self, request: HttpRequest):
        return render(request, 'cv_processor/filter.html')

    def post(self, request: HttpRequest):
        keywords = request.POST.get('keywords', '').split(',')
        min_experience = int(request.POST.get('experience', 0))
        cvs = CV.objects.all()
        shortlisted = []

        for cv in cvs:
            text = extract_text_from_file(cv.file.path)
            if text:
                keyword_count = sum(1 for keyword in keywords if keyword.strip().lower() in text.lower())
                has_experience = str(min_experience) in text or 'years' in text.lower()
                if keyword_count > 0 and has_experience:
                    shortlisted.append(cv)

        return render(request, 'cv_processor/results.html', {'cvs': shortlisted})
