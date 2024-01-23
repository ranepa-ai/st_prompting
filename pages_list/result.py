import streamlit as st

this_name = 'Основы промпт-инжиниринг💬🚀'

def result_page(df):
    # Section: Course Summary and Feedback
    st.header("Итоги 🏁")

    # Text content summarizing the course
    st.markdown("""
    Этот курс предоставил вам понимание важности и особенностей использования промптинга. Вы изучили базовые и продвинутые методы, а также способы неадекватного использования подсказок, чтобы распознавать и устранять возможные проблемы.

    Пройдя этот курс, вы приобрели навыки и знания, необходимые для применения методов промптинга для взаимодействия с моделями.

    При разработке материала мы руководствовались следующими источниками:
    - [Gigachat API - Prompt Engineering](https://developers.sber.ru/help/gigachat-api/prompt-engineering)
    - [Foundations of Prompt Engineering](https://explore.skillbuilder.aws/learn/course/17763/play/93257/foundations-of-prompt-engineering)
    - [Prompt Engineering: Advanced Techniques](https://www.mlq.ai/prompt-engineering-advanced-techniques/)
    - [Prompting Guide](https://www.promptingguide.ai/ru)

    CSI&NPS:

    Мы очень старались разработать этот курс для вас. Пожалуйста, ответьте на два вопроса:
    """)

    # CSI and NPS questions
    csi_rating = st.radio("Насколько вам понравился этот курс?", options=["1 (Совсем не понравился)", "2", "3", "4", "5 (Понравился очень)"])
    nps_rating = st.radio("Насколько вероятно, что вы порекомендуете этот курс своим знакомым?", options=["1 (Совсем не вероятно)", "2", "3", "4", "5 (Очень вероятно)"])

    # Display feedback based on ratings
    if csi_rating == "5 (Понравился очень)" and nps_rating == "5 (Очень вероятно)":
        st.success("Спасибо за высокие оценки! Мы очень рады, что вам понравился курс.")
    elif csi_rating in ["1 (Совсем не понравился)", "2", "3"] or nps_rating in ["1 (Совсем не вероятно)", "2", "3"]:
        st.error("Мы сожалеем, что курс не полностью соответствовал вашим ожиданиям. Мы постараемся улучшить его в будущем.")
    else:
        st.info("Спасибо за ваш отзыв! Ваши комментарии помогут нам сделать курс еще лучше.")

    df_sample = df.iloc[df[df['Name'] == this_name].index[0]:]
    this_track = df_sample.Track.iloc[0]
    
    N_cards_per_row = 3
    n_place = 0

    st.header("Продолжайте практику!")
    print(df_sample)

    if len(df_sample[df_sample['Name'] == this_track]) > 1:
        df_sample_new = df_sample[df_sample.Track==this_track].iloc[1:].reset_index(drop=True)
    else:
         this_track = df_sample.Track.iloc[1]
         df_sample_new = df_sample[df_sample.Track==this_track].reset_index(drop=True)
    cols = st.columns(N_cards_per_row, gap="large")
    print(df_sample_new)
    for n_row, row in df_sample_new.iterrows():
        
        st.write("")

        # URL изображения
        image_cot = f'https://github.com/Chetoff1228/images/blob/main/{row["Picture"]}.png?raw=true'

        with cols[n_place % N_cards_per_row]:
            st.markdown(f"**{row['Name']}**")
            st.markdown(f'<a href="{row["Source"]}"><img src="{image_cot}" alt="Foo" width="275" height="250"/></a>', unsafe_allow_html=True)
            st.caption(f"**{row['Caption'].strip()}**")
        n_place += 1
        
    st.write("---")