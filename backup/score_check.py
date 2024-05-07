import os
import json
import numpy as np

file_list = os.listdir("./results/")
word_average_scores = []
vocab_average_scores = []
phone_average_scores = []
syllable_average_scores = []
speechace_scores = []

for file_name in file_list:
    # if 'part' not in file_name:
    #     continue
    # file_name = '58_partB_6_0_audio_hesiation.json'
    try:
        result = json.loads(open("./results/" + file_name, 'r', encoding='utf-8').read())
        word_score_list = result['speech_score']['word_score_list']
        if len(word_score_list) <= 10:
            continue
        
        speechace_score = result['speech_score']['speechace_score']['pronunciation']
        speechace_scores.append(speechace_score)
    
    except:
        # print("No score, skip")
        continue
    
    print(file_name)


    ## Word-wise average
    word_scores = []
    for word in word_score_list:
        word_scores.append(word['quality_score'])
        
    average_score = np.mean(word_scores)
    word_average_scores.append(average_score)
    print("Word average score: ", average_score)
    
    
    
    ## Vocabulary-wise average
    vocab_count = {}
    for word in word_score_list:
        if word['word'] in vocab_count:
            vocab_count[word['word']].append(word['quality_score'])
        else:
            vocab_count[word['word']] = [word['quality_score']]
    
    vocab_scores = []
    for vocab, scores in vocab_count.items():
        vocab_scores.append(np.mean(scores))
    average_score = np.mean(vocab_scores)
    vocab_average_scores.append(average_score)
    print("Vocabulary average score: ", average_score)
    
    
    
    ## Phone-wise average
    phone_count = {}
    for word in word_score_list:
        for phone in word['phone_score_list']:            
            if phone['phone'] in phone_count:
                phone_count[phone['phone']].append(phone['quality_score'])
            else:
                phone_count[phone['phone']] = [phone['quality_score']]
    
    phone_scores = []
    for phone, scores in phone_count.items():
        phone_scores.append(np.mean(scores))
    average_score = np.mean(phone_scores)
    phone_average_scores.append(average_score)
    print("Phone average score: ", average_score)
    
    
    
    ## Syllable-wise average
    syllable_count = {}
    for word in word_score_list:
        for syllable in word['syllable_score_list']:            
            if syllable['letters'] in syllable_count:
                syllable_count[syllable['letters']].append(syllable['quality_score'])
            else:
                syllable_count[syllable['letters']] = [syllable['quality_score']]
    
    syllable_scores = []
    for syllable, scores in syllable_count.items():
        syllable_scores.append(np.mean(scores))
    average_score = np.mean(syllable_scores)
    syllable_average_scores.append(average_score)
    print("Syllable average score: ", average_score)
    
    print("Speechace score: ", speechace_score)



print("Word average")
word_diff = np.array(speechace_scores) - np.array(word_average_scores)
correlation_matrix = np.corrcoef(speechace_scores, word_average_scores)
correlation = correlation_matrix[0, 1]
print("Correlation coefficient:", correlation)
print(word_diff)
print(np.mean(np.abs(word_diff)))
print(np.mean(word_diff))
print(np.var(word_diff))


print("Vocabulary average")
vocab_diff = np.array(speechace_scores) - np.array(vocab_average_scores)
correlation_matrix = np.corrcoef(speechace_scores, vocab_average_scores)
correlation = correlation_matrix[0, 1]
print("Correlation coefficient:", correlation)
print(vocab_diff)
print(np.mean(np.abs(vocab_diff)))
print(np.mean(vocab_diff))
print(np.var(vocab_diff))


print("Phone average")
phone_diff = np.array(speechace_scores) - np.array(phone_average_scores)
correlation_matrix = np.corrcoef(speechace_scores, phone_average_scores)
correlation = correlation_matrix[0, 1]
print("Correlation coefficient:", correlation)
print(phone_diff)
print(np.mean(np.abs(phone_diff)))
print(np.mean(phone_diff))
print(np.var(phone_diff))



print("Syllable average")
syllable_diff = np.array(speechace_scores) - np.array(syllable_average_scores)
correlation_matrix = np.corrcoef(speechace_scores, syllable_average_scores)
correlation = correlation_matrix[0, 1]
print("Correlation coefficient:", correlation)
print(syllable_diff)
print(np.mean(np.abs(syllable_diff)))
print(np.mean(syllable_diff))
print(np.var(syllable_diff))
