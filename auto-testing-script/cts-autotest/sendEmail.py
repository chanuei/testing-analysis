# -*- coding: UTF-8 -*-
import sys
import os
import smtplib  
from email.mime.text import MIMEText
from email.header import Header

mailto_list=["qaoimu@163.com","xiaoluoyuan@163.com","elwin_mao@163.com","xyong@csnet4.cs.tsinghua.edu.cn","yuchen@mail.tsinghua.edu.cn","18701158269@163.com"] 
mail_host="smtp.163.com"  #设置服务器
mail_user="cscwlab"    #用户名
mail_pass="cscw9410"   #口令 
mail_postfix="163.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  
    me="cscwlab"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':
    filename = "mailSent"+sys.argv[2]
    if os.path.exists(filename):
	sys.exit(0)
    if send_mail(mailto_list,"testing something wrong",sys.argv[1]):
        print "发送成功"
	os.system('touch '+ filename)
    else:  
        print "发送失败"
