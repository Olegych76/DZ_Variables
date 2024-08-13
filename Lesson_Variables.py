dz_num = 12
hours_num = 1.5
name_course = "Python"

print("Курс: " + name_course + ',', "всего задач:" + str(dz_num) + ',', "затрачено часов:", str(hours_num) + ',',
      "среднее время выполнения", hours_num / dz_num, "часа.")

# вариант вывода через f-строки:
print(
    f"Курс: {name_course}, всего задач:{dz_num}, затрачено часов: {hours_num}, "
    f"среднее время выполнения {hours_num / dz_num} часа.")
