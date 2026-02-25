import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="centered")

# --- CSS NÂNG CAO CHO HIỆU ỨNG RUNG LẮC VÀ LAYOUT ---
st.markdown("""
    <style>
    /* Nền đỏ tết với hoa văn ẩn */
    .stApp {
        background: radial-gradient(circle, #b71c1c 0%, #7f0000 100%);
    }

    /* Hiệu ứng rung lắc ống quẻ */
    @keyframes shake-shaker {
        0% { transform: rotate(0deg); }
        25% { transform: rotate(15deg) translateY(-10px); }
        50% { transform: rotate(-15deg) translateY(5px); }
        75% { transform: rotate(10deg) translateY(-5px); }
        100% { transform: rotate(0deg); }
    }

    .shaker-box {
        font-size: 120px;
        text-align: center;
        margin: 20px auto;
        display: block;
        width: fit-content;
    }

    .shaking-active {
        animation: shake-shaker 0.2s infinite;
    }

    /* Tiêu đề thư pháp */
    .title-tet {
        color: #ffeb3b;
        text-align: center;
        font-family: 'cursive';
        font-size: 3.5rem;
        text-shadow: 3px 3px 0px #333;
        margin-bottom: 10px;
    }

    /* BỐ CỤC KẾT QUẢ (THEO PHÁC THẢO USER) */
    .result-container {
        display: flex;
        background: #fff;
        border: 10px double #ffd700;
        border-radius: 15px;
        width: 100%;
        max-width: 500px;
        margin: 20px auto;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        overflow: hidden;
        animation: slideIn 0.8s ease-out;
    }

    @keyframes slideIn {
        from { transform: translateY(50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    .card-left {
        flex: 1;
        background: #d32f2f;
        color: #ffeb3b;
        writing-mode: vertical-rl;
        text-orientation: upright;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: bold;
        padding: 20px;
        border-right: 5px solid #ffd700;
    }

    .card-right {
        flex: 2.5;
        display: flex;
        flex-direction: column;
        background-color: #fff9e6; /* Màu giấy cũ */
    }

    .wish-top {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        font-size: 1.6rem;
        font-weight: 800;
        color: #b71c1c;
        border-bottom: 3px dashed #d32f2f;
        text-align: center;
    }

    .image-bottom {
        flex: 2;
        padding: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .image-bottom img {
        max-width: 80%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- QUẢN LÝ TRẠNG THÁI ---
if 'status' not in st.session_state:
    st.session_state.status = 'idle'  # idle, shaking, result

# --- DỮ LIỆU ---
data = [
    {"money": "LÌ XÌ 50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
    {"money": "LÌ XÌ 100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
    {"money": "LÌ XÌ 200K", "wish": "TÌNH DUYÊN PHƠI PHỚI", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
    {"money": "LÌ XÌ 500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
]

# --- LOGIC HIỂN THỊ ---

if st.session_state.status == 'idle':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ KHAI XUÂN 🧧</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker-box">🏺</div>', unsafe_allow_html=True)
    
    if st.button("🏮 NHẤN ĐỂ XÓC QUẺ 🏮", use_container_width=True):
        st.session_state.status = 'shaking'
        st.rerun()

elif st.session_state.status == 'shaking':
    st.markdown('<div class="title-tet">ĐANG XÓC QUẺ...</div>', unsafe_allow_html=True)
    # Hiệu ứng rung lắc bằng CSS class
    st.markdown('<div class="shaker-box shaking-active">🏺</div>', unsafe_allow_html=True)
    
    # Giả lập thời gian xóc quẻ
    time.sleep(2)
    st.session_state.result = random.choice(data)
    st.session_state.status = 'result'
    st.rerun()

elif st.session_state.status == 'result':
    st.markdown('<div class="title-tet">QUẺ CỦA BẠN ĐÂY</div>', unsafe_allow_html=True)
    
    res = st.session_state.result
    # Layout đúng theo phác thảo của user
    st.markdown(f"""
        <div class="result-container">
            <div class="card-left">{res['money']}</div>
            <div class="card-right">
                <div class="wish-top">{res['wish']}</div>
                <div class="image-bottom">
                    <img src="{res['img']}">
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🧧 XIN QUẺ LẠI"):
        st.session_state.status = 'idle'
        st.rerun()
    
    st.balloons()

# Hiệu ứng hoa mai rơi xuyên suốt
st.snow()