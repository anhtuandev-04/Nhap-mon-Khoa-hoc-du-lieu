import requests
from bs4 import BeautifulSoup
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def scrape():
    url = "https://dulieuvietphuc.blogspot.com/2026/04/ve-ep-quyen-uy-trong-co-phuc-trieu.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print("--- Đang bắt đầu quá trình thu thập dữ liệu ---")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'lxml')
        title_tag = soup.find('h3', class_='post-title entry-title')

        if title_tag:
            raw_title = title_tag.get_text(strip=True)
            print(f"[1] Dữ liệu thô từ BS4: {raw_title}")
      
            clean_title = raw_title 
    
            main_topic_match = re.search(r'^[^:]+', clean_title)
            
            print("-" * 30)
            print(f"KẾT QUẢ CUỐI CÙNG:")
            print(f"Full Title: {clean_title}")
            if main_topic_match:
                print(f"Chủ đề chính: {main_topic_match.group().strip()}")
            print("-" * 30)

        else:
            print("Lỗi: Không tìm thấy thẻ h3 với class 'post-title entry-title'.")

    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối (Requests): {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

if __name__ == "__main__":
    scrape()