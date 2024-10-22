def customer_support_simulator(questions):
    # Определяем ключевые слова и ответы
    responses = [
        ("ошибка", "Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой."),
        ("заказ", "Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен."),
        ("вернуть", "Вы можете вернуть товар в течение 14 дней с момента получения.")
    ]
    default_response = "Благодарим вас за обращение. Ваш вопрос передан специалистам."

    # Список для хранения ответов
    answers = []

    # Проходим по каждому вопросу
    for question in questions:
        # Приводим вопрос к нижнему регистру для проверки ключевых слов
        lower_question = question.lower()

        # Проверяем ключевые слова в порядке приоритета
        answer_found = False
        for keyword, response in responses:
            if keyword in lower_question:
                answers.append(response)
                answer_found = True
                break

        # Если ни одно ключевое слово не найдено, даем стандартный ответ
        if not answer_found:
            answers.append(default_response)

    return answers
