from sklearn import tree

# Examples
# Weight Texture Label
# 150g   Bumpy   Orange
# 170g   Bumpy   Orange
# 140g   Smooth  Apple
# 130g   Smooth  Apple

features = [[150, 0], [170, 0], [140, 1], [130, 1]]

labels = [0 , 0, 1, 1]

label_names = ['Orange', 'Apple']

# Train Classifer
clf = tree.DecisionTreeClassifier()  # Decision Tree classifier
clf = clf.fit(features, labels)  # Find patterns in data

# Make Predictions
result = clf.predict([[160, 1], [145, 1]])

[print(label_names[prediction]) for prediction in result]












