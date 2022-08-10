import json

from model import prediction

def lambda_handler(event, context):
    """
    Function to predict house price and return prediction

    Input: 
        - event - JSON request containing list of house characteristics
    Returns:
        - JSON containing price prediction
    """
    input_data = event['characteristics']

    price = prediction(input_data)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
                'prediction': price, 
        })
    }