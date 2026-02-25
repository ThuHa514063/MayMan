import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="centered")

# --- KHỞI TẠO BIẾN LƯU TRỮ (DATABASE TẠM THỜI) ---
if 'lucky_list' not in st.session_state:
    st.session_state.lucky_list = [] # Lưu danh sách: [{"name": "A", "money": "50k"}, ...]
if 'state' not in st.session_state:
    st.session_state.state = 'input_name'
if 'current_user' not in st.session_state:
    st.session_state.current_user = ""

# --- CSS MƯA HOA ĐÀO & LAYOUT (GIỮ NGUYÊN PHONG CÁCH TẾT) ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #b71c1c 0%, #7f0000 100%); overflow-x: hidden; }
    
    .petal, .lixi {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall linear infinite;
    }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }

    .shaker { font-size: 100px; text-align: center; margin: 10px auto; display: block; }
    .shake-anim { animation: shake-crazy 0.1s infinite; }
    @keyframes shake-crazy {
        0% { transform: translate(1px, 1px) rotate(0deg); }
        50% { transform: translate(-3px, 2px) rotate(-10deg); }
        100% { transform: translate(1px, 1px) rotate(0deg); }
    }

    .result-card {
        display: flex; background: white; border: 6px solid #ffd700;
        border-radius: 15px; width: 100%; max-width: 450px; margin: auto; overflow: hidden;
    }
    .card-left {
        flex: 1; background: #d32f2f; color: #ffeb3b; writing-mode: vertical-rl; 
        text-orientation: upright; display: flex; align-items: center; justify-content: center;
        font-size: 1.8rem; font-weight: bold; padding: 20px; border-right: 4px solid #ffd700;
    }
    .card-right { flex: 2.5; display: flex; flex-direction: column; background-color: #fffaf0; }
    .wish-top {
        flex: 1; padding: 20px; font-size: 1.5rem; font-weight: bold; color: #b71c1c;
        border-bottom: 2px dashed #d32f2f; text-align: center; display: flex; align-items: center; justify-content: center;
    }
    .image-bottom { flex: 1.5; padding: 10px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 120px; }
    
    .title-tet { color: #ffeb3b; text-align: center; font-size: 2.2rem; font-weight: bold; text-shadow: 2px 2px #000; margin-bottom: 20px;}
    .stButton>button { background-color: #ffeb3b !important; color: #b71c1c !important; font-weight: bold !important; border-radius: 10px !important; }
    </style>

    <div class="petal" style="left:10%; animation-duration:8s;">🌸</div>
    <div class="lixi" style="left:30%; animation-duration:12s;">🧧</div>
    <div class="petal" style="left:50%; animation-duration:10s;">🌸</div>
    <div class="lixi" style="left:70%; animation-duration:9s;">🧧</div>
    <div class="petal" style="left:90%; animation-duration:11s;">🌸</div>
""", unsafe_allow_html=True)

# --- DỮ LIỆU ---
data = [
    {"money": "LÌ XÌ 50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
    {"money": "LÌ XÌ 100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
    {"money": "LÌ XÌ 200K", "wish": "SỨC KHỎE DỒI DÀO", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
    {"money": "LÌ XÌ 500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
]

# --- HÀM XỬ LÝ GIAO DIỆN ---

# 1. MÀN HÌNH NHẬP TÊN
if st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">🧧 NHẬP TÊN NHẬN LỘC 🧧</div>', unsafe_allow_html=True)
    name = st.text_input("Tên của bạn là gì?", placeholder="Nhập tên tại đây...", key="name_input")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏮 VÀO LẮC QUẺ", use_container_width=True):
            if name:
                st.session_state.current_user = name
                st.session_state.state = 'shaking'
                st.rerun()
            else:
                st.warning("Vui lòng nhập tên để nhận quẻ!")
    with col2:
        if st.button("📝 DS MAY MẮN", use_container_width=True):
            st.session_state.state = 'view_list'
            st.rerun()

# 2. MÀN HÌNH ĐANG LẮC
elif st.session_state.state == 'shaking':
    st.markdown(f'<div class="title-tet">ĐANG XÓC QUẺ CHO: {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker shake-anim">🏺</div>', unsafe_allow_html=True)
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3" type="audio/mp3"></audio>', unsafe_allow_html=True)
    
    time.sleep(2.5)
    result = random.choice(data)
    st.session_state.result = result
    
    # LƯU KẾT QUẢ VÀO DANH SÁCH
    st.session_state.lucky_list.append({
        "Tên": st.session_state.current_user,
        "Lì xì": result['money'],
        "Thời gian": time.strftime("%H:%M:%S")
    })
    
    st.session_state.state = 'result'
    st.rerun()

# 3. MÀN HÌNH KẾT QUẢ
elif st.session_state.state == 'result':
    st.markdown(f'<div class="title-tet">CHÚC MỪNG {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    res = st.session_state.result
    st.markdown(f"""
        <div class="result-card">
            <div class="card-left">{res['money']}</div>
            <div class="card-right">
                <div class="wish-top">{res['wish']}</div>
                <div class="image-bottom"><img src="{res['img']}"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🧧 LẮC LẠI (NHẬP TÊN MỚI)", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()
    if st.button("📝 XEM DANH SÁCH MAY MẮN", use_container_width=True):
        st.session_state.state = 'view_list'
        st.rerun()

# 4. MÀN HÌNH DANH SÁCH MAY MẮN
elif st.session_state.state == 'view_list':
    st.markdown('<div class="title-tet">📝 DANH SÁCH MAY MẮN 🧧</div>', unsafe_allow_html=True)
    
    if len(st.session_state.lucky_list) > 0:
        # Hiển thị bảng danh sách
        st.table(st.session_state.lucky_list)
    else:
        st.info("Chưa có ai lắc quẻ cả. Hãy là người đầu tiên!")
        
    if st.button("⬅️ QUAY LẠI", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()
