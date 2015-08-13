# '''
# Thomas Jackson
# 08/12/2015
# DPW
# Simple Form
# '''
# from main import MainHandler
# class View(MainHandler):
#     def __init__(self):
#         self.page_head = '''<!DOCTYPE HTML>
# <html>
#     <head>
#         <title>Simple Form</title>
#     </head>
#     <body>'''
#         self.page_body = '''<form method="GET" action="">
#             <label for="user">User: </label><input type="text" name="user" />
#             <label for="email">Email: </label><input type="text" name="email" />
#             <input type="submit" value="submit" />
#             </form>'''
#
#         self.page_close = '''
#     </body>
# </html>
#         '''
#     def print_html(self):
#         # return self.page_head + self.page_body + self.page_close
#         if self.request.GET:
#             user = self.request.GET['user']
#             email = self.request.GET['email']
#             return self.page_head + user + email + self.page_body + self.page_close
#         else:
#             return self.page_head + self.page_body + self.page_close
