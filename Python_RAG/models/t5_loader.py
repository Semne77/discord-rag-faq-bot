from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = "t5-base"  # Change to "t5-small" for faster or "t5-large" for better outputs

tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)