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

# --- TOÀN BỘ GIAO DIỆN CSS ---
st.markdown("""
    <style>
    /* Background ảnh của bạn */
    .stApp {
        background: url("https://image.dienthoaivui.com.vn/x,webp,q90/https://dashboard.dienthoaivui.com.vn/uploads/dashboard/editor_upload/background-tet-050.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Lớp phủ mờ giúp dễ đọc chữ */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.3); /* Làm tối nền 30% */
        z-index: 0;
    }

    /* Hiệu ứng mưa hoa đào & lì xì */
    .petal, .lixi {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall linear infinite; font-size: 25px;
    }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }

    /* Container bao quanh nội dung để tạo độ tương phản */
    .main-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(5px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        z-index: 1;
        position: relative;
    }

    /* Chữ tiêu đề: Màu trắng, viền đen cho cực kỳ dễ đọc */
    .title-tet {
        color: #ffffff;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        text-shadow: 3px 3px 10px #000000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
        margin-bottom: 20px;
    }

    /* Label text */
    label, .stMarkdown p {
        color: white !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 5px black;
    }

    /* Thẻ kết quả (Giữ nguyên phác thảo của bạn nma làm rõ hơn) */
    .result-card {
        display: flex; background: white; border: 5px solid #ffd700;
        border-radius: 15px; width: 100%; max-width: 450px; margin: auto; overflow: hidden;
        box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }
    .card-left {
        flex: 1; background: #d32f2f; color: #ffeb3b; writing-mode: vertical-rl; 
        text-orientation: upright; display: flex; align-items: center; justify-content: center;
        font-size: 2rem; font-weight: bold; padding: 15px; border-right: 4px solid #ffd700;
    }
    .card-right { flex: 2.5; display: flex; flex-direction: column; background-color: #fffaf0; }
    .wish-top {
        flex: 1; padding: 20px; font-size: 1.6rem; font-weight: 800; color: #b71c1c;
        border-bottom: 3px dashed #d32f2f; text-align: center; display: flex; align-items: center; justify-content: center;
    }
    .image-bottom { flex: 1.5; padding: 15px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 150px; }

    /* Shaker ống quẻ */
    .shaker { font-size: 100px; text-align: center; margin: 10px auto; display: block; filter: drop-shadow(0 0 10px gold); }
    .shake-anim { animation: shake-crazy 0.1s infinite; }
    @keyframes shake-crazy {
        0% { transform: rotate(0); } 50% { transform: rotate(-10deg) translate(-5px); } 100% { transform: rotate(10deg) translate(5px); }
    }
    </style>

    <div class="petal" style="left:10%; animation-duration:8s;">🌸</div>
    <div class="lixi" style="left:30%; animation-duration:12s;">🧧</div>
    <div class="petal" style="left:55%; animation-duration:10s;">🌸</div>
    <div class="lixi" style="left:75%; animation-duration:9s;">🧧</div>
    <div class="petal" style="left:90%; animation-duration:11s;">🌸</div>
""", unsafe_allow_html=True)

# --- DỮ LIỆU ---
data = [
    {"money": "50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
    {"money": "100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
    {"money": "200K", "wish": "SỨC KHỎE DỒI DÀO", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
    {"money": "500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
]

# --- LOGIC ĐIỀU HƯỚNG ---

st.markdown('<div class="main-box">', unsafe_allow_html=True)

if st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ KHAI XUÂN 🧧</div>', unsafe_allow_html=True)
    name = st.text_input("Nhập tên để nhận lộc:", placeholder="Tên bạn là gì...", key="name_input")
    
    if st.button("🏮 VÀO LẮC QUẺ", use_container_width=True):
        if name:
            st.session_state.current_user = name
            st.session_state.state = 'shaking'
            st.rerun()
        else:
            st.error("Ê, chưa nhập tên mà đòi lắc à?")
    
    if st.button("📝 DANH SÁCH MAY MẮN", use_container_width=True):
        st.session_state.state = 'view_list'
        st.rerun()

elif st.session_state.state == 'shaking':
    st.markdown(f'<div class="title-tet">ĐANG LẮC CHO {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker shake-anim">🏺</div>', unsafe_allow_html=True)
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3" type="audio/mp3"></audio>', unsafe_allow_html=True)
    
    time.sleep(2.5)
    result = random.choice(data)
    st.session_state.result = result
    
    # LƯU KẾT QUẢ
    st.session_state.lucky_list.append({
        "Tên": st.session_state.current_user,
        "Lì xì": result['money'],
        "Thời gian": time.strftime("%H:%M:%S")
    })
    st.session_state.state = 'result'
    st.rerun()

elif st.session_state.state == 'result':
    st.markdown(f'<div class="title-tet">CHÚC MỪNG {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    res = st.session_state.result
    st.markdown(f"""
        <div class="result-card">
            <div class="card-left">LÌ XÌ {res['money']}</div>
            <div class="card-right">
                <div class="wish-top">{res['wish']}</div>
                <div class="image-bottom"><img src="{res['img']}"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧧 LẮC TIẾP TỤC", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()
    if st.button("📝 XEM AI TRÚNG GÌ", use_container_width=True):
        st.session_state.state = 'view_list'
        st.rerun()

elif st.session_state.state == 'view_list':
    st.markdown('<div class="title-tet">📝 BẢNG VÀNG MAY MẮN</div>', unsafe_allow_html=True)
    if st.session_state.lucky_list:
        st.dataframe(st.session_state.lucky_list, use_container_width=True)
    else:
        st.write("Chưa có ai cả, mau lắc đi!")
    
    if st.button("⬅️ QUAY LẠI", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
