import re
import sys
import time

num = int(time.time())

args = sys.argv
try:
    SLA = int(args[1])
except:
    SLA = 1000

init_stdout = sys.stdout
file_name = "stats.log"
file = open(file_name)
sys.stdout=open("statistics_"+str(num)+".html","w")
print "<HTML>"
print "<BODY>"
flag = 0
count = 0
with file as f:
    for line in f:
        line_text = str(line).decode('utf-8-sig').encode('utf-8')
        if flag == 1:
            #print line_text
            if re.search("^[\-]+", line_text):
                count += 1
            if count==0:
                print "<TABLE BORDER>"
                print "  <CAPTION> REQUEST STATISTICS </CAPTION>"
                print "  <TR>"
                print "    <TH>Name</TH>"
                print "    <TH># reqs</TH>"
                print "    <TH># fails</TH>"
                print "    <TH>Avg</TH>"
                print "    <TH>Min</TH>"
                print "    <TH>Max</TH>"
                print "    <TH>|</TH>"
                print "    <TH>Median</TH>"
                print "    <TH>req/s</TH>"
                print "  </TR>"
            elif count==1:
                m = re.search("(.*)[\s]+(\d+)[\s]+(.*)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\|)[\s]+(\d+)[\s]+(.*)", line_text)
                if m:
                    print "  <TR>"
                    print "    <TD>"+m.group(1)+"</TD>"
                    print "    <TD>"+m.group(2)+"</TD>"
                    print "    <TD>"+m.group(3)+"</TD>"
                    print "    <TD>"+m.group(4)+"</TD>"
                    print "    <TD>"+m.group(5)+"</TD>"
                    print "    <TD>"+m.group(6)+"</TD>"
                    print "    <TD>"+m.group(7)+"</TD>"
                    print "    <TD>"+m.group(8)+"</TD>"
                    print "    <TD>"+m.group(9)+"</TD>"
                    print "  </TR>"
            elif count==2:
                m = re.search("(.*)[\s]+(\d+)[\s]+(.*)[\s]+(\d.*)", line_text)
                if m:
                    print "  <TR>"
                    print "    <TD><B>"+m.group(1)+"</B></TD>"
                    print "    <TD><B>"+m.group(2)+"</B></TD>"
                    print "    <TD><B>"+m.group(3)+"</B></TD>"
                    print "    <TD><B> </B></TD>"
                    print "    <TD><B> </B></TD>"
                    print "    <TD><B> </B></TD>"
                    print "    <TD><B> </B></TD>"
                    print "    <TD><B> </B></TD>"
                    print "    <TD><B>"+m.group(4)+"</B></TD>"
                    print "  </TR>"
                    print "</TABLE BORDER>"
        else:
            m = re.search("^\[(.*)\](.*)\:[\s](.*)", line_text)
            if m:
                text = m.group(3)
                flag = 1 if not text.find("Shutting down (exit code 1), bye.") else 0
                if flag == 0:
                    flag = 1 if not text.find("Shutting down (exit code 0), bye.") else 0
print "</BODY>"
print "</HTML>"
file.close()

sys.stdout = init_stdout
file_name = "stats.log"
file = open(file_name)
sys.stdout=open("distribution_"+str(num)+".html","w")
print "<HTML>"
print "<BODY>"
flag = 0
count = 0
with file as f:
    for line in f:
        line_text = str(line).decode('utf-8-sig').encode('utf-8')
        if flag == 1:
            #print line_text
            if re.search("^[\-]+", line_text):
                count += 1
            if count==0:
                print "<TABLE BORDER>"
                print "  <CAPTION> RESPONSE TIME DISTRIBUTION </CAPTION>"
                print "  <TR>"
                print "    <TH>Name</TH>"
                print "    <TH># reqs</TH>"
                print "    <TH>50%</TH>"
                print "    <TH>66%</TH>"
                print "    <TH>75%</TH>"
                print "    <TH>80%</TH>"
                print "    <TH>90%</TH>"
                print "    <TH>95%</TH>"
                print "    <TH>98%</TH>"
                print "    <TH>99%</TH>"
                print "    <TH>100%</TH>"
                print "  </TR>"
            elif count==1:
                m = re.search("(.*)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)", line_text)
                if m:
                    print "  <TR>"
                    print "    <TD>"+m.group(1)+"</TD>"
                    print "    <TD>"+m.group(2)+"</TD>"
                    print "    <TD>"+m.group(3)+"</TD>"
                    print "    <TD>"+m.group(4)+"</TD>"
                    print "    <TD>"+m.group(5)+"</TD>"
                    print "    <TD>"+m.group(6)+"</TD>"
                    print "    <TD>"+m.group(7)+"</TD>"
                    print "    <TD>"+m.group(8)+"</TD>"
                    print "    <TD>"+m.group(9)+"</TD>"
                    print "    <TD>"+m.group(10)+"</TD>"
                    print "    <TD>"+m.group(11)+"</TD>"
                    print "  </TR>"
        else:
            flag = 1 if not line_text.find("Percentage of the requests completed within given times") else 0
