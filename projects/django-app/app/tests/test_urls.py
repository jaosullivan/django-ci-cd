from django.urls import reverse, resolve

def test_health_url_resolves():
    resolver = resolve("/health/")
    assert resolver.view_name == "health"