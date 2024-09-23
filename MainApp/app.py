from flask import Flask, render_template, jsonify
from sniffer import capture_and_analyze_packets
from geolocation import get_geolocation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture')
def capture():
    # Capture and analyze packets
    packets = capture_and_analyze_packets()

    # You can modify this to send the packet, geolocation, and LLM analysis to the front-end
    packet_data = []  # This will hold the data structure for all packet captures

    for packet in packets:
        src_ip = packet['src_ip']
        dst_ip = packet['dst_ip']
        src_geo = get_geolocation(src_ip)
        dst_geo = get_geolocation(dst_ip)
        llm_result = packet['llm_analysis']

        packet_data.append({
            "src_ip": src_ip,
            "src_geo": src_geo,
            "dst_ip": dst_ip,
            "dst_geo": dst_geo,
            "llm_result": llm_result
        })

    return jsonify(packet_data)

if __name__ == "__main__":
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)
