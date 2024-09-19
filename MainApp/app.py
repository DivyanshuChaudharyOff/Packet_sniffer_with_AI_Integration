from flask import Flask, jsonify, request
from scapy.all import sniff
import threading

app = Flask(__name__)

# List to store captured packets
captured_packets = []


# Function to capture packets using Scapy
def packet_sniffer(packet):
    packet_info = {
        "source_ip": packet[0][1].src,
        "destination_ip": packet[0][1].dst,
        "protocol": packet[0][1].proto,
        "payload": str(packet[0][1].payload),
    }
    captured_packets.append(packet_info)


# Background thread to run the packet sniffer
def start_sniffer():
    sniff(prn=packet_sniffer, store=False)


@app.route("/start-sniffing", methods=["POST"])
def start_sniffing():
    sniff_thread = threading.Thread(target=start_sniffer)
    sniff_thread.start()
    return jsonify({"message": "Packet sniffing started!"})


@app.route("/packets", methods=["GET"])
def get_packets():
    return jsonify(captured_packets)


@app.route("/clear-packets", methods=["POST"])
def clear_packets():
    captured_packets.clear()
    return jsonify({"message": "Packet list cleared!"})


if __name__ == "__main__":
    app.run(debug=True)
