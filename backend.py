import torch
import torch.nn as nn
import torch.nn.functional as F 
import pandas as pd
#Initiating Model Class
def predict(my_df):
    class Model(nn.Module):
        #Initiating Layers and Connections
        def __init__(self, in_features=10, h1=8, h2=9, out_features=3):
            super().__init__()
            self.fc1 = nn.Linear(in_features, h1)
            self.fc2 = nn.Linear(h1, h2)
            self.out = nn.Linear(h2, out_features)

        def forward(self, x):
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.out(x)

            return x
    torch.manual_seed(41)
    model = Model()

    numRows = pd.shape[0]-1
    testPercent = (numRows-1)/numRows
    # Check if the dataframe is loaded correctly

    X = my_df.drop('PTS', axis=1)
    y = my_df['PTS']

    my_df.tail()
    X = X.values
    y = y.values

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testPercent, random_state=41)

    X_train = torch.FloatTensor(X_train)
    X_test = torch.FloatTensor(X_test)

    y_train = torch.LongTensor(y_train)
    y_test = torch.LongTensor(y_test)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    epochs = 100
    losses = []
    for i in range(epochs):
        #Pushes training data to get prediciton
        y_pred = model.forward(X_train)
        #Measures Loss
        loss = criterion(y_pred, y_train)
        #Append Loss
        losses.append(loss.detach().numpy())
        #print epoch and loss
        if i % 10 == 0:
            print(f'Epoch: {i} and loss: {loss}')
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    y_eval = model.forward(X_test)
    return y_eval


