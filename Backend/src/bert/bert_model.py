from transformers import AutoTokenizer, TFAutoModel

import tensorflow as tf


biobert_tokenizer = AutoTokenizer.from_pretrained("cambridgeltl/BioRedditBERT-uncased")
question_extractor_model1=tf.keras.models.load_model('src/models/question_extractor_model_2_11' , compile=False)