import streamlit as st
import random
import time

# Cấu hình trang
st.set_page_config(page_title="Lắc Quẻ Đầu Năm", page_icon="🧧")

# Hiệu ứng CSS để tùy chỉnh giao diện giống phác thảo của bạn
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; background-color: #d32f2f; color: white; border-radius: 10px; }
    .result-container { display: flex; border: 4px solid #d32f2f; border-radius: 15px; background: white; overflow: hidden; }
    .card-left { flex: 1; background: #d32f2f; color: white; display: flex; align-items: center; justify-content: center; font-size: 40px; font-weight: bold; padding: 20px; }
    .card-right { flex: 2; display: flex; flex-direction: column; }
    .wish-box { flex: 1; padding: 15px; border-bottom: 2px solid #eee; font-style: italic; font-size: 20px; text-align: center; color: #b71c1c; font-weight: bold; }
    .img-box { flex: 2; padding: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧧 Lắc Quẻ Lì Xì May Mắn")
st.write("Nhấn nút bên dưới để bắt đầu lắc quẻ khai xuân!")

# Danh sách dữ liệu
data = [
    {"money": "50k", "wish": "Vạn sự như ý, tỷ sự như mơ!", "img": "https://img.icons8.com/emoji/96/red-envelope-emoji.png"},
    {"money": "100k", "wish": "Tiền vào như nước, tiền ra nhỏ giọt!", "img": "https://img.icons8.com/emoji/96/money-bag-emoji.png"},
    {"money": "200k", "wish": "Công danh rạng rỡ, tình duyên phơi phới!", "img": "https://img.icons8.com/emoji/96/firecracker-emoji.png"},
    {"money": "500k", "wish": "Đại phú đại quý, phát lộc phát tài!", "img": "https://img.icons8.com/emoji/96/gem-stone-emoji.png"}
]

if st.button("🏮 BẮT ĐẦU LẮC QUẺ 🏮"):
    with st.spinner('Đang lắc quẻ...'):
        time.sleep(1.5) # Tạo hiệu ứng chờ đợi
        res = random.choice(data)
        st.balloons() # Hiệu ứng bóng bay/pháo giấy của Streamlit
        
        # Hiển thị kết quả theo đúng layout bạn vẽ
        st.markdown(f"""
            <div class="result-container">
                <div class="card-left">{res['money']}</div>
                <div class="card-right">
                    <div class="wish-box">{res['wish']}</div>
                    <div class="img-box"><img src="{res['img']}" width="100"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)