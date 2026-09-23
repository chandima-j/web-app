from flask import Flask, render_template_string, jsonify
from datetime import datetime
import random
import os

application = Flask(__name__)

# Cyber-Blue Neon Dashboard Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AURA_NETOPS | Blue Neon Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto+Mono&display=swap');
        body {
            font-family: 'Orbitron', sans-serif;
            background: #0a0f1c;
            color: #00e0ff;
        }
        h1, h2 {
            font-family: 'Roboto Mono', monospace;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- Header -->
    <header class="bg-black border-b border-cyan-700 p-4 flex justify-between items-center shadow-lg">
        <h1 class="text-2xl font-bold uppercase tracking-widest">AURA_NETOPS</h1>
        <span class="text-sm text-cyan-300">UTC: {{ current_time }}</span>
    </header>

    <!-- Main Content -->
    <main class="flex-grow p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Network Stats -->
        <div class="bg-[#111827] p-6 rounded-lg shadow-lg space-y-4 border border-cyan-800">
            <h2 class="text-lg font-bold border-b border-cyan-700 pb-2">NETWORK_STATS</h2>
            <p>Latency: <span class="text-white font-bold">{{ latency }} ms</span></p>
            <p>Packet Loss: <span class="text-white font-bold">{{ packet_loss }} %</span></p>
            <p>Throughput: <span class="text-white font-bold">{{ throughput }} Mbps</span></p>
        </div>

        <!-- Security Alerts -->
        <div class="bg-[#111827] p-6 rounded-lg shadow-lg space-y-4 border border-cyan-800">
            <h2 class="text-lg font-bold border-b border-cyan-700 pb-2">SECURITY_ALERTS</h2>
            {% if alerts %}
                <ul class="list-disc pl-5 text-red-400">
                    {% for alert in alerts %}
                        <li>{{ alert }}</li>
                    {% endfor %}
                </ul>
            {% else %}
                <p class="text-cyan-400">No active alerts.</p>
            {% endif %}
        </div>

        <!-- System Info -->
        <div class="bg-[#111827] p-6 rounded-lg shadow-lg space-y-4 border border-cyan-800">
            <h2 class="text-lg font-bold border-b border-cyan-700 pb-2">SYSTEM_INFO</h2>
            <p>Environment: {{ env_name }}</p>
            <p>AWS Region: {{ aws_region }}</p>
            <p>Status: <span class="text-green-400 font-bold">Operational</span></p>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-black border-t border-cyan-700 p-4 text-center text-xs text-cyan-500">
        [AURA_NETOPS] >> Flask v3.x >> Blue Neon Mode
    </footer>

</body>
</html>
"""

@application.route('/')
def dashboard():
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    env_name = os.environ.get('AWS_EB_ENVIRONMENT_NAME', 'LOCAL_DEBUG')
    aws_region = os.environ.get('AWS_REGION', 'us-east-1')

    # Simulated metrics
    latency = random.randint(10, 120)
    packet_loss = round(random.uniform(0, 5), 2)
    throughput = random.randint(50, 500)

    # Simulated alerts
    alerts = []
    if random.choice([True, False]):
        alerts.append("Firewall anomaly detected")
    if random.choice([True, False]):
        alerts.append("Unauthorized SSH attempt logged")

    return render_template_string(
        HTML_TEMPLATE,
        current_time=now,
        env_name=env_name,
        aws_region=aws_region,
        latency=latency,
        packet_loss=packet_loss,
        throughput=throughput,
        alerts=alerts
    )

@application.route('/health')
def health_check():
    return jsonify({
        "status": "operational",
        "latency_ms": random.randint(10, 120),
        "packet_loss_percent": round(random.uniform(0, 5), 2),
        "timestamp_utc": datetime.utcnow().isoformat()
    }), 200

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
