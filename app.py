import streamlit as st

st.set_page_config(
    page_title="연애 코칭 앱",
    page_icon="💕",
)

st.title("💕 연애 코칭 앱")

st.write("연애 고민을 입력하면 간단한 조언을 해드립니다.")

question = st.text_area(
    "고민 입력",
    placeholder="예: 썸녀가 답장이 느려요..."
)

if st.button("조언 받기"):

    if question == "":
        st.warning("고민을 입력해주세요.")
    else:

        text = question.lower()

        if "답장" in text:
            advice = """
            너무 자주 재촉하지 말고,
            상대의 생활 리듬을 존중하세요.
            가볍고 편한 분위기의 대화를 유지하는 게 중요합니다.
            """

        elif "고백" in text:
            advice = """
            완벽한 타이밍을 기다리기보다
            자연스럽고 솔직하게 표현하는 것이 좋습니다.
            """

        elif "이별" in text:
            advice = """
            감정을 억누르기보다 충분히 정리할 시간을 가지세요.
            자기 자신을 돌보는 것이 가장 중요합니다.
            """

        else:
            advice = """
            상대를 바꾸려 하기보다
            서로의 감정을 잘 이해하려는 대화가 중요합니다.
            """

        st.success("AI 연애 코칭 결과")
        st.write(advice)
