import streamlit as st
import qrcode
import io
import base64
from PIL import Image
import pyshorteners
import sqlite3
import datetime
import random
import string

# Database setup
def get_db_connection():
    """Establish connection to SQLite database."""
    conn = sqlite3.connect("qr_codes.db")
    conn.row_factory = sqlite3.Row  # Fetch columns by name
    return conn

def init_db():
    """Create the QR Codes table if it doesn't exist."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS qr_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT,
            short_url TEXT,
            qr_image BLOB,
            scans INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            password TEXT,
            expiration_date TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()  # Ensure DB is initialized

# Generate a random password
def generate_password(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Shorten URL
def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        return short_url
    except Exception as e:
        return url

# Generate QR Code
def generate_qr(url, color="black", bg_color="white", logo=None, box_size=5):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color=bg_color).convert("RGB")

    if logo:
        try:
            logo = Image.open(logo).convert("RGBA")
            img = img.convert("RGBA")
            logo.thumbnail((img.size[0] // 4, img.size[1] // 4))
            pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, pos, logo)
        except Exception as e:
            pass

    return img

# Convert image to bytes
def image_to_bytes(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return buffered.getvalue()

# Insert into Database
def insert_qr_code(original_url, short_url, img_bytes, password, expiration_date):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO qr_codes (original_url, short_url, qr_image, password, expiration_date) VALUES (?, ?, ?, ?, ?)",
              (original_url, short_url, sqlite3.Binary(img_bytes), password, expiration_date))
    conn.commit()
    conn.close()

# Retrieve all QR codes
def get_all_qr_codes():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, original_url, short_url, qr_image, created_at, password, expiration_date FROM qr_codes ORDER BY created_at DESC")
    data = c.fetchall()
    conn.close()
    return data

# Streamlit UI
st.set_page_config(page_title="Dynamic QR Code Generator", layout="wide")
st.title("🔗 Dynamic QR Code Generator")

url = st.text_input("Enter URL:")
color = st.color_picker("Pick QR Code Color:", "#000000")
bg_color = st.color_picker("Pick Background Color:", "#FFFFFF")
box_size = st.slider("Select QR Code Size:", 2, 10, 5)
expiration_days = st.slider("Set QR Code Expiry (Days):", 1, 365, 30)
password_protected = st.checkbox("Enable Password Protection")
password = generate_password() if password_protected else None
logo = st.file_uploader("Upload Logo (optional)", type=["png", "jpg", "jpeg"])

if logo is not None:
    try:
        img = Image.open(logo)
        st.image(img, caption="Uploaded Logo Preview", use_column_width=True)
    except Exception as e:
        st.error(f"Logo processing error: {e}")

if st.button("Generate QR Code"):
    if url:
        short_url = shorten_url(url)
        expiration_date = (datetime.datetime.now() + datetime.timedelta(days=expiration_days)).strftime('%Y-%m-%d')
        qr_img = generate_qr(short_url, color, bg_color, logo, box_size)
        
        if isinstance(qr_img, Image.Image):
            img_bytes = image_to_bytes(qr_img)
            insert_qr_code(url, short_url, img_bytes, password, expiration_date)
            
            # Display smaller QR code (Reduced size)
            st.image(img_bytes, caption="Your QR Code", width=300)  # Reduced width size (300 pixels)
            
            # Download QR Code
            b64 = base64.b64encode(img_bytes).decode()
            href = f'<a href="data:image/png;base64,{b64}" download="qr_code.png">Download QR Code</a>'
            st.markdown(href, unsafe_allow_html=True)

            if password_protected:
                st.success(f"🔒 Password: {password}")
        else:
            st.error("QR Code generation failed. Check console for errors.")
    else:
        st.error("Please enter a URL.")

# Display stored QR codes
st.subheader("📂 Stored QR Codes")
qr_data = get_all_qr_codes()
if qr_data:
    for qr in qr_data:
        st.write(f"🔗 Original URL: {qr['original_url']}")
        st.write(f"🔗 Short URL: {qr['short_url']}")
        st.write(f"📅 Created At: {qr['created_at']}")
        st.write(f"⏳ Expiration Date: {qr['expiration_date']}")
        if qr['password']:
            st.write(f"🔒 Password: {qr['password']}")
        st.image(qr['qr_image'], caption="Stored QR Code", width=300)  # Reduced width size (300 pixels)
        st.write("---")
else:
    st.info("No QR codes stored yet.")
