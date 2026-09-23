from flask import Flask, render_template_string, jsonify
from datetime import datetime
import random

application = Flask(__name__)

# Cyber-Forensic Dashboard HTML (Tailwind + Dark Ops Theme)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AURA_NETOPS | Cyber-Forensic Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Share Tech Mono', monospace; }
    </style>
</head>
<body class="bg-gray-900 text-green-400 min-h-screen flex flex-col">

    <!-- Header -->
    <header class="bg-black border-b border-green-700 p-4 flex justify-between items-center">
        <h1 class="text-xl font-bold uppercase">AURA_NETOPS</h1>
        <span class="text-sm text-green-300">UTC: {{ current_time }}</span>
    </header>

    <!-- Main Content -->
    <main class="flex-grow p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Network Stats -->
        <div class="bg-gray-800 p-6 rounded shadow-lg space-y-4">
            <h2 class="text-lg font-bold border-b border-green-700 pb-2">NETWORK_STATS</h2>
            <p>Latency: <span class="text-white font-bold">{{ latency }} ms</span></p>
            <p>Packet Loss: <span class="text-white font-bold">{{ packet_loss }} %</span></p>
            <p>Throughput: <span class="text-white font-bold">{{ throughput }} Mbps</span></p>
        </div>

        <!-- Security Alerts -->
        <div class="bg-gray-800 p-6 rounded shadow-lg space-y-4">
            <h2 class="text-lg font-bold border-b border-green-700 pb-2">SECURITY_ALERTS</h2>
            {% if alerts %}
                <ul class="list-disc pl-5 text-red-400">
                    {% for alert in alerts %}
                        <li>{{ alert }}</li>
                    {% endfor %}
                </ul>
            {% else %}
                <p class="text-green-400">No active alerts.</p>
            {% endif %}
        </div>

        <!-- System Info -->
        <div class="bg-gray-800 p-6 rounded shadow-lg space-y-4">
            <h2 class="text-lg font-bold border-b border-green-700 pb-2">SYSTEM_INFO</h2>
            <p>Environment: {{ env_name }}</p>
            <p>AWS Region: {{ aws_region }}</p>
            <p>Status: <span class="text-green-400 font-bold">Operational</span></p>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-black border-t border-green-700 p-4 text-center text-xs text-green-500">
        [AURA_NETOPS] >> Flask v3.x >> Cyber-Forensic Mode
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
    packet_loss = random.uniform(0, 5)
    throughput = random.randint(50, 500)

    # Simulated alerts
    alerts = []
    if random.choice([True, False]):
        alerts.append("Suspicious login attempt detected")
    if random.choice([True, False]):
        alerts.append("Unusual traffic spike on GPON interface")

    return render_template_string(
        HTML_TEMPLATE,
        current_time=now,
        env_name=env_name,
        aws_region=aws_region,
        latency=latency,
        packet_loss=round(packet_loss, 2),
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
