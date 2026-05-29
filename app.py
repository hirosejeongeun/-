import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Love Coach AI",
    page_icon="💕",
    layout="wide"
)

# -----------------------------
# 스타일
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #fffafc;
}

.big-title {
    font-size: 42px;
    font-weight: 800;
    color: #ff4b6e;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.result-box {
    background: #fff0f3;
    padding: 20px;
    border-radius: 12px;
    border-left: 6px solid #ff4b6e;
}

.small-text {
    color: gray;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:
    st.title("💕 Love Coach AI")

    st.write("연애 고민을 분석하고 코칭해주는 AI 앱")

    user_name = st.text_input("닉네임", "익명")

    relationship_stage = st.selectbox(
        "현재 상태",
        [
            "썸",
            "연애중",
            "짝사랑",
            "이별",
            "재회 고민",
            "소개팅"
        ]
    )

    st.divider()

    st.write("### 오늘의 연애 팁")

    tips = [
        "상대의 말투보다 감정을 읽어보세요.",
        "연애는 속도가 아니라 방향입니다.",
        "불안할수록 확인보다 대화를 선택하세요.",
        "상대의 시간을 존중하면 관계가 편해집니다."
    ]

    st.info(random.choice(tips))

# -----------------------------
# 제목
# -----------------------------
st.markdown('<p class="big-title">💕 Love Coach AI</p>', unsafe_allow_html=True)

st.write(f"안녕하세요, **{user_name}** 님.")
st.write("당신의 연애 고민을 분석해드릴게요.")

# -----------------------------
# 입력
# -----------------------------
question = st.text_area(
    "연애 고민 입력",
    height=180,
    placeholder="""
예시:
썸녀가 갑자기 답장이 느려졌어요.
제가 너무 들이대는 걸까요?
"""
)

# -----------------------------
# 분석 함수
# -----------------------------
def detect_emotion(text):

    score = 50

    negative_words = [
        "불안", "힘들", "이별", "답장", "읽씹",
        "무시", "싸움", "차였", "헤어", "외롭"
    ]

    positive_words = [
        "좋아", "행복", "설렌", "데이트",
        "고백", "잘됐", "사귐"
    ]

    for word in negative_words:
        if word in text:
            score -= 10

    for word in positive_words:
        if word in text:
            score += 10

    score = max(0, min(score, 100))

    return score

def detect_category(text):

    if "답장" in text or "읽씹" in text:
        return "연락 문제"

    elif "고백" in text:
        return "고백 고민"

    elif "이별" in text or "헤어" in text:
        return "이별/재회"

    elif "싸움" in text:
        return "갈등"

    else:
        return "일반 연애 고민"

def generate_coaching(category, emotion_score):

    if category == "연락 문제":
        return """
상대의 답장 속도만으로 마음을 단정하지 마세요.

지금은 감정 확인보다
편안한 흐름을 유지하는 것이 중요합니다.

연락 빈도를 줄이고
상대가 부담 없이 대화할 수 있는 분위기를 만들어보세요.
"""

    elif category == "고백 고민":
        return """
완벽한 타이밍만 기다리면
오히려 기회를 놓칠 수 있습니다.

중요한 건 거창한 이벤트보다
진심이 담긴 표현입니다.
"""

    elif category == "이별/재회":
        return """
재회는 조급함보다 거리 조절이 중요합니다.

감정적으로 매달리는 시기에는
오히려 관계가 더 멀어질 수 있습니다.

우선 자신의 생활 리듬을 회복하세요.
"""

    elif emotion_score < 30:
        return """
현재 감정 소모가 큰 상태로 보여요.

지금은 상대 반응 분석보다
스스로를 안정시키는 시간이 필요합니다.
"""

    else:
        return """
연애는 상대를 설득하는 과정이 아니라
서로를 이해하는 과정입니다.

감정보다 관계의 흐름을 보세요.
"""

def generate_reply_style(category):

    samples = {
        "연락 문제": [
            "오늘 많이 바빴어? 😊",
            "편할 때 답장해줘!",
            "너무 부담 갖진 마 ㅎㅎ"
        ],

        "고백 고민": [
            "너랑 같이 있으면 편하고 좋아.",
            "사실 요즘 더 신경 쓰여 🙂"
        ],

        "이별/재회": [
            "잘 지내고 있었어?",
            "갑자기 생각나서 연락했어."
        ],

        "갈등": [
            "내 입장만 생각했던 것 같아.",
            "우리 차분하게 이야기해볼까?"
        ]
    }

    return random.choice(samples.get(category, ["천천히 대화를 이어가 보세요."]))

# -----------------------------
# 버튼
# -----------------------------
if st.button("💕 AI 분석 시작", use_container_width=True):

    if question.strip() == "":
        st.warning("고민 내용을 입력해주세요.")
        st.stop()

    with st.spinner("AI가 연애 패턴 분석 중..."):

        emotion_score = detect_emotion(question)
        category = detect_category(question)
        coaching = generate_coaching(category, emotion_score)
        reply_tip = generate_reply_style(category)

    st.success("분석 완료")

    # -----------------------------
    # 상단 요약
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("감정 안정도", f"{emotion_score}%")

    with col2:
        st.metric("고민 유형", category)

    with col3:
        current_time = datetime.now().strftime("%H:%M")
        st.metric("분석 완료 시간", current_time)

    st.progress(emotion_score / 100)

    # -----------------------------
    # 탭
    # -----------------------------
    tab1, tab2, tab3 = st.tabs([
        "💡 AI 코칭",
        "📱 추천 답장",
        "🚨 관계 신호 분석"
    ])

    with tab1:

        st.markdown("""
        <div class="card">
        <h3>AI 연애 코칭</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="result-box">
            {coaching}
            </div>
            """,
            unsafe_allow_html=True
        )

    with tab2:

        st.markdown("""
        <div class="card">
        <h3>추천 답장 스타일</h3>
        </div>
        """, unsafe_allow_html=True)

        st.code(reply_tip)

    with tab3:

        st.markdown("""
        <div class="card">
        <h3>관계 위험 신호</h3>
        </div>
        """, unsafe_allow_html=True)

        if emotion_score < 30:
            st.error("감정 의존도가 높아질 가능성이 있습니다.")

        elif emotion_score < 50:
            st.warning("상대 반응에 지나치게 집중하고 있을 수 있습니다.")

        else:
            st.success("현재 관계 흐름은 비교적 안정적입니다.")

# -----------------------------
# 하단
# -----------------------------
st.divider()

st.caption("Love Coach AI • Streamlit Web App")
