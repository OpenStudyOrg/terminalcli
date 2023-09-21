import json

print("Welcome to OpenStudy!")
file = input("Please enter your study file: ")

with open(file) as f:
    data = json.load(f)["methods"]["typing"]
    print("Answer these questions by typing them: ")
    while not data == []:
        ndata = []
        for question in data:
            print(question["question"])
            answer = input("Answer: ")
            if answer == question["answer"]:
                print("Correct!\n")
            else:
                print("Incorrect!\n")
                ndata.append(question)
        data = ndata
    print("Study completed!")
