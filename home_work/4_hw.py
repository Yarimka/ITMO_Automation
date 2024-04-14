# Задание 1

# class rectangle():
#     def __init__(self, breadth, length):
#         self.breadth = breadth
#         self.length = length
#
#     def area(self):
#         return self.breadth * self.length
#     def perimeter(self):
#         return self.breadth * 2 + self.length * 2
#
# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите ширину прямоугольника: "))
# obj = rectangle(a, b)
# print("Площадь прямоугольника:", obj.area())
# print("Периметр прямоугольника:", obj.perimeter())
#
# print ()

# Задание 2
# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         return self.a + self.b
#     def multiplication(self):
#         return self.a * self.b
#     def subtraction(self):
#         return self.a / self.b
#     def perimeter(self):
#         return self.a - self.b
#
# a = int(input("Введите число 1: "))
# b = int(input("Введите число 2: "))
#
# obj = Math(a, b)
# print("результат сложения:", obj.addition())
# print("результат умножения:", obj.multiplication())
# print("результат деления:", obj.subtraction())
# print("результат вычитания:", obj.perimeter())
# print ()

# Задание 3
class ButtonOne:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

TextBox = ButtonOne ('Text Box', 'Кнопка', '')
home = ButtonOne ('Text Box','Кнопка', '')
print(home.text)
print(TextBox.click())

print('\n')

class ButtonTwo:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

CheckBox = ButtonTwo ('Check Box', 'Кнопка', '')
home = ButtonTwo ('Check Box','Кнопка', '')
print(home.text)
print(CheckBox.click())

print('\n')
class ButtonThree:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

RadioButton = ButtonThree ('Radio Botton', 'Кнопка', '')
home = ButtonThree ('Radio Botton','Кнопка', '')
print(home.text)
print(RadioButton.click())

print('\n')

class ButtonFour:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

WebTables = ButtonFour ('Web Tables', 'Кнопка', '')
home = ButtonFour ('Web Tables','Кнопка', '')
print(home.text)
print(WebTables.click())

print('\n')

class ButtonFive:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

Buttons = ButtonFive('Buttons', 'Кнопка', '')
home = ButtonFive ('Buttons','Кнопка', '')
print(home.text)
print(Buttons.click())

print('\n')

class ButtonSix:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

Links = ButtonSix('Links', 'Кнопка', '')
home = ButtonSix ('Links','Кнопка', '')
print(home.text)
print(Links.click())

print('\n')

class ButtonSeven:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

BrokenLinksImages = ButtonSeven('Broken Links - Images', 'Кнопка', '')
home = ButtonSeven ('Broken Links - Images','Кнопка', '')
print(home.text)
print(BrokenLinksImages.click())

print('\n')

class ButtonEight:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

UploadAndDownload = ButtonEight('Upload And Download', 'Кнопка', '')
home = ButtonEight ('Upload And Download','Кнопка', '')
print(home.text)
print(UploadAndDownload.click())

print('\n')

class ButtonNine:
    def __init__(self,text,type,loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

DynamicProperties = ButtonNine('Dynamic Properties', 'Кнопка', '')
home = ButtonNine ('Dynamic Properties','Кнопка', '')
print(home.text)
print(DynamicProperties.click())