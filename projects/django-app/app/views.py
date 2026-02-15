from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse(
        """
        <html>
            <head>
                <title>Django App</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 40px;
                        color: #333;
                    }
                    h1 {
                        color: #2c3e50;
                    }
                    p {
                        font-size: 1.1rem;
                    }
                    code {
                        background: #f4f4f4;
                        padding: 4px 6px;
                        border-radius: 4px;
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to the Django App</h1>
                <p>Your Kubernetes + Traefik + GitOps deployment is running correctly.</p>
                <p>Health endpoint: <code>/health/</code></p>
            </body>
        </html>
        """
    )

def health(request):
    return JsonResponse({"status": "ok"})