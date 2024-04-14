# num = 0
#
# if num >= 0:
#      print ('Число больше, либо равно 0')
# else:
#     print ('Число отрицательное')

# def task_yes_no(str_1,str_2):
#     if str_1 in str_2:
#         print('ДА')
#     else:
#         print('НЕТ')
#
# task_yes_no(str_1='test', str_2='testing')

# num_float =-3.4
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('Ноль')
# else:
#     print('Число отрицательное')

# num = -2
# permit_print = False
#
# if num >= 0 and permit_print:
#     print ('num - положительное число')
# elif not permit_print:
#     print('Печать запрещена')


def student_rank (years_of_study):
    if years_of_study == 1 or years_of_study == 2 or years_of_study == 3 or years_of_study == 4:
        print ('Вы - бакалавр')
    elif years_of_study in range (5,7):
        print ('Вы - магистр')
    elif years_of_study in range (7,10):
        print ('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(9)

# num =99
#
# if num > 100 or num <-100:
#     print ('-')
# else:
#     print ('+')