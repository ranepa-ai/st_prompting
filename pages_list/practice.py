import streamlit as st
import requests


def generate_prompt_response(prompt, api_url='http://localhost:5001/generate'):
    payload = {"prompt": prompt}
    response = requests.post(api_url, json=payload)
    generated_text = response.text
    return generated_text


def practice_page():
    st.header("6. Практика 📡", divider='rainbow')

    # Задание 1: Генерация текста для рекламного объявления
    st.subheader("Задание 1: Генерация текста для рекламного объявления")

    ex_1 = """Вы - маркетолог в компании 'ИноТехИнновации', которая готовится представить новый гаджет - 'Умный Ассистент'
Этот устройство разработано для оптимизации офисных процессов.
Напишите запрос к GPT-модели, чтобы получить несколько креативных идей для текста рекламного объявления,
подчеркивающего уникальные возможности 'Умного Ассистента' и привлекающего внимание целевой аудитории."""
    st.markdown(ex_1)
    prompt_text_1 = st.text_area("   ")
    
    if st.button("Сгенерировать запрос 1"):
        generated_response_1 = generate_prompt_response(prompt_text_1 + '\nНапиши ответ на данный запрос')
        st.write("Сгенерированный текст:", generated_response_1)
        
        # Оценка результатов
        model_rating_1 = generate_prompt_response(f"Тебе сейчас предстоит оценить задачу и ответ студента к ней (число от 1 до 5 одним символом, где 1 это совершенно сторонний ответ который не соответвует теме или совершенно случайный, а 5 это высококачественный ответ)\nЗадача: {ex_1}\nРузультат: {generated_response_1}\n Оцените результат по 5-балльной шкале:\n")
        st.write("Оценка модели:", model_rating_1)

    # Задание 2: Анализ текста в социальных сетях
    st.subheader("Задание 2: Анализ текста в социальных сетях")
    ex_2 = """Ваша цель - исследовать обсуждение в социальных сетях на тему 'Эффективность дистанционного обучения'.
Напишите запрос к GPT-модели, чтобы получить краткую аналитическую сводку основных аргументов,
высказанных в последних обсуждениях в Twitter и Reddit на русском языке.
Определите ключевые слова, такие как 'online learning', 'удаленное обучение' и уточните временной диапазон
для анализа, например, последние 3 месяца."""
    st.write(ex_2)

    prompt_text_2 = st.text_area(" ")
    
    if st.button("Сгенерировать запрос 2"):
        generated_response_2 = generate_prompt_response(prompt_text_2)
        st.write("Сгенерированный текст:", generated_response_2)
        
        # Оценка результатов
        model_rating_2 = generate_prompt_response(f"Тебе сейчас предстоит оценить задачу и ответ студента к ней (число от 1 до 5 одним символом, где 1 это совершенно сторонний ответ который не соответвует теме или совершенно случайный, а 5 это высококачественный ответ)\nЗадача: {ex_2}\nРузультат: {generated_response_2}\n Оцените результат по 5-балльной шкале:\n")
        st.write("Оценка модели:", model_rating_2)

    # Задание 3: Генерация текста пресс-релиза с переводом
    st.subheader("Задание 3: Генерация текста пресс-релиза с переводом")
    ex_3 = """Ваша компания 'Глобальная Динамика' готовится представить новую корпоративную стратегию.
Вам необходимо сначала создать пресс-релиз на русском языке, а затем перевести его на английский.
Напишите запрос к GPT-модели, чтобы получить текст пресс-релиза на русском языке,
подчеркивая ключевые аспекты стратегии.
Затем запросите перевод этого текста на английский, уточнив важность сохранения корпоративной
терминологии и стиля в переводе."""
    st.write(ex_3)

    prompt_text_3 = st.text_area("  ")
    
    if st.button("Сгенерировать запрос 3"):
        generated_response_3 = generate_prompt_response(prompt_text_3)
        st.write("Сгенерированный текст:", generated_response_3)
        
        # Оценка результатов
        model_rating_3 = generate_prompt_response(f"Тебе сейчас предстоит оценить задачу и ответ студента к ней (число от 1 до 5 одним символом, где 1 это совершенно сторонний ответ который не соответвует теме или совершенно случайный, а 5 это высококачественный ответ)\nЗадача: {ex_3}\nРузультат: {generated_response_3}\n Оцените результат по 5-балльной шкале:\n")
        st.write("Оценка модели:", model_rating_3)