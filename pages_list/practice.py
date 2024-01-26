import streamlit as st
import requests


def generate_prompt_response(prompt, api_url='http://localhost:5001/generate'):
    payload = {"prompt": prompt}
    response = requests.post(api_url, json=payload)
    generated_text = response.text
    return generated_text



def practice_page():
    #st.header("Практика", divider='rainbow')
    # Задание 1
    st.subheader("Задание 1: Генерация Контента для Блога")
    prompt_1 = st.text_area(
        """
        Ваша задача - использовать llm prompt инжиниринг для генерации интересных и информативных статей 
        для блога по теме, которая вам интересна. Сформулируйте запросы, которые приведут к созданию 
        оригинального и привлекательного контента.
        """
    )
    if st.button("Сгенерировать ответ темы блога"):
        st.write(generate_prompt_response(prompt_1))

    # Задание 2
    st.subheader("Задание 2: Оптимизация Текстов для SEO")

    prompt_2 = st.text_area(
        """
        Вы работаете в маркетинговом агентстве, и ваш клиент хочет оптимизировать свой веб-контент для 
        поисковых систем. Используйте llm prompt инжиниринг, чтобы создать запросы для генерации 
        SEO-оптимизированных текстов и ключевых фраз.
        """
    )
    if st.button("Сгенерировать советы для оптимизации маркетинга"):
        st.write(generate_prompt_response(prompt_2))

    # Задание 3
    st.subheader("Задание 3: Создание Ответов для Чат-Бота")
    prompt_3 = st.text_area(
        """
        Вам поручено создать мета-описание для онлайн-магазина по продаже органических продуктов. 
        Воспользуйтесь llm prompt инжинирингом для формулировки краткого, но привлекательного описания, 
        содержащего ключевые слова, способствующие высокому рейтингу в поисковых системах. Обратите внимание на акцент 
        на органичность, качество и преимущества использования органических продуктов.
        """
    )
    if st.button("Сгенерировать описание магазина"):
        st.write(generate_prompt_response(prompt_3))