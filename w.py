import streamlit as st
import random
import time
import pandas as pd

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

    /* Hiệu ứng rơi */
    .petal, .lixi {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall linear infinite; font-size: 25px;
    }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }

    /* Box nội dung chính */
    .main-box { z-index: 1; position: relative; max-width: 700px; margin: auto; padding: 10px; }

    .title-tet {
        color: #ffeb3b; text-align: center; font-size: 2.8rem; font-weight: bold;
        text-shadow: 3px 3px 12px #000; margin-bottom: 25px;
    }

    /* KHUNG KẾT QUẢ HÌNH CHỮ NHẬT NGANG */
    .result-card {
        display: flex; background: white; border: 6px solid #ffd700;
        border-radius: 20px; width: 100%; height: 320px;
        margin: 20px auto; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }
    .card-left {
        flex: 0.8; background: #d32f2f; color: #ffeb3b; 
        writing-mode: vertical-rl; text-orientation: upright;
        display: flex; align-items: center; justify-content: center;
        font-size: 3.5rem; font-weight: 900; padding: 10px; border-right: 5px solid #ffd700;
        text-shadow: 2px 2px 0px #000;
    }
    .card-right { flex: 3; display: flex; flex-direction: column; background-color: #fffaf0; }
    .wish-top {
        flex: 1; padding: 15px; font-size: 2rem; font-weight: 800; color: #b71c1c;
        border-bottom: 3px dashed #d32f2f; text-align: center;
        display: flex; align-items: center; justify-content: center;
    }
    .image-bottom { flex: 1.5; padding: 10px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 160px; }

    /* TRANG TRÍ BẢNG DANH SÁCH */
    .list-container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 15px;
        max-height: 400px;
        overflow-y: auto;
        border: 3px solid #ffd700;
    }
    .list-item {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px; border-bottom: 1px solid #ddd;
        color: #b71c1c; font-weight: bold; font-size: 1.1rem;
    }
    .list-item:last-child { border-bottom: none; }
    .gift-tag { background: #d32f2f; color: #ffeb3b; padding: 2px 10px; border-radius: 5px; }

    /* Nút Reset */
    .stButton>button[kind="secondary"] {
        background-color: #333 !important; color: white !important;
        border: 1px solid #555 !important;
    }

    /* Các văn bản khác */
    .stMarkdown p, label { color: white !important; font-size: 1.1rem !important; text-shadow: 1px 1px 3px black; }
    </style>

    <div class="petal" style="left:10%; animation-duration:8s;">🌸</div>
    <div class="lixi" style="left:40%; animation-duration:11s;">🧧</div>
    <div class="petal" style="left:70%; animation-duration:9s;">🌸</div>
""", unsafe_allow_html=True)

# --- LOGIC ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)

if st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">🧧 GIEO QUẺ KHAI XUÂN 🧧</div>', unsafe_allow_html=True)
    name = st.text_input("📝 NHẬP TÊN CỦA BẠN:", placeholder="Ví dụ: Anh Ba, Chị Bảy...", key="name_input")
    
    st.write("")
    if st.button("🏮 BẮT ĐẦU LẮC QUẺ", use_container_width=True):
        if name:
            st.session_state.current_user = name
            st.session_state.state = 'shaking'
            st.rerun()
        else:
            st.error("⚠️ Nhập tên đã bồ tèo ơi!")
    
    if st.button("📝 XEM DANH SÁCH MAY MẮN", use_container_width=True):
        st.session_state.state = 'view_list'
        st.rerun()

elif st.session_state.state == 'shaking':
    st.markdown(f'<div class="title-tet">ĐANG LẮC CHO {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:120px; text-align:center;">🏺</div>', unsafe_allow_html=True)
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/misc/sounds/shaking-dice-1.mp3" type="audio/mp3"></audio>', unsafe_allow_html=True)
    
    time.sleep(2)
    data = [
        {"gift": "50K", "wish": "VẠN SỰ NHƯ Ý", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614741.png"},
        {"gift": "100K", "wish": "TIỀN VÀO NHƯ NƯỚC", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "200K", "wish": "SỨC KHỎE DỒI DÀO", "img": "https://cdn-icons-png.flaticon.com/512/4359/4359942.png"},
        {"gift": "500K", "wish": "ĐẠI PHÚ ĐẠI QUÝ", "img": "https://cdn-icons-png.flaticon.com/512/2614/2614831.png"},
    ]
    result = random.choice(data)
    st.session_state.result = result
    st.session_state.lucky_list.insert(0, {"name": st.session_state.current_user, "gift": result['gift'], "time": time.strftime("%H:%M")})
    st.session_state.state = 'result'
    st.rerun()

elif st.session_state.state == 'result':
    st.markdown(f'<div class="title-tet">CHÚC MỪNG {st.session_state.current_user.upper()}</div>', unsafe_allow_html=True)
    res = st.session_state.result
    
    st.markdown(f"""
        <div class="result-card">
            <div class="card-left">{res['gift']}</div>
            <div class="card-right">
                <div class="wish-top">{res['wish']}</div>
                <div class="image-bottom"><img src="{res['img']}"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧧 QUAY LẠI LẮC TIẾP", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

elif st.session_state.state == 'view_list':
    st.markdown('<div class="title-tet">📝 BẢNG VÀNG MAY MẮN</div>', unsafe_allow_html=True)
    
    if st.session_state.lucky_list:
        # GIAO DIỆN BẢNG TỰ CHẾ
        list_html = '<div class="list-container">'
        for item in st.session_state.lucky_list:
            list_html += f"""
                <div class="list-item">
                    <span>👤 {item['name']}</span>
                    <span class="gift-tag">{item['gift']}</span>
                    <span style="font-size: 0.8rem; color: #666;">🕒 {item['time']}</span>
                </div>
            """
        list_html += '</div>'
        st.markdown(list_html, unsafe_allow_html=True)
        
        st.write("")
        # NÚT RESET DANH SÁCH
        if st.button("🗑️ XÓA TẤT CẢ DANH SÁCH", use_container_width=True, type="secondary"):
            st.session_state.lucky_list = []
            st.success("Đã dọn dẹp danh sách!")
            time.sleep(1)
            st.rerun()
    else:
        st.markdown('<p style="text-align:center;">Chưa có ai may mắn cả. Hãy gieo quẻ ngay!</p>', unsafe_allow_html=True)
    
    if st.button("⬅️ QUAY LẠI", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
