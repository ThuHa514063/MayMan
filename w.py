import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="wide") # Chuyển sang wide để có không gian to hơn

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
    /* Background & Overlay */
    .stApp {
        background: url("https://image.dienthoaivui.com.vn/x,webp,q90/https://dashboard.dienthoaivui.com.vn/uploads/dashboard/editor_upload/background-tet-050.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.4); z-index: 0;
    }

    /* Hiệu ứng mưa hoa & lì xì */
    .petal, .lixi {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall linear infinite; font-size: 30px;
    }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }

    /* Nội dung chính */
    .main-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        padding: 40px;
        border-radius: 30px;
        border: 2px solid rgba(255, 255, 255, 0.2);
        z-index: 1; position: relative;
        max-width: 900px; margin: auto;
    }

    .title-tet {
        color: #ffffff; text-align: center; font-size: 4rem; font-weight: bold;
        text-shadow: 4px 4px 15px #000; margin-bottom: 30px;
    }

    /* KHUNG KẾT QUẢ SIZE LỚN */
    .result-card {
        display: flex; background: white; border: 10px solid #ffd700;
        border-radius: 25px; width: 100%; max-width: 800px; /* Tăng chiều rộng tối đa */
        min-height: 450px; /* Tăng chiều cao tối thiểu */
        margin: 30px auto; overflow: hidden;
        box-shadow: 0 30px 60px rgba(0,0,0,1);
    }
    .card-left {
        flex: 1.2; background: #d32f2f; color: #ffeb3b; 
        writing-mode: vertical-rl; text-orientation: upright;
        display: flex; align-items: center; justify-content: center;
        font-size: 4rem; font-weight: 900; padding: 20px; border-right: 8px solid #ffd700;
        text-shadow: 2px 2px 0px #000;
    }
    .card-right { flex: 3; display: flex; flex-direction: column; background-color: #fff9e6; }
    .wish-top {
        flex: 1.2; padding: 30px; font-size: 2.5rem; font-weight: 900; color: #b71c1c;
        border-bottom: 5px dashed #d32f2f; text-align: center;
        display: flex; align-items: center; justify-content: center;
        line-height: 1.2;
    }
    .image-bottom { flex: 2; padding: 20px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 250px; width: auto; object-fit: contain; }

    /* Shaker ống quẻ */
    .shaker { font-size: 150px; text-align: center; margin: 20px auto; filter: drop-shadow(0 0 20px gold); }
    .shake-anim { animation: shake-crazy 0.1s infinite; }
    @keyframes shake-crazy {
        0% { transform: rotate(-5deg); } 50% { transform: rotate(5deg) scale(1.1); } 100% { transform: rotate(-5deg); }
    }

    /* Button to hơn */
    div.stButton > button {
        font-size: 1.5rem !important; height: 60px !important;
        background-color: #ffeb3b !important; color: #b71c1c !important;
    }
    </style>

    <div class="petal" style="left:5%; animation-duration:7s;">🌸</div>
    <div class="lixi" style="left:20%; animation-duration:10s;">🧧</div>
    <div class="petal" style="left:40%; animation-duration:12s;">🌸</div>
    <div class="lixi" style="left:65%; animation-duration:9s;">🧧</div>
    <div class="petal" style="left:85%; animation-duration:11s;">🌸</div>
""", unsafe_allow_html=True)

# --- LOGIC ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)

if st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ TẾT 🧧</div>', unsafe_allow_html=True)
    name = st.text_input("📝 NHẬP TÊN CỦA BẠN:", placeholder="Ví dụ: Anh Ba, Chị Bảy...", key="name_input")
    
    st.write("")
    if st.button("🏮 BẮT ĐẦU LẮC QUẺ 🏮", use_container_width=True):
        if name:
            st.session_state.current_user = name
            st.session_state.state = 'shaking'
            st.rerun()
        else:
            st.error("⚠️ Bạn ơi, nhập cái tên vào đã!")
    
    if st.button("📝 XEM DANH SÁCH MAY MẮN", use_container_width=True):
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
    
    # KHUNG KẾT QUẢ KHỔ LỚN
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
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧧 LẮC TIẾP", use_container_width=True):
            st.session_state.state = 'input_name'
            st.rerun()
    with col2:
        if st.button("📝 BẢNG VÀNG", use_container_width=True):
            st.session_state.state = 'view_list'
            st.rerun()

elif st.session_state.state == 'view_list':
    st.markdown('<div class="title-tet">BẢNG VÀNG MAY MẮN</div>', unsafe_allow_html=True)
    st.dataframe(st.session_state.lucky_list, use_container_width=True)
    if st.button("⬅️ QUAY LẠI", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
