import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="centered")

# --- KHỞI TẠO DỮ LIỆU ---
if 'lucky_list' not in st.session_state:
    st.session_state.lucky_list = []
if 'state' not in st.session_state:
    st.session_state.state = 'input_name'
if 'current_user' not in st.session_state:
    st.session_state.current_user = ""

# --- CSS TÙY CHỈNH ---
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: url("https://image.dienthoaivui.com.vn/x,webp,q90/https://dashboard.dienthoaivui.com.vn/uploads/dashboard/editor_upload/background-tet-050.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.3); z-index: 0;
    }

    /* Hiệu ứng rơi */
    .petal, .lixi {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall linear infinite; font-size: 25px;
    }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }

    /* Nội dung chính */
    .main-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        z-index: 1; position: relative;
        max-width: 850px; /* Giới hạn độ rộng của khung bao ngoài */
        margin: auto;
    }

    .title-tet {
        color: #ffffff; text-align: center; font-size: 2.8rem; font-weight: bold;
        text-shadow: 3px 3px 10px #000; margin-bottom: 20px;
    }

    /* KHUNG KẾT QUẢ - ĐÂY MỚI LÀ CÁI CẦN TO */
    .result-card {
        display: flex; background: white; border: 8px solid #ffd700;
        border-radius: 20px; width: 100%; 
        min-height: 400px; /* To chà bá ở đây */
        margin: 20px auto; overflow: hidden;
        box-shadow: 0 20px 50px rgba(0,0,0,0.7);
    }
    .card-left {
        flex: 1.2; background: #d32f2f; color: #ffeb3b; 
        writing-mode: vertical-rl; text-orientation: upright;
        display: flex; align-items: center; justify-content: center;
        font-size: 3.5rem; font-weight: 900; padding: 20px; border-right: 6px solid #ffd700;
        text-shadow: 2px 2px 0px #000;
    }
    .card-right { flex: 3; display: flex; flex-direction: column; background-color: #fffaf0; }
    .wish-top {
        flex: 1; padding: 25px; font-size: 2.2rem; font-weight: 900; color: #b71c1c;
        border-bottom: 4px dashed #d32f2f; text-align: center;
        display: flex; align-items: center; justify-content: center;
    }
    .image-bottom { flex: 1.8; padding: 15px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 200px; }

    /* Mấy cái khác thu nhỏ lại cho cân đối */
    .stTextInput label { font-size: 1.2rem !important; color: gold !important; text-shadow: 1px 1px 2px black; }
    .shaker { font-size: 120px; text-align: center; margin: 10px auto; }
    .shake-anim { animation: shake 0.1s infinite; }
    @keyframes shake { 0% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } 100% { transform: rotate(-5deg); } }
    </style>

    <div class="petal" style="left:15%; animation-duration:8s;">🌸</div>
    <div class="lixi" style="left:45%; animation-duration:11s;">🧧</div>
    <div class="petal" style="left:75%; animation-duration:9s;">🌸</div>
""", unsafe_allow_html=True)

# --- LOGIC ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)

if st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ TẾT 🧧</div>', unsafe_allow_html=True)
    name = st.text_input("Nhập tên để nhận lộc:", placeholder="Tên bạn là gì...", key="name_input")
    
    if st.button("🏮 VÀO LẮC QUẺ", use_container_width=True):
        if name:
            st.session_state.current_user = name
            st.session_state.state = 'shaking'
            st.rerun()
        else:
            st.error("Chưa nhập tên kìa bạn ơi!")
    
    if st.button("📝 DANH SÁCH MAY MẮN", use_container_width=True):
        st.session_state.state = 'view_list'
        st.rerun()

elif st.session_state.state == 'shaking':
    st.markdown(f'<div class="title-tet">ĐANG LẮC CHO {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker shake-anim">🏺</div>', unsafe_allow_html=True)
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3" type="audio/mp3"></audio>', unsafe_allow_html=True)
    
    time.sleep(2.5)
    data = [
        {"money": "50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
        {"money": "100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"money": "200K", "wish": "SỨC KHỎE DỒI DÀO", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
        {"money": "500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
    ]
    result = random.choice(data)
    st.session_state.result = result
    st.session_state.lucky_list.append({"Tên": st.session_state.current_user, "Lì xì": result['money'], "Giờ": time.strftime("%H:%M")})
    st.session_state.state = 'result'
    st.rerun()

elif st.session_state.state == 'result':
    st.markdown(f'<div class="title-tet">KẾT QUẢ CỦA {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    res = st.session_state.result
    
    # CHỈ CÁI KHUNG NÀY TO CHÀ BÁ
    st.markdown(f"""
        <div class="result-card">
            <div class="card-left">LÌ XÌ {res['money']}</div>
            <div class="card-right">
                <div class="wish-top">{res['wish']}</div>
                <div class="image-bottom">
                    <img src="{res['img']}">
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧧 LẮC TIẾP TỤC", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

elif st.session_state.state == 'view_list':
    st.markdown('<div class="title-tet">DANH SÁCH MAY MẮN</div>', unsafe_allow_html=True)
    st.table(st.session_state.lucky_list)
    if st.button("⬅️ QUAY LẠI", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
