import socket
import sys
import datetime
import random
import string
from urllib.parse import urlparse
import jinja2
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INFO="\033[1;35;40m"
global gserver
global gsp
global gst
global pserver
global psp
global pst
global ptserver
global ptsp
global ptst
global mfunc
global mpath
global m2func
global m2path
global m3path
global m3func
global r
global t
global td1
global td2
global td3
global td4
global c1
global c2
global c3
global c4
global secure
global path
global value
gserver=[]
gsp=[]
gst=[]
pserver=[]
psp=[]
pst=[]
ptserver=[]
ptsp=[]
ptst=[]
mfunc=[]
mpath=[]
m2func=[]
m2path=[]
m3path=[]
m3func=[]
r=[]
t=[]
td1=[]
td2=[]
td3=[]
td4=[]
c1=[]
c2=[]
c3=[]
c4=[]
path=[]
value=[]
def inject(path2,value2):
    path.append(path2)
    value.append(f"\n{value2}")
def secure(request):
    #this is a test for the CUSTOM property
    return True
def awpage(type,path,file,tlist="public", optfunc="ooo"):
    gserver.append(file)
    gsp.append(path)
    gst.append(type)
    td1.append(tlist)
    c1.append(optfunc)
def swpage(path,func):
    mfunc.append(func)
    mpath.append(path)
def npost(type,path,snd2,tlist="public", optfunc="ooo"):
    pserver.append(snd2)
    psp.append(path)
    pst.append(type)
    td2.append(tlist)
    c2.append(optfunc)
def sposts(path,func):
    m2func.append(func)
    m2path.append(path)
def nput(type,path,file,tlist="public", optfunc="ooo"):
    ptserver.append(file)
    ptsp.append(path)
    ptst.append(type)
    td3.append(tlist)
    c3.append(optfunc)
def sput(path,func):
    m3func.append(func)
    m3path.append(path)
def adf(type,resource,tlist="public", optfunc="ooo"):
    r.append(resource)
    t.append(type)
    td4.append(tlist)
def render(file,**args):
    jinja=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    jinja=jinja.get_template(file)
    return jinja.render(args)
