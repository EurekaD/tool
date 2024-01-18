from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline

tokenizer = BertTokenizer.from_pretrained("uer/gpt2-distil-chinese-cluecorpussmall")
model = GPT2LMHeadModel.from_pretrained("uer/gpt2-distil-chinese-cluecorpussmall")

text_generator = TextGenerationPipeline(model, tokenizer)
text = text_generator("你好", max_length=100, do_sample=True)
print(text)