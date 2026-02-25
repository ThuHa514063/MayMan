import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="centered")

# --- GIAO DIỆN CSS TÙY CHỈNH (TẾT VIBE) ---
st.markdown("""
    <style>
    /* Nền đỏ đậm chất Tết và hiệu ứng hoa mai rơi */
    .stApp {
        background: linear-gradient(rgba(183, 28, 28, 0.9), rgba(183, 28, 28, 0.9)), 
                    url('https://www.transparenttextures.com/patterns/paper-fibers.png');
        background-color: #b71c1c;
    }

    /* Tạo hiệu ứng chữ vàng thư pháp */
    .title-tet {
        color: #ffeb3b;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px #5d0000;
        margin-bottom: 30px;
    }

    /* Hiệu ứng Ống Quẻ Lắc */
    .shaker-container {
        text-align: center;
        padding: 20px;
    }
    
    .shaker-emoji {
        font-size: 100px;
        cursor: pointer;
        display: inline-block;
    }

    .shaking {
        animation: shake 0.5s infinite;
    }

    @keyframes shake {
        0% { transform: translate(1px, 1px) rotate(0deg); }
        10% { transform: translate(-1px, -2px) rotate(-1deg); }
        30% { transform: translate(3px, 2px) rotate(0deg); }
        50% { transform: translate(-1px, 2px) rotate(1deg); }
        70% { transform: translate(3px, 1px) rotate(-1deg); }
        100% { transform: translate(1px, -2px) rotate(0deg); }
    }

    /* LAYOUT KẾT QUẢ THEO PHÁC THẢO CỦA BẠN */
    .result-card {
        display: flex;
        background: white;
        border: 8px double #ffeb3b;
        border-radius: 10px;
        height: 350px;
        width: 100%;
        max-width: 500px;
        margin: auto;
        color: #333;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    .card-left {
        flex: 1;
        background-color: #d32f2f;
        color: #ffeb3b;
        writing-mode: vertical-rl;
        text-orientation: upright;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        font-weight: bold;
        border-right: 4px solid #ffeb3b;
        padding: 10px;
    }

    .card-right {
        flex: 2;
        display: flex;
        flex-direction: column;
    }

    .wish-section {
        flex: 1;
        padding: 20px;
        font-size: 1.5rem;
        font-weight: bold;
        color: #d32f2f;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        border-bottom: 2px solid #ddd;
    }

    .image-section {
        flex: 1.5;
        padding: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .image-section img {
        max-height: 100%;
        border-radius: 5px;
    }

    /* Ẩn nút mặc định của Streamlit để custom */
    div.stButton > button {
        background-color: #ffeb3b;
        color: #b71c1c;
        font-weight: bold;
        border: 2px solid #ffeb3b;
        border-radius: 20px;
        padding: 10px 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- KHỞI TẠO TRẠNG THÁI ---
if 'step' not in st.session_state:
    st.session_state.step = 'start'

# --- DỮ LIỆU ---
data = [
    {"money": "LÌ XÌ 50K", "wish": "Vạn Sự Như Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
    {"money": "LÌ XÌ 100K", "wish": "Tiền Vào Như Nước", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
    {"money": "LÌ XÌ 200K", "wish": "Tình Duyên Phơi Phới", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
    {"money": "LÌ XÌ 500K", "wish": "Đại Phú Đại Quý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
]

# --- MÀN HÌNH 1: LẮC QUẺ ---
if st.session_state.step == 'start':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ KHAI XUÂN 🧧</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="shaker-container">
            <div class="shaker-emoji">🏺</div>
            <p style="color: white; font-style: italic;">Thành tâm cầu nguyện rồi nhấn nút bên dưới...</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🧧 XIN QUẺ NGAY"):
        # Hiệu ứng lắc (giả lập bằng spinner)
        with st.spinner('Đang gieo quẻ...'):
            time.sleep(2)
            st.session_state.result = random.choice(data)
            st.session_state.step = 'result'
            st.rerun()

    st.snow() # Tạo hiệu ứng bông rơi (như hoa mai trắng/tuyết)

# --- MÀN HÌNH 2: KẾT QUẢ (THEO BẢN VẼ) ---
elif st.session_state.step == 'result':
    st.markdown('<div class="title-tet">CHÚC MỪNG TÂN XUÂN</div>', unsafe_allow_html=True)
    
    res = st.session_state.result
    
    # Render layout theo phác thảo của user
    st.markdown(f"""
        <div class="result-card">
            <div class="card-left">
                {res['money']}
            </div>
            <div class="card-right">
                <div class="wish-section">
                    {res['wish']}
                </div>
                <div class="image-section">
                    <img src="{res['img']}">
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("🏮 GIEO LẠI QUẺ KHÁC"):
        st.session_state.step = 'start'
        st.rerun()

    st.balloons() # Hiệu ứng chúc mừng