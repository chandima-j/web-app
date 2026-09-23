from flask import Flask, render_template_string, jsonify
from datetime import datetime
import random
import os

application = Flask(__name__)

# Minimalist Productivity Hub Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AURA_FOCUS | Daily Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Fira+Code&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background: #f9fafb;
            color: #374151;
        }
        h1, h2 {
            font-family: 'Fira Code', monospace;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- Header -->
    <header class="bg-white border-b border-gray-300 p-4 flex justify-between items-center shadow-sm">
        <h1 class="text-xl font-bold uppercase tracking-widest text-indigo-600">AURA_FOCUS</h1>
        <span class="text-sm text-gray-500">UTC: {{ current_time }}</span>
    </header>

    <!-- Main Content -->
    <main class="flex-grow p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Task List -->
        <div class="bg-white p-6 rounded-lg shadow-md space-y-4">
            <h2 class="text-lg font-bold border-b border-gray-200 pb-2 text-indigo-700">TASKS_TODAY</h2>
            <ul class="list-disc pl-5 space-y-2">
                {% for task in tasks %}
                    <li>{{ task }}</li>
                {% endfor %}
            </ul>
        </div>

        <!-- Inspiration -->
        <div class="bg-white p-6 rounded-lg shadow-md space-y-4">
            <h2 class="text-lg font-bold border-b border-gray-200 pb-2 text-indigo-700">INSPIRATION</h2>
            <blockquote class="italic text-gray-600">“{{ quote }}”</blockquote>
        </div>

        <!-- System Info -->
        <div class="bg-white p-6 rounded-lg shadow-md space-y-4">
            <h2 class="text-lg font-bold border-b border-gray-200 pb-2 text-indigo-700">SYSTEM_INFO</h2>
            <p>Environment: {{ env_name }}</p>
            <p>AWS Region: {{ aws_region }}</p>
            <p>Status: <span class="text-green-600 font-bold">Stable</span></p>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-300 p-4 text-center text-xs text-gray-500">
        [AURA_FOCUS] >> Flask v3.x >> Productivity Mode
    </footer>

</body>
</html>
"""

@application.route('/')
def dashboard():
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    env_name = os.environ.get('AWS_EB_ENVIRONMENT_NAME', 'LOCAL_DEBUG')
    aws_region = os.environ.get('AWS_REGION', 'us-east-1')

    # Simulated tasks
    tasks = [
        "Review GPON OLT configs",
        "Write forensic case notes",
        "Update Python automation scripts",
        "Plan microservices prototype"
    ]

    # Random inspirational quotes
    quotes = [
        "Focus on progress, not perfection.",
        "Small steps every day build big results.",
        "Discipline is the bridge between goals and success.",
        "Your future is created by what you do today."
    ]
    quote = random.choice(quotes)

    return render_template_string(
        HTML_TEMPLATE,
        current_time=now,
        env_name=env_name,
        aws_region=aws_region,
        tasks=tasks,
        quote=quote
    )

@application.route('/health')
def health_check():
    return jsonify({
        "status": "stable",
        "tasks_remaining": random.randint(0, 5),
        "timestamp_utc": datetime.utcnow().isoformat()
    }), 200

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
