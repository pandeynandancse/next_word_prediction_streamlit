import os
import streamlit as st
import torch
import string
import pynput
# from pynput.keyboard import Key, Controller
# keyboard = Controller()



from pynput import keyboard

# class MyException(Exception): pass






top_k = 10
def load_model(model_name):
	try:
  		print("inside load function")
        if model_name.lower() == "bert":
      	from transformers import BertTokenizer, BertForMaskedLM
      	bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
      	bert_model = BertForMaskedLM.from_pretrained('bert-base-uncased').eval()
      	return bert_tokenizer,bert_model
  	except Exception as e:
    	pass








def decode(tokenizer, pred_idx, top_clean):
	print("decode funciton")
	ignore_tokens = string.punctuation + '[PAD]'
    tokens = []
    for w in pred_idx:
    	token = ''.join(tokenizer.decode(w).split())
        if token not in ignore_tokens:
            tokens.append(token.replace('##', ''))
    return '\n'.join(tokens[:top_clean])




def encode(tokenizer, text_sentence, add_special_tokens=True):
	print("encode funtion")
    text_sentence = text_sentence.replace('<mask>', tokenizer.mask_token)
    # if <mask> is the last token, append a "." so that models dont predict punctuation.
    if tokenizer.mask_token == text_sentence.split()[-1]:
        text_sentence += ' .'

        input_ids = torch.tensor([tokenizer.encode(text_sentence, add_special_tokens=add_special_tokens)])
        mask_idx = torch.where(input_ids == tokenizer.mask_token_id)[1].tolist()[0]
    return input_ids, mask_idx







def get_all_predictions(text_sentence, top_clean=5):
    # ========================= BERT =================================
    print(text_sentence)
  	input_ids, mask_idx = encode(bert_tokenizer, text_sentence)
  	with torch.no_grad():
    	predict = bert_model(input_ids)[0]
  	bert = decode(bert_tokenizer, predict[0, mask_idx, :].topk(top_k).indices.tolist(), top_clean)

  	return {'bert': bert}








def get_prediction_eos(input_text):
	print("prediction eos function")
  	try:
    	# input_text = ' '.join(request.json['input_text'].split())
    	input_text += ' <mask>'
        # top_k = request.json['top_k']
    	res = get_all_predictions(input_text, top_clean=int(top_k))
    	return res
  	except Exception as error:
    	pass








try:

  	# screen = Screen()
  	st.title("Next Word Prediction with Pytroch")
    st.sidebar.text("Next Word Prediction")
    model_name = st.sidebar.selectbox(label='Select Model to Apply',  options=['BERT', 'XLNET'], index=0,  key = "model_name")


    bert_tokenizer, bert_model  = load_model(model_name) 
    input_text = st.text_area("Enter your text here", "enter")
  # res = get_prediction_eos(input_text)
  # def space_triggered:
  #   st.text_area(input_text)
  

  # screen.onkey(space_triggered, "space")

  # screen.listen()

  # screen.mainloop()


    def on_press(key):
    	if key == keyboard.Key.space:
            res = get_prediction_eos(input_text)
            st.text_area("Next Preds",res)

# Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:

        try:
            listener.join()
        except MyException as e:
            print('{0} was pressed'.format(e.args[0]))



except Exception as e:
    print("SOME PROBLEM OCCURED")