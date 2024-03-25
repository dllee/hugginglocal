from transformers import pipeline

# Mistral-7B-Instruct-v0.2 모델을 사용하여 텍스트 생성 파이프라인 초기화
generator = pipeline('text-generation', model='mistralai/Mistral-7B-Instruct-v0.2')

# 모델에 텍스트 입력하여 생성 시작
text = "대한민국 수도는?"
generated_text = generator(text, max_length=50, num_return_sequences=1)

print(generated_text[0]['generated_text'])
