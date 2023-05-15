![logo](https://github.com/ThatBlackFox/Questgen.ai/assets/108296426/7d3961bc-20c5-4247-abc8-ae89dfd01ac5)

## 1. Abstract:
intelliDoc is an API service built around a NLP model which generates questions for a given image which contains text, an image of a text book or an article. Makes use of Flask for the backend and a landing page which was coded by [me](https://github.com/ThatBlackFox/) while using the NLP model from [Questgen.ai](https://github.com/ramsrigouthamg/Questgen.ai) with minor changes and debugging to get it to work. As a proof of concept of utilization of this API service we also made a [desktop app](https://github.com/Assault-OPS/intelliDoc) built around this API by my friend [Anand](https://github.com/Assault-OPS).

**Note: This was meant as a college project**


## 2. Installation and Running the server:

```
python setup.py
wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
tar -xvf  s2v_reddit_2015_md.tar.gz
python main.py
```

## 3. Making queries:

image.png

![image](https://github.com/ThatBlackFox/Questgen.ai/assets/108296426/86efef62-e9c6-4729-b942-7e613549c992)

### Code:

```
import requests

files = {'file': open('image.png','rb')}
r = requests.post("http://localhost:5000/api/v3?type=img&full=true", files=files)
print(r.json)
```

### Output:

```
{
   "mc_qs":{
      "questions":[
         {
            "answer":"ddos attacks",
            "context":"Learn about DoS and DDoS attacks.",
            "extra_options":[
               
            ],
            "id":1,
            "options":[
               "Ddos"
            ],
            "options_algorithm":"sense2vec",
            "question_statement":"What are the DoS and DDoS attacks?",
            "question_type":"MCQ"
         }
      ],
      "statement":"& | Toots and Methods\nUsed in Cybercrime\n\nLearning Objectives\n\nAfter reading this chapter",
      "time_taken":19.39649772644043
   },
   "short_qs":{
      "questions":[
         {
            "Answer":"ddos attacks",
            "Question":"What are the DoS and DDoS attacks?",
            "context":"Learn about DoS and DDoS attacks.",
            "id":1
         }
      ],
      "statement":"& | Toots and Methods\nUsed in Cybercrime\n\nLearning Objectives\n\nAfter reading this chapter"
   },
   "text":{
      "input_text":"& | Toots and Methods\nUsed in Cybercrime\n\nLearning Objectives\n\nAfter reading this chapter",
      "max_questions":10
   }
}```