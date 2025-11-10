import os
import datetime


class Calculator:
    def __init__(self):
        self.history = []
        self.history_file = "history.txt"
        self.load_history()
    
    def add(self, a, b):
        """Сложение двух чисел"""
        return a + b
    
    def subtract(self, a, b):
        """Вычитание двух чисел"""
        return a - b
    
    def multiply(self, a, b):
        """Умножение двух чисел"""
        return a * b
    
    def divide(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно!")
        return a / b
    
    def calculate(self, num1, operator, num2):
        """Выполняет вычисление и сохраняет в историю"""
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        
        if operator not in operations:
            raise ValueError("Неподдерживаемая операция!")
        
        try:
            result = operations[operator](num1, num2)
            # Форматируем запись для истории
            calculation = f"{num1} {operator} {num2} = {result}"
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            history_entry = f"[{timestamp}] {calculation}"
            
            # Добавляем в историю
            self.history.append(history_entry)
            
            # Сохраняем в файл
            self.save_to_file(history_entry)
            
            return result
            
        except Exception as e:
            error_msg = f"Ошибка: {str(e)}"
            print(error_msg)
            return None
    
    def show_history(self):
        """Показывает историю вычислений"""
        if not self.history:
            print("История пуста.")
            return
        
        print("\n" + "="*50)
        print("📜 ИСТОРИЯ ВЫЧИСЛЕНИЙ")
        print("="*50)
        
        # Показываем последние 10 записей
        recent_history = self.history[-10:] if len(self.history) > 10 else self.history
        
        for i, entry in enumerate(recent_history, 1):
            print(f"{i:2d}. {entry}")
        
        if len(self.history) > 10:
            print(f"\n... показаны последние 10 из {len(self.history)} записей")
    
    def clear_history(self):
        """Очищает историю вычислений"""
        self.history.clear()
        # Очищаем файл
        try:
            open(self.history_file, 'w').close()
            print("📝 История очищена.")
        except Exception:
            print("⚠️ Не удалось очистить файл истории.")
    
    def save_to_file(self, entry):
        """Сохраняет запись в файл"""
        try:
            with open(self.history_file, 'a', encoding='utf-8') as f:
                f.write(entry + '\n')
        except Exception:
            print("⚠️ Не удалось сохранить в файл.")
    
    def load_history(self):
        """Загружает историю из файла при запуске"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.history = [line.strip() for line in f.readlines() if line.strip()]
            except Exception:
                print("⚠️ Не удалось загрузить историю.")


def main():
    calc = Calculator()
    
    print("="*60)
    print("🧮 КАЛЬКУЛЯТОР С ИСТОРИЕЙ - Командная разработка УП.05")
    print("="*60)
    
    while True:
        print("\n" + "-"*40)
        print("Выберите операцию:")
        print("1. ➕ Сложение")
        print("2. ➖ Вычитание") 
        print("3. ✖️  Умножение")
        print("4. ➗ Деление")
        print("5. 📜 Показать историю")
        print("6. 🗑️  Очистить историю")
        print("7. 🚪 Выход")
        print("-"*40)
        
        choice = input("Ваш выбор (1-7): ").strip()
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                
                operators = {'1': '+', '2': '-', '3': '*', '4': '/'}
                operator = operators[choice]
                
                result = calc.calculate(num1, operator, num2)
                if result is not None:
                    print(f"\n✅ Результат: {num1} {operator} {num2} = {result}")
                    
            except ValueError:
                print("❌ Ошибка: Пожалуйста, введите корректное число!")
            except Exception as e:
                print(f"❌ Произошла ошибка: {str(e)}")
                
        elif choice == '5':
            calc.show_history()
            
        elif choice == '6':
            confirm = input("Вы уверены, что хотите очистить историю? (да/нет): ")
            if confirm.lower() in ['да', 'yes', 'y', 'д']:
                calc.clear_history()
            else:
                print("📝 Очистка истории отменена.")
                
        elif choice == '7':
            print("\n👋 Спасибо за использование калькулятора!")
            print(f"📊 Всего выполнено вычислений: {len(calc.history)}")
            break
            
        else:
            print("❌ Неверный выбор. Пожалуйста, выберите число от 1 до 7.")


if __name__ == "__main__":
    main()