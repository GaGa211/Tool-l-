import requests
import cloudscraper

# Đọc Authorization từ file
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"[ERROR] Không tìm thấy file {filename}")
        return None

auth_token = read_file("Authorization.txt")
token = read_file("token.txt")

if not auth_token or not token:
    print("[ERROR] Thiếu Authorization hoặc Token. Hãy kiểm tra lại!")
    exit()

# Dùng CloudScraper để bypass Cloudflare
scraper = cloudscraper.create_scraper()

# Headers
headers = {
    "Authorization": auth_token,
    "x-token": token,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive"
}

url = "https://gateway.golike.net/api/tiktok-account"

try:
    response = scraper.get(url, headers=headers)
    
    if response.status_code == 200:
        print("[SUCCESS] Dữ liệu nhận được:")
        print(response.json())
    elif response.status_code == 403:
        print("[ERROR] API bị chặn (403 Forbidden). Thử các cách sau:")
        print("  - Kiểm tra lại token có hợp lệ không")
        print("  - Dùng VPN hoặc đổi IP (có thể bị block IP)")
        print("  - Nếu API yêu cầu CAPTCHA, có thể cần xử lý thủ công")
    else:
        print(f"[ERROR] Lỗi {response.status_code}: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Lỗi khi gửi request: {e}")
print("B\u1ea1n \u0111ang s\u1eed d\u1ee5ng phi\u00ean b\u1ea3n qu\u00e1 th\u1ea5p vui l\u00f2ng n\u00e2ng c\u1ea5p \u1ee9ng d\u1ee5ng m\u1edbi nh\u1ea5t !")
print("B\u1ea1n \u0111ang s\u1eed d\u1ee5ng phi\u00ean b\u1ea3n qu\u00e1 th\u1ea5p vui l\u00f2ng n\u00e2ng c\u1ea5p \u1ee9ng d\u1ee5ng m\u1edbi nh\u1ea5t !")