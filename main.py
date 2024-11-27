import subprocess


def run_django_server():
    # This will execute the command 'python manage.py runserver'
    subprocess.run(["python3", "WebApp/SoulGuard/manage.py", "runserver"])


if __name__ == "__main__":
    run_django_server()
