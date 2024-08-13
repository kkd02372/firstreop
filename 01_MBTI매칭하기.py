import streamlit as st

# MBTI 특성 및 추천
mbti_traits = {
    'ISTJ': '🔍 신중하고 실용적인 현실주의자. 계획적이며 책임감이 강해요.',
    'ISFJ': '🌸 친절하고 배려 깊은 수호자. 타인의 필요를 잘 이해해요.',
    'INFJ': '✨ 통찰력 있는 상담가. 깊이 있는 감성과 미래 지향적이죠.',
    'INTJ': '💡 전략가. 독창적이고 논리적이며, 목표 지향적이에요.',
    'ISTP': '🛠️ 실용적 문제 해결사. 즉흥적이고 독립적인 성향을 가지고 있어요.',
    'ISFP': '🎨 자유로운 영혼. 감성적이고 미적 감각이 뛰어나요.',
    'INFP': '🌈 이상주의자. 깊은 감정과 가치관을 중요시하며 창의적이에요.',
    'INTP': '🧠 분석가. 호기심 많고 독창적인 아이디어를 좋아해요.',
    'ESTP': '🚀 활동적이고 현실적인 문제 해결사. 즉각적인 피드백을 중요시해요.',
    'ESFP': '🎉 사교적이고 즐거운 성격. 사람들과의 상호작용을 즐기죠.',
    'ENFP': '🌟 열정적인 촉진자. 창의적이며 새로운 가능성을 탐색해요.',
    'ENTP': '🤔 혁신적인 발명가. 호기심 많고 논리적 사고를 중시해요.',
    'ESTJ': '📋 효율적인 관리자. 조직적이며 책임감이 강하고 실용적이에요.',
    'ESFJ': '💖 친근하고 협력적인 사람. 타인을 돕고 사회적 관계를 중요시해요.',
    'ENFJ': '🌟 카리스마 있는 리더. 타인의 발전을 돕고 공감능력이 뛰어나요.',
    'ENTJ': '🚀 대담한 전략가. 강력한 리더십을 가지고 있으며 목표를 위해 노력해요.'
}

# 가장 잘 맞는 유형과 맞지 않는 유형
compatibility = {
    'ISTJ': ['ESFP', 'ENFP'],
    'ISFJ': ['ENTP', 'ESTP'],
    'INFJ': ['ESTJ', 'ESFJ'],
    'INTJ': ['ESFP', 'ISFP'],
    'ISTP': ['ENFJ', 'INFP'],
    'ISFP': ['ENTJ', 'ESTJ'],
    'INFP': ['ESTJ', 'ENTJ'],
    'INTP': ['ESFJ', 'ISFJ'],
    'ESTP': ['INFJ', 'ISFJ'],
    'ESFP': ['INTJ', 'ISTJ'],
    'ENFP': ['ISTJ', 'ESTJ'],
    'ENTP': ['ISFJ', 'ESFJ'],
    'ESTJ': ['INFP', 'ISFP'],
    'ESFJ': ['INTP', 'INFP'],
    'ENFJ': ['ISTP', 'INTP'],
    'ENTJ': ['ISFP', 'INFP']
}

st.title('MBTI 성격 분석기 🔮')

name = st.text_input('이름을 입력해주세요: ')
mbti_type = st.selectbox(
    '당신의 MBTI 유형을 선택해주세요:',
    list(mbti_traits.keys())
)

if st.button('분석 결과 보기'):
    st.write(f'안녕하세요, {name}님! 👋 당신의 MBTI 유형은 **{mbti_type}**입니다. 😊')
    st.write(f'👉 {mbti_type} 유형의 특성: {mbti_traits[mbti_type]}')

    best_match = compatibility[mbti_type][0]
    worst_match = compatibility[mbti_type][1]

    st.write(f'🔍 **가장 잘 맞는 유형**: {best_match} 👫')
    st.write(f'🚫 **가장 맞지 않는 유형**: {worst_match} 😕')
