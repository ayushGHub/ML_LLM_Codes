## Attention in Transformers: Concepts and Code in PyTorch

1. Machine Translation Paper by Yoshua Bengio group ICLR 2015, and Chris Manning group both gave similar idea. 
 --  Encoder Decoder model is effective for Machine Translation
2. Contextual Embedding
 -- Dense per word vector captures the meaning of the each words in the context of the sentence.
Once input is to these vectors then decoder uses thesev ectors as input. Output one word at a tome.
3. Decoder has access to each word embedding of the input sentence.
4. In 2017 Attention is all Need - Published by Google Brain Team - Introduced Transofrmaer Architecture and more general form of Attention. - Highlyt Scalable to be designed for GPU. Followed Machine Translation.
5. Encoder Model is the basis for the BERT (Bi-Directional Encoder Representation from Transformer) Algorithm - basis for all the embedding algorithms in RAG etc.
6. Decoder Model has been used as the basis for GPT (Generative Pre-trained Transformer) family of LLM and laos the basis for Mistral, Gemini, Anthropic, Llamam.
7. BERT has 6 layer of attention while Llama3.2-405B by Meta has 126 and GPT3 has 96 layers but basisc architecture is same.

#### Main Idea Behind Transformaers and Attention
Transformers need 3 basic part. 1. Word Embedding, 2. Positional Encoding, 3. Attention
Word Embedding layers turns texts/sentences/words into numbers. 
Positional Encoding help keeps track of the word order.
Transformer establishes relationshio among words in the sentence. They have somethign called ATTENTION which correctly associates the words to oteher words for menaniful understanding.
1. Self-Attention - It works by seeing how a word is similar to all other words in the sentence. It calculates suimilarity between the first word and all other words in the sentence including itself. Self-Attention does this for every word in the sentence. Once similarity is calcuated it is then used to determine how transformer encodes each words - how each word is associated with other words.
#### Matrix Math for Calculating Self Attention 
How and Why the equaltion works the way it does.

- *Attention(Q,K,V) = softmax(QK^T/sqrt(d_k))V*, 

- Query, Key and Value - comes from Databse terminology. Search term is called is QUERY in database, where all actual entries are the KEYS, so computer compare query with all the keys in the dabatse and ranked each one of them. So computer return the VALUE. Query we are using to search the database and 
to get a value at the end.
- How to determine QKV in context of Attention.
First -SA calcutaes similarity btw each word and all other includes itself in the sentence. We need to calcutae Query and Key for each word. Each Key needs to return a value. It's more common to use 512 or more numbers to encode/represent a word.
- Calculates Scaled Dot product similaroties among all the words, convert those scaled similarities into percentages with the softmax function, and then use those percentages to scale the Values to become the Self-Attention scores for each word.

