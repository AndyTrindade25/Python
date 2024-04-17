import re

def check_character(string):
    rule = re.compile(r'[^a-zA-z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character("ASDIAJISDJsdjnsda2125"))
print(check_character("#@!#{};<>"))