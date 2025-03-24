import os
import time
import cloudscraper
from pystyle import Colors, Colorate

while True:
    device = input(Colorate.Horizontal(Colors.blue_to_cyan, "Bạn đang dùng (1) Điện thoại (Termux) hay (2) Máy tính (Windows)? [1/2]: ")).strip()
    if device in ["1", "2"]:
        break
    print(Colorate.Horizontal(Colors.red_to_yellow, "⚠️ Vui lòng nhập 1 hoặc 2!"))

is_android = device == "1"

def open_url(link):
    os.system(f"termux-open-url {link}" if is_android else f"start {link}")

def clear_screen():
    os.system("clear" if is_android else "cls")

banner = r'''
─────────────────────────────────────────────────────────────────────────────
                『 🌟 』 ❯❯ TOOL : GOLIKE TIKTOK AUTO
                『 🚀 』 ❯❯ Version : 1.0
                『 🔥 』 ❯❯ Author : NHATTAN
─────────────────────────────────────────────────────────────────────────────
'''
clear_screen()
for line in banner.split("\n"):
    print(Colorate.Diagonal(Colors.blue_to_cyan, line))
    time.sleep(0.05)

if not os.path.exists('Authorization.txt'):
    with open('Authorization.txt', 'w') as f:
        f.write("")
if not os.path.exists('token.txt'):
    with open('token.txt', 'w') as f:
        f.write("")

with open('Authorization.txt', 'r', encoding="utf-8") as f:
    author = f.read().strip()
with open('token.txt', 'r', encoding="utf-8") as f:
    token = f.read().strip()

if not author or not token:
    author = input(Colorate.Horizontal(Colors.green_to_red, '💎 NHẬP AUTHORIZATION: ')).strip()
    token = input(Colorate.Horizontal(Colors.green_to_red, '🔑 NHẬP TOKEN: ')).strip()
    with open('Authorization.txt', 'w', encoding="utf-8") as f:
        f.write(author)
    with open('token.txt', 'w', encoding="utf-8") as f:
        f.write(token)

scraper = cloudscraper.create_scraper()

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
    'X-Requested-With': 'XMLHttpRequest'
}

def chonacc():
    try:
        response = scraper.get('https://gateway.golike.net/api/tiktok-account', headers=headers)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"⚠️ Lỗi khi gửi request: {e}"))
        return None

chontktiktok = chonacc()
if not chontktiktok or 'status' not in chontktiktok or chontktiktok['status'] != 200:
    print(Colorate.Horizontal(Colors.red_to_yellow, '⚠️ Authorization hoặc Token sai, hãy nhập lại!'))
    quit()

print(Colorate.Horizontal(Colors.blue_to_cyan, "\n🌟 DANH SÁCH TÀI KHOẢN TIKTOK 🌟"))
for i, acc in enumerate(chontktiktok['data'], start=1):
    print(Colorate.Horizontal(Colors.green_to_blue, f'[{i}] ➜ 🏆 {acc["nickname"]} '))

while True:
    try:
        luachon = int(input(Colorate.Horizontal(Colors.blue_to_cyan, '\n🎯 Chọn tài khoản để chạy: ')))
        if 1 <= luachon <= len(chontktiktok['data']):
            account_id = chontktiktok['data'][luachon - 1]['id']
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "⚠️ Số không hợp lệ, hãy nhập lại!"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_yellow, "⚠️ Vui lòng nhập số!"))

while True:
    try:
        delay = int(input(Colorate.Horizontal(Colors.green_to_blue, '\n⏳ Nhập thời gian delay (giây): ')))
        break
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_yellow, "⚠️ Vui lòng nhập số!"))

clear_screen()
print(Colorate.Horizontal(Colors.blue_to_cyan, '🚀 BẮT ĐẦU TOOL AUTO TIKTOK 🚀\n'))

while True:
    print(Colorate.Horizontal(Colors.green_to_blue, '🔄 Đang lấy nhiệm vụ...'), end='\r')

    response = scraper.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={account_id}', headers=headers)
    nhanjob = response.json() if response.status_code == 200 else None

    if nhanjob and 'status' in nhanjob and nhanjob['status'] == 200:
        ads_id = nhanjob['data']['id']
        link = nhanjob['data']['link']

        print(Colorate.Horizontal(Colors.green_to_blue, f"🔗 Mở link: {link}"))
        open_url(link)

        time.sleep(delay)

        response = scraper.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, json={'ads_id': ads_id, 'account_id': account_id})
        nhantien = response.json() if response.status_code == 200 else None

        if nhantien and 'status' in nhantien and nhantien['status'] == 200:
            print(Colorate.Horizontal(Colors.green_to_blue, f'💰 Nhận được {nhantien["data"]["prices"]} xu! 🎉'))
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, '⚠️ Không nhận được tiền - Bỏ qua nhiệm vụ!'))
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, '⚠️ Không có nhiệm vụ nào!'))

    print(Colorate.Horizontal(Colors.blue_to_cyan, '-------------------------'))
    time.sleep(2)
