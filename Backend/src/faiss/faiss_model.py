from src.gpt.gpt_model import gpt2_tokenizer
import faiss
import numpy as np
import pandas as pd



qa=pd.read_pickle('src/models/train_gpt_data.pkl')
question_bert = qa["Q_FFNN_embeds"].tolist()
answer_bert = qa["A_FFNN_embeds"].tolist()
question_bert = np.array(question_bert)
answer_bert = np.array(answer_bert)

question_bert = question_bert.astype('float32')
answer_bert = answer_bert.astype('float32')

answer_index = faiss.IndexFlatIP(answer_bert.shape[-1])

question_index = faiss.IndexFlatIP(question_bert.shape[-1])
answer_index.add(answer_bert)
question_index.add(question_bert)


def preparing_gpt_inference_data(question,question_embedding):
  topk=20
  scores,indices=answer_index.search(
                  question_embedding.astype('float32'), topk)
  q_sub=qa.iloc[indices.reshape(20)]
  ans = '`QUESTION: %s `ANSWER: ' % (
                        question)
  line = '`QUESTION: %s `ANSWER: ' % (
                        question)
  encoded_len=len(gpt2_tokenizer.encode(line))
  for i in q_sub.iterrows():
    ans = '`QUESTION: %s `ANSWER: %s ' % (i[1]['question'],i[1]['answer'])
    print(ans)
    line='`QUESTION: %s `ANSWER: %s ' % (i[1]['question'],i[1]['answer']) + line
    line=line.replace('\n','')
    encoded_len=len(gpt2_tokenizer.encode(line))
    if encoded_len>=1024:
      break
  return gpt2_tokenizer.encode(line)[-1024:]