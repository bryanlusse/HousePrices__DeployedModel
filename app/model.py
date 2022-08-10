import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class Net(nn.Module):
    def __init__(self, layers, input_shape, output_shape):
        super(Net, self).__init__()
        self.layers = layers
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.shapes = np.append(np.linspace(input_shape, output_shape,layers, endpoint=False).round(),output_shape).astype(int)
        self.fc_layers = nn.ModuleList()  
        for layer in range(layers):
            self.fc_layers.append(nn.Linear(self.shapes[layer], self.shapes[layer+1]))

    def forward(self, x):
        # Pass data through fully connected layers
        for layer in range(self.layers):
            x = self.fc_layers[layer](x)
            x = F.relu(x)

        output = x
        return output


def build_model(input_size, output_size, layers):
    """
    Build Pytorch model.
    Inputs:
        - input_size - size of the input characteristics
        - output_size - size of the output prediction
        - layers - nr of layers of the model
    Returns:
        - model - Pytorch model
    """
    MODEL_PATH = "best-model-parameters.pt"

    # Initialize model and load weights
    model = Net(layers, input_size, output_size)
    model.load_state_dict(torch.load(MODEL_PATH))
    return model


def prediction(characteristics):
    """
    Predict house price from array of house characteristics
    Input:
        - characteristics - list of house characteristics
    Returns:
        - price - float representing predicted price
    """
    # Check if input has correct size
    if len(characteristics) != 14:
        return 'InputError: Inputs need to consist of 14 characteristics'

    else:
        # Normalize data
        mins = [0.0, 1.0, 53.0, 1500.0, 0.0, 0.0, 2.0, 1.0, 1.0, -1.0, 0.0, 0.0, 15.0]
        maxs = [2448.0, 998.0, 844.0, 2022.0, 106.0, 87.0, 18.0, 7.0, 6.0, 10.0, 455.0, 45.0, 29775.0]

        processed_char = []

        for i, char in enumerate(characteristics):
            if i == 4:
                # This characteristic does not have to be normalized as it has a binary nature
                processed_char.append(char)
            elif i > 4: 
                processed_char.append((char - mins[i-1])/(maxs[i-1] - mins[i-1]))
            else:
                processed_char.append((char - mins[i])/(maxs[i] - mins[i]))
        
        # Load the model
        input_size = 14
        output_size = 1
        layers = 2    
        model = build_model(input_size, output_size, layers)

        input_tensor = torch.tensor(processed_char)
        output = model(input_tensor)
        price = int(np.round(output[0].detach().numpy()*100000.0))

        return price