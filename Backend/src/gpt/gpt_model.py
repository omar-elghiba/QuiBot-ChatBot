from transformers import GPT2Tokenizer,TFGPT2LMHeadModel
gpt2_tokenizer=GPT2Tokenizer.from_pretrained("gpt2")
tf_gpt2_model=TFGPT2LMHeadModel.from_pretrained("src/models/tf_gpt2_model_2_15_epoch_4")