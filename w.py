import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Đầu Năm", page_icon="🧧", layout="centered")

# --- KHỞI TẠO DỮ LIỆU ---
if 'lucky_list' not in st.session_state:
    st.session_state.lucky_list = []
if 'state' not in st.session_state:
    st.session_state.state = 'home'  # Bắt đầu tại trang Home
if 'current_user' not in st.session_state:
    st.session_state.current_user = ""

# --- CSS TÙY CHỈNH (TRANG TRÍ LẠI TRANG CHỦ) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Lexend:wght@400;900&family=Sriracha&display=swap');

    .stApp {
        background: url("https://image.dienthoaivui.com.vn/x,webp,q90/https://dashboard.dienthoaivui.com.vn/uploads/dashboard/editor_upload/background-tet-050.jpg");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.4); z-index: 0;
    }

    .main-box { z-index: 1; position: relative; max-width: 600px; margin: auto; padding-top: 20px; font-family: 'Lexend', sans-serif; }

    /* Tiêu đề chính lấp lánh */
    .title-tet {
        font-family: 'Dancing Script', cursive;
        color: #ffeb3b; text-align: center; font-size: 3.8rem; font-weight: bold;
        text-shadow: 0 0 10px #ffeb3b, 3px 3px 15px #000; margin-bottom: 20px;
    }

    /* Thiết kế lại Box trang chủ */
    .home-container {
        border: 4px solid #ffd700;
        background: rgba(183, 28, 28, 0.9);
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
        position: relative;
        overflow: hidden;
    }
    .home-container::before {
        content: "🧧"; position: absolute; top: 10px; left: 10px; font-size: 30px; opacity: 0.5;
    }
    .home-container::after {
        content: "🧧"; position: absolute; bottom: 10px; right: 10px; font-size: 30px; opacity: 0.5;
    }

    .home-box h2 {
        font-family: 'Sriracha', cursive;
        color: #ffd700; font-size: 2rem; margin-bottom: 15px;
    }
    .home-box p {
        color: #fff !important; font-size: 1.2rem !important; line-height: 1.5;
        text-shadow: none !important; margin-bottom: 10px;
    }

    /* Giữ nguyên các thành phần result-card của bạn */
    .result-card {
        display: flex; background: white; border: 6px solid #ffd700;
        border-radius: 20px; width: 100%; height: 320px;
        margin: 20px auto; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }
    .card-left {
        flex: 1; background: #d32f2f; color: #ffeb3b; 
        display: flex; align-items: center; justify-content: center;
        text-align: center; font-family: 'Lexend', sans-serif;
        font-size: 2rem; font-weight: 900; padding: 15px; border-right: 5px solid #ffd700;
        text-shadow: 2px 2px 5px #000; word-wrap: break-word;
    }
    .card-right { flex: 2; display: flex; flex-direction: column; background-color: #fffaf0; }
    .wish-top {
        flex: 1; padding: 15px; font-size: 2rem; font-weight: 800; color: #b71c1c;
        font-family: 'Dancing Script', cursive; border-bottom: 3px dashed #d32f2f; 
        text-align: center; display: flex; align-items: center; justify-content: center;
    }
    .image-bottom { flex: 1.5; padding: 10px; display: flex; justify-content: center; align-items: center; }
    .image-bottom img { max-height: 150px; width: auto; }

    /* List scroll giữ nguyên */
    .list-scroll {
        background: rgba(255, 255, 255, 0.9); border-radius: 15px;
        padding: 10px; max-height: 300px; overflow-y: auto; border: 4px solid #ffd700;
    }
    .list-row {
        display: flex; justify-content: space-between; align-items: center;
        padding: 8px 15px; border-bottom: 1px solid #eee; color: #b71c1c; font-weight: bold;
    }
    .gift-label { background: #d32f2f; color: #ffeb3b; padding: 2px 10px; border-radius: 5px; font-size: 0.9rem; }

    .stMarkdown p, label { color: white !important; font-size: 1.1rem !important; text-shadow: 1px 1px 3px black; }
    
    /* Hiệu ứng rơi rơi */
    .petal, .lixi { position: fixed; top: -10%; z-index: 9999; animation: fall linear infinite; font-size: 25px; pointer-events: none; }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }
    
    .shaker { font-size: 100px; text-align: center; margin: 20px; animation: shake 0.2s infinite; }
    @keyframes shake { 0% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } 100% { transform: rotate(-5deg); } }
    </style>

    <div class="petal" style="left:5%; animation-duration:8s;">🌸</div>
    <div class="lixi" style="left:25%; animation-duration:11s;">🧧</div>
    <div class="petal" style="left:45%; animation-duration:10s;">🌸</div>
    <div class="lixi" style="left:65%; animation-duration:9s;">🧧</div>
    <div class="petal" style="left:85%; animation-duration:12s;">🌸</div>
    <div class="lixi" style="left:15%; animation-duration:10s;">🧧</div>
    <div class="petal" style="left:75%; animation-duration:7s;">🌸</div>
