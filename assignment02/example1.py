
########### MOMINA ATIF DAR P18-0030

#import sys

#filename = sys.argv[1]

############################


def check_email(email):

    if '@' not in email:
        return "Invalid email. Please try again."

    username = email.split('@')[0]

    if username == "":
        return "Invalid username. Please try again.."
    
    for i in username:
                
        if i == '.' or i == '_' or (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
            continue
        else:
            return("Invalid username. Please try again..")
    
    domain = email.split('@')[1]
    s = check_domain(domain)
    
    if s != None:
         return s

###############################

def check_domain(domain):
    domain = '@'+domain
    l = ['@gmail.com','@outlook.com','@yahoo.com','@hotmail.com']

    if domain not in l:
        return 'Invalid domain. Please try again'
    else:
        return 'Valid email'

###############################

if __name__ == "__main__":

    file = open('data.txt', 'r')

    for line in file:
        line = line[:-1]
        ret = check_email(line)
        print(line+" - "+ret)

    file.close()