def run():
    global path
    def hints(path):
        return urlparse("/"+path)
    print(f"{bcolors.INFO}{bcolors.BOLD}[INFO]{bcolors.ENDC} Server is starting")
    Delete=True
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8000
    def Njinetemplate(data,vars):
        print(type(vars))
        f=(list(vars.keys()))
        f2=list(vars.values())
        things=[]
        for i in range(len(f2)):
            things.append("{{"+f[i]+"}}")
        print(things)
        for i in range(len(things)):
            data=data.replace(things[i],str(f2[i]))
        return data
    def bearer(u):
        for i in range(len(headers)):
            #print("Header[1] is " + headers[1].split(":")[1])
            try:
                var=(headers[i].split(": ")[i].rstrip())
                if var in u:
                    return True
            except:
                pass
        return False
    def cookiecheck(type, E=[]):
        if type == "P":
            for i in range(len(headers)):
                splt=[]
                splt=headers[i].split(" ")
                if splt[0]=="Cookie: " and splt[1].split("=")[0]=="256Pin":
                    return True
                    break
            return False
        if type == "E":
            for i in range(len(headers)):
                splt=[]
                msg=""
                splt=headers[i].split(" ")
                if splt[0]=="Cookie"and splt[1].split("=")[0]=="256Pin":
                    cookie=splt[1]
                    msg=False
                    if cookie in E:
                        msg=True
                    else:
                        msg = False
            if msg == True:
                return True
            else:
                return False
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    cbp=[]#cookie baced protection
    while True:
        now = datetime.datetime.now()    
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()
        # Parse HTTP headers
        print(f"{bcolors.INFO}{bcolors.BOLD}[INFO]{bcolors.ENDC} Request is coming:\n{bcolors.FAIL}{request}{bcolors.ENDC}")
        headers = request.split('\n')
        try:
            method = headers[0].split()[0]
        except:
            print(headers)
        print(f"{bcolors.INFO}Request method was {method}{bcolors.ENDC}")
        if method == "GET":
            try:
                filename = headers[0].split()[1]
            except:
                response = 'HTTP/1.0 400 Bad Request \n\n We seem to be having some difficulties, please reload the page'
            """
            HTTP GET REGISTORY
            """
            for i in range(len(gserver)):
                if filename == gsp[i]:
                    filename = gserver[i]
                    d=gst[i]
                    u=td1[i]
                    loc=i 
            try:
                if gsp[loc] in path:
                    injection=value[path.index(gsp[loc])]
                else:
                    injection=""
                content = gserver[loc]
                print(request)
                if d == "public":
                    if cookiecheck("P"):
                        response = 'HTTP/1.0 200 OK\n\n' + content
                    else:
                        # printing lowercase
                        letters = string.ascii_lowercase
                        key= "Set-cookie:"+"256PIN="+''.join(random.choice(letters) for i in range(256)) 
                        response=str("HTTP/1.0 200 OK\n"+key+"\n\n"+content)
                        cbp.append(key)
                        print(response)
                elif d=="private":
                    if cookiecheck("E", u):
                        response = 'HTTP/1.0 200 OK\n\n' + content
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your cookie is not present or your cookie does not have security permitions"
                elif d=="bearer":
                    if bearer(u):
                        response = 'HTTP/1.0 200 OK\n\n' + content
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your cookie is not present or your cookie does not have security permitions"
                else:
                    if c1[loc](request):
                        response = 'HTTP/1.0 200 OK\n\n' + content
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your auth is not present or your auth does not have security permitions"
            except FileNotFoundError:
                try:
                    for i in range(len(mpath)):
                        if filename.startswith(mpath[i]):
                            loc=mfunc[i]
                    response = 'HTTP/1.0 200 OK\n\n' + loc(request,hints(filename))
                except:
                    response = 'HTTP/1.0 404 NOT FOUND\n\nCrash! We cant seem to find the webpage your looking for, Make sure that you typed the url in corectly.'  

            r2=response.split("\n\n")
            r2.insert(1,injection)
            response=r2[0]+r2[1]+f"\n\n{r2[2]}" 
            client_connection.sendall(response.encode())
            client_connection.close()
        if method == "POST":
            try:
                filename = headers[0].split()[1]
                v=request.split("\n\n")
                del v[0]
                for i in v:
                    l=f"{l}{v[i]}"
                POSTMSG=l
            except:
                response = 'HTTP/1.0 400 Bad Request \n\n We seem to be having some difficulties, please reload the page'
            """
            HTTP POST REGISTORY
            """
            print("Processing POST")
            for i in range(len(pserver)):
                if filename == psp[i]:
                    filename = pserver[i]
                    n=pst[i]
                    u=td2[i]
                    loc=i
            try:
                if n=="public":
                    if cookiecheck("p"):
                        pserver[loc]()
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        letters = string.ascii_lowercase
                        key= "Set-cookie:"+"256PIN="+''.join(random.choice(letters) for i in range(256)) 
                        response="HTTP/1.0 200 OK\n"+key+"\n\n"
                        cbp.append(key)
                elif n=="bearer":
                    if bearer(u):
                        pserver[loc]()
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your auth is not present or your auth does not have security permitions"
                        
                elif n=="custom":
                    if c2[loc]:
                        pserver[loc]()
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your auth is not present or your auth does not have security permitions"
                else:
                    if cookiecheck("E",u):
                        pserver[loc]()
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your cookie is not present or your cookie does not have security permitions"
            except:
                try:
                    for i in range(len(m2path)):
                        if filename.startswith(m2path[i]):
                            loc=m2func[i]
                    response = 'HTTP/1.0 200 OK\n\n' + loc(request,hints(filename))
                except:
                    response = "HTTP/1.0 400 Bad Request \n\n"
            try: 
                client_connection.sendall(response.encode())
                client_connection.close()
            except:
                client_connection.sendall("HTTP/1.0 400 Bad Request \n\n".encode())
                client_connection.close()
        if method == "PUT":
            try:
                filename = headers[0].split()[1]
                v=request.split("\n\r\n")
                del v[0]
                l="\n\n".join(v)
                POSTMSG=l
            except:
                response = 'HTTP/1.0 400 Bad Request \n\n We seem to be having some difficulties, please reload the page'
            print("Processing PUT")
            for i in range(len(ptserver)):
                if filename == ptsp[i]:
                    filename = ptserver[i]
                    n=ptst[i]
                    u=td3[i]
                    loc=i
            try:
                if n=="public":
                    if cookiecheck("p"):
                        open(filename,"w").write(POSTMSG)
                        
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        letters = string.ascii_lowercase
                        key= "Set-cookie:"+"256PIN="+''.join(random.choice(letters) for i in range(256)) 
                        response="HTTP/1.0 200 OK\n"+key+"\n\n"
                        cbp.append(key)
                elif n=="bearer":
                    if bearer(u):
                        open(filename,"w").write(POSTMSG)
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your auth is not present or your auth does not have security permitions"
                        
                elif n=="custom":
                    if c2[loc]:
                        open(filename,"w").write(POSTMSG)
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your auth is not present or your auth does not have security permitions"
                else:
                    if cookiecheck("E",u):
                        pserver[loc]()
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your cookie is not present or your cookie does not have security permitions"
            except:
                e = sys.exc_info()[0]
                print( "<p>Error: %s</p>" % e )
                try:
                    for i in range(len(m3path)):
                        if filename.startswith(m3path[i]):
                            loc=m3func[i]
                    response = 'HTTP/1.0 200 OK\n\n' + loc(request,hints(filename))
                except:
                    response = "HTTP/1.0 400 Bad Request \n\n"
            try: 
                client_connection.sendall(response.encode())
                client_connection.close()
            except:
                client_connection.sendall("HTTP/1.0 400 Bad Request \n\n".encode())
                client_connection.close()
    # Close socket
    server_socket.close()
def about(request,hints):
    return "ahsan"
inject("/","Server:Njine")
di={'knights': 'that say nih'}
awpage("custom","/",render("index.html",knights="hello",posts="ak"),"public",secure)
swpage("/about",about)
awpage("bearer","/bearer","yooo",["Bearer abc"])
npost("bearer","/postb","bearer",["Bearer abc"])
nput("bearer","/test","templates/index.html",["Bearer abc"])
run()