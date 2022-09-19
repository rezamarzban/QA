from transformers import pipeline

qa_model = pipeline("question-answering")

context = "Reza Marzban is a chemical engineering and inventor with 16 years researchs, studies and experiments in IT, Electronics, Mechanics and so on."
print("	")
print("Context:", context)
print("	")

question1 = "Who is Reza Marzban?"
question2 = "How many years does he research?"
question3 = "Which fields does he research in?"
question4 = "Who is an inventor?"

result1 = qa_model(question = question1, context = context)
result2 = qa_model(question = question2, context = context)
result3 = qa_model(question = question3, context = context)
result4 = qa_model(question = question4, context = context)

print(" ")
print("Question 1:", question1)
print("Answer:", result1["answer"])
print("	")
print("Question 2:", question2)
print("Answer:", result2["answer"])
print(" ")
print("Question 3:", question3)
print("Answer:", result3["answer"])
print(" ")
print("Question 4:", question4)
print("Answer:", result4["answer"])
print(" ")
