import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Gieo Quẻ Bính Ngọ 2026", page_icon="🧧", layout="centered")

# --- KHỞI TẠO DỮ LIỆU ---
if 'lucky_list' not in st.session_state:
    st.session_state.lucky_list = []
if 'wishes_list' not in st.session_state:
    # Dữ liệu mẫu ban đầu cho sinh động
    st.session_state.wishes_list = [
        {"name": "Admin", "wish": "Chúc mọi người năm mới Bính Ngọ vạn sự hanh thông, mã đáo thành công!"}
    ]
if 'state' not in st.session_state:
    st.session_state.state = 'home'
if 'current_user' not in st.session_state:
    st.session_state.current_user = ""

# --- CSS TÙY CHỈNH ---
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

    .title-tet {
        font-family: 'Dancing Script', cursive;
        color: #ffeb3b; text-align: center; font-size: 3.8rem; font-weight: bold;
        text-shadow: 0 0 10px #ffeb3b, 3px 3px 15px #000; margin-bottom: 20px;
    }

    .home-container {
        border: 4px solid #ffd700; background: rgba(183, 28, 28, 0.9);
        padding: 30px; border-radius: 25px; text-align: center;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.5); position: relative; overflow: hidden;
    }

    /* Result Card giữ nguyên link ảnh và cấu trúc */
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

    /* Sticky note rực rỡ cho lời chúc */
    .wish-wall-item {
        background: linear-gradient(135deg, #fff9c4 0%, #fff176 100%);
        color: #b71c1c; padding: 20px; border-radius: 15px;
        border-left: 8px solid #d32f2f; margin-bottom: 15px; 
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
        position: relative;
    }
    .wish-wall-item b { color: #d32f2f; font-size: 1.2rem; display: block; margin-bottom: 5px; border-bottom: 1px solid rgba(211, 47, 47, 0.2); }

    .stMarkdown p, label { color: white !important; font-size: 1.1rem !important; text-shadow: 1px 1px 3px black; }
    
    /* Hiệu ứng rơi */
    .petal, .lixi { position: fixed; top: -10%; z-index: 9999; animation: fall linear infinite; font-size: 25px; pointer-events: none; }
    @keyframes fall { 0% { transform: translateY(0) rotate(0deg); } 100% { transform: translateY(110vh) rotate(360deg); } }
    
    .shaker { font-size: 100px; text-align: center; margin: 20px; animation: shake 0.2s infinite; }
    @keyframes shake { 0% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } 100% { transform: rotate(-5deg); } }

    /* Sidebar Tết */
    [data-testid="stSidebar"] { background-color: #b71c1c; border-right: 3px solid #ffd700; }
    [data-testid="stSidebar"] .stMarkdown h3 { color: #ffd700 !important; font-family: 'Sriracha', cursive; text-align: center; border-bottom: 2px solid #ffd700; padding-bottom: 10px; }
    </style>

    <div class="petal" style="left:5%; animation-duration:8s;">🌸</div>
    <div class="lixi" style="left:25%; animation-duration:11s;">🧧</div>
    <div class="petal" style="left:45%; animation-duration:10s;">🌸</div>
    <div class="lixi" style="left:65%; animation-duration:9s;">🧧</div>
    <div class="petal" style="left:85%; animation-duration:12s;">🌸</div>
""", unsafe_allow_html=True)

# --- MENU NỔI (SIDEBAR) ---
with st.sidebar:
    st.markdown("### 🏮 MENU TẾT 2026")
    st.write("")
    if st.button("🏠 Trang Chủ", use_container_width=True):
        st.session_state.state = 'home'
        st.rerun()
    if st.button("🧧 Gieo Quẻ Nhận Lộc", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()
    if st.button("📝 Bảng Vàng May Mắn", use_container_width=True):
        st.session_state.state = 'view_list'
        st.rerun()
    st.markdown("---")
    if st.button("✍️ Viết Lời Chúc Mới", use_container_width=True):
        st.session_state.state = 'write_wish'
        st.rerun()
    if st.button("📜 Bức Tường Lời Chúc", use_container_width=True):
        st.session_state.state = 'view_wishes'
        st.rerun()
    st.write("---")
    st.caption("Năm Bính Ngọ cát tường! 🐎")

# --- LOGIC CHÍNH ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# 1. TRANG CHỦ
if st.session_state.state == 'home':
    st.markdown('<div class="title-tet">Mừng Xuân Bính Ngọ 2026</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="home-container">
            <h2 style="color:#ffd700; font-family:'Sriracha';">🧧 KHAI XUÂN NHƯ Ý 🧧</h2>
            <p style="color:white;">Chào mừng bạn đến với hội xuân Bính Ngọ.</p>
            <p style="color:white;">Hãy chọn chức năng ở Menu bên trái để bắt đầu!</p>
        </div>
    """, unsafe_allow_html=True)

# 2. TRANG NHẬP TÊN
elif st.session_state.state == 'input_name':
    st.markdown('<div class="title-tet">Gieo Quẻ Khai Xuân</div>', unsafe_allow_html=True)
    name = st.text_input("Nhập tên để nhận lộc:", placeholder="Tên của bạn...", key="name_input")
    if st.button("🏺 VÀO LẮC QUẺ", use_container_width=True):
        if name:
            st.session_state.current_user = name
            st.session_state.state = 'shaking'
            st.rerun()
        else:
            st.error("Nhập tên đã bồ ơi!")

# 3. TRANG ĐANG LẮC (GIỮ NGUYÊN DANH SÁCH QUÀ & LINK)
elif st.session_state.state == 'shaking':
    st.markdown(f'<div class="title-tet">Đang lắc cho {st.session_state.current_user}</div>', unsafe_allow_html=True)
    st.markdown('<div class="shaker">🏺</div>', unsafe_allow_html=True)
    time.sleep(2)
    
    data = [
        {"gift": "1K", "wish": "Vạn Sự Như Ý", "img": "https://banner2.cleanpng.com/lnd/20250121/re/644d576f49df54bc2e004232f05991.webp"},
        {"gift": "Bim bim", "wish": "Gắn Kết Yêu Thương", "img": "https://as1.ftcdn.net/jpg/01/14/11/96/1000_F_114119627_5o7TexwSbzds5UgqS9VqZiJmNx0KWgVR.webp"},
        {"gift": "2K", "wish": "Cát Tường Như Ý", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "10K", "wish": "Tiền Vào Như Nước", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "20K", "wish": "Làm Ăn Phát Đạt", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Numismatics_and_Notaphily_icon.png"},
        {"gift": "Bánh quy", "wish": "Ngọt Ngào Cả Năm", "img": "https://cdn-icons-png.flaticon.com/512/541/541732.png"},
        {"gift": "Bánh bông lan", "wish": "Mềm Mại Hạnh Phúc", "img": "https://media.istockphoto.com/id/1352416535/vi/vec-to/b%C3%A1nh-sandwich-ng%E1%BB%8Dt-v%E1%BB%9Bi-c%C3%A1c-l%E1%BB%9Bp-b%E1%BB%8Dt-bi%E1%BB%83n-nh%C3%A2n-kem-%C4%91%C3%A1nh-vani-v%C3%A0-d%C3%A2u-t%C3%A2y-victoria-tr%C3%A1ng-mi%E1%BB%87ng.jpg?s=612x612&w=0&k=20&c=wcpZGWNUGl20QJrXQ6o1l2DD6vmClwLPsTlFwblgx6w="},
        {"gift": "5K", "wish": "Tấn Tài Tấn Lộc", "img": "https://cdn-icons-png.flaticon.com/512/2489/2489756.png"},
        {"gift": "Kẹo Socola", "wish": "Tình Duyên Viên Mãn", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMbL1kxhbd_HfaoN80mpXE416tFjo_NfqRFomsu6J37Q&s"},
    ]
    result = random.choice(data)
    st.session_state.result = result
    st.session_state.lucky_list.insert(0, {"Tên": st.session_state.current_user, "Quà": result['gift'], "Giờ": time.strftime("%H:%M")})
    st.session_state.state = 'result'
    st.rerun()

# 4. TRANG KẾT QUẢ
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
    if st.button("🧧 LẮC TIẾP", use_container_width=True):
        st.session_state.state = 'input_name'
        st.rerun()

# 5. TRANG BẢNG VÀNG
elif st.session_state.state == 'view_list':
    st.markdown('<div class="title-tet">Bảng Vàng May Mắn</div>', unsafe_allow_html=True)
    if st.session_state.lucky_list:
        list_html = '<div class="list-scroll">'
        for item in st.session_state.lucky_list:
            list_html += f'<div class="list-row"><span>👤 {item["Tên"]}</span><span class="gift-label">{item["Quà"]}</span><span>🕒 {item["Giờ"]}</span></div>'
        list_html += '</div>'
        st.markdown(list_html, unsafe_allow_html=True)
    else:
        st.markdown('<p style="text-align:center;">Chưa ai nhận lộc!</p>', unsafe_allow_html=True)

# 6. TRANG VIẾT LỜI CHÚC (TRANG RIÊNG)
elif st.session_state.state == 'write_wish':
    st.markdown('<div class="title-tet">Gửi Lời Chúc Xuân</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="home-container">', unsafe_allow_html=True)
        w_name = st.text_input("Tên người gửi:", value=st.session_state.current_user)
        w_content = st.text_area("Lời chúc của bạn:", placeholder="Chúc mọi người năm mới hạnh phúc...")
        if st.button("🧧 GỬI LỜI CHÚC NÀY", use_container_width=True):
            if w_name and w_content:
                st.session_state.wishes_list.insert(0, {"name": w_name, "wish": w_content})
                st.balloons()
                st.success("Lời chúc của bạn đã được dán lên tường!")
                time.sleep(1)
                st.session_state.state = 'view_wishes'
                st.rerun()
            else:
                st.warning("Bạn quên nhập tên hoặc lời chúc rồi!")
        st.markdown('</div>', unsafe_allow_html=True)

# 7. TRANG TRÌNH BÀY TẤT CẢ LỜI CHÚC (TRANG RIÊNG)
elif st.session_state.state == 'view_wishes':
    st.markdown('<div class="title-tet">Bức Tường Lời Chúc</div>', unsafe_allow_html=True)
    if st.session_state.wishes_list:
        for w in st.session_state.wishes_list:
            st.markdown(f"""
                <div class="wish-wall-item">
                    <b>👤 {w['name']}</b>
                    <span>{w['wish']}</span>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<p style="text-align:center;">Bức tường đang trống, hãy viết lời chúc đầu tiên!</p>', unsafe_allow_html=True)
    
    if st.button("✍️ VIẾT LỜI CHÚC CỦA BẠN", use_container_width=True):
        st.session_state.state = 'write_wish'
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
