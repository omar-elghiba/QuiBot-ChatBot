from src.bert.bert_model import biobert_tokenizer,question_extractor_model1
from src.gpt.gpt_model import gpt2_tokenizer, tf_gpt2_model
from src.prepare.prepare_data import preprocess
from src.faiss.faiss_model import preparing_gpt_inference_data
import tensorflow as tf
import numpy as np


def give_answer(question,answer_len):
    preprocessed_question=preprocess(question)
    question_len=len(preprocessed_question.split(' '))
    truncated_question=preprocessed_question
    if question_len>500:
      truncated_question=' '.join(preprocessed_question.split(' ')[:500])
    encoded_question= biobert_tokenizer.encode(truncated_question)
    max_length=512
    padded_question=tf.keras.preprocessing.sequence.pad_sequences(
        [encoded_question], maxlen=max_length, padding='post')
    question_mask=[[1 if token!=0 else 0 for token in question] for question in padded_question]
    embeddings=question_extractor_model1({'question':np.array(padded_question),'question_mask':np.array(question_mask)})
    gpt_input=preparing_gpt_inference_data(truncated_question,embeddings.numpy())
    mask_start = len(gpt_input) - list(gpt_input[::-1]).index(4600) + 1
    input=gpt_input[:mask_start+1]
    if len(input)>(1024-answer_len):
      input=input[-(1024-answer_len):]
    gpt2_output=gpt2_tokenizer.decode(tf_gpt2_model.generate(input_ids=tf.constant([np.array(input)]),max_length=1024,temperature=0.7)[0])
    answer=gpt2_output.rindex('`ANSWER: ')
    return gpt2_output[answer+len('`ANSWER: '):]


def final_func_1(question):
    answer_len=25
    return give_answer(question,answer_len)

  