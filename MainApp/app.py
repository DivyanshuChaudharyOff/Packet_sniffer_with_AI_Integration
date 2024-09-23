import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from sniffer import capture_packets, send_to_llm

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Main route to render the dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Route to capture packets and send data to LLM
@app.route('/analyze_packets', methods=['GET'])
def analyze_packets():
    # Capture packets
    packets = capture_packets(interface="eth0")  # Replace with actual network interface
    packet_summary = ' '.join(packets)  # Create a string summary of captured packets

    # Send packet summary to LLM for analysis
    llm_result = send_to_llm(packet_summary)

    # Return the result to be rendered on the front end
    return jsonify({'llm_result': llm_result})

if __name__ == '__main__':
    app.run(debug=True)
