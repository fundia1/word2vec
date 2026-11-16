import json

# 입력 및 출력 파일 경로
input_file = "proverbs.jsonl"
output_file = "proverbs.txt"

proverbs = []

# JSONL 파일 읽기
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        try:
            data = json.loads(line)
            ko = data.get("ko")

            if isinstance(ko, str) and ko.strip():
                proverbs.append(ko.strip())

        except json.JSONDecodeError:
            print("JSON 파싱 오류:", line[:100])

# TXT 파일 저장
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(proverbs))

print(f"추출 완료: {len(proverbs)}개")
print(f"저장 파일: {output_file}")
