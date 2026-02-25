import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="centered")

# --- HIỆU ỨNG MƯA HOA ĐÀO & LÌ XÌ (DÙNG CSS NGUYÊN BẢN) ---
# Mình rải sẵn các thẻ div với vị trí ngẫu nhiên để rơi liên tục
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #b71c1c 0%, #7f0000 100%); overflow: hidden; }
    
    /* Định nghĩa hiệu ứng rơi */
    .petal, .lixi {
        position: fixed;
        top: -10%;
        user-select: none;
        pointer-events: none;
        z-index: 9999;
        animation: fall linear infinite;
    }

    @keyframes fall {
        0% { transform: translateY(0) rotate(0deg); }
        100% { transform: translateY(110vh) rotate(360deg); }
    }

    /* Giao diện ống quẻ */
    .shaker { font-size: 100px; text-align: center; margin: 20px auto; display: block; }
    .shake-anim { animation: shake-crazy 0.1s infinite; }
    @keyframes shake-crazy {
        0% { transform: translate(1px, 1px) rotate(0deg); }
        20% { transform: translate(-3px, 0px) rotate(-5deg); }
        40% { transform: translate(3px, 2px) rotate(5deg); }
        60% { transform: translate(-3px, 1px) rotate(-5deg); }
        80% { transform: translate(3px, -2px) rotate(5deg); }
        100% { transform: translate(1px, 1px) rotate(0deg); }
    }

    /* BỐ CỤC KẾT QUẢ CHUẨN ẢNH PHÁC THẢO */
    .result-card {
        display: flex; background: white; border: 6px solid #ffd700;
        border-radius: 15px; width: 100%; max-width: 450px;
        margin: auto; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .card-left {
        flex: 1; background: #d32f2f; color: #ffeb3b;
        writing-mode: vertical-rl; text-orientation: upright;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.8rem; font-weight: bold; padding: 20px; border-right: 4px solid #ffd700;
    }
    .card-right { flex: 2.5; display: flex; flex-direction: column; background-color: #fffaf0; }
    .wish-top {
        flex: 1; padding: 20px; font-size: 1.5rem; font-weight: bold; color: #b71c1c;
        border-bottom: 2px dashed #d32f2f; text-align: center; display: flex; align-items: center; justify-content: center;
    }
    .image-bottom { flex: 1.5; padding: 10px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 120px; border-radius: 10px; }
    
    .title-tet { color: #ffeb3b; text-align: center; font-size: 2.5rem; font-weight: bold; text-shadow: 2px 2px #000; }
    </style>

    <div class="petal" style="left:5%; animation-duration:7s; animation-delay:1s;">🌸</div>
    <div class="lixi" style="left:15%; animation-duration:10s; animation-delay:2s;">🧧</div>
    <div class="petal" style="left:25%; animation-duration:8s; animation-delay:0s;">🌸</div>
    <div class="petal" style="left:40%; animation-duration:12s; animation-delay:3s;">🌸</div>
    <div class="lixi" style="left:55%; animation-duration:9s; animation-delay:1s;">🧧</div>
    <div class="petal" style="left:70%; animation-duration:11s; animation-delay:4s;">🌸</div>
    <div class="petal" style="left:85%; animation-duration:6s; animation-delay:2s;">🌸</div>
    <div class="lixi" style="left:95%; animation-duration:13s; animation-delay:0s;">🧧</div>
    <div class="petal" style="left:50%; animation-duration:15s; animation-delay:5s;">🌸</div>
    <div class="petal" style="left:33%; animation-duration:9s; animation-delay:2s;">🌸</div>
""", unsafe_allow_html=True)

# --- LOGIC APP ---
if 'state' not in st.session_state:
    st.session_state.state = 'home'

data = [
    {"money": "LÌ XÌ 50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
    {"money": "LÌ XÌ 100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
    {"money": "LÌ XÌ 500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
]

if st.session_state.state == 'home':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ ĐẦU NĂM 🧧</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker">🏺</div>', unsafe_allow_html=True)
    if st.button("🏮 NHẤN ĐỂ LẮC QUẺ 🏮", use_container_width=True):
        st.session_state.state = 'shaking'
        st.rerun()

elif st.session_state.state == 'shaking':
    st.markdown('<div class="title-tet">ĐANG XÓC QUẺ...</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker shake-anim">🏺</div>', unsafe_allow_html=True)
    # Phát âm thanh lạch cạch
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3" type="audio/mp3"></audio>', unsafe_allow_html=True)
    
    time.sleep(2.5)
    st.session_state.result = random.choice(data)
    st.session_state.state = 'result'
    st.rerun()

elif st.session_state.state == 'result':
    st.markdown('<div class="title-tet">QUẺ CỦA BẠN</div>', unsafe_allow_html=True)
    res = st.session_state.result
    
    # Hiển thị layout kết quả chuẩn
    st.markdown(f"""
        <div class="result-card">
            <div class="card-left">{res['money']}</div>
            <div class="card-right">
                <div class="wish-top">{res['wish']}</div>
                <div class="image-bottom"><img src="{res['img']}"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Nút quay lại
    if st.button("🧧 XIN QUẺ KHÁC"):
        st.session_state.state = 'home'
        st.rerun()
