# Team Name: Brute-Force 👨‍💻

## Team Members:
### 1. Gaurav Sahani 👨‍💻
### 2. Nilesh Verma 👨‍💻
### 3. Aishwarya Muchandi 👩‍💻
### 4. Harsh Parikh 👨‍💻
### 5. Archish Koshe 👨‍💻

# Project Name: Sarcasm and Sentiment Detection 😀😐☹
## Overview:
### Sarcasm and Sentiment Analysis is the project targeted towards dealing with Sarcastic comments associated and sentiments associated with them. Our main focus is the Product feedbacks, and to improvising them. We know nowadays, Sarcasm plays an crutial role when it comes to any product/business, interpreting wrong sentiments out of these comments can lead to misconceptions when dealing with product development/analysis/upgradations while genuine reviews stay aside!  
### Recently, a passenger flying with Indigo Airways, had wrote quiet a sarcastic comments which was negative in nature, the Indigo twitter bot was quiet intelligent to tackle these comments, which replied back in sarcasm. Well, with this growing sarcastic social world, there should be a need to capture or filter out these sarcastic comments, while keeping only genuine comments for analysis.
### There comes our project "Sarcasm and Sentiment Detection", where we have tried to tackle this rising issue. We target to not only detect the sarcasms out of the comments, but also capture the sentiments associated with them. Our UI/UX is designed to preoduce the results in a most interactive way possible.

## The problem it solves:
### For every New product launched/upgraded/replaced, gains tonnes comments, where these comments act crutial as far as product development is concered. With this growing trend of sarcasm, bots are incompatible to collect real sentiments associated with these comments. This is where our application comes into picture, our application detects these sarcastic comments, which can be later filtered out taking only Genuine comments into consideration. Also with sacrasm detection, our application also deals with extracting sentiments from these comments such as comments being Positive,Neutral or Negative. 

## Problems We Faced:
### The first problem we come across is that, unlike in sentiment analysis where the sentiment categories are very clearly defined (love objectively has a positive sentiment, hate a negative sentiment no matter who you ask or what language you speak), the borders of sarcasm aren’t that well defined. And it is crucial that before starting to detect it, to have a notion of what sarcasm is. 
### For that particular reason we used Bi-directional LSTM, Which is used for parsing the statements from both the ends, and since sarcasm is a twist of emotions introduced in the same statement, and there comes a need to detect those twist of emotions in statement. Hence we can detect the statement being a Sarcasm! These LSTM's executing from both ends will reach producing a polarity, which will be used to detect the Sarcasm!

