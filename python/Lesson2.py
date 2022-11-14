#Lesson 2: String
'''
    - Creating String
    - Handling Problems with strings
    - 
'''
# way 1:
s = 'This is my string "a quotes"'
# way 2:
s2 = "This's my 2nd string"
print(s)
print(s2)
#s3 = "This is my string "a quotes""
# multiple lines string
block_of_string = '''
    jdsgfjsjfhdklg
    dhsgjsdjkgfdks
    dsjafgdjsakfgd"""""""""""hs
    dhsgfjksagjfhsakgf
    gdgfjsgkfjgs
'''
block_of_string_2 = """
    jdsgfjsjfhdklg
    dhsgjsdjkgfdks
    dsjafgdjsakfgd'''''hs
    dhsgfjksagjfhsakgf
    gdgfjsgkfjgs
"""
print(block_of_string)
print(block_of_string_2)
# embedding value to string
number = 5
sub_string = 'five'
string = 'I have %s oranges'
print(string % sub_string)
