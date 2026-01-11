from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from app.utils import ContactEmailSender


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class AboutView(View):
    def get(self, request):
        return render(request, "about.html")


class ServiceView(View):
    def get(self, request):
        return render(request, "service.html")


class SingleServicesView(View):
    def get(self, request):
        return render(request, "single_services.html")


class CaseStudiesView(View):
    def get(self, request):
        return render(request, "case_studies.html")


class TeamView(View):
    def get(self, request):
        return render(request, "team.html")


class PartnershipView(View):
    def get(self, request):
        return render(request, "partnership.html")


class PricingView(View):
    def get(self, request):
        return render(request, "pricing.html")


class TestimonialView(View):
    def get(self, request):
        return render(request, "testimonial.html")


class FaqView(View):
    def get(self, request):
        return render(request, "faq.html")


class BlogView(View):
    def get(self, request):
        return render(request, "blog.html")


class SinglePostView(View):
    def get(self, request):
        return render(request, "single_post.html")


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        # Initialize the email sender with POST data
        sender = ContactEmailSender(request.POST)

        try:
            sender.send()
            messages.success(request, "Email sent successfully!")
            return redirect("contact")
        except Exception:
            # In a real app we'd log 'e'
            messages.error(
                request, "There was an error sending your email. Please try again."
            )
            return redirect("contact")


class SearchView(View):
    def get(self, request):
        return render(request, "search.html")


class X404PageView(View):
    def get(self, request):
        return render(request, "404_page.html")
