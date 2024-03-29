import streamlit as st

image_cot = 'https://github.com/Chetoff1228/images/blob/main/cot.png?raw=true'
image_gen_knowledge = 'https://github.com/Chetoff1228/images/blob/main/gen-know.png?raw=true'
image_zero_cot = 'https://github.com/Chetoff1228/images/blob/main/zero-cot.png?raw=true'

def advanced_page():
    # Section: Advanced prompting techniques
    st.header("4. Продвинутые техники промпт-инжиниринга 💡", divider='rainbow')

    st.markdown("""
    Базовые методы не всегда позволяют получить эффективные результаты. Поэтому в этом разделе мы расскажем о некоторых продвинутых техниках промптинга.
    """)

    # Subsection: Retrieval Augmented Generation (RAG)
    st.subheader("Дополненная поиском генерация — Retrieval Augmented Generation (RAG) 📥")

    st.markdown("""
    RAG — это метод, который сочетает в себе два основных подхода: поиск и генерацию. 
    То есть, генерация ответа осуществляется с учетом дополнительно найденной релевантной информации. 
    Таким образом, RAG обеспечивает более точные и информативные результаты.
                
    При использовании RAG сначала происходит поиск по базе данных или корпусу текстовых документов с использованием запроса. Затем полученная информация используется для формирования контекста, который затем подается в модель генерации текста. Этот двухэтапный процесс способствует более информативной и качественной генерации текста.

    RAG является более экономичным, поскольку не требует затрат на тонкую настройку модели. RAG также решает проблему частого изменения данных, поскольку он извлекает обновленную и актуальную информацию вместо того, чтобы полагаться на потенциально устаревшие наборы данных.

    В RAG внешние данные могут поступать из нескольких источников данных, таких как хранилище документов, базы данных или API. 

    """)

    # RAG diagram
    #st.image("rag_diagram.png", caption="Концептуальный процесс использования RAG с LLM.", use_column_width=True)