""", unsafe_allow_html=True)

# --- LOGIC ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# 1. TRANG CHỦ (HOME) - ĐÃ TRANG TRÍ LẠI
if st.session_state.state == 'home':
    st.markdown('<div class="title-tet">Mừng Xuân 2026</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="home-container">
            <div class="home-box">
                <h2>🧧 KHAI XUÂN NHƯ Ý 🧧</h2>
                <p>Năm mới Ất Tỵ sang, chúc bạn vạn sự hanh thông!</p>
                <p>Cùng gieo quẻ đầu năm để nhận lộc may mắn từ hội bạn nhé.</p>
                <br>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("🏮 BẮT ĐẦU GIEO QUẺ 🏮", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

# 2. TRANG NHẬP TÊN (Giữ nguyên link icon & thành phần)
elif st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">Gieo Quẻ Khai Xuân</div>', unsafe_allow_html=True)
    name = st.text_input("Nhập tên để nhận lộc:", placeholder="Tên của bạn...", key="name_input")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏮 VÀO LẮC QUẺ", use_container_width=True):
            if name:
                st.session_state.current_user = name
                st.session_state.state = 'shaking'
                st.rerun()
            else:
                st.error("Nhập tên đã bạn iu ơi!")
    with col2:
        if st.button("📝 BẢNG VÀNG MAY MẮN", use_container_width=True):
            st.session_state.state = 'view_list'
            st.rerun()
    
    if st.button("🏠 VỀ TRANG CHỦ", use_container_width=True):
        st.session_state.state = 'home'
        st.rerun()

# 3. TRANG ĐANG LẮC (Giữ nguyên)
elif st.session_state.state == 'shaking':
    st.markdown(f'<div class="title-tet">Đang lắc cho {st.session_state.current_user}</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker">🏺</div>', unsafe_allow_html=True)
    time.sleep(2)
    
    data = [
        {"gift": "1K", "wish": "Vạn Sự Như Ý", "img": "https://banner2.cleanpng.com/lnd/20250121/re/644d576f49df54bc2e004232f05991.webp"},
        {"gift": "Bánh kẹp", "wish": "Gắn Kết Yêu Thương", "img": "https://cdn-icons-png.flaticon.com/512/3225/3225096.png"},
        {"gift": "2K", "wish": "Cát Tường Như Ý", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "10K", "wish": "Tiền Vào Như Nước", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "20K", "wish": "Làm Ăn Phát Đạt", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Numismatics_and_Notaphily_icon.png"},
        {"gift": "Bánh quy", "wish": "Ngọt Ngào Cả Năm", "img": "https://cdn-icons-png.flaticon.com/512/541/541732.png"},
        {"gift": "Bánh bông lan", "wish": "Mềm Mại Hạnh Phúc", "img": "https://media.istockphoto.com/id/1352416535/vi/vec-to/b%C3%A1nh-sandwich-ng%E1%BB%8Dt-v%E1%BB%9Bi-c%C3%A1c-l%E1%BB%9Bp-b%E1%BB%8Dt-bi%E1%BB%83n-nh%C3%A2n-kem-%C4%91%C3%A1nh-vani-v%C3%A0-d%C3%A2u-t%C3%A2y-victoria-tr%C3%A1ng-mi%E1%BB%87ng.jpg?s=612x612&w=0&k=20&c=wcpZGWNUGl20QJrXQ6o1l2DD6vmClwLPsTlFwblgx6w="},
        {"gift": "5K", "wish": "Tấn Tài Tấn Lộc", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "Kẹo Socola", "wish": "Tình Duyên Viên Mãn", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMbL1kxhbd_HfaoN80mpXE416tFjo_NfqRFomsu6J37Q&s"},
        {"gift": "1K", "wish": "Hạnh Phúc An Khang", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Numismatics_and_Notaphily_icon.png"},
        {"gift": "Bánh kẹp", "wish": "Gắn Kết Yêu Thương", "img": "https://cdn-icons-png.flaticon.com/512/3225/3225096.png"},
        {"gift": "2K", "wish": "Mã Đáo Thành Công", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "10K", "wish": "Phát tài phát lộc", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "20K", "wish": "Phú Quý Cát Tường", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "Bánh quy", "wish": "Niềm vui phơi phới", "img": "https://cdn-icons-png.flaticon.com/512/541/541732.png"},
        {"gift": "Bánh bông lan", "wish": "Mềm Mại Hạnh Phúc", "img": "https://cdn-icons-png.flaticon.com/512/2682/2682430.png"},
        {"gift": "5K", "wish": "Tấn Tài Tấn Lộc", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "Kẹo Socola", "wish": "Vạn sự như mơ", "img": "https://img.pikbest.com/png-images/20241207/an-assortment-of-chocolate-truffles-garnished-with-glossy-coating_11224924.png!w700wp"},
    ]
    result = random.choice(data)
    st.session_state.result = result
    st.session_state.lucky_list.insert(0, {"Tên": st.session_state.current_user, "Quà": result['gift'], "Giờ": time.strftime("%H:%M")})
    st.session_state.state = 'result'
    st.rerun()

# 4. TRANG KẾT QUẢ (Giữ nguyên)
elif st.session_state.state == 'result':
    st.markdown(f'<div class="title-tet">Chúc mừng {st.session_state.current_user}</div>', unsafe_allow_html=True)
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

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🧧 LẮC TIẾP", use_container_width=True):
            st.session_state.state = 'input_name'
            st.rerun()
    with c2:
        if st.button("📝 BẢNG VÀNG MAY MẮN", use_container_width=True):
            st.session_state.state = 'view_list'
            st.rerun()

# 5. TRANG BẢNG VÀNG (Giữ nguyên)
elif st.session_state.state == 'view_list':
    st.markdown('<div class="title-tet">Bảng Vàng May Mắn</div>', unsafe_allow_html=True)
    if st.session_state.lucky_list:
        list_html = '<div class="list-scroll">'
        for item in st.session_state.lucky_list:
            list_html += f'<div class="list-row"><span>👤 {item["Tên"]}</span><span class="gift-label">{item["Quà"]}</span><span>🕒 {item["Giờ"]}</span></div>'
        list_html += '</div>'
        st.markdown(list_html, unsafe_allow_html=True)
        st.write("")
        if st.button("🗑️ RESET BẢNG VÀNG MAY MẮN", use_container_width=True):
            st.session_state.lucky_list = []
            st.rerun()
    else:
        st.markdown('<p style="text-align:center; color:white;">Chưa có ai may mắn cả!</p>', unsafe_allow_html=True)

    col_back1, col_back2 = st.columns(2)
    with col_back1:
        if st.button("⬅️ QUAY LẠI", use_container_width=True):
            st.session_state.state = 'input_name'
            st.rerun()
    with col_back2:
        if st.button("🏠 VỀ TRANG CHỦ", use_container_width=True):
            st.session_state.state = 'home'
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
