import socket
import os
import datetime
import random
import string
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
global mfgec
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
def secure():
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
print(f"{bcolors.INFO}{bcolors.BOLD}[INFO]{bcolors.ENDC} Server is starting")
def run():
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
        print(f"{bcolors.INFO}Server request is coming {request}")
        headers = request.split('\n')
        try:
            method = headers[0].split()[0]
        except:
            print(headers)
        print(f"{bcolors.INFO}Request method is {method}{bcolors.ENDC}")
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
                fin = open(filename.replace("/", ""))
                content = fin.read()
                fin.close()
                content=Njinetemplate(content,{'weather':'10','H':0})
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
                else:
                    if c1[loc]:
                        response = 'HTTP/1.0 200 OK\n\n' + content
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your auth is not present or your auth does not have security permitions"
            except FileNotFoundError:
                response = 'HTTP/1.0 404 NOT FOUND\n\nCrash! We cant seem to find the webpage your looking for, Make sure that you typed the url in corectly.'
            
            client_connection.sendall(response.encode())
            client_connection.close()
        if method == "POST":
            try:
                filename = headers[0].split()[1]
                POSTMSG=headers[10]
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
                        print("Hello " + POSTMSG)
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        letters = string.ascii_lowercase
                        key= "Set-cookie:"+"256PIN="+''.join(random.choice(letters) for i in range(256)) 
                        response="HTTP/1.0 200 OK\n"+key+"\n\n"
                        cbp.append(key)
                elif n=="custom":
                    if c2[loc]:
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your auth is not present or your auth does not have security permitions"
                else:
                    if cookiecheck("E"):
                        print("Hello " + POSTMSG)
                        response = 'HTTP/1.0 200 Ok\n\n'
                    else:
                        response = 'HTTP/1.0 403 Forbidden\n\n'+"Unautherized, either your cookie is not present or your cookie does not have security permitions"
            except:
                response = "400 Bad Request"
            try: 
                client_connection.sendall(response.encode())
                client_connection.close()
            except:
                client_connection.sendall("HTTP/1.0 400 Bad Request \n\n".encode())
                client_connection.close()
        if method == "DELETE":
            filename = headers[0].split()[1]
            """
            HTTP DELETE REGISTRY
            """
            if Delete:
                path=filename.split("/")
                print(f"{bcolors.WARNING}{filename}{bcolors.ENDC}")
                if filename=="/ris.html": #add a and to make sure that it is in a list of deletable resorces and that the user is allowed
                    d=True
                if filename == "/fcdns.txt":
                    d=False
                if not(d):
                    if cookiecheck("P"):
                        try:
                            os.remove(filename)
                            response = 'HTTP/1.0 200 Ok\n\nHTTP/1.1 200 OK Date: ',now,'<html><head><style>h1{font-family: "Gill Sans", sans-serif;font-weight: bold;</style></head> <body> <h1 id="bowl">File deleted.</h1> </body> </html>'
                            client_connection.sendall(response.encode())
                            client_connection.close()
                        except:
                            response = 'HTTP/1.0 204 No Content\n\n'
                            client_connection.sendall(response.encode())
                            client_connection.close()
                    else:
                        response = 'HTTP/1.0 204 No Content\n\n'
                        client_connection.sendall(response.encode())
                        client_connection.close()
                else:
                    if cookiecheck("E"):
                        os.remove(filename)
                        response = 'HTTP/1.0 200 Ok\n\nHTTP/1.1 200 OK Date: ',now,'<html><head><style>h1{font-family: "Gill Sans", sans-serif;font-weight: bold;</style></head> <body> <h1 id="bowl">File deleted.</h1> </body> </html>'
                        client_connection.sendall(response.encode())
                        client_connection.close()
                    else:
                        response = 'HTTP/1.0 204 No Content\n\n'
                        client_connection.sendall(response.encode())
                        client_connection.close()
            else:
                response = 'HTTP/1.0 204 No Content\n\n'
                client_connection.sendall(response.encode())
                client_connection.close()
        if method == "PUT":
            filename = headers[0].split()[1].replace("/")
            if filename == "index.html":
                typ="pub"
                filname="index.html"
            if typ=="pub":
                if cookiecheck("P"):
                    try:
                        n=headers.split("\n\n")
                        del n[0]
                        n='\n\n'.join(n)
                        with open(filename) as myfile:
                            data = myfile.read()
                            myfile.seek(0)
                            myfile.write(n)
                            myfile.truncate()
                        response=("HTTP/1.1 201 Created\n"+"Content-Location: "+filename)
                    except:
                        response=("HTTP/1.1 204 No Content\n"+"Content-Location: "+filename)
                    client_connection.sendall(response.encode())
                    client_connection.close()
                else:
                    letters = string.ascii_lowercase
                    key= "Set-cookie:"+"256PIN="+''.join(random.choice(letters) for i in range(256)) 
                    response="HTTP/1.0 200 OK\n"+key+"\n\n"
                    cbp.append(key)

    # Close socket
    server_socket.close()
awpage("custom","/","index.html",secure())
run()