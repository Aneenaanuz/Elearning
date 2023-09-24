from django.shortcuts import render
from django.views.generic import TemplateView

class ChatBotView(TemplateView):
    template_name="course-detail.html"
