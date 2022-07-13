# import requests
# from bs4 import BeautifulSoup
# url = "https://host-elterxrz-prod.prod.cywar.xyz:49817/"
# fireflies = "12431"
# method = "GET"
# session = requests.session()
# while True:
#     if method == "GET":
#         req = session.get(url+f"?FIREFLIES={fireflies}",verify=False)
#     elif method == "POST":
#         req = session.post("https://host-elterxrz-prod.prod.cywar.xyz:49817/",verify=False,data={'FIREFLIES':fireflies})
#     soup = BeautifulSoup(req.text,"html.parser")
#     soup = soup.find('canvas')
#     soup = soup.get('title')
#     fireflies = soup.split(" ")[1]
#     method = soup.split(" ")[0]
#     print(soup)

pass_strength = True
user_password = input("Password HERE -->> ")
if len(user_password) < 8:
    print("Password must be at least 8 characters")
    pass_strength = False
if user_password.islower():
    print("Password does not contain uppercase letters")
    pass_strength = False
if user_password.isupper():
    print("Password does not contain lowercase letters")
    pass_strength = False
if user_password.isdigit():
    print("Password does not contain lowercase or uppercase letters")
    pass_strength = False
if "0" not in user_password and \
    "1" not in user_password and \
    "2" not in user_password and \
    "3" not in user_password and \
    "4" not in user_password and \
    "5" not in user_password and \
    "6" not in user_password and \
    "7" not in user_password and \
    "8" not in user_password and \
    "9" not in user_password:
    print("Password must contain at least 1 digit")
    pass_strength = False
if pass_strength == True:
    print("Password is strong!")
else:
    print("Password is weak!")
4%0