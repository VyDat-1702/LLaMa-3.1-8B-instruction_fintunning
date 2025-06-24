import json

input_file = "/home/vydat/Code/AI/vietnamese chatbot/shuffled_vi_sentences.json" 
output_file = "/home/vydat/Code/AI/vietnamese chatbot/formated_data.json"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        custom_data = json.load(f)
except FileNotFoundError:
    print(f"Không tìm thấy file {input_file}. Vui lòng kiểm tra đường dẫn.")
    exit(1)
except json.JSONDecodeError:
    print(f"File {input_file} không đúng định dạng JSON.")
    exit(1)


converted_data = []
for item in custom_data:

    if "input" not in item or "output" not in item:
        print(f"Dữ liệu không hợp lệ, bỏ qua: {item}")
        continue
    
    conversation = {
        "conversations": [
            {
                "from": "human",
                "value": f"Hãy chuyển sang cấu trúc ngôn ngữ nói: '{item['input']}'"
            },
            {
                "from": "assistant",
                "value": item['output']
            }
        ]
    }
    converted_data.append(conversation)

try:
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(converted_data, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu dữ liệu vào '{output_file}' với {len(converted_data)} cuộc hội thoại.")
except Exception as e:
    print(f"Lỗi khi lưu file {output_file}: {str(e)}")

print("\nMẫu dữ liệu đã chuyển đổi (3 mẫu đầu tiên):")
for i, conv in enumerate(converted_data[:3]):
    print(f"\nMẫu {i + 1}:")
    print(json.dumps(conv, ensure_ascii=False, indent=2))