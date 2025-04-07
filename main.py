import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard 

def main():
    active_passcards = Passcard.objects.filter(is_active=True)

    
    total_passcards = Passcard.objects.count() 

    
    total_active_passcards = len(active_passcards)  

    
    print(f"Всего пропусков: {total_passcards}")
    print(f"Активных пропусков: {total_active_passcards}")

if __name__ == '__main__':
    main()