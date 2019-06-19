'''
Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов.
Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец.
Разрешается вывести пустой столбец после последнего пингвина.
Для упрощения рисования скопируйте пингвина.

Примеры:

Тест 1
Входные данные:
3

Вывод программы:
   _~_       _~_       _~_    
  (o o)     (o o)     (o o)   
 /  V  \   /  V  \   /  V  \  
/(  _  )\ /(  _  )\ /(  _  )\ 
  ^^ ^^     ^^ ^^     ^^ ^^   



Тест 2
Входные данные:
1

Вывод программы:
   _~_    
  (o o)   
 /  V  \  
/(  _  )\ 
  ^^ ^^
'''
num = input()
num = int(num)
print('   _~_\n  (o o)\n /  V  \n/(  _  )\\\n   ^^ ^^' * num)
input()