print "</BODY>"
print "</HTML>"
file.close()

sys.stdout = init_stdout
file_name = "stats.log"
file = open(file_name)
sys.stdout=open("errors_performance_"+str(num)+".html","w")
print "<HTML>"
print "<BODY>"
flag = 0
count = 0
header = False
cases=["50%","66%","75%","80%","90%","95%","98%","99%","100%"]
with file as f:
    for line in f:
        line_text = str(line).decode('utf-8-sig').encode('utf-8')
        if flag == 1:
            #print line_text
            if re.search("^[\-]+", line_text):
                count += 1
            elif count==1:
                m = re.search("(.*)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)[\s]+(\d+)", line_text)
                if m:
                    max_time = 0
                    failure_cases = []
                    for i in range(len(cases)):
                        time = int(m.group(i+3))
                        if time >= SLA:
                            failure_cases.append(cases[i])
                            max_time = time if time>max_time else max_time
                    if header is not True and failure_cases != []:
                        print "<TABLE BORDER>"
                        print "  <CAPTION> PERFORMANCE ERROR REPORT </CAPTION>"
                        print "  <TR>"
                        print "    <TH>Name</TH>"
                        print "    <TH># reqs</TH>"
                        print "    <TH>Failure Cases</TH>"
                        print "    <TH>Max Time Taken</TH>"
                        print "  </TR>"
                        header = True
                    if failure_cases != []:
                        print "  <TR>"
                        print "    <TD>"+m.group(1)+"</TD>"
                        print "    <TD>"+m.group(2)+"</TD>"
                        print "    <TD>"+str(failure_cases)+"</TD>"
                        print "    <TD>"+str(max_time)+"</TD>"
                        print "  </TR>"
        else:
            flag = 1 if not line_text.find("Percentage of the requests completed within given times") else 0
print "</BODY>"
print "</HTML>"
file.close()

sys.stdout = init_stdout
file_name = "stats.log"
file = open(file_name)
sys.stdout=open("errors_failures_"+str(num)+".html","w")
print "<HTML>"
print "<BODY>"
flag = 0
count = 0
with file as f:
    for line in f:
        line_text = str(line).decode('utf-8-sig').encode('utf-8')
        if flag == 1:
            #print line_text
            if re.search("^[\-]+", line_text):
                count += 1
            if count==0:
                print "<TABLE BORDER>"
                print "  <CAPTION> FAILURE ERROR REPORT </CAPTION>"
                print "  <TR>"
                print "    <TH># occurences</TH>"
                print "    <TH>Error</TH>"
                print "  </TR>"
            elif count==1:
                m = re.search("(\d+)[\s]+([a-zA-Z].*)", line_text)
                if m:
                    print "  <TR>"
                    print "    <TD>"+m.group(1)+"</TD>"
                    print "    <TD>"+m.group(2)+"</TD>"
                    print "  </TR>"
        else:
            flag = 1 if not line_text.find("Error report") else 0
print "</BODY>"
print "</HTML>"
file.close()

sys.stdout = init_stdout

empty_html = """<HTML>
<BODY>
</BODY>
</HTML>
"""
file_name = "errors_performance_"+str(num)+".html"
file = open(file_name)
html_performance_output = ""
with file as f:
    for line in f:
        html_performance_output+=line
file_name = "errors_failures_"+str(num)+".html"
file = open(file_name)
html_failure_output = ""
with file as f:
    for line in f:
        html_failure_output+=line
flag = 1
if html_performance_output != empty_html:
    print "Error : RESPONSE TIMES EXCEEDED SERVICES S.L.A. LIMIT!"
    flag = 0
if html_failure_output != empty_html:
    print "Error : SERVICES FAILED!"
    flag = 0
if flag == 1:
    print "Success : SERVICES TESTED SUCCESSFULLY!"
else:
    sys.exit(-1)
