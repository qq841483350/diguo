#coding:utf8
#帝国自动登陆发布文章，提示：7.0版本以后的帝国CMS先在后台设置系统-安全参数配置-开启后台来源认证码 改为：刺关闭模式
#选择栏目-修改-选项设置- 在检测标题重复前打上对号。
import urllib,urllib2,cookielib
def diguo(domain='域名网址不带/如：http://ww.domain.com',username='后台登陆用户名',password='后台登陆密码',classid='栏目ID',title='标题',newstext='内容'):

    #-----登陆帝国CMS并发布信息-------,
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        # "Host":"localhost",
        # "Referer":"http://localhost/e/admin/index.php"
    }
    #____伪装头部信息___
    cookie=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    #_____________构建头部信息结束___________________________
    login_data={
        "enews":"login",
        "username":username ,
        "password":password
    }
    login_url="%s/e/admin/ecmsadmin.php"%domain
    login_data=urllib.urlencode(login_data)
    req=urllib2.Request(url=login_url,data=login_data,headers=headers)
    html=urllib2.urlopen(req).read()

    if "LoginSuccess" in html:
        print '已成功登陆网站后台'.decode('utf8')
    else:
        print "LoginFail"
#-------------登陆成功开始发送数据---------------------------------
    post_data={
        "enews":"AddNews",
        "classid":classid,
        "oldchecked":"1",
        "title":title,
        "checked":"1",
        "copyimg":"1",
        "getfirsttitlepic":"1",
        "newstext":newstext,
        "addnews":"提交",

    }
    post_data=urllib.urlencode(post_data)
    post_url="%s/e/admin/ecmsinfo.php"%domain
    req=urllib2.Request(url=post_url,data=post_data,headers=headers)
    html=urllib2.urlopen(req).read()
    if "增加信息成功" in html:
        print '增加信息成功,标题是:'.decode('utf8'),title.decode('utf8')
    elif "标题重复,增加不成功" in html:
        print '标题重复,增加不成功,重复的标题为：'.decode('utf8'),title.decode('utf8')
    else:
        print html
if __name__=="__main__":
    domain='http://localhost'  #域名网址不带/如：http://ww.domain.com
    username='admin'  #用户名
    password='admin'  #密码
    classid="1" #栏目ID
    title='测试标题'
    newstext='正文'
    diguo(domain,username,password,classid,title,newstext)
    
