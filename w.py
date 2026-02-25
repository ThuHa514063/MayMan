import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="centered")

# --- CSS & JS: HIỆU ỨNG HOA ĐÀO RƠI + ÂM THANH + LAYOUT ---
st.markdown("""
    <style>
    /* Nền đỏ Tết */
    .stApp {
        background: radial-gradient(circle, #b71c1c 0%, #7f0000 100%);
        overflow: hidden;
    }

    /* Hiệu ứng rung lắc ống quẻ */
    @keyframes shake-shaker {
        0% { transform: rotate(0deg); }
        25% { transform: rotate(15deg) translateY(-10px); }
        50% { transform: rotate(-15deg) translateY(5px); }
        75% { transform: rotate(10deg) translateY(-5px); }
        100% { transform: rotate(0deg); }
    }
    .shaker-box { font-size: 100px; text-align: center; margin: 20px auto; }
    .shaking-active { animation: shake-shaker 0.15s infinite; }

    /* Hiệu ứng hoa rơi (Falling Flowers) */
    .falling {
        position: fixed; top: -10%; z-index: 9999;
        user-select: none; cursor: default;
        animation: fall linear infinite;
    }
    @keyframes fall {
        to { transform: translateY(110vh) rotate(360deg); }
    }

    /* LAYOUT KẾT QUẢ THEO PHÁC THẢO */
    .result-container {
        display: flex; background: white; border: 8px double #ffd700;
        border-radius: 15px; width: 100%; max-width: 450px;
        margin: 20px auto; box-shadow: 0 15px 40px rgba(0,0,0,0.5); overflow: hidden;
    }
    .card-left {
        flex: 1; background: #d32f2f; color: #ffeb3b;
        writing-mode: vertical-rl; text-orientation: upright;
        display: flex; align-items: center; justify-content: center;
        font-size: 2rem; font-weight: bold; padding: 15px; border-right: 4px solid #ffd700;
    }
    .card-right { flex: 2.5; display: flex; flex-direction: column; background-color: #fffaf0; }
    .wish-top {
        flex: 1; display: flex; align-items: center; justify-content: center;
        padding: 15px; font-size: 1.5rem; font-weight: 800; color: #b71c1c;
        border-bottom: 2px dashed #d32f2f; text-align: center;
    }
    .image-bottom { flex: 1.5; padding: 10px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 120px; border-radius: 10px; }

    .title-tet { color: #ffeb3b; text-align: center; font-size: 2.5rem; font-weight: bold; text-shadow: 2px 2px #333; }
    </style>

    <script>
    // Hàm tạo hoa đào rơi
    function createFlower() {
        const icons = ['🌸', '🧧', '🌼'];
        const flower = document.createElement('div');
        flower.className = 'falling';
        flower.innerText = icons[Math.floor(Math.random() * icons.length)];
        flower.style.left = Math.random() * 100 + 'vw';
        flower.style.fontSize = Math.random() * 20 + 10 + 'px';
        flower.style.animationDuration = Math.random() * 3 + 2 + 's';
        flower.style.opacity = Math.random();
        document.body.appendChild(flower);
        setTimeout(() => { flower.remove(); }, 5000);
    }
    setInterval(createFlower, 300);
    </script>
    """, unsafe_allow_html=True)

# --- HÀM CHÈN ÂM THANH ---
def play_sound(sound_url):
    sound_html = f"""
        <audio autoplay>
            <source src="{sound_url}" type="audio/mp3">
        </audio>
    """
    st.markdown(sound_html, unsafe_allow_html=True)

# --- QUẢN LÝ TRẠNG THÁI ---
if 'status' not in st.session_state:
    st.session_state.status = 'idle'

data = [
    {"money": "LÌ XÌ 50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
    {"money": "LÌ XÌ 100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
    {"money": "LÌ XÌ 200K", "wish": "SỨC KHỎE DỒI DÀO", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
    {"money": "LÌ XÌ 500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
]

# --- GIAO DIỆN CHÍNH ---
if st.session_state.status == 'idle':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ KHAI XUÂN 🧧</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker-box">🏺</div>', unsafe_allow_html=True)
    if st.button("🏮 NHẤN ĐỂ XÓC QUẺ 🏮", use_container_width=True):
        st.session_state.status = 'shaking'
        st.rerun()

elif st.session_state.status == 'shaking':
    st.markdown('<div class="title-tet">ĐANG XÓC QUẺ...</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker-box shaking-active">🏺</div>', unsafe_allow_html=True)
    
    # Phát âm thanh xóc quẻ (Sử dụng link âm thanh online)
    play_sound("https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3")
    
    time.sleep(2.5)
    st.session_state.result = random.choice(data)
    st.session_state.status = 'result'
    st.rerun()

elif st.session_state.status == 'result':
    st.markdown('<div class="title-tet">KẾT QUẢ CỦA BẠN</div>', unsafe_allow_html=True)
    res = st.session_state.result
    
    st.markdown(f"""
        <div class="result-container">
            <div class="card-left">{res['money']}</div>
            <div class="card-right">
                <div class="wish-top">{res['wish']}</div>
                <div class="image-bottom"><img src="{res['img']}"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧧 XIN QUẺ LẠI"):
        st.session_state.status = 'idle'
        st.rerun()
    st.balloons()