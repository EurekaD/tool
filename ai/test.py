from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


# 输入一个初始文本
input_text = "How are you ? Can I ask some question to you?"

# 将输入文本编码成模型可以理解的格式
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# 使用模型生成文本
output = model.generate(input_ids, max_length=200, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

# 将生成的文本解码成人类可读的格式
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# 打印生成的文本
print(generated_text)