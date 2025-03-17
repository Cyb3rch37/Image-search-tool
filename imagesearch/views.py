## views.py (Image Search & Upload)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from .models import SearchReport
import face_recognition
import cv2
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from django.core.mail import send_mail
from django.conf import settings
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

logger = logging.getLogger(__name__)

class ImageSearchView(LoginRequiredMixin, View):
    def post(self, request):
        uploaded_image = request.FILES['uploaded_image']
        reference_image = request.FILES['reference_image']
        
        try:
            ref_encoding = self.load_image_encodings(reference_image)
            test_encoding = self.load_image_encodings(uploaded_image)
            
            results = face_recognition.compare_faces([ref_encoding], test_encoding)
            match = results[0]
            
            # Log the result
            report = SearchReport.objects.create(image_name=uploaded_image.name, match_found=match)
            
            # Send email alert if a match is found
            if match:
                send_mail(
                    'Match Found Alert',
                    f'A match was found for {uploaded_image.name}.',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            
            logger.info(f"Image {uploaded_image.name} processed - Match: {match}")
            return JsonResponse({"match": match})
        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            return JsonResponse({"error": str(e)})
    
    def load_image_encodings(self, image_file):
        image = face_recognition.load_image_file(image_file)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            return encodings[0]
        raise ValueError("No face found in the image")

class DeleteReportView(LoginRequiredMixin, View):
    def post(self, request, report_id):
        try:
            report = get_object_or_404(SearchReport, id=report_id)
            report.delete()
            logger.info(f"Deleted report ID: {report_id}")
            return JsonResponse({"message": "Report deleted successfully"})
        except Exception as e:
            logger.error(f"Error deleting report: {str(e)}")
            return JsonResponse({"error": str(e)})

# Admin Authentication Views
def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')
