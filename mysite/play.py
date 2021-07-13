import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from polls.models import Choice, Question  # Import the model classes we just wrote.
from django.utils import timezone

q = Question(question_text="What's new?", pub_date=timezone.now())

q.save()

print(q.id)
print(q.question_text)
print(q.pub_date)
