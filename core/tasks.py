from celery import shared_task
from .models import Work

@shared_task(bind=True)
def saveworks(self, agents, manager_id):
    for agent in agents:
        try:
            work = Work.objects.get(idcustomer = agent["idcustomer"])
        except Work.DoesNotExist:
            work = Work()
        work.idcustomer = agent["idcustomer"]
        work.c_name = agent["c_name"]
        work.create_date = agent["create_date"]
        work.phone = agent["phone"]
        work.email = agent["email"]
        work.last_order_date = agent["last_order_date"]
        work.manager = agent["manager"]
        work.manager_id = manager_id
        work.save()