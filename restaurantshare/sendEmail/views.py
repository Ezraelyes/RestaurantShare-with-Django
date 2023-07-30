from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    mail_html = "<html><body>"
    mail_html += "<h1> 맛집 공유 </h1>"
    mail_html += "<p>"+inputContent+"<br>"
    mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다.</p>"
    for checked_res_id in checked_res_list:
        restaurant = Restaurant.objects.get(id = checked_res_id)
        mail_html += "<h2>"+restaurant.restaurant_name+"</h3>"
        mail_html += "<h4>* 관련 링크</h4>"+"<p>"+restaurant.restaurant_link+"</p><br>"
        mail_html += "<h4>* 상세 내용</h4>"+"<p>"+restaurant.restaurant_content+"</p><br>"
        mail_html += "<h4>* 관련 키워드</h4>"+"<p>"+restaurant.restaurant_keyword+"</p><br>"
        mail_html += "<br>"
    mail_html +="</body></html>"
    # print(mail_html)

    # 이메일 발신 정보
    sender_email = 'ryukai0927@gmail.com'
    app_password = 'gcngewhzvayzanas'  

    # 이메일 수신자 정보
    receiver_email = inputReceiver
    email_subject = inputTitle
    email_content = inputContent + mail_html

    # 이메일 설정
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_content, 'html'))

    try:
        # SMTP 서버 연결
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, app_password)

        # 이메일 전송
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # SMTP 서버 연결 종료
        server.quit()

        return HttpResponseRedirect(reverse('index'))
    except Exception as e:
        return HttpResponse("이메일 전송에 실패했습니다.")