##### Coding Self Attention in PyTorch
#### Self Attention and Masked Self Attention
- Main idea behind attention is that it helps establish the relationship among words.
- **How to convert words into numbers** -- 
Years before Transformers, people create standalone Neural Networks to create work embedding. Let's build 
The first thing we do is create inputs to a relatively simple neural network for each unique word. Then create output for each word.
Connect input to activation functions (one or more activation functions). The number of activation functions determine how many numbers we will use to represent each word that goes about having the dimenions of the word embedding. If there is 2 activation function then we will have 2 numbers for each word and then we can map those words in 2 dimensional space and that mapping will give us proximity of similar words. Like Great and Awesome lying somewhere together in the 2D plot.
We add WEIGHTS, numbers we multiply the inputs by, to the connection from the inputs to the activation functions. Weights are the word embdding alues are som random numbers. Then train them and chnage them accordingly. And then connection activation to outputs.
QUESTION is What we will be loss and how it will calculated? **MultipleNegativeRankingLoss** function????
- Just prediction next work does not give ots of contenxt to detrming the optimjial word embeddings. If we have complicated dataset adn then we have more input and more output and once we connect, longer sentence in training data, we can add more context in the training process. instead of using 1 workd to precict 1, we can use 4 words t predict next word to learn more about context, but htere we do not track thw eord order and all are jumbled up. Word order are critical. Tom ate Pizza and Pizza eat Tom have same meaningn wi this basic word embedding scenario. This is exactly what **Positional Encoiding** layer in a Transformer does. It allows us to take word order into the account when creating Embeddings. And that is then is followed by **Attention Layer** that, as we saw earlier, helps establish relationship among words. And when we use Self-Attention whcih factors in all of the words including those came after the word of interest. So then we end up areating a new kind of embeddng that is also called **Context Aware Embedding** or **Contexualized Embedding**. Compared to Word Embedding, which only clusters individual words, CAE can cluster similar sentences or documents.
- Transformers that only use Self Attention are called Encoder Only Transformers and the Context Aware Embeddings that they create are super useful. Then we can use CAE as inputs to a normal neural network that classifies the sentiment of the input.We can use it as a variable in logistic regression model for classification. It can be used in wide variety of settings. This is Encoder Only Transofmrer which only uses Self Attention.
- **Decoder Only Transformer** starts out with Word Embedding and Positional Encoding as well, but instead of using Self Attention they use **Masked Self Attention** and the big difference between them that SA can see words before and after word of interest but MSA ignores the words after the word  of interest. Beause Decoder Only Trasnformers use masked Self Attention, can can never look ahead oat what comes next, they can be trained really good hob generating responses to prompt. That is why ChatGPT which is Decoder Only Transofrmaer is callaed Generative Model.

#### Matrix Math for Calculating Masked Self Attention 
- *MaskedAttention(Q,K,V,M) = softmax(QK^T/sqrt(d_k) + M)V*
- The only difference beween the equation of SA ans MSA is that we add new matrix M to the scaled similarities. Masked Matrix M that is added has roght half diagnoally as *-inf* to the value needed to be maksed out, while adding 0 to the rest of the diagnoally left half so that those reamin unchanged after addition.
##### Coding Masked Self-Attention in PyTorch
#### Encoder-Decoder Attention
- So far we have seen how Encoder only used self attention for context aware emebdding for cluster similarm words, sentences or document and that is just start. And how Decoder only sed masked SA to generate long streams of new token based on previous tokens.
First tranfromer ever made was one part callned Encoder using Self Attention and another part Decoder which used Masked.
- Encoder-Decoder Attention uses the output from the Encoder to calculate the Keys and Values and the Queries are calcuated from the output of the MSA generated by the decoder. Once the Q,K and V are calucated ENcoder-Decoder Attention is calcuated is just like Self Attention using every similarity. The first Trasnfer was based on somthing called Seq2Seq or and Encoder-Decoder model.
- Seq2Seq moels were designed to translate text in one langauge, like Enlgish into another language like Spanish or French.
- Now we have 3rd type of Attention, Encoder Decoder attention which is also called Cross-Attention, which gives us flexibility in how we want to calculate the Q,K,V and how we want to use it as seen in Cross Attention.
- Although this style of Seq2Seq model has soemthwat fallen out of favour for language modeling, we still see it what are called Multi Model Model, in MMM, we might have encoder that are trained on images or sound, and the Context Aware Embedding could be fed into a text based Decoder via Encoder-Decoder Attention in order to generate audio prompts.
#### Multi-Head Attention
- So far we have seen Attention helps us establish how each word in the input is related to the other words. And for simple exapke it works fine. In order to correctly establish how words are relaed in longer, more complicated sentences and paragraphs we can apply Attentions to the Encoded Values multiple times simulatenoesly. Each Attention unit is called a HEAD and has its own sets of Weights for calculating the Questries, Keys, and Values. And when we have multiple head calculating Attention, we called it Multihead Attention. First transformaer had 8 Attention Heads. FCL to token output values. So Modify the weight of the Value Weight matrix.
##### Coding Encoder-Decoder Attention and Multi-Head Attention in PyTorch
