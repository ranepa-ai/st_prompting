import streamlit as st



def check_page():
    # Section: Knowledge Test
    st.header("5. Проверка знаний 🧠")
    # List of questions and correct answers
    questions = [
        {"question": "1. Что представляет собой промпт-инжиниринг?",
        "options": ["Создание языковых моделей", "Разработка и оптимизация промптов для эффективного использования генеративных моделей", 
                    "Исследование естественного языка", "Работа с графическими интерфейсами", "Ни один из перечисленных"],
        "correct_answer": "Разработка и оптимизация промптов для эффективного использования генеративных моделей"},

        {"question": "2. Что такое промт в промпт-инжиниринге?",
        "options": ["Ключ для шифрования данных", "Текстовый запрос для модели, используемый для взаимодействия с генеративными моделями", 
                    "Случайная последовательность слов", "Устаревшее название стрелки компаса", "Ни один из перечисленных"],
        "correct_answer": "Текстовый запрос для модели, используемый для взаимодействия с генеративными моделями"},

        {"question": "3. Из каких частей обычно состоит промпт?",
        "options": ["Загадка, отгадка, директива, форма ответа", "Нарратив, указание, вводная, типа ответа", 
                    "Директива, подсказка, форма ответа, тип ответа", "Задача, контекст, входные данные, индикатор вывода", "Нет правильного ответа"],
        "correct_answer": "Директива, подсказка, форма ответа, тип ответа"},

        {"question": "4. Что представляет собой техника Zero-shot prompting в промпт-инжиниринге?",
        "options": ["Метод, при котором используется только один промпт для задания вопроса модели", 
                    "Техника, при которой модели предоставляется возможность обучиться без промптов", 
                    "Подход, при котором модели предоставляется несколько промптов для обучения", 
                    "Метод, при котором модели дается возможность отвечать на вопросы, не видя обучающих примеров", "Нет правильного ответа"],
        "correct_answer": "Метод, при котором модели дается возможность отвечать на вопросы, не видя обучающих примеров"},

        {"question": "5. Как работает техника few-shot prompting в промпт-инжиниринге?",
        "options": ["Модель обучается с использованием всего одного промпта", 
                    "Модель обучается с использованием нескольких промптов для более точных ответов", 
                    "Применяется только в случае небольшого объема данных для обучения", 
                    "Модель обучается с использованием случайно выбранных промптов", "Нет правильного ответа"],
        "correct_answer": "Модель обучается с использованием нескольких промптов для более точных ответов"},

        {"question": "6. Что характеризует Chain-of-thought prompting (CoT) в промпт-инжиниринге?",
        "options": ["Применение только одного промпта для цепочки связанных вопросов.", 
                    "Последовательное использование промптов для формирования цепочки логически связанных вопросов", 
                    "Техника, при которой модель обучается только связанным вопросам", 
                    "Применение случайных промптов для формирования цепочки вопросов", "Нет правильного ответа"],
        "correct_answer": "Последовательное использование промптов для формирования цепочки логически связанных вопросов"},

        {"question": "7. Что представляет собой Retrieval Augmented Generation (RAG)?",
        "options": ["Метод поиска информации в интернете", "Метод генерации случайных текстов", 
                    "Метод, сочетающий поиск информации и генерацию текста", "Метод генерации изображений", "Нет правильного ответа"],
        "correct_answer": "Метод, сочетающий поиск информации и генерацию текста"},
    ]

    # Function to display and grade the quiz
    def display_and_grade_quiz():
        score = 0
        total_questions = len(questions)

        for i, q in enumerate(questions, 1):
            st.subheader(f"{i}. {q['question']}")
            selected_option = st.radio("Выберите один вариант ответа:", q["options"])
            if selected_option == q["correct_answer"]:
                st.success("Правильно! 🎉")
                score += 1
            else:
                st.error(f"Неверно. Правильный ответ: {q['correct_answer']}")

        st.markdown(f"**Вы ответили правильно на {score} из {total_questions} вопросов.**")
        if score == total_questions:
            st.success("Поздравляю! Вы успешно прошли тест. 🏆")
        else:
            st.warning("Попробуйте пройти тест еще раз, чтобы улучшить свой результат.")
    display_and_grade_quiz()

    

    # Text Prompt
    st.markdown("""
            Write Quiz Description and Instructions.
            """)

    # Create Placeholder to print test score
    scorecard_placeholder = st.empty()
    # Activate Session States
    ss = st.session_state
    # Initializing Session States
    if 'counter' not in ss:
        ss['counter'] = 0
    if 'start' not in ss:
        ss['start'] = False
    if 'stop' not in ss:
        ss['stop'] = False
    if 'refresh' not in ss:
        ss['refresh'] = False
    if "button_label" not in ss:
        ss['button_label'] = ['START', 'SUBMIT', 'RELOAD']
    if 'current_quiz' not in ss:
        ss['current_quiz'] = {}
    if 'user_answers' not in ss:
        ss['user_answers'] = []
    if 'grade' not in ss:
        ss['grade'] = 0


            # Function for button click
    def btn_click():
        ss.counter += 1
        if ss.counter > 2: 
            ss.counter = 0
            ss.clear()
        else:
            update_session_state()
            with st.spinner("*this may take a while*"):
                time.sleep(2)



                    # Function to update current session
    def update_session_state():
        if ss.counter == 1:
            ss['start'] = True
            ss.current_quiz = random.sample(quiz.sport_questions, 10)
        elif ss.counter == 2:
            # Set start to False
            ss['start'] = True 
            # Set stop to True
            ss['stop'] = True

            # Initializing Button Text
    st.button(label=ss.button_label[ss.counter], 
        key='button_press', on_click= btn_click)


# Function to display a question
def quiz_app():
    # create container
    with st.container():
        if (ss.start):
            for i in range(len(ss.current_quiz)):
                number_placeholder = st.empty()
                question_placeholder = st.empty()
                options_placeholder = st.empty()
                results_placeholder = st.empty()
                expander_area = st.empty()                
                # Add '1' to current_question tracking variable cause python starts counting from 0
                current_question = i+1
                # display question_number
                number_placeholder.write(f"*Question {current_question}*")
                # display question based on question_number
                question_placeholder.write(f"**{ss.current_quiz[i].get('question')}**") 
                # list of options
                options = ss.current_quiz[i].get("options")
                # track the user selection
                options_placeholder.radio("", options, index=1, key=f"Q{current_question}")
                nl(1)
                # Grade Answers and Return Corrections
                if ss.stop:
                    # Track length of user_answers
                    if len(ss.user_answers) < 10: 
                        # comparing answers to track score
                        if ss[f'Q{current_question}'] == ss.current_quiz[i].get("correct_answer"):
                            ss.user_answers.append(True)
                        else:
                            ss.user_answers.append(False)
                    else:
                        pass
                    # Results Feedback
                    if ss.user_answers[i] == True:
                        results_placeholder.success("CORRECT")
                    else:
                        results_placeholder.error("INCORRECT")
                    # Explanation of the Answer
                    expander_area.write(f"*{ss.current_quiz[i].get('explanation')}*")

    # calculate score
    if ss.stop:  
        ss['grade'] = ss.user_answers.count(True)           
        scorecard_placeholder.write(f"### **Your Final Score : {ss['grade']} / {len(ss.current_quiz)}**")        