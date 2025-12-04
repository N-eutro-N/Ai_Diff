"""
Главный модуль лабораторной работы №2
Вариант 8
Автор: [Ваше имя]
"""

import os
import sys

# Добавляем папку modules в путь для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

def print_menu():
    """Вывод меню программы"""
    print("\n" + "="*60)
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Синтаксис языка Python. Интернированные и встроенные типы данных")
    print("="*60)
    print("1. Задача 1: Выражение 7 - 'too soon to tell'.replace('o','*').replace('* ','')")
    print("2. Задача 2: Выражение 1 - [115,202,192,334,257][:4]")
    print("3. Задача 3: Конвертация регистра строк")
    print("4. Задача 4: Преобразование списка чисел в одно число")
    print("5. Задача 5: Проверка существования ключа в словаре")
    print("6. Задача 6: Длина множества двумя способами")
    print("7. Задача 7: Работа с файлами + поиск частого слова")
    print("8. Задача 8: Работа со словарями через pickle")
    print("0. Выход")
    print("="*60)

def clear_screen():
    """Очистка экрана консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Основная функция программы"""
    clear_screen()
    
    while True:
        print_menu()
        
        try:
            choice = input("\nВыберите задачу (0-8): ").strip()
            
            if choice == '0':
                print("\nВыход из программы. До свидания!")
                break
            
            elif choice == '1':
                clear_screen()
                print("\n" + "="*60)
                print("ЗАДАЧА 1: Вычисление выражения")
                print("="*60)
                from modules import task1
                task1.run()
                input("\nНажмите Enter для возврата в меню...")
                clear_screen()
                
            elif choice == '2':
                clear_screen()
                print("\n" + "="*60)
                print("ЗАДАЧА 2: Вычисление выражения")
                print("="*60)
                from modules import task2
                task2.run()
                input("\nНажмите Enter для возврата в меню...")
                clear_screen()
                
            elif choice == '3':
                clear_screen()
                print("\n" + "="*60)
                print("ЗАДАЧА 3: Конвертация регистра строк")
                print("="*60)
                from modules import task3
                task3.run()
                input("\nНажмите Enter для возврата в меню...")
                clear_screen()
                
            elif choice == '4':
                clear_screen()
                print("\n" + "="*60)
                print("ЗАДАЧА 4: Преобразование списка чисел в одно число")
                print("="*60)
                from modules import task4
                task4.run()
                input("\nНажмите Enter для возврата в меню...")
                clear_screen()
                
            elif choice == '5':
                clear_screen()
                print("\n" + "="*60)
                print("ЗАДАЧА 5: Проверка ключа в словаре")
                print("="*60)
                from modules import task5
                task5.run()
                input("\nНажмите Enter для возврата в меню...")
                clear_screen()
                
            elif choice == '6':
                clear_screen()
                print("\n" + "="*60)
                print("ЗАДАЧА 6: Длина множества двумя способами")
                print("="*60)
                from modules import task6
                task6.run()
                input("\nНажмите Enter для возврата в меню...")
                clear_screen()
                
            elif choice == '7':
                clear_screen()
                print("\n" + "="*60)
                print("ЗАДАЧА 7: Работа с файлами + поиск частого слова")
                print("="*60)
                from modules import task7
                task7.run()
                input("\nНажмите Enter для возврата в меню...")
                clear_screen()
                
            elif choice == '8':
                clear_screen()
                print("\n" + "="*60)
                print("ЗАДАЧА 8: Работа со словарями через pickle")
                print("="*60)
                from modules import task8
                task8.run()
                input("\nНажмите Enter для возврата в меню...")
                clear_screen()
                
            else:
                print("\nОшибка: выберите число от 0 до 8")
                input("Нажмите Enter для продолжения...")
                clear_screen()
                
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break
        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")
            input("Нажмите Enter для продолжения...")
            clear_screen()

if __name__ == "__main__":
    # Создаем папку data, если она не существует
    if not os.path.exists('data'):
        os.makedirs('data')
    
    main()