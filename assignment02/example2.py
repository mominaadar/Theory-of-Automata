
########## MOMINA ATIF DAR P18-0030

#import sys
import datetime

#filename = sys.argv[1]

#########################

def check_date(filename):
    
    days31 = ['01','03','05','07','08','10','12']
    days30 = ['04','06','09','11']
    days28 = ['02']
    
    data_list = []
    
    d = datetime.datetime.now()
    c = d.strftime("%Y-%m-%d")
    dt = str(c).split(" ")
    dt2 = dt[0].split("-")
    
    
    file = open(filename, 'r') 

    for line in file:
                
        l = line.split(" ")
        if l[0] >= '1' and l[0] <= '9':
            data_list.append(l[0])
                        
            
    for i in data_list:
        isplit = i.split('-')

#       Checking format (yyyy-mm-dd) and validity of date

        if len(isplit[0]) == len('0000') and len(isplit[1]) == len('00') and len(isplit[2]) == len('00'):
            
            if (int(isplit[1]) > 0 and int(isplit[1]) <= 12):
                
                if (isplit[1] in days31 and (int(isplit[2]) > 0 and int(isplit[2]) <= 31)) or (isplit[1] in days30 and (int(isplit[2]) > 0 and int(isplit[2]) <= 30)) or (isplit[1] in days28 and (int(isplit[2]) > 0 and int(isplit[2]) <= 28)):
                    continue
                else:
                    return("Invalid date at: ",i)
            else:
                return("Invalid month at: ",i)
        else:
            return("Invalid format at: ",i)
    
    
    val = check_future_date(data_list,dt2)
    
    file.close()

    if val != True:
        return "Invalid date (future date) at: ", val




#########################

def check_future_date(data_list,dt2):

    for i in range(0,len(data_list)):
        d = data_list[i].split('-')

        if datetime.date(int(d[0]),int(d[1]),int(d[2])) > datetime.date(int(dt2[0]),int(dt2[1]),int(dt2[2])):
            d = data_list[i]
            return d

    return True





if __name__ == "__main__":

   val = check_date('logs.txt')

   if val != None:
       print(val)

