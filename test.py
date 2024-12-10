import csv

def calculate_average_test_scores(file_path):
    total_scores = []

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                test_scores = [
                    float(row['Test1']),
                    float(row['Test2']),
                    float(row['Test3']),
                    float(row['Test4'])
                ]
                average_score = sum(test_scores) / len(test_scores)
                total_scores.append(average_score)
            except KeyError as e:
                print(f"Отсутствует столбец: {e}")
            except ValueError:
                print(f"Ошибка преобразования значения в строке: {row}")

    overall_average = sum(total_scores) / len(total_scores) if total_scores else 0
    return overall_average

file_path = 'grades.csv'
average_score = calculate_average_test_scores(file_path)
print(f"Среднее арифметическое оценок за тесты: {average_score:.2f}")

def get_letter_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

letter_grade = get_letter_grade(average_score)
print(f"Буквенная оценка: {letter_grade}")
