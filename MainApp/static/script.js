<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Packet Sniffer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .button {
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Network Packet Sniffer</h1>
    <button class="button" onclick="startSniffing()">Start Sniffing</button>
    <button class="button" onclick="clearPackets()">Clear Packets</button>

    <h2>Captured Packets:</h2>
    <table>
        <thead>
            <tr>
                <th>Source IP</th>
                <th>Destination IP</th>
                <th>Protocol</th>
                <th>Payload</th>
            </tr>
        </thead>
        <tbody id="packetTable">
        </tbody>
    </table>

    <script>
        function startSniffing() {
            fetch('/start-sniffing', { method: 'POST' })
                .then(response => response.json())
                .then(data => alert(data.message))
                .catch(error => console.error('Error:', error));
        }

        function clearPackets() {
            fetch('/clear-packets', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('packetTable').innerHTML = '';
                    alert(data.message);
                })
                .catch(error => console.error('Error:', error));
        }

        function fetchPackets() {
            fetch('/packets')
                .then(response => response.json())
                .then(data => {
                    const packetTable = document.getElementById('packetTable');
                    packetTable.innerHTML = '';
                    data.forEach(packet => {
                        const row = document.createElement('tr');
                        row.innerHTML = `<td>${packet.source_ip}</td>
                                         <td>${packet.destination_ip}</td>
                                         <td>${packet.protocol}</td>
                                         <td>${packet.payload}</td>`;
                        packetTable.appendChild(row);
                    });
                })
                .catch(error => console.error('Error:', error));
        }

        // Fetch packets every 5 seconds
        setInterval(fetchPackets, 5000);
    </script>
</body>
</html>
