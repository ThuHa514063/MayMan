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
    /* Nền và Overlay */
    .stApp {
        background: url("https://image.dienthoaivui.com.vn/x,webp,q90/https://dashboard.dienthoaivui.com.vn/uploads/dashboard/editor_upload/background-tet-050.jpg");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.4); z-index: 0;
    }

    /* Hoa đào & Lì xì rơi */
    .petal, .lixi {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall linear infinite; font-size: 25px;
    }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }

    /* Box nội dung chính - Giữ kích thước vừa phải */
    .main-box {
        z-index: 1; position: relative; max-width: 600px; margin: auto; padding-top: 20px;
    }

    .title-tet {
        color: #ffeb3b; text-align: center; font-size: 2.5rem; font-weight: bold;
        text-shadow: 2px 2px 10px #000; margin-bottom: 20px;
    }

    /* SỬA MÀU THÔNG BÁO LỖI (st.error) CHO DỄ ĐỌC */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 2px solid #ff4b4b !important;
    }
    .stAlert div { color: #b71c1c !important; font-weight: bold !important; font-size: 1.1rem !important; }

    /* KHUNG KẾT QUẢ - HÌNH CHỮ NHẬT NGANG (TO) */
    .result-card {
        display: flex; background: white; border: 6px solid #ffd700;
        border-radius: 20px; width: 100%; height: 320px; /* Cố định chiều cao để ra hình chữ nhật */
        margin: 20px auto; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }
    
    /* Bên trái: Hiện quà tặng xoay dọc */
    .card-left {
        flex: 0.7; background: #d32f2f; color: #ffeb3b; 
        writing-mode: vertical-rl; text-orientation: upright;
        display: flex; align-items: center; justify-content: center;
        font-size: 3.5rem; font-weight: 900; padding: 10px; border-right: 5px solid #ffd700;
        text-shadow: 2px 2px 0px #000;
    }
    
    .card-right { flex: 3; display: flex; flex-direction: column; background-color: #fffaf0; }
    
    /* Lời chúc bên trên */
    .wish-top {
        flex: 1; padding: 15px; font-size: 2rem; font-weight: 800; color: #b71c1c;
        border-bottom: 3px dashed #d32f2f; text-align: center;
        display: flex; align-items: center; justify-content: center;
    }
    /* Hình ảnh bên dưới */
    .image-bottom { flex: 1.5; padding: 10px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 160px; width: auto; }

    /* Shaker ống quẻ */
    .shaker { font-size: 100px; text-align: center; margin: 10px auto; }
    .shake-anim { animation: shake 0.1s infinite; }
    @keyframes shake { 0% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } 100% { transform: rotate(-5deg); } }
    
    /* Label text màu trắng cho dễ nhìn */
    .stMarkdown p, label { color: white !important; font-size: 1.1rem !important; text-shadow: 1px 1px 3px black; }
    </style>

    <div class="petal" style="left:10%; animation-duration:8s;">🌸</div>
    <div class="lixi" style="left:35%; animation-duration:11s;">🧧</div>
    <div class="petal" style="left:65%; animation-duration:10s;">🌸</div>
    <div class="lixi" style="left:85%; animation-duration:9s;">🧧</div>
""", unsafe_allow_html=True)

# --- LOGIC ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)

if st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ KHAI XUÂN 🧧</div>', unsafe_allow_html=True)
    name = st.text_input("Nhập tên để nhận lộc:", placeholder="Tên của bạn...", key="name_input")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏮 VÀO LẮC QUẺ", use_container_width=True):
            if name:
                st.session_state.current_user = name
                st.session_state.state = 'shaking'
                st.rerun()
            else:
                st.error("Nhập tên đã bồ tèo ơi!") # Đã sửa màu dễ đọc
    with col2:
        if st.button("📝 DS MAY MẮN", use_container_width=True):
            st.session_state.state = 'view_list'
            st.rerun()

elif st.session_state.state == 'shaking':
    st.markdown(f'<div class="title-tet">ĐANG LẮC CHO {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker shake-anim">🏺</div>', unsafe_allow_html=True)
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3" type="audio/mp3"></audio>', unsafe_allow_html=True)
    
    time.sleep(2.5)
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
    
    # KHUNG KẾT QUẢ HÌNH CHỮ NHẬT NGANG
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
