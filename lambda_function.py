import random
import time

def generate_metrics():
    appliances = {
        'refrigerator': random.uniform(350, 780),
        'washing_machine': random.choice([0, random.uniform(400, 1400)]),
        'air_conditioner': random.uniform(1000, 1500),
        'tv': random.uniform(50, 200) if random.random() < 0.3 else 0
    }
    
    metrics = []
    for appliance, power in appliances.items():
        metrics.append(f'appliance_power_consumption{{appliance="{appliance}"}} {power}')
    return "\n".join(metrics)

def lambda_handler(event, context):
    metrics = generate_metrics()
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": metrics
    }
