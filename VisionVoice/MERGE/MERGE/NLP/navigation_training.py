import spacy
from spacy.training.example import Example

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")

nlp = spacy.blank("en")
# Check if "ner" component exists in the pipeline, otherwise add it
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner") # loading the blank model

# Add new entity label for hyperlinks
ner.add_label("HYPERLINK")

# Training data in the format you provided
train_data = [
    {"text": "move to data section", "entities": [(8, 12, "HYPERLINK")]},
    {"text": "click the games link", "entities": [(10, 15, "HYPERLINK")]},
    {"text": "open the puzzles", "entities": [(9, 16, "HYPERLINK")]},
    {"text": "I want to learn geometry", "entities": [(16, 24, "HYPERLINK")]},
    {"text": "physics", "entities": [(0, 7, "HYPERLINK")]},
    {"text": "I want to go to basic maths", "entities": [(16, 27, "HYPERLINK")]},
    {"text": "Go to ratios", "entities": [(6, 12, "HYPERLINK")]},
    {"text": "Go to lcm and hcf", "entities": [(6, 17, "HYPERLINK")]},
    {"text": "Explore lcm and hcf", "entities": [(8, 19, "HYPERLINK")]},
    {"text": "lcf and hcf", "entities": [(0, 11, "HYPERLINK")]},
    {"text": "Open factorising quadratics", "entities": [(5, 27, "HYPERLINK")]},
    {"text": "Click factorising quadratics", "entities": [(6, 28, "HYPERLINK")]},
    {"text": "factorising quadratics", "entities": [(0, 22, "HYPERLINK")]},
    {"text": "move to functions", "entities": [(8, 17, "HYPERLINK")]},
    {"text": "Open gradients, graphs and curves", "entities": [(5, 33, "HYPERLINK")]},
    {"text": "gradients, graphs and curves", "entities": [(0, 28, "HYPERLINK")]},
    {"text": "I want to go to gradients, graphs and curves section", "entities": [(16, 44, "HYPERLINK")]},
    {"text": "Move to gradients, graphs and curves", "entities": [(8, 36, "HYPERLINK")]},
    {'text': 'Open stationary points', 'entities': [(5, 22, 'HYPERLINK')]},
    {'text': 'Move to stationary points', 'entities': [(8, 25, 'HYPERLINK')]},
    {'text': 'stationary points', 'entities': [(0, 17, 'HYPERLINK')]},
    {'text': 'Click stationary points', 'entities': [(6, 23, 'HYPERLINK')]},
    {'text': 'Open vectors', 'entities': [(5, 12, 'HYPERLINK')]},
    {'text': 'Go to vectors', 'entities': [(6, 13, 'HYPERLINK')]},
    {'text': "Open pythagoras' theorem", 'entities': [(5, 24,'HYPERLINK')]},
    {'text': "explore pythagoras' theorem", 'entities': [(8, 27, 'HYPERLINK')]},
    {'text': "pythagoras' theorem", 'entities': [(0, 19, 'HYPERLINK')]},
    {'text': "Go to pythagoras' theorem", 'entities': [(6, 25, 'HYPERLINK')]},
    {'text': 'Open bounds', 'entities': [(5, 11, 'HYPERLINK')]},
    {'text': 'Click bounds', 'entities': [(6, 12, 'HYPERLINK')]},
    {'text': 'bounds', 'entities': [(0, 6, 'HYPERLINK')]},
    {'text': 'Go to bounds', 'entities': [(6, 12, 'HYPERLINK')]},
    {"text": "Open introduction to algebra", "entities": [(5, 28, "HYPERLINK")]},
    {"text": "Go to introduction to algebra", "entities": [(6, 29, "HYPERLINK")]},
    {"text": "introduction to algebra", "entities": [(0, 23, "HYPERLINK")]},
    {"text": "Move to introduction to algebra", "entities": [(8, 31, "HYPERLINK")]},
    {"text": "Explore introduction to algebra", "entities": [(8, 31, "HYPERLINK")]},
    {"text": "I want to learn introduction to algebra section", "entities": [(16, 39, "HYPERLINK")]},
    {"text": "balance when adding and subtracting", "entities": [(0, 35, "HYPERLINK")]},
    {"text": "Go to balance when adding and subtracting", "entities": [(6, 41, "HYPERLINK")]},
    {"text": "Open balance when adding and subtracting", "entities": [(5, 40, "HYPERLINK")]},
    {"text": "Explore balance when adding and subtracting", "entities": [(8, 43, "HYPERLINK")]},
    {"text": "Go to introduction to algebra - multiplication", "entities": [(6, 46, "HYPERLINK")]},
    {"text": "introduction to algebra - multiplication", "entities": [(0, 40, "HYPERLINK")]},
    {"text": "Open introduction to algebra - multiplication", "entities": [(5, 45, "HYPERLINK")]},
    {"text": "I want to learn introduction to algebra - multiplication", "entities": [(16, 56, "HYPERLINK")]},
    {"text": "I want to study introduction to algebra - multiplication", "entities": [(16, 56, "HYPERLINK")]},
    {"text": "Order of operations - bodmas", "entities": [(0, 28, "HYPERLINK")]},
    {"text": "Open pemdas", "entities": [(5, 11, "HYPERLINK")]},
    {"text": "pemdas", "entities": [(0, 6, "HYPERLINK")]},
    {"text": "Explore pemdas", "entities": [(8, 14, "HYPERLINK")]},
    {"text": "I want to access pemdas", "entities": [(17, 23, "HYPERLINK")]},
    {"text": "Open substitution", "entities": [(5, 17, "HYPERLINK")]},
    {"text": "substitution", "entities": [(0, 12, "HYPERLINK")]},
    {"text": "Explore substitution", "entities": [(8, 20, "HYPERLINK")]},
    {"text": "I want to access substitution", "entities": [(17, 29, "HYPERLINK")]},
    {"text": "equations and formulas", "entities": [(0, 22, "HYPERLINK")]},
    {"text": "Open equations and formulas", "entities": [(5, 27, "HYPERLINK")]},
    {"text": "Explore equations and formulas", "entities": [(8, 30, "HYPERLINK")]},
    {"text": "Click equations and formulas", "entities": [(6, 28, "HYPERLINK")]},
    {"text": "inequalities", "entities": [(0, 12, "HYPERLINK")]},
    {"text": "Open inequalities", "entities": [(5, 17, "HYPERLINK")]},
    {"text": "Solving inequalities", "entities": [(0, 20, "HYPERLINK")]},
    {"text": "Click solving inequalities", "entities": [(6, 26, "HYPERLINK")]},
    {"text": "Go to the solving inequalities section", "entities": [(10, 30, "HYPERLINK")]},
    {"text": "open solving inequalities section", "entities": [(5, 25, "HYPERLINK")]},
    {"text": "Explore solving inequalities", "entities": [(8, 28, "HYPERLINK")]},
    {"text": "exponent", "entities": [(0, 8, "HYPERLINK")]},
    {"text": "I want to learn negative exponents", "entities": [(16, 34, "HYPERLINK")]},
    {"text": "negative exponents", "entities": [(0, 18, "HYPERLINK")]},
    {"text": "Go to the negative exponents section", "entities": [(10, 28, "HYPERLINK")]},
    {"text": "Open negative exponents", "entities": [(5, 23, "HYPERLINK")]},
    {"text": "Explore negative exponents", "entities": [(8, 26, "HYPERLINK")]},
    {"text": "I want to learn reciprocal in algebra", "entities": [(16, 37, "HYPERLINK")]},
    {"text": "reciprocal in algebra", "entities": [(0, 21, "HYPERLINK")]},
    {"text": "Go to the reciprocal in algebra section", "entities": [(10, 31, "HYPERLINK")]},
    {"text": "Open reciprocal in algebra", "entities": [(5, 26, "HYPERLINK")]},
    {"text": "Explore reciprocal in algebra", "entities": [(8, 29, "HYPERLINK")]},
    {"text": "Open square roots", "entities": [(5, 17, "HYPERLINK")]},
    {"text": "square roots", "entities": [(0, 12, "HYPERLINK")]},
    {"text": "Go to the square roots section", "entities": [(10, 22, "HYPERLINK")]},
    {"text": "Open cube roots", "entities": [(5, 15, "HYPERLINK")]},
    {"text": "cube roots", "entities": [(0, 10, "HYPERLINK")]},
    {"text": "Explore cube roots", "entities": [(8, 18, "HYPERLINK")]},
    {"text": "I want to learn cube roots", "entities": [(16, 26, "HYPERLINK")]},
    {"text": "Go to the nth roots section", "entities": [(10, 19, "HYPERLINK")]},
    {"text": "Open nth roots", "entities": [(5, 14, "HYPERLINK")]},
    {"text": "nth roots", "entities": [(0, 9, "HYPERLINK")]},
    {"text": "Open surds", "entities": [(5, 10, "HYPERLINK")]},
    {"text": "Go to the surds", "entities": [(10, 15, "HYPERLINK")]},
    {"text": "surds", "entities": [(0, 5, "HYPERLINK")]},
    {"text": "Go to applications of linear equations", "entities": [(6, 38, "HYPERLINK")]},
    {"text": "applications of linear equations", "entities": [(0, 32, "HYPERLINK")]},
    {"text": "applications of linear equations", "entities": [(0, 32, "HYPERLINK")]},
    {"text": "Go to absolute value equations", "entities": [(6, 30, "HYPERLINK")]},
    {"text": "absolute value equations", "entities": [(0, 24, "HYPERLINK")]},
    {"text": "Go to absolute value inequalities", "entities": [(6, 33, "HYPERLINK")]},
    {"text": "absolute value inequalities", "entities": [(0, 27, "HYPERLINK")]},
    {"text": "Open lines, circles and piecewise functions", "entities": [(5, 43, "HYPERLINK")]},
    {"text": "lines, circles and piecewise functions", "entities": [(0, 38, "HYPERLINK")]},
    {"text": "Open logarithm functions", "entities": [(5, 24, "HYPERLINK")]},
    {"text": "logarithm functions", "entities": [(0, 19, "HYPERLINK")]},
    {"text": "Visit to exponential functions", "entities": [(9, 30, "HYPERLINK")]},
    {"text": "exponential functions", "entities": [(0, 21, "HYPERLINK")]},
    {"text": "Visit to linear systems with two variables", "entities": [(9, 42, "HYPERLINK")]},
    {"text": "linear systems with two variables", "entities": [(0, 33, "HYPERLINK")]},
    {"text": "visit to linear systems with three variables", "entities": [(9, 44, "HYPERLINK")]},
    {"text": "linear systems with three variables", "entities": [(0, 35, "HYPERLINK")]},
    {"text": "solving inequality word questions", "entities": [(0, 33, "HYPERLINK")]},
    {"text": "explore solving inequality word questions", "entities": [(8, 41, "HYPERLINK")]},
    {"text": "I want to study completing the square", "entities": [(16, 37, "HYPERLINK")]},
    {"text": "completing the square", "entities": [(0, 21, "HYPERLINK")]},
    {"text": "equation of a straight line", "entities": [(0, 27, "HYPERLINK")]},
    {"text": "Open equation of a straight line", "entities": [(5, 32, "HYPERLINK")]},
    {"text": "Visit to equation of a straight line", "entities": [(9, 36, "HYPERLINK")]},
    {"text": "equation of a straight line", "entities": [(0, 27, "HYPERLINK")]},
    {"text": "Explore rationalizing the denominator", "entities": [(8, 37, "HYPERLINK")]},
    {"text": "rationalizing the denominator", "entities": [(0, 29, "HYPERLINK")]},
    {"text": "I want to study polynomial long multiplication", "entities": [(16, 46, "HYPERLINK")]},
    {"text": "polynomial long multiplication", "entities": [(0, 30, "HYPERLINK")]},
    {"text": "open polynomial long multiplication", "entities": [(5, 35, "HYPERLINK")]},
    {"text": "I want to study directly proportional and inversely proportional", "entities": [(16, 64, "HYPERLINK")]},
    {"text": "directly proportional and inversely proportional", "entities": [(0, 48, "HYPERLINK")]},
    {"text": "Open how to graph functions and linear equations", "entities": [(5, 48, "HYPERLINK")]},
    {"text": "how to graph functions and linear equations", "entities": [(0, 43, "HYPERLINK")]},
    {"text": "Visit how to solve system of linear equations", "entities": [(6, 45, "HYPERLINK")]},
    {"text": "how to solve system of linear equations", "entities": [(0, 39, "HYPERLINK")]},
    {"text": "Open polynomial functions", "entities": [(5, 25, "HYPERLINK")]},
    {"text": "polynomial functions", "entities": [(0, 20, "HYPERLINK")]},
    {"text": "Explore exponential and logarithmic functions", "entities": [(8, 45, "HYPERLINK")]},
    {"text": "exponential and logarithmic functions", "entities": [(0, 37, "HYPERLINK")]},
    {"text": "Visit to graph inequalities", "entities": [(9, 27, "HYPERLINK")]},
    {"text": "graph inequalities", "entities": [(0, 18, "HYPERLINK")]},
    {"text": "Visit to solving systems of equations in two variables", "entities": [(9, 54, "HYPERLINK")]},
    {"text": "solving systems of equations in two variables", "entities": [(0, 45, "HYPERLINK")]},
    {"text": "Visit to solving systems of equations in three variables", "entities": [(9, 56, "HYPERLINK")]},
    {"text": "solving systems of equations in three variables", "entities": [(0, 47, "HYPERLINK")]},
    {"text": "Go to matrix properties", "entities": [(6, 23, "HYPERLINK")]},
    {"text": "matrix properties", "entities": [(0, 17, "HYPERLINK")]},
    {"text": "Go to matrix operations", "entities": [(6, 23, "HYPERLINK")]},
    {"text": "matrix operations", "entities": [(0, 17, "HYPERLINK")]},
    {"text": "Go to how to graph quadratic functions", "entities": [(6, 38, "HYPERLINK")]},
    {"text": "How to graph quadratic functions", "entities": [(0, 32, "HYPERLINK")]},
    {"text": "Go to how to solve quadratic equations", "entities": [(6, 38, "HYPERLINK")]},
    {"text": "how to solve quadratic equations", "entities": [(0, 32, "HYPERLINK")]},
    {"text": "Go to basic knowledge of polynomial functions", "entities": [(6, 45, "HYPERLINK")]},
    {"text": "basic knowledge of polynomial functions", "entities": [(0, 39, "HYPERLINK")]},
    {"text": "Go to operate on rational expressions", "entities": [(6, 37, "HYPERLINK")]},
    {"text": "Go to logarithm and logarithm functions", "entities": [(6, 39, "HYPERLINK")]},
    {"text": "Go to logarithm property", "entities": [(6, 24, "HYPERLINK")]},
    {"text": "Go to arithmetic sequences and series", "entities": [(6, 37, "HYPERLINK")]},
    {"text": "arithmetic sequences and series", "entities": [(0, 31, "HYPERLINK")]},
    {"text": "Go to geometric sequences and series", "entities": [(6, 36, "HYPERLINK")]},
    {"text": "geometric sequences and series", "entities": [(0, 30, "HYPERLINK")]},
    {"text": "lines", "entities": [(0, 5, "HYPERLINK")]},
    {"text": "more on the augmented matrix", "entities": [(0, 28, "HYPERLINK")]},
    {"text": "pemdas", "entities": [(0, 6, "HYPERLINK")]}


]

# Convert training data to Example objects
examples = []
for item in train_data:
    text = item["text"]
    entities = item["entities"]
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, {"entities": entities})
    examples.append(example)

# Fine-tune the model
nlp.begin_training()
for _ in range(50):  # Increase iterations for better results
    for example in examples:
        nlp.update([example])

# Save the fine-tuned model
nlp.to_disk("fine_tuned_model")
doc = nlp("I want to go to Stationary Points")
print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
# Load the trained model

