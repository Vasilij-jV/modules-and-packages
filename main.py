# импорт модуля
import modules

modules.first_function()

modules.second_function()

# импорт модуля и его переименование
import modules as md

md.first_function()

md.second_function()

# импортирование переменных модуля

from modules import first_function, second_function

first_function()

second_function()

# импортирование переменных модуля и их переименование

from modules import first_function as ff, second_function as sf

ff()

sf()