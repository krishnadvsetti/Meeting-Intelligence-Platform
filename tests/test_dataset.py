from datasets import load_dataset

dataset = load_dataset("edinburghcstr/ami", split="train[:1]")

print(dataset)
print(dataset[0])