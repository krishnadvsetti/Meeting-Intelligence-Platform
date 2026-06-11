from datasets import load_dataset

dataset = load_dataset("huuuyeah/meetingbank")

print(dataset)

train = dataset["train"]

print(train[0])