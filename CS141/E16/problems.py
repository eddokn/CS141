def unique_lines():
    file = open("test.txt", "r")
    line_list = []
    for line in file:
        line = line.replace("\n","")
        if line not in line_list:
            line_list.append(line)
    print(len(line_list))

def grep(string,filename):
    file = open(filename, "r")
    for line in file:
        if string in line:
            print(line)
    
def average_quarters():
    file = open("AboutYou.csv","r")
    for line in file:
        print(line)
    file.seek(0)
    headers = file.readline()
    headers_list = headers.split(",")
    print(headers_list)
    quarters_index = headers_list.index("QuartersAtWestern")
    print(quarters_index)
    major = 0
    mquarters
    nonmajor = 0
    unsure = 0 
    for line in file:
        line_list = line.strip("\n").split(",")
        if "Yes" in line_list:
            
    
        