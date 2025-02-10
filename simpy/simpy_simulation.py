import simpy
import random

RANDOM_SEED = 42
ARRIVAL_RATE = 2  # Taux d'arrivée (lambda)
SERVICE_RATE = 3  # Taux de service (mu)
SIM_TIME = 10  # Durée de simulation (s)

class MM1Queue:
    def __init__(self, env):
        self.env = env
        self.server = simpy.Resource(env, capacity=1)
    
    def process_request(self, request_id):
        service_time = random.expovariate(SERVICE_RATE)
        print(f"{self.env.now:.2f}: Requête {request_id} en service ({service_time:.2f}s)...")
        yield self.env.timeout(service_time)
        print(f"{self.env.now:.2f}: Requête {request_id} terminée.")

def generate_requests(env, queue):
    request_id = 0
    while True:
        yield env.timeout(random.expovariate(ARRIVAL_RATE))
        request_id += 1
        print(f"{env.now:.2f}: Requête {request_id} arrive.")
        env.process(queue.process_request(request_id))

env = simpy.Environment()
queue = MM1Queue(env)
env.process(generate_requests(env, queue))

print("⏳ Démarrage de la simulation...")
env.run(until=SIM_TIME)
print("✅ Simulation terminée.")
