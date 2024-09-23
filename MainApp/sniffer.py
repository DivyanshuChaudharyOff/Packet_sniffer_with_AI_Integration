import scapy.all as scapy
import requests
import json
import os

# Function to capture packets
def capture_packets(interface="eth0"):
    print(f"Capturing packets on {interface}...")
    packets = scapy.sniff(iface=interface, count=5)  # Capture 5 packets for demo purposes
    return [packet.summary() for packet in packets]

# Function to send packet data to LLM (AI model)
def send_to_llm(packet_data):
    LLM_API_URL = "https://api.openai.com/v1/engines/davinci/completions"
    API_KEY = os.getenv('OPENAI_API_KEY')  # Fetch API key from environment variable

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        "prompt": f"Analyze this packet data for network anomalies: {packet_data}",
        "max_tokens": 100
    }

    response = requests.post(LLM_API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        return f"Error: {response.status_code}"
