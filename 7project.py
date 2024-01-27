letter='''   <name> 
           you are selected for interview 
           yyour date and tim is given below
        date:     <date>'''
name=input("enter the value of name\n")
date=input("enter the value of date\n")
letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)