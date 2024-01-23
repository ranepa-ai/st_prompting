import streamlit as st

def intro_page():
    st.header("LLM Prompt Инжиниринг✔️", divider='rainbow')
    st.subheader("Приветствую вас в главе **Введение**! 🌟")
    st.markdown("""
    Здесь мы рассмотрим, как основы llm prompt инжиниринга могут быть полезными в различных областях. 
    LLM (Language Model) - это мощный инструмент, способный генерировать текст на основе предоставленного контекста.

    **Промпт-инжиниринг** позволяет раскрыть потенциал генеративного ИИ, ставшего неотъемлемой частью современных технологий. 
    Вдохновленные высоким интересом к использованию генеративных моделей, мы создали курс, который поможет вам познакомиться с промпт-инжинирингом и его возможностями.

    На этом курсе вы научитесь создавать и оптимизировать **промпты (подсказки)** для различных моделей генеративного искусственного интеллекта. 
    Вы изучите принципы, методы и лучшие практики разработки эффективных подсказок. 
    Этот курс является базовым и рассчитан на начинающих пользователей, которые имеют мало опыта генерации контента.

    **Промпт (подсказка)** – текстовый запрос для модели. 
    *Чем точнее промпт, тем лучше результат, который выдает система.*

    **Промпт-инжиниринг** – процесс создания и оптимизации текстовых запросов (промптов) для эффективного использования генеративных моделей. 

    **Промпт-инженер** – специалист, который разрабатывает и оптимизирует промпты для эффективного использования моделей. 
    Вместо использования случайных или стандартных запросов, промпт-инженер фокусируется на создании таких промптов, которые максимально активируют специфические функции моделей. 
    Навыки промпт-инжиниринга помогают лучше понять возможности и ограничения моделей.

    **Зачем нужен промпт-инжиниринг?**
    - *Улучшение производительности:* эффективные подсказки улучшают результаты моделей, делая их более точными и релевантными.
    - *Понимание возможностей моделей:* промпт-инжиниринг помогает исследователям и разработчикам лучше понять, как использовать модели для специфических задач.

    **Где используется промпт-инжиниринг?**
    - *Исследования:* исследователи используют промпт-инжиниринг для улучшения функциональности моделей в различных областях, включая вопросно-ответные системы и генерацию текста.
    - *Разработка:* разработчики применяют методы промпт-инжиниринга для создания эффективных инструментов взаимодействия с моделями.

    Знание промпт-инжиниринга расширяет возможности в различных сферах, таких как исследования, работа с контентом, разработка приложений, анализ данных, машинное обучение и другие области, где используются генеративные модели.
    """)

    # Примеры
    st.subheader("""Рекомендации по созданию промптов:
        📄 **Пример 1: Генерация учебного материала**\n
        Представьте, что вам нужно подготовить учебный материал по новой теме. Вы можете использовать llm prompt инжиниринг для формулировки точных вопросов и получения информации для разработки материала.\n

        🤖 **Пример 2: Создание автокомплита для приложения**\n
        Если вы разрабатываете приложение с автокомплитом, llm prompt инжиниринг может помочь в создании эффективных запросов для получения точных и релевантных результатов.\n
        """
    )