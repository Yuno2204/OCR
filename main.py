import requests
def perform_ocr(image_path):
    response = requests.post(
        url="https://nonconvertibly-ungeographic-ranee.ngrok-free.dev/ocr",
        json={
            "image_url": image_path
        }
    )

    print("Response time =", response.elapsed.total_seconds())

    if response.status_code == 200:
        return response.json().get("response_message")
    else:
        print("Error:", response.status_code, response.text)
        return None


# ================== CHẠY Ở ĐÂY ==================

image_path = "https://adg.vn/wp-content/uploads/2022/02/Screen-Shot-2022-02-17-at-11.00.44-AM.png"

result = perform_ocr(image_path)

if result:
    print("OCR Recognition Result:")
    print(result)
else:
    print("Không nhận được kết quả OCR")
