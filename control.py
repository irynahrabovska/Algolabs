from lab1 import find_unsorted_subarray

def analyze_altitude_data():
    print("Система контролю")

    try:
        raw_input = input("\nВведіть дані: ")
        altitude_log = [int(x) for x in raw_input.split()]
        
    except ValueError:
        print("Помилка, введіть цілі числа")
        return

    if not altitude_log:
        print("\n Ви нічого не ввели. Спробуйте ще раз.")
        return

    print(f"Аналізуємо масив: {altitude_log}")

    start_index, end_index = find_unsorted_subarray(altitude_log)

    print("-" * 40)
    
    if start_index == -1:
        print("Політ проходить ідеально")
    else:
        print("Виявлено збій у даних")
        
        bad_segment = altitude_log[start_index : end_index + 1]

        print(f"Початок збою: {start_index}")
        print(f"Кінець збою:  {end_index}")
        print(f"Проблемна ділянка даних: {bad_segment}")
        
if __name__ == "__main__":
    analyze_altitude_data()