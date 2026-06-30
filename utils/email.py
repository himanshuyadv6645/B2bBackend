from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_email(subject, message, recipient_list, html_message=None):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception:
        return False


def send_otp_email(email, otp):
    subject = 'Your Verification Code'
    message = f'Your OTP is: {otp}. It will expire in 10 minutes.'
    html_message = f'''
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
        <h2>Email Verification</h2>
        <p>Your one-time password (OTP) is:</p>
        <h1 style="color: #4F46E5; font-size: 32px; letter-spacing: 8px;">{otp}</h1>
        <p>This code will expire in <strong>10 minutes</strong>.</p>
        <p>If you did not request this, please ignore this email.</p>
    </div>
    '''
    return send_email(subject, message, [email], html_message)


def send_order_confirmation_email(email, order_number):
    subject = f'Order Confirmed - {order_number}'
    message = f'Your order {order_number} has been confirmed.'
    return send_email(subject, message, [email])
