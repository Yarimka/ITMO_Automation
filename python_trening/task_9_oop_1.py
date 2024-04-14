# class Input:
#     def __init__(self,loc,text):
#         self.loc = loc
#         self.text = text
#
# search = Input ('input#search','Поиск ')
#
# print(search.text + search.loc)


# class Button:
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text
#
#
# home = Button ('Button#home', 'Домой ')
#
# print(home.text + home.loc)

# class Title:
#     def __init__(self, loc, text):
#         self.loc = loc
#         self.text = text
#
#
# home = Title ('Title#home', 'Заголовок ')
#
# print(home.text + home.loc)

class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


home = Link ('link#home', 'Домой ')

print(home.text + home.loc)