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





# Fake file directory structure
fake_file_directory = {
    "home": {
        "user": {
            "documents": ["resume.docx", "secret_plans.pdf"],
            "downloads": ["ssh_config.txt", "hacktool.exe"],
        },
        "admin": {
            "logs": ["system_log.txt", "firewall_log.txt"],
            "scripts": ["backup.sh", "start_server.py"],
        }
    }
}

# Function to simulate an attacker accessing the fake file system
def browse_fake_file_system(path):
    parts = path.strip('/').split('/')
    location = fake_file_directory
    for part in parts:
        if part in location:
            location = location[part]
        else:
            return "Directory not found."
    return location if isinstance(location, dict) else ', '.join(location)

# Example usage
fake_file = browse_fake_file_system('/home/user/documents')
print(fake_file)  # Will print: resume.docx, secret_plans.pdf

from geolocation import log_geolocation

# Function to capture and analyze packets
def capture_and_analyze_packets(interface="eth0"):
    packets = capture_packets(interface)
    for packet in packets:
        packet_data = packet.summary()
        
        # Extract IP address from packet (assuming it's an IP packet)
        src_ip = packet[scapy.IP].src if packet.haslayer(scapy.IP) else "Unknown"
        dst_ip = packet[scapy.IP].dst if packet.haslayer(scapy.IP) else "Unknown"
        
        # Log geolocation info
        src_geo = log_geolocation(src_ip)
        dst_geo = log_geolocation(dst_ip)
        
        # Send to LLM for analysis
        llm_result = handle_analysis_and_alert(packet_data)
        
        print(f"Source IP: {src_ip} -> Geolocation: {src_geo}")
        print(f"Destination IP: {dst_ip} -> Geolocation: {dst_geo}")
        print(f"LLM Analysis: {llm_result}")
