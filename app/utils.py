from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class ContactEmailSender:
    def __init__(self, data):
        self.data = data
        self.recipient_email = getattr(
            settings, "BUSINESS_EMAIL_RECIPIENT", "admin@example.com"
        )

    def send(self):
        subject = (
            f"New Contact Form Submission: {self.data.get('subject', 'No Subject')}"
        )

        # Prepare context with safe variable names (replace hyphens with underscores)
        context_data = {
            "first_name": self.data.get("first-name"),
            "last_name": self.data.get("last-name"),
            "email": self.data.get("email"),
            "subject": self.data.get("subject"),
            "message": self.data.get("message"),
        }

        html_message = render_to_string(
            "emails/contact_notification.html", {"data": context_data}
        )

        # Create a plain text version by stripping HTML tags (simplified for now)
        # For better plain text, we could use a separate template or a library
        plain_message = f"""
        New Contact Submission
        
        Name: {self.data.get("first-name")} {self.data.get("last-name")}
        Email: {self.data.get("email")}
        Subject: {self.data.get("subject")}
        
        Message:
        {self.data.get("message")}
        """

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [self.recipient_email],
            html_message=html_message,
        )
