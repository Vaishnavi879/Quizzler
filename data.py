import requests
AMOUNT=10

parameters={
    "amount":AMOUNT,
    "type":"boolean",
    "category": 18
}

response=requests.get(url="https://opentdb.com/api.php",params=parameters)
question_data=[]
for i in range(AMOUNT):
    question=response.json()["results"][i]["question"]
    answer=response.json()["results"][i]["correct_answer"]
    question_data.append({"question":question,"answer":answer})

