# 6.4 Упростите код из 6.3 с помощью цикла и добавьте 5 определений
test_theory = {
    'Тестирование ПО': 'проверка соответствия реальных и ожидаемых результатов поведения программы, проводимая на конечном наборе тестов, выбранном определённым образом.',
    'Верификация': 'процесс оценки системы, чтобы понять, удовлетворяют ли результаты текущего этапа разработки условиям, которые были сформулированы в его начале.',
    'Валидация': 'это определение соответствия разрабатываемого ПО ожиданиям и потребностям пользователя, его требованиям к системе.',
    'Дефект (bug)': 'отклонение фактического результата от ожидаемого.',
    'Серьёзность (severity)': 'показатель степени ущерба, который наносится проекту существованием дефекта. Severity выставляется тестировщиком.',
    'Срочность (priority)': 'показывает, как быстро дефект должен быть устранён. Priority выставляется менеджером, тимлидом или заказчиком',
    'Стадии разработки ПО': 'этапы, которые проходят команды разработчиков ПО, прежде чем программа станет доступной для широкого круга пользователей.',
    'Требования': 'это спецификация (описание) того, что должно быть реализовано. Требования описывают то, что необходимо реализовать, без детализации технической стороны решения.',
    'Отчёт о дефекте (bug report)': 'документ, который содержит отчет о любом недостатке в компоненте или системе, который потенциально может привести компонент или систему к невозможности выполнить требуемую функцию.',
    'Принципы тестирования': 'тестирования демонстрирует наличие дефектов, исчерпывающее тестирование невозможно, раннее тестирование, скопление дефектов, парадокс пестицида, тестирование зависит от контекста, заблуждение об отсутствии ошибок'
}
for key, value in test_theory.items():
    print(f'\n{key} — {value}')