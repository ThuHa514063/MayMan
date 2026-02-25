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
    .stApp {
        background: url("https://image.dienthoaivui.com.vn/x,webp,q90/https://dashboard.dienthoaivui.com.vn/uploads/dashboard/editor_upload/background-tet-050.jpg");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.4); z-index: 0;
    }

    /* Hiệu ứng rơi */
    .petal, .lixi {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall linear infinite; font-size: 25px;
    }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }

    .main-box {
        background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px);
        padding: 30px; border-radius: 25px; border: 1px solid rgba(255, 255, 255, 0.3);
        z-index: 1; position: relative; max-width: 850px; margin: auto;
    }

    .title-tet {
        color: #ffffff; text-align: center; font-size: 2.8rem; font-weight: bold;
        text-shadow: 3px 3px 10px #000; margin-bottom: 20px;
    }

    /* KHUNG KẾT QUẢ - HIỂN THỊ MÓN QUÀ */
    .result-card {
        display: flex; background: white; border: 8px solid #ffd700;
        border-radius: 20px; width: 100%; min-height: 450px;
        margin: 20px auto; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.8);
    }
    
    /* PHẦN ĐỎ: CHỈ HIỂN THỊ MÓN QUÀ QUAY ĐƯỢC */
    .card-left {
        flex: 1.2; background: #d32f2f; color: #ffeb3b; 
        writing-mode: vertical-rl; text-orientation: upright;
        display: flex; align-items: center; justify-content: center;
        font-size: 4.5rem; /* Cực to */
        font-weight: 900; padding: 20px; border-right: 6px solid #ffd700;
        text-shadow: 3px 3px 0px #000;
    }
    
    .card-right { flex: 3; display: flex; flex-direction: column; background-color: #fffaf0; }
    
    .wish-top {
        flex: 1; padding: 25px; font-size: 2.2rem; font-weight: 900; color: #b71c1c;
        border-bottom: 4px dashed #d32f2f; text-align: center;
        display: flex; align-items: center; justify-content: center;
    }
    .image-bottom { flex: 2; padding: 15px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 220px; width: auto; }

    .shaker { font-size: 130px; text-align: center; margin: 10px auto; filter: drop-shadow(0 0 15px gold); }
    .shake-anim { animation: shake 0.1s infinite; }
    @keyframes shake { 0% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } 100% { transform: rotate(-5deg); } }
    
    /* Chỉnh style input và button */
    .stTextInput>div>div>input { font-size: 1.2rem; padding: 10px; }
    div.stButton>button { font-size: 1.3rem !important; font-weight: bold !important; height: 55px !important; }
    </style>

    <div class="petal" style="left:10%; animation-duration:8s;">🌸</div>
    <div class="lixi" style="left:40%; animation-duration:11s;">🧧</div>
    <div class="petal" style="left:70%; animation-duration:9s;">🌸</div>
""", unsafe_allow_html=True)

# --- LOGIC ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)

if st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ KHAI XUÂN 🧧</div>', unsafe_allow_html=True)
    name = st.text_input("Nhập tên để nhận lộc:", placeholder="Tên của bạn...", key="name_input")
    
    if st.button("🏮 BẮT ĐẦU LẮC QUẺ", use_container_width=True):
        if name:
            st.session_state.current_user = name
            st.session_state.state = 'shaking'
            st.rerun()
        else:
            st.error("⚠️ Phải có cái tên mới gieo quẻ được chứ!")
    
    if st.button("📝 XEM DANH SÁCH MAY MẮN", use_container_width=True):
        st.session_state.state = 'view_list'
        st.rerun()

elif st.session_state.state == 'shaking':
    st.markdown(f'<div class="title-tet">ĐANG LẮC CHO {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker shake-anim">🏺</div>', unsafe_allow_html=True)
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3" type="audio/mp3"></audio>', unsafe_allow_html=True)
    
    time.sleep(2.5)
    # Danh sách quà tặng
    data = [
        {"gift": "50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
        {"gift": "100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "200K", "wish": "SỨC KHỎE DỒI DÀO", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
        {"gift": "500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
    ]
    result = random.choice(data)
    st.session_state.result = result
    st.session_state.lucky_list.append({"Tên": st.session_state.current_user, "Quà": result['gift'], "Giờ": time.strftime("%H:%M")})
    st.session_state.state = 'result'
    st.rerun()

elif st.session_state.state == 'result':
    st.markdown(f'<div class="title-tet">CHÚC MỪNG {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    res = st.session_state.result
    
    # KHUNG KẾT QUẢ HIỂN THỊ MÓN QUÀ TIÊU ĐIỂM
    st.markdown(f"""
        <div class="result-card">
            <div class="card-left">{res['gift']}</div>
            <div class="card-right">
                <div class="wish-top">{res['wish']}</div>
                <div class="image-bottom">
                    <img src="{res['img']}">
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧧 QUAY LẠI LẮC TIẾP", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

elif st.session_state.state == 'view_list':
    st.markdown('<div class="title-tet">BẢNG VÀNG MAY MẮN</div>', unsafe_allow_html=True)
    st.dataframe(st.session_state.lucky_list, use_container_width=True)
    if st.button("⬅️ QUAY LẠI", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
