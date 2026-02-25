import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="centered")

# --- TOÀN BỘ CSS & JS (HOA ĐÀO RƠI + PHÁO HOA + LAYOUT) ---
st.markdown("""
    <style>
    /* Nền đỏ Tết */
    .stApp {
        background: radial-gradient(circle, #b71c1c 0%, #7f0000 100%);
        overflow: hidden;
    }

    /* Hiệu ứng xóc ống quẻ */
    @keyframes shake-shaker {
        0% { transform: translate(0,0) rotate(0deg); }
        20% { transform: translate(-8px, 5px) rotate(-10deg); }
        40% { transform: translate(8px, -5px) rotate(10deg); }
        60% { transform: translate(-8px, -5px) rotate(-10deg); }
        80% { transform: translate(8px, 5px) rotate(10deg); }
        100% { transform: translate(0,0) rotate(0deg); }
    }
    .shaker-box { font-size: 100px; text-align: center; margin: 30px auto; pointer-events: none; }
    .shaking-active { animation: shake-shaker 0.1s infinite; }

    /* Hiệu ứng HOA ĐÀO & LÌ XÌ RƠI (MƯA) */
    .falling-item {
        position: fixed;
        top: -50px;
        z-index: 9999;
        pointer-events: none;
        animation: fall-animation linear infinite;
        user-select: none;
    }
    @keyframes fall-animation {
        0% { transform: translateY(0) rotate(0deg) translateX(0); opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg) translateX(30px); opacity: 0; }
    }

    /* LAYOUT KẾT QUẢ */
    .result-container {
        display: flex; background: white; border: 6px solid #ffd700;
        border-radius: 15px; width: 100%; max-width: 450px;
        margin: 20px auto; box-shadow: 0 15px 40px rgba(0,0,0,0.6); overflow: hidden;
    }
    .card-left {
        flex: 1; background: #d32f2f; color: #ffeb3b;
        writing-mode: vertical-rl; text-orientation: upright;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.8rem; font-weight: bold; padding: 20px; border-right: 4px solid #ffd700;
    }
    .card-right { flex: 2.5; display: flex; flex-direction: column; background-color: #fffaf0; }
    .wish-top {
        flex: 1; display: flex; align-items: center; justify-content: center;
        padding: 20px; font-size: 1.6rem; font-weight: 800; color: #b71c1c;
        border-bottom: 2px dashed #d32f2f; text-align: center;
    }
    .image-bottom { flex: 1.5; padding: 10px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 140px; border-radius: 10px; }

    .title-tet { color: #ffeb3b; text-align: center; font-size: 2.5rem; font-weight: bold; text-shadow: 2px 2px #000; margin-bottom: 10px;}
    </style>

    <script>
    // Hàm tạo mưa hoa đào và lì xì
    function createRain() {
        const items = ['🌸', '🧧', '🌸', '🌼', '🧧'];
        const container = window.parent.document.body; // Gắn vào body của Streamlit
        const item = document.createElement('div');
        item.className = 'falling-item';
        item.innerText = items[Math.floor(Math.random() * items.length)];
        item.style.left = Math.random() * 100 + 'vw';
        item.style.fontSize = Math.random() * 20 + 15 + 'px';
        item.style.animationDuration = Math.random() * 3 + 4 + 's';
        container.appendChild(item);
        setTimeout(() => { item.remove(); }, 6000);
    }
    setInterval(createRain, 250);
    </script>
    """, unsafe_allow_html=True)

# --- HÀM PHÁO HOA ---
def firecrackers_effect():
    st.components.v1.html("""
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            var end = Date.now() + (3 * 1000);
            (function frame() {
              confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0 }, colors: ['#ff0000', '#ffd700'] });
              confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1 }, colors: ['#ff0000', '#ffd700'] });
              if (Date.now() < end) { requestAnimationFrame(frame); }
            }());
        </script>
    """, height=0)

def play_sound(url):
    st.markdown(f'<audio autoplay><source src="{url}" type="audio/mp3"></audio>', unsafe_allow_html=True)

# --- LOGIC APP ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

data = [
    {"money": "LÌ XÌ 50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
    {"money": "LÌ XÌ 100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
    {"money": "LÌ XÌ 200K", "wish": "SỨC KHỎE DỒI DÀO", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
    {"money": "LÌ XÌ 500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
]

if st.session_state.page == 'home':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ KHAI XUÂN 🧧</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker-box">🏺</div>', unsafe_allow_html=True)
    if st.button("🏮 CHẠM ĐỂ XÓC QUẺ 🏮", use_container_width=True):
        st.session_state.page = 'shaking'
        st.rerun()

elif st.session_state.page == 'shaking':
    st.markdown('<div class="title-tet">ĐANG XÓC QUẺ...</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker-box shaking-active">🏺</div>', unsafe_allow_html=True)
    play_sound("https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3")
    time.sleep(2.5)
    st.session_state.result = random.choice(data)
    st.session_state.page = 'result'
    st.rerun()

elif st.session_state.page == 'result':
    st.markdown('<div class="title-tet">KẾT QUẢ CỦA BẠN</div>', unsafe_allow_html=True)
    firecrackers_effect() # Pháo hoa đỏ vàng nổ
    
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
        st.session_state.page = 'home'
        st.rerun()
